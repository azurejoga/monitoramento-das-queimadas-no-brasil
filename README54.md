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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d08c64a1-bf59-35c6-bafd-526b6d2e6550 | -5.13104 | -41.19279 | 2025-10-26 11:57:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| 774d98eb-86ad-34e7-9124-426c12df2cca | -6.07253 | -38.46843 | 2025-10-26 11:57:00 | TERRA_M-M | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 2c5a8b30-2d6e-33af-bf1b-832480be1916 | -3.70795 | -43.20117 | 2025-10-26 11:57:00 | TERRA_M-M | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0a51a069-4821-3505-9356-609773e11281 | -5.11076 | -43.19879 | 2025-10-26 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 53913e95-3a94-3f6a-b688-a5b48e112cbb | -3.36012 | -41.5215 | 2025-10-26 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 44110fa4-78ea-3501-ab94-702fc423c832 | -3.54061 | -42.05127 | 2025-10-26 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 695fbea0-0c8d-3c93-8c18-3010c6700052 | -3.53306 | -42.04129 | 2025-10-26 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| eea5ba5e-849a-3ab5-a3a9-c075c7318e8e | -3.94707 | -43.27219 | 2025-10-26 11:57:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 24fb6418-410a-352a-a475-3d0f63c5a3a7 | -4.46095 | -43.672 | 2025-10-26 11:57:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 08043c1d-c65d-3423-9729-21b1ec6d50f9 | -5.54822 | -41.24405 | 2025-10-26 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8f202da5-529c-3264-af2d-501b917c700d | -5.66943 | -42.58715 | 2025-10-26 11:57:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 604af55e-96ea-3476-aa28-53b6721dd8ac | -3.51017 | -41.62065 | 2025-10-26 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 74486224-082c-3161-9aba-615a415f613f | -4.61027 | -45.37253 | 2025-10-26 11:57:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0bf7d7a9-2875-38f5-a1a0-128ceba04106 | -3.91425 | -40.54083 | 2025-10-26 11:57:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| b81671b8-afdf-3127-b905-eb73c8631a8b | -6.17304 | -42.62338 | 2025-10-26 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| c8be513c-dce6-3b81-b195-902c57ea827d | -2.90602 | -42.36363 | 2025-10-26 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 511eaf25-5107-3877-9d69-8d6b65657e54 | -5.46349 | -37.85809 | 2025-10-26 11:57:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 53.5 |
| ef35520b-ff16-3df9-9906-62dffeaac76f | -5.47654 | -37.84512 | 2025-10-26 11:57:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 056a7c6e-977b-32c8-93b0-7addc9673f3e | -3.04965 | -42.58502 | 2025-10-26 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2c23c830-e3a2-35fe-8b78-c28fc9159bf2 | -3.54187 | -42.04251 | 2025-10-26 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 176.3 |
| 27a5852c-52d1-37d2-a0b7-022e7442a3ad | -3.24406 | -41.938 | 2025-10-26 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 33dcd4d5-de12-3ac1-b629-4ea7fe9f5be7 | -3.7663 | -47.57549 | 2025-10-26 11:57:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 203.0 |
| 77ebb15a-be0a-38e3-95be-8f1e12991fab | -3.91326 | -44.0058 | 2025-10-26 11:57:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| cc894da7-6778-3e9e-8225-4627d1386126 | -3.76377 | -47.59212 | 2025-10-26 11:57:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 7b33b319-9d25-3677-8cfc-b5372f5c8674 | -2.90729 | -42.35484 | 2025-10-26 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5090a6b7-8632-3b0e-b2a5-63f05a6bef3f | -6.77639 | -37.90813 | 2025-10-26 11:57:00 | TERRA_M-M | SÃO DOMINGOS | PARAÍBA | Brasil | 2513968 | 25 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 21fe4386-6eac-3072-9744-53b57eb9d2b2 | -5.46543 | -37.84368 | 2025-10-26 11:57:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 76.7 |
| b4a1f668-d585-3873-b6b5-97b411b763d3 | -3.3681 | -39.70618 | 2025-10-26 11:57:00 | TERRA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 3c3deced-0434-3509-8624-0f7eede823d9 | -3.86379 | -44.53415 | 2025-10-26 11:57:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4ba51d7d-95c4-34ea-8afe-5a1f4565b50e | -3.75982 | -47.56862 | 2025-10-26 11:57:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 168be8dc-9c21-3f11-931d-752705fd67fb | -4.9009 | -43.24808 | 2025-10-26 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ce7d154b-3fe6-3992-9613-701d6ddb8ce1 | -3.51144 | -41.61185 | 2025-10-26 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 05993da5-1570-3bd8-8206-7c84b15f69c3 | -3.91468 | -43.9962 | 2025-10-26 11:57:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0c223e93-b904-3c4c-a099-2f88462305b4 | -4.63853 | -42.50898 | 2025-10-26 11:57:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 5c56f7e9-df04-3bc0-9ac6-4e0cfdf67808 | -4.89461 | -43.22888 | 2025-10-26 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| b51dbf4c-8064-3c05-9670-ea5875d14f6b | -5.54951 | -41.23492 | 2025-10-26 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 86074495-895f-33b5-b119-06fc1cde0521 | -3.23428 | -40.71691 | 2025-10-26 11:57:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 95a77903-6a23-30c7-9d8d-53b314048904 | -2.85076 | -42.93588 | 2025-10-26 11:57:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 30a742a2-b7e1-3f00-aeeb-1da183e3ecb7 | -5.25141 | -44.01129 | 2025-10-26 11:57:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 28c1e88d-9cbc-3199-8ecc-7ace79c4d4b1 | -5.59293 | -41.32178 | 2025-10-26 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 16e407e0-7ce2-39df-95b5-a359189b5f54 | -3.03953 | -42.59264 | 2025-10-26 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6f0601b9-7473-3ccb-ae0b-6922d7f08470 | -6.17392 | -41.5783 | 2025-10-26 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| a1c44ac1-370e-3183-b614-b8b43eaff7c3 | -5.54413 | -41.40187 | 2025-10-26 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 1d5a00c7-4075-370b-94e5-e4039c4dc15f | -6.0097 | -43.87512 | 2025-10-26 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f4949633-8897-3724-8e5c-f46b27b905f4 | -3.91559 | -40.5314 | 2025-10-26 11:57:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 36cbe689-25c4-3e97-b20b-02e23a4998a5 | -2.88679 | -44.27528 | 2025-10-26 11:57:00 | TERRA_M-M | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 30b28be8-8698-3044-a10b-96c577d7389a | -5.2605 | -44.01258 | 2025-10-26 11:57:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1d6c6105-353d-3489-9100-7913373d09f8 | -4.26828 | -43.91901 | 2025-10-26 11:57:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a6af878c-686e-3db1-8644-f5204611ffdf | -3.53181 | -42.05005 | 2025-10-26 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 44.7 |
| 662502a7-979f-3967-96a3-2e6fbfab064b | -3.84126 | -44.31907 | 2025-10-26 11:57:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| df4d59b2-6b1e-3940-b7dc-647da3ef6866 | -3.00427 | -41.68039 | 2025-10-26 11:57:00 | TERRA_M-M | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 5d80b77a-44f5-353a-95bd-b73a29c0db6f | -3.18972 | -41.42236 | 2025-10-26 11:57:00 | TERRA_M-M | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 6839cb52-9e7b-3124-9363-aacf1591bec1 | -5.84559 | -43.924 | 2025-10-26 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bb38bb66-39dc-313a-aa6a-a5fa2afdf9d4 | -6.07926 | -38.46282 | 2025-10-26 11:57:00 | TERRA_M-M | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 55.6 |
| 974e8e00-0c77-307e-9dc2-fd67bf7b5536 | -5.25913 | -44.02198 | 2025-10-26 11:57:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 17806b9a-2d70-3eda-85e9-c78c233168e8 | -3.36138 | -41.51268 | 2025-10-26 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 28ce6966-5703-3da0-a173-ac634cb5e2ae | -2.8853 | -44.2854 | 2025-10-26 11:57:00 | TERRA_M-M | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2289dce8-65fa-339a-ab20-3eb79f334096 | -5.10188 | -43.19753 | 2025-10-26 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 0bded393-5023-348e-a47c-1748c48e562d | -6.2601 | -41.82308 | 2025-10-26 11:57:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| ff535802-0058-3c3e-86b7-90cf37f244e3 | -6.14054 | -41.8125 | 2025-10-26 11:57:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 1d9cfeed-4494-3853-bfb1-c4f8922ed193 | -5.55438 | -41.39397 | 2025-10-26 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| a08121ce-408d-343e-b949-16499e91555f | -3.70927 | -43.19211 | 2025-10-26 11:57:00 | TERRA_M-M | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| caa79c0b-f832-39fb-86d1-26e0970d24c6 | -3.234 | -41.94553 | 2025-10-26 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 138e59fb-f790-32ae-b047-56a778d328cc | -3.16223 | -42.25707 | 2025-10-26 11:57:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 445c9d33-60e9-3e06-b4fc-e81097c472d8 | -5.11205 | -43.18985 | 2025-10-26 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 43fb3bc4-72c8-3870-a964-d71ee1e331db | -6.02687 | -43.30864 | 2025-10-26 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 85f2e9d4-217c-399e-8160-29d4e104805a | -3.98884 | -45.48954 | 2025-10-26 11:57:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 17d1ff6b-316a-3f7c-9837-3f754662e7d8 | -3.85062 | -44.3204 | 2025-10-26 11:57:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8db37c0b-ffd1-3628-bfd1-400456ef1828 | -5.00679 | -37.83935 | 2025-10-26 11:57:00 | TERRA_M-M | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 1037226e-667a-3971-9233-4e543ea47749 | -3.2428 | -41.94675 | 2025-10-26 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 156fed29-6b04-3d06-afb5-aa0970a71e6b | -3.04838 | -42.59386 | 2025-10-26 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e3204d86-fcfc-3c14-a54c-0e298cf1c5ae | -6.06576 | -42.14673 | 2025-10-26 11:57:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 7ec36faf-73c9-3d4b-93ce-451038977321 | -4.83118 | -45.34276 | 2025-10-26 11:57:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 9a85a095-58ed-3e2d-8940-065cfae274bb | -3.40894 | -44.29402 | 2025-10-26 11:57:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d3d2db54-8662-3c3e-9f51-568c57c44b0c | -4.27094 | -40.69162 | 2025-10-26 11:57:00 | TERRA_M-M | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 08c9be08-2556-3e19-98fc-b189e9638390 | -3.83982 | -44.32904 | 2025-10-26 11:57:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a2c6d2e0-63ca-3b04-9cde-53b054059241 | -5.25003 | -44.0207 | 2025-10-26 11:57:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 9e8cccc2-5c01-3ffb-8c7b-1fe795cf9344 | -3.69106 | -38.93267 | 2025-10-26 11:57:00 | TERRA_M-M | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 5f6a613b-29cc-3e61-9a88-ab0496df4d11 | -6.26136 | -41.8141 | 2025-10-26 11:57:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| ff847d17-d145-3391-904d-8d9c816b2c42 | -5.54542 | -41.39279 | 2025-10-26 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 1f6f24f2-9c4c-3a9e-9445-20884519373b | -6.22843 | -42.55041 | 2025-10-26 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 983183c6-7c36-38fd-ae94-fa9f00bb28c9 | -3.42455 | -41.3231 | 2025-10-26 11:57:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 65.7 |
| ff90058e-640a-347b-a635-31b186f9ebb3 | -6.07428 | -38.45517 | 2025-10-26 11:57:00 | TERRA_M-M | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 6fc6b3ab-aeec-3342-ad0f-c069cc269a09 | -2.85205 | -42.92688 | 2025-10-26 11:57:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0481e72c-53b7-3709-ae04-fdbeb6c8956c | -3.78897 | -43.40501 | 2025-10-26 11:57:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7b75328b-0038-33ac-b878-9eb94848aa41 | -6.1743 | -42.61459 | 2025-10-26 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 6fba5ab0-ef3d-34bd-b618-47beb61d0182 | -2.88144 | -40.02251 | 2025-10-26 11:57:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 573ebc39-cdd7-3cbb-acf8-b8a301d3bc77 | -3.01182 | -41.69037 | 2025-10-26 11:57:00 | TERRA_M-M | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9df8c96b-74eb-3632-a9d3-22a303538f57 | -4.89201 | -43.24682 | 2025-10-26 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| eee2f470-11b0-3905-b57b-0b30b5c0146e | -5.66062 | -42.58593 | 2025-10-26 11:57:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 30fe4470-4f8e-36a2-bf7b-36d8842b8e7a | -3.65452 | -41.25858 | 2025-10-26 11:57:00 | TERRA_M-M | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ac0e0880-c88f-3ac0-b171-53fb4ed6e2a5 | -3.04081 | -42.58379 | 2025-10-26 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8cdb5369-c20c-31d6-84b0-ad5dfcb4c624 | -3.36667 | -39.71634 | 2025-10-26 11:57:00 | TERRA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 6dbe9527-1884-39af-9769-acf770532fe8 | -3.42325 | -41.33215 | 2025-10-26 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 768bb0f8-b7c5-357c-8eed-341e3f281112 | -13.547 | -49.5434 | 2025-10-26 12:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 410f8e32-4a3e-3f93-b404-cc4b9a6c6a89 | -14.6313 | -48.389 | 2025-10-26 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 6027b14e-5456-3318-8be8-5856b737ce2f | -6.31307 | -42.808 | 2025-10-26 12:00:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 8d6da0d1-9b1b-397f-9bfa-c4b8c39347ea | -6.83195 | -41.55493 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 900912b3-8c9b-3b1f-8de1-0153ef269cc6 | -6.45305 | -42.33379 | 2025-10-26 12:00:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 5c21c1eb-cef6-3ba9-a1ba-089d7d0ac06d | -15.72117 | -44.03556 | 2025-10-26 12:00:00 | TERRA_M-T | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README55.md)
