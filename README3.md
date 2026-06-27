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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed284d7d-41a8-3837-87f3-e2c250d20c65 | -12.6048 | -57.8743 | 2026-06-27 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| eda0bab7-45a7-34cb-8101-68ece65f774b | -7.755 | -44.1805 | 2026-06-27 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| a7154fc2-46e3-32ed-b7b1-6e7c7e9092fb | -11.9095 | -57.4134 | 2026-06-27 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 69b38b36-b10a-3f1a-b27b-6b9cf676ee58 | -5.7945 | -45.0586 | 2026-06-27 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| fc8adb25-33b9-3c23-932e-79f9a3a12f2a | -12.8165 | -44.3454 | 2026-06-27 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 9729c061-b44e-3a5a-89e2-fa42fa171933 | -10.5374 | -53.7094 | 2026-06-27 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| b20f80fd-ce19-330c-bff7-dc13566643ef | -5.7756 | -45.0826 | 2026-06-27 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| ca0e6514-2cb6-3f1d-991b-9719b653a431 | -12.6236 | -57.8926 | 2026-06-27 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 07df6115-5f4a-3d1a-93c3-da9a8ea66d2f | -5.7945 | -45.0586 | 2026-06-27 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ad238540-1384-3931-88ee-fb6bb84f344f | -11.9095 | -57.4134 | 2026-06-27 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 2cc1bb62-04e2-3f23-8fe6-a97bb7bd22a8 | -10.5634 | -46.2362 | 2026-06-27 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| d4f3cd17-2f2f-3f83-98e6-9a63b04e7e1d | -7.755 | -44.1805 | 2026-06-27 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| dabd5647-81ac-370a-95a4-3918321c02d4 | -10.6571 | -50.2212 | 2026-06-27 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 63a65cf9-5163-3822-8ad2-c31c30eea2ee | -12.4464 | -58.4825 | 2026-06-27 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 960b8cab-cfd1-38c7-bdba-48c6d2a50e69 | -12.6238 | -57.8727 | 2026-06-27 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 0fefba45-bbf1-3b75-916f-0334a8105b83 | -12.4462 | -58.5023 | 2026-06-27 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 5389bf1d-fae7-3f49-b8b9-404ac54f3c9b | -13.6671 | -53.9314 | 2026-06-27 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ce028e08-e5fa-3b9f-b1ca-8e1fe81c17e3 | -21.7626 | -56.2581 | 2026-06-27 00:30:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 34ad7f4c-55b4-3d3d-9cda-15a956746066 | -5.7758 | -45.0599 | 2026-06-27 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 795edef3-f657-39b3-889f-cef77ee259cd | -12.6236 | -57.8926 | 2026-06-27 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 58afca2b-cce4-3e7e-9aa3-a8ffaf5b912e | -10.6382 | -50.2232 | 2026-06-27 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| b02f1822-c9a3-3de7-92c2-a83b974f0fa9 | -10.563 | -46.2588 | 2026-06-27 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| a9000f1a-9581-3631-b66f-0e22dfb06116 | -12.8354 | -44.3657 | 2026-06-27 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 394f6525-b900-3739-a2ca-d6e26fb6c34d | -12.8359 | -44.3422 | 2026-06-27 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 9a859e67-766c-369b-a497-c43d88a24c8f | -21.7622 | -56.2795 | 2026-06-27 00:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 41.6 |
| fb6274a0-2855-372d-b1f1-55a3db12f514 | -12.4654 | -58.481 | 2026-06-27 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 18f5bcc5-f281-30b1-887c-e172cd964b6d | -12.6046 | -57.8942 | 2026-06-27 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 688569ad-ec0c-39dc-9f66-94e8374b784f | -7.7361 | -44.1823 | 2026-06-27 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ecb35206-8041-309d-abfd-8f9da9acac6a | -10.6385 | -50.2018 | 2026-06-27 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 1ca20080-7a14-37ec-88d2-f933828abfa8 | -5.7756 | -45.0826 | 2026-06-27 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 9a8dd7e9-11c9-3af9-a256-3e6443e910c2 | -12.4651 | -58.5009 | 2026-06-27 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| d111e4d2-ef5d-30e0-a300-5e13da00ecd4 | -10.6571 | -50.2212 | 2026-06-27 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 3d561682-1c7e-3574-89f4-54436b9dfdb7 | -12.4462 | -58.5023 | 2026-06-27 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 2de895b7-5a36-3e7d-b7c6-97c5dc6b93d4 | -12.8363 | -44.3186 | 2026-06-27 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| d187b9fb-6def-3177-850c-9d149a477e68 | -13.6671 | -53.9314 | 2026-06-27 00:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 7b1d717a-6d82-37d9-978f-0b9a802087b9 | -7.7361 | -44.1823 | 2026-06-27 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| c0e36ce4-458d-3544-8c41-006f586002e8 | -12.4651 | -58.5009 | 2026-06-27 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| e59f2a6c-dcab-3574-bae0-eacc5d35d572 | -12.4654 | -58.481 | 2026-06-27 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 6d5c271a-df3c-3a78-8dd2-def5bb577419 | -12.6238 | -57.8727 | 2026-06-27 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 1ecef722-5b99-3196-ad22-c9eb0c907301 | -5.7758 | -45.0599 | 2026-06-27 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 6630acab-8502-335e-8655-c0a10bbc5e7e | -12.8354 | -44.3657 | 2026-06-27 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| ce95eb6e-0e46-3508-9d33-f763180361e6 | -5.7756 | -45.0826 | 2026-06-27 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 04c89ec5-d763-3655-825f-71f64387b5ea | -10.6382 | -50.2232 | 2026-06-27 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 2f7b4af2-6a25-3486-9003-a7b914aeeced | -11.9095 | -57.4134 | 2026-06-27 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b5b616d6-f28c-3fcc-9ac8-f24b269d083d | -12.6046 | -57.8942 | 2026-06-27 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3caba8dc-85b1-3416-b208-a1f972607bd9 | -10.3557 | -50.1457 | 2026-06-27 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 72c10b85-92c3-3f25-a774-46e7e2c89585 | -5.7945 | -45.0586 | 2026-06-27 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0ff87796-ed11-3a23-a144-0a2f9e5011c8 | -10.6385 | -50.2018 | 2026-06-27 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4bd15737-b5c7-3306-babb-6d48d0dd4b8c | -12.4464 | -58.4825 | 2026-06-27 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 768b437e-9a0f-3791-8526-9fed66687cdc | -12.8359 | -44.3422 | 2026-06-27 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 221.1 |
| a1e0db2a-e188-3cb8-93e5-37e15966db29 | -12.8165 | -44.3454 | 2026-06-27 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| b9867aeb-8447-3ee0-acc5-74087006b3aa | -13.6668 | -53.9522 | 2026-06-27 00:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 54c61c77-2fc8-35af-95ae-d52f28c66508 | -12.6236 | -57.8926 | 2026-06-27 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 137.9 |
| f4885206-5a6a-3399-81da-a6388f1c03a1 | -12.6048 | -57.8743 | 2026-06-27 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 2e8a3f95-cd0b-3f91-976e-4cd4a2ef3fea | -13.6671 | -53.9314 | 2026-06-27 00:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 64856176-b2c5-380c-8ee9-7c7b73309329 | -12.6236 | -57.8926 | 2026-06-27 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| e9841309-516f-310a-a13c-3ceb83d339b9 | -10.6571 | -50.2212 | 2026-06-27 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f198788c-223c-3c5c-acd7-d6c02f3857ee | -11.9095 | -57.4134 | 2026-06-27 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0f59b825-e53b-39ad-9ea6-9bda3370b1f0 | -12.4654 | -58.481 | 2026-06-27 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 6beb455b-d509-3bd2-b3f3-342151bbba0c | -5.7756 | -45.0826 | 2026-06-27 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| cacdb414-30c9-381c-8a72-cde7d58de424 | -12.4651 | -58.5009 | 2026-06-27 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 894e8bfd-bf6d-3e9b-a1b2-0873e65f216a | -5.7945 | -45.0586 | 2026-06-27 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 70aa9438-114f-384a-9425-2e15e7a92c5b | -10.6382 | -50.2232 | 2026-06-27 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 05a4630e-4ca8-315e-8060-d0d2accb1d0e | -12.8359 | -44.3422 | 2026-06-27 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| eb57f248-aa25-3c2c-a123-9204cb7bc96c | -12.6238 | -57.8727 | 2026-06-27 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 61a72345-cef0-32ab-8682-86cd1abc9ecb | -12.8354 | -44.3657 | 2026-06-27 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 416d4475-3c32-3517-af42-b6f5bd576ce4 | -10.5634 | -46.2362 | 2026-06-27 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 7efe0914-3aaf-3140-9b90-4b57a30c7fde | -12.8165 | -44.3454 | 2026-06-27 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| d474fc37-7e31-31cf-b31d-6aa86f2e1c3c | -12.6046 | -57.8942 | 2026-06-27 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| aab3fa77-15d3-388a-85b0-cc2064c66216 | -12.6048 | -57.8743 | 2026-06-27 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| e529f54c-7b74-3338-9cc7-ecc19ea9d980 | -5.7758 | -45.0599 | 2026-06-27 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 24b86264-826d-327a-90df-e1d4669e3a28 | -7.7361 | -44.1823 | 2026-06-27 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 9544ae59-4240-3cb9-99d7-0d7f3c56162c | -10.6385 | -50.2018 | 2026-06-27 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 76d082ca-252d-3211-b705-bd77d23d2f71 | -13.6424 | -55.293098 | 2026-06-27 00:53:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c5d47f6-b238-3e52-8d9c-2c4302612ef8 | -10.6273 | -50.175098 | 2026-06-27 00:53:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0944e4b7-ad0d-3ea2-b18a-438c573bffde | -10.3032 | -57.135399 | 2026-06-27 00:53:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c0612f2-126b-3acd-afe4-8041e425c0ac | -13.2543 | -54.4048 | 2026-06-27 00:53:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e559262e-e521-3434-bc9d-c03eb936d10a | -13.6502 | -55.282101 | 2026-06-27 00:53:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7292dcc9-8512-3e02-b989-4653f3f9db5c | -12.6205 | -57.878502 | 2026-06-27 00:53:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 09c37a86-dfc0-3c7c-828c-3fb9987ed9a3 | -10.5318 | -53.707802 | 2026-06-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4df6690f-09bb-32d3-b30e-f62b0c166c22 | -13.6648 | -53.921398 | 2026-06-27 00:53:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1417def4-a6a9-3413-a0ea-96299380a9c2 | -12.795 | -54.8606 | 2026-06-27 00:53:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d9e3206-f446-39e9-8561-959375ec6fbf | -11.9137 | -57.404499 | 2026-06-27 00:53:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9fa7557-deea-3fab-b9c6-9bb202758fbc | -10.6228 | -50.197498 | 2026-06-27 00:53:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6b6c71c-76be-36f6-9d38-cde9ba3d10c5 | -13.6673 | -53.931599 | 2026-06-27 00:53:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fc4364ca-c703-3433-b24a-90928f612d99 | -12.9365 | -56.6465 | 2026-06-27 00:53:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7df917b7-4fc4-3c21-8a3c-850aaa5df476 | -10.6324 | -50.195 | 2026-06-27 00:53:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ccc79aed-75da-3a4b-9f62-947177d841d7 | -11.6434 | -54.886902 | 2026-06-27 00:53:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b58bc95-af81-37c3-bc04-758844120dce | -13.225 | -54.412102 | 2026-06-27 00:53:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d08f8dc3-2fa0-3a0a-94ce-37c87dbc9884 | -11.3227 | -54.4552 | 2026-06-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 006abe21-d58e-3258-8293-de5499f654b5 | -10.8991 | -56.855701 | 2026-06-27 00:53:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ebf691b-d0f2-33bc-a1a0-63baad76bf65 | -13.6522 | -55.290699 | 2026-06-27 00:53:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e2b63999-cab1-3050-b6b3-e035dc80a5ca | -12.6221 | -57.885601 | 2026-06-27 00:53:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| acdd8ec0-2ef5-309c-a7be-594090693a19 | -13.2445 | -54.4072 | 2026-06-27 00:53:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b38145b2-d780-3426-af06-c6e99871ddb4 | -12.0455 | -55.446499 | 2026-06-27 00:53:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 157a7395-32a4-34be-a7cb-f7f539068762 | -12.9312 | -56.623501 | 2026-06-27 00:53:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3d32b1e-1f0c-3ce9-a283-dc7f21bd60f8 | -9.0331 | -61.3269 | 2026-06-27 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4d133d2-d948-3cf9-8ef6-eeacb500fdc5 | -10.6279 | -50.2173 | 2026-06-27 00:53:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6c0aa13-3ed9-342f-aea9-d241e9b950e4 | -10.5415 | -53.705399 | 2026-06-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06de0415-51fc-3f41-a39e-502b6163c02a | -12.4578 | -58.4814 | 2026-06-27 00:53:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
