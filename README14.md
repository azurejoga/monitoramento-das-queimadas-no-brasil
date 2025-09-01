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
| ed5bba10-18cd-3a9c-941c-b91bb2c966dc | -6.14922 | -44.14796 | 2025-09-01 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dac5e7ce-8a83-3a78-828e-0542920b990c | -6.28255 | -43.29277 | 2025-09-01 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af885b9c-175d-3773-8878-df4bb005c580 | -6.50313 | -43.56361 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f35f3fe-8a9c-3105-827b-b48f2e50c2d0 | -6.82754 | -43.3305 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| e31f84d9-60be-3487-8fec-c369bd96bd0b | -7.07473 | -44.35715 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4380d45a-6581-3eaf-8a91-23510d3a640c | -6.09483 | -43.18449 | 2025-09-01 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| acacab35-50d5-3839-9eba-4d19efd7acd9 | -7.0868 | -44.34954 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 1f86a205-afdc-31bf-9048-f99f315f105d | -7.24581 | -44.24258 | 2025-09-01 03:42:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa111eff-fa15-3379-b38b-866c0b669e7d | -6.52157 | -43.54552 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a86f2c5c-0460-3256-8b05-4f651ef85dda | -6.81259 | -45.68855 | 2025-09-01 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c1fe052-f722-3302-a9f1-bcabfe3820f8 | -7.08508 | -44.35925 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| d57f77d2-8642-394f-b120-9865436bf934 | -6.16006 | -43.34489 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ae37711-d863-3be7-b6a3-9d2f58b32dea | -3.42243 | -43.3308 | 2025-09-01 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 571ab9a6-f6ee-3392-a2a9-aca9c55a49be | -6.81003 | -43.34446 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b8e8eae2-b2ba-36d8-ade9-1f6172d16f94 | -6.42391 | -43.9638 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4826ab8-5d98-3c21-8b24-64783950db6a | -6.80773 | -40.5887 | 2025-09-01 03:42:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 95081428-2a53-301c-b0d2-9cc7a11720fd | -6.24164 | -41.82634 | 2025-09-01 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a377ffba-8390-3c38-a62a-1249be6773e6 | -6.29836 | -43.6153 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dff0cb7-6faf-3e9e-8d96-589642e50f92 | -6.15514 | -43.34398 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b81f4669-efe3-39b9-9639-1c5abfe57814 | -6.50968 | -43.55521 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb3920c5-769c-31cd-a0c7-a41c78ad8a57 | -6.50866 | -43.56119 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c57c3d9-3e4d-32da-9f0a-8e27a32f7f48 | -6.29289 | -43.55833 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e39a92b7-689a-3072-a8f6-b4859a07ef79 | -5.32833 | -42.86528 | 2025-09-01 03:42:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4acfbe4e-97c1-3f79-80a3-13bdcde26b6f | -6.8217 | -43.33516 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 49660a95-8b80-3f32-bf77-197bfcb2a634 | -7.07703 | -44.34421 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 09cd226d-8b3d-3396-a10c-bbb3a2c1c3c4 | -6.29781 | -43.61839 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1ab8ff6-eac4-35ee-b352-e72343c0702d | -7.10861 | -44.56108 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25292e54-c008-3bf1-9647-81eccb89b33e | -6.75903 | -43.78188 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7a3215c3-0d74-3153-8d28-d4f0e51e53db | -7.06837 | -44.33269 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a5e4a0f1-3d52-3ffc-8967-43a3ed56bf09 | -6.30227 | -43.62449 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 11c41f08-0566-3b3a-804a-b133af59fcd2 | -7.09255 | -44.34734 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1d3218bf-5cdd-372b-8d5e-c935b2ca5c5e | -5.64935 | -43.65239 | 2025-09-01 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e388c709-d176-3e88-adc1-057bb9ea64a0 | -7.09367 | -44.34099 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 058521ba-5dac-3251-93ed-b814bd6684ca | -5.85236 | -43.21757 | 2025-09-01 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b919c52a-d49a-3250-9b6c-bfa663e6e845 | -6.45407 | -43.95742 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a65b592e-7d18-3348-98fc-e9c9409ed6a6 | -6.84032 | -43.34364 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e58f88d7-acd6-3414-b542-8442ef23a5f8 | -5.97738 | -44.26451 | 2025-09-01 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc97b744-f687-3a89-864e-11f218cbea93 | -6.29048 | -43.30529 | 2025-09-01 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f57d582b-dbae-3b7d-8d4a-be6548b15514 | -7.08386 | -44.3359 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 760a3511-c36d-3732-9f3e-695f9a94908e | -7.08222 | -44.3452 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| fb9fcf79-7d1d-33bf-a148-68d7da76ccf0 | -6.40964 | -43.62798 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5bc9c85-3cbf-3454-8fa8-334dd0712b0f | -6.26493 | -43.54156 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69a47405-5786-3598-ab4d-95333b125e46 | -5.64475 | -43.6487 | 2025-09-01 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07f1dcd7-b43e-3dfc-b365-f0dd29b04162 | -6.57001 | -43.71366 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c24eb47d-061e-3321-9577-f27545ef47e6 | -7.07072 | -44.34959 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c2cea85f-a349-3d93-9db4-6c5d5761200d | -6.15318 | -43.32614 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 412e79c2-e66c-3198-a2e6-b5e02ce2fd22 | -4.90896 | -43.18798 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbb12e42-ae1c-3d71-91e7-10514736caff | -7.11025 | -44.76474 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17f1bc86-55dc-31cc-b178-f80c6520f7d7 | -6.17474 | -43.31881 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8c42dfc0-595d-3b21-a493-8fd71830d5be | -6.74389 | -43.77953 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3fcfa6cf-8054-3559-870c-39d2bfcd478d | -6.29166 | -43.62616 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ebd5746-d723-33c4-9a09-44c3cff98e11 | -6.28948 | -43.31109 | 2025-09-01 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| baf8e642-e421-3775-8e65-61e0f105f44c | -7.06781 | -44.33583 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| daa65323-f706-3165-a1cc-77509bcd7da0 | -6.19652 | -43.33953 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 63b29de7-0f98-39d6-9eef-5cf0029eee39 | -6.31095 | -43.63176 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 346999ee-3293-3aa5-9986-31fa29629bc2 | -4.90992 | -43.18232 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22a9d23c-2493-388d-8510-1756b3517ad5 | -6.15712 | -43.33266 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 351b2aba-a3d0-37dc-bdb6-d769a6fecc71 | -3.42707 | -43.33465 | 2025-09-01 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b678ffa-693b-313a-b2e9-8f28c67defc0 | -6.98222 | -43.12143 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4d5d1dc-9328-3084-959e-c77fbcde3474 | -7.07877 | -44.36465 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 641e3706-1396-36ab-aa77-695aad171440 | -6.30594 | -43.63087 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b1af0e4f-1121-31f0-8fa1-b3bd8c7d12ce | -6.4521 | -43.95315 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55e9bed2-4597-369e-8b84-dc548ecc945d | -4.91298 | -43.19451 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca01a881-df69-3208-905c-0791d9583562 | -6.1806 | -43.31425 | 2025-09-01 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f71452db-f458-34d8-bed7-b227d30465b1 | -5.64425 | -43.65163 | 2025-09-01 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c305df48-49bc-3aa9-97b6-162a68f8e965 | -4.90848 | -43.19081 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10806418-88bc-399f-8ed5-17851cab5f37 | -5.33315 | -42.85852 | 2025-09-01 03:42:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e6acb087-95f8-308d-b8ea-583092d9d725 | -5.64761 | -43.65197 | 2025-09-01 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e95d8976-e386-3c37-9c26-c4822983695a | -6.58545 | -43.71408 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da8683ff-e99e-3e99-8ccd-8962acd58c7a | -6.71182 | -42.2535 | 2025-09-01 03:42:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 875952ac-ce4a-3f17-bbba-0776a289807d | -6.76808 | -44.62824 | 2025-09-01 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de3f9ae0-d970-3e0c-841f-8451fac3d65b | -6.15906 | -43.32154 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| efe1d571-d200-3f8e-bb41-a553f81147af | -4.9104 | -43.17948 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36674da9-2f72-3fb0-96f6-0726a4043e1d | -7.10965 | -44.76812 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a92fd518-69c4-3413-8a71-218f436050e0 | -7.07932 | -44.3615 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 5e6866c8-4ac1-3d9f-8e32-38132f53b438 | -6.82848 | -43.3251 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 0c676b8a-6ffb-341a-a46a-9e157ca2e508 | -6.7838 | -44.62256 | 2025-09-01 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8068bec3-f444-3113-a3fb-b777b124ca37 | -7.10904 | -44.77153 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e62b8d40-110e-30bb-8978-7376b0ce69a4 | -6.30965 | -43.78716 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d88f8d4-d55a-30bb-94d2-7c48516fff22 | -5.9768 | -44.26777 | 2025-09-01 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c48cd3d-28b3-3494-8528-d15c53390b6d | -6.26826 | -42.60978 | 2025-09-01 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a39b5ae6-973a-305f-8434-be4c055d2615 | -6.70796 | -42.24876 | 2025-09-01 03:42:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf878e79-deef-345a-a98e-4f18f3100da9 | -7.11411 | -44.31604 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c65c551f-41df-3dad-b29b-4c08374f19b8 | -5.65034 | -43.64648 | 2025-09-01 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52bfd9df-6db4-309a-a264-010e3a3bd658 | -5.83358 | -45.20024 | 2025-09-01 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 719a2be8-f95d-361a-9bb8-c97e630dfa92 | -6.19811 | -45.37887 | 2025-09-01 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11a722b0-4052-3387-b89c-fad83eb08e3a | -6.29544 | -43.30587 | 2025-09-01 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9c6fa04-ac1f-3b75-bbf5-6531eb6029f2 | -6.23649 | -41.80279 | 2025-09-01 03:42:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2df20eb5-9814-319a-8ac8-e9eda2f90905 | -7.07185 | -44.34324 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a236269e-d14f-37c6-8024-42bae20c879f | -6.2458 | -42.41652 | 2025-09-01 03:42:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8cc85854-5f56-30f6-9e31-9443f89561b2 | -6.24027 | -43.38089 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e5ab6f6-d00a-39c0-bf9d-f4275cbb5698 | -6.15021 | -43.34314 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4eab5263-2a76-3c8f-9cb8-291c7fe85256 | -6.93714 | -42.01585 | 2025-09-01 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0958d0bb-2da1-3997-a3c2-fd16b61941a6 | -7.07129 | -44.34638 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e620fdd-d4cc-3ffd-a92a-f600e1b8ff1c | -7.08622 | -44.35282 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 6bbc4507-4f07-3ffd-bfca-7fd40f421535 | -7.08565 | -44.35606 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 1259a117-ece3-3b15-b8f9-5092fc1272ac | -6.80558 | -45.68416 | 2025-09-01 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a385fbdd-29fd-3bc6-b0e0-fe0cd3c60d64 | -6.16422 | -44.12339 | 2025-09-01 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 856befee-9942-3af9-b2de-1abd47d14dc0 | -3.42473 | -43.33654 | 2025-09-01 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f41e8d14-2e3f-3fa3-9e31-bdfbb8bc7187 | -6.29339 | -43.55542 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README15.md)
