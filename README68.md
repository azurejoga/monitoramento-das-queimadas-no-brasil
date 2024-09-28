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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1be7184-4b2b-3d10-8fc2-10bc1db6a3b2 | -5.39296 | -44.64258 | 2024-09-28 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49ea76cc-1e2b-3818-a3eb-63157f62fda8 | -5.39216 | -44.6482 | 2024-09-28 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f49a789-b026-30d1-9321-948831c807d2 | -5.25491 | -44.72939 | 2024-09-28 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c2e40fb-1a0c-3c3e-b5d4-c300055f2c20 | -7.88727 | -44.60312 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a49aae89-4e3a-3d60-88ab-c77ed59ed518 | -7.88564 | -44.61587 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 96be3e8f-e2b7-3935-b18f-db3916ce2d2b | -7.88048 | -44.60215 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ec9d0bdd-698f-3a7d-ae7d-faf0b5e963c0 | -7.79392 | -44.67129 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.5 |
| b2dab161-c11a-3c57-a1ae-2584c9aa2653 | -7.79314 | -44.67732 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c1c7d0f9-63a7-37e5-adcd-b8c6f6075722 | -7.79236 | -44.68339 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b2b81fbd-7448-3163-a097-35bd9ed2d48f | -7.78718 | -44.67025 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 833fe635-1984-3bc8-8c53-f0b1e1f18a86 | -7.7864 | -44.67625 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9bab9a63-b1fe-37d5-91e2-16bd25f913c8 | -7.78562 | -44.68236 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 909bd90b-6578-37fb-8193-e60853bc2500 | -7.77292 | -44.67415 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7a52ffb6-0d03-3751-a12e-950f1ec2af2b | -7.77212 | -44.68041 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 572843d4-cf72-38ec-9f12-116ddd147a65 | -7.77133 | -44.68658 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| fa4687b5-48a7-3b30-82d0-ff52485db882 | -7.76693 | -44.66719 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e30a5d58-5e68-3fba-b42d-7bd8638935a4 | -7.76617 | -44.67316 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 79acfeb4-e064-31d7-ba2a-63ed99954597 | -7.76539 | -44.67929 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2e7b88fd-904a-3408-8f25-82826f10c8c8 | -7.7646 | -44.68547 | 2024-09-28 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| eeaa1620-ce66-3e17-bb49-9d50ea2a85ab | -7.27944 | -44.9644 | 2024-09-28 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f26b7f3-271f-302d-9855-48d1562e5f1b | -7.27476 | -44.96141 | 2024-09-28 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fa12c05-e9d5-3e28-915f-c553945c59fc | -7.27398 | -44.96717 | 2024-09-28 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 225f6dad-23a6-3881-b2c5-321b14d25c23 | -7.27281 | -44.96368 | 2024-09-28 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3b9deee7-2b8e-3e0c-a8f6-e312fdb3b70c | -7.26936 | -44.93803 | 2024-09-28 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4eb6d98f-dd3e-3d6c-a1f9-8e6a5cf2bfa7 | -6.58555 | -44.17887 | 2024-09-28 05:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 024174d5-eaaf-3e19-bede-f8061621224a | -6.58471 | -44.18515 | 2024-09-28 05:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a92883b6-51c8-3c8b-b724-ebe021e19b7f | -6.57857 | -44.17885 | 2024-09-28 05:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cadc92e0-5595-3417-90f1-e2695ed3a117 | -6.57781 | -44.18457 | 2024-09-28 05:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bbc4a7b8-b186-3594-9fe6-c00f4539d3c1 | -6.57165 | -44.17833 | 2024-09-28 05:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5cc436e3-1353-3673-b47d-4d8a7c0aab57 | -8.3627 | -45.48295 | 2024-09-28 05:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06ddf184-1e4b-35f2-ae3b-92717f89b8b4 | -8.36251 | -45.48431 | 2024-09-28 05:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39d22fe9-0dff-365d-b7bb-8a851b3117cb | -8.36182 | -45.48995 | 2024-09-28 05:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 34291d3b-772d-3bc3-a2f2-86833f5c0881 | -8.36123 | -45.49414 | 2024-09-28 05:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 13971a95-a304-335e-ab9e-4158bfb7571b | -8.71473 | -44.7834 | 2024-09-28 05:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 521e4c16-38c7-3755-a167-e42f1eccdd9b | -8.714 | -44.78926 | 2024-09-28 05:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2f072cf-24dd-3e91-8a02-8f5d69caec12 | -4.98518 | -45.40533 | 2024-09-28 05:08:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 978e2d22-80d0-3a8e-bdf9-004335155782 | -6.17837 | -45.43629 | 2024-09-28 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e0799b44-a414-328d-81ad-8603e1b008e3 | -6.17209 | -45.43508 | 2024-09-28 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6a1e7872-faea-3a09-9e9d-2871c7e77be3 | -6.17141 | -45.44015 | 2024-09-28 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 01140967-92c7-3686-a9f4-1c74c35af639 | -5.77035 | -45.54943 | 2024-09-28 05:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b31941dc-4046-32ad-817b-2952652f940c | -5.76413 | -45.54835 | 2024-09-28 05:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1c4ab24-edaa-3b45-856b-105e92d50864 | -5.7085 | -46.45141 | 2024-09-28 05:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 129a62c2-847f-3f3f-a220-fc17064e93a1 | -5.70791 | -46.45574 | 2024-09-28 05:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e913f559-2ccf-3152-a898-cd2a508bc708 | -5.56745 | -46.28178 | 2024-09-28 05:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0e1cc05-db21-316a-a86e-83391bf77564 | -5.56682 | -46.28626 | 2024-09-28 05:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3bedb97-e81f-3f98-8df3-f02dfa229b45 | -5.56085 | -46.28556 | 2024-09-28 05:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa1148db-d2a3-3924-9ac2-175cc617f066 | -5.33 | -45.43222 | 2024-09-28 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acdec9de-2695-3ea9-b5df-805a70f5e935 | -5.09236 | -45.83504 | 2024-09-28 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e436484-0cbb-340b-86d0-4b844cc6b645 | -5.09168 | -45.83981 | 2024-09-28 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7277417e-38a0-3e7d-ac7f-867ef6562db5 | -5.19799 | -44.94739 | 2024-09-28 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e43fb591-004d-387a-84b0-2beca23c2ed1 | -5.19725 | -44.95266 | 2024-09-28 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b2b217e-e5fd-3a59-a73d-8b5a6b0a20f7 | -5.19235 | -44.94076 | 2024-09-28 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f03800b-f4ba-3ebb-9e3a-e4b97accc007 | -5.19156 | -44.94643 | 2024-09-28 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b97096b-78ee-39a5-b35a-e282446ef12a | -7.83426 | -45.48315 | 2024-09-28 05:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e50213e7-bda6-345c-a3ae-1ce56de2a156 | -7.8335 | -45.48066 | 2024-09-28 05:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51adabf4-b9f1-3ce0-8573-d3fb2818160d | -7.83287 | -45.48539 | 2024-09-28 05:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39e154d0-c84b-3112-b6f5-3886d9fce35a | -7.82781 | -45.48232 | 2024-09-28 05:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 15ba766d-38ee-3908-bae6-818528398b67 | -7.82708 | -45.47964 | 2024-09-28 05:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 907db5c2-48a8-3639-ad28-21b7d6750dbc | -7.82646 | -45.48425 | 2024-09-28 05:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 558c596b-267c-380f-ac2c-b7c968599f6c | -7.82688 | -45.54152 | 2024-09-28 05:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bccfc897-d299-3bb4-a799-55d107b820d8 | -7.81962 | -45.54734 | 2024-09-28 05:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2006f7e3-4dd5-34f5-8241-59a21e1779c9 | -7.74721 | -46.16738 | 2024-09-28 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbdc625d-535d-34fe-9880-b9a490c47c9b | -7.7466 | -46.17214 | 2024-09-28 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef647109-b19b-3d29-8365-c94650db5ad2 | -7.32787 | -46.68548 | 2024-09-28 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bef8baa8-bf31-3bf0-bac7-fa80403e2f7e | -7.32248 | -46.68061 | 2024-09-28 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01f1fd78-9525-3670-b1ac-ce68c4212397 | -7.32188 | -46.68502 | 2024-09-28 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cc01895-79b5-39ac-980f-c75630824f17 | -7.28868 | -46.14205 | 2024-09-28 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ff40463-6f28-3b29-91f8-4dbbf6446742 | -7.28804 | -46.14681 | 2024-09-28 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c82d5d2d-d759-3869-b347-5dab2954d79b | -7.26749 | -46.61359 | 2024-09-28 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af39777a-91d3-38d8-b325-00932a6167b9 | -7.26489 | -46.61249 | 2024-09-28 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f325b5c0-fe99-32cb-b104-9778d5e0f8f2 | -7.26433 | -46.61679 | 2024-09-28 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 615ec37b-20f9-3eb4-9b84-5e5d0d775a62 | -7.2615 | -46.61295 | 2024-09-28 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 81a10851-a854-3d87-a7db-29b0c4cb108c | -7.26091 | -46.61726 | 2024-09-28 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6bc59772-c0fc-31f6-84f9-f83c015c8a38 | -7.25889 | -46.612 | 2024-09-28 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44ab39b9-e1c8-3a5a-a5e4-b5cec732680e | -7.25834 | -46.61623 | 2024-09-28 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b33ff3fb-696d-3b3a-aff2-5a2b8a8a1056 | -7.14423 | -45.44271 | 2024-09-28 05:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9bc16f8d-4584-30db-b654-66bcec60fa53 | -7.03128 | -45.34877 | 2024-09-28 05:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61f130ad-ab44-36cf-8d18-34ca045c805a | -7.02549 | -45.34292 | 2024-09-28 05:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 27c55cee-54f2-32c3-9cbf-47681cec5dfc | -7.02482 | -45.34805 | 2024-09-28 05:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c903934e-0949-3727-bbca-0862f1bd9946 | -7.02389 | -45.3451 | 2024-09-28 05:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b6659cd5-0233-36b1-a8da-37ffd1c051f5 | -7.02319 | -45.35018 | 2024-09-28 05:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 29d316c0-0be5-3111-a1aa-b69e27d4fae1 | -7.01904 | -45.34215 | 2024-09-28 05:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93b73b0a-4f65-3556-af3e-75aeb2f9c475 | -7.01838 | -45.34726 | 2024-09-28 05:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ce83c8df-dab8-32a8-95f1-4388349310ba | -7.01746 | -45.34427 | 2024-09-28 05:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9f646f87-af88-3759-bbee-89fa4f3f84e3 | -6.5779 | -45.71534 | 2024-09-28 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d317ea3-6314-3e76-ad42-a584f0bc34c1 | -8.88281 | -45.65717 | 2024-09-28 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9920b1d4-9ac8-3c2a-b6f3-6d80ecba045f | -8.8764 | -45.65588 | 2024-09-28 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f4f5f7d-eb2b-3f80-b4b6-93b8bd432550 | -8.1213 | -46.79812 | 2024-09-28 05:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8ed5348-ce63-396b-b6fd-1aaffbde1d88 | -8.11536 | -46.79715 | 2024-09-28 05:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eef8cafd-33c7-3d29-a5ff-b06c27f629b8 | -1.7639 | -47.19132 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3135e981-ab5a-3820-9333-9f96343a371d | -1.7634 | -47.1946 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a99135f-9aa4-3704-ad49-0d7eee5f007d | -1.72664 | -47.12515 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| aa473c5c-2da3-3454-aedf-a6f718b90491 | -1.72612 | -47.12843 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 548e7c8b-6387-336a-a6f2-6272a9c82345 | -1.72561 | -47.13171 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4415e3a9-0d8a-35b2-8d34-7ff254d19ba0 | -1.72497 | -47.12504 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c0fd8f75-41ee-32db-bc0c-6c7671898003 | -1.72448 | -47.12833 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 8072197b-7d28-3b55-886f-615bc587b170 | -1.724 | -47.13162 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0b371a32-65af-3b4b-82f4-447141f697fd | -2.71936 | -46.72753 | 2024-09-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6930027-6b12-3ca6-95a8-036e4fac0a95 | -2.71881 | -46.73119 | 2024-09-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35e07aea-a72c-394e-b899-4d591fd5c108 | -2.71381 | -46.72675 | 2024-09-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README69.md)
