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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09189a6a-cc1b-31d9-8a02-30f4bd7475d5 | -5.6014 | -47.951599 | 2024-10-04 00:44:46 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 947a6184-75be-3eda-a631-e59a929a1b7c | -5.603 | -47.9585 | 2024-10-04 00:44:46 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3d66238-9a96-3545-8a46-989b22d20ab9 | -5.5916 | -47.9538 | 2024-10-04 00:44:46 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 082f023e-467b-3677-9ef9-33e0c56b15ec | -5.5932 | -47.960701 | 2024-10-04 00:44:46 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| deb7841f-ffa5-3c25-a173-7759ae503bc9 | -5.002 | -45.489899 | 2024-10-04 00:44:46 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c48923d-2bfa-338e-be4e-c70aa618c098 | -4.9548 | -45.5089 | 2024-10-04 00:44:47 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cbbbd9c4-e0d0-3973-b276-d7d7e5c2b403 | -5.1006 | -46.1357 | 2024-10-04 00:44:47 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e925398e-eb2a-321d-88e5-3ee8402423fc | -5.1023 | -46.143002 | 2024-10-04 00:44:47 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d00d5cc4-32c4-3a7c-9b78-3c9c0acd3c2e | -5.7898 | -49.3237 | 2024-10-04 00:44:48 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 025b08de-9f5a-3358-b98d-49330f4586bc | -5.3074 | -47.253799 | 2024-10-04 00:44:48 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 47ae5fd8-1026-3e02-9fe1-0d91e0ffb7b5 | -5.309 | -47.2607 | 2024-10-04 00:44:48 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 934f8949-6206-30d0-957d-aeeda61491c3 | -5.3105 | -47.267502 | 2024-10-04 00:44:48 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 33250437-cf46-3664-a21b-30b95f86aa4e | -5.3886 | -47.697201 | 2024-10-04 00:44:48 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9674d8b-5eb1-3a1c-beeb-ebde34029d2a | -5.2808 | -47.3176 | 2024-10-04 00:44:49 | METOP-C | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7dd3896-f89e-3a23-bc67-f66850e61fe5 | -5.2824 | -47.324501 | 2024-10-04 00:44:49 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a7eac78-4dac-3a4f-a70f-7cbdf06292b4 | -5.2967 | -48.1063 | 2024-10-04 00:44:51 | METOP-C | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0e21ea9-8500-34d8-bbdd-8d794689e06e | -5.2982 | -48.113201 | 2024-10-04 00:44:51 | METOP-C | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d21ba322-67e9-3c21-9246-b081e1bec8bc | -5.5061 | -48.799198 | 2024-10-04 00:44:51 | METOP-C | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33a5136a-d798-329d-b6c5-f91911b4c647 | -5.5077 | -48.806198 | 2024-10-04 00:44:51 | METOP-C | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 493f89a2-eb47-38f3-bb7c-29e51d098443 | -5.4963 | -48.801399 | 2024-10-04 00:44:51 | METOP-C | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 532f8ee1-0f82-39bd-9cc6-b36d06784a58 | -5.4979 | -48.808399 | 2024-10-04 00:44:51 | METOP-C | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3655d04-4582-39f1-809e-bd8399a21422 | -5.4995 | -48.815399 | 2024-10-04 00:44:51 | METOP-C | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aee7d6ef-8035-3a15-b0a1-a6f7795a2b2c | -5.4807 | -48.9594 | 2024-10-04 00:44:52 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3ed63fb-8c16-31ec-9896-3f620c3d80f3 | -5.4822 | -48.9664 | 2024-10-04 00:44:52 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8fde573-a35c-370f-9a0f-7daefc4b51bb | -4.9209 | -46.7854 | 2024-10-04 00:44:53 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2880b6f-0925-353d-9dfb-1a7ac010f9d1 | -4.6888 | -45.872601 | 2024-10-04 00:44:53 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac18b196-54da-35ee-8e3c-ee60e8a82f71 | -4.6905 | -45.8801 | 2024-10-04 00:44:53 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b254d5d-1ff7-3820-b18c-7da081a5648f | -4.6773 | -45.867298 | 2024-10-04 00:44:53 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa39c663-70e1-3809-a7d9-e53696713019 | -4.679 | -45.874802 | 2024-10-04 00:44:53 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bce30faf-b1f1-32a2-8bd6-27c096d3e150 | -4.6807 | -45.882301 | 2024-10-04 00:44:53 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e77c6cb4-3bab-34a9-9a71-3006c8f2a987 | -4.6825 | -45.889702 | 2024-10-04 00:44:53 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 625f6dcf-a7bb-38fb-a244-0da302ab1306 | -4.6675 | -45.869499 | 2024-10-04 00:44:53 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f3cce269-dedd-3346-81d1-3d5392367ea2 | -4.6692 | -45.876999 | 2024-10-04 00:44:53 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fec01ab6-f853-3b43-b3f8-ce2313afd7a6 | -4.6709 | -45.884499 | 2024-10-04 00:44:53 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a82a6a7f-4c57-3a18-bda0-a57e71bee751 | -4.0288 | -43.2346 | 2024-10-04 00:44:54 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 742b8617-cc9c-3897-95b7-b2f84386294f | -4.019 | -43.236801 | 2024-10-04 00:44:54 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3e4170f-df21-3ac2-97b2-d2881611b20b | -4.5968 | -45.743099 | 2024-10-04 00:44:54 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba36dfb-5ecc-3077-81a8-a5531e4c79d8 | -4.5985 | -45.750702 | 2024-10-04 00:44:54 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8340079a-df53-391c-ae63-417d600a7639 | -4.4073 | -45.372501 | 2024-10-04 00:44:56 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6dedaf9e-c587-3a84-93ca-584fdd15d4ee | -4.4091 | -45.380402 | 2024-10-04 00:44:56 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f041c64d-20d0-3f91-939e-c054588f441b | -4.6858 | -46.749802 | 2024-10-04 00:44:56 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5f164453-6a6b-35f6-84a6-8089a866c551 | -4.6874 | -46.756802 | 2024-10-04 00:44:56 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a7b6e9e6-3af7-3fbd-8db1-d60e4c4e52ba | -3.4118 | -42.281502 | 2024-10-04 00:45:00 | METOP-C | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4b07e53-7f8a-3419-ad79-d23089c7f916 | -3.3992 | -42.271599 | 2024-10-04 00:45:00 | METOP-C | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bca8a349-1619-3117-a023-51333008ccd3 | -3.4021 | -42.283798 | 2024-10-04 00:45:00 | METOP-C | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d698476b-864c-356b-b4ca-04787224669f | -3.4049 | -42.295898 | 2024-10-04 00:45:00 | METOP-C | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c738b13d-3213-36cc-92b4-b8dfa4f25ab8 | -4.6309 | -47.4063 | 2024-10-04 00:45:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 972d69e2-1ce0-30c0-8d46-94e34a1b47ba | -5.0138 | -49.7621 | 2024-10-04 00:45:02 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ded0eaf-f646-3b6a-9531-d91e8ba5cd7c | -5.0154 | -49.769402 | 2024-10-04 00:45:02 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e67a05cc-09b3-3400-b5b0-7e894653c925 | -5.0171 | -49.776699 | 2024-10-04 00:45:02 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e77d8bda-dc48-3e1e-ad16-06dc59043173 | -4.5735 | -48.009701 | 2024-10-04 00:45:03 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45d812bc-ec29-332d-85df-d00354f040e0 | -4.5751 | -48.016499 | 2024-10-04 00:45:03 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6f71c99-a8a7-3384-a60e-1d6e4cd4ac6e | -4.1749 | -46.369099 | 2024-10-04 00:45:03 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4effa3db-7748-3aac-b3b8-fb263570f335 | -4.1765 | -46.376301 | 2024-10-04 00:45:03 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| facaef86-e006-38ff-8d61-fe0664547644 | -3.4233 | -43.3311 | 2024-10-04 00:45:04 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32b3032b-2cd3-3404-a868-ae39f67d2ecd | -3.4258 | -43.341499 | 2024-10-04 00:45:04 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7be812eb-19af-36f6-bb1b-1977f5e800b7 | -3.4282 | -43.351799 | 2024-10-04 00:45:04 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e21a1067-7a62-3236-8cf6-1ec640cbb371 | -4.3379 | -47.298199 | 2024-10-04 00:45:04 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4cb8c80-2154-34dc-9d34-37236f649689 | -3.2611 | -43.123402 | 2024-10-04 00:45:06 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39277f65-5943-3293-acfc-d2519eca8ff3 | -3.2636 | -43.134102 | 2024-10-04 00:45:06 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f59f67d-555f-38ef-837d-be2e6a7a060c | -3.2662 | -43.144798 | 2024-10-04 00:45:06 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6800399-4283-36ec-8252-a39b7567ccb7 | -4.6524 | -49.530602 | 2024-10-04 00:45:07 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b180f45-035e-399e-a84c-0602508fa69d | -3.9217 | -46.434101 | 2024-10-04 00:45:07 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5dd8abda-d9fc-3303-b3b5-8e26e5824d54 | -3.9021 | -46.438499 | 2024-10-04 00:45:08 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ba7a9ba-ec01-3691-b0bc-89ec83a79f02 | -3.9038 | -46.445801 | 2024-10-04 00:45:08 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e930b9e8-9099-3db9-ad80-a38949d34620 | -4.1735 | -47.8839 | 2024-10-04 00:45:09 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a25d79b-322a-3c40-b1e1-7fc2fa693b9e | -4.1751 | -47.8908 | 2024-10-04 00:45:09 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c285d6f-2548-3198-9885-3c557a7b4a34 | -4.4449 | -49.614201 | 2024-10-04 00:45:11 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d192dbbc-595a-32c2-b31d-df39490fe722 | -4.4465 | -49.621399 | 2024-10-04 00:45:11 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3172c668-5008-3dae-a08e-562054c79e71 | -4.6594 | -50.882099 | 2024-10-04 00:45:12 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28f427fa-6d8b-351c-827f-0b67e134de48 | -4.0912 | -48.469601 | 2024-10-04 00:45:12 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 247ca7af-ae6f-3078-9623-4a1e6dda1f76 | -4.0798 | -48.465 | 2024-10-04 00:45:12 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37f9d6bc-4000-3f9c-bec8-67e35fa1cc5d | -4.0814 | -48.471802 | 2024-10-04 00:45:12 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8e1fdb8-c959-30f9-8551-8af8e8f4c3c9 | -4.083 | -48.478699 | 2024-10-04 00:45:12 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bf0e474-c61f-3f0e-b88a-46a932e69ee2 | -4.0845 | -48.4855 | 2024-10-04 00:45:12 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6423502f-b438-342e-a200-ecdec196758c | -4.0861 | -48.492401 | 2024-10-04 00:45:12 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2c8f38a-ed05-3d4c-8ad0-9ab20eadb91d | -4.0716 | -48.473999 | 2024-10-04 00:45:13 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce2ab07a-c545-3acb-898b-88f1b7f684a0 | -4.0732 | -48.4809 | 2024-10-04 00:45:13 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50cca4c6-6837-3256-bbc3-c5e181c34346 | -4.0747 | -48.487701 | 2024-10-04 00:45:13 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a87dc5f3-19f5-367d-81a2-3a65bcdeae9a | -4.0763 | -48.494598 | 2024-10-04 00:45:13 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01317fd2-486e-3403-9a9f-c7d1cfff1146 | -4.372 | -50.428799 | 2024-10-04 00:45:15 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58846c99-db35-38f0-be5f-bd60f650bd5f | -4.0188 | -48.919102 | 2024-10-04 00:45:15 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 125d8134-5355-36b7-aa63-478a9e751534 | -4.0203 | -48.925999 | 2024-10-04 00:45:15 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d84e6c0-f674-3efe-9485-c895d4f30412 | -3.2387 | -46.067902 | 2024-10-04 00:45:17 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bfad1822-3d63-3793-9c70-7225c526839d | -3.2404 | -46.075401 | 2024-10-04 00:45:17 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b35ed30d-a525-33a2-9720-91d429429a96 | -3.2388 | -46.202099 | 2024-10-04 00:45:18 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2563a52f-dd2a-3120-89e7-87e1235f699a | -3.3168 | -46.984798 | 2024-10-04 00:45:19 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66f44aab-acd1-3c0a-97a1-ebee2fcdc5d8 | -3.3184 | -46.991901 | 2024-10-04 00:45:19 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eaf8300-f654-374d-a0e7-44747671304e | -3.307 | -46.987099 | 2024-10-04 00:45:19 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2af03ffb-5ced-32b5-899f-73845be87feb | -3.3086 | -46.994099 | 2024-10-04 00:45:19 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e57c6730-9d6b-3178-979e-d11a38444996 | -3.3135 | -47.015301 | 2024-10-04 00:45:19 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2df368f6-c3fa-31c7-b8b6-b95771771ff3 | -3.3152 | -47.0224 | 2024-10-04 00:45:19 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b267cd5e-3ad4-317f-b7f8-ac7fc7118802 | -4.0326 | -50.384201 | 2024-10-04 00:45:20 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ee487ec-5017-3892-97fe-f241a8ec3e80 | -3.2349 | -50.3695 | 2024-10-04 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b7b47e83-50f7-377d-9c10-b2107ea823f9 | -3.2534 | -50.3689 | 2024-10-04 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 0399fe02-2829-30ae-869b-a6bba2ce78ea | -3.4039 | -42.3094 | 2024-10-04 00:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 48.7 |
| c9a9a8ef-3120-3db5-883c-6ff2928751b9 | -3.404 | -42.2858 | 2024-10-04 00:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 152.3 |
| b3340ae9-dd81-3924-92b2-df90628b54ab | -3.4042 | -42.2621 | 2024-10-04 00:45:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 4648ab9e-c2e0-3f77-821d-0d28c3426171 | -3.2899 | -50.4725 | 2024-10-04 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| f38be64b-3532-33d2-8ef3-4473cca6bcc1 | -3.2899 | -50.4516 | 2024-10-04 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 267.7 |


[Clique aqui para ver as próximas entradas](README18.md)
