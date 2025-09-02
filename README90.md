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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11c68d7d-0306-3fbe-9a9d-fa701385338b | -6.07057 | -45.63694 | 2025-09-02 12:34:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 41d03566-508d-3bdb-bfc2-dc8d660a027d | -6.81536 | -44.27515 | 2025-09-02 12:34:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 7469bb3e-e911-3d6d-8f4d-16067c9ab60c | -5.95227 | -44.28814 | 2025-09-02 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 5922bab3-d028-3690-989f-4cfc7ab807ac | -5.81739 | -41.94341 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| a3469a9d-9601-36de-8bd3-5159dcf2581c | -10.05032 | -48.12144 | 2025-09-02 12:34:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3825dfd2-c642-364c-81ad-0ae9313c29d3 | -8.13953 | -49.82461 | 2025-09-02 12:34:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b1892720-02f1-3b83-bd03-2ff7f870f0e2 | -8.0183 | -44.06808 | 2025-09-02 12:34:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| ad21a20b-a061-3fb9-8860-4113866ec8cc | -6.07269 | -45.6214 | 2025-09-02 12:34:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| c58b6532-e926-39a3-9f98-b1ea9079b6d0 | -6.20235 | -43.34174 | 2025-09-02 12:34:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c1f744ee-6912-3392-a5da-1d1bb051592a | -6.88697 | -45.87727 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 72bc91ec-f324-3b57-8297-ae2dfc0bde6a | -7.09496 | -45.34066 | 2025-09-02 12:34:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b419c0c3-76ff-3cc3-bd51-46e4e28eb96f | -5.78527 | -45.08548 | 2025-09-02 12:34:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 09358d05-c778-34b4-98f6-491f50592cdd | -8.19671 | -44.81237 | 2025-09-02 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 175127c7-a269-3aaa-ab8f-874c10dd2cd9 | -8.13822 | -49.83387 | 2025-09-02 12:34:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8ff5bc9a-4c5b-3556-a58b-5c89555391fc | -6.88481 | -45.8834 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 3ef13098-17b8-3e3c-aaf5-adeb22254564 | -6.27052 | -43.5252 | 2025-09-02 12:34:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 56aeefc0-b1dc-31a6-87c4-955918204946 | -7.92399 | -46.44096 | 2025-09-02 12:34:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 423b0475-808f-3f08-9230-b88347bcafd0 | -6.8776 | -45.8606 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 81e55817-c509-3a48-8e38-d65312435170 | -6.34548 | -42.55363 | 2025-09-02 12:34:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 48fe4f71-d52b-3b7c-b87d-f2a81ff6aa4c | -6.18767 | -44.18983 | 2025-09-02 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 053c3d03-bfa7-3edf-b111-6e75b59418fc | -6.98571 | -43.10721 | 2025-09-02 12:34:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 9206a424-d4d2-3cf4-886b-1335f02e1b98 | -7.92208 | -46.45565 | 2025-09-02 12:34:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 259.6 |
| 3f044cd7-e7ad-385d-a051-8017a6cbc9d3 | -7.49712 | -45.34772 | 2025-09-02 12:34:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| d289be7a-8767-3eb7-b68f-bfdfd9d13eee | -4.7803 | -45.33314 | 2025-09-02 12:34:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4d545326-6bde-3dc9-80fc-ec317e37b953 | -7.95895 | -46.51787 | 2025-09-02 12:34:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 4864c052-6c2a-3bf8-ac11-378769ab3dda | -9.50229 | -46.46125 | 2025-09-02 12:34:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| ef00ce2d-669d-3d8e-b462-b03f7b0d898c | -8.34999 | -52.52623 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8e8869fb-8659-3320-8c7c-6b784724888a | -6.29975 | -43.6231 | 2025-09-02 12:34:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 84b0d3fe-94c5-3bd7-a26d-921631d6d358 | -8.73948 | -46.68911 | 2025-09-02 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f5fa7b97-d456-3353-af1c-203f6a31c735 | -9.59539 | -47.1584 | 2025-09-02 12:34:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 78ae3a4b-21fc-3fa7-b165-b0a38636e018 | -6.34909 | -45.61321 | 2025-09-02 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 5ff01080-a59e-3536-aaa0-2510387b4892 | -7.91048 | -46.44743 | 2025-09-02 12:34:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 644da6e5-e508-31aa-9cf5-dd077ed80877 | -7.76389 | -49.48376 | 2025-09-02 12:34:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 7c831564-b4c4-3c36-bcfd-bf3e2300862a | -8.86257 | -50.57713 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9ba06f5a-623a-3a4c-97f4-a4fb3a261ddb | -5.81347 | -41.97358 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 48.9 |
| dc150d76-ccaa-32f0-a6f5-0ba3a4b7b2fb | -3.22786 | -47.12748 | 2025-09-02 12:34:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f0a0cc1e-c984-37bf-a2a3-7729b6d47301 | -9.60855 | -47.83487 | 2025-09-02 12:34:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 092524df-aecc-31ea-9aac-6a680dff67c2 | -6.88906 | -45.86201 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 259.4 |
| 550c04d9-33d9-32d1-84dc-1cb11b399163 | -5.39501 | -43.39073 | 2025-09-02 12:34:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| bcf53a37-98aa-303e-a3ea-4f94ed793b3b | -3.22939 | -47.11642 | 2025-09-02 12:34:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 06946ca6-9908-3fa8-8bc9-f475d0354376 | -6.18589 | -44.1961 | 2025-09-02 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ad9d5a9e-635b-39fd-816a-d19553035ceb | -5.88003 | -43.00335 | 2025-09-02 12:34:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 47.1 |
| 7e201cb8-6b68-3035-bd32-10496518b004 | -10.05881 | -48.13482 | 2025-09-02 12:34:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| e447c8ac-e13e-3b22-8905-a5e085f4f145 | -6.98711 | -43.24113 | 2025-09-02 12:34:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 052f855a-05e2-35dc-8ec9-915490f1937e | -6.35725 | -45.62084 | 2025-09-02 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 504667dc-a74e-30ca-9749-fadd6519f328 | -3.23065 | -44.18867 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 16f80c17-56b4-37c0-8446-c8dcebf6ece8 | -8.01541 | -44.09047 | 2025-09-02 12:34:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| b542c731-b814-3340-878b-ca6eb46ef252 | -10.00769 | -46.89393 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 605e7504-cdb4-37bd-a56b-de344461cf99 | -8.46677 | -47.36427 | 2025-09-02 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| a4999c84-3dad-3d81-bf4b-e7a0d8c82f24 | -8.86739 | -45.79378 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| c710cb82-1471-3f8b-adaf-2c3716f2602d | -8.85554 | -45.79189 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| edd3a37f-6707-341c-a1f6-9bd200e11cbb | -9.12137 | -46.04591 | 2025-09-02 12:34:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c750690e-480a-3817-982b-41759d37233b | -9.69272 | -51.03078 | 2025-09-02 12:34:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bd2391b3-8ded-374c-bcf3-99c5ab517c1c | -7.77271 | -49.48133 | 2025-09-02 12:34:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ff056522-493a-319a-9e3c-6b51499de346 | -8.74136 | -46.6748 | 2025-09-02 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 91dff0e7-e387-37b0-ae2c-386dde309cb9 | -7.78934 | -45.44528 | 2025-09-02 12:34:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 8443277b-8d03-3259-8e6f-84a9753ae0c9 | -9.73922 | -48.98298 | 2025-09-02 12:34:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 11a66096-88af-3dc9-ab5c-5c3d8c6de745 | -6.07013 | -44.68431 | 2025-09-02 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| f144de16-bde5-3541-bcea-e3b989d76c82 | -9.24304 | -47.04656 | 2025-09-02 12:34:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1b0f8b0e-2e99-38a9-8e26-6bf7f499b608 | -8.84149 | -49.55027 | 2025-09-02 12:34:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 57ff53aa-10e3-347a-8d81-2a295a5f91ff | -9.48314 | -46.52061 | 2025-09-02 12:34:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| faf87ab9-6a86-3d81-8e19-a7d8c3f43bce | -5.88315 | -42.97845 | 2025-09-02 12:34:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| ad968199-23ae-3eb9-8128-9fd52f1266b6 | -5.79809 | -41.97144 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 7223cc85-601b-3141-92a5-411a6ac4aab7 | -6.39963 | -51.60746 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7be90735-426e-341f-bc2d-f923eb071a0a | -6.79582 | -52.8077 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 73081ad5-6b1f-3447-9db3-18fb5a198f71 | -7.10743 | -44.75731 | 2025-09-02 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 3296f40f-f5b8-35cb-9de5-707f4d3f899e | -8.85367 | -50.57589 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| c76c8397-84a4-3fbb-9ea0-42e5e5cd7e6c | -6.33971 | -45.59546 | 2025-09-02 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 33cbc253-47e8-3dc9-9f8d-8301c23a376d | -8.44755 | -47.34892 | 2025-09-02 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a3942dce-618a-3dd9-9fdc-a0bfdd0370ae | -10.06529 | -48.08704 | 2025-09-02 12:34:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 8ee9a594-61af-321c-b2f7-00aa91ca9332 | -9.01798 | -47.97573 | 2025-09-02 12:34:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9c23d012-3b31-3393-9beb-64beafee019a | -9.01293 | -45.9917 | 2025-09-02 12:34:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| be102348-df57-3cf8-841a-925329247f8c | -6.88679 | -45.86806 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 404.2 |
| 7799e165-4f54-30bb-8049-d327ce622b55 | -8.01282 | -44.07413 | 2025-09-02 12:34:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 1196702f-b180-3d3d-a59c-230afdf1f77b | -8.12851 | -49.24502 | 2025-09-02 12:34:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 18077046-bed0-3773-90a5-c68225505442 | -8.19671 | -44.8071 | 2025-09-02 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 60ff8573-b246-34f3-8b70-c9761743fcba | -8.8654 | -52.02823 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e47ed38e-80f6-3a98-a6f4-4473debedfcd | -4.91039 | -43.18085 | 2025-09-02 12:34:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 888edf6f-cd1d-365b-979c-a8658f4fe425 | -7.10612 | -44.75154 | 2025-09-02 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 5747b0e4-4c0a-3b6c-8991-cc0037105e7e | -10.06371 | -48.09871 | 2025-09-02 12:34:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0571f9fb-feff-347f-901c-238a8e6cf31e | -6.3442 | -53.43478 | 2025-09-02 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 46c0bb5a-538f-34bd-acec-29395d5f35dd | -6.34688 | -45.6295 | 2025-09-02 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 82881d1e-94a8-32b2-a113-eebee75da5c2 | -6.59261 | -45.40152 | 2025-09-02 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 85c39b94-70cd-30c1-9ec0-2f8b078bb1b8 | -5.07914 | -43.0714 | 2025-09-02 12:34:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| b361ec9e-86f1-3bc4-81eb-ea20eeae7301 | -6.27768 | -43.51946 | 2025-09-02 12:34:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 1b47e08b-92bf-3ec8-b024-1d5bac5d6ffd | -7.47668 | -44.82972 | 2025-09-02 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| c076c1bf-ede3-3905-9204-7255a99ebcd4 | -7.91101 | -46.45395 | 2025-09-02 12:34:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8777188f-8fce-381f-998a-d91e6033741e | -9.48509 | -46.50536 | 2025-09-02 12:34:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| fe4f6ff1-743c-32eb-b67e-8f5b135b3781 | -6.96135 | -44.3634 | 2025-09-02 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 4c91e764-5ab2-30ad-b1ad-af622c51abc5 | -7.47904 | -44.81094 | 2025-09-02 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 1e123ba3-c49f-3b15-96bd-22bc7483284c | -7.66793 | -46.71667 | 2025-09-02 12:34:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4fc3d56d-b4f6-3a35-b5b7-44270901152b | -9.694 | -51.02182 | 2025-09-02 12:34:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d610d8dd-e773-3979-83e6-305c1fbf796c | -7.71309 | -45.0066 | 2025-09-02 12:34:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f8e66f27-8312-34e6-962f-e64294174961 | -9.72967 | -48.98169 | 2025-09-02 12:34:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ac4f92e3-2cd6-3c4b-aa1b-8a1250438563 | -9.65314 | -47.79662 | 2025-09-02 12:34:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a11f3d3f-e002-3a73-b6b1-70796013893d | -8.76178 | -49.39461 | 2025-09-02 12:34:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 709849ee-3c95-3022-9108-4f453ad6a65f | -7.71514 | -45.01336 | 2025-09-02 12:34:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| ae4399e8-d4c2-3e87-a678-a6bf43ba8488 | -9.64433 | -47.80215 | 2025-09-02 12:34:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d809af2a-2096-30b4-a014-7e6f23760bda | -4.60546 | -43.30857 | 2025-09-02 12:34:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 53ea052d-7ec0-3cc7-b05b-605daec08cd4 | -9.28555 | -47.08617 | 2025-09-02 12:34:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |


[Clique aqui para ver as próximas entradas](README91.md)
