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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9b0ed41-815d-3e2f-b1cd-ead181057f90 | -10.27724 | -47.0359 | 2025-09-14 12:17:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 059ed9bd-0450-36a5-b349-808c1d6eaa13 | -10.74073 | -46.44498 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3af43e20-6e2f-3f83-9014-6e96b0893568 | -8.93134 | -46.13399 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 35a7d25d-3973-3b1a-988d-90e753fea7ee | -8.44334 | -47.228 | 2025-09-14 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 0affc870-23ef-3b55-b173-5b47b0a2b226 | -7.47698 | -46.12874 | 2025-09-14 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 0388891e-4aa0-3425-ae1e-b714b3100b41 | -11.7822 | -46.63287 | 2025-09-14 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 25c58452-0966-3642-be7a-ce3f2f033924 | -12.77199 | -48.02709 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 5b27cbf5-8f3a-3ea5-92de-51cf97b22046 | -7.60754 | -46.69307 | 2025-09-14 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ad737aae-7e56-3fab-8301-af2c193b53d6 | -9.71274 | -46.86345 | 2025-09-14 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4c3b8441-5f9e-394a-8b25-743d45b9b718 | -8.88906 | -45.45796 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 0cacf301-30d8-3cc6-9ed4-729406cbf053 | -8.77071 | -46.04069 | 2025-09-14 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| ced656bb-b863-3d1a-8271-a39463423887 | -8.44204 | -47.23693 | 2025-09-14 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 41103b32-2de9-3218-96b7-adab3f9b2737 | -11.63008 | -46.92878 | 2025-09-14 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7e0301cc-60ca-369b-b1ea-1397f084a467 | -11.77962 | -46.65114 | 2025-09-14 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 5a1b3bde-235d-31eb-80fb-5e7f7bc95525 | -8.9474 | -44.44005 | 2025-09-14 12:17:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 447e3816-45fc-373a-9091-2d2fe1d92afa | -8.93445 | -46.18639 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 66ec961b-dc8c-323a-8bac-8eb502e20a27 | -9.86234 | -46.4617 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fe66a5c6-7568-3293-9f15-31e41a0dad9a | -9.76751 | -41.90287 | 2025-09-14 12:17:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| b6908254-1c93-3a0d-829d-ba9356ef5c1c | -5.94128 | -44.86568 | 2025-09-14 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 976786b9-1293-307c-b60e-97404cc7d6c7 | -7.8785 | -49.50343 | 2025-09-14 12:17:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 1d120df8-d011-3f8c-993e-f8142a1b1a1a | -11.72586 | -46.9028 | 2025-09-14 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6b747c6b-6592-34bd-a61b-63b949fedfac | -12.05346 | -46.53968 | 2025-09-14 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2ecffaf4-7ace-3fae-b8b9-bfd64259495b | -8.98179 | -45.77952 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 66a358f5-a5d3-3265-bd5b-b0e12f9f5fc2 | -12.14609 | -47.57932 | 2025-09-14 12:17:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c6ffa11e-799b-3591-9e0b-9c8b5656a41c | -11.50258 | -50.8112 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 6a94062c-0dab-3cfa-8b4d-929c215daea9 | -12.8131 | -47.16087 | 2025-09-14 12:17:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 76f9f329-ce44-3097-a59a-5cfb034e83f3 | -12.81568 | -47.14272 | 2025-09-14 12:17:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| d4abba9d-9ad5-33f7-95f9-2e191125504c | -7.23217 | -43.84398 | 2025-09-14 12:17:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c0447539-4402-350b-b1a8-774e7fbf5862 | -11.82869 | -46.3675 | 2025-09-14 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 50d0050a-e798-3a9b-9cea-0d44acd4f9be | -11.23585 | -47.62293 | 2025-09-14 12:17:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| ed136774-c2fe-3aa9-a57a-5ddce5af29cc | -10.8873 | -45.45108 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 35ea521c-c7c6-3dc9-b4d2-8110e277e68d | -12.76444 | -48.01676 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ccd5bf3b-9b8a-3ac8-92bd-044e6dd414c8 | -8.99698 | -45.80637 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 24891276-0d17-3e90-adcd-66dbfe5834d8 | -8.89813 | -45.45913 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 8ac943b7-fedc-386a-a715-c0bcd9191183 | -9.57026 | -48.03493 | 2025-09-14 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 65e0ffb8-3f50-3873-955d-f9340cdc0880 | -7.20198 | -44.13831 | 2025-09-14 12:17:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 69c29c2d-c474-3adf-909d-2dd79486ce59 | -10.89841 | -47.2048 | 2025-09-14 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 260067e5-b48e-38a4-a1d4-3cb61467619c | -12.51006 | -44.75891 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 49bae2a3-8a10-3231-853c-2a0e9a6057b8 | -11.63134 | -46.58974 | 2025-09-14 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b418a499-e401-3cc7-a20e-e1c15db9909f | -7.31148 | -43.93721 | 2025-09-14 12:17:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 83398969-e1ff-38d5-a241-460e992ece89 | -10.34307 | -50.48779 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 4821ce3c-b617-381c-a618-a42b057fdefa | -13.50663 | -41.46395 | 2025-09-14 12:17:00 | TERRA_M-T | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 51.4 |
| eae97d6c-06c0-3795-8cae-ad5206cbc3cb | -10.92509 | -45.58515 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 1c87d09c-3bfc-3455-9545-8ad493f1ee65 | -10.53329 | -51.55185 | 2025-09-14 12:17:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 4d14814c-0f49-31ad-abf9-639d27041e67 | -7.5987 | -46.69182 | 2025-09-14 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 98dc4af2-76db-3352-8d76-464c13bac1f5 | -6.98117 | -44.54337 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1be63689-7a65-3570-9364-741115662fc3 | -9.738 | -46.87613 | 2025-09-14 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| de7c98a1-515c-3a27-b30d-982ec58a2364 | -11.56442 | -47.45117 | 2025-09-14 12:17:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 613057b6-09a5-3e9a-9cd4-b9dd749c8e66 | -9.13636 | -46.96199 | 2025-09-14 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2e90b7b9-2332-34e4-9b05-71a62c04693d | -9.07555 | -50.26453 | 2025-09-14 12:17:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 59ebd205-1a2b-373b-8ff1-0ffd525b553e | -11.40612 | -50.43987 | 2025-09-14 12:17:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 466dd550-de41-3f0e-add8-b00d81509be4 | -9.56892 | -48.04409 | 2025-09-14 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7f4af1a2-0393-3d38-95d2-a165c66b20be | -11.76276 | -50.52077 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| bffcc884-9501-3ae8-b905-ecd866ff50b6 | -8.43318 | -47.23566 | 2025-09-14 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| aec13513-95eb-3e71-b2ca-644ae9e1443b | -12.44678 | -46.8885 | 2025-09-14 12:17:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 9ca586ce-b7cb-371c-b168-9add27c1bca3 | -7.71842 | -49.68887 | 2025-09-14 12:17:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| b3fe5f8a-ef4a-3e94-9c38-dadf12bec07b | -8.42561 | -47.22547 | 2025-09-14 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8c4f1dd8-c3ea-33a4-a5ed-6ceacff536a2 | -6.38291 | -45.65022 | 2025-09-14 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 585bc063-4338-3587-b17a-db27dd15f55b | -10.75345 | -46.48382 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c15e6bed-b0bb-38c4-9d67-1f21a8d690eb | -13.55145 | -43.82288 | 2025-09-14 12:17:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3889afe0-81bb-3ca4-9bde-2561aa857e72 | -6.97983 | -44.55305 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cca06dcd-383b-3d97-8921-14abd1c9b166 | -6.80799 | -38.18364 | 2025-09-14 12:17:00 | TERRA_M-T | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 40.7 |
| 0b08e736-05ea-3cca-b984-ef01e41cafeb | -10.78621 | -45.98551 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| f0ccaa6f-32a8-30b9-860c-734666333a96 | -8.99312 | -45.76849 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7a5e9e23-fe83-3a62-b94e-adc71233c7da | -6.9891 | -44.55422 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 06a45f0b-404b-3271-b10e-781aa1317294 | -8.90588 | -45.46977 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 5e84edc1-5d2e-39f0-9beb-4791b4b4e41d | -8.98048 | -45.78874 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c351fc21-bf3f-3808-a78b-a6d2402ab697 | -11.38572 | -47.34885 | 2025-09-14 12:17:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bd977599-bb52-302e-8362-4ce4d1a2f87a | -10.75089 | -44.77618 | 2025-09-14 12:17:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cb20df60-a1b8-3b3f-91c1-66cad781736a | -9.1002 | -44.80497 | 2025-09-14 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| aee86e57-7aa5-3609-bba6-269561027761 | -8.90713 | -46.17651 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| e9addbde-56fe-3bee-a2e6-601eab80cd10 | -7.69858 | -44.68127 | 2025-09-14 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2d17e9f4-201c-3c07-936c-34dc3b45bdd2 | -6.68348 | -45.54585 | 2025-09-14 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 476ab6a4-9c9b-301c-ad32-099122ebdf66 | -13.54156 | -43.00327 | 2025-09-14 12:17:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| f273309f-f6e2-387e-99c7-4650a9bf0eb3 | -10.89705 | -48.17316 | 2025-09-14 12:17:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1bde10da-2e64-3081-993b-6610380886fa | -10.80357 | -45.99374 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0ff6340f-d7a6-3687-822f-1660a2d9e3fa | -11.44913 | -43.91589 | 2025-09-14 12:17:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| e7666685-1461-3387-a2ef-385fe4dad156 | -10.91862 | -45.56433 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3f76e958-f404-3c0b-95a7-334109357709 | -10.73141 | -46.43772 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| e54ff6de-2b97-3f21-b009-f6cbfacabe00 | -8.64278 | -45.70426 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 6cd0e4b9-8a6b-34ff-944e-6e198e3014c7 | -7.06094 | -43.89458 | 2025-09-14 12:17:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c6d5b17c-9690-31b0-9666-1a467d984afe | -7.55449 | -46.73373 | 2025-09-14 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 1a306237-58a1-352c-b9a3-3965bbbf0de8 | -10.90946 | -47.20373 | 2025-09-14 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c8420db5-73ad-3110-a32e-9793521670bc | -12.79887 | -47.9664 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 1afc10d1-145c-3a8e-8d31-7b30e27d6f9d | -11.4486 | -46.90887 | 2025-09-14 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1000ab28-e8db-3431-8097-5fff98752dd6 | -11.4795 | -50.76456 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ea989ea5-a5bf-3c69-aa73-b8e22741b29f | -6.42686 | -42.62125 | 2025-09-14 12:17:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| 42db8740-6c8e-3f1d-8091-b905b201c820 | -6.42518 | -42.6336 | 2025-09-14 12:17:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| c78f67aa-1ea6-3c69-87b5-a83041bda9c7 | -12.77856 | -47.98175 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| c0c7ff98-b2b8-37a6-bbc8-fc5f42101688 | -6.44338 | -43.32195 | 2025-09-14 12:17:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b2994e10-6202-3141-9467-88efd8af0193 | -12.13508 | -47.58046 | 2025-09-14 12:17:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3cacf3b1-6558-3a0d-8910-17831963edd9 | -9.71147 | -46.87236 | 2025-09-14 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 72d73826-17e4-32f5-9c6b-ec5cb4a291d2 | -11.33101 | -51.13312 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a6688116-41a6-3f1b-8682-6463e17b9952 | -7.5256 | -47.63894 | 2025-09-14 12:17:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 62b05d96-ff83-30a4-8163-4f6fe1625cb0 | -11.44877 | -43.90944 | 2025-09-14 12:17:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 3b412720-e808-3dda-aa43-141d2df89dea | -6.99972 | -44.54569 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| be31a3c5-b7f3-3f45-a30a-052fd9a5a2c4 | -6.72857 | -45.29311 | 2025-09-14 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b8dd6c60-3d94-3a26-8ddd-6b260affbf33 | -12.79757 | -47.97534 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 52a90614-74e6-3155-92d3-da7d0130f492 | -11.14626 | -45.31802 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 707ac0dd-ab4c-35b6-bdff-3ef3dc6eea19 | -10.27851 | -47.02698 | 2025-09-14 12:17:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |


[Clique aqui para ver as próximas entradas](README79.md)
