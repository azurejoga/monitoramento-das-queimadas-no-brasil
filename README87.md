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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7977df09-9434-3bb8-ba9b-ffe82bff0d4e | -14.7527 | -60.2321 | 2025-09-14 14:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 32144df4-890f-39e8-8a51-021c73da042c | -9.4978 | -47.9389 | 2025-09-14 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| e831161d-c780-3171-8533-d85142fc5052 | -11.2885 | -51.1122 | 2025-09-14 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 286b86ce-27a9-3d67-90c4-be4011a2f478 | -14.2917 | -45.0964 | 2025-09-14 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b3e6063c-0f5b-329c-8117-ca16d9d71c47 | -8.9976 | -45.8098 | 2025-09-14 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 1346cdde-317a-32a2-920d-48840619ffae | -11.2933 | -50.7716 | 2025-09-14 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 777ff7b1-e1fd-3093-8cfd-bc41a3cd189f | -10.7579 | -44.7721 | 2025-09-14 14:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 1baac63f-09c0-3561-a92a-1845b372cb1f | -8.7871 | -46.0353 | 2025-09-14 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 1fda9870-719d-3661-969e-d2bafb7882cd | -16.0056 | -47.9555 | 2025-09-14 14:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 3e0b40e9-5132-38c1-bf1b-de17f57c73ad | -13.5876 | -51.6715 | 2025-09-14 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 330b10a2-0907-32c8-8c18-2ab567c20cfc | -14.1917 | -46.1552 | 2025-09-14 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| fb39c5d7-c725-387c-b963-b3aaef9c9633 | -9.1082 | -50.5422 | 2025-09-14 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 867820d0-aa55-3d98-b1a5-e9bef0e4bcd1 | -9.9754 | -50.3761 | 2025-09-14 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 6f3aaf4b-29c6-36ec-b0c0-2649974e9dc5 | -10.3512 | -50.4876 | 2025-09-14 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 22806538-b48f-3ad5-986f-8a1e8220ead2 | -12.7478 | -48.0263 | 2025-09-14 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 568b3e99-3338-3c7f-ba02-eb1479e9d181 | -11.3831 | -47.3429 | 2025-09-14 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| c9b38839-6766-3d5e-aa29-969b5ebe9dd2 | -14.3285 | -46.1088 | 2025-09-14 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 1d04858b-6454-360b-a51c-62ceab14917b | -12.8019 | -47.1474 | 2025-09-14 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f23d71e6-5fcf-314e-b5a7-0184c285d300 | -10.9452 | -47.3538 | 2025-09-14 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 5fa67c56-85dd-331b-9ab9-00141e117082 | -8.9746 | -46.1279 | 2025-09-14 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 248.7 |
| 8b5dacda-351d-3a07-bf30-b3094cfcf484 | -8.6436 | -44.0396 | 2025-09-14 14:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 1a3b0579-b318-3ba0-b823-70814bae081b | -8.9079 | -45.457 | 2025-09-14 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| dd320cc9-c5ac-37e3-bfb6-ca41bacb5c5d | -14.1722 | -46.1585 | 2025-09-14 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 20794f73-31e0-3a9c-878c-69959fb4820e | -10.8994 | -45.4426 | 2025-09-14 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| f1f46203-eb84-3e16-a097-a8fe3ec2d9e4 | -10.7477 | -50.5106 | 2025-09-14 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ebf31fa9-bfed-32bb-a6f2-7fcfebeb7721 | -11.353 | -43.495 | 2025-09-14 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 3978000b-b930-3ab7-a417-bb21ab5c5a41 | -14.4137 | -52.901 | 2025-09-14 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ed9b8808-2aeb-36da-8f56-1fde52189c54 | -6.9798 | -44.5529 | 2025-09-14 14:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 47bb914d-d852-34b2-a690-84e9f3023fe2 | -15.7591 | -53.4846 | 2025-09-14 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f08e7ad2-8616-33db-bec7-a06cf8cd01f8 | -8.1386 | -43.653 | 2025-09-14 14:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 832dd90b-355e-3124-9253-152849e63b43 | -14.2107 | -46.1749 | 2025-09-14 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 18c031b7-f064-3c88-a0fb-9dde5ad4989f | -13.5879 | -51.6502 | 2025-09-14 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| f7e2d124-0fbb-3938-b636-2b5463f2622a | -16.0061 | -47.9329 | 2025-09-14 14:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 3c8d45bf-9bae-307d-8ac4-800e62a7e7b7 | -12.8212 | -47.1445 | 2025-09-14 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 68cfe962-45a8-37ae-8484-7d84f5278932 | -14.1912 | -46.1782 | 2025-09-14 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 309753bf-2509-309d-ae79-e137752b2e18 | -8.6404 | -45.7122 | 2025-09-14 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| a4f0c685-2e01-31bf-ab3f-4d38d1041cb5 | -12.7671 | -48.0236 | 2025-09-14 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f4e5d0b5-65da-350a-8e35-9579228a3c4b | -10.4065 | -50.5884 | 2025-09-14 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a928fe3a-a5e4-317d-b185-2d665efbb81f | -9.9757 | -50.3548 | 2025-09-14 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 8356a3a6-82b4-3399-8ab6-8395bb280ef2 | -8.8109 | -47.1272 | 2025-09-14 14:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 4f09a70d-1eef-3f7a-8a36-72f26ea9a2df | -15.2186 | -50.129 | 2025-09-14 14:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 0e0b9774-0db6-33ac-bc4e-cce03f797274 | -12.8208 | -47.1671 | 2025-09-14 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 927226b2-7812-3f15-aa6e-6182e0d95592 | -8.956 | -46.1074 | 2025-09-14 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 391.8 |
| ab2e2e93-9b01-3faa-a545-be7df878f2c8 | -10.5586 | -51.9661 | 2025-09-14 14:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| ce827998-cc34-3e40-8451-d693fd1d39bf | -10.8991 | -45.4656 | 2025-09-14 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 230.5 |
| 065b2033-372b-317a-8b18-1ffdfc85b92b | -9.8646 | -50.1951 | 2025-09-14 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| be81a440-9c6d-3d71-8b61-6fb57ce8c2be | -12.1427 | -47.5763 | 2025-09-14 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 57c8c16c-9d93-3871-b295-7cf06b67cf76 | -12.0856 | -47.5618 | 2025-09-14 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| b9b0add8-109a-3202-bfa2-8bce5d27d7be | -8.889 | -45.459 | 2025-09-14 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 782ef9bb-b57a-3c92-989c-68f9e12cc97a | -10.3885 | -50.5264 | 2025-09-14 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 56fd1243-af82-31e0-b65f-8ece42b0dff4 | -8.9371 | -46.1094 | 2025-09-14 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 267.3 |
| 3f2fdfb5-cac2-3273-b5c3-0e84bf2d4170 | -8.1383 | -43.6764 | 2025-09-14 14:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 401e9547-2770-3aa8-b2be-5836b6c3b7d9 | -15.7333 | -56.2122 | 2025-09-14 14:00:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 53d434f2-5db4-3602-9249-a723c06ad14f | -11.2695 | -51.1142 | 2025-09-14 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| f4e2bff5-1906-3247-bcbc-7680bdb48e49 | -10.7474 | -50.5319 | 2025-09-14 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| de38d58e-04e3-3651-b417-5eb3ea1b9214 | -15.0971 | -52.4944 | 2025-09-14 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e49dd560-41f5-3e4f-bad1-2f2b1850d043 | -13.5096 | -51.7451 | 2025-09-14 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| d64c7513-b10f-3584-80dc-3ee7136415d4 | -8.7683 | -46.0373 | 2025-09-14 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| c3844f0f-c4dd-3573-9d5f-946c65fb5a1c | -15.1995 | -50.1101 | 2025-09-14 14:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 56c4f4b8-aed1-3ab0-b18e-bdbf7f94f9c0 | -8.9749 | -46.1054 | 2025-09-14 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 8da1b931-fb90-3c91-b7b4-c438a0344109 | -14.2912 | -45.1198 | 2025-09-14 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 30e9d351-448f-3a6d-9f5b-29b794579330 | -11.0391 | -51.3502 | 2025-09-14 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| cc03be35-1f44-3e06-8238-466d6f63216c | -8.9595 | -44.4436 | 2025-09-14 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 159.9 |
| fa067f9e-047b-3362-ba8f-6f48c73cf822 | -10.5451 | -51.5476 | 2025-09-14 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 6ba2c6d1-7c1b-37f6-a203-7b42ebb037da | -10.9262 | -47.3561 | 2025-09-14 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 12b5ff09-b41e-350c-84e7-7009c6dcd008 | -9.572 | -48.0408 | 2025-09-14 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 8ce37619-4808-33e0-978c-fa242a1dd200 | -8.9076 | -45.4797 | 2025-09-14 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 459d0e24-ffd4-3ee5-83ef-546eeb8d289d | -10.769 | -46.4583 | 2025-09-14 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 40f7726e-2723-36f5-8e09-e300613a694b | -8.6436 | -44.0396 | 2025-09-14 14:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 69fb1f99-a35c-37e0-97ac-30d097c145c9 | -14.3285 | -46.1088 | 2025-09-14 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 6b208b27-63ac-3422-86f0-db882e170c2b | -10.3512 | -50.4876 | 2025-09-14 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 63597504-bed6-36e4-ab7d-01eebf7fc7b0 | -10.7474 | -50.5319 | 2025-09-14 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 4fa93dcd-0e61-38de-ab0b-d28c30b88d30 | -13.9288 | -44.8106 | 2025-09-14 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| fca1a5cd-a97e-3da2-b01b-04f2330811b6 | -14.394 | -52.9245 | 2025-09-14 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| c199666c-6958-336c-99a5-897f98d5f4ec | -13.5876 | -51.6715 | 2025-09-14 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 9be5c7f1-dc53-3db1-b784-a2a227865b29 | -11.3831 | -47.3429 | 2025-09-14 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 3bfc864b-406d-3b4c-95b1-a0c9cadb78f4 | -10.7667 | -50.5086 | 2025-09-14 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 7d4a8955-d44e-303c-8bcd-0a2bdc38a36d | -7.5281 | -47.642 | 2025-09-14 14:10:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 93d9d99f-e415-32f3-8e8c-d4e4fba0a008 | -12.8019 | -47.1474 | 2025-09-14 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 908cfd86-345b-3e8e-ba86-b180b02a3a75 | -14.4779 | -47.3368 | 2025-09-14 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 863cdd2d-6744-3670-be3d-220b76398f14 | -12.9587 | -48.0409 | 2025-09-14 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a6c01bde-234c-3f1c-83e5-015ef01ef566 | -8.9365 | -46.1545 | 2025-09-14 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 51743791-1735-3697-b2e4-76635973313a | -9.0193 | -47.0394 | 2025-09-14 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 56cb142b-02ea-3368-a4d6-56bd7d788cdb | -10.9262 | -47.3561 | 2025-09-14 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 86e5114b-898f-37e7-9e48-ea28e367f47d | -11.2924 | -50.8356 | 2025-09-14 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 25447792-e57a-3aca-b734-145125b5fb52 | -11.0427 | -49.7283 | 2025-09-14 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 2530eff8-858e-3266-afe9-4af53b2bf388 | -5.9643 | -47.0138 | 2025-09-14 14:10:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e3784e61-6772-3e40-8245-df38ca9bb7cf | -10.3882 | -50.5477 | 2025-09-14 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 1d1689c8-0800-3190-a652-82b09de8089e | -8.9368 | -46.132 | 2025-09-14 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 557.4 |
| 4b438e3f-da76-3a5e-8c90-4cbc35735a3a | -14.329 | -46.0857 | 2025-09-14 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 30867b89-697b-35a2-839d-21239d9c4ff9 | -10.9182 | -45.463 | 2025-09-14 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 421.4 |
| b92202eb-a2c1-3a19-ada1-c1b746500080 | -8.7683 | -46.0373 | 2025-09-14 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 250.3 |
| 40b68347-06ee-3428-9564-117a6d2dab6f | -11.0574 | -51.3905 | 2025-09-14 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c8112d2c-e3c8-311f-9f12-33865203e9ca | -15.943 | -47.2407 | 2025-09-14 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 106.7 |
| b86aa7e4-cf8b-303a-a28a-636485c3eeab | -10.5451 | -51.5476 | 2025-09-14 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7e8fa832-6e00-365d-9a3e-0e294a97442c | -15.2186 | -50.129 | 2025-09-14 14:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| cd8970fb-8fa9-3347-ba2a-746522a510ce | -12.442 | -46.8847 | 2025-09-14 14:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 567d1b12-2306-3acf-bcd7-5f401ae5e8f8 | -6.3165 | -43.3381 | 2025-09-14 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 4817415b-e0ce-307d-baff-2f392032234a | -8.9079 | -45.457 | 2025-09-14 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 086de2d2-cdb3-3bb0-bbc0-bbc4a34965f6 | -8.9371 | -46.1094 | 2025-09-14 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 167.7 |


[Clique aqui para ver as próximas entradas](README88.md)
