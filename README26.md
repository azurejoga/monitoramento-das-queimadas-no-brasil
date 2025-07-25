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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63c9f900-8aa2-3149-b31f-5c072337a282 | -20.68286 | -46.31216 | 2025-07-25 04:49:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e229b23-fec9-39a3-b595-375c5da452cf | -17.3471 | -45.70993 | 2025-07-25 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45070393-e61e-3991-9265-d5470dd0ef14 | -18.42229 | -54.55952 | 2025-07-25 04:49:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf6341eb-17b8-371d-8249-aa1c10669906 | -18.22643 | -54.5522 | 2025-07-25 04:49:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6251abe-600c-37a7-9883-aca62c9012c5 | -16.5118 | -50.85151 | 2025-07-25 04:49:00 | NOAA-20 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aeda63f5-fd5f-3d55-9680-f2958b87720e | -16.82093 | -47.60122 | 2025-07-25 04:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63d69477-a3f9-3cdf-8cf4-73f3467729f8 | -17.70285 | -44.30735 | 2025-07-25 04:49:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2229f407-8efa-3ef8-a6ea-da87c322aa5c | -20.26826 | -49.18306 | 2025-07-25 04:49:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5ac78a7-7cb3-3cf0-bf93-03a5793ca413 | -20.26781 | -49.18673 | 2025-07-25 04:49:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dac2bb2c-f29c-3fd3-a29c-0aa1bc3f9da3 | -18.41839 | -54.56259 | 2025-07-25 04:49:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1534b491-5878-3174-a1f0-af961b3bba0f | -17.34224 | -45.70941 | 2025-07-25 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab4dced5-1f65-37db-a91f-55e0e38f8e85 | -21.47085 | -44.96459 | 2025-07-25 04:49:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 77850aa5-6d3d-3330-b961-7b4523d0ca08 | -17.34291 | -45.70389 | 2025-07-25 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b7d0194-3f43-30af-aba6-7abcb55ca72d | -20.68342 | -46.30687 | 2025-07-25 04:49:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a51bf8a4-dd8d-375f-8124-574e29013778 | -17.70247 | -44.31075 | 2025-07-25 04:49:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 55432518-f3be-3f7a-9cd2-a8dc83f3c90b | -18.85055 | -41.99504 | 2025-07-25 04:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d887a8bf-40e9-38b5-8f57-c34f9cde9a64 | -20.22415 | -50.91647 | 2025-07-25 04:49:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 92c0210c-e4b2-360d-9581-a3f477328ebf | -16.60544 | -47.96763 | 2025-07-25 04:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52ad7c93-ea56-3fa5-872a-20c9a27169fb | -18.97125 | -54.37734 | 2025-07-25 04:49:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc43bb93-452f-3f60-b40a-bdabb717f4b6 | -20.68071 | -46.30577 | 2025-07-25 04:49:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bd8b9f4f-0c86-3d64-b177-30fac2015b12 | -16.50829 | -50.85098 | 2025-07-25 04:49:00 | NOAA-20 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8fb0aa8b-5c7d-3333-a856-22c8efb6b9bd | -21.46803 | -44.96473 | 2025-07-25 04:49:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df1e7267-9143-330a-848d-419cde9995b2 | -18.0886 | -54.28906 | 2025-07-25 04:49:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba1af7d6-e62b-3e49-b447-0c6d9b2617db | -16.56288 | -49.05694 | 2025-07-25 04:49:00 | NOAA-20 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4243f0ab-4544-370d-9b59-5c3e614e0de2 | -18.22702 | -54.54855 | 2025-07-25 04:49:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0a5a3ba-130f-36d1-a70c-00e4f9969a94 | -19.16412 | -46.58892 | 2025-07-25 04:49:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24c2b8a2-0f7c-3b57-83b8-cfd857fdf351 | -19.7538 | -54.00284 | 2025-07-25 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9ff3e35-d7d7-3f75-b3d8-b3a184697dfb | -18.41897 | -54.55894 | 2025-07-25 04:49:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d997314e-4bf7-3fac-8890-e7f755658cfe | -16.38615 | -49.92559 | 2025-07-25 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba7d8d1b-33d1-3eac-9a18-37f8db2bb41d | -7.2597 | -43.0645 | 2025-07-25 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 939acf8c-e953-3114-9681-67ba07c00573 | -8.9064 | -45.5706 | 2025-07-25 04:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 9da8a347-c9e4-3f70-b5ed-47b268d4f0ea | -11.4584 | -45.1126 | 2025-07-25 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 11fc9318-f396-3338-8ab8-1544c1f01125 | -22.39867 | -49.79862 | 2025-07-25 04:51:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 59fa4970-28f3-37d8-b763-4de9c67bcac2 | -23.08175 | -54.25166 | 2025-07-25 04:51:00 | NOAA-20 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eed34e20-ffab-3afc-9554-7b299a4adb7a | -21.60763 | -57.57282 | 2025-07-25 04:51:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7fe5b10-c15f-3425-afad-90b785215eec | -21.61114 | -57.57355 | 2025-07-25 04:51:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cde8331-f4cf-3f1f-b96b-38a6abad0fb0 | -21.30894 | -56.11781 | 2025-07-25 04:51:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60a33165-6386-30c5-8f4a-48dee485e179 | -22.21583 | -56.19396 | 2025-07-25 04:51:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0432486-65bb-394e-b30a-d32961456884 | -21.43959 | -54.57705 | 2025-07-25 04:51:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5a4c39a-43b8-3673-a92c-473994474a42 | -21.5946 | -57.60535 | 2025-07-25 04:51:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b09d27e-65a6-32a1-869f-721d6de205e7 | -11.4584 | -45.1126 | 2025-07-25 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| a2abe2cd-070f-309f-9c7b-e3b7efce04ab | -11.4584 | -45.1126 | 2025-07-25 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 57f0d5c5-638b-3c98-bc44-d71ebc005d74 | -11.4584 | -45.1126 | 2025-07-25 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 8e559204-f5eb-3457-b7d8-d2bf2574bafe | -11.4584 | -45.1126 | 2025-07-25 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 0a44c2d2-1bf8-3c91-89d1-7fba4a252cb5 | -6.9816 | -43.31829 | 2025-07-25 05:33:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| ddc3410b-98ac-3c17-82f8-a9ffc8d736f6 | -2.90249 | -48.23484 | 2025-07-25 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| a635786d-aba7-3876-85b7-328ff0745de5 | -2.89943 | -48.25401 | 2025-07-25 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 5261a234-e352-3739-8b52-69e772543768 | -7.24445 | -43.05204 | 2025-07-25 05:33:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 13b43372-79ab-39da-90e4-2ab4ecc1306d | -6.95112 | -44.55519 | 2025-07-25 05:33:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 0231a9b3-3f32-39f9-abd1-6891c7ff98e9 | -3.05193 | -47.37318 | 2025-07-25 05:33:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| df2e7783-99da-369e-b4b3-0b563c7365c4 | -7.2607 | -43.06346 | 2025-07-25 05:33:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| e8ec879a-4c0b-340b-a822-7d95f1d0e24e | -7.25191 | -43.06215 | 2025-07-25 05:33:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 37.8 |
| 7cce0f37-c981-361c-b04b-87b5cc1d166d | -6.6716 | -43.96496 | 2025-07-25 05:33:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| afb1ab3a-42ee-309d-b702-3c5e112b31ab | -7.25938 | -43.07225 | 2025-07-25 05:33:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5f1b9842-258e-34e1-b9b1-c3ead96787b9 | -7.24312 | -43.06084 | 2025-07-25 05:33:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 905cc53b-af6d-36d0-9e8e-5c5b6f7dd99d | -3.30958 | -51.66347 | 2025-07-25 05:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d5f9f0b-27a3-36da-8cb6-7d2ca73f0c83 | -6.94967 | -44.56467 | 2025-07-25 05:33:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4c4e340a-bf9d-3393-8077-07f17f739616 | -3.04347 | -47.38161 | 2025-07-25 05:33:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 896886a2-be32-3f2e-a2af-7d65dd78941c | -2.91513 | -48.23663 | 2025-07-25 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 332e3055-5a14-3c39-a361-0ef268f4ed34 | -4.35473 | -47.67668 | 2025-07-25 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| e55feb99-6e46-3920-8429-ece8634eafd1 | -4.35218 | -47.69311 | 2025-07-25 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| dc828ca1-affa-3157-8a37-ae91ea96d5bf | -2.90014 | -48.24662 | 2025-07-25 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 4f3d55c9-05df-398b-930d-e479c8c73ba4 | -8.3683 | -51.0787 | 2025-07-25 05:36:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a692019b-5fb9-357c-85b4-f9636f535960 | -8.89871 | -45.58104 | 2025-07-25 05:36:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 184574d7-1efb-3169-83b7-83efed914c71 | -8.50845 | -43.30915 | 2025-07-25 05:36:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 4624eccc-366f-37e3-8e9e-d5e095a36cb9 | -6.78336 | -61.96541 | 2025-07-25 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a2a95ec-6200-32f9-8fe1-41122c11a91a | -7.03995 | -55.50135 | 2025-07-25 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c5c93bd-65a9-3c50-9c37-b4e8976b71de | -8.08861 | -43.15195 | 2025-07-25 05:36:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| f3e97666-17a5-3eb5-9db7-fc3084a26add | -7.91153 | -44.08076 | 2025-07-25 05:36:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 4e9c6b34-d574-3b5a-87f3-d82ef4f7165f | -7.77336 | -44.55341 | 2025-07-25 05:36:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e5151e11-0e29-3da4-b75c-c4cb52c50376 | -7.49515 | -63.81738 | 2025-07-25 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 196e0abf-bc9b-327d-8e85-949478646d9a | -7.49461 | -63.82084 | 2025-07-25 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3272f80e-cb9d-33d5-ae12-e7cbd272626a | -3.75893 | -52.66671 | 2025-07-25 05:36:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3621727-5d26-34d5-bc2c-7e806ab3ba68 | -8.11997 | -50.46061 | 2025-07-25 05:36:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59c521b1-8634-3d0d-92b1-51534fc88c58 | -8.1299 | -50.46843 | 2025-07-25 05:36:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 61394777-24b2-3b9b-a95e-cc9013f34681 | -8.07103 | -43.14933 | 2025-07-25 05:36:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| c0efa953-55af-362b-9f49-447c179ad7c2 | -7.27349 | -60.17726 | 2025-07-25 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83ba9341-0cbe-3af8-a1ee-b679d4607ac1 | -10.6164 | -44.76525 | 2025-07-25 05:36:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 90b19892-6438-3b3b-b140-7a974d678b78 | -7.91905 | -44.09114 | 2025-07-25 05:36:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| c275361b-30e8-3e09-81e6-08f999121252 | -7.03766 | -55.50097 | 2025-07-25 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4e0b9d5-fda1-3efd-9a32-142a48a2d21b | -8.12619 | -50.46914 | 2025-07-25 05:36:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46eb0fc6-794a-32eb-a58a-7fecbe0ed620 | -10.6074 | -45.23825 | 2025-07-25 05:36:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| f6db6d36-b16c-3fb2-91c3-367f8540eb3f | -7.98683 | -43.82535 | 2025-07-25 05:36:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 0f7c061d-0687-3c90-9c4b-7a4b77cc25c7 | -7.92795 | -44.09251 | 2025-07-25 05:36:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 33b26085-710c-3877-9537-878afbab535c | -8.89711 | -45.59124 | 2025-07-25 05:36:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b9628b84-abea-30f4-a411-121058dc9c40 | -8.07982 | -43.15064 | 2025-07-25 05:36:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 27aebea1-8bee-3e07-beaa-0af7e3e21492 | -8.28726 | -45.0003 | 2025-07-25 05:36:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 239fcb49-8517-3cc4-af64-8c94895736b6 | -7.81979 | -61.33033 | 2025-07-25 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5a2d39a-02f9-3321-b71a-f71c3e7b3516 | -7.77483 | -44.54387 | 2025-07-25 05:36:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 68489773-2cd8-3f45-8395-fc8d96797323 | -8.12279 | -50.46737 | 2025-07-25 05:36:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8aa3a8ee-ec5d-3187-900d-702aefc29c1a | -7.92043 | -44.0821 | 2025-07-25 05:36:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1000e9cf-009d-315f-b55f-3f0cf72e031f | -10.63566 | -44.75884 | 2025-07-25 05:36:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 74dfc38d-3966-316d-9b88-41f5f639c356 | -6.63344 | -56.29202 | 2025-07-25 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbcb2201-1adb-3f44-8bf0-1aaa4250a901 | -7.90263 | -44.07938 | 2025-07-25 05:36:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2b0cf638-9792-3b28-815b-5ad3011576db | -8.50712 | -43.31797 | 2025-07-25 05:36:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 883cb628-5286-3125-b313-0f08b51178ad | -7.91014 | -44.0898 | 2025-07-25 05:36:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d9b80fb3-3f54-3af9-9add-fa28483857db | -7.81624 | -61.32978 | 2025-07-25 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e68c490e-e3d6-3f8a-90a2-9257cc650738 | -9.97013 | -64.95297 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd833d19-43c2-3b61-954f-f5f0e3cb2cf2 | -11.67964 | -58.48623 | 2025-07-25 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce0c0fd7-82a9-3c33-a783-c119c1673d05 | -13.71021 | -45.68007 | 2025-07-25 05:38:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |


[Clique aqui para ver as próximas entradas](README27.md)
