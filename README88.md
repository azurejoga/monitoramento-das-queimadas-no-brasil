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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42465269-daf0-3774-8196-cc25ac99e6ef | -11.30378 | -46.33107 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8c94a7a-4a61-3309-a96c-a51880401d7e | -11.29684 | -46.32523 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b359c0ab-2b2d-3d7d-8bfd-6a7836122c68 | -11.10879 | -46.18037 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5229128b-98aa-359e-adaf-6ec05644624d | -11.10495 | -46.1799 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83b73338-9a30-3763-b59c-cd3bd92e2bd4 | -11.09236 | -46.1584 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 784f8ed7-ecde-334d-84cc-328eaaccb6f8 | -11.08921 | -46.153 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93b48a0d-b374-3793-9abf-a9acfb08ec67 | -11.69342 | -46.36212 | 2024-09-27 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 737df23c-3956-3bf1-9e80-f726a5b98aa2 | -11.92724 | -47.3697 | 2024-09-27 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccc572a3-0384-3194-810e-8d419ccf7b86 | -11.90193 | -47.15877 | 2024-09-27 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89cf88bc-3c0b-3019-811f-dfcbe6f39cb9 | -11.88729 | -47.15657 | 2024-09-27 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ef809af-2df9-34f9-bf71-59cf858c6b50 | -11.88364 | -47.15599 | 2024-09-27 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eab59ae2-fec2-3d7b-bf23-a943982b5c55 | -11.83344 | -47.78555 | 2024-09-27 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8431aa46-b6c2-32ff-bbfd-f2607d02454a | -11.70757 | -47.10712 | 2024-09-27 04:40:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95366281-19e9-3dee-b6bf-bdfa56b24ddb | -11.70693 | -47.11153 | 2024-09-27 04:40:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1257c2a-c0fa-31b4-b7e4-0f26869b1700 | -11.52063 | -47.42132 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05a26c65-6d23-3873-8f71-8488720da057 | -11.32938 | -46.90551 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78730ee0-4567-3f3b-ad58-04862dc2f7d5 | -11.27757 | -47.1339 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ca163a4-5fbe-3a4f-8f47-55c11a43301c | -11.27394 | -47.13332 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb208f03-3b9f-3b74-afde-2957d32b04b7 | -11.26188 | -47.1138 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ceefa54-7d45-3beb-9e3c-7887f6d834e2 | -11.26125 | -47.11814 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| be3e6298-c0b8-37a5-b2bd-11b0ffc011ad | -11.25823 | -47.11327 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 45d4280f-982c-3f0d-8416-4ebaf8b993ef | -11.25459 | -47.11274 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ff8c4f8b-1e05-33ad-bcde-899ff3eb964a | -11.25397 | -47.11703 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 59bfd87d-1fec-30d7-bb44-e70b95a268f7 | -11.25336 | -47.12133 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 845c8717-f41d-3a68-9a04-c568676f1194 | -11.25274 | -47.12563 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ee33845-63ea-3379-8075-fc5c489cb4b0 | -11.25033 | -47.1165 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8ef6804-f3bd-339d-9685-764285dd2fff | -11.24972 | -47.12079 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e47b0b1f-bba6-31e6-b838-f8cda043a4de | -11.2491 | -47.1251 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 891df1b2-b0ef-3a70-90d8-f2433ffc8989 | -11.24669 | -47.11596 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f237686e-07e1-366d-8e8e-ba89c7475625 | -11.24608 | -47.12025 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 232c0c75-8f8f-3be8-93ce-9076ca72e713 | -11.24546 | -47.12456 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 17c50730-3ee1-3c81-8e2d-a3b6e42b1abd | -11.24243 | -47.11973 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dd05ec3-6e39-3317-97a3-bca3971065d2 | -11.24182 | -47.12402 | 2024-09-27 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69df6634-d0d3-3577-ba68-8906cff72392 | -13.64251 | -47.58155 | 2024-09-27 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd6ab3c4-7156-3bc6-af9b-fc851111662d | -13.48319 | -48.0303 | 2024-09-27 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e95e729c-1079-37a7-9f8f-36b2c4022e8c | -13.48255 | -48.03458 | 2024-09-27 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f35f71d-bfe3-3261-8638-ee8340f45e99 | -13.48205 | -48.03274 | 2024-09-27 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e40ddb4-a10c-3b0d-a00c-6e3e85de5f0d | -13.47899 | -48.03403 | 2024-09-27 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc80c8ce-a03c-3277-aef7-07cba6dab200 | -13.47848 | -48.03219 | 2024-09-27 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d1a3895-4b32-363a-85fd-66d26daf8c59 | -13.42255 | -48.04652 | 2024-09-27 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 475646b5-cead-31b8-91d9-1a06549095d9 | -13.3992 | -46.73924 | 2024-09-27 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c78b84e-cfb4-31f5-9758-11dde60f2b97 | -12.78446 | -47.25874 | 2024-09-27 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1119fbae-00e1-354d-a415-95c4588d70b8 | -6.1595 | -47.69296 | 2024-09-27 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03410f98-8c6d-3fef-9b32-992d987d04c5 | -6.15612 | -47.69244 | 2024-09-27 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0b32941-935a-377c-ac38-a4d98938f0d8 | -6.15329 | -47.68828 | 2024-09-27 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f202038a-19e3-39fa-8a79-3e80f239c6a8 | -6.15273 | -47.69193 | 2024-09-27 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a65ad46-b65e-378c-8a9a-545b73fda981 | -6.12412 | -48.08116 | 2024-09-27 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6980b610-e215-394e-a35a-5d860095ec2d | -6.12077 | -48.08064 | 2024-09-27 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6104b0f2-9d33-3a67-b07e-3f3c14a3bd4a | -6.09817 | -47.65422 | 2024-09-27 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9849496e-0f67-3904-b68b-cc8543562e32 | -6.0914 | -47.65318 | 2024-09-27 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39899214-ab76-3a20-a384-5256a4c90138 | -6.09084 | -47.65684 | 2024-09-27 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba82ef6e-64ab-3aed-a43e-5101929a1a67 | -6.09028 | -47.6605 | 2024-09-27 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2423a93-2e5b-34eb-89cc-a5303e3e34c1 | -6.08972 | -47.66415 | 2024-09-27 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3e009a6-0a31-36e4-8d8c-358c8f73c7ca | -6.08916 | -47.66777 | 2024-09-27 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 185b826f-586a-3fc7-954c-599e20fdafba | -6.08522 | -47.67085 | 2024-09-27 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 683d286b-2365-327c-9c4d-385a58ddf330 | -6.08467 | -47.67448 | 2024-09-27 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a7c428c-252b-3960-a168-d8adadb8169e | -6.04061 | -47.43469 | 2024-09-27 04:40:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eacd0a70-575d-3357-bcfe-4811121c70f7 | -6.03663 | -47.43787 | 2024-09-27 04:40:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80dcaacb-a0b9-3abc-ae9b-fb1bda717f74 | -6.03323 | -47.43734 | 2024-09-27 04:40:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 629e1315-8b43-323c-baa3-9672315ef62e | -6.37958 | -46.93218 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e59a56f5-9e07-335c-8059-eada0b9e6b13 | -6.33958 | -46.90313 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0543984a-b80d-3a9a-a16a-3fb249001fb7 | -6.3361 | -46.90258 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0c7c503-2d71-38b1-8e64-1fa91babdbf4 | -7.93666 | -47.23823 | 2024-09-27 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bae8acff-352d-328e-9831-17b3a4e2223d | -7.84214 | -47.19278 | 2024-09-27 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37709f37-927a-3291-bacb-35dc25a3d35b | -7.84026 | -48.35239 | 2024-09-27 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2eeb961-6534-33ee-a7b2-6890874ff0df | -7.83803 | -47.19624 | 2024-09-27 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9273bd9-08a5-3315-a642-e653d1ed2d04 | -7.77165 | -47.11395 | 2024-09-27 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8219f53-fe92-392d-8df6-76681d816075 | -7.76815 | -47.1134 | 2024-09-27 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6036a27-85a5-3931-8fdc-6814bdfe1956 | -6.80069 | -47.06933 | 2024-09-27 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15c7a814-e617-3c84-9048-2b276431870a | -7.51523 | -47.56356 | 2024-09-27 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5fcbd19-99f3-32c1-9b4d-6a74027df35f | -7.5118 | -47.56303 | 2024-09-27 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15ed9e44-df31-3b92-b070-f98dd73e7451 | -7.50836 | -47.56252 | 2024-09-27 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be593720-b9d6-33a6-8794-73bf9e0d9aef | -7.4884 | -47.60169 | 2024-09-27 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae4358a5-c9ab-3fb2-80d8-0d1360595248 | -7.10979 | -48.06033 | 2024-09-27 04:40:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b9fa8ca-5889-3401-aca8-f309e9736cff | -7.01925 | -46.81668 | 2024-09-27 04:40:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d09f4b32-f47b-30a7-8024-431eb3501271 | -7.01573 | -46.81612 | 2024-09-27 04:40:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1545c503-b149-373b-8102-43c08eefc0eb | -9.01062 | -48.72398 | 2024-09-27 04:40:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16f1871e-a00a-382b-ab7d-0c6b7cc7e3a3 | -8.89089 | -47.3719 | 2024-09-27 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c3f4eeb-1689-373e-afd4-d260a1062d69 | -8.8903 | -47.37584 | 2024-09-27 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f89ddf5d-e1c8-371e-a2c1-c5414c5ba678 | -8.52392 | -47.33485 | 2024-09-27 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d42d6b4e-f708-376a-bfa2-83498bf3cd13 | -8.52042 | -47.33431 | 2024-09-27 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f83dd03-7cbc-3cb4-87c4-d38a55aa6ff8 | -8.36377 | -47.58455 | 2024-09-27 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17946674-27d3-3eb5-a3d9-1ebd84e96249 | -8.36031 | -47.58403 | 2024-09-27 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 994a4816-42c0-33d6-b00b-3879b29154eb | -8.35685 | -47.58353 | 2024-09-27 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72f54f55-d215-30dc-9454-79e7b0e011a7 | -8.35339 | -47.58302 | 2024-09-27 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09f215e2-f0a7-360d-98cb-a95b4145313e | -10.78153 | -48.0767 | 2024-09-27 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 145c192d-2dd9-37af-ab36-4967c9f8a66b | -10.66964 | -47.91839 | 2024-09-27 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9222b5fc-ee25-3493-b1fe-74cedc94652f | -10.66905 | -47.92233 | 2024-09-27 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b593c243-3669-3cb5-a580-da3ae1a51480 | -10.54467 | -48.07344 | 2024-09-27 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f8a8a9a-b952-3891-bd0d-ed0370210bdd | -10.54369 | -48.073 | 2024-09-27 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3760a862-5ddb-3380-97f2-e98e9ebb3a97 | -10.53883 | -48.0653 | 2024-09-27 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 50a13191-5b81-3a73-9e69-618c2aa0a430 | -10.53536 | -48.06487 | 2024-09-27 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5632c5f6-c7d1-377e-b16d-fcc35263e8b8 | -10.53483 | -48.0684 | 2024-09-27 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2c7dc633-391c-3011-a791-8c0968c40f5c | -10.53428 | -48.072 | 2024-09-27 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 841a71ec-c509-3df8-b1bc-86c3c10bb7e0 | -10.53136 | -48.06793 | 2024-09-27 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af57746e-6179-3d76-ab1c-1d692bab6f67 | -10.53082 | -48.07152 | 2024-09-27 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a59e6da6-b5a2-37b8-a892-8a55b67358a7 | -10.53026 | -48.07524 | 2024-09-27 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f9cd817-46e2-39b1-a357-5991ec3ca0a6 | -9.96495 | -47.5009 | 2024-09-27 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0e7cfe4-02cc-3474-af71-7f3f8d8374ac | -9.96435 | -47.50491 | 2024-09-27 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6887ecda-2a0c-3c5a-ad7c-143a6dabbe4b | -9.96143 | -47.50038 | 2024-09-27 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README89.md)
