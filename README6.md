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
| efc9682a-7628-3a8b-84e5-bd4b94864ddf | -6.2537 | -48.5357 | 2025-06-09 04:57:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0a6b561-39d4-361f-98b3-dec6a28c1cf0 | -4.48947 | -43.77311 | 2025-06-09 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3282a7bf-2779-3a69-9e15-2d0397bf5470 | -10.25578 | -46.91065 | 2025-06-09 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34af171f-8f32-3ff4-a3c8-e551711ba6ae | -10.25645 | -46.90788 | 2025-06-09 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbbb7958-b3b7-3e97-8459-748c14050392 | -7.01467 | -44.6127 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cf1d14d8-94fc-372b-9341-135ae615d61a | -10.25038 | -46.91301 | 2025-06-09 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93860684-fc51-38a9-91ce-b5634a649b8b | -8.96558 | -47.9683 | 2025-06-09 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 218c8935-9840-3070-bd72-78a19116b584 | -9.4142 | -48.43925 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae1a15ed-4940-3744-b5f0-d3a63e229b11 | -10.6475 | -44.48104 | 2025-06-09 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 66f96942-3fc7-3f27-ab2e-1d3de3a615c7 | -8.01456 | -46.78617 | 2025-06-09 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e714683b-50f9-392f-8d7e-dc246932b185 | -6.22318 | -48.53864 | 2025-06-09 04:57:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f627b4d-b37f-3f0e-a05c-abcc54726fd2 | -4.48894 | -43.77696 | 2025-06-09 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| faa72dff-b548-3209-b6ca-596d70d68225 | -7.01015 | -44.60424 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cab8e48c-134d-3ef2-89ea-1b0fdb458f3f | -7.58783 | -45.99174 | 2025-06-09 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76071374-562d-3c8d-9862-fa0df1adea72 | -6.01349 | -45.77175 | 2025-06-09 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 454a9749-2f43-3aa2-899f-2bb7dfdcfe99 | -7.87121 | -47.89232 | 2025-06-09 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1cc7a17-03f2-3cdc-b65d-2517c63367f7 | -7.01363 | -44.62022 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d53aa90e-37ba-3dd3-8d7c-ae65cbb8b331 | -7.00865 | -44.61521 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9c6124ae-cd9c-3d5a-a435-7e522a84eeed | -7.01415 | -44.61647 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a8c61da2-fc4f-30ac-ad4d-609247f55c88 | -12.15788 | -57.72867 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12174696-2b7f-3e84-b0ff-6213ace95c3e | -10.8491 | -53.77623 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8f45c04d-9aca-3372-b27b-368a85c9f5f8 | -14.25019 | -52.4694 | 2025-06-09 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc20b7bb-f415-364f-86a7-4bc386fe1122 | -10.37033 | -57.50266 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0704d585-ae6b-38a2-878a-80c1c2510c1e | -10.74758 | -52.5096 | 2025-06-09 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65976bf4-ca86-3dfb-b047-f015465d9886 | -14.23891 | -45.47671 | 2025-06-09 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 289284c5-3339-33fe-8051-e3ada2d25ca6 | -14.24328 | -45.49004 | 2025-06-09 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce8a8580-d441-3a73-89c3-8c8fe72e40aa | -13.89256 | -54.66005 | 2025-06-09 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5630465b-5e48-3d92-b8da-db405f4940a9 | -11.78716 | -54.78118 | 2025-06-09 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a1bd8a6-2ff3-333e-8a92-ee36c3f3b377 | -14.14754 | -53.72364 | 2025-06-09 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da3320c5-67df-3d9c-abdb-06212924fa34 | -10.84518 | -53.77935 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 144e5757-4329-3b90-ac66-aaa81a65456f | -11.37793 | -56.56238 | 2025-06-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24c935f3-90bb-375e-a0f4-4279fbeeb104 | -11.37575 | -56.55466 | 2025-06-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c107692-bdcd-387b-b28f-b97c3ccaed58 | -11.37125 | -56.5613 | 2025-06-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6249aff3-5110-3a83-be3a-4ba3562033fd | -11.36734 | -56.56434 | 2025-06-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 376b6b57-910e-3b6b-8ca1-1bf5837f995e | -12.351 | -57.43118 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 845ae93c-ad59-3e58-aa3d-9dd8fa432cf0 | -11.78384 | -54.78065 | 2025-06-09 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9db93e8-d5a1-39a0-8aad-0c9d1d414887 | -11.12162 | -54.64317 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f544773e-5702-3ede-99e5-63e58fb4852c | -14.25388 | -52.46989 | 2025-06-09 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc1450dd-4298-36a3-9af7-b60a9f5d3737 | -13.02102 | -47.86835 | 2025-06-09 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f34eedb5-6675-351f-85a6-b8b1fec868a4 | -14.24376 | -45.48583 | 2025-06-09 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94b277df-1adb-3bc6-b2cc-75d2c33e19bd | -12.3688 | -57.40744 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76acb965-5361-371a-bdbf-92493ac2c286 | -11.12548 | -54.64016 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0636f6dd-1c98-3653-bcaf-61dbf4fbb296 | -12.15724 | -57.7325 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbd338fd-71d7-3bea-b37e-fca75a1f8fc7 | -9.92837 | -59.93345 | 2025-06-09 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98251539-ec32-32b5-a023-3c1d6b761825 | -10.36687 | -57.50209 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b15c2f48-51d2-3f8a-a462-d35321402ea7 | -11.36792 | -56.56075 | 2025-06-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95273473-2690-3372-a11e-5690b9316e24 | -10.85083 | -53.78766 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73d50fc7-9230-342b-ba7d-f420a0584d39 | -11.30198 | -54.70815 | 2025-06-09 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 463b251e-9143-3fa2-81c2-d37f5ede999c | -14.2528 | -52.47278 | 2025-06-09 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdc5fc1c-98e6-34a7-92fa-e6eba1421dca | -14.24423 | -45.48161 | 2025-06-09 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e1f0732-e53e-36b2-afa0-50e34aa024b5 | -13.02167 | -47.86297 | 2025-06-09 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7c0926e-842b-396a-a129-d8573aa54355 | -14.03402 | -55.13821 | 2025-06-09 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1277fcb9-7578-351d-9ffb-29233f3ca0e2 | -11.3685 | -56.55716 | 2025-06-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eddc035-7753-3434-b71b-192d873e66c0 | -12.2117 | -49.63733 | 2025-06-09 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ecb6694-61f7-30db-93b8-0c133e343a80 | -12.36541 | -57.40688 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 369944bf-3942-394a-b418-7ab6d5cfcf4e | -11.37851 | -56.5588 | 2025-06-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e12b59c-0134-386d-9433-53a0e9d7c969 | -15.84093 | -50.88883 | 2025-06-09 04:59:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84d58175-6f8f-347e-b9ed-87066a49c9cc | -10.29735 | -57.13238 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f4c7fbf-2b97-3c69-b410-bdfa3521db18 | -12.3648 | -57.41061 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d510bd7-920e-3fac-a778-fae1e2eabd6b | -14.68623 | -54.34602 | 2025-06-09 04:59:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cf20f21-7bc3-3619-b6fc-22d4dc2b4c70 | -11.9128 | -54.82675 | 2025-06-09 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61fb954e-7539-3d12-8489-d95a66155269 | -14.25219 | -52.47725 | 2025-06-09 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6231e970-0150-3dc0-bbca-726bd599c6e4 | -10.36751 | -57.49823 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 331b4c55-9670-37af-b50a-2c314699705a | -12.37158 | -57.41175 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b71a860-19d5-31ad-b69e-ed57eaec6597 | -10.37096 | -57.4988 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4be5e028-6413-3cf4-93a2-9d064bf8148f | -14.24956 | -45.48645 | 2025-06-09 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0271ed79-910f-3e43-80a7-b3db598a746f | -12.88359 | -61.6442 | 2025-06-09 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54df0ceb-8679-37d0-8f87-afef696d2da3 | -12.89035 | -62.09485 | 2025-06-09 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b4f3a66-c9b0-3bb9-a719-036ba0b164f3 | -11.91611 | -54.82728 | 2025-06-09 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c24bd520-ca9f-35e5-bd37-ceb36f8de8b4 | -11.38576 | -56.5563 | 2025-06-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcc2992b-0e04-3220-a19b-e40c6fd18313 | -13.02255 | -47.86832 | 2025-06-09 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18262536-760c-374d-9086-b3409409a14f | -10.84856 | -53.77987 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f28c3782-1084-3353-9487-b8c585e675f0 | -9.92869 | -59.93675 | 2025-06-09 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 770436bb-7d7d-320e-a0cf-1400bb6360f8 | -11.12494 | -54.64368 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b64e1663-786d-38f2-ae9a-70d39cbe74be | -16.68454 | -43.88494 | 2025-06-09 04:59:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 17dced57-5482-36e0-99cc-44d328eca078 | -14.49937 | -43.80898 | 2025-06-09 04:59:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 519e0fc0-d3c4-3bbf-80bb-f5f70c351d08 | -12.35221 | -57.42374 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0eaf5888-4807-34b5-9575-4f37715d7c51 | -10.8553 | -53.78091 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4598437d-4e72-3d1b-ab50-e5727aadf6fd | -12.3728 | -57.40428 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a6839b1-5e7c-31d4-beff-45e45618504b | -11.0798 | -55.06789 | 2025-06-09 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e88fb5e0-2db7-3ea1-a851-550a743812ee | -14.68679 | -54.34228 | 2025-06-09 04:59:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70ca14f6-c2f5-38fe-b9a3-e9cf4c0145d6 | -12.52685 | -58.3467 | 2025-06-09 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb910805-a7c8-3853-a721-967988faa43a | -11.70792 | -54.4996 | 2025-06-09 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 376e5e76-11cc-3051-b70e-52c7ba78650c | -10.84182 | -53.77882 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f214c320-9644-3764-90fd-1a6e8c6f886f | -12.53036 | -58.34729 | 2025-06-09 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df566d38-4273-3190-9fba-de8bedcb06e6 | -10.85248 | -53.77676 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 486c4a50-0234-3800-a968-ea98d11fab36 | -12.52618 | -58.3507 | 2025-06-09 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7620025-820b-33a6-b5fd-d47ac3686ff1 | -12.02595 | -57.08942 | 2025-06-09 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e18b898-ee4d-3d8f-b178-36742a7995a4 | -10.85192 | -53.7804 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a513a775-f61e-365a-afd9-5b7def504305 | -12.20267 | -54.26343 | 2025-06-09 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba6ece53-b533-3573-a1c6-2f1f8f5a3b97 | -14.24908 | -45.4907 | 2025-06-09 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4390e63-c07d-39a8-adb8-15b550941db9 | -12.355 | -57.42802 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2359086-39c8-3df4-a49d-4c1106027a41 | -11.38242 | -56.55575 | 2025-06-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 044af89f-c5d5-3c33-88d3-e515ba16409d | -13.50958 | -47.86462 | 2025-06-09 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52948557-ffe8-3e77-ba2a-bd8bbe3d64d4 | -10.3697 | -57.50651 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6df620aa-734e-3527-8817-302d1d823d72 | -10.4935 | -53.66257 | 2025-06-09 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcba6c30-d1cf-3387-8ed9-314a3ced19ce | -10.84801 | -53.7835 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ad97ac0c-67a5-38e8-b7f8-0c9b45ae63e3 | -11.40926 | -54.7177 | 2025-06-09 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cf98cd0-b008-36d3-8380-eaf7cd845307 | -12.35439 | -57.43176 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 103c91cb-a604-3771-b9dc-541d21349131 | -13.01838 | -47.86226 | 2025-06-09 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README7.md)
