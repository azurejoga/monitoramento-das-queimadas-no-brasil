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
| ee9a8fff-543b-3a92-b58c-c9e7d134863a | -6.9281 | -47.485802 | 2024-10-15 00:17:33 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0af47556-6db3-3b79-a470-f2c08de635a9 | -6.9311 | -47.5 | 2024-10-15 00:17:33 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ad72107-66df-3ea6-b6b3-3d9dfebea4e8 | -5.3768 | -41.143398 | 2024-10-15 00:17:35 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bb70653e-f52b-3c0d-be42-65bc94651101 | -5.9634 | -43.785 | 2024-10-15 00:17:35 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b274ca98-0cf4-3141-a668-4d70cef23ffa | -6.4654 | -46.057701 | 2024-10-15 00:17:35 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8d54b3e-66b8-37fc-b1e1-a23756b748fe | -6.8571 | -47.9147 | 2024-10-15 00:17:35 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 607aa4ba-5463-340a-be8e-5b8967af7627 | -5.9677 | -43.8965 | 2024-10-15 00:17:36 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab0aed8e-743e-3b68-8442-da838c7ee339 | -5.8508 | -43.741299 | 2024-10-15 00:17:37 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1e57b00-08ca-35fa-b2a4-62b38e4c3e9c | -3.6851 | -42.944901 | 2024-10-15 00:17:40 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 707150db-2344-35c5-82c8-4c1e415c181b | -5.1257 | -41.669201 | 2024-10-15 00:17:41 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2cabf926-a552-3a27-adf7-0365b7c47d7c | -5.1273 | -41.676201 | 2024-10-15 00:17:41 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 57ef3010-81c4-3dab-aa98-64439d1d8e53 | -5.1159 | -41.671398 | 2024-10-15 00:17:41 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| efc4237b-9c3d-3cdc-9924-675b76e8a75b | -5.1175 | -41.678398 | 2024-10-15 00:17:41 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a0b3eb98-f13b-3fa5-a03b-f22e1cf5a2c8 | -5.534 | -44.7159 | 2024-10-15 00:17:46 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ddc09e7a-2b85-3df4-a96b-815f05c2e85e | -5.536 | -44.724998 | 2024-10-15 00:17:46 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3b1dd67-6ebf-3c0e-9f1f-9098f328275e | -6.4068 | -49.564701 | 2024-10-15 00:17:49 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 929d5d57-a7f3-3594-bddb-d4d3e9c8c2f9 | -6.4109 | -49.584099 | 2024-10-15 00:17:49 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f04a4c31-31ea-3b53-b45e-1bee0ac6d338 | -5.0387 | -43.6506 | 2024-10-15 00:17:50 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cea3e3e-10e2-3cf3-a2de-f452b091597c | -5.0405 | -43.658501 | 2024-10-15 00:17:50 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 041ca856-a8a7-3291-9a28-686d093943e9 | -5.0423 | -43.666401 | 2024-10-15 00:17:50 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc0c6c06-5394-3400-b3d3-6e28673bf340 | -5.0441 | -43.674301 | 2024-10-15 00:17:50 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff9d7dca-4f6e-37f0-aa4e-8ae3e4984807 | -4.0177 | -47.209599 | 2024-10-15 00:17:50 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96403a74-f816-3d46-a538-fb587cdedd93 | -4.2336 | -40.3848 | 2024-10-15 00:17:51 | METOP-C | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f5a735f9-abc5-3ab8-b94f-855e96262390 | -5.3159 | -45.582001 | 2024-10-15 00:17:52 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ec3780a-286f-3326-a01f-67cfa89d426d | -5.1604 | -45.0667 | 2024-10-15 00:17:53 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 422aa14e-8f72-3001-9971-259db76fbdb8 | -5.1506 | -45.068901 | 2024-10-15 00:17:53 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb237819-f734-3b63-99d9-f76758cfd117 | -5.2329 | -45.484699 | 2024-10-15 00:17:53 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cca12f53-f88e-3ba0-8bbd-7311e890604d | -4.9986 | -44.5718 | 2024-10-15 00:17:54 | METOP-C | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37a566d8-0d3a-38cb-9ef6-e1170af9f11e | -5.0006 | -44.580502 | 2024-10-15 00:17:54 | METOP-C | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abd1a0a0-6b70-36ca-a6e5-394dfa87d915 | -4.5156 | -42.883301 | 2024-10-15 00:17:55 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5225bdd0-464d-3829-af59-15f2dccb0b25 | -4.5173 | -42.890598 | 2024-10-15 00:17:55 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28baf889-d91b-3cb7-9952-0f19277de4a8 | -5.2975 | -46.378799 | 2024-10-15 00:17:55 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b87a546-c2dd-33e0-90e7-6827825983d8 | -5.3 | -46.390099 | 2024-10-15 00:17:55 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8117133c-3031-3413-b679-ed0d437752fb | -4.6502 | -43.752499 | 2024-10-15 00:17:56 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08fcf262-59b4-373f-aab1-ece3915beaab | -5.2877 | -46.380901 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3a39525-a720-3b87-a0a4-d74236db9bfb | -5.2902 | -46.3922 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aaf1a4a9-ecb3-3ff2-bdd3-02dd76b6a58f | -5.2927 | -46.403599 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4e770f84-14e5-3d48-94d1-1494af290d79 | -5.2705 | -46.3493 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc20acc4-21d0-3e45-b38f-d83d6d363efb | -5.273 | -46.3605 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6c134d3-273d-3bc0-b767-59dd7946c969 | -5.2755 | -46.371799 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9aa06b3-7807-3ab7-a308-1c33b9684236 | -5.278 | -46.383099 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dac49ebc-c032-39cb-bd13-7d0726cca5cd | -5.2805 | -46.394402 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad37b5e7-002b-3c20-9368-5359a5f3767e | -5.283 | -46.405701 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9258cbfc-92b8-34a8-a62a-0ac59101327a | -5.2632 | -46.362598 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8291756-cb26-3b09-810f-052480e3b711 | -5.2657 | -46.373901 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2bd3fc87-598e-38c2-bbdd-65e21b715677 | -5.2682 | -46.385201 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9edd530c-b26b-32ea-9a4e-8c99d9187c82 | -5.2707 | -46.3965 | 2024-10-15 00:17:56 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c706f591-60b4-37c2-a713-ecf5bfc2b121 | -4.8674 | -45.409801 | 2024-10-15 00:17:59 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32259482-1f6a-32c3-9ece-21cd4812f66a | -19.65612 | -40.47751 | 2024-10-15 00:18:00 | TERRA_M-M | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| ecffbb35-0cde-3463-a98a-0ea0ea9ea6bd | -19.64721 | -40.49206 | 2024-10-15 00:18:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 35c2ce95-9967-348d-a0e2-4f706b7aa955 | -19.64569 | -40.47904 | 2024-10-15 00:18:00 | TERRA_M-M | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 6924a2a0-2ee8-3f30-ae9c-472fce2c124a | -18.83996 | -42.4175 | 2024-10-15 00:18:00 | TERRA_M-M | SANTA EFIGÊNIA DE MINAS | MINAS GERAIS | Brasil | 3157500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.9 |
| 7d9772ff-4c50-3eca-9850-ec767561a810 | -18.83577 | -42.42993 | 2024-10-15 00:18:00 | TERRA_M-M | SANTA EFIGÊNIA DE MINAS | MINAS GERAIS | Brasil | 3157500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| 466a0616-761a-3e18-8264-3ccec01e03ce | -18.8339 | -42.41225 | 2024-10-15 00:18:00 | TERRA_M-M | SANTA EFIGÊNIA DE MINAS | MINAS GERAIS | Brasil | 3157500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.6 |
| 75888a7a-b106-3997-93db-eef89e0a10da | -18.78084 | -41.80464 | 2024-10-15 00:18:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| b2d3f70b-6f86-3758-af09-538cd2fdec08 | -18.7793 | -41.79884 | 2024-10-15 00:18:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| 8df646a4-9e12-3d30-be14-26fb528517b7 | -18.77893 | -41.78844 | 2024-10-15 00:18:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| c85b6e65-cf79-393c-b32b-2a5f43fa3d18 | -18.35539 | -42.7068 | 2024-10-15 00:18:00 | TERRA_M-M | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 40af91d0-99bc-3863-bf9a-533aba12176a | -16.77808 | -42.84345 | 2024-10-15 00:18:00 | TERRA_M-M | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3977239e-f25c-3554-9819-45cb10ffe2a0 | -4.1 | -42.277802 | 2024-10-15 00:18:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3f5c1e5b-80cd-3cdc-b92c-32df6cbea423 | -4.1015 | -42.284801 | 2024-10-15 00:18:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 68f557a8-9deb-3a2d-951d-ae1828207c75 | -4.0901 | -42.2799 | 2024-10-15 00:18:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b6ae0ce4-4d81-3faf-9a42-4467128ebe39 | -4.0916 | -42.2869 | 2024-10-15 00:18:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 25fdc794-4d28-386b-b05c-f7a59f96ba9a | -4.0932 | -42.2939 | 2024-10-15 00:18:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d6e2f23f-221c-3eef-9d1b-4358a8aeea92 | -5.5566 | -49.387199 | 2024-10-15 00:18:02 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baa014ea-3c08-3353-9e77-f5606ca6e66d | -5.5605 | -49.405602 | 2024-10-15 00:18:02 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc1fb994-2b01-302b-bd41-91e227e225dd | -4.6837 | -45.782501 | 2024-10-15 00:18:03 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9aa7f220-fc8d-31db-9229-5287b752c655 | -4.6859 | -45.792599 | 2024-10-15 00:18:03 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d6089fc7-86e0-3af5-aa38-a76350b9fbd5 | -4.6739 | -45.784599 | 2024-10-15 00:18:03 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b72c3300-408c-3372-a09c-c7826c0f579c | -4.6761 | -45.7948 | 2024-10-15 00:18:03 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6cdd0a05-0087-3bc5-b731-bfe8da3e3e92 | -2.8036 | -45.275101 | 2024-10-15 00:18:03 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c9c3bd8-1b77-306e-a66c-4304dc62d1d1 | -2.8056 | -45.284 | 2024-10-15 00:18:03 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4d5b4c7-bba0-3c65-893f-76ad34fb69f5 | -4.0183 | -43.233002 | 2024-10-15 00:18:05 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b663875f-6be6-3813-99a5-2dd3c2434696 | -4.02 | -43.240501 | 2024-10-15 00:18:05 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56d1c34f-ddac-3985-a4dc-f6b73e75cc76 | -4.8642 | -47.104801 | 2024-10-15 00:18:05 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 18f58f8e-ea54-3f98-a425-d8ec75845c84 | -4.6397 | -46.322498 | 2024-10-15 00:18:06 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e1e19c4-9226-3c0d-89af-7d157096854e | -4.7151 | -46.7085 | 2024-10-15 00:18:06 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3fb89260-2532-3f97-8981-7d33078fef50 | -4.7177 | -46.7202 | 2024-10-15 00:18:06 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf838fb-d395-32fc-9d6b-de3696741734 | -4.4579 | -45.8741 | 2024-10-15 00:18:07 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 57f716e2-ee2b-3c8b-a577-12a3f29cd0cc | -4.4602 | -45.8843 | 2024-10-15 00:18:07 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa640755-26b6-3211-827c-adb2dde270ef | -4.4625 | -45.8946 | 2024-10-15 00:18:07 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8773a6ab-7304-3717-8546-46155f2da6ed | -4.5376 | -46.554501 | 2024-10-15 00:18:08 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 235c6547-e757-3801-be8e-10f37f61b0fe | -4.5401 | -46.5658 | 2024-10-15 00:18:08 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44f9a859-afd7-3d5a-a36c-fa95d387ab03 | -4.5278 | -46.556599 | 2024-10-15 00:18:09 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f5f8c463-c57c-35d1-8197-1391724ad484 | -4.5303 | -46.567902 | 2024-10-15 00:18:09 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 93625d5f-d79f-3e6f-ab7b-8a8fdc0775fb | -4.5329 | -46.5793 | 2024-10-15 00:18:09 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 595a2ba3-b9b2-3ae6-aed8-95483105705d | -3.5159 | -43.243099 | 2024-10-15 00:18:13 | METOP-C | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c98d2271-2f4c-3fd9-b846-511ae9cd7d06 | -3.5176 | -43.2505 | 2024-10-15 00:18:13 | METOP-C | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90b5a688-4838-3025-85d4-ebb6a27d095a | -4.3577 | -47.266102 | 2024-10-15 00:18:14 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed19f8f-7002-3ba5-83c2-7c976a211562 | -4.3605 | -47.278599 | 2024-10-15 00:18:14 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9d07422-cb5e-302b-89b9-4d34d5e97405 | -3.415 | -43.343102 | 2024-10-15 00:18:15 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10a0b345-89b6-3536-b04a-301f16bfa89c | -3.4167 | -43.350498 | 2024-10-15 00:18:15 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f61223d-f111-3eef-be3e-a13ece3a480f | -4.3833 | -47.751099 | 2024-10-15 00:18:15 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 531c1c74-8e40-3971-b065-0d235c3d8714 | -4.3863 | -47.764599 | 2024-10-15 00:18:15 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2ef8638-f014-3d1e-a8e7-7b83db796351 | -4.3736 | -47.753201 | 2024-10-15 00:18:15 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b11b53f3-eab3-3e83-bfdc-18bc18cfd260 | -4.3765 | -47.766701 | 2024-10-15 00:18:15 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0d5a5cc-e3c4-3e5e-928c-7a883a51badf | -3.1444 | -50.438999 | 2024-10-15 00:18:16 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcf402f3-f949-3ef0-814a-fbb31c51b1b9 | -3.1488 | -50.4589 | 2024-10-15 00:18:16 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f02eb5d9-0b05-3865-b502-549316203da9 | -3.9456 | -46.426998 | 2024-10-15 00:18:18 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 373fb641-5ca9-3190-b5b7-7f2125e6e21a | -3.948 | -46.437901 | 2024-10-15 00:18:18 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
