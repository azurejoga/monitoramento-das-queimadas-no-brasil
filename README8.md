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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68bfe8de-4c10-392e-8ef1-db0d0e78aa8b | -6.70437 | -42.04847 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b0909c41-331f-314f-bb34-7a9865e4eff1 | -10.76745 | -44.22764 | 2025-10-26 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00d3419a-52bd-3d27-9d7a-3a0dcd317030 | -12.02816 | -43.63451 | 2025-10-26 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbc84f8b-4aa8-3b9a-a83a-cc6cd2bdd67a | -6.69932 | -42.04754 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 4b76fc46-736d-3f7c-9f47-d6765bc4aa5e | -6.07784 | -42.14846 | 2025-10-26 03:40:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 60844eb4-0456-3ffe-b12b-6221b796f661 | -8.0322 | -41.20269 | 2025-10-26 03:40:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 778d78de-55f9-3a3d-b57e-7d64cf1b2792 | -10.88922 | -48.03504 | 2025-10-26 03:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91d481d0-39e9-3224-aa3f-673a4f2da3a0 | -7.80172 | -45.39659 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb2e0ad2-01e9-32bd-87cc-fbc6bb39abe1 | -9.30696 | -45.2258 | 2025-10-26 03:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 045891be-6312-3663-8859-dfbebf62a1fb | -6.70385 | -42.0514 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8506ee68-b43f-3635-a7b1-5733b51c1685 | -9.31504 | -43.09436 | 2025-10-26 03:40:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 18d1e7bf-6643-3629-8c9f-7ee0f4764106 | -6.4399 | -45.73244 | 2025-10-26 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f88dd8f-f6a9-3b0a-b5b7-e5b615004f03 | -10.9515 | -48.0783 | 2025-10-26 03:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72e1111a-8305-3015-b53b-896e8d6f704a | -6.73552 | -44.1557 | 2025-10-26 03:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66013e59-193d-3d23-ae07-0826292b58c6 | -6.7141 | -44.63213 | 2025-10-26 03:40:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a428ef7-d139-3ccc-bca2-edf022a4937e | -5.10473 | -43.20078 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09c88ea5-ba35-3d4d-9ce9-d4d25c4cdf45 | -6.71491 | -44.6277 | 2025-10-26 03:40:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 024e32cc-ac09-3756-8b72-f85caf85335d | -11.1138 | -43.22633 | 2025-10-26 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7d4deb9-e71c-3065-a4e1-a6ae1953bafe | -7.64714 | -42.31367 | 2025-10-26 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6b7a32bc-2307-30c2-802c-6a135b36c263 | -10.88365 | -48.02884 | 2025-10-26 03:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ce5932c-bbe4-3675-811e-708f8aed3395 | -6.70941 | -42.04942 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| cb271e4e-edeb-38ba-8e94-d703c2a05f23 | -6.18769 | -42.62339 | 2025-10-26 03:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c120c696-5e2c-353f-a44c-797f10f636c0 | -6.35954 | -38.36946 | 2025-10-26 03:40:00 | NPP-375D | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 473cd1b4-99e1-3c2e-879e-8628be57e704 | -8.15495 | -47.74884 | 2025-10-26 03:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c74ab25f-c8df-363b-b808-dd3f7442e63b | -11.42906 | -44.67768 | 2025-10-26 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 205649fb-2499-3ff1-9b50-0050e67571c1 | -10.42837 | -44.49428 | 2025-10-26 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6d7bb97d-d5d0-3d2c-a74f-2ddbc93f8ba0 | -6.39192 | -45.77613 | 2025-10-26 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5a09186-629f-3e90-8661-ca3a47d7b612 | -9.31445 | -43.09753 | 2025-10-26 03:40:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3bc3f354-5f5f-3483-b364-6a758f1c0ff7 | -6.06705 | -42.14954 | 2025-10-26 03:40:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 08de1828-f1a6-36e1-be4f-34b50493cbe2 | -7.64745 | -42.16763 | 2025-10-26 03:40:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a912b7b7-7813-3850-afab-f11eda75b974 | -6.30338 | -40.87602 | 2025-10-26 03:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f8124fdf-601c-30ff-925f-b4a78e5dbb01 | -7.69544 | -42.18856 | 2025-10-26 03:40:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 75cb1924-5323-32c6-93a9-009c19d40055 | -8.03307 | -41.19783 | 2025-10-26 03:40:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e65374c8-bf7b-34fa-ab4c-6c673b799638 | -11.18162 | -41.05296 | 2025-10-26 03:40:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b414784a-4dd4-3d16-983b-b930601a9a57 | -7.80079 | -45.39232 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a7e72af-f31f-381d-8b29-41417ae1ec4a | -6.73572 | -44.14932 | 2025-10-26 03:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8a4365a-a214-365b-bd3a-f9a7d8477572 | -6.44804 | -42.3377 | 2025-10-26 03:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b519bd44-415a-3710-aba0-a596b3181244 | -6.73051 | -44.15022 | 2025-10-26 03:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23c845b9-5158-3d8b-a99a-36d030b5cd5f | -8.3354 | -48.17892 | 2025-10-26 03:40:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da22507d-30ab-3e02-a594-7bb678dbdfbf | -6.52899 | -37.98355 | 2025-10-26 03:40:00 | NPP-375D | BOM SUCESSO | PARAÍBA | Brasil | 2502300 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 962e109e-c69f-3985-99a5-7e271524fe77 | -6.55327 | -43.23619 | 2025-10-26 03:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 9.6 |
| a2acc130-04fc-3d87-8285-110c91a6840f | -6.18235 | -42.62269 | 2025-10-26 03:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b817c737-6cc2-39f2-a6be-7ff02bd2dcf8 | -6.01639 | -43.30603 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1fac04e0-8951-3ea6-b3a1-210485ed5f1c | -7.84232 | -46.44099 | 2025-10-26 03:40:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fffe98a2-201a-3753-b26e-0643abaf69dc | -5.88619 | -41.30748 | 2025-10-26 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a67afea7-0d1f-3d9a-9da5-1bf270792bbb | -6.30354 | -42.96004 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1ab289b-cfca-3ff6-89fa-647cbc01144a | -6.60087 | -42.05545 | 2025-10-26 03:40:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e0dfc53b-86a1-3898-ac28-e0fdc1089b1d | -6.51027 | -38.60387 | 2025-10-26 03:40:00 | NPP-375D | BERNARDINO BATISTA | PARAÍBA | Brasil | 2502052 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8c354942-fde9-349e-b770-0b0d74cbbf86 | -8.36515 | -41.33999 | 2025-10-26 03:40:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3fd9d5d9-0804-35a8-bd9b-f7533e146b26 | -6.54683 | -41.57968 | 2025-10-26 03:40:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 100bd517-fe7b-393d-86ff-7d4c917ae397 | -6.21166 | -42.54957 | 2025-10-26 03:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a78de4d4-b566-3e74-8708-0d960d90f9bc | -5.4721 | -40.86859 | 2025-10-26 03:40:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 27423885-0571-3da6-a7fe-406d14b8cb0e | -8.30443 | -42.31261 | 2025-10-26 03:40:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 821fab4a-5ae3-3ceb-ad48-3f357be70d3e | -6.39092 | -45.78154 | 2025-10-26 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b620026f-399a-3101-bd62-ad0b07d88aed | -7.78402 | -45.38891 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44f0fc38-365a-36fe-931d-53e8470cb5da | -7.69145 | -42.18192 | 2025-10-26 03:40:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 724d1d9d-ba89-3c65-982b-9633589f5733 | -10.97799 | -47.88126 | 2025-10-26 03:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91cb6f60-b58a-3e39-8bb6-02eca1d0176d | -5.54673 | -41.40062 | 2025-10-26 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d850fac7-e137-3ae3-b82a-7cfcb4d9d358 | -7.05037 | -39.74353 | 2025-10-26 03:40:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 57bcd999-dd8e-3561-ab66-07bc11b3b976 | -6.3042 | -42.95641 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70470bf2-94c1-336e-8688-c0a7894a4c19 | -6.4493 | -37.08938 | 2025-10-26 03:40:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc83ac0e-d1a4-3175-8848-752021962c4d | -5.693 | -46.29182 | 2025-10-26 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6cc49e4-f12e-3c7c-bfdf-d1bd1c373d43 | -6.70993 | -42.04651 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 4970e89d-787b-33fe-b812-426aab7b3983 | -7.0933 | -39.5675 | 2025-10-26 03:40:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc684579-f8c1-3301-84b7-f4fd56500ec6 | -7.80072 | -45.40207 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa4d8718-6e09-33de-9ee8-9b88e3b4731b | -11.43458 | -44.67881 | 2025-10-26 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5841da53-81be-3c01-b06f-f6c52de2eb66 | -7.8483 | -45.37688 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be99a3d8-a327-32b3-b91f-afcb1ea283b1 | -10.40762 | -45.32242 | 2025-10-26 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 169ed86b-05bb-3e18-8fdc-8133361e6d86 | -5.85726 | -39.26362 | 2025-10-26 03:40:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9230c3f7-989b-3063-9c07-0e4cedfc5c66 | -6.02257 | -43.30343 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 056b70e4-2e56-3512-9abb-3387e1364428 | -5.54577 | -41.40621 | 2025-10-26 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 85919a0c-48ef-35c7-844b-9a6cfb32fced | -10.8908 | -48.02865 | 2025-10-26 03:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25a3abc4-c7a2-31c1-b20a-f81f7f183d1a | -6.33199 | -42.75764 | 2025-10-26 03:40:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ebf164f1-2f12-3346-9c84-2a32de2c094c | -5.58954 | -41.32826 | 2025-10-26 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 654cbf56-5626-3449-a4b3-f5210ab32783 | -7.8459 | -46.44546 | 2025-10-26 03:40:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ef1d071-d398-3781-a5a7-56ef98822abc | -4.89032 | -43.25376 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e756a5b4-b150-367d-ba49-cc82278d3d3b | -7.78216 | -45.38968 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e530fafb-24c1-3cdd-83d1-ae42fedbd6d6 | -6.70488 | -42.04558 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8d5508aa-71ae-385e-98cf-4964d99b806a | -7.05175 | -43.88632 | 2025-10-26 03:40:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faca75ef-260f-3b16-85ce-12aacc201dad | -6.44819 | -37.08719 | 2025-10-26 03:40:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 33ec0ab7-a89b-3d15-a86f-cf46fe4eb6ab | -7.34821 | -42.44442 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7ca13b45-2c04-3ee9-b213-b0a34f04b05d | -8.32528 | -48.19264 | 2025-10-26 03:40:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 364027f1-1183-3c9b-a2a6-dcdc9c47fb2f | -10.42531 | -44.50119 | 2025-10-26 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 15662ab5-8da9-30df-a253-9dae0fe2dc2c | -10.40795 | -44.73992 | 2025-10-26 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c0fd164-4646-3068-8005-cfa62d97d841 | -10.87541 | -48.03435 | 2025-10-26 03:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3af23c4-3cc5-393e-86c6-4186483ae67f | -6.71492 | -42.04774 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cf8421cc-a9ac-3f0d-a0fe-51f9a51be126 | -9.43576 | -46.33703 | 2025-10-26 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6615bb81-c2da-3a83-baa7-d47bf50f4d4c | -7.44368 | -44.74265 | 2025-10-26 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2d4a162-542e-38ce-a9e8-0faba244fb9f | -7.35334 | -42.44535 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7cab9163-bf48-33ab-8df6-d1b0d6dfc82c | -6.79202 | -45.41085 | 2025-10-26 03:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f9d9e49-0783-3bd4-ab81-9858a7593b49 | -4.72477 | -47.42087 | 2025-10-26 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e12ac1f-8b83-3c19-9fb9-5e91d84ad887 | -10.89086 | -48.02721 | 2025-10-26 03:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8eea82ee-cb3c-39ea-a6e0-4e9ffac38669 | -7.68539 | -42.18692 | 2025-10-26 03:40:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 554df33a-bead-3793-9f27-aa0b6ba646f2 | -9.43716 | -46.33935 | 2025-10-26 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76ad1264-badf-3119-9311-e1d31bea53dd | -7.69042 | -42.18773 | 2025-10-26 03:40:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 16564d96-5c90-3236-a800-86d011fbdd9b | -10.42682 | -44.49347 | 2025-10-26 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c22e5b53-ed18-3a8a-8ae5-01a6b3985737 | -6.20756 | -42.54205 | 2025-10-26 03:40:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 980c360a-64f7-3aa5-aa02-0e432ae4692c | -8.15593 | -47.04298 | 2025-10-26 03:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d5bce49-1c7e-392a-812c-edd2a1067f86 | -6.44532 | -45.73883 | 2025-10-26 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b125035-5b95-3aea-a922-434276dc5f14 | -5.89481 | -41.28665 | 2025-10-26 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README9.md)
