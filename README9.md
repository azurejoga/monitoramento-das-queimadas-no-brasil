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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a1dd99a-b431-3669-bbad-57ded2e1a3f9 | -8.4778 | -57.613098 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b730aeb7-ebb1-3fb6-89ec-d8abc64b2994 | -6.6508 | -59.921299 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d29c8165-ffb0-37c9-b9ee-239f89302d07 | -2.4139 | -58.260899 | 2026-09-22 00:57:00 | METOP-B | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 301839bf-b99e-34c1-8e5a-60237d63e8ce | -6.1608 | -57.717499 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3e72a27-96d3-3f58-ae16-2c1b7b149a1c | -6.0392 | -57.814301 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35244c26-8dd3-3044-8225-21d290dda79d | -6.3042 | -59.938702 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1d35b58-3424-36dd-bf3e-aa6f1daf2228 | -3.3963 | -59.577099 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a6e2562-df1e-348e-87d8-099e85964d62 | 2.3242 | -60.9142 | 2026-09-22 00:57:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 800c3b65-8713-3e61-b7d6-966aa06bd3de | -5.9119 | -55.704601 | 2026-09-22 00:57:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef954446-3de6-3927-b982-f328e685f8bb | -12.7888 | -54.037102 | 2026-09-22 00:57:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e372fe6f-9e35-370b-bd48-c8194556552c | -9.296 | -58.909901 | 2026-09-22 00:57:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a38331f4-1c33-3385-9765-c18ad51d4869 | -9.5686 | -66.018799 | 2026-09-22 00:57:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 265bf4c3-41c2-3240-a6c3-4ad7cf58a091 | -3.4673 | -59.527199 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27c5fc6d-a96c-348f-a332-953c98dff928 | -8.6175 | -54.622002 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e24413d5-61a9-3627-a9de-1484bdefc309 | -6.7438 | -59.070801 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1715966-7343-30ae-9ffb-36a58a0068c4 | -3.4232 | -61.320202 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 190b3665-297b-3e09-8863-5f3c679633b9 | -3.9177 | -60.549099 | 2026-09-22 00:57:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34a5e14c-a336-3ade-b853-c5e26812b514 | -6.0913 | -57.684502 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50dd80fa-67a6-31cd-9295-26d4310ec28e | -11.3147 | -51.366798 | 2026-09-22 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fc8a6bda-ecbc-3531-bef4-bb62bccc2b37 | -7.6978 | -61.5354 | 2026-09-22 00:57:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa2ff776-e01e-3847-9414-bbe46eef7da6 | 1.0818 | -60.672501 | 2026-09-22 00:57:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5cfeb01a-e5fa-3bee-affa-725ad176e7c9 | -8.2497 | -55.272202 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8664937-b0c4-3712-b3e3-891d624d0a3c | -6.0935 | -57.693901 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be680441-cd5b-3469-9ae1-174d91bcaa41 | -4.404 | -55.245701 | 2026-09-22 00:57:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c7658d8-0ff1-3ec6-a7e1-fde97997b9e0 | -9.5566 | -66.010498 | 2026-09-22 00:57:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 42af3681-7b56-3751-9bb3-95ff47bedd93 | -9.9444 | -60.210602 | 2026-09-22 00:57:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3afe9faf-6e4e-3705-8160-09b33f9a70ae | -8.7937 | -69.007301 | 2026-09-22 00:57:00 | METOP-B | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 8873f26a-93ff-39ec-81b9-edad5923c87b | -6.6905 | -60.004501 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1bce56e9-5cba-3bba-940b-b04faf949375 | 0.1745 | -60.4958 | 2026-09-22 00:57:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b9c5ffd7-80e8-3c7a-93d1-57fad18c7df4 | -3.1695 | -58.591 | 2026-09-22 00:57:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4df56a0e-5b14-3def-a727-b7d9db8822bd | -6.3487 | -57.771198 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba5670c4-be1a-3e1c-a12f-bfd516897641 | -10.5949 | -53.9809 | 2026-09-22 00:57:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 860434ed-0196-3f53-a9af-90e5bf5cebcb | 0.7963 | -59.202599 | 2026-09-22 00:57:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f5392295-3e09-30ea-9e22-29fd477c41b1 | 0.1763 | -60.4879 | 2026-09-22 00:57:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 72bad7db-6796-3df4-bfa8-c905ef073ea3 | -5.8154 | -57.738998 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac63e432-29c2-3df2-b1b8-bb30cc465c5b | -6.3369 | -59.946701 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69c4e1be-2e0e-3446-ae59-b170ce20a7f5 | -6.6474 | -59.906601 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a4b2f7b-3318-33dc-8b20-37e495cc91f2 | -3.7116 | -60.5495 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 215cbbb1-0fc7-34af-b63d-85d6f4a3d230 | -9.5522 | -65.9897 | 2026-09-22 00:57:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 377ff212-e95b-37f7-8e8c-62d1465de9bb | -6.2467 | -57.7757 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9e32c6e-5827-368d-a54b-f147e9ad4c24 | 0.7984 | -59.193199 | 2026-09-22 00:57:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7ed467c2-81f9-3113-8ba2-ad389a86407e | -2.4086 | -58.282398 | 2026-09-22 00:57:00 | METOP-B | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7bbee38-02af-3598-8de2-3216d7447521 | -9.1416 | -67.932701 | 2026-09-22 00:57:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b11e929b-ec02-3520-9ffc-efbf1f19d78b | -6.9117 | -59.6203 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7dcc73d6-7add-340b-aa75-c04ad8bb620f | -7.5784 | -57.693802 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30dc2d48-b627-3e3b-82a7-8068383effca | -5.4532 | -60.140099 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10d56316-b761-3b4f-a226-df7b9240d479 | -2.8543 | -57.805698 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 40495db3-4895-31e4-92fb-7cb9c9207e14 | -3.7183 | -60.578701 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c937eab-ca18-3f0b-aac5-8a55583b0d16 | -6.4646 | -59.963799 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3c07502-a9aa-37bd-b805-5e269aac8a0b | -12.8148 | -54.0168 | 2026-09-22 00:57:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1884800b-ef8b-3869-b2c6-30e6c07e91bb | -6.4548 | -59.966099 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f3bf146-6dc7-311a-91c2-ee584ec1b09a | -2.6028 | -59.7565 | 2026-09-22 00:57:00 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46b71584-985a-3c1a-ad12-4274e7f66258 | -2.9945 | -60.795101 | 2026-09-22 00:57:00 | METOP-B | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94bbdb26-d759-3476-954e-1e0163815b77 | -8.2586 | -55.309101 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfb78261-3419-39d5-b46d-d0325ec1ada3 | -3.1087 | -60.708199 | 2026-09-22 00:57:00 | METOP-B | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| caea6c99-46dc-3859-8ce5-277b4bdaace7 | -2.7861 | -59.882301 | 2026-09-22 00:57:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90d19527-991f-3391-9818-87c4b5d50962 | -3.3957 | -61.289501 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f222143c-4f7e-3a2a-b19a-840ab71537e2 | -6.4433 | -59.960999 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ceae7271-320c-3503-a123-cc615ac8ea96 | -8.2564 | -55.257401 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50b5dffb-40fa-3e72-b53a-dc6a58cdcf5f | -1.9295 | -56.607601 | 2026-09-22 00:57:00 | METOP-B | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf36c8b7-7c20-3fc3-bc0e-e7f1c264e3df | -3.4722 | -59.593601 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe2d681f-50cb-385f-85b4-9a5866fbdd42 | -5.9314 | -59.9772 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c230ff07-b2b5-338b-8b76-29b770b73d40 | -3.5202 | -59.937901 | 2026-09-22 00:57:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ecc57efe-a713-3651-b453-fe2ddf0ecbeb | -11.3223 | -54.040901 | 2026-09-22 00:57:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b59cfac-6eae-3eec-9a1d-ad7172bc5967 | -4.0897 | -62.077 | 2026-09-22 00:57:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa9aa160-8218-3c60-bd1a-4d6268dc7bbb | -6.4244 | -55.6087 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2df65931-cb32-327c-937e-83f9df06810b | -6.0967 | -57.663502 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f68a5f6-d3e7-33bf-b5bc-82d48b4a6e0a | -3.3581 | -61.305302 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb0ff55-1dde-301b-8e60-70ace568725a | -6.3086 | -57.731998 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 083493a2-afbb-3d29-9ae5-87692cd97a94 | -3.061 | -61.268398 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf16b9fb-4b8c-310c-b438-97133dc0264d | -6.1389 | -59.937599 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88671c13-f160-3495-9252-cd6084181e09 | -3.7005 | -60.636299 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79f1a2bf-4d1c-3a44-bfe8-c2d5c6d734b1 | -3.642 | -58.764198 | 2026-09-22 00:57:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd3ca4b8-1ea4-3cd2-bb12-532a359b7479 | -3.0642 | -61.282501 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b179c08c-9317-31c3-80ce-cd4227a7edc4 | -3.2974 | -57.8526 | 2026-09-22 00:57:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46c509ff-6851-315a-8107-02dfeb65c7fa | -3.0528 | -61.277699 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3225e822-4531-3d8d-b873-30e3d2767ca3 | -9.9451 | -53.982101 | 2026-09-22 00:57:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5802a72c-33e2-3a3d-8f23-61c7e0bfaeab | 1.5445 | -55.745899 | 2026-09-22 00:57:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56e92f46-514d-39c1-a26c-5d9d1c1651ee | -3.1922 | -61.120098 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea6f843c-dc10-3549-ad84-a8e5bb0c5aa3 | -3.395 | -61.0597 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0fb70765-ea29-3d76-b9ad-6b86c5eef78c | -3.6021 | -60.566502 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8aec4c9d-37e0-34b8-9708-5d2f39e7e6c2 | -3.5531 | -59.946602 | 2026-09-22 00:57:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e82a3d9-c395-3db0-9f3a-68d375152d6e | -10.6081 | -53.992199 | 2026-09-22 00:57:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce6db396-7c16-36f4-9526-246bbc9fa46e | -3.0464 | -61.2495 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10162e37-f5b5-3a00-8e53-b814b6b0ac43 | -6.6214 | -59.928101 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3672927-b26c-3dd5-b0b9-f76d60f0776d | -6.1836 | -57.770901 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44930373-1dcb-3ad1-abdb-82e6fbb9699e | -8.8218 | -50.480499 | 2026-09-22 00:57:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fe20755-1f79-3b54-9dbb-50c53d370dd4 | -6.1355 | -59.922901 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f1a466e8-2b7d-35e4-98d1-3bddc73e73c4 | -3.3833 | -59.520802 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12df1cb6-e66a-337d-92f2-e51acbe51efe | -6.8633 | -59.9035 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e513e420-48b5-3d52-8d94-f6ae776633c0 | -3.048 | -61.2565 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b2cd25c-6a8e-31b6-8d46-33164643637c | -3.6872 | -60.577999 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84f6a98c-9d6d-3429-bb07-c0afdcf9c18b | -5.4192 | -60.217098 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6aa6be5b-bb13-3f64-850a-f83bedd0d019 | -10.4495 | -51.288799 | 2026-09-22 00:57:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c48b084-b7e5-34ba-ad7c-edac7ef2ca11 | -3.3981 | -59.585098 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88385a53-a2a8-3436-9bf3-21db49d21115 | -9.2943 | -58.902302 | 2026-09-22 00:57:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37446d53-3cba-354f-91e1-0fa44f31bab0 | -6.0511 | -57.821301 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9deb066e-0691-3dc2-8946-060ea80b1b2a | -6.7042 | -58.988499 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 375b229d-6cc4-3845-a5aa-0750add38215 | -8.2527 | -55.2845 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8ed8a4a-12d0-3d85-841d-1bdc8c088ce0 | -12.776 | -54.026901 | 2026-09-22 00:57:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
