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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43712c17-b7e8-36c2-b336-609dd0c0338e | -28.66581 | -50.24945 | 2025-05-14 04:00:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 98e6526d-92fc-3ffb-b624-cd7be4175ff1 | -29.77892 | -51.17379 | 2025-05-14 04:00:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| cb344191-ccb5-3b72-85a8-229bd6a1dca5 | -29.58589 | -51.79208 | 2025-05-14 04:00:00 | NOAA-20 | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8c5ef193-4543-3f0a-a2f7-07344af2b323 | -13.9713 | -56.7874 | 2025-05-14 04:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 1bbb1c7d-1c53-3b2e-a8a5-c557bbf3258a | -15.2755 | -43.0758 | 2025-05-14 04:40:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 9fd699c2-643e-391f-a051-e07455b3fd89 | -6.65478 | -41.99393 | 2025-05-14 04:44:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 19252b61-87a3-30bc-b7cb-e7d698f8ecc2 | -6.91388 | -47.1879 | 2025-05-14 04:44:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fb9f828-3828-35a9-9896-2eb36de78c45 | -6.60574 | -43.88996 | 2025-05-14 04:44:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f98da7f0-9ea7-3f77-8e6f-568f9ac22ad9 | -6.32703 | -43.74521 | 2025-05-14 04:44:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 55ac83a8-9159-35ae-9894-918a481f135d | -6.3365 | -49.56189 | 2025-05-14 04:44:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c9770d2a-a0de-33e5-b718-727db9c2bf27 | -6.34398 | -43.38665 | 2025-05-14 04:44:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e90d8632-4abe-3491-826f-b7073fef929c | -7.41044 | -43.45208 | 2025-05-14 04:44:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77f42457-5ff9-385f-973a-3177cdebe032 | -6.19181 | -48.04032 | 2025-05-14 04:44:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f59c8e6-95ec-3324-97a9-f7992f499f0d | -6.64901 | -41.99657 | 2025-05-14 04:44:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9a6a3115-9f91-381f-a9ad-aa05cb85b051 | -6.19477 | -48.04491 | 2025-05-14 04:44:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 139aae10-1827-3c1d-8824-6b35cf12dae5 | -5.77112 | -43.49433 | 2025-05-14 04:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d562fec-c788-3ea7-a0c4-aec18fcc74ac | -2.7528 | -54.5928 | 2025-05-14 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93a9012a-1da0-3444-8d8c-f5dbbde78e84 | -6.18462 | -48.06413 | 2025-05-14 04:44:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab06d591-23c0-32cc-b290-3bbc0850324d | -7.36045 | -43.74466 | 2025-05-14 04:44:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d42c2cee-ec2f-36de-b555-b309a10edf5e | -5.68896 | -45.19291 | 2025-05-14 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9861210-2ef4-3146-aa68-4633e4daca69 | -6.60108 | -43.88932 | 2025-05-14 04:44:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| add6644d-c88d-3471-aac0-d9fa9ffb1119 | -6.97455 | -42.78825 | 2025-05-14 04:44:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6269056e-9543-3bc8-83a3-855a723d68b5 | -6.65432 | -41.99729 | 2025-05-14 04:44:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| aee8ddfc-2e0c-3ab5-87dc-7860be0b1f7d | -6.51379 | -44.72615 | 2025-05-14 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d1087f9-02e9-30e0-b3a4-39eb46d6b168 | -6.97497 | -42.78523 | 2025-05-14 04:44:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 52d8ea9c-0adf-324c-8e30-afa95321423b | -2.14465 | -53.64785 | 2025-05-14 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8a3f1e7-4b54-344d-8054-73d7afb76157 | -5.78706 | -43.619 | 2025-05-14 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 358a7eec-ccc2-3ae4-95db-9f0f9fd78b2a | -11.55557 | -47.6103 | 2025-05-14 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dec9a02f-a042-3c71-9adf-1c80822730ae | -10.08835 | -46.55096 | 2025-05-14 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8bba1bf-ceef-3f80-b334-77ebb98aacb9 | -14.62743 | -45.1002 | 2025-05-14 04:46:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25b22034-4ea6-3a77-94d8-41fbdc781770 | -10.18345 | -48.0281 | 2025-05-14 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 691693ee-cccc-3d84-9f05-2d4136f743af | -7.72358 | -46.34087 | 2025-05-14 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68910006-080c-3428-ac1a-c5f676bf1811 | -10.48589 | -49.14758 | 2025-05-14 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fa40b6e-29f1-3541-9bb1-6ea58653a04e | -11.7903 | -47.36443 | 2025-05-14 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91e0d42d-874d-30fb-a1cf-13a2169c0072 | -13.39313 | -47.50895 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c929cfb1-8d65-320a-b639-d88248288b69 | -11.79293 | -47.36602 | 2025-05-14 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9a009dee-8808-3b84-a35b-838b36a73a9c | -12.15701 | -48.01103 | 2025-05-14 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1974121f-e965-3f3d-b121-90d4f93f5f17 | -12.15634 | -48.01586 | 2025-05-14 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89ab334c-8caf-3bc0-859a-466b8cd5d9ec | -13.67776 | -53.94955 | 2025-05-14 04:46:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c79520ed-db3a-398f-9b07-5658cfc90820 | -11.80152 | -44.27248 | 2025-05-14 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef097455-9a49-32d6-a331-fc40dc206e3d | -11.62971 | -48.4696 | 2025-05-14 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79e99e84-4f55-389e-bae5-bdac98e2aa05 | -14.63157 | -45.10624 | 2025-05-14 04:46:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a4936a9-a78e-3839-98af-8deca78ee546 | -11.84612 | -57.8529 | 2025-05-14 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b0315f0-25ce-3b03-8443-9bcb06b06a8c | -11.14826 | -48.67776 | 2025-05-14 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6af272e4-fe17-32f5-8365-d9b9f74cda03 | -13.55528 | -52.88098 | 2025-05-14 04:46:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a32f430d-7075-3795-abee-668c58837f7e | -11.63529 | -48.1219 | 2025-05-14 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8f8b7027-0260-3716-91f7-f71c5f9fcc9a | -11.35042 | -55.09142 | 2025-05-14 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aceb8866-629a-3d39-917b-b87bd7d90dcc | -12.72881 | -54.97394 | 2025-05-14 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89e4d82e-a7d3-3349-9b88-54d6a55edb7b | -14.63571 | -45.11228 | 2025-05-14 04:46:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7354988-3c33-3cf3-a5cc-5c22bc925f3a | -14.63638 | -45.10689 | 2025-05-14 04:46:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7336a9a-b7e2-38d6-9d2a-55641b558793 | -8.80577 | -49.81704 | 2025-05-14 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e44f93da-33f0-3012-9a47-7a811830d069 | -13.07059 | -52.02065 | 2025-05-14 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a116ac7-5a99-37c7-96c6-a90f1c08afbb | -7.90003 | -44.48417 | 2025-05-14 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 544d7c1b-f227-3fa0-80ab-9ade22961f6d | -13.08915 | -52.29495 | 2025-05-14 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9f02af6-eb02-3ab4-9503-105624e6c35e | -9.57223 | -49.1082 | 2025-05-14 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98fcd560-5922-3576-9d5a-9de0c14f0118 | -11.40964 | -48.70736 | 2025-05-14 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 965fe180-c59c-3848-a2dc-27b59aaf1761 | -11.91964 | -54.40612 | 2025-05-14 04:46:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ef31714-2cac-3f4e-9b51-edfa3faea6b4 | -10.02722 | -48.69888 | 2025-05-14 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 228c24a6-69a0-3102-9099-12821d57b65e | -12.2894 | -52.47138 | 2025-05-14 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23f5198f-f262-38a6-9a4f-1e9fa07a6cc5 | -7.72405 | -46.33751 | 2025-05-14 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3571548-c6cb-3419-b8a8-bfcced6b21d9 | -11.80311 | -46.6408 | 2025-05-14 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e76846f-ad8b-367f-bee0-e6a19becc786 | -11.79843 | -46.64408 | 2025-05-14 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f4a0dfa-b01e-34aa-8f44-be41820dc4b0 | -12.86986 | -55.06219 | 2025-05-14 04:46:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 979867fc-c827-3a36-bf1d-2de6c62eb644 | -11.80779 | -46.63754 | 2025-05-14 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec49dc13-1561-3945-81c4-e035f6634bd6 | -10.73568 | -59.32023 | 2025-05-14 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b51e2b3d-6804-3139-bb51-c97c559346b1 | -12.86702 | -55.05766 | 2025-05-14 04:46:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3bb19c4-d290-3a5b-940c-20c6bb8b9f47 | -14.63091 | -45.11163 | 2025-05-14 04:46:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80d53804-45f9-3294-abf4-d9108671f5d0 | -11.21544 | -47.26265 | 2025-05-14 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17c87ff8-4126-3d0e-b90d-00c83e1c84af | -12.48564 | -48.9434 | 2025-05-14 04:46:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aed9cbab-236f-36d8-9137-847d563de099 | -10.47169 | -49.60551 | 2025-05-14 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e3318d0-26c7-39a0-9888-0065350e08fd | -8.31157 | -48.05219 | 2025-05-14 04:46:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51c3c250-8c9e-379c-909e-7a493a094107 | -10.24142 | -47.59543 | 2025-05-14 04:46:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e961f42-928d-3550-8547-a3f1c2238539 | -11.80082 | -44.27802 | 2025-05-14 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b75a003-5a9b-31c2-bc2e-fed5207b176f | -11.78956 | -47.36963 | 2025-05-14 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c6fd747-47a1-31d6-81fb-523af2c257b5 | -11.14889 | -48.67346 | 2025-05-14 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9770881-3aaf-351f-9824-e602b344e5d4 | -13.68585 | -47.77493 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e050053d-a61f-3838-af20-93ede0b62fe0 | -12.49426 | -44.49567 | 2025-05-14 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e3afb9c8-f136-3348-bccf-91d15f8e313a | -10.18533 | -48.03024 | 2025-05-14 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e396ba2f-1048-3979-9e87-26dcc89ead3a | -11.86562 | -54.79099 | 2025-05-14 04:46:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef98aac8-086c-3fb8-91c0-fd1ccb7974b0 | -11.91926 | -54.40551 | 2025-05-14 04:46:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc2b4b23-d638-3cc6-b2ad-b671eab60731 | -12.41794 | -54.36696 | 2025-05-14 04:46:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8de68f14-2db6-351c-8698-de37f26072a3 | -13.62357 | -54.88132 | 2025-05-14 04:46:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fcf1a84-ad14-3075-8339-76e0651198b3 | -13.09024 | -52.2879 | 2025-05-14 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8515628c-2fa9-3741-bb6d-6d330a1cda49 | -13.23915 | -49.8588 | 2025-05-14 04:46:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9532db0-4302-3e6e-ad2a-306fa58c9d8b | -11.65652 | -54.95324 | 2025-05-14 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38d8dbe5-6d5a-3e78-aa3d-a9104fc97223 | -7.71957 | -46.34028 | 2025-05-14 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ed922a7-773d-3c90-b63c-00574d4b443c | -11.92269 | -54.40608 | 2025-05-14 04:46:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06339ddd-2608-3063-b873-b70ba6c308bf | -13.68719 | -47.76487 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88be1cee-1552-377e-9ffb-4bd230c6301c | -11.79663 | -44.27179 | 2025-05-14 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb0131db-9435-3669-9477-ec086be5be98 | -10.00917 | -47.83725 | 2025-05-14 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d6689f86-5e2c-3172-9f19-9320b8900d6d | -13.57015 | -52.87256 | 2025-05-14 04:46:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1091b320-1e16-3ddc-be2c-ec62dade66f2 | -13.56574 | -52.87907 | 2025-05-14 04:46:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71bcf299-9021-3747-902e-81729343d292 | -7.9013 | -44.4749 | 2025-05-14 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12290684-35eb-3592-a11c-f22fd1baf8d2 | -11.57574 | -47.60825 | 2025-05-14 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1972c59f-32c2-3840-8403-c8bd93f9bba9 | -13.67835 | -53.94592 | 2025-05-14 04:46:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52ad068e-97ca-3ea1-9510-1298be516085 | -9.47154 | -40.31969 | 2025-05-14 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b6bc3a7-f576-3ca2-a091-a3cd85f14701 | -9.26747 | -50.21941 | 2025-05-14 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a0a2aee-12b7-3726-b61b-c324aa5d9bee | -11.79919 | -47.40929 | 2025-05-14 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1206861-060b-3362-81a4-777643043dac | -13.67893 | -53.9423 | 2025-05-14 04:46:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bf50fac-ecf0-359d-b6af-b7af18639290 | -12.50585 | -57.21503 | 2025-05-14 04:46:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README7.md)
