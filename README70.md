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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6414de67-6c18-34b9-b5f0-7d6585eddb76 | -5.608 | -42.8798 | 2025-09-05 14:30:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| bb05a13b-d09a-3edb-be74-5e188752bac9 | -11.2005 | -55.0195 | 2025-09-05 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 991e5ad8-9039-3ad1-bd9d-a60ac3b154ff | -12.1316 | -50.6335 | 2025-09-05 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| a0db9052-bce1-38dd-a004-5be634d0a99e | -5.55 | -43.0719 | 2025-09-05 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 458bad87-ba8e-34ac-8512-2c179835d1b0 | -13.884 | -47.9929 | 2025-09-05 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 6e788426-1750-3b4a-a296-1405284aa214 | -6.2421 | -43.2743 | 2025-09-05 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 265f03be-825a-3368-b859-4bd9d96669d1 | -6.0043 | -46.7018 | 2025-09-05 14:30:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 4639d055-80c4-3d7f-9d5c-b6501b5b20b5 | -6.2857 | -53.4369 | 2025-09-05 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 98b01f6d-04f8-3c57-8b62-92bb22f71954 | -12.2535 | -50.1464 | 2025-09-05 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 517a1e89-ea88-3f4e-ab88-9ff0a6b4b09b | -14.0499 | -53.9914 | 2025-09-05 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| a11c9334-644d-3a1a-a0d6-2747b8e2189d | -15.4571 | -52.9759 | 2025-09-05 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ecf3ae7d-aded-3cfd-9f63-218d79d0e9ec | -5.6432 | -43.135 | 2025-09-05 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 0499f31d-73f2-3a44-b35c-1663bb685584 | -7.6083 | -43.8477 | 2025-09-05 14:30:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 1ca6eb1d-38cc-3a6b-83f6-e8f764d429df | -6.1679 | -43.1869 | 2025-09-05 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 93674ea7-f5c6-32d8-b0aa-dfdea04c2417 | -8.5187 | -51.3293 | 2025-09-05 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 2d4c4071-cf3b-3f72-af5f-fb071976bcad | -8.2001 | -49.5988 | 2025-09-05 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| dbe6f034-43cb-356e-b381-90e33040d7be | -9.6916 | -48.9872 | 2025-09-05 14:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 22a1ad10-3871-3076-ad5b-bff26f29f38e | -8.3456 | -48.3133 | 2025-09-05 14:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 5f49a7f4-ee5b-3a8a-b4ef-a8b81f16ae36 | -5.7925 | -45.2852 | 2025-09-05 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 6fe64738-e8fb-3575-a304-79db095ee0eb | -11.0058 | -45.93 | 2025-09-05 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| cd6471cb-4d5e-3714-b918-13fad1dadbb6 | -6.2299 | -42.6173 | 2025-09-05 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 5bee83ea-3e2a-32e7-bc55-2402a924b077 | -9.7762 | -46.9132 | 2025-09-05 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 4a820c15-c2e3-3fd6-b364-991cc9511de7 | -5.9173 | -45.9735 | 2025-09-05 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| db3ccecc-ca23-3ece-a4ac-80c726d72cb5 | -5.8877 | -45.0972 | 2025-09-05 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 8a12d399-8449-3059-9e9e-db2638051127 | -5.9846 | -44.7261 | 2025-09-05 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 78d5379a-280e-3d64-ad77-d9674879920f | -15.6141 | -52.891 | 2025-09-05 14:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 132.9 |
| ea949513-f857-3f8f-b79c-b9be7ea152e8 | -13.3192 | -51.6626 | 2025-09-05 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| a97261ef-9966-3f2d-b8f2-6c73f4d71ffb | -11.2005 | -55.0195 | 2025-09-05 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| f4f1dcb5-55a3-34d5-8ce8-1326bc3866aa | -16.3149 | -52.9415 | 2025-09-05 14:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3b81a617-7158-31e2-ad97-7de78742293c | -11.6238 | -47.7786 | 2025-09-05 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 2a736efe-a546-315d-9602-b2a819fdcebb | -5.9846 | -44.7261 | 2025-09-05 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 170.3 |
| d26fab79-d0f6-307d-8c78-428713f901bb | -5.7736 | -45.3091 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| f202f38b-d5ca-3e61-8484-f601ccae56a2 | -5.6992 | -45.2692 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 9d30063d-3f5e-3ec6-8eae-8414bbadb23c | -5.7925 | -45.2852 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| ea337072-5d72-34cd-9a1f-0484f1e07319 | -6.2194 | -45.6373 | 2025-09-05 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f7e8a18b-c31f-3734-b3d3-27881cf887fc | -5.9844 | -44.7489 | 2025-09-05 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 8170cfc3-716b-3c48-8e93-071c8ea1a7d5 | -8.3364 | -47.4824 | 2025-09-05 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 7a3f6bf8-397b-3b77-b6ed-338bd95f6ac6 | -15.7182 | -53.5954 | 2025-09-05 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| ec69967f-a7ac-3568-9311-ea25269b60fb | -8.9034 | -45.7973 | 2025-09-05 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 992673f4-cd61-3ebe-abec-f315c3efac5f | -6.376 | -43.0287 | 2025-09-05 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 0a85b4d6-c65d-3e79-857a-b2efa8d4fbdf | -7.358 | -44.3344 | 2025-09-05 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 66b79621-2a86-38c5-b47c-893358c063e4 | -10.2373 | -50.5417 | 2025-09-05 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 83d3a83b-4cf6-3a1d-830f-057495a3cb52 | -8.5573 | -62.633 | 2025-09-05 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f920a976-81f0-3f9d-b790-8bbebccbc035 | -6.9568 | -44.9434 | 2025-09-05 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1581e03d-8a40-3702-9618-303912376cf2 | -7.0128 | -43.2525 | 2025-09-05 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 0fb0ba32-4ef2-37e7-9dd5-3385789aa591 | -15.4571 | -52.9759 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 139.9 |
| f5098298-dbf7-326a-8a31-cea2921574e9 | -6.9167 | -45.197 | 2025-09-05 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 5fdbe264-c9e0-3daf-a8d0-53590ef8a1bd | -5.811 | -45.3065 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0c612726-cabd-38b6-8306-7cead4d85c36 | -5.55 | -43.0719 | 2025-09-05 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 74f51d09-5181-3ec1-96b5-bd3ff1706fb1 | -6.6957 | -44.8062 | 2025-09-05 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 9d5ec1d9-2d44-3ad3-8c28-d1d36919da3b | -15.235 | -52.3693 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 39a35707-04ed-3105-aa80-b37084896d9c | -12.2535 | -50.1464 | 2025-09-05 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 3147dc33-cb13-3455-bcec-4ff5b904e36c | -7.8011 | -52.1331 | 2025-09-05 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2677f88b-5f18-3cd9-af61-40ec51e1a325 | -14.0499 | -53.9914 | 2025-09-05 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 1bcacca1-e283-3745-bd70-2b164ec19e4c | -15.6141 | -52.891 | 2025-09-05 14:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 127.5 |
| ae7d7a7e-d6ae-3734-99fe-1c1857b29832 | -11.6235 | -47.8008 | 2025-09-05 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 40357881-2770-3dbe-be8b-c81c43400b39 | -14.3737 | -52.9903 | 2025-09-05 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 17028981-d66f-3ee8-a7d0-7d81111edbeb | -6.2672 | -53.4379 | 2025-09-05 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 113ac0eb-06c8-398d-a36d-a02d26278935 | -6.6954 | -44.829 | 2025-09-05 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 171092d9-919a-3681-977a-ecf54864bc34 | -15.3071 | -52.6783 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| fa22d45c-d429-3052-9275-8fc9fc137ed3 | -9.7105 | -48.9853 | 2025-09-05 14:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| a10c068b-eb1d-3fce-b4b8-3ecd382ef0aa | -6.2421 | -43.2743 | 2025-09-05 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| a99fbd33-ef42-39b0-8a90-ffdb0c3346b2 | -15.7554 | -53.6957 | 2025-09-05 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 0642c495-29d5-3c62-a092-adb8f201f2fb | -5.9963 | -47.6478 | 2025-09-05 14:40:00 | GOES-19 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 505bb060-c22a-3da8-a2dc-e0869e0798e0 | -8.9037 | -45.7747 | 2025-09-05 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 5f73f8a4-0e99-32d7-b604-21cb14b080ea | -15.2877 | -52.6809 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 183.3 |
| c8ee7bc5-2946-3471-8805-9de1e4bfeec8 | -6.1679 | -43.1869 | 2025-09-05 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 8cf71300-260d-31b1-9d5e-697283806e69 | -6.2609 | -43.2727 | 2025-09-05 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| d853a5ba-90f4-39be-9ca2-eb5b5aee0fea | -8.3458 | -48.2916 | 2025-09-05 14:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| bc5cd41c-e315-3945-bdef-35fbd208b359 | -11.864 | -50.7075 | 2025-09-05 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 05352d09-448b-3e18-a3fe-b3273a54f8c0 | -15.7565 | -53.6324 | 2025-09-05 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 9d94cdf6-8411-38a0-8c85-1a4a372132fe | -10.9852 | -49.7778 | 2025-09-05 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| c7a6bef8-ca3b-36c5-9fd6-7741c01c81c0 | -7.9252 | -63.2608 | 2025-09-05 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 8687949d-907b-352d-a59a-cd1951eb1bb2 | -6.2418 | -43.2976 | 2025-09-05 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8c52d12b-26f4-3e96-9238-28ca5dd3cc21 | -15.7756 | -53.6509 | 2025-09-05 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 3a9cd04e-4e6e-3e1a-b17f-76d7b40bdc00 | -8.2004 | -49.5773 | 2025-09-05 14:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 752ea365-0f5c-37fe-b21f-867a806c33f1 | -8.6882 | -62.4192 | 2025-09-05 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ee4bf191-4f67-33ed-9540-088be8edbe79 | -15.1831 | -48.0303 | 2025-09-05 14:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 4a7023a0-ce81-346a-b7b0-3e0865a7d871 | -15.3435 | -53.9382 | 2025-09-05 14:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 542958be-0748-3703-9f5f-1c6f3e0ce778 | -7.0502 | -43.2724 | 2025-09-05 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| efc1a10d-2744-37d2-adf2-3c9ca79d6021 | -15.7561 | -53.6535 | 2025-09-05 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 228.0 |
| 297d8345-563c-3fd2-8f5d-3c4329e2fd5e | -7.8923 | -45.2893 | 2025-09-05 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 3a356a51-9e91-30af-a7fb-a7da0ad846c5 | -8.9031 | -45.82 | 2025-09-05 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 1fe3adb4-5aa1-3d19-841d-cf1e04fcbb59 | -6.8981 | -45.1759 | 2025-09-05 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 1d3d6027-9b2c-340a-b0cb-f10190f6d67e | -5.7179 | -45.2679 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 1a3458ed-d608-3da5-a788-d8c02d19b894 | -13.884 | -47.9929 | 2025-09-05 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 8634ed6b-fef9-3403-8141-88a150bd8b67 | -8.5187 | -51.3293 | 2025-09-05 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 273.6 |
| cc2cbb59-65a2-3c8d-95fa-f0fa06e9f9ab | -7.0314 | -43.2742 | 2025-09-05 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.9 |
| 2aae938d-ad6a-324a-b9ef-55491e8de8c6 | -15.4567 | -52.9971 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| b4410490-e7a1-325b-897c-a3d29c7c2bd4 | -7.53 | -47.4662 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 97605317-e324-330b-9d8c-c6390554764e | -12.1234 | -43.35 | 2025-09-05 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 633e8d89-d815-35da-9971-6aebbcf42ab6 | -4.6973 | -41.951 | 2025-09-05 14:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 182.2 |
| 9976de68-32d6-30a9-adab-28ab736e817a | -6.2381 | -45.6358 | 2025-09-05 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4ef85c5c-642e-3958-8a24-35d0b9165119 | -7.7128 | -61.5276 | 2025-09-05 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 03a0a6e4-9b8a-355a-995c-c5c6f642ebc1 | -15.7558 | -53.6746 | 2025-09-05 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 35e0269f-8b27-39da-bcda-b9ea9818d402 | -9.7762 | -46.9132 | 2025-09-05 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 339db340-81c3-357d-8ce3-c4f2115b54f7 | -5.9443 | -43.0178 | 2025-09-05 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 77ad7a91-69d2-3f51-8c73-80c03487f5c6 | -7.6186 | -47.9406 | 2025-09-05 14:40:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 7f174423-ce72-3fc9-b5ad-4bfbce8236bd | -5.1585 | -45.1698 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| da7c6b3b-40b4-3a27-9c59-b49a5ee77687 | -8.479 | -45.0704 | 2025-09-05 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |


[Clique aqui para ver as próximas entradas](README71.md)
