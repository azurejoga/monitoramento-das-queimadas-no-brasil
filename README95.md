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
| 0a47ffb0-fa5c-3e8d-9d86-c563765087a6 | -9.7608 | -46.31103 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acdd30fb-81fd-31c1-9a10-fae6a3e848b3 | -7.75788 | -42.55419 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| cc8cde7f-9dde-3604-b023-65701613d766 | -7.88185 | -47.3197 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f184dac-fc14-3ecc-9fe4-bd7759b8d8a5 | -10.28259 | -50.37493 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32936e3e-d235-3803-861c-35f5569ed354 | -10.28728 | -50.30357 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| faf5be30-27d5-3298-849e-163ef6db2002 | -11.55771 | -47.66348 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f695af5d-2b79-3a1f-ac7b-e678d5710314 | -11.77521 | -46.82751 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9fd6850-90a0-3b55-a61c-f13a1c5e329e | -10.00976 | -50.23895 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b31382c0-8f0b-31e8-a66e-136762c86ea1 | -11.22069 | -41.60236 | 2025-10-03 04:32:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e2fab8b3-8fae-3b81-8cc7-871de0814026 | -5.83155 | -42.85845 | 2025-10-03 04:32:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 50b8d652-9933-3d06-a365-36d839643b9d | -7.74531 | -42.58333 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cc137f77-1abd-3941-aa0d-4b6e7e414d0f | -8.45327 | -47.66039 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5da4cbc-64ad-3906-a947-cab049684bb0 | -7.76056 | -42.53525 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7b35c980-f083-3135-9073-f265cc3bccad | -11.91948 | -46.27908 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 6e8f7b20-7f96-38f5-8256-b4fe0bd31721 | -11.26663 | -47.79523 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa31af4a-7717-3135-90fb-2fff4dd582d8 | -10.27687 | -48.07143 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7339794-744e-30c3-a77e-b8adbb79f2ef | -4.66488 | -45.79127 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cdcbdcc9-a121-3212-b584-891da43ef820 | -10.88173 | -46.71833 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49983525-3da4-3cf4-a5b2-2559003202d1 | -7.43099 | -47.00811 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48a1ab3e-26c6-3edf-b15e-1ac5bbe6916e | -9.94079 | -43.74593 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9e306568-fa00-3de7-a074-88cf4e40843d | -10.8783 | -46.71778 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9283ba00-25d6-361c-90e2-b956411daa0b | -10.89835 | -46.70152 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8529eeff-394a-34ec-b2f8-0a64d10d244b | -7.78663 | -50.08463 | 2025-10-03 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0df97afe-b2df-3f8f-931d-2477d2b5063d | -11.63053 | -45.05813 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27787f9d-b5fc-3dc7-b806-4f959f27473f | -12.11738 | -43.44006 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e456bc6-fdbd-32ca-b20a-f9ffdd6f2b07 | -8.55277 | -44.80395 | 2025-10-03 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d83f205e-9259-390e-b243-260d39bc2205 | -9.91054 | -43.73111 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| cee0579f-a52c-37ba-a9a5-a8c19e5433d8 | -7.71107 | -46.21023 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 255ff096-5884-388c-8ff4-29248028c27d | -11.91531 | -46.28289 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 1d1dffec-2d1e-3603-a9b9-28b3ea42a65c | -9.06691 | -46.65973 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a1ad2a4-4c59-310c-b1fc-015c71af0a37 | -9.63105 | -54.31218 | 2025-10-03 04:32:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71ba4920-d203-39a6-acc1-ee8598438b06 | -11.61207 | -45.0262 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55364404-def2-3a4b-9a49-fb65e87ce5fd | -11.34968 | -44.94248 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0401e4af-1189-3124-8c84-61c86029192f | -9.91451 | -43.73171 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a6699d8f-7863-3273-9460-eef99c09bc00 | -4.66452 | -45.80242 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cac0a84a-f1a0-31b3-b6df-8039d282ef5b | -10.85553 | -47.2166 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7eef8e1-8ce6-3f04-ad9b-dcfcece796b6 | -8.51621 | -47.25647 | 2025-10-03 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bd39d77-1bd6-38d9-8086-111bd7b03b3e | -10.75868 | -45.33778 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08aadc18-ba2e-3a02-ac3d-bc79c5186468 | -10.85675 | -45.40781 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6e75d20-bcd6-3d47-981e-c9fde7eb8c8f | -7.29153 | -44.1882 | 2025-10-03 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8772313-eae0-3f36-ab91-2f211b134f4b | -8.07915 | -49.9013 | 2025-10-03 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8969864c-455b-37c7-8375-c475457b798f | -7.79969 | -49.87228 | 2025-10-03 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e586bab5-9a77-37a7-af3d-9b23e7ec4b74 | -11.42965 | -43.49343 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e71d840-c934-3a42-9401-990c705e5370 | -4.87743 | -45.62157 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c019e47-8373-328e-8b84-cc929a849611 | -11.17084 | -47.18588 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4bd5849-ac33-31ff-949f-8157f4752cd0 | -4.66036 | -45.798 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8897f85c-761c-306b-91a5-f262ce622ebe | -7.74615 | -42.59124 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e93cd3b-8012-3f23-a4df-9937f2546a0d | -11.21964 | -50.82347 | 2025-10-03 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6176366-5ecd-39e2-986a-e9fa9576f12a | -6.35948 | -44.75915 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24700639-4dd2-302b-a229-30fe55a0b9a4 | -10.30139 | -48.28286 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b0b4654-5193-3df0-a7be-46879d7ce0de | -11.07929 | -48.36804 | 2025-10-03 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db04ceab-b83b-336f-ade7-a220913aa3c6 | -11.80555 | -45.02018 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44fa2d4e-5625-30e4-a5c5-4f50b6e2e6ec | -10.88059 | -46.72591 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd61c72b-413c-3139-84b3-e524a313b4dc | -10.89265 | -53.74268 | 2025-10-03 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 804f4208-57e6-33df-a649-815fbc10dea4 | -5.63171 | -43.90555 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6b492c36-9014-37e4-bb01-a81aff54f8e2 | -11.49857 | -43.50206 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 927b837c-43d9-3601-a091-e125e6b07841 | -6.0744 | -44.61377 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ce7c620-30a1-3c71-ae3a-201d0d98ada3 | -11.80929 | -45.02086 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f2611a6-0073-37cd-8e6e-c0cd0eaab9cf | -9.95888 | -48.77597 | 2025-10-03 04:32:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4ae357ac-67b0-3bbb-a58a-e8966cc3c8de | -11.20945 | -41.59524 | 2025-10-03 04:32:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c5042ea5-63bb-3833-a3d6-9211cf8814b3 | -9.0519 | -47.0149 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b6f7adc-0f71-3c7d-aa7d-3171c6f9ffe1 | -7.76367 | -46.25594 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1be09df6-430e-3573-b8df-56c0addb9bb1 | -5.64856 | -41.24588 | 2025-10-03 04:32:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b008027f-d536-3c17-9150-2d33362891de | -11.22801 | -50.79384 | 2025-10-03 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b32a35e7-14d9-3ea9-aa1b-652d963a452e | -11.16464 | -47.18106 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28cffb38-4575-36fc-ae67-c7197ef5f2e2 | -12.53869 | -43.19226 | 2025-10-03 04:32:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87f622ff-694c-3962-9c19-ebaab4c83f4a | -7.80088 | -49.86487 | 2025-10-03 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 484eae10-8f7e-35b6-957f-86d04a05078c | -11.59576 | -47.66201 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df1fc65c-f9a8-3160-9272-323177957f7b | -10.21017 | -48.19379 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1700f8f5-60e1-3f92-bb78-4e090447080b | -10.10353 | -50.35324 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 71317695-002b-3fbf-b9df-3c5053b6380a | -6.04805 | -44.61808 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b000b744-2158-3250-b057-8741080da051 | -8.07575 | -49.90074 | 2025-10-03 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9da31c8c-ff7c-3819-aa69-1b9bd2f1cac4 | -9.95205 | -43.66858 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff91fd50-002a-3e83-94af-72307b4e6c2f | -11.46355 | -45.1391 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdb2687d-c54a-3ca1-91d9-f5f16ecb8c46 | -7.2467 | -49.41263 | 2025-10-03 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a7c248a-f2fa-3c23-9368-9798b8c08a59 | -8.11258 | -49.7596 | 2025-10-03 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19285e74-73bc-31c5-a236-abaa51627979 | -6.72188 | -45.97124 | 2025-10-03 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7730525e-e14b-3f85-bd14-b3b8bbbfa137 | -11.50218 | -43.50644 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea9990b2-3c30-378e-a77f-7206b71af150 | -6.64865 | -42.79348 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9eb7791c-a337-3f9f-802e-d2de6db3a56e | -10.27979 | -50.37066 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 466ae79f-8fb0-35f2-91d9-4b138f974e42 | -10.30084 | -48.28636 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efb81569-9bb3-3902-aaf8-3aa872a70a8c | -4.67351 | -45.78897 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 192defd4-ffb9-3565-b52c-5be1338185a4 | -9.94325 | -43.75684 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d43f4d03-0ef2-3f17-8313-8fe414ba0257 | -6.67378 | -42.79039 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 87fe1eb7-2bde-3717-abba-c024c2960e64 | -10.21254 | -53.87548 | 2025-10-03 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95e43ea7-d383-30cc-9d5f-e4011de6a50a | -6.23703 | -44.22837 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f97f5b2-d2d3-304b-8afe-db1985054e60 | -6.35933 | -46.43578 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cdf814e-b256-3ac0-91cf-f9a1e5f75f22 | -12.41826 | -44.08392 | 2025-10-03 04:32:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b84a3686-79af-3ed3-b6a2-7101cf02c699 | -9.75172 | -48.3457 | 2025-10-03 04:32:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6517108-c9ad-3672-8942-0366443cd6e6 | -6.94944 | -45.35238 | 2025-10-03 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9703cd3-5670-3fc9-8128-6d3dcf695fe1 | -7.3141 | -42.87234 | 2025-10-03 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e3f41e0f-033b-3009-bace-d5fb0a19c2eb | -8.10937 | -48.01279 | 2025-10-03 04:32:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e3f165f-58c3-39ae-a8e3-69657cb12b48 | -7.19738 | -45.3842 | 2025-10-03 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 901afc42-a5fd-3a68-b39e-ae6841c53ec1 | -11.14451 | -43.40013 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 423dd644-5706-31f5-9dba-734a1ef01944 | -11.87792 | -45.02744 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d9e86df-c822-3029-8ec9-bea616caefa4 | -11.99268 | -47.19214 | 2025-10-03 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c58c6794-e0d6-30a7-8464-bfcc0ee9597c | -7.89076 | -47.34983 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f95ae46-b3eb-38ed-8c3e-93a632483275 | -10.95275 | -46.70934 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e7826e9-2455-3b87-9227-be3a92862326 | -8.88841 | -46.59482 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61505684-2c75-32fb-a5fa-8631e3cb2a55 | -11.9165 | -46.2748 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README96.md)
