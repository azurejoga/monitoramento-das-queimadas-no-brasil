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

## Dados Diários - Página 335

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 337ea0b7-27ff-32b0-8fff-ffd49a6eb344 | -10.67303 | -47.81505 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 71cb9e26-683a-39ba-bc4c-a2f6b053fd51 | -11.08961 | -41.31863 | 2026-10-08 16:37:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ebb5e97a-6331-3678-9ebd-5ba74507048c | -11.76452 | -45.52569 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9fb9af53-aa76-3eef-940a-40d2ab72cbc7 | -6.80071 | -45.05791 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 566876d2-c56f-373b-ab86-7d1d53351b71 | -11.38574 | -47.73156 | 2026-10-08 16:37:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6603ce27-09fb-3434-a3b9-0d2ebc928b39 | -8.30506 | -45.46156 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1f403ad6-ff77-393d-9337-261347cb0e59 | -6.33269 | -43.83144 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f6471738-25a7-3a54-a0f0-ec2a9dee64ee | -11.23956 | -44.01939 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 0e3c7867-bde3-35f4-8adc-282191461a90 | -6.53222 | -45.38649 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 432622a2-821d-34e3-b98c-af7d793b2126 | -8.60789 | -45.64397 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dbacb7a6-77d7-31c7-9d2f-25070727aa4f | -8.78182 | -47.37379 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f955a710-ce6c-3330-9a8c-6c7b9e2a0a9a | -8.94525 | -45.18814 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 9073bf81-e2c1-3204-97ea-3ebefa39c573 | -7.51097 | -44.42512 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 12053f54-45dc-3f76-aae5-ac46ba33d033 | -9.53293 | -45.61473 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d6e38453-6b08-3c16-8282-8f226da56dfc | -11.93535 | -47.20869 | 2026-10-08 16:37:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5426c5f2-81f5-3805-8d38-21b137cd0213 | -8.30889 | -45.73107 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5661851c-17bb-36e3-bbe3-ac6019b6e55b | -10.85018 | -42.81121 | 2026-10-08 16:37:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 372da8fe-51cc-3834-a80e-51c8e1ae1462 | -11.08694 | -44.02215 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 54ebeb45-145f-3258-b451-15808c60a9d9 | -5.75124 | -41.71661 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 8cc1cf85-3016-3bf1-9b44-b467024fca76 | -9.39859 | -45.89368 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae3acd8f-67c2-3942-b9b8-dc655de2876d | -7.61072 | -44.80868 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 76e3ba72-cf7e-312b-8115-e9a03c337994 | -7.82252 | -38.85646 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 6e72c390-16bd-36d5-9484-63b5176c2e2d | -8.07743 | -45.61489 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 6f63a588-e120-3470-be55-7c42e8ef0165 | -10.74597 | -48.54367 | 2026-10-08 16:37:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| f2025f97-f27f-3b9b-b9e2-0a90e0bf9ab7 | -9.44241 | -44.60259 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 89bac1a4-54e3-3c85-94f1-19ab58b350e2 | -7.87795 | -54.97061 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8b824106-b7a2-33fd-bba3-01afbbf1ed20 | -9.89656 | -44.86232 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 00596d15-9027-3e82-8fd4-45b903dd2331 | -10.58099 | -47.29771 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b2cac3f2-5f14-3797-953c-87df55959dd2 | -6.32425 | -35.13461 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 22b9ecc0-30f5-349c-a721-05fc8930aac2 | -11.77758 | -45.56736 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 845defe1-a303-3eba-8693-4a0341bef072 | -12.77806 | -44.86913 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| a3ccc025-252a-32f3-a46c-62691ef1ca58 | -13.14368 | -46.34034 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4d3077ed-6a38-3abc-87e4-ef0b9ab9d534 | -6.89284 | -43.83086 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e78e3be6-c293-37cb-8a1e-ca93806f2989 | -6.44224 | -45.92983 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cd8aecb5-a930-3310-bddc-70df94bf1495 | -7.94588 | -50.96357 | 2026-10-08 16:37:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d5493249-ad03-3ad9-85ae-78be0991ebaf | -9.84462 | -47.85061 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1aed13c1-2aea-3f35-b64c-0ea4ce1bee5f | -6.67415 | -45.38205 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 13831395-f1ed-3632-9554-eb83ac1247cf | -5.53364 | -39.85275 | 2026-10-08 16:37:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0af0750e-3dde-3a6f-8961-4835baf7375a | -8.52419 | -46.91173 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1ee6829-5b48-35f0-b873-b5f789e0dd9e | -9.78888 | -44.77963 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 78879c6d-9e20-3f8e-86bf-3454db073f5f | -8.81378 | -48.48664 | 2026-10-08 16:37:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bc6e676-df8c-3244-9646-1c10711b44dc | -10.42293 | -47.26215 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8d64e4b5-601b-382a-a29e-865537150478 | -12.84477 | -39.96056 | 2026-10-08 16:37:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 683ec446-27bb-33a2-b094-28b7daae10b5 | -9.35986 | -45.95044 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 269.0 |
| b5f788b6-a918-3ad8-9dbf-765008fa8ca0 | -6.3341 | -35.15534 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 19d33f09-90c7-3f47-97ef-fd8489d9212a | -8.44018 | -47.02857 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f780e993-8bf3-36e0-8935-f34cc5e021ba | -6.66634 | -40.51939 | 2026-10-08 16:37:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 64e5dc5e-e5d8-393a-9a25-57212ff21d61 | -6.45926 | -46.0192 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 525e78f8-6115-3ea8-9706-8581bef34315 | -11.15661 | -47.28868 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ea5bacbc-9f42-3acb-acd0-259fa6cea990 | -8.93993 | -45.15336 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 179be96f-4934-30c6-8463-bc4af159c588 | -13.12272 | -46.3629 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bbb75ced-3a19-3195-b3ab-bcb92ef4a1d5 | -7.84709 | -45.50642 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ecd9e863-7724-3c33-8a2c-209b333df99b | -7.18906 | -44.26288 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 382ab564-a82c-33f8-979e-61e840b4e82f | -11.76651 | -45.56174 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a271c84a-3b63-38fb-941c-e4241be80de1 | -7.04668 | -45.44255 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 64b387fb-3560-30f3-806a-05c7a93128f5 | -12.20562 | -48.42175 | 2026-10-08 16:37:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dcf8fa48-53c8-31bb-a861-c873f165af5a | -9.37262 | -45.94487 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aaeac214-a5be-30b7-bae1-6eba42f1069d | -13.1634 | -54.3246 | 2026-10-08 16:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 409443ba-dbfa-3717-90ce-eed1fc218c80 | -11.35594 | -43.14719 | 2026-10-08 16:37:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 11baa0d9-6351-3ecd-812c-c33d0b9483d4 | -11.27494 | -45.202 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 5d008f8c-fdae-3614-a1fa-92f0357780ab | -10.76388 | -46.61026 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2644b18-f5ca-3aa5-b725-ed4078567780 | -6.88564 | -43.69706 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| ef58fc22-de01-30bb-82cf-a42e443c5d74 | -11.19897 | -45.21503 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 518f8762-fbd9-3be2-b4e3-266d20e7ab4e | -9.02808 | -44.38049 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 2f0b3281-9092-366d-b428-3b14c280041c | -6.23066 | -35.3387 | 2026-10-08 16:37:00 | NOAA-20 | JUNDIÁ | RIO GRANDE DO NORTE | Brasil | 2406155 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 46bab5fe-4fd6-36aa-bb68-8e87842334e5 | -6.99341 | -40.45278 | 2026-10-08 16:37:00 | NOAA-20 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 51f5ef1f-0f21-36b3-a45e-7301770b612e | -8.24725 | -54.65214 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b19ccbd0-6991-31a4-9666-d96e6a360c85 | -6.88278 | -43.70133 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 44.8 |
| dc60819c-d727-3bd6-9199-e939bbfe7123 | -9.94909 | -45.96893 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 2e097cf7-2f03-39b1-bf8a-54b5295b8df6 | -11.83464 | -48.09095 | 2026-10-08 16:37:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b6fb0270-ae3a-31dc-82e9-1776cf09fa0e | -14.3265 | -52.07637 | 2026-10-08 16:37:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 22f8e1ec-017f-3904-a1e4-e27a3e21007a | -6.8532 | -39.4591 | 2026-10-08 16:37:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 9d4d7826-5962-3db3-bd4a-aa9f138451d1 | -9.91722 | -44.79827 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 04b690ec-30d3-3e3d-9da6-1b2aaecf76f5 | -7.51441 | -45.77323 | 2026-10-08 16:37:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| b423f8d6-d007-335a-bdaf-0566caba7db3 | -8.78923 | -47.37649 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cf083d19-7540-3abb-acb0-4ae41c7e974b | -7.69988 | -45.43046 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9a872b19-4079-34d7-b33e-9006e7f2cd9e | -11.7747 | -43.53475 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d1f86c44-aeca-3535-a94d-b3b71fa632c6 | -7.87479 | -54.98861 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b024589a-bc1e-3618-b66c-a38a356bcd0c | -11.24765 | -45.2458 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8cf686f5-d3a4-329a-9cd6-cbb1c202c5b2 | -11.78805 | -46.77354 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3931f4c-6167-3d3e-a7d9-7bcb923969e0 | -5.77923 | -42.05991 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 05de9d14-5588-3508-8b29-abe1b00432da | -6.7547 | -45.13351 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 14cfc8e1-2e52-36ee-8053-d0147aabfa74 | -7.18852 | -44.28146 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 5177fbaa-a98e-3006-8dac-5c20eb04c9fc | -8.53485 | -46.91381 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 23b437ed-9113-3467-b605-8e42138dd4c5 | -8.21227 | -46.32533 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4cc6676-c307-3e77-9cdd-4ea9bd12efea | -10.88311 | -57.07666 | 2026-10-08 16:37:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 77ee5408-1060-36f3-a263-f286367ce3d4 | -13.65145 | -47.67614 | 2026-10-08 16:37:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6190f1d4-dd5a-32fb-abfc-2559821a787f | -10.67381 | -54.53191 | 2026-10-08 16:37:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 98d30451-892f-362e-ad57-dabf29bb9791 | -9.44682 | -44.60911 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 61ff4776-f25f-357c-a084-a0c3fb0d4de2 | -11.77609 | -47.73185 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9cb84ee1-0dcb-35ca-ba68-3111de2dcbbd | -13.22439 | -54.50364 | 2026-10-08 16:37:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| bd70576b-5d00-3c3a-807a-19868cf4a587 | -6.68576 | -41.76891 | 2026-10-08 16:37:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 93d82695-cf86-3c22-8aa0-2d47c9591067 | -7.46418 | -42.82978 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 272b3798-5abd-30dc-a9d6-4f8971c1a792 | -12.04173 | -43.43548 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 33b6eb96-70b9-3839-8fb6-3201639c0190 | -8.94141 | -45.18518 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0944cd45-f1c0-323e-85c1-7f3097eb7c23 | -13.11707 | -46.34821 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1cdb540c-6c37-36b3-a30b-7e868f5a1f8a | -11.77993 | -46.79007 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fe831b4-a758-35d3-891f-ed294d2d436a | -6.53104 | -45.4009 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 21797b66-d389-3f28-b9be-882ad205b899 | -8.85968 | -49.74384 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| db3ebbaa-52a4-3706-a598-a689e5a109cc | -18.53791 | -43.24238 | 2026-10-08 16:37:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README336.md)
