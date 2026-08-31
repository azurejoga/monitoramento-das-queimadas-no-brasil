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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ea2c84d-a446-3ee0-ae74-d30d4c18ef20 | -10.1578 | -45.76405 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b959892e-8c70-3aab-9bc7-92996c2cb427 | -10.15081 | -45.68841 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| dedcf197-e895-326a-a4ec-c9700893ef46 | -10.70139 | -48.21842 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 53cb56db-8163-36ac-8623-187416c4020f | -13.27446 | -51.60896 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f3e4eec8-111e-3ff9-89f8-c30ce379bcdb | -12.07033 | -44.99105 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f0d12af0-62db-328a-9d79-ef47204b5d71 | -13.19259 | -44.07287 | 2026-08-31 16:30:00 | NPP-375 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f54a1c7-20f8-30fd-b070-a43c16585165 | -11.79484 | -44.88462 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| acb56f16-55a7-3761-985c-4f27691dd0b1 | -11.01957 | -49.69707 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 276d8bb6-4dad-3c16-a125-d10cf86ec2f2 | -11.67897 | -44.87193 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a1761853-d5ab-3d6a-aebe-c8f1ea1b0aca | -11.24598 | -54.0132 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| d1d1a7ea-d7c5-34f0-b8c1-ce31f55c4009 | -12.09722 | -47.16019 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 10f3d45d-62a1-3955-b356-179afce1cc30 | -14.58427 | -53.58483 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 943b29b3-d8ca-390e-bc57-bdf3f113c759 | -14.47673 | -49.03843 | 2026-08-31 16:30:00 | NPP-375 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d60385e6-4485-3545-a6a1-44bd525e50a5 | -8.85577 | -47.07804 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| dbf8e7fe-dc47-3dcf-9b5c-50ede30a4a27 | -10.50393 | -45.04435 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ba5c4319-b224-3de4-95d4-914e84d77e0f | -11.63746 | -49.41214 | 2026-08-31 16:30:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| dbf93139-1e30-3c7d-9c6f-099b714f5d12 | -9.20811 | -51.56302 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 662071f9-c611-39b0-a985-2cdcf972700d | -10.11156 | -50.2876 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6dafc177-4eca-3c98-b138-db51d1a108df | -9.6861 | -47.93867 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 8140e994-d3df-36cd-b0a4-61277fbfbabe | -14.23164 | -43.83086 | 2026-08-31 16:30:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 895d7d2f-1187-3788-9050-14d9cd18c61b | -14.21441 | -48.64748 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d5560aa7-07f7-34ae-97dd-8531d133084e | -10.56361 | -50.36815 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 89f008ca-8589-33ac-bd31-c113a615b932 | -11.2133 | -45.3407 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 91785cbb-25f9-36c8-bd22-16bd3d0468b4 | -10.65866 | -46.25938 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 94548bb4-ed5c-37ce-bc50-8e34ee289b58 | -11.08655 | -51.54239 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1d877137-03fe-3976-b1c8-7c3edbe79c9e | -10.74341 | -54.04827 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| a9554fb0-5608-333e-85b1-8b484a3114e1 | -11.04292 | -49.68255 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5f5b664e-ebd8-3e93-999c-ab5ca0bc7318 | -15.24011 | -53.88105 | 2026-08-31 16:30:00 | NPP-375 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e19b12ea-bbc1-3f58-9fae-98cec2097bf3 | -11.93138 | -45.06807 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| dc49a58f-1373-3c6b-8a35-fdaf9d33fc8a | -9.59762 | -47.60813 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 30198a83-1a7f-33b2-99af-113b62385ecd | -11.57987 | -47.71294 | 2026-08-31 16:30:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2f5ed90a-b996-3489-a8d0-f0782468aa0f | -11.24591 | -45.14 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 51b88791-d1a0-3f33-8ea1-d1b87e1e6f25 | -9.66549 | -50.86393 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| bf587692-21c1-377e-a9de-f13434611fc7 | -11.08045 | -47.15406 | 2026-08-31 16:30:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 964d7c0c-65a7-3388-8e86-a96be2d1be9e | -11.2317 | -45.14645 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 8fc36904-df13-3301-bf72-2ab0d1cf03eb | -15.01589 | -52.7583 | 2026-08-31 16:30:00 | NPP-375 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| ea8230d1-4d8c-362e-9ccb-66f13dc9bba7 | -8.85124 | -47.0751 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 256520d3-9051-33a0-bf66-f8c4a3041e43 | -14.66561 | -53.55899 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 704881e0-88d7-30bb-8fd2-d2044c13352b | -12.09927 | -47.14366 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| daac4b00-2608-3f62-83e0-4a924531c3f5 | -11.04217 | -49.6769 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 57c4bb54-4ae3-34f1-a15e-7d1bf1f9df0d | -11.91734 | -45.0834 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b9af86a9-8682-38e1-84d1-5dfbc42ba1e2 | -9.29788 | -45.3911 | 2026-08-31 16:30:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f6cd6736-99bf-38a7-a566-e1f207d86c48 | -8.75263 | -46.47311 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| d0da4641-da48-3c8b-adc2-8893af9298c6 | -15.26878 | -53.89147 | 2026-08-31 16:30:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 88ec5190-b2b1-3600-953d-17172d2286a8 | -9.05376 | -36.81298 | 2026-08-31 16:30:00 | NPP-375 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 12a5a378-cf98-3d53-9c5c-e94f68832d18 | -8.77063 | -46.4526 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 067f1881-70ae-3857-9289-e9b0a94d2ed5 | -13.06094 | -45.18079 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6778d412-ce77-39c1-967c-4e8388b08124 | -10.0846 | -46.61956 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| de45fb97-7b04-3c6a-ae5a-563e4705cda5 | -9.96825 | -46.30674 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 80d7382a-9eae-3b6b-b6fb-1d3349038588 | -11.06884 | -51.51448 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| be2e9684-7fea-32fc-9ce1-8bc47ed8efae | -12.09157 | -47.15442 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 631482b6-4686-3c4d-a2a4-6d2590542ea9 | -12.08232 | -47.14601 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 555921df-7eb3-3a90-a7f7-a31bd229da48 | -9.20605 | -47.99765 | 2026-08-31 16:30:00 | NPP-375 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bac35822-6f77-36d6-8335-518646b6ff0f | -10.6633 | -46.26392 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9631b7ac-6165-36ff-8479-0547af5d223a | -9.87499 | -46.12519 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| d6e08904-9c18-39ac-8403-f3762edaacfe | -11.1572 | -45.04519 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 6533eb54-34eb-38ce-a1e7-332ce333422e | -11.73844 | -47.62963 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 349cd0af-bd1a-38ed-aa62-48e1c139144f | -10.85588 | -45.37171 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b6adba50-9c74-32b2-a713-c09e6445841d | -13.41329 | -51.38682 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b2a6ecae-8597-3ea1-a108-6ea69f074b3f | -10.12847 | -50.29766 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2b7a2931-9d85-3906-a2ae-4d575acb98f3 | -8.91953 | -44.16763 | 2026-08-31 16:30:00 | NPP-375 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 4307b47a-dff0-31f3-a19d-c7a2fbce70d8 | -9.70253 | -48.15678 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 447fcec0-4b7e-33ac-8541-ed66962e857c | -12.89652 | -45.84227 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 47a35adf-6784-3998-9c5f-ce083861e03c | -9.6585 | -50.8515 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 99bc1b0d-31c0-3293-a78f-cebd1bec471f | -14.66259 | -53.559 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 01dd83c3-fad0-3cce-aa32-8a2e8b1c3682 | -11.54323 | -45.4748 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6f88bcb7-b55f-3934-b682-1e077d2720ae | -8.63342 | -47.467 | 2026-08-31 16:30:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a8c86ee8-9603-3f59-8c0b-bbc6eb07cc7c | -12.0969 | -44.99139 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 45254fc4-d709-30cc-ba14-e67e93eea3ea | -9.83116 | -46.34979 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| cb9722d4-e947-369a-95a1-0ed35d0bf7d4 | -10.34474 | -49.97444 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7d00880d-6377-3314-b743-48eee9d513b6 | -11.22523 | -45.37158 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8519dccc-a6df-30ed-9248-b02668eedb77 | -9.83183 | -46.35472 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1b04cc48-0d69-3fdb-bab1-0dc46898b479 | -12.95243 | -45.92845 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 595bfae0-5355-3060-8e0d-94a79a00d2d6 | -8.86865 | -47.07588 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 4b148411-2eb5-32bf-9e9d-e5069cb02bd2 | -10.8528 | -45.37685 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 741b6194-c01b-3057-9713-ee900bf55119 | -14.44883 | -52.5162 | 2026-08-31 16:30:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 00f6eb10-c95f-3e00-a03b-ec15b95effe6 | -11.21558 | -45.08589 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0deb94c7-35da-390c-b717-26dac9d78622 | -11.24555 | -51.24422 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 698bc930-d902-31fa-b70f-8eb685e03d9b | -10.0825 | -46.61835 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2e6469f8-8e14-3d53-8565-9d897fdb0c66 | -11.08516 | -51.53098 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 58e37d71-8f5b-3080-b109-91892e160401 | -8.75578 | -46.46755 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| a669dfaa-fc8b-31f7-8dab-467344a72899 | -10.14639 | -45.6844 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e0b0d9fa-fc89-3296-97c9-2271a8056d38 | -8.76001 | -46.44218 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 934477de-9853-30fd-b8ca-1a385a5b43c4 | -9.67536 | -47.95677 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 744dc4f3-102b-3e4e-87d2-828eaf9f9efc | -10.92109 | -50.62061 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 33e45f97-8c1c-3d75-ba62-cbcc5a83683d | -8.86941 | -47.08705 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8c9d1fd4-f452-360c-adfd-743e28f7e8d1 | -10.74435 | -54.03943 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9b424698-dd98-3c8f-9d5a-c68f94d510e7 | -10.45562 | -46.54742 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1356b11d-007e-31b4-84ac-01231d84e8bd | -14.26133 | -54.65491 | 2026-08-31 16:30:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| fd075440-15cd-3eda-89ce-89664d5c8aa7 | -10.10096 | -50.28592 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8b67191c-7cb4-3476-8af8-a9edc4993b1f | -11.32536 | -45.18438 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 0fb77671-d9d8-3c59-8040-009962eafe9a | -11.21517 | -45.32663 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 368d21a1-7d7b-3721-8b09-cb99080e5a7d | -13.27417 | -51.60415 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6464f5a5-5fe3-3443-8bf9-f53a2c639c0e | -9.59921 | -47.61992 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 57b3808a-22f3-3b43-8ff4-012fdaa5627f | -11.71745 | -47.64482 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 93c9583a-0b95-30a2-acfd-2b8e99645a90 | -8.93131 | -45.03899 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 4496c943-59aa-3786-8417-842cd4c8d841 | -10.75188 | -54.064 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 52273ca0-84d0-35a6-bd19-960c1588f8cd | -13.68083 | -46.62664 | 2026-08-31 16:30:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0aefdcb8-795c-3d2c-bb10-33b381c2362d | -8.86787 | -47.07644 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a38e0aa3-688f-367f-bd3a-88f7cdd02a1c | -10.09979 | -50.27691 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README115.md)
