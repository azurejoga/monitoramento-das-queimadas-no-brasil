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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d818c08b-2c68-3700-9fad-bbbcab54c45b | -2.94152 | -57.71574 | 2026-09-29 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8af81972-5e9e-3380-a99d-a53189e0a2f9 | -3.01009 | -54.21832 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0bfb124-6ef0-35d7-a04c-20d6b6ddaf37 | -6.15134 | -52.90646 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d149d70d-f990-35fe-ad50-03f35333eb22 | -8.23815 | -45.44059 | 2026-09-29 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4051565e-a8cc-309a-ae91-47776cf04e48 | -7.69649 | -48.86395 | 2026-09-29 05:10:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ec8bef50-52ec-353f-b045-eea230ed8749 | -2.56747 | -54.26754 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ebc2db3-c45f-3333-8d4d-a1edba9fe528 | -3.71068 | -54.22998 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 79eabd99-fa3a-3e3c-9762-b16fbb640755 | -7.46889 | -45.80698 | 2026-09-29 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4075233d-5dd4-30d1-9ab7-150e5b617d53 | -4.4958 | -49.64653 | 2026-09-29 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d47c97ee-cf54-3cb9-8e24-556c3f731457 | -1.0642 | -50.60785 | 2026-09-29 05:10:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13a37eed-6206-38e1-a455-d91479c14f9e | -1.04809 | -53.56392 | 2026-09-29 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4a0ccf7b-7022-3432-b5be-4b9eaa2b3261 | -3.2296 | -52.22957 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0dfdbbf-8493-359c-a38d-856b2fe14484 | -3.81684 | -55.90336 | 2026-09-29 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72a4fcb1-18c4-3c66-90f7-deff666fb90b | -3.02389 | -53.86943 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f4e665e-9b0d-3ae5-9f2a-78659e7f95d9 | -6.2009 | -52.90835 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eac6be1a-1ceb-3513-b82f-3cee64791e0e | -6.09729 | -57.63476 | 2026-09-29 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6928fc4c-53bf-3ee2-a50b-9802e5fa5fee | -7.67921 | -44.89416 | 2026-09-29 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30237ab1-97f7-3a65-9db3-56227350a9fd | -6.30222 | -43.60667 | 2026-09-29 05:10:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7089f2c7-7bf6-3b1e-a859-15fa7b67f300 | -6.31471 | -52.6249 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 12175b5b-02ae-3c99-84e8-8ab65cfff2d5 | -6.16387 | -57.69812 | 2026-09-29 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 014058da-d81f-31f5-9962-a17b8913d975 | -6.51609 | -54.96131 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4403012f-6cb9-3a00-9fbc-f864da123a8f | -5.72502 | -53.46473 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ec57c27-7f28-3f9b-9c97-829645c11768 | -6.30624 | -56.03658 | 2026-09-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a13a533-52ef-33f7-912b-08d6c4442a10 | -5.43981 | -47.27183 | 2026-09-29 05:10:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab10cd29-6cd7-3acb-bcdb-2c40f19de6c8 | -3.2685 | -54.00223 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33c9c2ab-ec3d-3a76-a726-dd6f4b0885cf | -5.30339 | -55.82788 | 2026-09-29 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6b2a64b-e3af-37ae-a158-3b70903eee58 | -7.99689 | -43.26503 | 2026-09-29 05:10:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f6da4f3b-04c0-35df-b66c-106ea20d00c3 | -7.47891 | -45.82021 | 2026-09-29 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e7b3108-6686-39e0-b468-f50b4bf4c073 | -2.89499 | -54.08496 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 522f0196-4e4f-34fe-a656-8eb202d79a2e | -7.01112 | -45.30392 | 2026-09-29 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e690992-98b6-3f60-80e4-5d69115554ba | -6.30884 | -43.60719 | 2026-09-29 05:10:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c3874e9d-48d0-3b79-b832-c83d2753c2d4 | -7.53985 | -47.12204 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5cdf881-d2e2-3b50-acb9-1a555fe03b59 | -7.82806 | -45.8177 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ef491929-9957-3ae9-a41e-544ef790c3af | -4.49914 | -49.64536 | 2026-09-29 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 132e2946-4a9f-35ea-81ab-0827ec58b163 | -7.0866 | -46.71234 | 2026-09-29 05:10:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61b84f86-279e-3857-a809-0c651262019b | -6.30017 | -56.03208 | 2026-09-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 65971995-913c-3bb7-a03b-2651beeb5e2a | -6.09389 | -57.63421 | 2026-09-29 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c41f48eb-c2d8-3b4c-b6a1-251dc29c5a31 | -5.48629 | -45.12951 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7498c0fc-f380-339d-84c1-a1f6aad1e83b | -2.9252 | -57.66138 | 2026-09-29 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb6e2c55-acac-3744-9f97-388c384d7a47 | -5.30394 | -55.82443 | 2026-09-29 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 546e220b-7ab0-391d-94ba-199a299d57f6 | -3.71012 | -54.2335 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b5c362d-3ecc-37ae-86aa-86089a649c78 | -5.36535 | -46.22408 | 2026-09-29 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7598bc6-acc3-3195-91f5-7678e31bd1ef | -3.15674 | -54.0861 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 996e3bb0-1a98-30f2-a7d8-c8ff6a64527c | -6.09789 | -57.63109 | 2026-09-29 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f42a0b81-a4b2-3c06-8001-0bc097f1b627 | -3.01398 | -54.21534 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9d6a0fe-9056-3b42-bdca-917abbd2080c | -3.04688 | -46.9283 | 2026-09-29 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5860af94-5a4e-35ae-b6bc-fdc59bd90d39 | -5.19475 | -46.07923 | 2026-09-29 05:10:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2e67030b-ea50-33cf-8ee7-56e9f8259567 | -7.26102 | -45.34351 | 2026-09-29 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bede4af6-2e46-3372-bebe-255df18ba943 | -3.0893 | -57.65147 | 2026-09-29 05:10:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 091e23bd-16e1-353c-9fe7-29cc1ebe3983 | -2.89505 | -54.17136 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44b6a542-c9ce-3903-8221-184b183a45ab | -8.35633 | -45.39737 | 2026-09-29 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e25ef135-1843-3382-bb64-5d22e4d2439b | -2.43666 | -54.70818 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78ad7acf-3fc9-3f30-baf0-3f6b393a3f54 | -2.90169 | -54.10764 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 311db550-a34b-3203-8648-9702403c577c | -8.35581 | -45.40138 | 2026-09-29 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 235750fd-a25c-35a8-8d19-cfc18e4b4659 | -2.89834 | -54.10712 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e6b0179-e4d3-372f-8e01-30cedee52608 | -6.16328 | -57.70179 | 2026-09-29 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4eef176-143c-3b4b-90f2-7de7c65a8019 | -3.71233 | -54.21941 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a8fe648-4bee-3848-abe3-2530b2961641 | -3.57265 | -54.35257 | 2026-09-29 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8eeda4bc-6743-3b2b-9d77-d607d8d78d7f | -4.71758 | -50.64045 | 2026-09-29 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db6a30b3-9d7d-39f0-920a-a3afa149754e | -5.61196 | -44.99738 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 97ddf2cc-d3e4-3e45-b40a-aa05a4a36151 | -3.18605 | -57.83755 | 2026-09-29 05:10:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 152bdcc2-8b44-3d4f-bd3a-f08f1c1dbcd8 | -5.73941 | -45.17327 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5363fe7d-15ee-3f8a-bb5a-f542e455a950 | -1.32347 | -55.34297 | 2026-09-29 05:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80906981-7d31-3f1e-92fb-d5e90db882c0 | -4.81379 | -45.63804 | 2026-09-29 05:10:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba0d689f-b708-3e9a-b22f-4138cfdd2b58 | -3.00898 | -54.22534 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 605c7202-c57d-358e-9a0f-7452b64977ff | -6.30348 | -56.0326 | 2026-09-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a2a84c53-b5c4-3943-9cb9-c08d460033bc | -5.48873 | -45.31238 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 346a67ae-78ed-3f4e-9e82-3b4a49c2ede8 | -3.14836 | -54.09568 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb85f155-58ff-34ee-95d6-02195e08b816 | -5.60537 | -45.00089 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 366a8dd8-3a7e-375f-8c94-4f31d978f3b6 | -6.31313 | -43.6152 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ba4cbb8-cc5d-3b38-b013-1b21e1f39abd | -6.16146 | -52.91217 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc86a3f6-6568-3c9d-b14e-ce73b8a97417 | -4.31859 | -48.6328 | 2026-09-29 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d139188-5859-3031-80fc-55229f120c18 | -3.48654 | -54.72781 | 2026-09-29 05:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e66a6f4-3960-38c0-87fc-a5e1de851c72 | -5.73825 | -45.18151 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 37ec957c-f5c0-319a-afac-836b9c889ef6 | -5.60819 | -45.00457 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 691ec6d1-8446-339d-9b75-8330ee40fc8c | -3.71288 | -54.21588 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a136b66d-694a-3b21-99b7-7967d041b7da | -2.86885 | -54.12054 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a679e3b9-fab9-358b-992f-f19eff6782d9 | -6.29598 | -43.65184 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4b7db3b5-e14b-3147-ad12-63579b5a00a5 | -7.53805 | -47.12199 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f9a0172-5b06-3540-898c-3ea03f92484d | -7.27594 | -46.7953 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2508d450-9a98-3686-a81f-3d5f123a7e2a | -2.91787 | -54.20006 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 125f47ce-078c-3412-b9ca-8c32efb07373 | -1.99451 | -47.63175 | 2026-09-29 05:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8a15bc8-50b8-3d40-99f1-aab184446999 | -5.60878 | -45.00029 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4df9d95b-b4bc-3db6-9dba-b0a93509941f | -6.67342 | -55.10858 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af313160-7aa6-37de-9e60-1e0b84b299f3 | -3.70564 | -54.21837 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7150de5b-69fc-3007-bf3f-e11373f615a2 | -4.32362 | -48.63112 | 2026-09-29 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49dc187c-80bc-320d-a70b-0fe817a68fd8 | -3.82678 | -55.90493 | 2026-09-29 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b80030b1-9fdc-380e-8be9-65359fc55288 | -6.99379 | -45.3419 | 2026-09-29 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6cb8c3d-d5a6-3120-9aa4-1ac6ef56defe | -3.70508 | -54.2219 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3251c6f8-b787-3f63-a503-06ba979b7fb5 | -3.14725 | -54.08103 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b5f775f-8fe1-3bfc-9ff3-01e3083ceade | -5.08937 | -44.84381 | 2026-09-29 05:10:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ff67566-195d-358f-9662-5fb02b03e360 | -5.48933 | -45.30815 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dedd0671-95be-3f74-9369-ff8d51ed65f6 | -3.71178 | -54.22293 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dbee50c-1727-3a1b-8977-459a84db147e | -6.12558 | -43.73323 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98f7a09d-2174-39f3-ae4d-3c82d7ad5be3 | -6.30079 | -43.60741 | 2026-09-29 05:10:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 383d08c7-b9ec-3512-818c-b85ae689c8dd | -3.53777 | -48.1797 | 2026-09-29 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87d77375-1ea6-356a-bb54-a5d204e28e9c | -4.32316 | -48.63349 | 2026-09-29 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e0c44f3-f495-3f05-906e-1932f5caeb46 | -2.98296 | -54.53893 | 2026-09-29 05:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d6c9fb8-df67-3817-b44e-9eb26b99a22e | -6.32136 | -52.63025 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80961dd7-adbb-37dd-bbe7-dcdec31bcb7c | -2.57358 | -54.7438 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README58.md)
