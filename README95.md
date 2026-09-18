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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f09c7a05-9774-34fe-82bf-6b5d5cb133f9 | -8.4329 | -45.7337 | 2026-09-18 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 103d0962-a053-3390-a05f-0eb707bbb037 | -4.5587 | -42.9523 | 2026-09-18 13:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| a55b0b39-0e08-3576-a223-a550cefea3ed | -7.6574 | -46.1013 | 2026-09-18 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| d29115fe-06f9-3dac-8b66-44b565dc2ab4 | -12.1719 | -46.9906 | 2026-09-18 13:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| d4931bfc-8812-35ab-a437-e68bf18f2145 | -10.3772 | -49.9508 | 2026-09-18 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 89a9df8d-afe0-3418-805d-02d919b5eac1 | -11.8753 | -47.5679 | 2026-09-18 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| dc3afbc4-5fac-328f-a8b2-6c44104e040d | -10.6536 | -50.4778 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 1b1d6d1a-f110-3a64-8a3f-57345ebe672d | -10.3307 | -45.3112 | 2026-09-18 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f8a1f6b3-d428-351f-96f2-472756c200b4 | -11.3437 | -44.0141 | 2026-09-18 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 207.8 |
| e663d45f-f6cb-3456-b807-32fbb74e2827 | -10.6379 | -50.2446 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| cc41ef66-da97-33c1-8a4e-24c73f409d4a | -14.7303 | -50.2894 | 2026-09-18 13:00:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 9d12ceb3-fc6a-3c4f-ba4f-1f3dae2f9df7 | -11.2783 | -43.388 | 2026-09-18 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 942203fb-d427-3152-b980-dc4feb8ffdb8 | -10.6189 | -50.2466 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 6f52b853-f3dc-3778-8179-1f97ff50c52f | -10.6533 | -50.4991 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| e528ae9b-ca89-3a24-8a03-20d564156e7d | -12.0676 | -47.4974 | 2026-09-18 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f5bc6d6a-7f2d-3a63-be81-e6ec64eba9fe | -10.5181 | -46.7142 | 2026-09-18 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3ab046ce-b59d-3b9d-9cbc-cf97129f77b9 | -10.6726 | -50.4758 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 37c2c472-f6b9-3609-abb9-8f342e583f53 | -9.9505 | -45.336 | 2026-09-18 13:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| fd9ce167-03e3-356f-974b-fb36944c51a5 | -10.6187 | -50.268 | 2026-09-18 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 6a96f90a-620b-3706-b56a-90c7b5cd3286 | -19.5545 | -47.6113 | 2026-09-18 13:10:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 30955e9b-5552-3245-a6ac-09e5d751ee46 | -13.6341 | -46.9304 | 2026-09-18 13:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 125.6 |
| b6e2d046-210b-37ba-9751-e66b91a363e7 | -10.6726 | -50.4758 | 2026-09-18 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 170.6 |
| cd5ff5d7-d7a5-3b75-ac42-aabed5110ec2 | -7.0352 | -44.6396 | 2026-09-18 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 3910dd42-4866-3b57-9501-5fb8dd6cda70 | -9.9502 | -45.3589 | 2026-09-18 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 125.0 |
| fc9e7e3a-7578-3de7-8214-905f3b49a6fc | -11.3442 | -43.9906 | 2026-09-18 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| b1a4584d-ac8c-37f0-a184-b149907ec08b | -11.3617 | -44.0817 | 2026-09-18 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 62d6507b-af64-3917-b8e2-a66987f930f2 | -8.3769 | -47.236 | 2026-09-18 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| e1ead036-9f98-35ef-a57b-e88344ae952a | -7.6577 | -46.0788 | 2026-09-18 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 2546d72e-8d69-3b06-aac7-1a181d809c83 | -13.4303 | -51.9036 | 2026-09-18 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 259.7 |
| 01fa7b8a-4d6d-39f4-95d0-61e11041f35f | -9.8316 | -48.3854 | 2026-09-18 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 2284646b-cc4a-3d16-a153-6604e109ab90 | -12.0672 | -47.5198 | 2026-09-18 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 1d6700fd-7952-3ba4-856e-51aa5d26dbbf | -8.4506 | -45.8222 | 2026-09-18 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 91bb90b3-2dc9-3ed1-9cf5-5ce865cecc0e | -10.6533 | -50.4991 | 2026-09-18 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0b204878-7435-3caa-a0d0-adb6ca60a687 | -10.6755 | -50.262 | 2026-09-18 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| e2e558d5-ad43-3adb-a9ea-b7ae81f411cd | -7.3546 | -44.6334 | 2026-09-18 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| bc465d5e-0dd4-32cb-9b2f-768672c78fd0 | -11.3809 | -44.0788 | 2026-09-18 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 8947de6c-db33-3a7f-9c78-e189ead52b1e | -14.1737 | -45.1641 | 2026-09-18 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9d629e86-6f50-3a8a-a4e1-a19353cc163d | -12.0676 | -47.4974 | 2026-09-18 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 3e6bb23d-f0eb-3559-873a-0bf0654edff3 | -11.0636 | -48.3118 | 2026-09-18 13:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| adb9ed7a-3867-32f2-ad7a-1a7b5fe267d3 | -11.3437 | -44.0141 | 2026-09-18 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 182.2 |
| c7acb52e-e58b-3778-a67a-533581c5d7a9 | -11.083 | -48.2875 | 2026-09-18 13:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 32cef0c0-5ae7-3bf2-8fef-e03e855865eb | -11.0643 | -48.2678 | 2026-09-18 13:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 60b9925d-17d7-3bda-95bc-dfbb73b26a32 | -11.2975 | -43.3851 | 2026-09-18 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| c0387f7c-17d2-34c3-a3d0-a1efac7e1377 | -12.998 | -46.9381 | 2026-09-18 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 5f607175-1d5e-3678-a9df-2066b2296d68 | -8.4675 | -44.4984 | 2026-09-18 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 56fee2f6-9f4b-3986-9fb0-26c40986a81d | -10.6758 | -50.2406 | 2026-09-18 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 6dc9d733-b116-36f2-a843-cb75d632712d | -7.5494 | -45.6839 | 2026-09-18 13:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4f59354f-d182-3bde-b5ea-766517ad2f81 | -19.5539 | -47.6346 | 2026-09-18 13:10:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 150.1 |
| be2530a3-4923-345e-856c-b7e943df730f | -10.6379 | -50.2446 | 2026-09-18 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 8bf65975-e452-309f-b622-e22d73561f01 | -8.6817 | -45.4359 | 2026-09-18 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 43956a39-28be-3a28-ba01-1dbe81a2f441 | -9.9505 | -45.336 | 2026-09-18 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 141.8 |
| e2d9de70-27cc-34f0-b447-f4baf18142ff | -13.4307 | -51.8823 | 2026-09-18 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 69fcd479-2ad8-393d-b364-730147ab4d1d | -7.6574 | -46.1013 | 2026-09-18 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| b15df97b-b26f-3f59-95c7-84355e5fb1f8 | -14.1732 | -45.1875 | 2026-09-18 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 64fb59ee-6e1b-3510-9d09-eeaef78d2203 | -13.6337 | -46.9531 | 2026-09-18 13:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 960165ea-6ef7-3095-97c7-934b41951d81 | -10.6944 | -50.26 | 2026-09-18 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 16588bc9-dbef-35f5-b29b-fca1031fd641 | -10.6376 | -50.266 | 2026-09-18 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 2c81346c-3c3a-312e-adb0-538d1ad42b13 | -8.4672 | -44.5214 | 2026-09-18 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 23a0c17a-5825-3242-b4bf-e6740f614ae7 | -11.064 | -48.2898 | 2026-09-18 13:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 677c78ba-9612-3bd0-846c-b694a714c32b | -8.452 | -45.7092 | 2026-09-18 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| f4036fc2-4516-3fed-8d43-5bfe7cbb9c28 | -8.4503 | -45.8448 | 2026-09-18 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 1b4ff65a-43bc-3b47-9adb-73052872f0b2 | -10.6536 | -50.4778 | 2026-09-18 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| c875d442-b683-3ff2-83fe-8e0d2105bd92 | -9.9315 | -45.3383 | 2026-09-18 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| f9cdbe28-bc8c-325c-87cb-1efef3a1ebe9 | -11.8115 | -46.8158 | 2026-09-18 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| a24dd308-f617-3e70-b568-e6a9e85ab7f5 | -10.6723 | -50.4972 | 2026-09-18 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| bb7c2253-c28e-3cda-963e-508569d864d2 | -13.2485 | -46.9226 | 2026-09-18 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 58dbed32-4bf2-3520-9e52-756a21d3a9a7 | -10.6189 | -50.2466 | 2026-09-18 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 2c80155c-fdf5-3dee-ad1f-7cc625004762 | -11.4861 | -45.7279 | 2026-09-18 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 152a89a0-c029-38b6-b0c6-b0975818469e | -10.5178 | -46.7366 | 2026-09-18 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 86a66db3-0f33-3dc3-b982-181d2eac734d | -11.2783 | -43.388 | 2026-09-18 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| a3fa0a98-4628-3cf9-8325-a5d985a2524a | -12.57 | -50.72 | 2026-09-18 13:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 13d80803-0ec2-3be6-9ac6-34b62d42912b | -13.66 | -45.98 | 2026-09-18 13:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 63f7cf4e-5b1f-3f44-8262-397401412a52 | -4.58 | -42.93 | 2026-09-18 13:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b32cb5e-42b2-3f44-801b-e47b4fa00f3e | -4.58 | -42.97 | 2026-09-18 13:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e3d017f-c237-3aed-befe-a40a7fc1467a | -11.2975 | -43.3851 | 2026-09-18 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 571290e6-768b-3c61-b766-39c8fdae6127 | -10.6376 | -50.266 | 2026-09-18 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 7f317651-a310-3f84-8758-995a09958e2b | -14.1732 | -45.1875 | 2026-09-18 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 5b2ae234-bd50-3d81-872a-fe63451c224d | -13.4307 | -51.8823 | 2026-09-18 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| adf6f79b-582d-34a7-a77c-588e094d30b6 | -10.5178 | -46.7366 | 2026-09-18 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 72e55c51-16d2-37fd-8e5a-471b4c4538a7 | -10.6189 | -50.2466 | 2026-09-18 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 7a0f53e4-e2d7-3a90-9428-13b1a0252570 | -11.8556 | -50.0006 | 2026-09-18 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| ebc81826-e074-3fc1-bdb1-54d3dd280d4f | -10.6379 | -50.2446 | 2026-09-18 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| e6396978-ac1b-3f80-8100-236bb7d1c8b4 | -10.6755 | -50.262 | 2026-09-18 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 6d13e530-c8f6-3990-91f3-cf275be9288e | -12.998 | -46.9381 | 2026-09-18 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 8d46e6bd-8ab9-3640-82fa-340a42e5f799 | -11.9118 | -50.0585 | 2026-09-18 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 839709e4-3571-3fab-a000-c447f198e379 | -10.3769 | -49.9723 | 2026-09-18 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4aaa7aab-035f-3bc8-bdea-fe920bfe47cd | -10.6533 | -50.4991 | 2026-09-18 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| bf430357-a8af-3e2c-a995-8a06fdb4c8c8 | -11.3617 | -44.0817 | 2026-09-18 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 8f2c4350-f7df-3300-9b15-30d13b4ce6a1 | -10.3772 | -49.9508 | 2026-09-18 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 135bb3e4-343d-34e3-9191-1ea5b8e8c74f | -11.064 | -48.2898 | 2026-09-18 13:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 46747358-812d-3bc8-800d-e7b5af66a202 | -13.2485 | -46.9226 | 2026-09-18 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 4f607968-c2c8-3b48-903e-5faf6579a8cf | -10.2632 | -50.0055 | 2026-09-18 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| f5f08f1a-f37a-3f9f-930a-707c719d3c55 | -11.2971 | -43.4088 | 2026-09-18 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 8db8b4f6-e765-3cdc-be3e-99fff653d65f | -10.5966 | -46.5474 | 2026-09-18 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 6ba6341d-a6e6-3d55-80af-855e0b698680 | -12.5879 | -50.7285 | 2026-09-18 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 11e7728e-376c-30fa-8c52-ed826a4f1181 | -11.3809 | -44.0788 | 2026-09-18 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 203.1 |
| de0651e2-09b0-3b15-8315-39e9b8994bdd | -11.0643 | -48.2678 | 2026-09-18 13:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 4aad5ec6-b22d-3d0e-98e5-ad9cd5fb9b56 | -10.3307 | -45.3112 | 2026-09-18 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 56271232-cd28-3a16-95b4-c5564aca74fd | -11.9115 | -50.0801 | 2026-09-18 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 78107672-ec3a-3289-90a7-3bcb0a0b3bea | -11.8115 | -46.8158 | 2026-09-18 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 175.7 |


[Clique aqui para ver as próximas entradas](README96.md)
