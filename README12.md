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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b52330e8-ff01-398a-aaca-c62dc68f4db3 | -3.82326 | -41.55485 | 2025-08-08 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 63444d9c-5378-32c7-adc9-cfaf9110119d | -5.39878 | -45.12119 | 2025-08-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c03a6769-ee55-3f21-bb2a-7f628a0426cc | -3.25024 | -43.26701 | 2025-08-08 04:32:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1f04e2d3-1a98-3830-b54a-2f04973da02b | -6.46695 | -44.58016 | 2025-08-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac80c635-9250-3e8b-9a06-d724064932ec | -5.3466 | -45.27074 | 2025-08-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf128dbc-21c1-318c-846e-a11b92e6b7f5 | -5.07394 | -48.3152 | 2025-08-08 04:32:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fa2f11d-52ab-3f2a-aa48-6809edd126df | -5.42284 | -47.14979 | 2025-08-08 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d24356d8-09f2-3551-b642-03d578165cf5 | -6.12734 | -42.96063 | 2025-08-08 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 16694a57-a00c-3ad5-af46-383d90bfed3c | -6.96495 | -42.86939 | 2025-08-08 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 79d8cd90-6b68-306c-a3d5-f54af2fe95a7 | -4.02808 | -48.06487 | 2025-08-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a69e3c49-0a47-3447-a33f-72e8ace474d7 | -4.17573 | -42.03273 | 2025-08-08 04:32:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ddb4ebe9-77ef-34cb-90c0-a0863ccb9fea | -5.16195 | -37.98574 | 2025-08-08 04:32:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0c1ea769-0327-350b-833a-c593cc172e66 | -7.91914 | -45.54512 | 2025-08-08 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61925aef-1b19-352e-ab89-77e3aa698179 | -7.25305 | -44.5999 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3a1a4b47-0a35-395c-8206-859d66e67643 | -9.46858 | -57.85138 | 2025-08-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c9c3fec-b19a-3046-aeef-1db4aa7c367d | -10.48495 | -44.38245 | 2025-08-08 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c201fdf-8c44-3730-901d-2654e393a2d8 | -8.91061 | -60.5582 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb0604de-84cf-3873-8fa1-548e66a44daf | -6.15156 | -55.80465 | 2025-08-08 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 639062fb-4ab5-3dbf-994c-e07f0fa9e157 | -8.90892 | -62.42867 | 2025-08-08 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 12d18af7-3ee7-3c7f-9196-2e0b87cb509d | -11.74994 | -47.50514 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f9bf2ef-7f24-386c-aa0b-5baed58c29bc | -10.63641 | -44.7394 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77a6c13d-ad59-3e61-b872-681ff11e1ff8 | -9.31782 | -62.64822 | 2025-08-08 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9e74ee9-5f15-317d-9402-e8cf22286c81 | -12.3397 | -46.06195 | 2025-08-08 04:34:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f763a485-e2cb-325d-b443-f3b2e9d95c5d | -7.57129 | -44.41346 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cadafb9b-3ee4-357b-bfd4-63d0339edb40 | -9.70787 | -61.29851 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9799cba-1c96-38fa-a0dc-40507ec1dfd5 | -12.61903 | -48.10849 | 2025-08-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b98766c-7289-317e-ad57-4e5f89ea0c74 | -12.53961 | -47.09663 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1440d358-d180-303b-b1d5-51ab126d6fc5 | -12.52577 | -47.14222 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 60994a3b-80e0-37ba-a70e-5f3441fec3a1 | -10.63904 | -44.7574 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ac3c08cf-9d73-3306-997f-39c996945178 | -7.32439 | -44.6984 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dff2056b-260f-3132-9fbf-6cacf96c451f | -11.20977 | -45.36508 | 2025-08-08 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e44ef746-f9e1-317c-b2de-c36030f3438d | -6.15257 | -55.80849 | 2025-08-08 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0586a626-e629-3cf2-b2cc-ba7dfb873848 | -8.48629 | -46.00767 | 2025-08-08 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c360cad-4a69-34af-9894-4fb5575463d8 | -8.21299 | -45.06162 | 2025-08-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd838c19-2d3f-3129-8f70-9c47ff4e106e | -13.30047 | -40.36057 | 2025-08-08 04:34:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 80898dc2-bc8e-376c-8cff-4465a40160d0 | -10.63452 | -44.76162 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f478aad5-ad4e-3cea-b1b8-acd04aa8a764 | -7.91559 | -45.54462 | 2025-08-08 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36d180a2-6dfc-3514-acf9-c87095a17da4 | -12.51884 | -47.14114 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e2a89c5-f7a5-35bf-b80c-9f00e809ad65 | -12.56213 | -47.13613 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 735045f0-5835-3e27-8a40-2b345d088e9a | -7.85936 | -39.711 | 2025-08-08 04:34:00 | NOAA-21 | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c7ffef0c-48ab-3e66-84ff-17ffc856534b | -11.32135 | -55.21541 | 2025-08-08 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6e42002-480e-3d6a-922c-ef00453f6ce5 | -12.55809 | -47.13942 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e745ab74-121b-38f8-b37b-aef652ccd97e | -6.15545 | -55.81097 | 2025-08-08 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30ad3143-927a-3cc0-bb00-543c87aa104f | -12.58306 | -47.17773 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bec6358c-1b45-3cd9-9b78-784ce1add880 | -9.65194 | -43.84928 | 2025-08-08 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d81996c0-8432-327e-9523-b56dd806e1c4 | -8.90627 | -60.54682 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 573af35b-4117-3354-ab50-9cee2606b875 | -9.94013 | -60.47124 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 85650dbb-e33f-370e-af40-ab1289b1c128 | -7.91142 | -45.54816 | 2025-08-08 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a56b8dd1-49e3-3e94-a80e-45ee8acafda4 | -9.70944 | -61.28882 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5195b9c1-ae7d-3c5a-a731-62c6144ff545 | -8.25231 | -45.07455 | 2025-08-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14963f7f-fedf-3b1f-b55c-48f6e1939d35 | -9.65145 | -43.85267 | 2025-08-08 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 02fb7b1e-90c8-334a-9c34-dae65fc56c38 | -12.56099 | -47.14379 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edfc4ad6-da06-3616-87df-a028bdb9b4ad | -7.25194 | -44.6583 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7b621e5c-dfb1-37e9-9a4d-4fc518705370 | -9.93638 | -60.4625 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd000b03-0125-3ffc-b306-68931621a4f9 | -7.11541 | -44.22066 | 2025-08-08 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 551a19f6-1795-3bea-871b-ff916ea75240 | -10.61923 | -44.75933 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e934075d-9037-3d6a-8e11-fbd683bc6460 | -7.37702 | -44.64845 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 930892de-6093-3a19-b940-883ac0cb29b3 | -12.71707 | -46.3756 | 2025-08-08 04:34:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b523ac15-9bb0-32ad-b132-78c4fb0e5d5c | -9.4693 | -57.84523 | 2025-08-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c28baff-b86f-318a-8bdc-31c13c22ff1c | -9.93436 | -60.50029 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 873576cf-6343-3af1-a684-71f84cbcb02e | -7.7412 | -47.39183 | 2025-08-08 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| decb80de-ee7c-3ea9-999f-c6d587136c46 | -7.24825 | -44.65775 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c93e9e80-a036-330c-9338-77c9c3f1705c | -7.758 | -43.59173 | 2025-08-08 04:34:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 709155ef-a198-3f40-bae9-edac0c574ffb | -9.93454 | -60.47211 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df9901d0-3dc6-3979-8e2e-13fa401ca853 | -7.06553 | -55.41709 | 2025-08-08 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2dddbf46-cc7a-3968-b95e-9c1f1576fc54 | -9.92411 | -60.45989 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 12db36c1-55cf-38cc-b20f-2af31a6d6142 | -12.54367 | -47.14103 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 79214e3e-4db5-3985-bfa5-af3a4891d21a | -11.4595 | -47.319 | 2025-08-08 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2f1efe1-a31c-3f00-8757-c987a2032186 | -9.9411 | -60.46639 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0735e214-a9b6-3401-ae97-afd17735ed82 | -7.37833 | -44.63967 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 843b69d6-29c8-348e-a20d-8456d3d3d418 | -7.11367 | -44.20643 | 2025-08-08 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5944e0ef-7cda-3111-92f8-178a8231c14c | -7.10989 | -44.20587 | 2025-08-08 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b4cca3f-39d7-3201-b7b8-90d6d22ab4d8 | -9.93015 | -60.48928 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e882712-1292-3877-b671-a92a8a61ad84 | -11.65482 | -46.8724 | 2025-08-08 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dc562a6-1294-38fb-b56f-e03a601e8532 | -12.72066 | -46.37613 | 2025-08-08 04:34:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b796cb2a-2faf-3413-a05c-6446baac8b8a | -7.25439 | -44.33095 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3ba3d49-4dcd-3822-90c1-e76b52435455 | -12.56446 | -47.14429 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e465e473-4d21-3cf0-ae04-faa1a17e139c | -11.74544 | -47.51192 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87f2fb07-1bbe-3ead-abb1-ffda4ff3ebb3 | -9.70243 | -61.29171 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 46ad2a7b-dab7-35b5-990b-53a6bfab12ae | -7.24024 | -44.66094 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44e1bc30-b0d8-36b3-b2ba-cae82e34ec79 | -12.71647 | -46.37978 | 2025-08-08 04:34:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3763b879-0b70-3e36-ac5f-1dcc3219edb3 | -12.46456 | -43.56182 | 2025-08-08 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 868a0afc-906d-3acc-8674-6e9f877c14aa | -12.52227 | -47.11784 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 09cc6e8c-2e78-3ee9-8cea-d5347187ece9 | -7.91742 | -45.53251 | 2025-08-08 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 680f8ba4-b835-370e-b5b7-d8e289d73d44 | -7.2515 | -44.63583 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8842a2fe-bec7-3b7c-a60e-5e3a9edf3545 | -11.18858 | -51.4327 | 2025-08-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cccce9f5-5d4a-3143-8269-c9cce0e99579 | -7.2489 | -44.65334 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 52730bba-beb8-3a16-9aa6-5a5e60474308 | -12.53327 | -47.13942 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 257cdf0c-04eb-33b1-975a-b9dd32257288 | -12.51995 | -47.10952 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 321cca1e-57c2-33fe-9c6b-86d149a71379 | -12.57493 | -47.16061 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6e54b47-dcd3-332e-81d5-097297f6b5bb | -11.45955 | -47.31601 | 2025-08-08 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e99f497-6047-3ad3-a7fc-3f102c1eb6a2 | -7.38137 | -44.64462 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| b2ac6fc7-3d44-3f80-8250-b0ab38050535 | -12.30783 | -50.00438 | 2025-08-08 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3299c993-e92a-3c36-a008-e472333808c9 | -10.57951 | -45.2561 | 2025-08-08 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ee6e925-1428-3d4f-9023-909d8fc25ee8 | -12.54308 | -47.09718 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54c17d26-46eb-35cd-821e-3fd4581d05db | -8.86289 | -47.27385 | 2025-08-08 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ab586155-9271-3c30-8a77-37c8b17b5c55 | -9.06907 | -45.06484 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43d0220e-32f4-3674-a9c6-e32db096cb94 | -10.62305 | -44.7599 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17ef59a3-1da4-31c2-b84a-daf633863a5f | -9.93418 | -60.50735 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4109fc27-90e6-3ae4-bc40-124d78686e9e | -11.45898 | -47.31976 | 2025-08-08 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README13.md)
