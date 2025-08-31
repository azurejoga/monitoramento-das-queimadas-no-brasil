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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37a1812b-65d7-307a-9746-77b10c2380d3 | -6.5021 | -43.5553 | 2025-08-31 13:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 284a2ca1-2ec0-3cf6-a238-2e838242583a | -8.294 | -46.3099 | 2025-08-31 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 819e7418-2ae8-30b5-8b8a-8fe58129fca8 | -7.8543 | -46.9525 | 2025-08-31 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 329.5 |
| e8fc4651-7e96-3556-b177-20320e19c28b | -12.6302 | -48.1757 | 2025-08-31 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 5db7c25d-a47c-334a-8777-3e1ceef07ad4 | -13.3439 | -46.9757 | 2025-08-31 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| c4d0fd88-2b5a-3c83-99b8-725ec1d2aeaa | -7.8543 | -46.9525 | 2025-08-31 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| e99fb881-ce21-36b8-a1eb-3dc6e25d28ff | -14.8013 | -46.7371 | 2025-08-31 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 1e50f918-4a96-342a-bc24-8ed78210daa3 | -12.3287 | -45.7201 | 2025-08-31 13:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 3a6dada1-4df8-35c5-bb39-d77babdec2bc | -12.6486 | -48.2175 | 2025-08-31 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 38a536fa-5ada-341e-89fe-2a5a6df8e545 | -14.0313 | -44.5578 | 2025-08-31 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 0dd59fa0-d67a-33da-8322-8e5e726871b9 | -4.7346 | -44.4457 | 2025-08-31 13:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 248.7 |
| dc662755-3a12-3a7c-9afa-ebda1f558083 | -5.8884 | -42.9753 | 2025-08-31 13:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| c0ef3a27-07f9-3f2b-8921-aab872da660d | -7.8541 | -46.9747 | 2025-08-31 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 312.9 |
| 3b861fa1-8c8b-3beb-8e36-5104edd29978 | -12.649 | -48.1953 | 2025-08-31 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e9abccf6-2168-3007-85a3-a03ff3e6cf14 | -11.8181 | -46.4314 | 2025-08-31 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8ca46d4b-6d3f-3a74-9706-a89d548be373 | -15.7107 | -48.9255 | 2025-08-31 13:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 6120dc00-4cf6-3dda-8549-17c2de18cb87 | -7.2275 | -44.2315 | 2025-08-31 13:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 8d54e8a0-2f59-3a0c-b82b-d8911fb57021 | -6.2411 | -43.3677 | 2025-08-31 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5859a1da-6f00-3f32-ad1d-1fb31612f8e8 | -15.7102 | -48.9479 | 2025-08-31 13:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7bee96a3-790a-3754-aed9-5a6bab67226c | -6.5209 | -43.5537 | 2025-08-31 13:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| f0e432ce-ff88-36f1-ad7f-4d85e450dfa7 | -7.4466 | -44.8079 | 2025-08-31 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.7 |
| e7fac8a0-6701-3d5e-949b-58044ba9e3e5 | -16.2221 | -52.6778 | 2025-08-31 13:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 68e467be-84eb-3495-83a2-1a1dbf9c5dee | -9.245 | -47.0824 | 2025-08-31 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e3afd819-5c49-317b-8364-527da7336acc | -13.3636 | -46.95 | 2025-08-31 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| cad0c0ab-7bd3-3fcf-83a6-883ad8825a93 | -6.2409 | -43.3911 | 2025-08-31 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 1cacb282-1b08-3d06-b553-e7d00d233285 | -7.0951 | -44.3128 | 2025-08-31 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| cc3406c7-6ace-3843-9eb4-c735d76833e7 | -12.3095 | -45.723 | 2025-08-31 13:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5f7522db-987b-3107-af56-1769fd3a7c95 | -14.0508 | -44.5543 | 2025-08-31 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 7e5de89a-2bc9-3086-be51-d6af862c02c5 | -11.8357 | -46.5194 | 2025-08-31 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| a35dc999-ec6b-3664-8188-eb53fce1d4ad | -7.2142 | -45.443 | 2025-08-31 13:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 5c3c1370-0cd8-3b17-b79c-33f9fad572fc | -14.8208 | -46.7337 | 2025-08-31 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 6b835e52-a736-35a3-88d8-bb84aabaa97e | -6.5021 | -43.5553 | 2025-08-31 13:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 9532b156-f509-3bdc-a3f3-7fa6b8e19da6 | -15.7098 | -48.9702 | 2025-08-31 13:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 96cea5ac-7946-3420-a873-5f7cad888e36 | -16.2217 | -52.6992 | 2025-08-31 13:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| abae1d65-04ca-3de4-8af6-93bcef8cbbcb | -8.294 | -46.3099 | 2025-08-31 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 715d3f5d-0e61-3fe3-b67a-15ce33720035 | -11.8361 | -46.4967 | 2025-08-31 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 84ba0b2e-6a74-34ad-b482-75a584752452 | -14.0307 | -44.5814 | 2025-08-31 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 0c5a6d8c-8d20-3568-8ca6-e7e546072860 | -5.4824 | -44.3969 | 2025-08-31 13:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 0e733c19-698c-382e-b7ce-42e584cca9b7 | -5.8696 | -42.9768 | 2025-08-31 13:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 158.1 |
| 7292268b-e70a-32d7-9355-2f4933a1ebb7 | -7.1139 | -44.3111 | 2025-08-31 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| f45c2503-ef8f-3e78-8a18-a5d6c2bfd1bc | -11.0849 | -44.611 | 2025-08-31 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9480dace-b559-370b-b114-7c1e4e437de6 | -11.9143 | -46.3953 | 2025-08-31 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| f4227b8b-e1b8-3217-bda7-019392ba7494 | -13.3443 | -46.953 | 2025-08-31 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 19e09e48-21b2-3a72-98a0-47d6bded6c87 | -12.6298 | -48.1979 | 2025-08-31 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 924.9 |
| 22df1477-1731-3d81-8129-b626a14ccfbd | -11.0658 | -44.6137 | 2025-08-31 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| b90417fe-ed40-3bc0-8837-92dad0d627c6 | -16.2417 | -52.675 | 2025-08-31 13:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 151813b6-c15d-3a06-a8be-1531166daab0 | -10.0434 | -48.0998 | 2025-08-31 13:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 99bb121c-ed69-35c6-b1cc-02fbc7a09690 | -11.8357 | -46.5194 | 2025-08-31 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7580f18a-579a-39af-8948-01a2dc85b0e0 | -7.5002 | -45.0538 | 2025-08-31 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 5ed07663-d078-3a68-abac-0d1ba2805d37 | -11.0654 | -44.637 | 2025-08-31 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| db532ce8-0847-39d9-810f-7dc83e2e3369 | -7.8543 | -46.9525 | 2025-08-31 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 03bc6941-b940-3ca4-97cc-2e5b673299aa | -9.2453 | -47.0602 | 2025-08-31 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| dddbb90c-f7f9-3008-bea6-56a4dee7400e | -15.7107 | -48.9255 | 2025-08-31 13:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| aebc061c-f246-337d-ac7b-f98424682633 | -5.4824 | -44.3969 | 2025-08-31 13:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 181.0 |
| cd40e809-588a-3f56-a950-7135e44634f3 | -11.0845 | -44.6343 | 2025-08-31 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| a6a97944-a87c-3c6e-a418-ea8633c37ee1 | -14.8208 | -46.7337 | 2025-08-31 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 985afcab-8700-3cf5-b968-e022d74e2759 | -15.7098 | -48.9702 | 2025-08-31 13:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 146.7 |
| d47bbcd3-ea7c-3929-8070-adc7985a1582 | -11.0849 | -44.611 | 2025-08-31 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 182c3c16-3297-371b-9e0d-0cc52e13077b | -7.8541 | -46.9747 | 2025-08-31 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 391.5 |
| 21d0acd5-f7fe-372f-8147-858a53395e6f | -14.0313 | -44.5578 | 2025-08-31 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 2218616a-c49e-34ae-89a4-9bd4520550c7 | -12.3099 | -45.7 | 2025-08-31 13:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 1b81ba86-2818-3ccf-9921-14a3d014d726 | -8.875 | -45.0961 | 2025-08-31 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 43928113-6388-3e25-ba98-0e5d9323d7bc | -14.0508 | -44.5543 | 2025-08-31 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 170d6220-0e6c-373f-b7e1-0767ded6a0d5 | -15.7102 | -48.9479 | 2025-08-31 13:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| cc94d1d2-e68d-3540-af29-a9fb7e3e9ca3 | -12.6486 | -48.2175 | 2025-08-31 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| f139cc27-17cf-3e1f-b54e-3042e15c4de4 | -5.7696 | -43.6613 | 2025-08-31 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3fae7241-b14f-3f77-8be9-4951a5aef284 | -14.8013 | -46.7371 | 2025-08-31 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 9290236e-5b2f-3df7-ac13-3f03f25cafdb | -13.3439 | -46.9757 | 2025-08-31 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 536cd682-5cf9-3e64-8c18-0d6a414aae7c | -17.1536 | -46.0817 | 2025-08-31 13:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f0e5e42f-d567-3bd1-ac24-a682a6eb13f4 | -6.5021 | -43.5553 | 2025-08-31 13:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 559c3b53-9e20-3f68-8a2b-cdc668e2e0b2 | -5.8696 | -42.9768 | 2025-08-31 13:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| b944d8c3-d560-38c7-bd86-82efd3318147 | -14.0307 | -44.5814 | 2025-08-31 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 232.4 |
| 8d2cd154-ec45-3aa8-8830-63d5326b030d | -12.6294 | -48.2201 | 2025-08-31 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1226.7 |
| 4e2d7b3f-a45b-3342-9430-254c298cfcf6 | -7.0951 | -44.3128 | 2025-08-31 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 857c3972-4e99-3dc1-9cb1-74e253b1f8de | -7.1139 | -44.3111 | 2025-08-31 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 7a48f7fd-3ce5-311d-ac43-6735c5a48cb8 | -13.3443 | -46.953 | 2025-08-31 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 1f0c0862-b88e-3260-b7bc-d703afbe240c | -12.6298 | -48.1979 | 2025-08-31 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 623.4 |
| 570161a6-1c38-3d07-8583-f45e5c02ef60 | -11.8181 | -46.4314 | 2025-08-31 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b07edd00-175c-3ce9-a12d-51526d91d00c | -14.3532 | -51.9132 | 2025-08-31 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| f4d266cb-aea8-3e1e-944c-19cfa325509e | -6.2597 | -43.3895 | 2025-08-31 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 276e00bf-f162-3f43-9088-30fdc37386ad | -9.245 | -47.0824 | 2025-08-31 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 145.7 |
| f229484e-88bc-3a31-be12-7f42a7cb7cc6 | -16.2221 | -52.6778 | 2025-08-31 13:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 7c30ee9c-6a5f-3eef-8bea-d5559a0c06b2 | -5.7694 | -43.6845 | 2025-08-31 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| a6f88df8-7fbe-3c02-bd1e-e5982d05697b | -11.9143 | -46.3953 | 2025-08-31 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 18f71261-d56e-3709-9f86-b8199a622be7 | -6.5758 | -43.6885 | 2025-08-31 13:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 86263a5e-7df0-3f0b-b389-547aaaec6226 | -6.5209 | -43.5537 | 2025-08-31 13:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 2410ea04-fd89-3796-89c9-6430805a2b03 | -5.6573 | -43.6465 | 2025-08-31 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 706d5458-0456-3e9e-80e6-2443ffeff0ef | -6.2411 | -43.3677 | 2025-08-31 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 9f48356e-44e4-3c96-ab52-7554541be38e | -6.2409 | -43.3911 | 2025-08-31 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 29d1cb54-fa38-3e15-aa93-69d3b3c9a4d0 | -12.3287 | -45.7201 | 2025-08-31 13:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 40b64478-2324-32ec-bbb0-72a599aa211c | -13.3636 | -46.95 | 2025-08-31 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 7af92554-16b0-38fa-81ff-d9c7a6fd63f9 | -6.5209 | -43.5537 | 2025-08-31 13:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 0d6f4352-c018-33f9-a162-84ff9ac6e706 | -9.4433 | -60.5499 | 2025-08-31 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b7f8b64a-cf2d-3c86-adba-58f4a8e6a62a | -9.2453 | -47.0602 | 2025-08-31 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 2dfbe5da-66e5-3f20-a77c-ed1519f27779 | -14.3346 | -51.873 | 2025-08-31 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 60feda05-7a0d-3350-95ac-efa49c79eece | -11.0654 | -44.637 | 2025-08-31 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 39f5cbdd-f2f4-3ea0-88bd-d62a58a33b69 | -9.4432 | -60.5692 | 2025-08-31 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 04ceacf8-2993-365b-be42-ab34e742e596 | -14.3536 | -51.8918 | 2025-08-31 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 691782f3-a97c-34ad-ad44-8b1f39d6f480 | -6.2956 | -43.5496 | 2025-08-31 13:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d464fb5c-fca1-37c3-8208-be6653ccecaf | -15.7107 | -48.9255 | 2025-08-31 13:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |


[Clique aqui para ver as próximas entradas](README90.md)
