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

## Dados Diários - Página 214

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdac5fa2-a6c3-32e0-a591-e1e7d2ee2a2d | -6.59939 | -37.88629 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| c2be9e0f-5123-38b9-8f54-ee9c26b0c621 | -3.63471 | -44.80747 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3b15f805-0f9a-3e47-a664-4801c6a2e3c7 | -4.88799 | -38.90939 | 2026-10-07 16:37:00 | NPP-375 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd11e121-b047-3a05-8883-72cd9fe38784 | -5.49619 | -42.84482 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 37.2 |
| a514fe3a-12b4-3c29-91d0-202358dd4e5c | -5.37349 | -44.17139 | 2026-10-07 16:37:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| a574b1ee-5bf6-36bb-a26d-7c841943e3ed | -7.87229 | -54.9901 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1a55120b-6928-3d19-94ec-97bdd68ff1ff | -3.77641 | -41.87772 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| f09f6ba1-6a58-3b18-bff1-2b7c0650d2ff | -3.5624 | -39.46791 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 75a91b26-2426-3ce3-bfc7-8343be838a38 | -6.46007 | -55.46001 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 10e3a9d0-d650-30da-bcd5-91be84df855d | -6.04339 | -53.21544 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 19b7deda-530c-3f75-9b31-736f389fe781 | -10.88245 | -47.60268 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 89379e04-9f41-38c1-ad83-55e76992905b | -3.80694 | -40.47044 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| ce92db64-b5f6-314d-a97f-41c2056379fb | -3.43473 | -42.21012 | 2026-10-07 16:37:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 9.5 |
| e168043f-a29e-3913-981b-5b7e10341339 | -9.23716 | -45.66105 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 7bf80b34-53dc-3740-9279-4d12343d1c60 | -6.71716 | -44.00716 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 181050b9-4318-3418-a0fa-1c9e8004f7d1 | -9.14945 | -45.8311 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a48e2b72-d2f1-3e5d-97d6-d2314e67e880 | -5.50467 | -42.83245 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| de8ce75b-f522-3afd-8e9a-daef5dab5586 | -7.19698 | -44.29383 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 31cc385f-560d-38f0-b858-d381a3ee231b | -7.0327 | -43.43755 | 2026-10-07 16:37:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 37f81b81-510e-3f81-9567-3dc1f99f0e44 | -8.99387 | -45.94599 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0a922dd9-835d-3479-96d4-02de1327460a | -7.24367 | -37.97552 | 2026-10-07 16:37:00 | NPP-375 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e69faa46-cd3d-3821-a1ba-4b858b5752ce | -9.70472 | -47.75855 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 96ee82a7-d6f7-3612-b588-6c3dbbe6aaae | -5.24489 | -50.92177 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ebf348c6-4e0e-379a-a1dc-a1444d033a76 | -7.17265 | -47.80405 | 2026-10-07 16:37:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ceab09f6-8eaa-3be9-a2d4-d8a7240fab29 | -3.8948 | -44.11899 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 50bd6053-2271-3eb4-9098-2f461eb791e5 | -3.73811 | -44.97479 | 2026-10-07 16:37:00 | NPP-375 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 89f38c1b-1686-39af-894f-162046e80075 | -6.23118 | -53.14908 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0f071a48-c0b2-3e35-93ec-e9f8bfcc9dcb | -3.58778 | -39.14383 | 2026-10-07 16:37:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| dab3c50a-ed40-3278-bc9e-a09798e446a8 | -9.25921 | -45.64198 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f0a68e68-ad9e-320b-9124-c2751b0c81b0 | -7.39715 | -46.21854 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ca2bb0a7-c2c5-3053-b62b-c90edd8f5ff4 | -3.79785 | -38.59136 | 2026-10-07 16:37:00 | NPP-375 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6bd297d8-0cf0-3e77-9e5c-a0f28ade6f52 | -8.7546 | -44.15516 | 2026-10-07 16:37:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4f372fce-c8ac-3251-9845-db4eed166bae | -6.70489 | -52.98208 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 37a86afc-2f3e-3e3e-9bb1-3027fab1ab52 | -7.46406 | -42.99428 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3a4d2103-909a-3148-90f7-d4d341055909 | -6.12347 | -52.72167 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| fc5faacc-5eee-3bd9-8f53-eb262b1a8a76 | -7.20545 | -45.0891 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1bdd8ea8-31d5-3b98-a105-b6092fd85def | -9.80455 | -44.78069 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 953fbe72-36b7-3a12-9481-67a0d8c46ae9 | -6.04762 | -53.48728 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 9518824a-8073-3d47-8312-43f961c54ec8 | -3.89986 | -44.10756 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f6ed0b05-dbbe-3c2c-9663-a9c3a7a4c7f6 | -3.22229 | -42.65257 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 186dd4f9-b333-31c2-9434-1c7473a67771 | -9.88909 | -48.74063 | 2026-10-07 16:37:00 | NPP-375 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b14119d5-78b2-361e-8fee-b74ac5194c01 | -9.97061 | -43.50566 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| eb7ba7e0-32f4-35ba-b63a-429e7ba4d062 | -5.96062 | -53.55127 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f74fe5b0-7b48-3509-9568-b3c27f352eba | -7.47793 | -42.79642 | 2026-10-07 16:37:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 43fe302e-f7d6-3c74-be7a-eb2681c44b9c | -6.81806 | -38.53098 | 2026-10-07 16:37:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 41.3 |
| b433e140-4df3-34dc-a01e-41ad94338e82 | -5.14547 | -55.94831 | 2026-10-07 16:37:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 72865e04-58bf-342c-8dfe-296caa92b780 | -6.19981 | -40.80379 | 2026-10-07 16:37:00 | NPP-375 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 1fa16750-396e-3952-a7e9-8efc5dd9f478 | -3.6682 | -41.44392 | 2026-10-07 16:37:00 | NPP-375 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 89527f4e-d404-3dc7-af93-300c372f0a22 | -9.58263 | -46.20765 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ec6652b8-74c6-3911-abf0-c619d82a499f | -5.96709 | -55.35974 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8edb4c45-b7c1-3c81-9c46-7ebc539ac390 | -8.78288 | -48.25527 | 2026-10-07 16:37:00 | NPP-375 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10349489-dede-3b0d-b66a-450dc7da6a77 | -3.7109 | -43.53773 | 2026-10-07 16:37:00 | NPP-375 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 7fb06183-962e-31a8-a53a-b1e362378ba5 | -7.56691 | -35.3359 | 2026-10-07 16:37:00 | NPP-375 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 78ad20af-e8f8-3959-ad72-d4514fe92a8e | -6.01257 | -53.52555 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| a3e6fc5c-652f-37f2-8243-92efcc9a1c0f | -5.99326 | -43.60342 | 2026-10-07 16:37:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 46b1b641-0493-3216-97be-b1961870e783 | -9.86942 | -46.31029 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7ab21abe-b823-39a1-bfbe-08cef22efd3e | -8.29396 | -45.4735 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 5a28381d-389d-3c3a-8c8e-75f25c1b1a71 | -11.10736 | -47.58637 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4c08766e-5b24-3cbb-bb72-cfcc97da1bc5 | -6.21071 | -52.84381 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4397f0a1-edf2-3924-9129-0d8e5e53c3d9 | -6.22117 | -52.84261 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b556d0f6-ee2f-37a2-9fb8-f09807c95267 | -5.85417 | -42.6545 | 2026-10-07 16:37:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 737bc3d7-e52f-3965-81eb-8f368cc305b7 | -5.49281 | -42.84534 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 37.2 |
| fc91a9d5-e4e8-3951-8e55-c9fe3c443672 | -5.23327 | -50.90515 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c48f5f0d-fc4c-33c1-9823-ca78f56e2466 | -6.98622 | -43.29086 | 2026-10-07 16:37:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 0d76d51b-7877-3e31-879e-401e9268060c | -10.97982 | -45.40432 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 13145f83-41f5-3949-822e-e6f51e7178ec | -5.946 | -46.36477 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 151720b1-a512-3859-8f61-6d8351a2c16b | -5.95753 | -46.37077 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| cb56c3fe-fbf3-3303-90e3-bcb7d35ea1b8 | -14.67847 | -41.45829 | 2026-10-07 16:37:00 | NPP-375 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fd89aa8c-ed35-3c33-89a2-bf0a935fa903 | -15.66614 | -39.70454 | 2026-10-07 16:37:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a30c2439-af92-3b3c-9304-e7d1b003fb75 | -3.52679 | -43.83743 | 2026-10-07 16:37:00 | NPP-375 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 24d65c7b-4809-3440-9179-d67d21775b12 | -11.21847 | -46.23482 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e74a6a7d-08b3-3c84-be6e-ff6234f29c51 | -9.86402 | -46.0685 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9508a42c-53e4-3085-967c-b3dc5b658b05 | -3.76339 | -41.72233 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 402de488-1ab8-32fc-adb1-8f86fd71e08f | -6.84526 | -39.55161 | 2026-10-07 16:37:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 51b1402d-ed17-3d7d-965c-a6e32032c9fb | -5.24478 | -50.90598 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| ce1ecf32-d6ca-3907-b1ec-4c94c6b95889 | -4.51354 | -42.87717 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d9ddba00-16da-32c1-a2e6-c4dac616d90c | -6.67911 | -41.76809 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 7c02cdf6-b5a1-3c88-a03e-6ae7815e8779 | -5.80817 | -44.89502 | 2026-10-07 16:37:00 | NPP-375 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 48d10bf0-b7dd-3207-9320-c51cb3c528fd | -7.47788 | -42.81826 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 7911ac10-4c4d-330c-81c1-12fa4ec959d9 | -5.98053 | -40.95005 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 70a0e00d-27d1-3f33-a0be-8c1a798e3ae4 | -6.95078 | -45.25628 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4b685068-a0c3-3d34-a547-aa1a45350c39 | -7.21227 | -55.17809 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0148797d-1ea2-3252-8d38-922b3e5df82c | -4.70476 | -41.91563 | 2026-10-07 16:37:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 430a8b77-6d37-381b-b658-f92720fd1abc | -4.78465 | -43.33826 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 25c57d27-ca69-3c7c-8d1a-ffeb47c28bfd | -8.52669 | -54.6172 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0fa82362-1324-3de8-9f74-992c7f87be47 | -6.47319 | -51.23538 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 202334c9-af70-3d5d-a529-d9593254af94 | -5.64623 | -45.18579 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f5b41629-2ef9-3f6f-a7bb-3cb3d8868a4e | -6.13601 | -44.64699 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 73424cc5-e30d-34c2-98e3-d768dd8a8909 | -3.35854 | -41.91235 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b127bbe4-dcf8-3d5c-9dee-55916dd55fbb | -7.77225 | -43.81023 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 659c9934-ff57-3faf-b5ab-3f83685d0476 | -15.99942 | -38.92309 | 2026-10-07 16:37:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 8cb1895b-f21d-33ce-9ce1-3cf221d9919c | -5.48371 | -45.63277 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 119cf170-d096-373f-a818-60b27ae2abf5 | -8.61772 | -48.35075 | 2026-10-07 16:37:00 | NPP-375 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4e883d77-1620-36ce-aecf-787c136a68d3 | -10.469 | -47.21205 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| cfd68927-17c3-3df6-a468-80f7f9fb247c | -8.76233 | -44.16116 | 2026-10-07 16:37:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 9b94191d-9423-3fda-ba2d-68bc2b0797fa | -17.02383 | -45.91047 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 5ba06b1d-d785-323d-8d55-7f430329898e | -6.02239 | -52.75941 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7f7439e-8acf-3c51-9094-272af8a8b464 | -5.31087 | -55.91868 | 2026-10-07 16:37:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d6a3c5fa-10f2-3ee4-a8d6-703feeef4b27 | -4.79026 | -43.33012 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0e183162-84c1-33eb-8fa0-873f61d391ef | -5.01394 | -49.94081 | 2026-10-07 16:37:00 | NPP-375 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |


[Clique aqui para ver as próximas entradas](README215.md)
