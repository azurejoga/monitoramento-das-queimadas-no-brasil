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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58718f26-7b68-3248-92bc-7dcb8f2f43a4 | -6.92687 | -43.53775 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f2569bd2-f7fe-32ee-88b0-4c319157c5c1 | -7.70372 | -35.26172 | 2024-12-13 03:55:00 | NOAA-21 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f4da5cf6-d31e-32c2-b9ce-08c50855d373 | -3.30968 | -42.74228 | 2024-12-13 03:55:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0facccc8-1a49-3884-8b51-18e833c7147c | -6.05955 | -44.04932 | 2024-12-13 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7c4c67e-13a4-393e-b4f3-ec6a674e359e | -5.20604 | -43.30342 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdb043bb-0609-347d-93e5-221df3d78719 | -4.87793 | -44.40687 | 2024-12-13 03:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79fbda66-5875-3b3b-838b-9306cc5c4ec7 | -2.91224 | -48.01379 | 2024-12-13 03:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8148c85d-8740-345b-b4ff-e1a0a2f2cf85 | -5.20957 | -37.88117 | 2024-12-13 03:55:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2f3caf24-65aa-3b64-939a-777d46271b21 | -7.87219 | -38.384 | 2024-12-13 03:55:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c569488-e847-321a-be2c-d66fefdbbe99 | -5.21986 | -43.29471 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3f6442b0-61e8-3160-b06f-4b4aef928fa4 | -6.93566 | -43.534 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a67e4191-2c2f-3b56-8610-1d86e5b8d4d7 | -10.20845 | -36.23569 | 2024-12-13 03:55:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| de51d48f-3210-3030-915f-1b6bd26d1405 | -1.46208 | -46.8132 | 2024-12-13 03:55:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03976904-82cb-3444-a438-c8301d43c9df | -5.82232 | -35.52919 | 2024-12-13 03:55:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9a78040a-8c39-3ee3-baa0-aff8d3da329e | -6.49807 | -37.81578 | 2024-12-13 03:55:00 | NOAA-21 | JERICÓ | PARAÍBA | Brasil | 2507408 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f964ae6f-6ea1-38d5-bb4d-56d65afc2d58 | -4.53934 | -43.29196 | 2024-12-13 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be5f7858-b107-3f79-bf3f-9104fded74b2 | -6.56489 | -39.43537 | 2024-12-13 03:55:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 52653360-896d-322f-9591-1c3bd4dd94a1 | -4.88152 | -44.40323 | 2024-12-13 03:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f37c8c1f-fda2-3250-aeec-8b624d8da250 | -6.11781 | -43.95541 | 2024-12-13 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 92879cc2-71f3-351b-baaa-fadec32806ed | -6.59277 | -44.15943 | 2024-12-13 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2183d35-fcb4-3c5f-b2db-20eafa7b7d3a | -6.93481 | -43.53911 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a9e8531-fe3a-33ce-a778-f37182c223be | -5.98403 | -42.31147 | 2024-12-13 03:55:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c718bf0b-9ed8-35b7-9a60-ed877e1f9b2f | -6.10168 | -44.76067 | 2024-12-13 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7058ae38-014c-39b5-b8f3-c990b6188202 | -1.61824 | -46.6657 | 2024-12-13 03:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4fef1d03-06f7-3196-9335-77e5cff3929a | -4.22066 | -40.56221 | 2024-12-13 03:55:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5e2a856d-89fc-33a1-9a4e-64ae71067ac5 | -3.30418 | -43.53626 | 2024-12-13 03:55:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b723b5bd-0f9b-33f8-8fc0-c6174267cef9 | -4.40981 | -48.30293 | 2024-12-13 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3132b305-6e2d-32d9-8ab9-f5e3f6a3cb66 | -3.29128 | -45.59662 | 2024-12-13 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 23dd422b-7442-3941-873e-f9576cd02ca0 | -6.30721 | -43.46497 | 2024-12-13 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 328cde71-9c4c-3313-aaa0-79e8d41ce6cf | -7.11146 | -38.90245 | 2024-12-13 03:55:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a302a082-e133-3aa7-ac5f-07cd6a299ddc | -7.58034 | -47.11322 | 2024-12-13 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c58cb605-ac46-359a-b32a-6e91ab998929 | -4.37752 | -47.62702 | 2024-12-13 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11cb7e14-27f3-3dad-8f24-58581c124eed | -5.20663 | -43.2999 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 75565de3-60b7-34fd-a7e4-23496e3e0183 | -6.92161 | -43.54481 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 566e8dd9-7df3-3b16-85d5-936ec082ab47 | -6.91764 | -43.54416 | 2024-12-13 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa1d1852-d41a-30dd-936a-d5b8fbbedc06 | -4.16742 | -42.44572 | 2024-12-13 03:55:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 6e7f8fe2-7af2-3f56-a928-d5ebad825429 | -4.27032 | -40.40834 | 2024-12-13 03:55:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 72723ffe-ac41-3129-8dcf-dffdb1653b8b | -6.12879 | -42.53849 | 2024-12-13 03:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 11b403bb-6389-3eeb-82b4-56dfd8359406 | -4.99419 | -37.09712 | 2024-12-13 03:55:00 | NOAA-21 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e633ae11-cb6b-3de2-93ed-a9a5ad5eb455 | -5.45196 | -44.80997 | 2024-12-13 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6a2a645c-3a02-37e9-9feb-eaa7a2d2b989 | -6.92443 | -43.55238 | 2024-12-13 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f183135-c9ab-34db-b9c3-5c5e1efdf533 | -4.91261 | -39.81462 | 2024-12-13 03:55:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9feb5783-c58b-37b3-801f-3ee44b31a3b7 | -1.90008 | -46.81654 | 2024-12-13 03:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8431ef86-c348-30a1-b54a-99ff7c74137b | -6.74009 | -38.20635 | 2024-12-13 03:55:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f3a19f09-8713-32cf-90eb-a1243f1e8057 | -6.08656 | -43.53537 | 2024-12-13 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfb87245-1563-3b73-a4dc-9c036ac12ab9 | -8.65494 | -36.90969 | 2024-12-13 03:55:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aed9df12-0f7a-3f61-9d64-c9f9bfa98ae3 | -5.08472 | -42.56445 | 2024-12-13 03:55:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| be1d4e1e-d662-3892-ae1d-d60b18b945e6 | -6.91582 | -43.53063 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 72ac7be6-742a-32e6-825d-882e9177b4eb | -6.92104 | -43.54826 | 2024-12-13 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71e19159-251d-36ec-9fd8-077f8de36b06 | -5.24241 | -37.69131 | 2024-12-13 03:55:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d5725958-33ca-387e-844d-63ed7ba19ff5 | -4.83506 | -40.32386 | 2024-12-13 03:55:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b1334bfe-3869-30f3-8975-d2dd7adbebab | -1.97405 | -45.39589 | 2024-12-13 03:55:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9835f408-6aa9-3ca3-87be-e6cb59b3ea05 | -7.27449 | -46.16592 | 2024-12-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61b07501-3209-39ff-9c5e-f4c787f60a61 | -6.63187 | -38.29244 | 2024-12-13 03:55:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ead1bbc6-7e5e-33cc-8273-419e79bdcd90 | -5.05503 | -44.23647 | 2024-12-13 03:55:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de800c95-5967-370e-9459-cfbb4ac0c575 | -1.53252 | -46.29803 | 2024-12-13 03:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c82132ec-654c-3561-80b4-de7a69101a87 | -7.58482 | -47.11699 | 2024-12-13 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b0704f5-2b2d-3923-a690-c3c5638b990f | -3.47588 | -45.80091 | 2024-12-13 03:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d462977d-9950-3a67-85ff-ffec581f6528 | -5.19917 | -43.29515 | 2024-12-13 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e790e6f1-15fc-35e2-b75e-585baa35b06f | -7.86359 | -39.74294 | 2024-12-13 03:55:00 | NOAA-21 | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 63f7a151-b1c5-320e-81a2-ea3f732c7359 | -5.21124 | -43.29697 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 75c10729-8b91-30bc-87b8-ffd0a7f1dcc4 | -4.18057 | -42.4379 | 2024-12-13 03:55:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6d9492d6-c758-3333-b29c-188b716bfd32 | -3.37789 | -42.32785 | 2024-12-13 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d0cedfa6-f34d-35e2-a2dd-58fc62fdf222 | -6.92376 | -43.53196 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e38e54d0-6436-3547-810e-0801781bcec3 | -6.77027 | -44.825 | 2024-12-13 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f87d76f-2a11-3a1b-bf07-1a223cc0b764 | -4.86031 | -38.44018 | 2024-12-13 03:55:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 24a359b0-71fb-3446-a268-33daf5118092 | -6.30664 | -43.4684 | 2024-12-13 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cd7131ec-97c0-3a37-b579-9172e259451b | -3.98381 | -44.5681 | 2024-12-13 03:55:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9c1996c-afae-303d-9d7b-2807ddf83ac8 | -6.91668 | -43.5255 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7909519e-036b-3cce-9110-a1a0a6abe437 | -4.1632 | -43.06336 | 2024-12-13 03:55:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 704d524a-713a-3884-9245-b6642bfdc405 | -4.55159 | -43.57531 | 2024-12-13 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 557af2e2-9c66-3c2f-bf42-5adf4b887b84 | -3.70175 | -50.93924 | 2024-12-13 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bcc6fd94-cf99-3e0f-af2f-6cad9454c631 | -6.59212 | -44.16325 | 2024-12-13 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4617c250-3566-351d-a803-bc15da0715df | -6.92218 | -43.54139 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d78e25d-1faf-3938-865e-6e862a316662 | -13.05915 | -52.0389 | 2024-12-13 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c2444b14-d804-3328-979c-7ece6e346c28 | -10.89789 | -40.41053 | 2024-12-13 03:57:00 | NOAA-21 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6dd1a268-b25b-3bb2-9359-5d7abb80a241 | -12.36391 | -45.67376 | 2024-12-13 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9abb4677-b23e-3a55-85d7-ecbb10337f6d | -9.16979 | -49.47387 | 2024-12-13 03:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8b14b846-3fcc-364f-a9d2-881ba988f816 | -13.06537 | -52.04014 | 2024-12-13 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3651d799-07df-331d-87bf-53b3e6e81c06 | -12.92411 | -47.89131 | 2024-12-13 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3a87334-329d-3a4e-9dbe-67246576f6ca | -12.35235 | -44.71553 | 2024-12-13 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a43f85c-c38f-35dd-9cb1-1a9dc4e1daea | -12.05493 | -46.88642 | 2024-12-13 03:57:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38102275-a27d-34bd-b38a-58b237ec2ca2 | -11.16119 | -49.44127 | 2024-12-13 03:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78f8f07c-9a85-32bf-a864-c26348ebc9e3 | -13.70624 | -43.98369 | 2024-12-13 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddd8fdd2-f8fd-3236-9b5a-a0d37dbc76c4 | -13.57563 | -41.99607 | 2024-12-13 03:57:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 61ff91d5-2354-3b95-862d-4d88657dcf41 | -10.32722 | -42.39527 | 2024-12-13 03:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a2615824-da99-3905-bb82-58881f36a24d | -12.41444 | -43.80087 | 2024-12-13 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c900973-c191-341e-80c3-76e857cbb968 | -11.48211 | -48.22141 | 2024-12-13 03:57:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d683b748-eaa2-3eae-971a-1382efeccceb | -11.20902 | -53.83239 | 2024-12-13 03:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| aadada09-7485-31e2-ab8f-9c2a021a616a | -14.16146 | -39.02549 | 2024-12-13 03:57:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 09bb596d-57fe-381c-963e-7aac99b1183b | -13.07263 | -52.03627 | 2024-12-13 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4ff9112d-946a-3a87-9c8b-8bfadc949759 | -13.05809 | -52.04401 | 2024-12-13 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1870eb93-d8c0-3e0d-8e26-d372f16a9023 | -11.1619 | -49.43763 | 2024-12-13 03:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a57ff289-87f6-3807-81a7-b0c1dd68a26a | -11.48311 | -48.22016 | 2024-12-13 03:57:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed82f638-b479-3f02-9daf-79e9cd343173 | -11.68564 | -48.07383 | 2024-12-13 03:57:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9679e3d-1e3a-3a3f-8281-b72b0556f98e | -14.16256 | -39.01817 | 2024-12-13 03:57:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c3eeba3c-091c-31bf-8d4a-8afeec52d51a | -12.35628 | -44.71624 | 2024-12-13 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 689ef461-b1bb-38c3-b965-ff226f4d903e | -14.16592 | -39.0187 | 2024-12-13 03:57:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e9edf1a2-fcc6-31b6-952e-1d8e28850145 | -9.19815 | -49.4793 | 2024-12-13 03:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fc4f90e-1c24-3735-96f6-4573d8a3c031 | -13.0602 | -52.0338 | 2024-12-13 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README14.md)
