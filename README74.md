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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d3662c1-3dc0-340d-bb65-29f4eebd2266 | -6.03673 | -57.80487 | 2026-08-19 12:34:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8ea69c06-f1d2-306b-9f9c-745615a41342 | -6.00064 | -57.85738 | 2026-08-19 12:34:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 4ba04704-25e0-3060-99ae-81580e2357e7 | -6.39656 | -51.7581 | 2026-08-19 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 24f10944-d364-30d2-87aa-99580f7d07bf | -5.49734 | -60.14104 | 2026-08-19 12:34:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cef3d070-e9e0-3144-b4b3-c4c6976f754d | -6.11056 | -57.73253 | 2026-08-19 12:34:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| de9cb733-65fa-3f30-b26c-500bd76a4fd2 | -6.80662 | -59.4538 | 2026-08-19 12:34:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8ddcf815-b3d1-36a6-bad2-d7bf55a282a4 | -6.85929 | -59.02648 | 2026-08-19 12:34:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ba585613-56b4-3055-afc4-c8262c4dc5bb | -5.14393 | -56.27855 | 2026-08-19 12:34:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e322e48f-07d9-3b5f-b775-174080d94d5a | -11.04814 | -51.0424 | 2026-08-19 12:34:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 34.0 |
| be131f95-d491-3097-9c25-70a0225bc853 | -6.14926 | -57.85388 | 2026-08-19 12:34:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 73b09aad-2df3-3496-b5aa-9d27bf545380 | -6.80791 | -59.44487 | 2026-08-19 12:34:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 24233a27-7a4d-3580-a898-a778f4ed2bb9 | -8.64983 | -62.82795 | 2026-08-19 12:34:00 | TERRA_M-T | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 47477254-3f13-3fdf-ab3e-c95f71eaef14 | -9.42399 | -60.42202 | 2026-08-19 12:34:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b3ee5433-13ae-3b8b-b1cf-a5241be33577 | -6.08374 | -57.92091 | 2026-08-19 12:34:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 80d03bc2-aca3-3189-bf92-27aa8006ddc1 | -6.0947 | -57.91936 | 2026-08-19 12:34:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f97e994d-0a70-398a-93c9-02834b48e449 | -6.99416 | -59.04282 | 2026-08-19 12:34:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8614d7fe-d611-3816-a576-cf4d72b22f88 | -6.09596 | -57.91041 | 2026-08-19 12:34:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| d3bc172b-7de6-3229-a346-cd777c3dc93f | -9.41992 | -60.44962 | 2026-08-19 12:34:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9f1a4cff-fde7-3c82-a986-5ed23a9399e7 | -8.50184 | -54.86871 | 2026-08-19 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 17d30206-6cdc-3115-b7bc-5cc273df7962 | -5.4329 | -48.3968 | 2026-08-19 12:34:00 | TERRA_M-T | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 02304c22-4a0b-3860-bf27-f82d8bdc1f6a | -8.21592 | -55.02908 | 2026-08-19 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 73a2d96f-9f53-3061-afa0-d65d993188c5 | -6.35393 | -54.8958 | 2026-08-19 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 77ff2bc5-9389-35da-be47-4fff86ca5d03 | -7.05471 | -59.83865 | 2026-08-19 12:34:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ce3f8441-1057-3b0d-974a-81bd532a57e1 | -8.50365 | -54.8551 | 2026-08-19 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8746c265-fceb-3ad2-b58f-fadc4f360e63 | -6.08501 | -57.91197 | 2026-08-19 12:34:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| d488ab12-40fc-3902-a57c-a45d82aaeac5 | -21.5343 | -52.0046 | 2026-08-19 12:40:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.8 |
| 9aca0fc8-e815-37d1-ad6a-9a513193bda8 | -8.5413 | -54.7389 | 2026-08-19 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 8cc55d45-9269-349d-87f1-c376701fa38d | -11.4036 | -47.2511 | 2026-08-19 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 2a666aa8-3707-3192-af56-bfdb4f7fb1c2 | -8.56 | -54.7377 | 2026-08-19 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| ae37b54d-a9ae-3eff-a026-55f2f7930009 | -14.221 | -52.9041 | 2026-08-19 12:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| e4fcd8d5-8ae2-32f3-845e-c3becb8c1042 | -6.0912 | -57.9187 | 2026-08-19 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| c61266cb-064c-3a6d-bfe1-834ad8e85f4b | -9.1078 | -46.046 | 2026-08-19 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| df22eb61-fcdf-32bb-adb3-37180ab52839 | -11.9319 | -49.9914 | 2026-08-19 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d93bb087-ff72-30db-9aeb-355ee88554da | -9.1078 | -46.046 | 2026-08-19 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 1027069e-6939-3632-99b0-3fcc7f74746c | -8.5785 | -54.7566 | 2026-08-19 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 4c038ba4-e79e-3e34-bbbf-a78d4b50d31f | -21.5343 | -52.0046 | 2026-08-19 12:50:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.6 |
| aa82a6ba-4c21-306d-94bb-739e57759ffb | -11.404 | -47.2287 | 2026-08-19 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ab65ead7-8926-31f0-a99a-4010661f190a | -8.56 | -54.7377 | 2026-08-19 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 24cc66f5-6b3d-32e8-86ce-457c3eed244b | -11.4036 | -47.2511 | 2026-08-19 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 7448baab-04ea-3d3b-9a77-279934b7d4b9 | -14.2017 | -52.9065 | 2026-08-19 12:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| a3a94376-5cc1-353f-9394-18cc4060bc18 | -11.0431 | -51.0535 | 2026-08-19 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 3d489137-7df4-3c8a-8421-cac36205b8f7 | -14.221 | -52.9041 | 2026-08-19 12:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 414bc6c5-daad-39e7-b3a5-d4db277c1993 | -6.0912 | -57.9187 | 2026-08-19 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 54448670-f7c7-3742-9b62-adea01a28dd1 | -8.5413 | -54.7389 | 2026-08-19 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 7c95d524-e9e8-3626-a8d2-be6f427f5120 | -9.1267 | -46.044 | 2026-08-19 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| b6404bbc-907a-375c-9084-90ce16ddc2ed | -15.1879 | -52.8427 | 2026-08-19 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| b29a77ae-cb2b-3a4c-a677-4688daad13b0 | -9.127 | -46.0214 | 2026-08-19 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 62321e93-20c2-32a0-aad1-390787bdcd91 | -8.5412 | -54.7591 | 2026-08-19 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| dc81c5e2-6d3c-3e64-81e3-302435c48510 | -10.7687 | -50.359 | 2026-08-19 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| f654b711-201f-31a4-b22f-96de6d121ce7 | -8.5413 | -54.7389 | 2026-08-19 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 26869767-840f-37c2-9fed-1329472bd0ff | -5.9274 | -49.2505 | 2026-08-19 13:00:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7b3e07c8-14d6-3dcc-9b6e-c73fdec83e52 | -21.5343 | -52.0046 | 2026-08-19 13:00:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 168.2 |
| 9ea062d8-d59f-3952-9b4e-1a0d6cd5d9bf | -8.56 | -54.7377 | 2026-08-19 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 12a47402-bd2d-3028-b7d3-5d069274990a | -9.7537 | -43.2962 | 2026-08-19 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 05fcb5db-ca8c-39e1-91c0-dd6856fd5e12 | -9.1267 | -46.044 | 2026-08-19 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 1af5af53-a0b5-327f-b08d-2b24bc700a0a | -6.0912 | -57.9187 | 2026-08-19 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 169.9 |
| f5d9b0f0-d2dc-352f-ba9f-f40e370fe1fb | -11.9319 | -49.9914 | 2026-08-19 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| d8644428-9290-3b00-9cbd-a649fb621bb3 | -16.5374 | -54.6831 | 2026-08-19 13:00:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 748e4c1c-7755-3aa6-8fb6-f2f64072aedb | -8.5785 | -54.7566 | 2026-08-19 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f73211e6-99bd-3523-9451-c7812879e09e | -9.1078 | -46.046 | 2026-08-19 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 3222fc64-bd2b-3000-b798-95c65f595faf | -14.2207 | -52.9252 | 2026-08-19 13:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| acfbc67e-5328-3720-a49b-30cdc60f7634 | -14.2213 | -52.883 | 2026-08-19 13:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 5692d63a-c661-3008-817f-b1c7327e49e4 | -14.221 | -52.9041 | 2026-08-19 13:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 34eca01f-2ecc-3ff0-9d3d-cfc181a364a2 | -8.5598 | -54.7579 | 2026-08-19 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 48d8ba57-b685-3389-af97-31cbd1b14d4e | -14.5272 | -53.0341 | 2026-08-19 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| bbccfe06-9d0c-3f46-aa08-9c75ed81216a | -9.7533 | -43.3199 | 2026-08-19 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 131.5 |
| 6dba1aaa-94a8-3b1e-9be1-a0679d467f67 | -8.503 | -54.8625 | 2026-08-19 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 6f812c7b-8c68-362d-98aa-692390e3a26c | -8.5785 | -54.7566 | 2026-08-19 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 187b2367-636b-3722-a73b-59bb76197354 | -9.7533 | -43.3199 | 2026-08-19 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 78.5 |
| ac29fd5e-059b-323b-a02c-1ea5292299bf | -5.9274 | -49.2505 | 2026-08-19 13:10:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 79cad8eb-93fa-3c1c-a413-cac57930fa0b | -5.9272 | -49.2719 | 2026-08-19 13:10:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| dfd01ff9-0f06-344e-bde8-72b9be97e532 | -6.0912 | -57.9187 | 2026-08-19 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 167.0 |
| 3bbcaf16-9b84-3f76-bf1d-aebea13f2c9b | -14.2017 | -52.9065 | 2026-08-19 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 8e00da1f-8082-3b02-b3ad-7a6df16dd5a3 | -8.5412 | -54.7591 | 2026-08-19 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 27074669-83b1-36a7-9996-cb7caac2db0f | -16.5374 | -54.6831 | 2026-08-19 13:10:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 2e089c43-80d7-352a-a8b9-66f17ed705f0 | -11.9319 | -49.9914 | 2026-08-19 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 906812db-3f05-3dba-8a21-5c3d7a9989c2 | -21.5343 | -52.0046 | 2026-08-19 13:10:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 146.5 |
| 954eb411-b963-3e83-8386-1532ec90ba5f | -8.5413 | -54.7389 | 2026-08-19 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 41fe6de9-7094-3180-bc2f-87b122619984 | -8.5598 | -54.7579 | 2026-08-19 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| e4edd8fe-96f7-3c53-84bd-21ce881a9299 | -9.7537 | -43.2962 | 2026-08-19 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 513af868-c160-3576-97b0-ac704b538cac | -8.503 | -54.8625 | 2026-08-19 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 88432185-63dd-3adc-a641-6acbf854e216 | -8.56 | -54.7377 | 2026-08-19 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 30720f0e-0b60-3916-86ed-e27c77c53450 | -8.5787 | -54.7364 | 2026-08-19 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7d54c6c4-55aa-3bfd-a6e8-ff343ff8e5e3 | -14.221 | -52.9041 | 2026-08-19 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| a3e4a9db-eaaf-3c89-975d-f169e78f4c4d | -5.4317 | -48.4212 | 2026-08-19 13:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 81e4e5b9-da7f-30eb-bc33-adb57db0c3cb | -7.4615 | -45.1484 | 2026-08-19 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 2e4f0102-b94e-30ac-9cbb-d8a297e79ee8 | -9.4366 | -48.2955 | 2026-08-19 13:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 610f9df5-d1fd-3406-858d-d23c2f17e16d | -15.1879 | -52.8427 | 2026-08-19 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6ba78417-f634-3192-b5d8-935fc3c88b9d | -14.2207 | -52.9252 | 2026-08-19 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 8ef15e7e-10fd-335b-bd0d-89f7c7eea142 | -15.3834 | -52.7528 | 2026-08-19 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| b2d120a0-1d51-3d4e-b49f-f1d35ebd3986 | -5.4317 | -48.4212 | 2026-08-19 13:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 25458d87-d6ff-32a9-81a4-3c8473475100 | -5.9274 | -49.2505 | 2026-08-19 13:20:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 1db5d8a3-7571-335c-b5b2-c5ca70a08ea3 | -14.5272 | -53.0341 | 2026-08-19 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ab14593f-6363-3bcf-8205-cb90691a831b | -6.0912 | -57.9187 | 2026-08-19 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 5ec13762-4e65-34fc-8709-16883dc0f177 | -14.2213 | -52.883 | 2026-08-19 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ed474509-9045-3c60-b3c8-5236a1a41e4d | -14.3529 | -51.9345 | 2026-08-19 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 78c73d94-ed68-35ea-b0fd-90efb504e40c | -15.1879 | -52.8427 | 2026-08-19 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 3822038d-04a3-3c54-8653-f0f007448046 | -14.221 | -52.9041 | 2026-08-19 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 3dd51e85-2ee0-3fca-8939-558a1bdd6843 | -8.3688 | -46.3473 | 2026-08-19 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| e6959999-3fd1-3d46-a431-144dc4f2473a | -14.2017 | -52.9065 | 2026-08-19 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |


[Clique aqui para ver as próximas entradas](README75.md)
