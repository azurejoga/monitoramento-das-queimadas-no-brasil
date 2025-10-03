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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a74c408-a2b3-3875-944c-8533b80618b8 | -9.63425 | -63.19991 | 2025-10-03 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 094dc2d9-f934-3987-8144-f8958aa14145 | -10.01387 | -50.24019 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9be4388a-c8df-3b53-a784-937e8f1b060d | -1.14703 | -54.19536 | 2025-10-03 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c46b7b4-9ec7-3809-9992-34bd65022ec1 | -10.25272 | -58.48232 | 2025-10-03 05:23:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad459af0-9e3a-3cda-8e31-7fd79d1923b9 | -3.68616 | -64.44816 | 2025-10-03 05:23:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8e33991-0b7d-34aa-884a-9731fa55c221 | -3.09482 | -47.02102 | 2025-10-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 40400384-2544-3870-87b3-422cf6648708 | -11.28026 | -57.87156 | 2025-10-03 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d64fbf73-b6ea-310d-a80a-d58d414ce5fa | -3.04854 | -51.10538 | 2025-10-03 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70b50f5f-f297-3269-82c5-92d8f47a81e9 | -5.78204 | -53.45758 | 2025-10-03 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59444d07-7bd8-3c06-964e-2e249c7302a0 | -9.99568 | -50.23768 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b0899f45-fca3-3753-b99e-c2afbbc5cab5 | -11.30863 | -47.83525 | 2025-10-03 05:23:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b35a3fc4-5516-3de8-8f84-7e7758d47106 | -12.93246 | -48.44189 | 2025-10-03 05:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b93db02-7c3c-37e0-bf46-e046036ed8d6 | -11.12358 | -47.87135 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| be8c395c-4432-3e0c-a28c-de2560acb364 | -10.96847 | -51.09271 | 2025-10-03 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 59b10856-2ffa-3ff1-a223-d858a976683a | -10.25588 | -61.92705 | 2025-10-03 05:23:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dfdb92e5-1353-3756-bff3-b4fde15d05aa | -2.92656 | -48.30207 | 2025-10-03 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8a1d4f38-050e-3291-8b6a-8a54cf610936 | -10.64276 | -56.76694 | 2025-10-03 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8992ebeb-a4af-314c-b396-c1fd6c3442be | -3.20974 | -54.74928 | 2025-10-03 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bc49740-4196-3974-829a-e2426559c27a | -10.89926 | -56.19491 | 2025-10-03 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29162a82-e1a8-31ef-9c03-b601ee2f0100 | -12.94554 | -48.44191 | 2025-10-03 05:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a74271f6-5bc6-3039-ba51-be95fa57bc81 | -10.00077 | -50.23353 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| f09db2e1-cf53-385f-9028-5c7cec6bbaa5 | -6.21055 | -55.66742 | 2025-10-03 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d022b56-f7fd-3e8e-b148-817b63c9057e | -9.99529 | -50.22807 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 307fd3e8-e728-3eca-b778-913b9e523759 | -10.97096 | -51.07178 | 2025-10-03 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ae8f6f02-31ee-3a62-9508-a9fd754eda52 | -9.30518 | -59.4257 | 2025-10-03 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1e9be7a-786d-3b68-8a80-76989a18f4fa | -10.58565 | -48.7121 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8b3fb4b-49fb-337e-a10d-f55941564070 | -10.10136 | -50.34396 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 33ab9ba2-16b1-3adf-9442-a38385a289d5 | -10.00285 | -50.22927 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 5831516f-e677-3b52-a863-9eeccef78340 | -6.7841 | -47.16127 | 2025-10-03 05:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 922341bc-21d8-3872-b413-b19ac9a4c236 | -9.91191 | -50.50294 | 2025-10-03 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3fa663c-9896-33e4-ade7-627a33680875 | -5.49183 | -52.13078 | 2025-10-03 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a6de81c-3ffa-3f20-bfee-c6516a336412 | -10.34308 | -54.19017 | 2025-10-03 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bc7cc6f-d7fd-3fc1-8174-8638d782b04e | -10.58956 | -48.70853 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bd310bb6-62bc-3cb2-b96e-33d548b2c302 | -9.63092 | -54.3102 | 2025-10-03 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a047006d-bab6-31e7-8c25-f206e5bc4cca | -9.9996 | -50.24275 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 775acec2-7682-3547-bbed-9dab8d1ea858 | -12.72166 | -48.57731 | 2025-10-03 05:23:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0251530b-18c8-3b95-b7f8-013749c3af8b | -9.62632 | -54.30957 | 2025-10-03 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78b4ad0c-57d9-3262-9ff7-6d9fa0bf73db | -9.99842 | -50.25199 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82a3956d-74c0-30b2-8e68-1558046247eb | -10.10739 | -50.34479 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db9ebcd4-8bad-3df9-b05f-02080b31dbb0 | -1.76338 | -54.17386 | 2025-10-03 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12e23e13-de56-39ab-a257-1752e5012502 | -10.6024 | -48.71536 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 72be325e-0f64-343b-8417-34565728d38b | -10.00801 | -50.22507 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| a7b61f03-1116-3fed-b2d9-730b728d2614 | -10.00502 | -50.26248 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61827f78-9300-3f31-ad0c-529d262e894d | -10.88492 | -53.77599 | 2025-10-03 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48059b53-4b3b-3da1-bb1c-291a33d38728 | -4.55669 | -50.46775 | 2025-10-03 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1eb1fc12-4808-39f9-a5ad-fc896c8e5324 | -5.14674 | -60.37221 | 2025-10-03 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac03157d-152d-3101-8b71-f8abe1d78978 | -3.56101 | -51.12804 | 2025-10-03 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 394d5574-3f0b-3c39-a773-4ebca61d2e37 | -10.60184 | -48.72029 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0fca67e5-2aea-3725-9cb2-a91411f3de36 | -4.65251 | -47.54605 | 2025-10-03 05:23:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 92926973-ce9e-3822-9c17-388173eaad20 | -4.89459 | -49.96347 | 2025-10-03 05:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9888dd60-91fc-3b6d-83ef-84a6ddc9a9fb | -10.11624 | -54.99689 | 2025-10-03 05:23:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06af9fa2-c5d6-37c7-84d6-d87d651b0d07 | -11.08978 | -47.87601 | 2025-10-03 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2e4f1026-bcc0-3d2a-b4b6-68edfc93010a | -10.96897 | -51.08851 | 2025-10-03 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0dc80f62-9d45-371d-8be2-98bb5c64647f | -10.44282 | -49.3582 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1caf9227-131d-314c-a62f-3d11f227f5ed | -10.00396 | -50.21998 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1bc7f382-6dd3-35f7-b1d6-1127b142e983 | -10.00566 | -50.24357 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c7b2de8a-9cbd-3a45-b909-80ff160e860c | -11.63204 | -47.98205 | 2025-10-03 05:23:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c6a08634-1fdf-37a0-8980-07ad23d24b42 | -7.24976 | -48.48028 | 2025-10-03 05:23:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a92f1a38-a988-3c2a-8368-e6d1b9748ac4 | -9.999 | -50.20985 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29819ef5-5d78-3390-b7a9-c5c812b98bb1 | -2.92305 | -48.31457 | 2025-10-03 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b74b8db-e5d2-3416-b0d4-15a1624297fd | -11.2974 | -47.83354 | 2025-10-03 05:23:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a9e95dd0-6ca5-3452-99df-579618f34baf | -5.49102 | -52.13655 | 2025-10-03 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b45be41-1952-3df7-b8df-84333e1a6609 | -11.29441 | -47.83335 | 2025-10-03 05:23:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 011e82da-58d1-3ff1-9de6-b146c98ad5c8 | -11.63124 | -47.98916 | 2025-10-03 05:23:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9a5fe958-cfd6-3f8f-943a-01132bd4f3a5 | -3.56142 | -51.12513 | 2025-10-03 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e83f8fd4-fc38-394b-9554-e60b6289da9c | -11.0953 | -47.86723 | 2025-10-03 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a0b28bd5-b32c-316b-83db-90b3f8e92760 | -10.96797 | -51.09689 | 2025-10-03 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6832390d-c02d-3be5-8d23-2dd1792f7d19 | -1.08011 | -53.68347 | 2025-10-03 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8087cbd-917f-370f-89d7-8a7264a836d4 | -9.87678 | -47.81166 | 2025-10-03 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4444693b-836e-3f6a-9712-ebb60d640481 | -10.00312 | -50.21499 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e9e851be-26be-36c3-857a-930c05da8079 | -9.13579 | -61.92875 | 2025-10-03 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e06b4b04-bbb5-336a-9531-697516b288f5 | -2.94221 | -51.27629 | 2025-10-03 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4259ee2-12e7-3d39-a32d-f9bea00e34c3 | -10.44347 | -49.35266 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fe310a2-01bb-389e-b8cc-5a039fb1d32b | -3.16957 | -48.60707 | 2025-10-03 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4a9b78e-9a05-3393-8dc4-841a7923efb7 | -3.09359 | -47.01228 | 2025-10-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 05369034-6013-3a84-9ff0-38510030a1cb | -3.19893 | -51.02973 | 2025-10-03 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 167d85fe-b5d0-3e29-bdfd-5aecb660eaa0 | -7.25629 | -48.48005 | 2025-10-03 05:23:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40ec7e96-af85-34ad-b456-a664fe3ab387 | -12.72134 | -48.58081 | 2025-10-03 05:23:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f66e7cd5-77cc-3e81-ae35-4c936a69596c | -10.97528 | -51.08515 | 2025-10-03 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f70b5d7f-3026-3466-93b6-b18966b959ca | -10.89463 | -56.19801 | 2025-10-03 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1aab59ee-d802-3463-ad1a-14f2c84f4b3a | -10.10684 | -50.34935 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f9427cda-6e05-3b5d-a144-1d2977b17e67 | -9.99127 | -50.22295 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0601d4ec-a02c-30af-815a-c88c99e2aa0e | -11.06266 | -47.79696 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b854a8af-ce5b-3961-98e9-9d51abf9078e | -10.00174 | -50.23853 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b2f60bee-9fdf-3c97-8f30-0b8114048a82 | -11.06899 | -47.80483 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e73da24-848b-348a-becf-db0f0f2ac2fe | -10.5863 | -48.70665 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20dd77b5-5b06-3e3d-bcd6-8e04f6ddeffa | -1.13198 | -54.21158 | 2025-10-03 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 692347fc-73bf-3006-9bd6-cafe9e9fabcd | -10.00341 | -50.22462 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 78f98787-874e-3dc8-a758-b511e50f3c91 | -11.06934 | -48.36166 | 2025-10-03 05:23:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 864d78bb-226f-324d-ae39-87faded58719 | -11.10522 | -47.84174 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 886552c3-7562-3041-b955-e1bfc8655e7b | -9.91788 | -50.50364 | 2025-10-03 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec9219b2-ba45-3aae-8e8d-f887eee2ab8d | -10.00195 | -50.22426 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 10599ba9-446c-3bec-804c-963799feabd6 | -10.5923 | -48.71344 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3427d28a-4192-38ec-a2f9-736b1e61c2c4 | -10.0033 | -50.26203 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 894b8f18-3093-377b-ac6a-d8195c590c9f | -10.00119 | -50.24314 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8bdf2b58-26a4-34a8-b72e-04cb0697c5ed | -12.93937 | -48.44351 | 2025-10-03 05:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eac85023-5e5d-3ac1-bc41-cc8ba79c30a0 | -9.88384 | -47.81209 | 2025-10-03 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1091bfdd-f4c3-3159-9652-a980eccc51b9 | -10.63881 | -56.76638 | 2025-10-03 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17fbd2bc-9e8b-3aa7-bccb-cf0976ba99a7 | -10.33959 | -48.18085 | 2025-10-03 05:23:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a99c022-9865-3c43-a7f1-864275ba6cfe | -11.53972 | -49.82595 | 2025-10-03 05:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README137.md)
