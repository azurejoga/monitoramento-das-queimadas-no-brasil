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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3862ba0-bf16-381e-aeb1-cf26723bf1d2 | -10.79443 | -50.68009 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dccbe2f-b291-3af4-8a44-f679aa4ad36e | -6.92292 | -44.79786 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 05eee1b9-0078-3fab-a24a-1248d3406e95 | -7.06934 | -44.15541 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0af01334-879f-3eb8-8a98-87da1ac53bba | -5.55946 | -44.9632 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0f550879-e5ea-36aa-81f6-db1c93a8d4d1 | -5.61183 | -42.89978 | 2025-09-16 04:02:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 74e30611-51fa-36ae-82b8-83bff0613f91 | -9.06896 | -50.30865 | 2025-09-16 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c078b927-afa4-343e-8b61-67c474daea25 | -8.79255 | -46.03178 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce9ea1fc-5782-3412-9740-71cfe5e76892 | -11.12279 | -45.30947 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a45e7d26-37bf-3876-bebb-ac49a338505a | -6.46385 | -43.68094 | 2025-09-16 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b272c21-75ea-3df7-beae-dba222e2d415 | -6.18668 | -43.47117 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09c6127d-8dfc-37b0-8acd-38a0abbc2c7d | -6.15834 | -43.66738 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19baea25-911a-31ff-bc25-ec340d488352 | -11.0208 | -45.06442 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4bba6af5-3b0a-38d4-9e1a-ab28719dce93 | -6.17547 | -41.2226 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f3757fac-9a85-33c4-b739-db30da8561c2 | -9.32057 | -40.80987 | 2025-09-16 04:02:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 67a32d94-e5c7-3e7d-bc66-eacbfe7867af | -5.79277 | -45.92489 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42f6aa9c-4452-3bf5-b02e-89e5ac702adc | -7.43604 | -46.17697 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8d7b366c-2493-39f2-b821-96482dcdf7f0 | -5.87183 | -45.8663 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49c24550-acb3-3f91-8754-8cdb7cac43c0 | -11.47817 | -43.58252 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d4aedfc-d693-3f12-80e9-2162d3f7381b | -11.44594 | -46.94365 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8eea6d0b-f944-3ac9-b2d8-0b948b1751ff | -7.43023 | -44.87107 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 664b668e-5ed0-3cba-851d-68b8c9a0801f | -10.7951 | -50.67655 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85e6db1a-f3ed-3c13-9f81-7352caf8498f | -7.53731 | -43.98101 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 450d79aa-11ea-3298-ace1-4e2b06125de6 | -8.3339 | -44.73788 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf7b49b6-8985-3f86-bb8c-a1e6eef9a9c4 | -10.71967 | -46.48441 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 35db1772-de6f-37fb-97aa-e1cdf995f241 | -7.67622 | -46.29907 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9202ec68-93b5-3edc-89c7-3834d2d24351 | -8.33627 | -44.74088 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31754a62-29b2-3776-90e3-0f01cf087e75 | -9.87185 | -46.45314 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce41a8d2-853f-3482-8a45-ac549f76fef8 | -8.97827 | -46.24102 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8806fbbc-2d94-3a06-b77b-0db21c9ff24a | -5.95921 | -42.72897 | 2025-09-16 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4967efaf-2bd3-3d3b-81be-d16f5049a058 | -8.61202 | -46.39558 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cca17701-3780-396b-a748-9bdd20e2805b | -6.29764 | -42.40371 | 2025-09-16 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b96efca-cc59-39f7-a204-4bef77200a0d | -6.5247 | -41.82112 | 2025-09-16 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 07dafe1d-0ace-3248-88a8-5c01bd6e2445 | -11.23614 | -49.40308 | 2025-09-16 04:02:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de007cfd-6615-347e-b61a-f3fd6c0c29e8 | -5.63209 | -45.33101 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d827f7f-c7f6-3884-86d8-bd75bcb73e0d | -8.41584 | -45.74015 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f32c2f7-1d04-3af7-bab4-2c4d2e8c2193 | -7.40154 | -50.00203 | 2025-09-16 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1a661c79-d7ac-311a-b26e-a77644c0e6d4 | -9.05388 | -44.84758 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5dc9fadc-4882-3b46-97ad-3db43adb1d77 | -10.71432 | -44.76565 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7af605c-6430-3c32-ad8a-3fc0f7ee0379 | -6.18486 | -41.20264 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8397ef42-cd6f-3235-98b7-4692d3c879be | -5.05667 | -45.20232 | 2025-09-16 04:02:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4f133d4-6f0f-3982-be93-af78fb280c3e | -9.18724 | -47.04227 | 2025-09-16 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2759793-8add-3884-8cc9-3193ec176bba | -11.70401 | -46.88652 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94a14417-4032-3d8a-bb32-aa65cdc1c52c | -10.72585 | -44.75058 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dec4045e-ef15-3c0f-822c-4d7bf6c112c0 | -10.43538 | -45.14077 | 2025-09-16 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fce9278-6fca-3cb0-84c3-dff5fda5c918 | -11.7055 | -46.87811 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 641b02a0-b998-300d-945b-973c27ae74de | -7.04223 | -44.13287 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be885c21-b613-3058-9aa8-846429205b2b | -5.76515 | -43.93301 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e64712a6-067a-368c-96e5-ad491a5a3dfb | -5.86588 | -43.71655 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31ed6bbe-01ed-3d34-8dcf-502c89055fca | -11.11577 | -45.32774 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c81c6c8-b554-33f6-ac0e-7dcae5a8c5dd | -5.78931 | -43.95108 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f36a6e25-e366-333d-b7e9-c4cf63ba33f9 | -6.34538 | -43.16672 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 91813e99-24fe-3d2c-a71a-d910cf788064 | -7.26607 | -46.60659 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 06f63593-e24f-3d38-87f2-0f91534f3d07 | -10.80241 | -45.9795 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 7f3b4b2b-90c9-34c6-bafc-21c80b836c44 | -6.67865 | -46.30984 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 79dc5cd3-89f5-3ae7-a561-890886014001 | -6.17925 | -41.2163 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 28319ee4-088e-3268-9ce7-8e6b49247d4b | -10.8265 | -44.09359 | 2025-09-16 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dfafdeb-c465-3b85-b5db-20f33624f1bb | -8.12816 | -50.16475 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2ee293a-6a42-34b6-88c8-64ccd2c77181 | -6.54996 | -44.00439 | 2025-09-16 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ca8daac-2d63-3206-9a1f-7e7ec2f321d0 | -8.09546 | -50.15765 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b17bd93-5268-3bae-b768-7027b624a738 | -6.17982 | -41.21275 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 21fcb117-65c2-30aa-8126-de2f3ca5c2e8 | -11.32991 | -43.48296 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d74b940-8201-380e-b513-f962968e2e72 | -9.06729 | -47.02893 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7aca9ae9-d5d7-3b8c-926d-e8638f8c97ea | -8.95324 | -45.8773 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 969bf2e5-2626-3dc8-a136-c5384eab8732 | -7.52585 | -47.65833 | 2025-09-16 04:02:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0c72f3f-81bb-387a-abbd-f821d8cf656e | -9.07163 | -47.02991 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c7fb527d-e2cc-3ff6-81bf-1cdeb74aca44 | -7.83782 | -46.11673 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 521ca8d0-4f44-32cf-be7b-449a81e65c5f | -10.71153 | -46.50701 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 1e6be4ad-452d-3ef9-876e-ec7218adcf06 | -11.45205 | -43.55431 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cb2f351-dd68-335c-b9c4-1e193b055e59 | -12.1178 | -44.82578 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7c92378-0ec2-3714-a012-ab4552ba5a81 | -8.70636 | -49.41783 | 2025-09-16 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5ae74a7-8157-3cae-a8c1-479fa482e8da | -6.12794 | -43.37064 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7f10f55-4fa5-37e5-8f04-83add9ba016d | -11.11036 | -45.33656 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf7e7d04-3205-39d6-9f68-65c8a1cb762e | -6.29537 | -42.39563 | 2025-09-16 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b830f793-d8a1-324e-a784-2294f79818ea | -11.70288 | -46.86881 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 633a02f5-ad6f-34d6-8e5f-0d06d60bd2a9 | -9.22886 | -45.6578 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 704794de-f316-302f-a3ce-23d31424f88e | -11.20636 | -41.60448 | 2025-09-16 04:02:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 976a776b-fea3-3bfb-a4ea-ebb55c30cf0a | -7.43723 | -45.83817 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de4ebc2f-2f29-38d3-a64e-54caca2a6e56 | -9.10015 | -44.84858 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 90947aa8-42b2-373a-8d9d-482e56920580 | -6.44934 | -43.31003 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7048b6a-82e6-319f-ab12-f761427f8bce | -7.13839 | -47.98092 | 2025-09-16 04:02:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2455bc32-b491-346a-97de-4814bc779caa | -3.95282 | -49.43413 | 2025-09-16 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a84c3965-15cc-3bef-bb28-079d361a394f | -11.11334 | -45.34198 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29f1ad47-69d6-3110-8fda-b11054063e7a | -5.79384 | -43.94707 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af38bc7e-43de-3413-8366-4a285332db34 | -8.65465 | -46.34988 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1fc7abf-62ab-3f0d-bf18-842d8c442947 | -8.97375 | -44.19399 | 2025-09-16 04:02:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a52bb59-eadd-3bf4-b50f-8c96692c30c2 | -10.74109 | -44.76494 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 027297b7-4faf-362d-8f6a-f961b4d1fc1c | -5.79932 | -45.93847 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a56b6442-4684-33cd-8e5a-731fd118080b | -5.67589 | -43.49805 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf73216d-4189-39a8-9e59-41d51515fda5 | -10.71918 | -44.745 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bb75a8e4-814e-3c9b-bd6d-8ecb3b992970 | -7.44729 | -46.16242 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aec18aed-3153-3d1c-b3cd-8a43544b784f | -7.27115 | -46.60326 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f4477ce-5f96-3bd5-b534-5f036efdcc65 | -6.62859 | -45.57684 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae7409eb-86ff-3795-b611-8b2d544787f5 | -7.8842 | -41.86266 | 2025-09-16 04:02:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d5578dce-3e88-338e-a8fc-056c54de7381 | -5.42183 | -43.18708 | 2025-09-16 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 416490c0-62e9-3ce1-abb6-72b631722c9e | -11.35386 | -47.34298 | 2025-09-16 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a2e89c7-f62e-3a65-91f8-33eba65de78e | -5.55889 | -44.96671 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3065bc9c-365a-3e73-b0fa-20de346c67e7 | -11.44293 | -43.54478 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 119f87e3-1aa3-34cf-b4ec-49cb46bd805d | -8.00529 | -45.6694 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ecc6e2c-4fa6-3a71-82d7-3770fa208266 | -9.06005 | -47.01888 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3563cd07-1668-3e63-9ebe-24182d043cf3 | -11.11416 | -45.33719 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README15.md)
