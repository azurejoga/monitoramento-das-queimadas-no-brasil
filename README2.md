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
| 182145fe-c701-3378-9c6d-75877c9d4caa | -12.6372 | -47.077301 | 2026-09-10 00:05:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e2bddb2-d30e-3e62-9ece-683b6bd8bdd2 | -9.3274 | -45.6231 | 2026-09-10 00:05:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 26e102ac-e9ec-3de8-ae72-64af2e3056e4 | -6.4783 | -46.2822 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a2462e4-d9fc-3c87-8a9e-d4d5d549f4ed | -11.2144 | -46.341202 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba45c518-6c7c-3715-bc63-c0a94e500c84 | -12.2081 | -49.3899 | 2026-09-10 00:05:00 | METOP-B | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0ca0359-0b42-3817-95c8-84f94301b2ab | -6.1622 | -44.651901 | 2026-09-10 00:05:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2651e19-a464-3711-b1f2-06efcc818753 | -7.2616 | -45.343399 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b108d25e-0255-397e-8cb3-fdc08b0de898 | -5.7672 | -45.079899 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4f922b7-7704-3e05-9cff-f293461cf01b | -7.9843 | -43.980499 | 2026-09-10 00:05:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8fcdb344-6062-388c-88b5-696d6d603b86 | -9.69 | -43.472099 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2d6dad43-3eae-3af8-9b64-af4966cc9864 | -5.1052 | -46.947399 | 2026-09-10 00:05:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b88a533c-d7a5-3a86-a395-4d3af6f0a6ec | -5.376 | -46.285599 | 2026-09-10 00:05:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b39baeab-b13b-32a2-b901-a34ff0f1b8ac | -5.4795 | -45.128201 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9439d9f-6f52-3a69-9aa1-40406bc7ce3e | -2.7205 | -57.607399 | 2026-09-10 00:05:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3268e50a-a0ad-3327-ab3c-52664ef44052 | -10.4586 | -44.939602 | 2026-09-10 00:05:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1fceb181-d1e5-3d9f-8202-ec5f7687d73b | -7.479 | -45.2584 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d808960-4d6e-3e9d-aab8-1edc24c3fef3 | -7.5986 | -46.761101 | 2026-09-10 00:05:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db6bc6bc-79d0-3a8d-b344-83a3c0a60672 | -6.1702 | -43.0228 | 2026-09-10 00:05:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d0839f9-e66b-3e6d-a756-5ddc39fba7fe | -12.8425 | -44.3176 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7e74079-255b-3160-a219-152abdf640a2 | -10.6691 | -46.0751 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c5846c32-0966-3e93-8885-c40e404cbeaa | -2.1657 | -47.4786 | 2026-09-10 00:05:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4af886b4-c96c-3ee7-ab8d-02c9b43de229 | -3.5502 | -48.174 | 2026-09-10 00:05:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f320bb6b-b430-35bc-89ca-def48340c422 | -10.2615 | -45.201302 | 2026-09-10 00:05:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9bf52769-cfaf-34d3-94cd-8875a512afd5 | -12.8287 | -44.3465 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 62be1eee-52f7-338e-919f-0c46a9956adf | -2.939 | -50.484402 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b447a876-6980-3abd-a0d1-b825c6aa463b | -10.7485 | -45.926399 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 173b9c73-09b4-3695-a849-4b94195a0e38 | -8.634 | -47.370499 | 2026-09-10 00:05:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3387ccfb-b9c1-3900-80db-b5d27918dcff | -9.6803 | -43.474499 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6b35e05c-51a0-3e9a-9c0c-ea270f33ad8f | -14.0656 | -46.324902 | 2026-09-10 00:05:00 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ac25a623-2320-3f3e-8a38-b95b581c0cc5 | -6.7635 | -44.578098 | 2026-09-10 00:05:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0db2acf9-5803-31fd-9dfa-cde13b8eab35 | -2.9456 | -50.468201 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5233a4d-6802-3723-b973-ccad79ab2ce2 | -5.586 | -45.365101 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5006a82-8e1c-3f39-be00-e4e71e4fd58f | 0.2963 | -51.437599 | 2026-09-10 00:05:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4c176139-313f-3a13-a718-e182d0f64345 | -11.4818 | -49.686501 | 2026-09-10 00:05:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29a40e78-e63c-31d4-8072-c8d03f442ac3 | -7.0522 | -42.703701 | 2026-09-10 00:05:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 318f52bb-b5bc-3f1b-96aa-2640fc1bb5af | -19.815201 | -57.9804 | 2026-09-10 00:05:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 883d51f9-7f56-3120-8938-83ac206a94db | -6.7593 | -44.560101 | 2026-09-10 00:05:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ca299ef-5e27-3e63-ad59-eac4c32ad969 | -6.1699 | -44.640598 | 2026-09-10 00:05:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 833a997b-c0c7-3959-91d1-c88ce49ec42c | -7.5005 | -45.262001 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c5343dc-899d-3bb7-aaea-8fb5907caedf | -7.9919 | -43.9688 | 2026-09-10 00:05:00 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cb629f2a-cce0-3135-ab74-1c942e988e5d | -5.588 | -45.373501 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad4f68d7-76d5-38ca-b8f6-96f6af7e9929 | -9.6975 | -43.4603 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6d6ac87e-99f6-3842-8cbe-93dbe15ce7ee | -4.8104 | -42.757 | 2026-09-10 00:05:00 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7448478c-bebc-36a5-a168-19d4c63a2598 | -2.9374 | -50.477402 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 437f01d6-dfba-3d4c-aff6-0a6154d19c9e | -3.2456 | -47.243801 | 2026-09-10 00:05:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b1e8dfa-4707-3e65-b7fe-3ca3cbf9e9aa | -6.8146 | -43.047001 | 2026-09-10 00:05:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 99247b19-b7f3-3712-a1e1-4603fe2740ff | -6.8473 | -47.898899 | 2026-09-10 00:05:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4629dab-b5f7-3bac-b111-edf242b1f103 | 2.4744 | -50.829899 | 2026-09-10 00:05:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 04eb0300-afb1-3165-bc72-0207e126de1d | -12.3488 | -48.193001 | 2026-09-10 00:05:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5bc9624-5cce-3de1-9b92-817b82c0318e | -15.3275 | -47.2384 | 2026-09-10 00:05:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e081223-1cc0-3076-8b05-f2565253bda1 | -7.4652 | -46.134701 | 2026-09-10 00:05:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03f2abf5-968e-3876-bd1e-e8487d59b48d | -7.5652 | -47.202202 | 2026-09-10 00:05:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c123ea2-4042-3349-b868-395ed758b940 | -12.6388 | -47.084301 | 2026-09-10 00:05:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e84b836f-3636-3742-8572-72db7c772efa | -7.9897 | -43.959499 | 2026-09-10 00:05:00 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7ab4e8af-d630-3be5-9afd-7460bcbcc28d | -2.7303 | -57.605301 | 2026-09-10 00:05:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b5f435d-0239-388d-84d6-a341bb481f53 | -15.7845 | -43.559502 | 2026-09-10 00:05:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7c50e215-6eaf-39c1-96ed-615b8c95b90b | -4.8133 | -42.769402 | 2026-09-10 00:05:00 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d4b1462f-8228-3cda-87bf-33aecf6f1f4c | -10.9362 | -50.777401 | 2026-09-10 00:05:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4142af3d-4b59-3e54-87ea-217eb31f7ff9 | -12.831 | -44.312 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d22ac33-779a-3a14-b03c-8e3fdc33af20 | -10.073 | -45.456501 | 2026-09-10 00:05:00 | METOP-B | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a953f313-17f8-3c1b-acd1-e709765530a1 | -18.870399 | -48.930599 | 2026-09-10 00:05:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f27c9c45-3cbe-3927-bce6-5dfe23121db6 | -1.7037 | -55.0159 | 2026-09-10 00:05:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a032749f-f746-3cca-a88a-281ca5bc452b | -7.9821 | -43.9711 | 2026-09-10 00:05:00 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0890140b-c972-35c8-a0f6-c953581a1a2c | -12.8584 | -44.606701 | 2026-09-10 00:05:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb343764-4dbd-3b01-a136-1f1d6e0fa65d | -9.7131 | -43.395599 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 62448356-a92d-3dd5-a8b2-d71c37904f10 | -12.8407 | -44.309601 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b813a464-19e1-3b99-a5c4-25e189274af4 | -12.823 | -44.322399 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9407ed49-5e17-37d7-a3b5-be6a4d9dc0c4 | -5.7712 | -45.097198 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b58c2fd-54b2-396a-801e-1ec28d1051e3 | -14.1971 | -41.598499 | 2026-09-10 00:05:00 | METOP-B | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e53c9670-fe75-3b8d-97a7-0b591f1c3dfd | -8.9517 | -44.9823 | 2026-09-10 00:05:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 70cb2927-65de-33f5-93be-04df6aa2538f | -12.8347 | -44.327999 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c9f20961-54ae-3429-9a7a-6437adfc5451 | -9.7206 | -43.383598 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 50933ed7-5376-3543-8663-c0704620b933 | -7.4669 | -46.1422 | 2026-09-10 00:05:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf33bab1-55db-37d9-b061-07f968d20560 | -7.4571 | -46.144501 | 2026-09-10 00:05:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04694519-0530-3e2b-bb4a-942a6e2d9942 | -4.0351 | -50.873299 | 2026-09-10 00:05:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90603479-0b27-38b1-8ed6-7e41d18f326d | -5.647 | -44.299999 | 2026-09-10 00:05:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc9e4153-63cc-33fa-933a-7800ab0c1e1f | -8.6325 | -47.363602 | 2026-09-10 00:05:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f156cd11-f3af-3ff2-a887-a3c857980c27 | -5.7554 | -45.073502 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44e948a3-2da7-33ee-9790-eaad7ac0b42e | 0.2505 | -51.457298 | 2026-09-10 00:05:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf2eb1d-9406-3f6d-9c99-147329ff2106 | -3.5766 | -45.007301 | 2026-09-10 00:05:00 | METOP-B | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10f3943b-1de4-320c-b8b7-405d31d9efe9 | -7.9745 | -43.982899 | 2026-09-10 00:05:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 487ea7e4-e884-3c10-80d6-9d9dcb733bde | -6.4766 | -46.2747 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c6b2a96-c16c-341a-9343-ae2c13abb0ec | -12.8189 | -44.348801 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50985fb5-05e5-3433-8ff2-b2cf49d8daa3 | -2.1585 | -45.9137 | 2026-09-10 00:05:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc1d8fb8-8fdb-3ab7-b6cf-2906c62d0f9e | -3.9592 | -44.3493 | 2026-09-10 00:05:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e8ee637-807d-340d-9b3c-315a6f8f398a | -9.7802 | -43.4604 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d610fb6c-960e-3fa6-90ad-29f0dc07b2cf | -2.9327 | -50.456402 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a461e25f-4510-3041-95cb-a7330bb074e5 | -10.7501 | -45.933701 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 692ef26a-368d-3d98-b00a-91647cf91020 | -2.7341 | -57.6227 | 2026-09-10 00:05:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a75f8555-09bb-3cea-bc75-f476b0c152ac | -14.1145 | -44.0159 | 2026-09-10 00:05:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e6ae5e4-9ce4-3d43-a0fc-64dec170da7d | -3.2608 | -50.0839 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c6d9711-151c-3aea-af37-ee7c00bafbbb | 0.2815 | -51.411999 | 2026-09-10 00:05:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1d3b1f2b-dedc-3a2a-b4fa-681e405839d9 | -5.3778 | -46.293301 | 2026-09-10 00:05:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91657491-b262-3b35-bc87-887a5da7f7bc | 2.5121 | -50.845501 | 2026-09-10 00:05:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce060eb-e0e1-32c3-acd3-91690c1c4943 | -9.7876 | -49.171001 | 2026-09-10 00:05:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a0a9aa6-3f22-3134-aec8-b75a37096a7b | -9.6877 | -43.462601 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b6cb7168-8f91-398a-a756-db42f3ac572f | -5.598 | -44.840099 | 2026-09-10 00:05:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36ddb317-1e31-3cb9-95ea-5500d6962f16 | -8.6883 | -47.976299 | 2026-09-10 00:05:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f834e5d5-dd59-333d-b048-b6d74d78fa2e | 2.5137 | -50.838699 | 2026-09-10 00:05:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1d750479-30d3-37e0-b120-3573bbfeee82 | -9.7779 | -43.450901 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
