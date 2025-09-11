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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a089e6fc-8d2f-314c-a4a6-a84d88a8a544 | -11.4836 | -43.6875 | 2025-09-11 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 693ad36d-ee27-3c59-9211-767d91333e14 | -16.6335 | -49.7683 | 2025-09-11 14:30:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3c2af560-769c-362f-877e-ee76191987c5 | -9.976 | -50.3334 | 2025-09-11 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 213.4 |
| 5f8e5ef8-5cbe-32f7-a708-8f203de6d42a | -8.1103 | -49.2419 | 2025-09-11 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| ac4fd621-a361-3892-a022-27f18a2e472c | -10.6793 | -48.6415 | 2025-09-11 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| d30cbcbe-7325-3945-b0ba-e4a71b4bc0be | -15.8006 | -52.2687 | 2025-09-11 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 306.3 |
| 3a1f81d8-04a4-31fd-acb0-45f4f1c9f181 | -5.8582 | -44.2088 | 2025-09-11 14:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 65c9db99-3254-30d5-9b72-9e92c4ffe353 | -11.0959 | -51.3443 | 2025-09-11 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 316.8 |
| 1cd715ee-a4d6-3148-9584-1ffdbf0189e5 | -11.0997 | -48.4392 | 2025-09-11 14:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 23acc2ca-4dbc-33b9-b89e-2211ec6c063a | -15.1215 | -50.1219 | 2025-09-11 14:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 70cb24e3-f9a2-3721-aae5-0ea01c726e86 | -8.4315 | -47.3853 | 2025-09-11 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 9e67f039-5b90-33c4-8c5c-35c1213d871a | -11.702 | -46.5153 | 2025-09-11 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 213.0 |
| cbb49c56-f850-3416-8cee-5e72b80cea6c | -7.8708 | -45.5181 | 2025-09-11 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 0932de99-b625-3fde-8d77-9fc2905a530d | -5.7923 | -45.3078 | 2025-09-11 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| bf3eabe1-8c99-3767-bf50-85938c1c9bd2 | -14.5605 | -52.2049 | 2025-09-11 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| dda2a23f-d45d-3a9c-913b-4f90837d201f | -23.3545 | -47.2112 | 2025-09-11 14:30:00 | GOES-19 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.8 |
| 45dffb85-e562-3a77-9ebd-6dc7341a7059 | -15.8014 | -52.2258 | 2025-09-11 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1ed70733-da06-34e7-9d3f-894677e7f57b | -9.1331 | -46.9831 | 2025-09-11 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| eed6afbb-7569-3c09-aa03-b55438316ebb | -10.1657 | -46.1724 | 2025-09-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 79bf2c41-f043-36ae-bdc4-1905aacd35e0 | -6.1705 | -41.0658 | 2025-09-11 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| bb1b0824-91cc-3220-90ba-4f658068ccb8 | -15.0853 | -48.0467 | 2025-09-11 14:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 652beac6-adc1-32d8-9574-f3dcad8643d6 | -9.0265 | -49.5046 | 2025-09-11 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 96ce969c-6ccf-3463-bddd-79b5af793956 | -11.7215 | -46.49 | 2025-09-11 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 0842fed5-5add-3528-8619-4e68ba5333b1 | -9.5454 | -45.8389 | 2025-09-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| ca402fd9-88a9-35e6-a09c-1ce65edddb6b | -8.994 | -46.0808 | 2025-09-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 137.5 |
| acd8855b-9ea9-34ab-a545-4c77f4916963 | -10.8898 | -47.2494 | 2025-09-11 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| de4f1b4d-787a-3729-9d74-4689578f224a | -9.0547 | -45.7809 | 2025-09-11 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 2596525e-761d-3311-bd8e-9a82b9c221cd | -8.9752 | -46.0829 | 2025-09-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 3b855581-10de-3358-9cf6-92a6745e9fba | -9.0942 | -47.076 | 2025-09-11 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 4699465d-96d4-3b18-9e60-f3658933d334 | -10.3696 | -50.5283 | 2025-09-11 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 9ec641b6-4086-3d39-8f6a-67b3a51016a3 | -13.2606 | -51.7335 | 2025-09-11 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 309.2 |
| bfc18530-4081-3396-b852-c0d10cc2f294 | -10.1844 | -46.1927 | 2025-09-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 299.2 |
| b3a1e4b8-a00a-3bf6-b60e-ebafc9968758 | -10.6606 | -48.6218 | 2025-09-11 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 8b040f9c-cbf7-3919-bdaa-aeb5d34cafe9 | -5.642 | -45.4087 | 2025-09-11 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 676454c8-c646-3899-a4d8-37e5cec73e5a | -14.7527 | -60.2321 | 2025-09-11 14:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 5da134c0-7ade-3d20-9b7c-03c174f9b5c6 | -6.0746 | -43.1244 | 2025-09-11 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 77663800-af07-3f59-977e-e3c922edaacf | -11.4845 | -43.6402 | 2025-09-11 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 350360e6-c392-384d-a127-45c68fdd9642 | -9.0979 | -49.8194 | 2025-09-11 14:30:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 161.9 |
| a0a35115-bd3d-35d6-ab01-358cc6a79d3d | -9.1514 | -47.0257 | 2025-09-11 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| b61e54f1-0d0f-3266-a085-db295841dbfc | -17.3372 | -46.6718 | 2025-09-11 14:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 580f585e-147d-38ce-87d6-0ef65d3b7a86 | -13.2798 | -51.7312 | 2025-09-11 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 72da7433-234f-31ad-b8f4-8efa4c2dee95 | -7.4349 | -45.8519 | 2025-09-11 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| cf31c3dd-4639-38ad-a181-4069e07267af | -15.1049 | -48.0434 | 2025-09-11 14:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 0c87855e-9678-37ee-9058-6c95d48c588d | -6.2038 | -43.3475 | 2025-09-11 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 04028b88-b544-39a4-9aa2-03e0c7b60841 | -11.1685 | -45.3144 | 2025-09-11 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 859b8ffb-4d69-3b14-b3fd-2f91f6ebbfaf | -11.1689 | -45.2914 | 2025-09-11 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| ac7ddea0-3746-3a59-b460-4dc013d5fb28 | -15.1211 | -50.1438 | 2025-09-11 14:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 143.3 |
| ab32ea63-9cba-315d-83e8-70a2b4edf5ec | -6.4364 | -44.4847 | 2025-09-11 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 8b98a6d1-a788-3fc2-878b-8b71071694e0 | -9.0976 | -49.8408 | 2025-09-11 14:30:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 294.9 |
| b6638e0d-f425-3a59-b2cb-0b3d2935e960 | -11.7786 | -46.5047 | 2025-09-11 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 148.3 |
| f9c46d8a-df9c-3875-88a5-99e9e2d3098b | -11.077 | -51.3462 | 2025-09-11 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 219.5 |
| 27f36fce-1c4b-36c1-a468-58f4aaf934fa | -6.4848 | -45.2781 | 2025-09-11 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 319.8 |
| d41d500c-e2f2-3b52-b041-b3ee8a1a7201 | -15.1021 | -50.1249 | 2025-09-11 14:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 370e27ef-039e-3197-adfd-7b57fa795e33 | -15.1053 | -48.0209 | 2025-09-11 14:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 941ed0d5-0721-3d58-a2d4-92dc290d6405 | -9.0262 | -49.5261 | 2025-09-11 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 64e9c90b-d73a-3c34-b5cf-7d19b24c511a | -8.1101 | -49.2634 | 2025-09-11 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 1490bd3e-c058-3336-ba58-c6b66f026948 | -9.0565 | -47.08 | 2025-09-11 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 8e53b682-c3f1-3512-8179-d904f824b6ce | -6.4836 | -41.7373 | 2025-09-11 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| df9fc552-2130-337e-b78e-b744f0805b07 | -6.3041 | -53.4562 | 2025-09-11 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 8481a18f-657c-3811-938e-fba23a12715a | -10.7557 | -46.0987 | 2025-09-11 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 252.0 |
| 99a3086e-5767-3a32-8125-629c22557d3b | -9.0567 | -47.0577 | 2025-09-11 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 013bd5d6-a763-3bc0-93cd-950e30896bb0 | -7.4161 | -45.8536 | 2025-09-11 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 9b59becc-a5f1-3e75-94ed-4a61ca6ff1c4 | -10.203 | -46.213 | 2025-09-11 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 509755dc-1ebd-38bf-ab45-d4ba5db51926 | -14.7524 | -60.2519 | 2025-09-11 14:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9036c0c1-6530-3478-b14f-fee54928a21e | -6.2968 | -43.4331 | 2025-09-11 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 190f7719-641f-319c-a284-27055f743a32 | -11.7115 | -48.2536 | 2025-09-11 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 737c715b-86fe-3c7e-9e61-ef2fc3bab195 | -15.801 | -52.2472 | 2025-09-11 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 59f04229-200a-3ee5-98f3-07760f0f76d2 | -9.0129 | -46.0788 | 2025-09-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.2 |
| e8c5294c-eead-314e-b412-b93d04944035 | -11.7024 | -46.4927 | 2025-09-11 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| f7ec61ee-d8b3-3c9d-bc3d-f4fc3cecd449 | -9.7445 | -47.8468 | 2025-09-11 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 523a99aa-07c7-30ec-9af6-18eb75165f70 | -9.0361 | -45.7603 | 2025-09-11 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 58e82838-3689-30ad-baa8-18c3364da7d5 | -10.5482 | -49.8899 | 2025-09-11 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| bed6f6ef-6abf-3bb8-8ed2-18253565439d | -9.0745 | -45.7109 | 2025-09-11 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 31c1ec61-4530-337b-8bab-aeca390ee434 | -11.1 | -48.4172 | 2025-09-11 14:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| b85cb23d-c33e-3498-a59c-500a641037bb | -9.9026 | -50.17 | 2025-09-11 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 900528c3-6199-3fbf-90c5-1da8046d5d57 | -19.9994 | -47.6271 | 2025-09-11 14:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 225.6 |
| 6d2e16a8-8454-30dd-be53-0c37bd34bab6 | -12.1335 | -44.8508 | 2025-09-11 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 58c86b70-db7e-377a-99c9-0bf8556151cd | -9.4801 | -46.4545 | 2025-09-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 6f20734f-cd0a-35bc-a565-d7bf523d54b3 | -9.0605 | -49.8014 | 2025-09-11 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 94f8f1a9-9496-3b26-bf78-b41fdac0c279 | -22.6809 | -53.1309 | 2025-09-11 14:30:00 | GOES-19 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 129.2 |
| f5128d96-2779-3e06-a296-167a52cbd11e | -9.887 | -49.915 | 2025-09-11 14:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| f9c72242-1bba-3026-b7c0-ecb11ae13c57 | -6.3801 | -44.4893 | 2025-09-11 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 11c1d480-2631-3cb8-be90-a07db3b4c739 | -9.0793 | -49.7997 | 2025-09-11 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| d1b7df17-510d-39c6-be40-e6cc99bf12d0 | -10.0695 | -50.3881 | 2025-09-11 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| e0a512b5-bef3-3a80-826e-32d29f0c84a0 | -15.8703 | -54.9358 | 2025-09-11 14:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| ce4dd097-a56a-3f69-ae31-ee9dcaca584f | -11.1 | -48.4172 | 2025-09-11 14:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 495b6f5b-2efe-3b49-98ca-16ab3bae6284 | -6.5966 | -45.337 | 2025-09-11 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| c0f7b182-3ad9-3749-8f0a-c17d4f7f32f5 | -13.2798 | -51.7312 | 2025-09-11 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 969b0840-0ded-3d15-96f7-151f9a46e078 | -5.9193 | -45.7492 | 2025-09-11 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ed9e2cdf-7b0b-3e61-941c-7e05833d1f58 | -14.5612 | -52.1623 | 2025-09-11 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 767f9390-19ee-3949-ac7f-6769272cf0d5 | -7.4448 | -44.9678 | 2025-09-11 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 51d3d6f9-6248-3f25-9646-46c8943a6c05 | -11.429 | -43.5307 | 2025-09-11 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 2117778f-aadc-3553-a1bb-1dbfb2b56db3 | -5.7923 | -45.3078 | 2025-09-11 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| bc07ad55-c88d-34a9-8eb7-2ad7f6b43a11 | -9.9762 | -50.3121 | 2025-09-11 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 4eed2404-e80d-31f7-9b52-769d25104e02 | -12.9289 | -54.7744 | 2025-09-11 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 387df210-e83f-3ccc-b889-5dc8d9e411d6 | -13.0169 | -48.0103 | 2025-09-11 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 731e33e5-4653-3921-8a95-df128677a2a6 | -9.9026 | -50.17 | 2025-09-11 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 7961e89a-aea5-30c2-b338-dc179af4b425 | -10.1365 | -48.1993 | 2025-09-11 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 40154cd2-c980-3b3c-b840-af1798121ca7 | -15.1049 | -48.0434 | 2025-09-11 14:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 099f0c88-3269-3eff-b3c1-0c2d9d3e041c | -6.8525 | -47.8707 | 2025-09-11 14:40:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |


[Clique aqui para ver as próximas entradas](README149.md)
