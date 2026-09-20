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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73273b2e-26ab-3889-8dc9-6264de212054 | -6.65096 | -50.91806 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 716fb14d-1368-36cd-adec-a4deea6e77db | -8.38421 | -45.63276 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9524ebd8-450a-3531-aea0-ea6319b0b570 | -8.42597 | -54.72441 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bfb6dc0-6573-3f93-9e6f-6a13138442ed | -7.53369 | -44.93288 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 837c39b9-4985-3126-84a5-c841e549b8bb | -12.64544 | -50.92445 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03def61d-6b58-35c5-bf39-0660a50c58f1 | -13.88659 | -48.58112 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d5ec7977-29ef-3ffe-b621-e3ee8874c5b5 | -10.11207 | -49.54628 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc87ad53-4b76-3afa-adf2-790bbb736eb6 | -8.29556 | -50.8127 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36fe33e2-f0b6-3188-a9f9-efcdf928e78c | -8.04457 | -46.27182 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fd1d7cd-2119-35ee-9841-d0f39b35f6b6 | -11.87935 | -49.00555 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9de9351a-e993-32d4-b7af-2c302ddf19e6 | -11.43008 | -45.4187 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d3afd50-8ff5-3289-8772-0d9079995702 | -9.12188 | -45.72365 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6e2664c-4d91-391d-99f0-38341077922e | -9.11831 | -45.72309 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36c65921-991f-3f1d-a917-084955005d7f | -7.35406 | -44.46519 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2da42ba-db61-3296-ab08-d54a09411ec2 | -11.81441 | -48.83621 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07a46e7f-f349-371a-9243-5f0143f32264 | -8.92067 | -50.76412 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ec71bf0-7ae2-3f38-a65c-9211f0887421 | -11.22687 | -54.07978 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 28010a47-882b-39af-ad52-ab3a2e9e8e0e | -9.88672 | -46.5401 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbdaf896-5383-3241-b443-ae8594b3f498 | -11.45885 | -45.40445 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0e3ea47-c989-3021-941d-9609b34677b5 | -10.56563 | -46.55178 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 745899ba-04ad-3e23-af02-30c2223d7c48 | -12.34347 | -50.69089 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f319d551-b2bb-3f86-901c-733f0b7b2018 | -9.73646 | -46.07998 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55602f77-f575-31cb-a10b-61d0fcb3d097 | -11.44594 | -45.38844 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f744490-f92e-3dd0-8f9e-de7332db843d | -7.14173 | -47.43364 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9440076-3764-3fd8-81fe-8f5ad6bc98ec | -9.96283 | -46.54307 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f50a09c7-979d-3109-98c6-36216047e775 | -9.01642 | -48.16668 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 382366b0-28ee-3d8d-b41c-e64f1c11038e | -8.97111 | -44.66628 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cb2ca58-8c39-3f4a-9927-15c32c08dddf | -5.73038 | -53.45299 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 745e407f-079b-37f5-bcc8-68743ef180e5 | -11.45302 | -45.36621 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11b59c7e-21e1-3ec5-9a9f-8d85d3dd9e2b | -10.27777 | -50.27211 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8be0ca1b-a680-386e-849a-973ef060e7ae | -11.98545 | -52.47947 | 2026-09-20 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43c22540-e0ac-37c7-b122-3b8af254846a | -9.02187 | -48.73481 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b504715-ab90-3764-ad9c-53aa0f7473ed | -12.34742 | -50.68783 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d587db1f-d93d-3519-b244-6409c3e1d4d4 | -9.83469 | -46.43724 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bbae2c57-5167-303f-bcb8-d39c5de45026 | -9.26434 | -46.19035 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d19cba7-068e-36a2-bb74-b9c2ff4fe4c7 | -7.55854 | -45.68977 | 2026-09-20 04:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2c6def9-9a32-3455-bb4e-b742ace478ae | -10.87514 | -54.08514 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5038093d-a51a-3a1e-bc6d-4d11991b8cfe | -11.69596 | -47.73396 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29efebf2-0fab-380d-b3ee-b258989acd8e | -12.31798 | -50.72018 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0d76d66-b188-37fd-808c-23f429a8d67c | -11.02349 | -54.14114 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a7b82f1-48b9-3a3f-89e0-ddd606ec65d3 | -7.34981 | -44.61906 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2ff9c3a-89be-3e59-bdf3-fe52c3dbd4aa | -11.23824 | -48.37509 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e0c7b0d-8bd7-3cb4-b470-727ccd436e55 | -5.84937 | -53.55041 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 248b6bd5-33a9-3121-8028-677639f1ff53 | -7.53551 | -45.43792 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 4a391094-5872-39ab-9375-ea6df38b1e54 | -13.88886 | -48.58878 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb2dd358-5e34-3a60-b128-3695d2915ee7 | -9.80764 | -48.31725 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98243779-c80c-3cbd-b8c2-14d52044d57a | -5.97995 | -57.77633 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a35baa7-7885-3887-955f-8ff6194d45dc | -8.42483 | -45.86378 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11c672fa-aeba-37e2-93e2-2c16089ac6c9 | -6.36581 | -58.31042 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ceaead54-1d4f-3aef-8553-186d4bf17918 | -8.17809 | -54.74803 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ca92716-a9d4-32f7-a959-834240bfad59 | -5.97831 | -55.36922 | 2026-09-20 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9ca285e-3de1-3290-b760-f8fe34edffca | -11.12505 | -47.72893 | 2026-09-20 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 765b1927-0d29-38bd-9191-3b62885ad1d8 | -10.33054 | -47.98772 | 2026-09-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b4c6ca71-eef6-3b22-9462-d0a646033bed | -13.31984 | -51.81231 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af25aa0f-66ef-3724-8f87-7fffae4a22a4 | -11.02442 | -54.1596 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc483f8d-d5e5-3f77-bdb2-6b1e16e3a6ae | -10.30211 | -50.23875 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 8426dc1f-31ec-34e6-8282-b0fe8b816de5 | -12.65148 | -49.47083 | 2026-09-20 04:40:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 93b4054c-4744-3669-94a2-9553a4f56c58 | -12.12942 | -47.03789 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a34f606f-ab6d-30dd-a232-babceb4c75ed | -11.86228 | -47.67278 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f778344b-09e9-37ad-9730-a69a103cbb3f | -10.46055 | -51.27629 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b9e3106-32d1-3064-8925-0535fa6716ef | -14.10579 | -44.83071 | 2026-09-20 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60133b3f-7353-3530-a40d-facf9f8afb45 | -10.87241 | -53.97079 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a55fd3a-b538-34c7-9f4b-1aafeb0e4329 | -8.84689 | -50.46748 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f83bcee6-bdfb-3605-98aa-ffb4e53d7c6a | -6.77795 | -48.66036 | 2026-09-20 04:40:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a68a5d99-1462-3b5e-9752-da56a2cc02b4 | -9.96587 | -45.30404 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bddbdc29-ddb0-3c1f-bafd-8fc909b8d636 | -10.4663 | -45.08871 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a686e93-a153-3d7f-af61-1bb342b6ee56 | -9.791 | -45.07684 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c0ef081-adda-3e0c-9ace-edf957293fff | -10.38744 | -48.99128 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7eafa784-4062-3708-930c-045e03854b01 | -13.00983 | -46.92051 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02e2f86a-002a-3f18-9c99-f729a73feb56 | -9.78501 | -48.3315 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa4dc082-df8f-3d3c-9c86-87559b296267 | -11.04443 | -54.16342 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4a1b05f5-2e32-316f-a68c-6749b9b807ba | -7.54849 | -45.44825 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9956d81-6699-3446-82d9-146a1be8dd8d | -7.54448 | -45.42686 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 2904315e-14b1-3255-b4cd-c08f1c3bc860 | -12.56691 | -47.08255 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc34aae1-5676-3aaf-a268-227f48db8da9 | -13.96217 | -47.85416 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a3d5451-0791-34df-9897-37abca356a71 | -12.5338 | -50.03826 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 277afef2-385d-32a7-a272-b549454af07f | -10.31807 | -50.20436 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86a7a90d-0a4b-3314-842c-f1ab7baf81e7 | -6.6654 | -50.94114 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df73281c-2a80-39f5-ac4d-01559fab959d | -11.73718 | -54.55635 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17860ba4-67cd-30f2-9a3c-752e45d8e775 | -10.31513 | -50.22238 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d8f19a8-5f25-3ebd-858e-409bda75f56e | -8.29886 | -46.84774 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d299803-8562-3aea-a33c-05cd941dadc9 | -9.89947 | -45.10019 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62bcdf54-75c9-3045-93dd-4fc6c3b0c5df | -8.99826 | -45.00425 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfb52141-29bd-39e8-8b4b-dd6566cd29ad | -9.56254 | -46.5554 | 2026-09-20 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 043bf483-d0c7-3a57-b3e0-fa39288a5ef2 | -12.41875 | -47.46627 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| deaa7d1d-26f2-3877-aa98-bd721c743a63 | -9.03346 | -49.83279 | 2026-09-20 04:40:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 470a65d5-47a2-3e5e-bcc6-1912d0a3e1fc | -6.46992 | -48.43962 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28eb6269-7f48-397f-aa45-d57f0cc85cf2 | -12.37699 | -46.99834 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d22ad224-6498-3e60-b22c-09ea0a9f87b5 | -5.87213 | -52.03978 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e40ddb1-98ec-3f16-85e8-b8e002c4f001 | -11.03242 | -54.16112 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a613eb1c-4771-39a8-bbde-cc84c402b7a2 | -5.98566 | -55.69792 | 2026-09-20 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e91ddb4-0f4e-38d5-a0bc-0e08e5cf2bcc | -11.0503 | -54.16125 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cde716c1-7b01-354a-9d19-5cfceb84cc5e | -9.81096 | -48.31775 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f491a23-8b5a-3abe-98f5-0ae5054a00f3 | -9.89544 | -46.52956 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d9dba10-af78-3f3e-b0ed-54c1ebfc20e7 | -5.86248 | -52.03189 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0044178-63e3-3ad0-b3d5-4d99b44f1a6a | -9.18921 | -60.76195 | 2026-09-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 340b4d00-d5db-3cef-b816-90bcf7fa4ac0 | -11.46894 | -45.33594 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f758acd7-1a9f-3238-b1ae-4a0e4073fa33 | -13.27917 | -46.73336 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ad7909c-bf36-305c-afc7-819b9f7841b6 | -10.89736 | -53.98211 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b6cfe6a-6d65-32f7-ba4e-9a7c90a8fedf | -12.74983 | -46.19057 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |


[Clique aqui para ver as próximas entradas](README71.md)
