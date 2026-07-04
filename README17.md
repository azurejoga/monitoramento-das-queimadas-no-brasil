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
| b048005e-3367-377a-a565-a0e0a4b896e7 | -10.9209 | -43.0384 | 2026-07-04 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 28077d38-7339-3436-8a04-fd3f015ca598 | -12.7553 | -44.5194 | 2026-07-04 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 1990a895-c7e8-35a3-9e42-a1daab4e7a80 | -10.9205 | -43.0622 | 2026-07-04 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| ae9861ac-ba4d-3cff-8941-4b199dd121f9 | -12.7741 | -44.5396 | 2026-07-04 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 98f6079e-dfe8-3ae8-9fc2-9dc59dd2f9d5 | -12.7548 | -44.5428 | 2026-07-04 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 224.2 |
| f7b99a9f-b8b0-3734-9f2b-77fbaf59417f | -13.2595 | -54.3283 | 2026-07-04 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e1e8c27c-4072-34ce-b871-b9c69e9f6e4b | -10.9401 | -43.0355 | 2026-07-04 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 173.1 |
| a30d125a-6485-338a-a9f2-d4add4c54e6f | -4.69745 | -55.98867 | 2026-07-04 05:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9f747b6-1858-3747-9605-97d9a37a9473 | -7.73456 | -44.17191 | 2026-07-04 05:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f658e15-0981-3ef1-a0f3-7f95c1a93f81 | -4.29313 | -48.35261 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4a66e2f-46d6-380f-9dd4-4ce7675a271e | -4.57479 | -48.02906 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb515af4-39ff-38c3-8dfe-babc673d4595 | -4.14201 | -48.83971 | 2026-07-04 05:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e76d33f1-27fe-334b-b60e-b55ccdd39075 | -4.01058 | -48.06636 | 2026-07-04 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acf83917-55f3-3677-b8bb-4fb3a9e7d150 | -7.7305 | -44.17605 | 2026-07-04 05:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 601318fe-a26f-3a5e-a6c1-6da81d3bf501 | -4.1475 | -48.8375 | 2026-07-04 05:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d239f08a-81f1-3995-956a-0d2a757f6aca | -7.23319 | -47.11184 | 2026-07-04 05:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03f052e9-fbb6-3df8-b5c5-b696a9571dac | -7.1683 | -47.05553 | 2026-07-04 05:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55311f9f-9e54-3663-b41a-46ca543ab002 | -4.29329 | -48.35436 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9770af1b-389b-3955-beaa-226c245e67bc | -4.33854 | -48.95867 | 2026-07-04 05:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e37fbfaa-68bb-3777-965c-d3c81e7af434 | -4.00926 | -48.06582 | 2026-07-04 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 241bdfbb-a9cb-3354-bd64-d4afd1f8cd9e | -7.16772 | -47.0598 | 2026-07-04 05:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b10a6ba6-d871-31d1-ad3a-934da6a6b674 | -5.31963 | -43.56019 | 2026-07-04 05:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14895521-5651-3b3a-b7ea-d81093b48d9a | -6.93189 | -43.7148 | 2026-07-04 05:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c89534c0-5572-3f4c-abc3-e67dd0bd764f | -6.67091 | -47.92187 | 2026-07-04 05:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bf19e0b7-4223-37a5-96fb-ec3e66707d8c | -7.73367 | -44.17894 | 2026-07-04 05:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e01008f-00d1-39f2-8b38-dede010a0430 | -5.31866 | -43.56694 | 2026-07-04 05:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c4601fb-4be0-3f7e-b71c-3905eea6b6e1 | -2.76932 | -48.57472 | 2026-07-04 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 298ce372-bdc7-3b37-b59a-c9401dfaaeff | -4.28753 | -48.35701 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ebc54378-23f6-34a2-a351-52afb3bcdd0a | -3.284 | -50.69746 | 2026-07-04 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eca83518-239e-3925-be1c-3feba3d00d98 | -5.31051 | -43.57281 | 2026-07-04 05:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ad8efe92-f0b4-3466-acbd-2ab63c8decc3 | -4.14244 | -48.83677 | 2026-07-04 05:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 208b076f-9d72-39c1-9f1e-b17e4f83349c | -4.01106 | -48.06318 | 2026-07-04 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ffa2083-a8a2-3572-8fe5-15d7c8c0c613 | -3.51172 | -48.03693 | 2026-07-04 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18607919-a62e-3887-b0b7-f7fc29417d0d | -7.23261 | -47.11595 | 2026-07-04 05:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ac6053d-1d57-3b32-b5fa-6ceb39074b01 | -3.506 | -48.03915 | 2026-07-04 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c5f99ca-8e27-39bc-a519-dc793700303d | -6.70483 | -51.88387 | 2026-07-04 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5e66fb0-0420-30a9-92a6-b815cb21a18a | -6.93385 | -43.71347 | 2026-07-04 05:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2157e95d-b5b8-36bd-a046-e37df9157337 | -5.31568 | -43.55833 | 2026-07-04 05:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d8994779-52e8-35a3-8973-032bbbbec9c9 | -4.01633 | -48.06422 | 2026-07-04 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f4ee0d3-c20b-3d69-9beb-00a13686256b | -4.34862 | -47.76802 | 2026-07-04 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c24b6126-7cf9-31b4-97fa-82d837e8ebc3 | -3.51221 | -48.03365 | 2026-07-04 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dea6b3c-333c-3ffd-813a-04e4b6b15a1b | -4.34318 | -47.76715 | 2026-07-04 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f5eacab9-7c62-3d40-9308-f37b3552abc7 | -7.23909 | -47.11283 | 2026-07-04 05:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7bcf27ff-6133-3e76-9923-42bde560a215 | -6.66585 | -47.91743 | 2026-07-04 05:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1c661ca-ff4d-34e9-ab20-0c9bae334b01 | -6.93292 | -43.72082 | 2026-07-04 05:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9372b1b0-f7ac-36af-a6ee-d33c52ddea9a | -5.46712 | -45.424 | 2026-07-04 05:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99764041-35ee-3ba4-83e1-3d9f704dfebd | -4.00533 | -48.06513 | 2026-07-04 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 451a6143-0ade-33f0-b2e1-e81aab186a25 | -4.34914 | -47.76448 | 2026-07-04 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5552933b-e257-371d-93c3-d6d3896576db | -5.43736 | -44.65392 | 2026-07-04 05:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeb0c0b0-ff6e-37f0-92f8-004cfdfe4d5a | -3.1879 | -61.17127 | 2026-07-04 05:21:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8da532e8-111e-38b2-bdbf-044c053bbbd0 | -2.76975 | -48.57187 | 2026-07-04 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 666da142-e335-3208-8b2b-e6e2b994c6e5 | -4.00581 | -48.06197 | 2026-07-04 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7431f039-9c4c-3d4d-b6e8-8f282d449eaf | -3.51128 | -48.03996 | 2026-07-04 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ecd8aff-20b4-3ed7-8623-7e7ed0db8a65 | -5.31383 | -43.57189 | 2026-07-04 05:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 62ce7f17-317e-3bb2-b41e-3a457f2263dd | -6.67143 | -47.91824 | 2026-07-04 05:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a7a30ba0-44ff-3e05-b1f9-9f17725e767f | -5.43059 | -44.65314 | 2026-07-04 05:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b04642a1-edcf-3bca-9b04-c4ecc8323288 | -7.73765 | -44.17687 | 2026-07-04 05:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 899f4595-38aa-3fbf-9274-77e1ed7fbf6f | -2.76564 | -48.57482 | 2026-07-04 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1997b712-7600-3e09-b196-6bca2d79efd1 | -5.79934 | -43.63741 | 2026-07-04 05:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5ff7f75-8949-3894-b001-d62f100945ba | -5.31473 | -43.56527 | 2026-07-04 05:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 63ef6d66-f348-39a0-bd54-e4b7747a24c1 | -7.23851 | -47.11695 | 2026-07-04 05:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 012249f7-dddb-35f8-87c3-21b9b1dde0d6 | -5.31146 | -43.56614 | 2026-07-04 05:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| daf24be9-7f1e-3abd-b8de-93a4c20b8a58 | -4.28788 | -48.35198 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb9eab06-a0a4-363d-9beb-760229f587b2 | -4.01499 | -48.06375 | 2026-07-04 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b257d047-ba7e-3cd5-8ce7-d887f71b6d51 | -4.29266 | -48.35588 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c2e50f5-15cd-38bd-891e-1a1642ca6561 | -4.3437 | -47.76363 | 2026-07-04 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 36dff702-7b98-30fc-b5a5-8b9a5c27bdae | -7.73863 | -44.16949 | 2026-07-04 05:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07437f42-c26d-3923-bf30-ef177ccdeee3 | -6.93092 | -43.72209 | 2026-07-04 05:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3373b56e-6b42-3d64-83f2-abb5209c4b80 | -4.58064 | -48.02655 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59f92249-a5c2-3734-8e1a-1717ff84f0f7 | -4.28703 | -48.36032 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d82ccb4d-9d8e-3f6c-8765-a166c658f7a9 | -4.58016 | -48.02986 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9feb0e7-bbf6-3e7a-be37-46927b77a1b6 | -2.76471 | -48.5711 | 2026-07-04 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8dd5ff5-aa20-3be3-9b0f-65fb32bb7e7a | -7.24171 | -47.11479 | 2026-07-04 05:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| def392df-e042-3191-856e-0c14dae35833 | -5.31244 | -43.55928 | 2026-07-04 05:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0699de28-ea83-30fe-a104-b345c622f69d | -7.23578 | -47.11395 | 2026-07-04 05:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c127ff6-161c-33c6-b4fb-c783e9d232c6 | -4.28741 | -48.35523 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9b06772-a697-3470-95c9-5760229f407b | -2.96332 | -52.64959 | 2026-07-04 05:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fe8b642-a3ec-395e-8976-80a84a9b3249 | -7.16175 | -47.05919 | 2026-07-04 05:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 327eae78-fdf3-303f-97d9-51b3eac0d14d | -7.16231 | -47.05498 | 2026-07-04 05:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f1abfbf-988a-3a99-9b6b-99ac8ed1011d | -4.57526 | -48.02578 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 637effcd-da8c-3c01-a17d-a804f69df85d | -4.28803 | -48.35372 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eeb11cad-8d07-3986-9dc1-7e51e9804b22 | -4.00972 | -48.06263 | 2026-07-04 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6bc021b-004a-31df-bb78-f7e84ecc07e3 | -5.7984 | -43.64444 | 2026-07-04 05:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48cf5a83-6bfc-37c2-b7f7-2dce87495685 | -4.28693 | -48.35855 | 2026-07-04 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0c90a3e0-1798-3ac4-9925-12df5b409938 | -10.29946 | -57.12456 | 2026-07-04 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 191a0374-bc82-3951-915a-acddb508ace4 | -13.22535 | -54.39959 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b0f3e67-0767-3e72-9b37-34aa8addbd9d | -17.54791 | -46.9459 | 2026-07-04 05:23:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cea7a693-9999-38ab-a6ed-86f7e508f7e5 | -9.11499 | -61.48825 | 2026-07-04 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4fc890-9d9d-333a-b56e-db7ab719dcd4 | -8.08269 | -47.1619 | 2026-07-04 05:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55bf9afa-620a-3323-9e7a-769976194b1c | -7.62663 | -50.036 | 2026-07-04 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5bb845bf-22b7-3089-8761-fc5b151454a3 | -13.22241 | -54.36237 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00983130-f506-390f-983e-4a3e561c62e4 | -9.96796 | -54.93549 | 2026-07-04 05:23:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74f0dbc3-7e6c-3053-9bc2-9a75ea3e8543 | -11.63195 | -59.01274 | 2026-07-04 05:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9862721-5d4c-36e5-b018-ae5cf8085346 | -13.2329 | -54.37439 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1f25669-218f-335f-83fb-45457e91b548 | -11.4373 | -46.57299 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c1d7dfa-2202-3f2e-8163-a79031984f32 | -13.23902 | -54.35951 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43b591bd-2adf-3ed4-a2c8-396a3ed5366a | -13.23758 | -54.36981 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a262bb51-d8d5-396e-b633-541de1c95c79 | -13.22457 | -54.34674 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 966adc20-f8e3-3df9-9aca-8cd023e5efcf | -13.25312 | -54.34561 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 89c4e97f-aa1e-3c9c-9f7b-e6934216f07d | -13.23003 | -54.39503 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README18.md)
