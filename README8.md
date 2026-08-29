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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c3d2c8b-e930-3b40-b6cf-a30e2d30fbcf | -4.3588 | -47.7636 | 2026-08-29 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 236a66a8-f9de-332d-9c09-6ed183b8165f | -10.8805 | -46.6241 | 2026-08-29 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 09e1e35f-ce89-38d1-a6f9-aa2cce9be594 | -10.4981 | -64.5005 | 2026-08-29 00:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7a1a54e6-69e4-3f54-9406-6dcd14b61c3e | -10.4794 | -64.5012 | 2026-08-29 00:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 5afadbbe-bccb-33b1-8cbd-3cd1ab779b23 | -11.0443 | -57.2222 | 2026-08-29 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 1dbf86c4-3629-3a30-8b52-f5f46a942701 | -5.9079 | -57.7506 | 2026-08-29 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b2b66952-d960-3860-878c-e053e9076233 | -5.8895 | -57.7513 | 2026-08-29 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 225.2 |
| 086adb8d-a6e4-3c2e-ab22-52ef571a4262 | -4.3587 | -47.7853 | 2026-08-29 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2594ecc0-7736-360e-a9ee-b80411d623e3 | -5.871 | -57.7715 | 2026-08-29 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 23591067-5b34-35e9-a5ec-a075782cf4ae | -11.0254 | -57.2237 | 2026-08-29 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 1d2dae8b-12d3-3ee6-a727-4663f48cb39a | -5.8894 | -57.7708 | 2026-08-29 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 218ef71a-440d-3ad9-ad5d-8d53007f1ab8 | -8.9613 | -63.279 | 2026-08-29 00:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| bea04e4e-82b3-35d8-9da7-ace7e0107b89 | -4.3774 | -47.7627 | 2026-08-29 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 1f423b5f-bc34-36bd-87cb-c5644ea66c4d | -6.7514 | -55.6654 | 2026-08-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 49fe7941-81d4-3dbd-b588-88c1e39ba56c | -6.7343 | -55.4671 | 2026-08-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| ecbbb0e8-0da2-34ba-b791-a43cb32dece9 | -6.7341 | -55.487 | 2026-08-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e8c56841-4815-38fe-b91c-50aa66ae4b27 | -5.4177 | -43.1986 | 2026-08-29 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 2a54404e-012d-3a00-8fbe-9092dbe3a26a | -6.6127 | -43.7549 | 2026-08-29 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 9f7f6e27-2e5d-303d-811f-c1b653af88fa | -11.0441 | -57.2421 | 2026-08-29 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| d44c255c-89b4-3ad1-9746-36d2e3acb73f | -12.43 | -43.4182 | 2026-08-29 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 62f4c16e-f635-3cdb-9029-7868f4eea2dc | -6.6129 | -43.7317 | 2026-08-29 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| be0aea62-c84f-3a3d-b605-8642dd3d261b | -11.2565 | -54.025002 | 2026-08-29 00:52:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 991460d2-1690-32d6-879f-17fe3f927525 | -6.7492 | -58.715801 | 2026-08-29 00:52:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9f1f5bc-a3ff-3596-bf5a-75315ad27fb7 | -13.4585 | -57.038399 | 2026-08-29 00:52:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82dd4209-e443-3ebc-9932-3a2adad605c3 | -14.8897 | -52.6199 | 2026-08-29 00:52:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7296d254-b962-3417-8dc5-9767d196fda1 | -13.4799 | -57.041302 | 2026-08-29 00:52:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f986787f-38d2-3aa1-8336-1ec50f3e394a | -6.9618 | -55.6875 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e71cbc61-0bcd-3aff-8f02-0cfe06f96bdc | -8.5996 | -54.772999 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1b56e2e-00bb-3da8-9ae5-aa85c336bb3d | -9.2214 | -59.754601 | 2026-08-29 00:52:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 978df95b-b4d7-3d0f-95d2-60fea9f0df76 | -5.8825 | -57.771801 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8cdc06c-a3df-3c28-b120-f20b06a700ef | -17.587099 | -51.608898 | 2026-08-29 00:52:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 61888472-f6d0-3954-a7f2-7b5a8ff5c179 | -14.742 | -57.645699 | 2026-08-29 00:52:00 | METOP-B | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a6c519e-cd8b-3f86-be64-42227ba267dc | -9.5141 | -65.553703 | 2026-08-29 00:52:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fd5d9e10-e431-3f99-b424-2e6f78f274d2 | -8.9643 | -50.778999 | 2026-08-29 00:52:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebe9b7ee-fffd-3b41-a97a-0525e423dc2e | -11.0434 | -57.2131 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 490e3d53-8886-3723-907f-990fd727a891 | -6.5918 | -59.108898 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 660f77f2-8de0-3295-b696-6a60222c9df2 | -6.8454 | -59.453201 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d08edf2e-ffbe-31ae-9e1c-92b0bb162a53 | -19.4725 | -57.566502 | 2026-08-29 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 30939ac4-c560-306f-a192-bdf4e13e3626 | -11.2538 | -54.013802 | 2026-08-29 00:52:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e992a0c-0c49-34a2-b011-ded0194848d4 | -6.7902 | -59.391899 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2cfc35e-c239-38c4-9c0a-3324497e5e74 | -11.0451 | -57.220798 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01b86b7f-7ec0-38e2-a2a1-01ce5656a74a | -11.1947 | -55.0947 | 2026-08-29 00:52:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd83f1b-2696-39cc-997a-e037b012ce86 | -6.7238 | -60.006802 | 2026-08-29 00:52:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb8ef507-5115-3525-ba7d-1b72b9d9fb19 | -20.9459 | -57.579498 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3b71e6f3-b900-39b3-af9b-2968bca9c5c6 | -10.4978 | -64.498398 | 2026-08-29 00:52:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f64a0bb0-20ca-34cc-8881-f2dc74da42e1 | -20.942801 | -57.5648 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0ecd8589-a57f-3fe5-abfb-b7d2d8c6972a | 4.5463 | -60.720699 | 2026-08-29 00:52:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bc125728-f105-31a2-a6ce-4f0bdc8af111 | -10.5588 | -59.611198 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03bad8ad-6821-3662-9d80-a976b528305c | -14.9133 | -56.3223 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b5a9e854-754e-393e-b4c6-366a2a544080 | -14.1931 | -52.855 | 2026-08-29 00:52:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2225f7df-de2b-33d2-acd6-9fe1ed4b33b2 | -11.0398 | -57.197701 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f8119ef-0adf-32e0-9bf2-7b8a4b78d982 | -6.9546 | -59.48 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 725a87d2-3aff-385a-b91e-28978b7ad9e6 | -9.278 | -57.074799 | 2026-08-29 00:52:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc3a0ddb-ddd2-3b9d-8233-0440af98e5b7 | -14.274 | -57.040199 | 2026-08-29 00:52:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90b13a12-a357-3547-a7ac-eb2d7b8aabb3 | -13.4683 | -57.036098 | 2026-08-29 00:52:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e9b4178-a6ee-36f1-97ad-8ce17d83ec72 | -7.5989 | -61.3363 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0c3c99e-8014-3676-8130-8ee50e51b29a | -14.9505 | -56.304901 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cea46a2f-4514-3aaa-8adb-07d94faf0cc9 | -9.9547 | -53.9356 | 2026-08-29 00:52:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce006623-1363-3bca-8b51-b83e7fda64b4 | -6.2583 | -55.413799 | 2026-08-29 00:52:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4750018e-d3b8-3185-b009-a71ab32a4ff9 | -11.0309 | -57.248501 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9abe5f5c-47b9-3ab4-aa2a-b889cfcd9b6d | -9.0139 | -57.536098 | 2026-08-29 00:52:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70c2f59f-7559-33c0-b6ac-3a5a7b39c056 | -10.755 | -54.0429 | 2026-08-29 00:52:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2edc6c5f-94ee-3314-aead-99e0d4aad619 | -7.602 | -61.350399 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4209868-c772-373c-9a26-29cb597bcb81 | -3.6078 | -60.532101 | 2026-08-29 00:52:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d20d911-64d1-31f7-baad-6bafc146ed47 | -6.7374 | -55.479698 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e7d8cec-e487-3eb5-8a36-f7ea5f81d0bd | -4.5342 | -54.9119 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47834ad4-430c-3352-9027-bc9dace6230b | -7.5586 | -61.293598 | 2026-08-29 00:52:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06979760-beb9-338e-8f33-d42173c9e5e3 | -7.5676 | -61.1959 | 2026-08-29 00:52:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0ce0763-8e6b-3d9c-9048-35ac6eb0d91d | -6.8504 | -59.429901 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b09bff7-76bb-3efc-ba87-18f377d20477 | 3.2853 | -60.6082 | 2026-08-29 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| be6592f3-7867-327c-aab2-ee380dd7dc3e | -6.8628 | -59.0322 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 966832bc-944c-3bb1-9c31-4b202e978d97 | -6.9122 | -59.474899 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ddb1e0e4-d090-3ef5-889d-26b1fa525dab | -11.2164 | -53.987499 | 2026-08-29 00:52:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecba4403-1633-3ae8-b473-83eb6321a09a | -13.165 | -55.648602 | 2026-08-29 00:52:00 | METOP-B | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91e7326d-6131-3a31-ba09-7fdb021294b4 | -3.2097 | -61.1394 | 2026-08-29 00:52:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16b6f882-c724-309a-b443-a64028522631 | -14.3878 | -50.055302 | 2026-08-29 00:52:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 46e147da-1cf8-38a7-80a7-28972e0b3b8c | -6.8403 | -59.929798 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ec8948e-1474-3e08-82d7-053a4158ad50 | -20.9217 | -57.562199 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a5c95d7f-dc4b-3c78-a11d-4dcf374cc11f | -19.065001 | -57.3978 | 2026-08-29 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| abba1199-ade6-393d-b3fb-946cb12ad674 | 0.9143 | -59.620399 | 2026-08-29 00:52:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1defb0d6-85e2-3399-9ea6-e1254fb8a824 | -11.718 | -54.522301 | 2026-08-29 00:52:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea541163-ec9c-31ca-a366-fa808be87e56 | -14.8867 | -52.6078 | 2026-08-29 00:52:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5512838b-6971-388f-9d82-3206b44127d8 | -7.5875 | -61.331501 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6153a113-81b7-345e-9cb7-8289f87f4fd2 | -4.0554 | -56.292 | 2026-08-29 00:52:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b71dcd1-aa4e-3505-ad9a-b489050cb65a | -10.2946 | -62.813499 | 2026-08-29 00:52:00 | METOP-B | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d177564-49d9-31d8-80d1-54425a4d509c | -9.8768 | -60.291199 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dcdd54ce-0c48-3fc2-8e93-536f874275fe | -17.629101 | -51.610901 | 2026-08-29 00:52:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 12e5e576-18ee-3e29-b522-d0c50f3a9950 | -5.9849 | -57.680099 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 156111b6-dbde-3374-84fd-0fe0e978f56a | -10.4053 | -61.193501 | 2026-08-29 00:52:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0dd1135-545d-3c5a-9985-6df23586d322 | -7.2877 | -49.550098 | 2026-08-29 00:52:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1e3f9a8-9452-30c3-b266-23665d7aced0 | -9.418 | -51.6805 | 2026-08-29 00:52:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74786635-6f5b-371f-ab54-de2e6e35ee46 | -14.9346 | -56.325298 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5aefa93-43cb-38a9-a7f9-352811976499 | -9.1836 | -59.632198 | 2026-08-29 00:52:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e36c5e40-f19a-33ad-a1cf-aa356d4be6a0 | -15.1171 | -53.580299 | 2026-08-29 00:52:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d0f402e3-aa9d-3636-98bb-4d64693b9669 | -6.9363 | -58.947601 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1fc6834a-159b-3b72-9b05-48fe22886d45 | -7.4984 | -55.298599 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54a3b36e-0f1f-3039-b55e-7f702eba3991 | -19.0634 | -57.390598 | 2026-08-29 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7d47acbf-1a7a-3068-941f-7c5977896c5e | -7.586 | -61.324402 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7fa18dd2-0c6b-34ae-9b30-d73f2c712f0e | -5.9732 | -57.674198 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f29138b-43cc-3abb-be71-91d84b4094cb | -19.223101 | -57.649502 | 2026-08-29 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README9.md)
