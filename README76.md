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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0dc0cda0-db9c-39c0-8f67-e83e2b43b951 | -10.64824 | -48.50655 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8418321f-0fca-32ed-b5ff-151fbd259861 | -12.08321 | -44.92071 | 2025-10-02 04:29:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d51ea1ed-0797-38ac-9bae-ae2631a50502 | -8.89807 | -47.61461 | 2025-10-02 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1e17d0b-e344-3c0a-8d84-ef85c31bde22 | -10.91095 | -44.318 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 245db151-1798-3dbf-92a5-8bc82520fa73 | -10.43256 | -47.47248 | 2025-10-02 04:29:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 083a2b9d-7f70-3852-b836-7b8c50db3833 | -10.99373 | -46.59052 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43cb0e92-e1e5-3422-acb3-a948cc3c6c91 | -7.56604 | -42.3995 | 2025-10-02 04:29:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 173a6172-92f5-35e0-9532-aa8a7fa605a1 | -11.59544 | -47.64617 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8356e26f-c63e-3739-a8c5-00ec0cf3a655 | -9.08579 | -46.72525 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c76ec00-9496-3678-9052-bb0e69dad3e6 | -11.17794 | -47.26814 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b6c482dc-2296-3865-a1fc-7d3f278775ca | -10.84738 | -48.00673 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbd97332-3b14-3e54-87c7-c2f399062d55 | -11.09051 | -47.71241 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 282fe206-43a0-3ec6-a3b6-0bddd657a49d | -11.86938 | -45.00595 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| adae05e7-a5a8-308e-bcee-24733c2d45f7 | -10.18875 | -52.5618 | 2025-10-02 04:29:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47397698-a7a0-3427-a5b1-18e03f876395 | -10.23263 | -50.3125 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61a9f9ed-2eba-3fc9-ad47-88ade7805b43 | -7.77682 | -45.73791 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2e97721-5d90-3a8d-ae13-8b9e8000f7a4 | -11.27415 | -47.83304 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79f3866b-3acd-3246-a48e-e76e0e479f07 | -10.83403 | -46.63445 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| e1d3fc14-96cb-336c-8759-9c0c38425ffb | -11.67431 | -45.32598 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 452130e0-3f82-373f-af55-0c19d4d27003 | -9.03916 | -46.68163 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcd1dd8c-423b-32bb-aacd-a5d73f2da5c7 | -11.79399 | -44.97972 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebbcddc8-9709-3d0c-9cd9-0e10612607bc | -7.01049 | -44.49627 | 2025-10-02 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6ca3726-6846-370c-9f28-bff0805da3a7 | -5.8634 | -45.73741 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f91bbea0-33f6-3974-bbfa-ebd4664d5c3e | -11.20344 | -47.19283 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7df1cac-9118-34fc-864d-099f86e88c70 | -8.8592 | -47.30541 | 2025-10-02 04:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ede58f6-6859-3ac6-bc32-33f91761adb0 | -11.4788 | -44.99528 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9d57540-22b8-340d-9644-e1a2bcee4f41 | -7.77912 | -42.53362 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ff6ba91c-29fa-3466-889c-99987181457f | -12.11335 | -43.43769 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e44c6292-e757-366e-83f3-170001ffeb85 | -10.67472 | -47.79705 | 2025-10-02 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13f3e5a5-9821-30f6-a772-ea3e2f8c089a | -11.61354 | -45.03331 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e618867-8ec6-32b0-89c7-e43a7beab5f5 | -10.24418 | -50.31017 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| bf0a0edb-f404-3254-b100-b5ed3f3088b1 | -6.35592 | -43.30317 | 2025-10-02 04:29:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8162824c-345f-3385-b182-101a944b597d | -6.9653 | -45.3477 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6dad7c7-fc84-3427-98cb-9df55a0047b6 | -11.43562 | -43.49675 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1b8339d-c2eb-30e8-8e54-fe7a6c544708 | -9.34035 | -45.91931 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e1fb4b1-6a04-379a-abec-6d567eaa26a7 | -8.88267 | -46.59594 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5051d803-ae67-3406-8ab8-316e4a6ba788 | -8.51166 | -47.80374 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0df701f8-0951-3120-9522-b1155299192d | -11.70264 | -45.35043 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8a28bcc-b3eb-3968-b066-6426d5806ffa | -7.77804 | -42.51419 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| abab4925-5cf6-3450-b473-ae2d557b6a28 | -9.42286 | -47.35275 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3503ea20-c31b-3828-b1b4-be9e0de67ee3 | -10.65558 | -48.50402 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bbbab848-0518-3cf1-98d6-8ce4fa1a5909 | -9.93643 | -43.77156 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c8afbccb-fd67-3fb4-9c76-e52566866c2e | -11.08532 | -47.80927 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51f829d8-3777-3d7b-8d3f-5cd8031f9317 | -11.61993 | -45.0387 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db2a7994-8be5-3a5b-94e8-c392023db73a | -11.1696 | -47.19101 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eba40f86-fda5-3108-915f-8424e8ddbfd5 | -7.30962 | -42.87394 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8a220fa6-4a63-3377-b7ad-11e67424b5d2 | -7.34639 | -45.22998 | 2025-10-02 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 768122c9-bbbf-3adb-8e5e-5bb137e1e137 | -6.82204 | -47.97294 | 2025-10-02 04:29:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a8f3523-12c9-3bb4-b70e-4ac3c766523c | -9.93313 | -43.71843 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3e337fb5-3100-3975-afce-2d1479cc5585 | -11.14078 | -43.38079 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d5ca6318-3e54-3c75-97f4-04f0315e4ad1 | -11.8186 | -45.00777 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c4b56a1-d5ca-3f96-a060-9888b7d4c421 | -11.59592 | -45.05204 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b3d27815-d8ac-34e0-898c-cd5fe4d31e14 | -8.38424 | -47.98851 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41700753-1622-3233-8bde-1f29146f05b3 | -8.16201 | -46.25945 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed71eb9c-6064-35fa-b818-e72fe4d3b3fc | -9.92642 | -43.71303 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f8bb205-ee39-3a3a-af97-65e56bf91c9f | -11.81944 | -45.02699 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 800813d0-9bdb-37b4-b4a9-1d42df90c77c | -9.94176 | -43.71088 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 715a945c-5e70-3ba3-83d6-7ee281ba034d | -6.30214 | -43.81004 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71426f75-aa6d-3b6a-90c0-414ee555dc6c | -10.66276 | -48.52375 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74c7a1d6-8f41-39a3-bca4-2c89adf23748 | -6.00766 | -52.38476 | 2025-10-02 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 707a1776-88a5-32e9-b1bc-5c99518107ce | -11.00878 | -46.58193 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01435cff-a1a3-3bde-b25b-aa535b5d40df | -11.51368 | -43.53954 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b28d6150-cde9-3b97-bfca-b608ce98ca8d | -8.70722 | -44.82177 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 261aafaa-77e9-3842-ae65-d0ffbd142c7f | -11.20066 | -47.18876 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d5adf59-04ba-3437-bbcf-2077db0398d3 | -10.95927 | -46.65783 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1c6609e-5cc6-353b-941d-07e24e23ee86 | -10.25722 | -50.32103 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f92179cf-6ba4-3d43-bf67-e65c2dfd318c | -6.94756 | -46.3042 | 2025-10-02 04:29:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 828354b7-c5bf-37c6-b2f7-256efd03f024 | -10.6776 | -48.58188 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 613f9190-89ab-312e-a68b-4dbb3766cebc | -9.92874 | -43.64671 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c607c8f5-102d-32b8-a33e-bfa38b03283e | -11.79992 | -47.57057 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4787819-c441-3f77-8ae3-af1553550f8a | -7.05216 | -43.27877 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 12653af9-0e8c-335a-b9e1-50c845e798db | -8.7427 | -47.33722 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 06a293c1-38a5-3ed0-b04b-7f13d53c8766 | -6.2274 | -45.33527 | 2025-10-02 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df48dbb9-dd34-3d4e-89f5-c7ee966ec5d7 | -6.18053 | -44.06509 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 156fd00c-e38e-3828-88eb-a7bca2f2e768 | -11.51746 | -43.54009 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7343f07-bb02-3002-accc-0a806c62b87f | -10.30616 | -42.39652 | 2025-10-02 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4785c4b0-f2a0-3164-b6cc-e7846a1a2930 | -6.8116 | -44.47506 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38e958af-7092-3e19-87cd-e3d51bc11b5d | -12.27683 | -44.12188 | 2025-10-02 04:29:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4593d2d0-e22a-3d04-bb77-d859bdf87343 | -11.81255 | -44.90418 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 711d7565-9faa-3dff-9852-8e911ed1709d | -11.78336 | -47.3942 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f359a126-00e1-3ce9-869b-de94dc8f30ce | -6.72121 | -44.62805 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a681a9a-2d19-38e2-b06a-fe060b352ddd | -8.65967 | -47.09062 | 2025-10-02 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbcc6084-c1dd-3dca-bb29-605f10ffc05d | -11.07865 | -47.80818 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f1f3017-2390-3bef-94a8-32f98747f4d8 | -11.49558 | -43.5035 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f61f4f24-1f31-37f9-85b9-12fc97d4e753 | -11.78993 | -47.56894 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67d1717e-0e26-3fa6-8f9d-0b32c220f32d | -12.27558 | -44.13071 | 2025-10-02 04:29:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 88407ae1-0ebb-30b5-8e42-560577dd072b | -7.55609 | -42.63857 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 93eed9ac-56fb-3b3a-80e3-f9e964fe1af4 | -10.84292 | -46.62133 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a5c5f5c-c0e2-39d9-8176-b90016544e1a | -8.89711 | -46.61259 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55617c85-7548-3317-a0a7-ca3c5081381c | -6.2611 | -43.89136 | 2025-10-02 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f05c79b-db7d-3d48-9222-c798df3f78ee | -11.7392 | -44.42677 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e2cd9fe-a59c-3594-b0ce-89c8e4c5a6c4 | -10.22606 | -50.28551 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88f33e7c-fc4b-3a07-98f7-be69471c7221 | -11.03212 | -47.82981 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da91d654-15b5-331a-9265-0bca792d48f0 | -11.59433 | -47.65323 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c854aa1d-aee0-30d8-bf5b-cec59a58b2de | -11.14147 | -43.37598 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f48cfdf-68d6-3194-a335-2a934571cc91 | -11.8139 | -45.01508 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 330bbb5a-b550-3b0c-8924-2b74270c8a15 | -11.59283 | -47.22995 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43ea991e-10f5-36d3-be50-01c70f735c3d | -9.33536 | -45.70509 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dae769a3-a923-3437-946c-ea18f78954be | -10.41741 | -51.66488 | 2025-10-02 04:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c176f66-a635-365d-8487-20b1bc99e906 | -9.80347 | -47.8297 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README77.md)
