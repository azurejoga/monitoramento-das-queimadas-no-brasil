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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82e37c0c-346b-3fa1-bee2-86199f338c0b | -13.89297 | -48.3011 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97695430-3c7e-38dd-887c-988c29d8e94f | -12.70768 | -54.70342 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d0a77901-948b-314d-a042-fa763e0239b2 | -7.8756 | -49.49184 | 2025-09-14 05:08:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f78cf324-2230-3f09-bca6-b62a38386456 | -12.65844 | -54.67142 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c34c74cf-1a01-3a93-9fc4-4a0e71359cad | -14.62459 | -46.37003 | 2025-09-14 05:08:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 918bbc4a-2c4d-39b5-bb82-a23d0d91db15 | -12.66019 | -54.68398 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 4da93880-26c2-39f6-ab7a-60fed11ffe4e | -13.27547 | -51.69359 | 2025-09-14 05:08:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79ed947b-f4bc-3881-a784-f7de58f27d23 | -11.24959 | -44.77488 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| cd0c0885-ebce-3bbc-8dc1-0c264d25bccb | -13.94375 | -44.85197 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 9fc9646a-cd93-362b-99d6-243ae707d379 | -11.82435 | -50.48998 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a43f8ba2-26ee-3fbf-b18b-33200d09800c | -10.34684 | -48.83102 | 2025-09-14 05:08:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f1d33e5-2015-397c-bea1-516542efd0ab | -10.7386 | -46.43677 | 2025-09-14 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4c5f7a8-4a03-3cbe-ab3e-199c0cbf1ff6 | -12.12294 | -44.83835 | 2025-09-14 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21886ea8-7ca3-3501-8522-b91d67370dab | -11.78869 | -46.64716 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7d3e275-8f5e-37d0-9c85-67f25279cc34 | -12.85743 | -52.9785 | 2025-09-14 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40c37ed9-0219-31a3-8bc1-89d98d28f324 | -8.10108 | -50.16593 | 2025-09-14 05:08:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9b2f7f5-b39a-3a70-b175-6b5da346933d | -14.1715 | -46.15385 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54fded81-57e9-3bd3-9fc1-2ccd04058195 | -12.14223 | -47.59738 | 2025-09-14 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af142005-0e66-375e-97a9-3766178e7ee0 | -12.6766 | -54.69466 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 532c0c36-72b5-31f0-91bb-7ee97c82d660 | -12.66723 | -54.68506 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2bb2e0d2-c577-3b66-a5d8-de8506cbb011 | -12.78411 | -47.99572 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f4295604-ef33-3af6-8518-43f57ac0cb3d | -12.93248 | -54.73972 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d92a82ee-adb7-3852-a4e8-19c8addd8894 | -11.14171 | -47.65318 | 2025-09-14 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3aadc7ec-e9bf-31e6-a913-a984ef82a0d4 | -10.89822 | -45.56761 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75d8e966-91a0-33a9-a8de-a6b1930d7f73 | -12.80506 | -47.14146 | 2025-09-14 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3463fbe-69a4-3373-8448-1cee54e3a289 | -12.69826 | -54.7183 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2b3f85cd-2bcf-3cb4-97e7-b4af7c2eb6f7 | -11.23207 | -47.62927 | 2025-09-14 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9f1fc4f-598f-39fc-abc3-bbdfeb14622a | -13.92928 | -44.8618 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 29b4eb5a-a4c2-3f33-a20e-ec30e46366c6 | -12.7851 | -47.98793 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61fd9bd1-b205-3c6b-be24-52aaea38b9db | -11.85408 | -50.4715 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 598cc11d-882e-3001-9182-54bf508b6348 | -12.6936 | -54.70134 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f8c780cc-42cb-3eab-a38a-836c1f4ed513 | -11.89532 | -50.53606 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8e35495c-a579-3e70-bc3b-d7bc32477331 | -11.78182 | -46.65429 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2e4b1800-cfdc-3562-8a5c-28152ec5bc55 | -11.38756 | -47.33851 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3a85f743-c180-3129-841a-894db00e3312 | -10.66693 | -48.6705 | 2025-09-14 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43890e39-fc3d-394a-92e1-32f323c43a12 | -11.28957 | -51.09889 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72d570fb-947c-32a3-a63c-07b4c3623592 | -12.67249 | -54.69814 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47488025-478c-31b0-af61-a848ac35c760 | -10.59958 | -44.32801 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5c7d52e-8d6e-3b28-a5a3-41a4066557d5 | -13.93289 | -44.828 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f405b212-6d5b-3e9e-80ab-71e8f71dd030 | -11.89027 | -50.53986 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 822f9cb6-0768-3d79-b642-0512c911df0c | -13.01081 | -46.74598 | 2025-09-14 05:08:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d468460a-509b-33a9-8cb5-a1d31c35f432 | -10.97207 | -49.56567 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b7213ab3-4ece-3f69-81f0-51e9c2cf9ee1 | -12.72508 | -48.03313 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32c99d31-fa42-3469-aaff-75ac9cdace9a | -12.80116 | -47.97078 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac1ab56a-5339-3bac-bdef-f4c31976c810 | -12.77731 | -48.00647 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 52998480-6d75-3e74-8a49-5191e8473a8b | -14.15434 | -46.25576 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a245395d-0c5b-3491-94a3-9ee8b8d33428 | -12.67605 | -54.67411 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| daedab2f-c9d6-3f8d-904c-57e05b94f50d | -11.82261 | -50.48186 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e55f5995-626a-3ff8-a516-d8c5614e5921 | -12.93868 | -54.74763 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b1f4850-6a57-3589-bb66-6e0499e671a3 | -14.20119 | -46.16663 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ab68b62-9da3-3868-9e4f-3765ae716e28 | -11.91202 | -55.90652 | 2025-09-14 05:08:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d3fc969-f7bf-35ad-ad3e-6c4153ec1177 | -11.83714 | -50.49631 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 817bc510-b22b-3bdd-bba6-d3675a2c81ec | -12.67664 | -54.67012 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5ea57436-5cd0-371d-9dd8-e935a83f99bf | -10.91308 | -47.19863 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ff0ea64-3a2e-31b9-95c4-48e27a7811c3 | -11.84724 | -50.48869 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 99a9b876-d8dd-3c6a-bb49-4a07425cbfa3 | -13.96796 | -44.81451 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 48744c09-4acd-353c-9416-ec32aa2acb85 | -11.83832 | -50.48743 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 95535329-e1f5-35ad-bdf2-c38cdb779fcc | -13.96128 | -44.81403 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d3dd888d-6826-31d0-935e-e66019a0d066 | -11.83327 | -50.49125 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 315a7d28-5194-3b81-93ac-c1aa1c1fe02a | -12.09262 | -44.87116 | 2025-09-14 05:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 791dc5ce-52da-3572-a280-f0719817dcf9 | -14.4816 | -53.9317 | 2025-09-14 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c627d415-9fec-311b-94e0-c85dfa616e1c | -12.66664 | -54.68906 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a1f7f9ae-551c-36f5-85b2-24f7888b3e16 | -11.24314 | -44.7741 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ce41937-d2bb-39fe-91da-b0c61d1bd91d | -13.02681 | -47.9948 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff048b5d-12f5-3fdd-a8f0-2c3f7a19a677 | -12.09019 | -47.5667 | 2025-09-14 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e21ae972-cee1-3c66-a361-ce191561a2f8 | -12.94834 | -48.03282 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d751e73-42d6-38e5-9507-79668cf2d503 | -9.97367 | -55.03844 | 2025-09-14 05:08:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abac3fd1-cf2e-3741-a103-e982a2050084 | -11.46443 | -48.70819 | 2025-09-14 05:08:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| fcbc6b8a-3816-3f8b-9db0-966c06525d81 | -12.12351 | -44.83327 | 2025-09-14 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee901c4d-e493-33ea-b38b-0b63d9a7edbe | -12.66255 | -54.66796 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61471ba5-4d2e-3572-8ee0-22187ccd0e24 | -8.76408 | -46.04685 | 2025-09-14 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 902a7b7f-0e75-3484-bbea-06b991660415 | -12.9125 | -54.75296 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8bea5738-bdd9-353f-9539-4427702e099c | -11.37586 | -47.33897 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 002abfbf-51f4-3964-b380-6730a2244b57 | -12.77199 | -48.00555 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e3d7d52-9ad5-3c10-9a21-1b0baeabb861 | -11.67081 | -46.50513 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24685c03-44d4-3ac3-8c11-2b3a7093cf16 | -12.78642 | -48.04786 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69cba9d6-8a80-3bef-9722-52e468e4db25 | -12.69723 | -48.30012 | 2025-09-14 05:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92acf96b-165a-3485-9f8f-f7867a3504a4 | -11.36996 | -47.34144 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5766eb66-b120-360a-bccb-ac0dcc4a4f20 | -10.601 | -44.33368 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55cf051a-8b6b-3222-9411-7a5f7c38f71c | -10.59893 | -44.33354 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cd2e9a5-cbf5-3f73-b6d8-eaf63cfa5a92 | -11.28821 | -51.13918 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc7c1acc-e7b8-3ffd-b2d1-31f1b3b8abbb | -12.67779 | -54.68664 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 1d45364f-3bed-38e8-83c5-f17ae99b8e33 | -11.38677 | -47.3449 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f8e8ae10-84ca-3fba-88da-574f438bc869 | -11.27941 | -51.10958 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1610d3ac-0f5f-3316-a668-487549ef37b9 | -11.83269 | -50.49569 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ae7c5f41-e098-39e2-b192-ce62a60d01f7 | -11.81815 | -50.50267 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f13261a9-8a5d-3507-b0bb-e4d09e7f7942 | -11.89977 | -50.53668 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 17faf449-3d62-37cc-98a0-7f29dd9d4fd2 | -12.77735 | -48.03306 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12d7d754-458e-3099-b937-76134a083a27 | -11.7892 | -46.64312 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61e3aff0-dbab-34f8-9e03-faf9b871bbde | -12.74277 | -48.02181 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa9c2964-9771-3647-b365-c6819f636c0d | -7.87816 | -49.50581 | 2025-09-14 05:08:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2525d3f2-76bd-3a53-b329-d995ef861f9c | -12.96234 | -48.05141 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee652d61-f9cb-36e8-9af4-4fd266ed316d | -11.25033 | -44.77554 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 93ab4ad9-c97c-30d7-abea-009cd963ac0e | -11.47822 | -50.77678 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f71539d-9ec3-3da6-bee0-b780fbe91d1a | -12.75101 | -47.99934 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a657d600-5b05-30c4-97d9-a5ec72b2c33d | -12.78288 | -47.98701 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ec6b5c2-d9f3-3f57-9cd4-0cd252a64985 | -12.67312 | -54.66959 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 130b0ef4-abf7-38b2-bdd9-ba759e259137 | -10.13793 | -47.19089 | 2025-09-14 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47610af5-7ddd-3167-bfac-ebb35aa41ac6 | -14.39528 | -52.91316 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bee6943-4872-314e-ab5f-917d4a1dd3ed | -12.77772 | -48.00323 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README59.md)
