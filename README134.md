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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 098b0c71-8bf7-3c6b-887f-2c3d101a7dfe | -13.95704 | -48.1068 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5ead363-eb5b-3139-b7e3-87f6dd0c25a9 | -9.79804 | -45.95101 | 2025-10-02 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23bef227-e436-3eeb-ba5a-fc96ec353347 | -11.06432 | -47.81087 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64bfd199-c3fe-3bc0-9da0-c93f3915613f | -12.765 | -50.55331 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95d93528-102e-3ad8-85cd-9d0babb473d8 | -13.30015 | -47.19616 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7e1b424-3abd-32d5-b80d-3bdc6128730b | -13.95378 | -48.13076 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6fc4242c-5f44-3ace-bab2-71811322516e | -14.6599 | -48.1186 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2841a1e8-3b51-3fe7-963f-f452ace7e6e5 | -12.40527 | -51.07366 | 2025-10-02 04:51:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f00aa43a-7579-3108-9b0a-ebcb9222c299 | -9.93367 | -43.71965 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 081556e2-ef5c-3b5b-a280-a5d223019aec | -12.08187 | -44.9191 | 2025-10-02 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8791f790-1923-36e4-a545-207fbc4dd54e | -11.19863 | -47.7737 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2da40c1f-6c1e-3ac7-b283-a7c91ef6529d | -11.15235 | -54.13031 | 2025-10-02 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb9559c0-a143-3e0f-a7ce-1649076b024a | -15.16932 | -52.80081 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17c51999-c25c-366d-80b8-d8c8fb05187d | -13.74954 | -48.71083 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 592107ac-5b89-3925-a7a9-1b108d4e84c4 | -12.9084 | -47.16364 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 992cd217-2358-33f4-bb6f-ec45161cf627 | -10.83131 | -46.62874 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 584b30b5-76c9-305c-859f-3ef56c5baca8 | -9.85708 | -46.88358 | 2025-10-02 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb0cc67a-7ca4-3ed0-9bf1-6447c2cfafe9 | -11.83658 | -44.9604 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 520a4bab-95cb-322b-bc76-f72bae92700b | -13.22026 | -47.35003 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0f49560-5491-3e62-9cb8-15989287dbd9 | -11.16957 | -47.28388 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a4101ebe-6372-3db7-9596-e68157fa8fc0 | -12.88239 | -46.93169 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55027138-8a1a-3da3-88b9-a7935325ff8d | -13.78625 | -48.05541 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c97f85a1-8256-396c-a676-8d533ae59209 | -11.4663 | -45.06379 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b463180e-4ddb-35ef-b4ed-52e45296db7b | -13.31012 | -47.58834 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 077f96c0-4edb-3610-9f2e-5f167bf7333e | -13.76119 | -48.01147 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55af4c29-3a7e-3b62-bd47-e27ff641f2f2 | -14.79491 | -46.99319 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95ce1bd4-f152-3457-9945-84a9d4efb168 | -9.63186 | -50.89566 | 2025-10-02 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a675d2e4-a019-3151-aa85-bc549d9eacf0 | -9.94149 | -43.74583 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f89e507f-c820-3dd3-abd2-fbee533ba7c6 | -10.93276 | -46.67457 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1bae67d-8336-3e3c-a9a0-bed6f83ed9d9 | -10.14872 | -48.47806 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fbb5238-27cc-3e8a-82d7-e5db69ee3e0a | -14.91392 | -47.23518 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 97574476-43e6-33aa-acf9-f1c41314a042 | -14.3161 | -45.88251 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 682bdff0-dcc0-3f55-86a1-b7c77ccbe3f1 | -11.85905 | -44.99053 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a30b40a-e671-3e0f-91c7-5cb8923ed2af | -14.32726 | -45.87506 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e097ec6-303b-3a37-adb5-0f4286533756 | -15.29488 | -45.09028 | 2025-10-02 04:51:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83c78904-dea8-3122-aa61-d5420c39ec18 | -13.6598 | -47.30594 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a407fcf2-c6a0-3010-a9e7-5e7fd83af30e | -15.55198 | -48.17645 | 2025-10-02 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3c6187d3-b4a1-3e37-bc44-955913d2c3c4 | -12.83492 | -46.86799 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f1a541e-8b9f-31ea-b463-cfcbd7f940cd | -13.18449 | -47.79485 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6de08c8-965b-3bbc-b275-d5ecf15d1a54 | -13.23488 | -47.34304 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2834586-5041-3eb3-97e6-9f051808d41f | -11.86901 | -45.03543 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 12cc4af6-fc55-3f76-9966-07ce0de577b8 | -13.16858 | -47.81468 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c36b0c9b-e2c4-393a-9282-253183893ff5 | -13.4253 | -47.80131 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 0c132b5b-15d8-3037-8721-b36cefe53675 | -15.25751 | -56.77501 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df560907-02df-34ed-b1ee-e2b7ea853f12 | -11.87105 | -49.08319 | 2025-10-02 04:51:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5786e645-bb5b-3083-bda3-fe74eb07b1c2 | -14.31676 | -45.99983 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 47f4db78-24db-3537-a8c4-ce077606397a | -10.35212 | -43.73713 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 046cd9a4-cdb2-3219-90df-f8f88be98623 | -12.68669 | -48.57235 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd6f91da-8247-3daf-98b8-063eac6d1945 | -13.07903 | -46.99786 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61800d42-6b21-3433-b054-a28ec5dbbf2a | -11.81522 | -45.00472 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bd9a414-1469-39b0-9a52-1223b95fd405 | -10.81329 | -46.58688 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9073806-6185-37ae-a4b8-aebaead27e6f | -12.80216 | -46.90254 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 056100d6-268e-31ee-ae60-eb32241242a0 | -20.19023 | -46.02164 | 2025-10-02 04:53:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ec1ba77-b2ad-364b-b051-309958fdcca1 | -20.11475 | -44.39286 | 2025-10-02 04:53:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e19f158e-e8a0-3fd8-86cb-cd8a14bde8d1 | -17.67562 | -43.83363 | 2025-10-02 04:53:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ae25acc-59b2-396e-b174-cdc537f31b19 | -22.27564 | -46.73974 | 2025-10-02 04:53:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 213f8a7e-70b8-3b42-a85d-7c1d2dceb926 | -22.2487 | -43.05564 | 2025-10-02 04:53:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cc885d57-99ce-304a-b8de-b4c9ac3b8eb9 | -18.50612 | -44.03696 | 2025-10-02 04:53:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a399cc10-6d2d-359f-88d6-8fd42c0e0e79 | -17.32784 | -49.38697 | 2025-10-02 04:53:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 541b336f-2806-372e-bccc-f2a29777ca0d | -17.08217 | -48.55976 | 2025-10-02 04:53:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91280df9-64fb-34f5-84a3-81b10df9e420 | -19.71171 | -45.91181 | 2025-10-02 04:53:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a009802-9a49-3b59-9936-8475955a9b84 | -16.18625 | -57.59913 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 8d737d97-45c2-370a-8ba1-7c7afa12158f | -19.80353 | -46.50303 | 2025-10-02 04:53:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 787c11ce-20d4-3966-baa6-0f78d293eee5 | -22.62099 | -44.50305 | 2025-10-02 04:53:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 75bf6033-3915-348e-b571-24ebcccf71e4 | -17.9655 | -44.39909 | 2025-10-02 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bfe99721-efab-345c-b005-634ef847ddd8 | -16.17637 | -57.59295 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0778496c-8e67-3d15-b14e-ea2bbdca5322 | -20.22359 | -43.89792 | 2025-10-02 04:53:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f22079c9-c717-3c1f-b8b1-a77d60bb8918 | -17.21115 | -46.98806 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fed4a2d-819d-391f-9ef0-9ae7778dc2c3 | -20.87531 | -46.46508 | 2025-10-02 04:53:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28da7abd-5e10-3508-9e7a-f0a6c3cf1c6f | -18.34241 | -44.50715 | 2025-10-02 04:53:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85cdd49c-1a08-36c1-851c-eafb4ef5e10f | -17.16327 | -47.03297 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0c496979-fc5d-3334-8b59-b8371a36262b | -20.22314 | -43.90286 | 2025-10-02 04:53:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| aecb04df-96ba-3918-83d3-7fea4a900fdd | -20.18785 | -46.01836 | 2025-10-02 04:53:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27c4f074-fc73-308d-9215-134abbe62e20 | -17.75894 | -51.82535 | 2025-10-02 04:53:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d296bcd3-0280-3fd0-aec4-857bbd0aba54 | -20.85252 | -49.47963 | 2025-10-02 04:53:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bfa9fc24-a9f0-3f28-af97-4e53375f8399 | -20.84102 | -49.42924 | 2025-10-02 04:53:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 80fe3b92-c81b-3f12-af48-50ae008f2782 | -21.78392 | -47.20079 | 2025-10-02 04:53:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bc6d85bb-9e98-3b79-ba76-74e32a05bcfe | -17.68161 | -43.8344 | 2025-10-02 04:53:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5bca63f3-c8ba-3fc2-8391-b0b364419b80 | -18.18229 | -53.27904 | 2025-10-02 04:53:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 912f74e4-cb72-3abf-b0b1-8573241b2b5c | -17.32918 | -49.39018 | 2025-10-02 04:53:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bfcc124-8f5e-3dbb-915a-997b6f7376e4 | -19.85954 | -42.59086 | 2025-10-02 04:53:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| dedded94-d326-35f4-bdbd-e9d5e4a1ee4a | -17.213 | -46.98838 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d26495d9-e379-3e64-b0ef-170a92c35480 | -22.38092 | -50.03417 | 2025-10-02 04:53:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| aff33d9e-3628-3e0f-9576-7dab3b817a06 | -20.13308 | -46.35521 | 2025-10-02 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec76204e-7997-3817-8def-d614685b062a | -17.18118 | -47.03489 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 5a1f9ea4-5faf-3261-a362-a6eb4ec0a443 | -19.01116 | -45.00147 | 2025-10-02 04:53:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a79ff4d9-c468-32eb-891a-ec7966369c29 | -22.56837 | -46.7812 | 2025-10-02 04:53:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6f2dc696-d712-3165-8287-2da311974b10 | -19.51948 | -43.6077 | 2025-10-02 04:53:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b88e8480-3ae5-3788-98bd-12b2f7c5d466 | -18.19721 | -43.57268 | 2025-10-02 04:53:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 76d39dbc-4a58-3b0a-995a-4e12f2018fa6 | -22.25526 | -43.05668 | 2025-10-02 04:53:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 677a71e9-df57-3aad-9da1-b84cd8445512 | -22.56277 | -46.78394 | 2025-10-02 04:53:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| de6af182-3441-3b8f-bf2d-fa072cad8ddf | -19.04978 | -48.13395 | 2025-10-02 04:53:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90aec07c-3d4a-350e-ab24-14cd4aefe36a | -19.72444 | -45.89432 | 2025-10-02 04:53:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d64856c2-ed03-3378-bd7c-3477a71a77a2 | -16.42442 | -52.17414 | 2025-10-02 04:53:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de5b7075-0a37-3aab-8fb8-009e925daa2e | -21.579 | -44.96149 | 2025-10-02 04:53:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dd8be70d-3902-3f80-abe7-a8ddf576ed31 | -15.9738 | -57.22731 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 745e3fd6-6145-3993-8da1-6916a129ebac | -17.75642 | -51.82352 | 2025-10-02 04:53:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 600139a9-b289-3abb-a400-74d59a0ed634 | -22.25358 | -43.05445 | 2025-10-02 04:53:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6e0f8820-4fbc-3a30-abbe-55a46705768d | -20.73249 | -46.03553 | 2025-10-02 04:53:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66d87ad9-4987-3c4c-9959-e69a7c523144 | -17.0193 | -49.14898 | 2025-10-02 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README135.md)
