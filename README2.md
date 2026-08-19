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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3bbab35-c49a-3efb-bf71-dd6119c2bf1f | -8.36171 | -46.35683 | 2026-08-19 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ea744c3d-f27e-33b6-86fa-b984b8fb326e | -11.4877 | -45.11174 | 2026-08-19 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5e739b2b-d25c-3643-b245-a9438602a376 | -6.44248 | -52.74193 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| dae5c618-263f-39b6-a446-8e497672ef79 | -7.04258 | -59.84037 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 546dab04-e209-329f-87b8-cbf25d47e99d | -10.5169 | -50.787 | 2026-08-19 00:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 35456e4c-cd81-3574-9be0-0b22c99be100 | -14.3417 | -51.95329 | 2026-08-19 00:09:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2e9ecfcd-96f3-3c58-bc7a-8167b23614f9 | -9.07242 | -50.80832 | 2026-08-19 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1ff6a2b5-8b5e-39e4-baf4-53aa35520302 | -5.44044 | -48.42299 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 49d6ba68-0e1a-3b7f-895c-23c6ec2fe321 | -8.49212 | -50.93626 | 2026-08-19 00:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 406252db-45f5-3609-9c92-7f8c2a010c78 | -13.4138 | -43.87279 | 2026-08-19 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3063981f-a8d1-338d-baaf-4cb3b99420f6 | -6.89109 | -56.42715 | 2026-08-19 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f4ab8dc7-639f-3d9e-8025-305f7fdd9a33 | -13.29216 | -51.65173 | 2026-08-19 00:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4fd16f91-385f-314f-9f77-c5c9a5a011bd | -11.23058 | -55.07061 | 2026-08-19 00:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 064b2d15-76e6-34ec-bdd6-5943705b017e | -11.69383 | -54.56161 | 2026-08-19 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 37b45a95-f5bf-3c60-80f7-4f49baf730b2 | -8.58761 | -54.75346 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 3154541e-14c8-30e1-8df0-47e0d7ffea09 | -6.02104 | -50.20665 | 2026-08-19 00:09:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 451aad6b-422c-3a9f-9a1e-d0774bb4b364 | -6.84849 | -59.02587 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 6d20845c-74cb-3e59-90eb-9af48b0a187f | -10.77079 | -50.35884 | 2026-08-19 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 97e7aaac-37cf-3a26-aae4-faa588fd183d | -5.43068 | -48.4244 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 025a618a-6b59-3718-be26-dd544068618a | -10.93584 | -57.11412 | 2026-08-19 00:09:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| dded5379-db09-3957-a7d4-c58d750f0c13 | -5.4421 | -48.41632 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 019a7aab-1d79-3319-a98b-4a82c1c11e35 | -11.41589 | -47.2346 | 2026-08-19 00:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fe408f1b-54f6-3c6e-8a13-98d3852e647e | -11.21342 | -54.00495 | 2026-08-19 00:09:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 02ec685c-d312-327d-b1f2-7229ec8a0380 | -7.94829 | -44.65074 | 2026-08-19 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 36c16a88-56ab-3162-9827-573f3d6494ef | -5.41937 | -48.41479 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 577b5a11-cf69-3f71-8eee-5efe0383b16b | -8.54525 | -54.75908 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| b5ba1938-fdf0-33e1-86fb-aed676c039ba | -6.74497 | -59.0442 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 920aaff1-a010-3506-8da9-024902023d26 | -8.93953 | -47.60071 | 2026-08-19 00:09:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8f6d2008-3e8d-3080-89a2-59957810d082 | -5.92365 | -43.64161 | 2026-08-19 00:09:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 7c44c488-eb82-343d-b767-bc991db02e99 | -12.51836 | -47.83738 | 2026-08-19 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cd23760a-1c0f-3d59-81f1-9aa85a3cb7dc | -10.64694 | -51.61606 | 2026-08-19 00:09:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e00c8e0f-c2a9-3758-a0dc-b1f466068307 | -6.64914 | -56.43652 | 2026-08-19 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1da3ea6b-fc6b-305e-af94-1cbe932da029 | -6.79552 | -59.45258 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| b1994085-d1c4-336a-8a10-53883fea5b17 | -6.29027 | -43.63743 | 2026-08-19 00:09:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| b590dcb2-5166-33ea-9e43-532fe1082af6 | -6.4503 | -52.73123 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| f0863bcf-3593-3c27-8683-a9f92a65ccc7 | -9.09096 | -50.87806 | 2026-08-19 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5b2657d5-df69-30c2-92a5-f084796bcfe6 | -5.16942 | -48.16633 | 2026-08-19 00:09:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f81ac8a4-90d6-385c-b179-87b4c1f994f1 | -9.49554 | -51.67869 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c62e007f-db89-3123-904b-671300ad4ba4 | -11.4175 | -47.24559 | 2026-08-19 00:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ed9fe9b1-1a54-3f29-95cc-5d70c15417f1 | -11.08212 | -47.60764 | 2026-08-19 00:09:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 386e5b3c-34d6-33be-9d5b-d63017d380b7 | -9.59478 | -49.32334 | 2026-08-19 00:09:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| f3b45bfd-8a1e-3049-9ca4-1c27f7aae4e6 | -6.44904 | -52.72181 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| fad58fae-eaa3-31d7-afdd-c62431ec22a3 | -11.23243 | -55.08599 | 2026-08-19 00:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| f25ea45a-8daa-3277-88c7-cef244ee2a9b | -5.79208 | -43.9263 | 2026-08-19 00:09:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 8ce3b2b3-180a-3350-af49-a5e702be2a8d | -6.409 | -46.63424 | 2026-08-19 00:09:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3d5ab569-d600-3c39-9bf2-7b4026a40cdf | -9.47916 | -51.63054 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 156e2fe4-5a57-3c73-aae6-416ec258b301 | -8.54025 | -54.71981 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| fe628e2e-8606-3bb5-9480-b90a1e17d20f | -9.01432 | -60.52676 | 2026-08-19 00:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 045436d0-a815-3f20-bb18-2e4572a705c0 | -8.5664 | -54.7561 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 32e43084-84aa-3365-bbdb-f8cce2dccf50 | -6.88458 | -59.07602 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 1cbbbfbd-d6c8-396a-94d9-dc27970bc505 | -11.71391 | -54.6319 | 2026-08-19 00:09:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8a4c0540-77a5-33f6-8185-5f4fc717bf16 | -7.28268 | -44.07741 | 2026-08-19 00:09:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 5c5e2be8-9dc8-36d3-af34-b20c5e9d1a5c | -7.24172 | -49.89947 | 2026-08-19 00:09:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1664069f-4774-3686-943e-2a87d8124f39 | -6.8793 | -56.42862 | 2026-08-19 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| f0cd23a8-5d78-3ef4-b18e-efb7d3cf009d | -6.81056 | -59.45056 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 5084845d-1d0c-3382-84ba-16a6b7c37b1c | -8.51015 | -54.86407 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| cc7b5ff1-4526-3f18-8e8a-759646308335 | -15.07468 | -45.33363 | 2026-08-19 00:09:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c995a376-9532-3e7e-affd-fe2cf797e2e9 | -8.359 | -46.36308 | 2026-08-19 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| caeffd19-5a56-3cda-bfa1-99bb0a04ddab | -6.88114 | -59.04941 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 0d5f124e-4335-3be3-9845-4eb151dfefa7 | -10.12361 | -52.11251 | 2026-08-19 00:09:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 18510b4e-613f-3796-8549-cda78347da53 | -9.46643 | -51.60403 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9dedb273-a479-3871-8707-773b1d0a2eb0 | -8.57913 | -54.6885 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| bd51b107-306e-3401-83c6-25694307e519 | -13.58311 | -51.69591 | 2026-08-19 00:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2927f2b6-55b8-32d7-a696-ba9c89f31ff7 | -8.54693 | -54.77231 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| eb07b837-4afb-358f-b14d-e506e226a3ae | -6.27701 | -43.27689 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8e0e6dd8-0926-349e-999b-c22c3ad23bf3 | -7.94526 | -44.63135 | 2026-08-19 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 1ccb1fe8-e3ec-3bb9-b2af-678eb3cb7ca3 | -6.01743 | -49.91827 | 2026-08-19 00:09:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fda5267b-a493-3c87-b6a7-7a52dbaeadfc | -6.34163 | -54.92262 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5275daf1-dd98-3a95-a6ee-6d48cc3d86ca | -8.4909 | -50.92741 | 2026-08-19 00:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| a98f41f8-1c72-38e7-bd0d-196f7d7d7588 | -7.05819 | -59.83876 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 3ac557f6-b4f8-30ee-a4dd-4e49bd9b61fe | -6.36073 | -54.90734 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ef152b9e-89b1-3daf-8448-b266bb1dd202 | -8.58422 | -54.72748 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| dd61b179-4379-36da-b878-466ea7e72709 | -10.28834 | -48.22992 | 2026-08-19 00:09:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e5c2f6e7-67d0-37ec-b269-b37307551a71 | -11.32096 | -45.22403 | 2026-08-19 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| ce3fa824-dcca-31df-adfe-d96e2a77c678 | -9.9929 | -53.95291 | 2026-08-19 00:09:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d1ceb5c2-963f-38a7-9326-1a9eb4188363 | -6.28557 | -43.64383 | 2026-08-19 00:09:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2083a23e-593e-3676-b985-4671ee545927 | -10.19166 | -54.24394 | 2026-08-19 00:09:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9761b1eb-8732-3c03-bd00-a98a571ad971 | -8.56858 | -54.6898 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c9cb315d-3f31-3548-986c-0da73a6ba2e5 | -8.56473 | -54.74313 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a83b5009-5b81-3acc-94e4-0d57fb84375e | -6.39239 | -51.7571 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b142a337-054f-3f8c-acb7-2ee5d258f7fc | -6.68856 | -59.08488 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 9e45d24a-3bae-3fb1-b183-d9d11673e168 | -6.85021 | -59.0189 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| bedefe03-6b82-3ba3-b5c8-8414d31dc637 | -6.44121 | -52.73249 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fe2ae22f-0d55-30cc-a608-564c189a9989 | -12.24787 | -43.16505 | 2026-08-19 00:09:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 83f3646b-311d-3262-af9f-00feb5b88baa | -14.46528 | -45.63641 | 2026-08-19 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| aeffd043-c36b-3382-ac01-0fca6dac1ef9 | -9.00996 | -60.4893 | 2026-08-19 00:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| fdff4eec-2cb9-33be-bc78-680d8b88b348 | -6.87716 | -56.41221 | 2026-08-19 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7f36c88c-70d1-3f92-a32c-ad2fde18bd52 | -8.58933 | -54.76664 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 8c3d9ad6-4571-3c00-af26-b16cec4595be | -5.91594 | -49.25602 | 2026-08-19 00:09:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 338a4cbb-076c-356a-bcca-ff0e39b8be8c | -14.34036 | -51.94272 | 2026-08-19 00:09:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6a4bdc2d-37bc-3099-814e-d6f0eb470a87 | -6.34003 | -54.91018 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| c73cd393-7b18-3430-a9af-0ecb0deab499 | -9.40712 | -60.60917 | 2026-08-19 00:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 6abc8bf4-4aed-3df4-a23e-1c809c9f8d7f | -8.54192 | -54.73294 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 755d3a1a-6edf-3680-bfae-65e33f290471 | -6.86653 | -59.05116 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 70a89ac2-b4f7-3c0f-aad8-28ebf3f04c3f | -8.54358 | -54.74599 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| c6756b7c-859f-3222-8e89-d60c86e788c4 | -6.86308 | -59.02429 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 5d84fa65-979c-3b7a-a6a4-9da19132b651 | -12.37553 | -46.45066 | 2026-08-19 00:09:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 13299793-2cc6-3f38-b350-abf9d883555c | -6.30386 | -55.88663 | 2026-08-19 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 6e9de70c-8a3d-3b3d-9989-607626fcf752 | -11.06176 | -46.51245 | 2026-08-19 00:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 5a822a8e-cdee-3928-977b-445f19d4109c | -5.66308 | -43.57963 | 2026-08-19 00:09:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |


[Clique aqui para ver as próximas entradas](README3.md)
