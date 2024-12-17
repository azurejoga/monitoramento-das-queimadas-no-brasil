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
| 53605d64-b327-3ade-8be3-7dc7be9498ce | -1.4565 | -46.792599 | 2024-12-17 00:09:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e40860c-8fd1-34a3-a1b1-781c33255dc2 | -1.4045 | -47.465199 | 2024-12-17 00:09:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f21ee5f9-0142-3c3b-aae2-f432c65f159c | -3.1458 | -44.457001 | 2024-12-17 00:09:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ec7845d9-6a9b-3ca9-b351-7ba91246d53a | -1.4592 | -46.8046 | 2024-12-17 00:09:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42d3ee99-3369-3414-b50b-39c2cb8b7f60 | -2.811 | -45.113098 | 2024-12-17 00:09:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3412707c-47b0-391e-a0b1-ee42ae5263d4 | -3.2296 | -46.7929 | 2024-12-17 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca91df07-f424-38c5-8276-909a8b5156e3 | -4.226 | -44.004601 | 2024-12-17 00:09:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6f1b5e9-c309-3757-b92d-94e26d25bd26 | -3.9528 | -47.007702 | 2024-12-17 00:09:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a18fd2f8-fead-3438-a604-fe63d856a489 | -6.9653 | -40.627602 | 2024-12-17 00:09:00 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 25224937-e6e6-3af1-909d-23cce3dd026c | -1.6299 | -45.839802 | 2024-12-17 00:09:00 | METOP-C | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8580288-41df-3927-916e-4b252e691705 | -5.3854 | -40.659599 | 2024-12-17 00:09:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bfde3ca7-ee19-3524-a736-40f02f7cdcdb | -8.8729 | -41.098701 | 2024-12-17 00:09:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| edcfea13-a757-375d-85c2-c7ffb45aaf24 | -2.1325 | -48.011902 | 2024-12-17 00:09:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93ec6835-41dd-3e47-bef6-be460a2056f2 | -7.2181 | -44.9203 | 2024-12-17 00:09:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd4b531c-e610-3f1a-a77b-7235cb4f4fb5 | -4.7848 | -46.377102 | 2024-12-17 00:09:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e07c2172-882b-3a16-9493-0179b6879480 | -1.4015 | -47.452 | 2024-12-17 00:09:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d31814b8-2dc9-3cbf-b557-fb10ae5bdb4e | -9.0138 | -35.964298 | 2024-12-17 00:09:00 | METOP-C | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 945c9a13-36d6-33d9-a7bb-65de0737a025 | -4.1178 | -43.568802 | 2024-12-17 00:09:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82371662-bca7-365c-a8e5-813a0eb1b957 | -5.2159 | -43.2845 | 2024-12-17 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18ba2645-0e3b-31d4-ae96-1287c74b96d6 | -3.8472 | -45.843399 | 2024-12-17 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b26d1a0a-ebe4-3c6e-8206-89e8fe68ec88 | -3.136 | -44.459202 | 2024-12-17 00:09:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f10c8153-5694-3443-87d8-82234a63b68b | -2.568 | -45.947701 | 2024-12-17 00:09:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 196b9912-9155-39da-a3d3-888750208800 | -5.6206 | -44.8283 | 2024-12-17 00:09:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4f8a98b-7309-32e6-a057-97d8e1808f96 | -3.1749 | -46.685699 | 2024-12-17 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43dfac90-3cbb-34f3-a806-69bc35bf4410 | -1.6323 | -45.850201 | 2024-12-17 00:09:00 | METOP-C | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 95afe160-45e3-3fe3-8daf-46691e9df01c | -4.7095 | -38.435799 | 2024-12-17 00:09:00 | METOP-C | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c3af74ed-a8a4-38b1-b7e2-71953de1927a | -5.1423 | -43.230999 | 2024-12-17 00:09:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af5a5113-bd33-3a9d-a698-b988ee821afc | -5.73 | -35.439301 | 2024-12-17 00:09:00 | METOP-C | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 1cf227cd-a46e-3312-92cd-ffe8c889e16d | -3.6557 | -47.143101 | 2024-12-17 00:09:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40356836-8798-3168-88e5-912fb4f5e4a5 | -4.5562 | -43.552101 | 2024-12-17 00:09:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0faef23-7877-37fd-9a49-4461412b5e3b | -6.2023 | -46.2216 | 2024-12-17 00:09:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49eeed66-d0f4-3c41-a964-d0737bbdec2f | -5.8674 | -39.1604 | 2024-12-17 00:09:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6487936c-70ef-382b-b925-041edee391a6 | -7.4076 | -44.709099 | 2024-12-17 00:09:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7aab6c27-ac2a-3f6c-8333-185e16d3e528 | -4.8563 | -41.369301 | 2024-12-17 00:09:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 727edbb8-03ec-346e-b1d2-63dcfc8876e3 | -5.1325 | -43.233101 | 2024-12-17 00:09:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f008b8f-31f8-32ab-adc7-47eab6957fd5 | -2.0399 | -46.6516 | 2024-12-17 00:09:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60b1c837-261c-3807-9fbd-0346a7d01207 | -3.1721 | -46.673199 | 2024-12-17 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76763913-4f67-35e9-8f43-09f75de26182 | -3.8349 | -45.834301 | 2024-12-17 00:09:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44acd872-380a-3150-9791-42f6c5bb1ad3 | -3.862 | -47.0131 | 2024-12-17 00:09:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 59c033a2-844f-3d4b-bba6-12036bbfa2af | -4.8901 | -44.171501 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7483cd0-babd-3e2e-817a-c6197adadefa | -2.5656 | -45.936699 | 2024-12-17 00:09:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b396c283-ff85-377c-9764-0ad4ef6fe5be | -9.9523 | -36.3074 | 2024-12-17 00:09:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bea35f97-a6b3-3eb8-9820-a74d3097ede4 | -4.8782 | -44.164501 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41839281-4260-39a6-be43-7d53b5d2e71c | -5.2061 | -43.286701 | 2024-12-17 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00eefa90-5ba1-310f-adb2-dcef48a2f334 | -5.1002 | -43.916401 | 2024-12-17 00:09:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85a36b52-3cc5-313b-9a3d-fd8abbc54063 | -5.1134 | -43.194099 | 2024-12-17 00:09:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 953bb96d-c18c-39e3-a15b-7f767f12c772 | -4.4488 | -44.632999 | 2024-12-17 00:09:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 844a669b-ecbc-3b82-aa4e-5cab90cb4d11 | -3.2365 | -46.778099 | 2024-12-17 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2dbfbfc7-a637-36f7-87d6-1b77a04e6ea7 | -4.7876 | -46.389801 | 2024-12-17 00:09:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c908df6a-3888-3e64-9cc4-68c6f87fe66a | -5.7002 | -46.777 | 2024-12-17 00:09:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bacaf0e-c7d5-32d7-9601-7e939178812e | -3.9835 | -44.160198 | 2024-12-17 00:09:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65e3c0f0-f647-3761-935d-9d7e338687eb | -1.3948 | -47.4674 | 2024-12-17 00:09:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f63f13d0-39f5-3427-8501-2ef2c99f3959 | -4.8823 | -44.182899 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57f593fa-62ad-3551-ad8c-2c4464273772 | -2.7188 | -45.205601 | 2024-12-17 00:09:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 07a3fb29-544d-37fd-867a-6a7ee5ef11b8 | -5.3937 | -40.650501 | 2024-12-17 00:09:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 108612b5-eb9e-3009-b9e5-3cc6b4be700e | -1.6225 | -45.852402 | 2024-12-17 00:09:00 | METOP-C | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ee056178-cdfa-3171-a805-fd708ec93cce | -5.933 | -43.782398 | 2024-12-17 00:09:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92a6a0df-b09d-30ae-9ae3-1cf08669b76d | -5.9784 | -44.591 | 2024-12-17 00:09:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3710cdfc-b255-375e-b014-ea8b06e022a6 | -5.0982 | -43.907398 | 2024-12-17 00:09:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51c73c50-784f-3bdd-a78f-593509a24747 | -5.3519 | -44.0326 | 2024-12-17 00:09:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 978ee31f-900c-3a63-a7f3-dddeacb643f1 | -4.1719 | -42.440498 | 2024-12-17 00:09:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 591881a8-5b09-37c4-af13-334f16d5b211 | -4.7946 | -46.375 | 2024-12-17 00:09:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8a4377e-ab7a-39b4-b03a-5050ac969195 | -2.6527 | -45.549301 | 2024-12-17 00:09:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4fd0f658-c1a3-3ccf-9656-0d5c5ad30980 | -5.7705 | -44.346199 | 2024-12-17 00:09:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c49345e-694e-3e28-beef-f788ab3b9d4b | -6.1966 | -46.195702 | 2024-12-17 00:09:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39b122d8-f3dd-37a7-9bf2-010dbec02c2f | -7.5656 | -35.087799 | 2024-12-17 00:09:00 | METOP-C | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b730bfcb-4ddf-3fab-a78c-48f7d84242a2 | -3.7794 | -47.102001 | 2024-12-17 00:09:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62da21ef-678c-39f1-8c09-04f65519d9b0 | -4.6731 | -44.028198 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f7bb7d5-fc49-3e4a-898e-cc299ce92fd8 | -4.116 | -43.560501 | 2024-12-17 00:09:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57528081-459d-31da-824a-184ee3f4a204 | -5.0962 | -43.898499 | 2024-12-17 00:09:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81820b7e-5288-397f-ab94-3e31debac3c9 | -3.9182 | -45.426998 | 2024-12-17 00:09:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d1b1f50-35f4-3f9c-8a71-ac16163765cd | -2.1272 | -45.632198 | 2024-12-17 00:09:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 130912c0-8fbf-38c2-ae86-b74ca1f06a36 | -6.9751 | -40.625401 | 2024-12-17 00:09:00 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3c148f9e-c862-38d0-964c-7e1a507fb031 | -5.0844 | -43.891701 | 2024-12-17 00:09:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79804d96-2c94-3274-ae38-6678d99c0629 | -4.7974 | -46.387699 | 2024-12-17 00:09:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 325c54c5-73c5-37d0-9be7-bccb31db8427 | -3.228 | -45.369301 | 2024-12-17 00:09:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 640384d5-8722-3fff-85b4-f295346174c3 | -0.7395 | -47.738998 | 2024-12-17 00:09:00 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebb5ee0c-e226-3842-80ac-d5bf2dd3addb | -4.4586 | -44.630798 | 2024-12-17 00:09:00 | METOP-C | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58211ab6-929a-3e47-bcbd-095e299325bd | -3.2257 | -45.359001 | 2024-12-17 00:09:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd9f7ce-7522-3f88-948b-3f3749962d32 | -6.2063 | -46.1936 | 2024-12-17 00:09:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78147a5e-0c07-3f48-aaff-f84703e46c82 | -5.0884 | -43.9095 | 2024-12-17 00:09:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02d4fc29-5fe0-32c1-87ac-f2f1665d4c03 | -5.4856 | -39.115601 | 2024-12-17 00:09:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 36c37d47-5475-3cbd-b94e-a030c1b6e026 | -2.721 | -45.2155 | 2024-12-17 00:09:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0045a3f9-a16d-31dd-a36d-23ecdfff3021 | -4.6462 | -44.321602 | 2024-12-17 00:09:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1981143-8aed-3bd0-9d23-b6fc1013ee6f | -4.7527 | -46.6954 | 2024-12-17 00:09:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fd7d40dd-f8a0-3f71-92cb-4af26f7b3eef | -12.6855 | -38.397202 | 2024-12-17 00:09:00 | METOP-C | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c4cdc6d8-5d70-39c6-bcff-cd3c31e9472a | -4.9607 | -43.7062 | 2024-12-17 00:09:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3aed3b33-facd-3a60-bfa7-5ee83a14aee8 | -6.1952 | -35.226398 | 2024-12-17 00:09:00 | METOP-C | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3e1899c4-508f-3fff-b019-bceaf3b56709 | -3.7593 | -47.149399 | 2024-12-17 00:09:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8541ea81-236b-3cf6-ad5d-d37069d81353 | -5.3617 | -44.030399 | 2024-12-17 00:09:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72626fe3-ae52-3236-903b-2fcbae331694 | -5.9075 | -42.883099 | 2024-12-17 00:09:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1af0f30d-9e62-3d1e-b3d0-792c84e593d9 | -12.0816 | -38.008099 | 2024-12-17 00:09:00 | METOP-C | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e64f26e1-3a0a-3554-847a-c61f3d3c60b5 | -5.8789 | -35.4147 | 2024-12-17 00:09:00 | METOP-C | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 91bd2e08-c328-3751-b89b-1addd42c6d9b | -5.1306 | -43.224899 | 2024-12-17 00:09:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5cf81fb-d9f7-3f6b-bcf3-046c39021954 | -5.0766 | -43.902699 | 2024-12-17 00:09:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4091ebca-84bd-319c-a8fd-92ed037d5854 | -4.7112 | -38.4431 | 2024-12-17 00:09:00 | METOP-C | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 78bb2f7b-5fab-33df-a8db-46775aa2e66c | -3.2268 | -46.780201 | 2024-12-17 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaede5ea-7911-3e60-8614-ba487882069c | -5.2613 | -41.383202 | 2024-12-17 00:09:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 22c0a80f-a083-35b3-a090-b088848c47a0 | -3.9558 | -47.021198 | 2024-12-17 00:09:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6e7115-54b9-3a8d-8cb7-7a3cde962b24 | -5.1773 | -37.518501 | 2024-12-17 00:09:00 | METOP-C | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README3.md)
