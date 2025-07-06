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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f94f3708-d765-38ae-9f7d-f2d18e21136c | -12.02724 | -57.08842 | 2025-07-06 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 00b51a62-4797-3ffa-8942-184b6bc6f0a9 | -12.02768 | -57.08483 | 2025-07-06 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 57c66282-784c-3db0-89e7-6ea1be82e518 | -7.9062 | -61.51198 | 2025-07-06 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f2765253-2870-3961-861b-f82c1cb390d7 | -12.02308 | -57.07684 | 2025-07-06 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3925c7ac-ea00-3667-83f4-0be3ee2c4ea1 | -7.18023 | -56.71891 | 2025-07-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73b676a8-c26e-364e-b5db-229c2a537ce9 | -9.01293 | -64.12306 | 2025-07-06 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dee26a1-bf93-326d-9f46-d4626981003c | -9.3131 | -62.65607 | 2025-07-06 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c1fbe21-e3c9-316d-8a32-516e4494a5b3 | -10.04639 | -64.98386 | 2025-07-06 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e1ee1c1-8c24-3aec-97ed-4ae747e098ca | -7.18067 | -56.71568 | 2025-07-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fcddc08-e78d-3c35-9c59-01d3b20624d6 | -9.91883 | -59.91233 | 2025-07-06 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5119e0a9-97a7-35a5-b1ed-dee79bdbea95 | -9.29143 | -65.86176 | 2025-07-06 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7b28fcf-ce4d-3131-bae0-7eb5467c7303 | -11.98047 | -55.51827 | 2025-07-06 05:42:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f601be09-a2fb-3957-9fe0-d646da793534 | -9.35219 | -58.84491 | 2025-07-06 05:42:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 884888c5-7025-3540-936e-a51aa6194be5 | -11.47133 | -61.94154 | 2025-07-06 05:42:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 861661cd-b00b-302e-b3ea-8bf0e825040f | -7.43021 | -60.02962 | 2025-07-06 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9052215e-f241-315a-a5bf-ae8299681582 | -12.58311 | -56.98579 | 2025-07-06 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d80c3b3-3bac-345b-8459-64f6abd8d7e5 | -11.77757 | -62.92646 | 2025-07-06 05:44:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2128095f-53a0-3a05-af88-bd66e922653c | -12.58267 | -56.98952 | 2025-07-06 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64e04bd6-badc-36de-b9ac-dbb36be9709f | -12.578 | -56.98135 | 2025-07-06 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c75f1f7f-2d4d-3070-9ff0-f4b4618bcbe7 | -12.0266 | -57.0845 | 2025-07-06 05:50:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| ee775ea1-dd66-3403-bde9-f62398dd9966 | -12.0266 | -57.0845 | 2025-07-06 06:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 020c1027-0ab9-3363-b667-c938774bf93d | -12.0266 | -57.0845 | 2025-07-06 06:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| cbd23d7a-012f-3872-a3d0-9a05b9fe42e8 | -12.0266 | -57.0845 | 2025-07-06 06:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 8c51c7de-0f2b-37d8-af00-00651c62ecb0 | -12.02589 | -57.08738 | 2025-07-06 06:25:00 | AQUA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 47aa2862-b473-3386-8ca0-bb0ff2eacaf5 | -7.89916 | -61.50521 | 2025-07-06 06:25:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 1d9cfaa0-3adf-3b96-8ad3-b8de017582dd | -9.93085 | -59.93097 | 2025-07-06 06:25:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8b64e1d2-aca9-362e-9f63-8cd23d26c6b5 | -12.02726 | -57.07839 | 2025-07-06 06:25:00 | AQUA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 2fe5202d-f718-3648-ba1b-c909a9731766 | -12.02863 | -57.06941 | 2025-07-06 06:25:00 | AQUA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| bb9781bc-8a6f-32d7-81da-585f86ce83cf | -12.01844 | -57.07703 | 2025-07-06 06:25:00 | AQUA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| a461128b-253e-3228-b665-220b04b0c9d7 | -12.0266 | -57.0845 | 2025-07-06 06:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 5c981388-a479-3cc8-bf6e-6d946af7c305 | -12.0266 | -57.0845 | 2025-07-06 06:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| d82236fc-05c1-3507-a04e-ce1c5bb6d144 | -12.0266 | -57.0845 | 2025-07-06 06:50:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e1397ad8-8310-3767-be1e-6e9b494ec09a | -12.0266 | -57.0845 | 2025-07-06 07:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a7c5019e-6551-3510-a3cf-d8414152cd15 | -12.0266 | -57.0845 | 2025-07-06 07:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| ec74f624-845c-336d-9747-ba95b77e2537 | -12.0266 | -57.0845 | 2025-07-06 07:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 67bff1a8-3bee-3bb5-8310-3655f2afcf4b | -12.0266 | -57.0845 | 2025-07-06 07:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f81e2b61-085d-3321-83cc-c3a084e2c82f | -12.0266 | -57.0845 | 2025-07-06 07:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 3c6b2277-0e93-3253-9a3d-09618dd42f0c | -12.0266 | -57.0845 | 2025-07-06 07:50:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| f4dc0ff8-49eb-365c-bd20-04745bfce6d4 | -12.0266 | -57.0845 | 2025-07-06 08:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| f14405b9-4b37-3d40-a3c8-665840adeda1 | -12.0266 | -57.0845 | 2025-07-06 08:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4337f1ac-5489-37e3-8ac4-cd2aa533d284 | -12.0266 | -57.0845 | 2025-07-06 08:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 3a1ccfb4-4481-33b6-99c4-2124c248868b | -12.0266 | -57.0845 | 2025-07-06 08:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 59743afc-3513-3dba-a7c0-e13d58f2b394 | -12.0266 | -57.0845 | 2025-07-06 08:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 4ccc6a6e-b42b-332c-88d2-c6f78ca45c0d | -12.0266 | -57.0845 | 2025-07-06 08:50:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 796328ea-3949-3a3f-8e6c-671e531e46a1 | -12.0266 | -57.0845 | 2025-07-06 09:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| be3f3227-c558-3d7f-93cf-8a3ac5f685fd | -12.0266 | -57.0845 | 2025-07-06 09:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 87accb80-c759-31a4-bfe1-e1ff4661ac3e | -12.0266 | -57.0845 | 2025-07-06 09:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8747758c-55a5-39ba-b335-b166490a1122 | -12.0266 | -57.0845 | 2025-07-06 09:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| dc13105b-42ec-3e3e-af91-5f4a057d8da3 | -5.6065 | -45.1852 | 2025-07-06 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 58bbd6e5-5e0d-3d7a-acf6-2a47f8cfadaf | -4.97815 | -41.74686 | 2025-07-06 12:06:00 | TERRA_M-T | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 44a69b44-58e9-3f24-963a-4a41dc8001b6 | -3.45463 | -41.62151 | 2025-07-06 12:06:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 41d5332d-a56d-3f91-bdb8-b976710aea16 | -4.10058 | -42.46748 | 2025-07-06 12:06:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0633a9d2-d527-381e-9a76-d83d64fac4ab | -10.99999 | -42.78772 | 2025-07-06 12:08:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 8aadd4ee-b1c5-3a1f-a2dd-ec3e9517dcbb | -8.52511 | -47.52256 | 2025-07-06 12:08:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6d506551-6ff0-3986-972b-c17d1b352378 | -8.73822 | -46.74069 | 2025-07-06 12:08:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b5fbc2a0-1516-36ca-a73e-cdcfe8b6d967 | -11.45196 | -45.10015 | 2025-07-06 12:08:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c5a49ddd-54b4-3bd9-b4aa-c2ea89122edf | -5.57255 | -45.21771 | 2025-07-06 12:08:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b50082fe-85bb-3248-8dee-a299eac077aa | -8.74822 | -46.74214 | 2025-07-06 12:08:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 15e43c5b-bf3e-38ab-a88a-9fdc5f97c976 | -8.24643 | -46.93776 | 2025-07-06 12:08:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3b75e6b4-659c-3e93-9a12-a80b4217c78b | -6.83796 | -45.07753 | 2025-07-06 12:08:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5e2cf528-71d9-3c25-9e79-cde9e5d997a8 | -10.18278 | -49.5097 | 2025-07-06 12:08:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b0192416-32bb-3556-8b1a-da360b8ff522 | -6.963 | -43.73328 | 2025-07-06 12:08:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4ceb1ef3-d9e0-3361-acee-4f0d8bb70375 | -7.37835 | -43.72654 | 2025-07-06 12:08:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0f879350-908e-3288-a76b-9402c98efd4e | -7.04497 | -44.05333 | 2025-07-06 12:08:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0fe5468f-6e26-37b7-9946-ce92d6c8464f | -5.60401 | -45.20128 | 2025-07-06 12:08:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ccb7f209-5777-318c-ac33-443904bd0946 | -7.3872 | -43.72781 | 2025-07-06 12:08:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| aab0b176-52e5-3d65-b017-0e6c61eb95f6 | -7.04365 | -44.06239 | 2025-07-06 12:08:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 8b6c2a65-6368-38c7-abe1-064f7114741e | -5.57407 | -45.20743 | 2025-07-06 12:08:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| ef636c1c-cd74-37cb-84bd-9673364916a8 | -6.28701 | -45.73251 | 2025-07-06 12:08:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cd28d34a-05d1-32fd-81be-970f48a1b392 | -8.74 | -46.72913 | 2025-07-06 12:08:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e58b5128-682c-381c-a43d-dad3cf2ad19e | -5.60701 | -45.18076 | 2025-07-06 12:08:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 3b373213-b315-3787-b2f7-91b396892098 | -6.40134 | -44.97317 | 2025-07-06 12:08:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 264d3d58-79d1-3adb-a978-2a5726c86816 | -7.00784 | -43.54913 | 2025-07-06 12:08:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f2de5c13-60cf-358a-984e-6f61c5e57662 | -10.86537 | -47.18317 | 2025-07-06 12:08:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9b12148c-d685-3fab-a877-205f40283323 | -11.45059 | -45.10936 | 2025-07-06 12:08:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 99451656-abd9-3a89-98c5-148cc88ebf53 | -6.9643 | -43.72438 | 2025-07-06 12:08:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| cb2be6ba-f0dd-3349-94b6-9e629014c329 | -5.59754 | -45.17939 | 2025-07-06 12:08:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| c52330ef-a615-34ae-bca8-f6a7e1f8519b | -6.28864 | -45.72174 | 2025-07-06 12:08:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f8ddb23f-e9fb-36e4-97cb-f2091b335ad4 | -6.76019 | -44.61152 | 2025-07-06 12:08:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c1def7e5-41fa-32e3-aefb-d7054e02c21d | -6.68809 | -43.1456 | 2025-07-06 12:08:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8b4d1db6-f860-3bdc-9844-827683361078 | -7.32913 | -39.95566 | 2025-07-06 12:08:00 | TERRA_M-T | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 96f576a7-7328-3330-9967-ef0fd08571c8 | -10.18558 | -49.49221 | 2025-07-06 12:08:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| fbee6dc4-6abb-39de-84fd-91f1096869f1 | -6.83945 | -45.0676 | 2025-07-06 12:08:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| edf585df-5e68-307e-b265-312cbecc4c18 | -5.60551 | -45.191 | 2025-07-06 12:08:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 2c16d2f2-6767-37de-b7c6-99e0858014ea | -6.40282 | -44.96325 | 2025-07-06 12:08:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 75d62838-839b-3409-9fdd-e34187b7b31f | -5.6065 | -45.1852 | 2025-07-06 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| c4d95f5f-eb61-330f-a9a9-a7e4352ade06 | -14.03131 | -46.25187 | 2025-07-06 12:10:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 5811e52d-2405-3884-9a2b-23dd415a5f5c | -12.01451 | -47.77556 | 2025-07-06 12:10:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 379871a4-a033-32dc-95a2-2e31d2ca33ce | -13.83925 | -43.04307 | 2025-07-06 12:10:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5de5c19f-bdd2-3831-89a4-737143ad1578 | -13.84058 | -43.03349 | 2025-07-06 12:10:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 21d8fded-2997-365a-a07b-df705c2a6f3d | -14.03277 | -46.24205 | 2025-07-06 12:10:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b6e3ad6e-3b14-3b59-ae62-d3994c648328 | -19.79437 | -46.29657 | 2025-07-06 12:12:00 | TERRA_M-T | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6ab43ad1-2b2a-31d2-95ce-3503c26c7722 | -19.793 | -46.3059 | 2025-07-06 12:12:00 | TERRA_M-T | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 81d98313-f495-358f-84ee-e6244817c88e | -22.67633 | -42.8433 | 2025-07-06 12:12:00 | TERRA_M-T | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 00ca4a3e-c81d-3a26-bbf2-feefbbd3f234 | -21.32375 | -44.24659 | 2025-07-06 12:12:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 953db1df-2058-3d90-9004-969a4d9e1f1d | -21.32512 | -44.23626 | 2025-07-06 12:12:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 322c0d27-4150-3286-9712-775db28b2e4a | -22.67479 | -42.85605 | 2025-07-06 12:12:00 | TERRA_M-T | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 9525f1c2-7c26-34ba-96f0-ee686c3edf19 | -16.50761 | -50.39981 | 2025-07-06 12:12:00 | TERRA_M-T | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ca341057-9b56-3b6c-b64b-b2904ca9032d | -17.43978 | -43.64418 | 2025-07-06 12:12:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 66df483e-b887-3925-970a-d0fab9f0753a | -15.95989 | -47.41429 | 2025-07-06 12:12:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README11.md)
