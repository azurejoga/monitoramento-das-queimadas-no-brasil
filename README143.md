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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffcd6342-a6b7-3a3a-8052-0cf9206c25f4 | -11.4285 | -43.5544 | 2025-09-11 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 892403a6-24c7-3d2b-bae7-122ce216ae87 | -6.3226 | -53.4553 | 2025-09-11 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| acaac3b8-3529-3dc8-a7f2-2dbd194fd8b9 | -8.1103 | -49.2419 | 2025-09-11 13:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| e563f1f9-6aa4-3b85-960f-0505d63c261e | -6.8374 | -45.6108 | 2025-09-11 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| f8e9543f-bd98-3dcc-be23-3b98df136118 | -10.7362 | -46.1238 | 2025-09-11 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| ea1683e1-2c2c-3679-848e-975a5dc76d4a | -12.5796 | -44.6412 | 2025-09-11 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| edc0a9f9-a288-3383-a3c2-f8a6898e909b | -9.4801 | -46.4545 | 2025-09-11 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 358.1 |
| 111eb499-d1c1-3fca-a075-b592fc509415 | -6.9319 | -45.5352 | 2025-09-11 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| d8dd5a85-14f9-3863-9aa6-160ef438cd7f | -8.1649 | -46.0983 | 2025-09-11 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d601c037-84c1-3b58-97a5-adc5780b8a49 | -6.8187 | -45.6123 | 2025-09-11 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 464faf9e-4f2c-3d54-bc7a-0b10887d2237 | -15.1759 | -52.4199 | 2025-09-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 2a09a87e-6093-34ef-b994-78eb41fb3362 | -13.49 | -51.7688 | 2025-09-11 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 507bb611-772c-3fb7-ae2c-ac7d9fba8166 | -11.0959 | -51.3443 | 2025-09-11 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 7c89affb-4cf1-3eca-8c7e-f4363fda2270 | -9.0567 | -47.0577 | 2025-09-11 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 42d276dc-87d2-331c-9181-dba8cccbe0c1 | -9.0074 | -49.5278 | 2025-09-11 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| a3e80507-0f6a-3252-951c-3cf88f18a3a8 | -15.6929 | -47.0354 | 2025-09-11 13:50:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 6c18dcce-31c8-335b-81ad-3d31c85e111d | -10.7557 | -46.0987 | 2025-09-11 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 558.6 |
| d3a3c9c3-fed8-3f7c-bda8-f17e3ebe74e5 | -10.5671 | -47.2442 | 2025-09-11 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 340.2 |
| 48db1f96-4d67-3320-87c5-988107ba3ead | -9.0753 | -47.078 | 2025-09-11 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 3e5bc6ad-6632-3f6a-a4a8-773d170cef90 | -8.994 | -46.0808 | 2025-09-11 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 369275b7-da38-3c77-88e3-267b5bedc001 | -9.7634 | -47.8447 | 2025-09-11 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 45649253-666b-335b-8f3e-cf9487004bc2 | -6.3737 | -45.1509 | 2025-09-11 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 65c35c0b-c69b-3932-91e7-9417997e04bd | -11.0997 | -48.4392 | 2025-09-11 13:50:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 37b38f7e-4ba4-345b-8d21-7575cff25b6a | -6.3735 | -45.1736 | 2025-09-11 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 01239833-d927-38a6-bb56-9d084735855a | -14.4464 | -53.2544 | 2025-09-11 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| f12b6cc6-97e9-327f-b55c-9b3f64e9fdb1 | -7.1721 | -44.1444 | 2025-09-11 13:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| dfe64542-6a27-312d-9b29-048edcd14fae | -9.7445 | -47.8468 | 2025-09-11 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| aa114250-3b77-36c9-b929-31ee83295500 | -15.6732 | -47.0389 | 2025-09-11 13:50:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 207.9 |
| ac2d5eb5-5bf3-3f26-8ee9-df5ca73d87a5 | -9.9004 | -51.8811 | 2025-09-11 13:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 19dbc504-b599-38bb-bcc0-41a79b19eace | -10.6793 | -48.6415 | 2025-09-11 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 270.3 |
| d4d38db2-7f31-37ad-9dab-040e34d960de | -10.203 | -46.213 | 2025-09-11 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 39eee49a-8c50-3043-b3d4-d7ce4640ec46 | -9.1514 | -47.0257 | 2025-09-11 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 4b275947-4ee6-3e07-b9f2-c29ae4f44309 | -15.6536 | -47.0425 | 2025-09-11 13:50:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c9c7b32c-2ca5-3977-8c80-7dc9de60477b | -15.1371 | -52.4252 | 2025-09-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 4cb2314e-5119-3f9e-b358-85757bdb6b50 | -11.0962 | -51.3231 | 2025-09-11 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 32782a87-99d7-3722-bcae-74cd2b6334cf | -9.4804 | -46.4321 | 2025-09-11 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| adb196a6-efcb-3e6c-97dc-6570782d422c | -10.6796 | -48.6196 | 2025-09-11 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 228.7 |
| 38194f01-e514-3269-bf4f-5e9329bf6aba | -9.887 | -49.915 | 2025-09-11 13:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3995744f-616d-31cc-ac01-71a8994fb507 | -8.1101 | -49.2634 | 2025-09-11 13:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 88fee614-f9f2-3d8c-85db-cbd90f6abb55 | -10.9536 | -46.8168 | 2025-09-11 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 5837f874-fb7c-3419-847c-ed9f3a45e8d4 | -9.4571 | -46.7479 | 2025-09-11 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 0604750f-c339-3f07-a45c-8c63afc199b8 | -10.7366 | -46.1011 | 2025-09-11 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 7225faf7-1dab-36b1-b5b2-3c093fa147bd | -15.1012 | -50.1687 | 2025-09-11 13:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 213.6 |
| 46796d78-031b-3680-bac4-aabefcb3e597 | -6.4645 | -41.7631 | 2025-09-11 13:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 2622c4f7-b43e-3370-939c-0b5f7d6f2f9d | -11.1685 | -45.3144 | 2025-09-11 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3e7bfaa5-9bd9-3895-aa18-87aaf0b523e1 | -15.1021 | -50.1249 | 2025-09-11 13:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 35a694b7-2233-3a9c-9b50-f991effee457 | -6.4833 | -41.7613 | 2025-09-11 13:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 8b342be8-d4d6-3d9a-82b6-7295ec6b2e1c | -6.8374 | -45.6108 | 2025-09-11 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 1c3ef634-d256-3013-b139-1c55c6fe06d6 | -6.2226 | -43.3459 | 2025-09-11 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| f5afbddd-8ed3-3236-83bb-89564beb7185 | -15.1016 | -50.1468 | 2025-09-11 13:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 71c8caf6-2959-31b7-8394-c3c393ec679d | -15.1367 | -52.4466 | 2025-09-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 81fec9a0-ab1b-3d7f-a6f2-59a7f7346602 | -16.6335 | -49.7683 | 2025-09-11 13:50:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| c1673ece-88c8-3af2-a454-a936bcac56ac | -6.3226 | -53.4553 | 2025-09-11 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 11e3e088-c7b3-368e-af23-9bf67bbd27a6 | -10.7362 | -46.1238 | 2025-09-11 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| b6e77f84-3249-3089-b558-b37af783ddd2 | -9.4797 | -46.477 | 2025-09-11 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 211.7 |
| 430a2701-42ae-319b-af7a-1b60afa9991e | -11.7211 | -46.5127 | 2025-09-11 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 07aebea4-6a95-3c8f-9bb2-ef868730e1e8 | -5.9193 | -45.7492 | 2025-09-11 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 357b46be-2665-35fc-8bf1-2a678cf88f03 | -22.9611 | -49.762 | 2025-09-11 13:50:00 | GOES-19 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 173.6 |
| 0638b7bb-7215-3e56-b4b3-09ef4472a6e9 | -15.1557 | -52.4652 | 2025-09-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| c568bcb3-4e02-35ae-84b2-f61dc1d5b1e1 | -15.8014 | -52.2258 | 2025-09-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 31f0e98b-2ca9-3d62-a2c6-af1ee26070a8 | -6.5038 | -45.2539 | 2025-09-11 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ac7f0bb2-4c8e-310c-b341-1eeab11ab499 | -8.1103 | -49.2419 | 2025-09-11 13:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 99f7bb6c-0b80-3a67-bdf1-0bea00fa00f8 | -9.057 | -47.0355 | 2025-09-11 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8b758afe-a4ad-303e-92f5-c66c3cbf81d0 | -8.3613 | -46.9719 | 2025-09-11 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| f7a715e8-1fec-3b99-b32b-4d28775a0da5 | -9.9398 | -46.064 | 2025-09-11 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 747.0 |
| 87cf7367-b41c-3211-8238-deb9e7fa1b7d | -9.0553 | -45.7356 | 2025-09-11 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 0eaaf454-f49d-321e-b5c1-8e6f5eaa5b97 | -9.0127 | -46.1014 | 2025-09-11 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 26d7c445-4e32-30fe-b380-de2239682eaa | -6.1944 | -53.2585 | 2025-09-11 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 42a40254-7e50-349a-ac3c-b8574b68263e | -10.0695 | -50.3881 | 2025-09-11 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 18f2797b-b80a-3a98-a6ba-28d790d11c31 | -16.633 | -49.7905 | 2025-09-11 13:50:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4bcb8e7a-328a-3b2f-ba2d-8239e575860b | -7.4159 | -45.8761 | 2025-09-11 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 89412cbb-40fa-309a-a297-1347d575b1d8 | -15.1363 | -52.4679 | 2025-09-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 859b1f99-c25a-3666-acee-b5866ea4cfe3 | -11.1 | -48.4172 | 2025-09-11 13:50:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 13158b6c-eefc-3234-b331-98e21cebc013 | -9.0939 | -47.0983 | 2025-09-11 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 669f7446-68bd-3a94-a5c2-581fc806072f | -15.1374 | -52.4039 | 2025-09-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 7f539de6-114c-304d-b2b1-af9eb613024c | -11.4845 | -43.6402 | 2025-09-11 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 33bb661b-84e8-37a3-b5f9-05ae597582b6 | -9.0262 | -49.5261 | 2025-09-11 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 1d7ef095-664b-3294-88a9-cd1c3f00a58f | -11.4836 | -43.6875 | 2025-09-11 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| e4481558-38dc-30a7-a240-118c665a0f15 | -11.7399 | -46.5326 | 2025-09-11 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 005a3384-c100-3c99-9ac2-7d3fd85f26f7 | -7.4161 | -45.8536 | 2025-09-11 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 25b56533-7299-3148-9e72-da358f4f48c8 | -17.3372 | -46.6718 | 2025-09-11 13:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 035c6213-db1e-30d3-8142-65ad44de7b2a | -6.2228 | -43.3226 | 2025-09-11 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| e7ea81f1-4682-3e22-b543-0bb3d404e06b | -4.553 | -43.7439 | 2025-09-11 13:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 4c412978-1458-36ed-8a64-6f4b1f0bd0de | -9.0265 | -49.5046 | 2025-09-11 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 3cef4b2f-f777-3ed4-b008-785917cddda4 | -6.0746 | -43.1244 | 2025-09-11 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 9f2f8d67-4fe4-3a7c-8304-a747fb827d54 | -9.075 | -47.1002 | 2025-09-11 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 36db08f4-d1d8-3163-9b10-f231f613ff69 | -9.0129 | -46.0788 | 2025-09-11 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| b40f6950-8ade-3fb8-a2e0-fabb1c115416 | -15.5628 | -54.7453 | 2025-09-11 13:50:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d1ddd3de-895d-3a00-a8f6-8f6bd37e898b | -11.7115 | -48.2536 | 2025-09-11 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 374.8 |
| 9b4fb99d-468d-3f2b-a266-1a1b7c359dea | -9.0565 | -47.08 | 2025-09-11 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 653cc9e3-5d24-347e-90cd-4e4213503813 | -9.0361 | -45.7603 | 2025-09-11 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 3b4c634e-43c6-34dd-b5ab-c16974fa1ce9 | -12.9292 | -54.7538 | 2025-09-11 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 846d8b08-4e65-3dab-a919-66f39c9314f8 | -6.4836 | -41.7373 | 2025-09-11 13:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 122.7 |
| 220174c6-ee6d-3287-818c-219018571d5e | -8.8755 | -49.5613 | 2025-09-11 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 160.5 |
| e888b9da-5b9c-3329-ac11-ea87ded4685f | -7.852 | -45.5199 | 2025-09-11 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1425398d-da13-3057-ba8b-3ed17f90c746 | -6.0784 | -44.6961 | 2025-09-11 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 40a8a963-4f5e-31ff-af9a-3728c9209a86 | -15.8006 | -52.2687 | 2025-09-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 62231c37-2b10-38a1-8713-59be1ee531cf | -15.1561 | -52.4439 | 2025-09-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| f6a000ed-0e4b-3ef8-ac68-da2fcddd1b35 | -8.0474 | -48.1439 | 2025-09-11 13:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 71f16a41-5740-3e03-b508-ca17c063a02f | -22.9617 | -49.7387 | 2025-09-11 13:50:00 | GOES-19 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 297.3 |


[Clique aqui para ver as próximas entradas](README144.md)
