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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 865a9cf9-121a-379c-b1e5-bc79ecf2bddc | -9.47204 | -60.49402 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66ca20bc-2703-3770-ae84-9a822eea72f5 | -9.39833 | -46.77974 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e596e55-f8b9-3337-9c12-62038c45a66c | -6.62065 | -53.37149 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e9ea9a2-a5a3-34f2-9d55-9544abe3d88b | -12.41741 | -47.80393 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0175143-086c-3efa-9e98-a3ed9cdf1aa6 | -12.64611 | -56.98083 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7c0b0f88-1785-3e49-bba1-198c434f5311 | -7.70474 | -45.15739 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 113bc81a-1e14-3cdf-9bed-524f9259fd5b | -8.47972 | -47.31686 | 2025-09-09 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c180eb68-8b63-33d0-a270-cee2efba3058 | -8.00561 | -46.34674 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b8c1216-ec8b-3c2b-a178-91254241a64c | -11.6992 | -45.60478 | 2025-09-09 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5bb456f-3952-3e08-ae61-f8d936f62325 | -11.60646 | -52.20161 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0088ca74-dd7c-393d-972d-0bc88d6e630d | -10.28473 | -48.81571 | 2025-09-09 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 266c2e5d-38a6-3320-a886-8c940f93638d | -11.42299 | -43.5854 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2be4662-618c-3676-bfb6-ca166d5d04a1 | -11.24719 | -49.4043 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb8444ba-df82-3190-b002-e3d2fd6e2340 | -13.80202 | -46.28912 | 2025-09-09 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b1a93180-7a91-3d98-9f81-3bd2fcb564c2 | -10.97635 | -45.11567 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e7f606a5-a664-3ba7-aca8-c1cb83938d35 | -13.7432 | -46.89694 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6f519c5-84f1-35f6-8acb-7aebfeb6376a | -9.21345 | -60.81505 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8286653f-f2ec-325d-b63d-38f7194bf381 | -14.2589 | -47.10287 | 2025-09-09 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4eb0f72c-f5d5-3a5d-a64f-a3a4984f01bb | -12.83735 | -52.94082 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1248afcd-b048-3021-98ad-a433649c4b75 | -8.15985 | -46.09021 | 2025-09-09 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91aad288-834a-3e1d-bd4a-3e603897dc89 | -10.33342 | -47.7321 | 2025-09-09 04:34:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 540f5b74-eb66-3ff8-acec-3f9379a2e77e | -13.03097 | -48.0268 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03176870-b609-3cc2-b8a0-1c300240f1ea | -10.1585 | -46.20459 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 667b712c-7504-3bca-b3c8-92c86e124528 | -13.80933 | -46.29 | 2025-09-09 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f981b42-7306-352f-938f-0c9e4fb2e106 | -12.62708 | -56.96964 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| acc0a220-1e2d-312d-9177-63db5a4681dd | -11.86443 | -50.94951 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 291b9afb-7c8e-3368-ac88-c291d58900e3 | -11.9485 | -46.6573 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5497d070-5832-36ac-95ad-197bc3baa23c | -7.56333 | -44.66283 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6b5cdf7-abb7-39e9-a3f1-935b3ded5267 | -13.47125 | -43.61588 | 2025-09-09 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 559dfcf0-04b0-3c2f-be54-5d83d35fecbf | -7.87624 | -46.25029 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa46ee63-6154-3636-ad1d-b2310c3e696b | -7.74238 | -50.75226 | 2025-09-09 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e74a7f79-db78-34cd-9910-824a2b07f48f | -9.48024 | -60.48512 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2baaec94-5eba-3eab-bd50-1c52e8aacf89 | -7.99932 | -46.34195 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c12071d-5249-3fa0-8aac-589dc3a21946 | -7.87224 | -46.25354 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e085483c-4881-302b-8db1-79969589e101 | -11.21822 | -55.00594 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4f74d35-c460-32b3-a313-7136a336f527 | -7.25302 | -44.81631 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 87f9c4a2-4663-3d46-9f21-b1062ce4fb55 | -14.13908 | -47.05695 | 2025-09-09 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a4b1b87-c98c-3e36-b2df-6d88323626ef | -14.60715 | -43.92637 | 2025-09-09 04:34:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33d834eb-ad0a-38dd-97a1-77966a8e89df | -13.18262 | -47.24625 | 2025-09-09 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73fd2e61-c749-315b-a254-5e83811f5f7b | -13.94246 | -48.23938 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d14e754c-8993-3c74-b1c9-002a51396f48 | -12.41594 | -47.80419 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f9ea314-2740-34fb-9793-6a70520fc42e | -9.45183 | -60.50874 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30604c91-059a-36be-8374-68223adc6440 | -12.86446 | -47.97513 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4a12a90-c299-3b8c-8341-8d32d18b1c64 | -12.9562 | -54.76289 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7afd6f1c-e860-37bd-a754-f32a5e6c19b5 | -6.39881 | -58.20082 | 2025-09-09 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3bb4ae19-7ec2-3bc8-b5d4-4db4fa24c278 | -8.12432 | -44.86824 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cee621d-9643-392d-a669-068fd5c15127 | -9.9478 | -60.13269 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ebf0ad47-6b92-30f5-9599-5731331a044e | -7.57504 | -44.6601 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37763dde-38d8-3637-898e-ccc2d270b309 | -13.9402 | -48.23148 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 86a6b413-40cb-33b5-ba1f-11ebfb830198 | -8.23338 | -49.54403 | 2025-09-09 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c838312-203c-313d-b57c-be823d375781 | -9.50584 | -48.26984 | 2025-09-09 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f0525ed-b8dc-3d60-a646-e60d1a279c22 | -8.05771 | -48.65785 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf4b97e4-3cd8-302d-ac63-0d959b8b5e08 | -14.1752 | -48.98919 | 2025-09-09 04:34:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c1289441-8f16-3594-afa0-bcb1a72eb8f5 | -8.85426 | -47.24665 | 2025-09-09 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f34bb03-2c36-3bd7-9d0f-783b519d16bd | -14.30745 | -44.88207 | 2025-09-09 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c4a72c9-51a2-3605-83e4-d20c67446023 | -9.71342 | -43.51677 | 2025-09-09 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab6396af-45bd-3098-a0b7-e823dcf858d0 | -11.28917 | -46.48752 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a45a6864-f552-3b16-9804-3624177aab77 | -8.76838 | -61.44212 | 2025-09-09 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8aa4bf8-cc21-3d06-b295-860999d182b5 | -12.6111 | -56.97723 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8958982-a445-3428-854d-7d4f44ca2eb0 | -7.39513 | -61.63337 | 2025-09-09 04:34:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19d1de2e-ab9f-3c4a-b30a-49a42680a721 | -6.27359 | -53.42439 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0fa830c-3954-3e1c-926c-cd0da8ed655c | -11.30782 | -46.50676 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c15b0c4b-0972-3e07-a60c-2fe56bfef3f5 | -8.65958 | -45.74963 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1997d4f0-84c5-3b14-81d1-ced7901df0f0 | -12.02861 | -51.08679 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45922e53-fe85-3f5c-88ba-e38e2fe8cb08 | -11.42508 | -43.6013 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9737daf3-1f47-3892-981c-0ea0b8e80344 | -11.96133 | -50.98056 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a3184da2-e732-313e-94ad-07d55684f7c6 | -13.83985 | -46.23322 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e95e6f0-cca6-36ed-9e5a-2ff735bc973f | -10.96766 | -46.80732 | 2025-09-09 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 567ac713-e443-3297-aa33-554e873ef683 | -9.55606 | -48.66699 | 2025-09-09 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a603f06-95ea-333d-a0d4-d0a99006b487 | -13.80262 | -46.2849 | 2025-09-09 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04eaf8e4-f8a6-3399-b516-9cb7069cfa64 | -7.56377 | -44.6652 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc5912b2-2deb-3238-8b82-9a072086d1f8 | -12.63019 | -56.96208 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e995894b-603c-3d42-b23b-1e34230d6949 | -7.67353 | -50.28913 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c857555-1d9e-3dc7-b08e-fa85d64cf30e | -13.7497 | -46.90198 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ceb856b9-f1d6-3a59-a751-4c5b918bbc36 | -11.65373 | -46.88432 | 2025-09-09 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7877fa8-c117-3d78-b258-ddc004b6d250 | -13.80994 | -46.28571 | 2025-09-09 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67cdeafa-93db-3a40-99b0-6cbc1fc58af8 | -9.48146 | -60.48861 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d02e663-12df-33a7-bdb8-a63d27023f20 | -13.04725 | -48.02115 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 999fa753-b565-3387-9c91-66f0c1816d2e | -11.95794 | -50.97999 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d79ca190-d875-3e46-8011-069523729cc0 | -8.48414 | -47.31031 | 2025-09-09 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 223f1ab6-6533-324f-af6e-813183c6344e | -13.94527 | -48.2436 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 353ebfdb-49a1-38cb-9415-50b06bc29f9a | -9.94513 | -60.14669 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e8fdc3dd-15e7-3fc1-83e4-d5cfc1bf86e4 | -8.05328 | -48.64296 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bc4cdfea-4405-3a16-a859-b85a399a9e02 | -7.7484 | -50.73727 | 2025-09-09 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c585ef06-43fd-3275-8ce1-f86591ebc385 | -8.44685 | -47.29013 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1afdcca4-cca3-31a1-ab88-8305cf7b5c1e | -11.97466 | -51.00564 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 228a65a5-f176-30db-863a-89b200d0d616 | -7.56445 | -44.6607 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d0dd19d-afe3-3d66-83bb-a7a537649a30 | -9.35213 | -46.50768 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96a75d75-1d50-3bc6-a05c-5c676ce37932 | -7.79732 | -46.09916 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc3e3bc9-faf6-31e9-b9b8-e0477bb9fc3a | -9.4533 | -46.44035 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82ed8bf7-9209-30c9-bed6-ff41dcb7337a | -14.32543 | -47.31458 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| deb76d4b-f6b2-3d05-8c1a-b13a7fe71978 | -13.0456 | -48.03221 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa83743e-67c5-32ec-81f0-ab062cca600e | -7.79155 | -46.09047 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3af709de-2d6c-301b-ba87-cda2211e943f | -11.79206 | -62.74398 | 2025-09-09 04:34:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0d162981-fec7-3c8b-9f84-d66c8480aa83 | -10.25125 | -48.33125 | 2025-09-09 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42a07b4f-4061-3f2b-a466-85c650051fd9 | -8.40689 | -49.0954 | 2025-09-09 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0efe3a6c-2b11-365e-bd57-e8324808d28e | -11.75761 | -47.12737 | 2025-09-09 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d71fc2ef-ba5e-36af-a193-541e72226044 | -12.90892 | -48.00047 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3df9fe5-6f96-3ade-bc84-a11aba468f6f | -11.15466 | -45.26621 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44be65f0-a6d6-35ad-8ca9-c36f2f0ad051 | -6.81851 | -51.87328 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README37.md)
