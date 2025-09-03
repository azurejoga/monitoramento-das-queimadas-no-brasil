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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a582a329-3014-3f5d-a24e-5e84d5f807b8 | -8.3849 | -48.30858 | 2025-09-03 00:50:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 1683fa50-9afe-3feb-9244-d609eb712d56 | -11.21707 | -55.06839 | 2025-09-03 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b3e167f1-b767-34cb-9709-ba16f7c07641 | -7.71565 | -48.7611 | 2025-09-03 00:50:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 3d059323-22b4-3605-b654-87a851c00e28 | -10.49225 | -53.63924 | 2025-09-03 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 480b40d9-7e5b-3390-8664-b1317201973b | -12.4966 | -53.83641 | 2025-09-03 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 6dd37a86-2f93-364f-aa66-1381fc8b0411 | -10.91623 | -50.84402 | 2025-09-03 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 076d97a4-75e6-3727-87f5-91467f205cf2 | -15.58054 | -48.31812 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8ce8ec1e-a781-39fe-835b-9ee541c5b06d | -8.37103 | -52.54361 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fc00f3aa-a4ec-394d-9a14-4b38495959a6 | -12.18018 | -53.88853 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| e024ae9a-9517-3317-a183-1118a1885158 | -10.96636 | -50.93467 | 2025-09-03 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8183e6bf-f260-3a7f-a832-0b9850a8fb40 | -14.57873 | -54.54884 | 2025-09-03 00:50:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 270df5a6-5a38-314b-9864-75a07277e73f | -15.54979 | -48.31077 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 276810ed-4b4d-3f9f-b3b8-9eaecc8ea408 | -12.64593 | -57.01093 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 52aa8263-d085-3901-bad2-23d5ec879916 | -9.3404 | -55.22889 | 2025-09-03 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 78a2d96a-7abd-3d59-b290-291d22147ea3 | -14.34765 | -52.81376 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 50c421c1-888a-3d82-9dbb-a65f03314084 | -11.68973 | -52.14744 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 027b0496-e557-352b-b0bc-c352ae5f42da | -12.48744 | -47.47929 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| c034223a-f9d2-3ff6-a54e-87f7a6e5660d | -18.14201 | -51.74341 | 2025-09-03 00:50:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 924582c5-7e99-31a8-a1e6-7a701f6c5d15 | -13.00439 | -48.09484 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| adccb244-dcb4-3f31-84c2-252577b10f05 | -12.84296 | -48.05235 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| b21d2fac-6ad2-3eee-9980-d27d54fa3fde | -12.83276 | -48.054 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8ea2c384-0e5c-3a06-91e4-b1d2ea95829e | -11.6219 | -52.06301 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 71d38635-f8d2-34ca-a08b-58e8137b741d | -11.8892 | -50.62011 | 2025-09-03 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6b340bbd-cb61-32be-b438-b07256ec5192 | -11.60425 | -52.06559 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| e63ac7a6-6e82-35e4-bb57-fa754e67522e | -10.91491 | -50.83469 | 2025-09-03 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1c8923f8-f05e-3b1d-a313-65592062922e | -7.72185 | -50.2528 | 2025-09-03 00:50:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 520ae54d-91ab-3f6b-8f1a-9f34436a47fc | -11.47657 | -54.61878 | 2025-09-03 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5dabd18a-c2cc-32d2-9c98-c87220c0094d | -12.88399 | -48.04707 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 47fec0c5-a147-39d5-9b55-4edd3bc36718 | -7.90188 | -46.44912 | 2025-09-03 00:50:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| bd6c7a65-d3ec-391e-b0d6-903806eabdb0 | -8.05034 | -52.3547 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bde819d7-0c4b-339c-b4c9-989e7cf05183 | -11.59527 | -52.13087 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| e51b0a6e-52e1-398d-bd80-c5417dc1b10c | -11.07915 | -52.00551 | 2025-09-03 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d514fcca-dd52-30e6-87aa-089d35f9eb52 | -7.71375 | -48.74837 | 2025-09-03 00:50:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 4ec79811-222b-3cdb-aef7-726a6f50dac8 | -10.46362 | -53.62987 | 2025-09-03 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 64e4c64e-99a1-3585-a86d-ba6b90382403 | -15.89768 | -48.17227 | 2025-09-03 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 0a230cff-cabd-3559-883c-4fef8212b4ee | -12.99425 | -48.09663 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9df62dec-3239-3b0a-a7a3-677f3ac37a92 | -7.93009 | -46.46415 | 2025-09-03 00:50:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 763c1efa-60b0-3932-9520-2939edb7f41e | -12.84944 | -48.02653 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 8079561c-0862-38a3-8b88-3aedd36feda8 | -8.06041 | -52.36235 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8a7c421c-59e7-3547-a3eb-cf5944a5ea48 | -17.53859 | -47.58487 | 2025-09-03 00:50:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d164358c-f85b-363a-897e-0ca7d073ff1b | -14.99896 | -50.18744 | 2025-09-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 45eab511-3f7e-3466-94eb-2e0f255516d0 | -10.45738 | -54.78095 | 2025-09-03 00:50:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 88c8915d-e268-3673-af19-0a2ad12dbd08 | -11.39064 | -43.62031 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 7011821a-887b-34de-8a0b-0dce3e70af56 | -10.53324 | -50.42505 | 2025-09-03 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| bca5a713-ff75-337c-ac72-da5bcb53c6e7 | -10.4935 | -53.64867 | 2025-09-03 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d775b7fc-f858-30aa-bfd7-e5403d82e129 | -9.63095 | -47.87043 | 2025-09-03 00:50:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bbf6d586-7fd9-3e35-8b19-f21ea644bba1 | -10.95296 | -48.15151 | 2025-09-03 00:50:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 51f83e0b-419d-3e7c-8479-615f25b110b3 | -15.11512 | -48.16087 | 2025-09-03 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9ea04d3a-a37c-3e62-bf67-31f891090e55 | -11.64698 | -52.1142 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 36a60348-5573-30ed-acc1-7c7920de03af | -14.62936 | -48.93369 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 168e6d67-216e-390c-9e5a-d8218b0cb13d | -12.48729 | -53.83772 | 2025-09-03 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 67e3ec6a-5ff7-3a3a-9b59-338fb4950019 | -8.88264 | -45.83175 | 2025-09-03 00:50:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 7cbeaab1-5444-3d1a-bf3f-a3b0c3f37465 | -8.88989 | -45.80307 | 2025-09-03 00:50:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 76ef5402-352b-31f0-8d32-3300cbce52f8 | -9.5195 | -48.90311 | 2025-09-03 00:50:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f80c25d2-4527-37c5-95be-3d18c1bd8ba4 | -9.50758 | -48.89268 | 2025-09-03 00:50:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2cf60d02-3057-334e-85a7-82db61d4d2ca | -15.02623 | -50.05865 | 2025-09-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6e81a221-dc7f-334f-8d82-2ce7932e7c28 | -12.96014 | -48.0778 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6e6d83ed-f1df-33eb-94f3-550758c845e2 | -12.80305 | -48.05191 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 39556189-c9c8-3c5b-93cb-f8ee5eb4e7f3 | -11.58273 | -52.10527 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b0776260-57d1-375e-a732-d4d567db1e0c | -8.35094 | -52.52843 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a7ca0edc-96e6-3cd0-91a4-b8837c69140a | -11.86566 | -51.55454 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f419379e-3ea2-384a-a102-5a726a1ca848 | -12.61104 | -57.01508 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f05327ed-f02e-330c-9ae5-a6fb62356320 | -11.60673 | -52.0835 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| c28fed53-3b26-389e-879b-feb6a3aac743 | -12.94129 | -56.98814 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| db9ba2a5-dd86-36bb-91e3-e3471747e454 | -8.36329 | -48.31176 | 2025-09-03 00:50:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| f6f70741-26a5-3cad-b056-c05a65c381ff | -11.21856 | -55.07974 | 2025-09-03 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 88aefd90-bf9e-33e3-86a7-6df70417ad3c | -12.98478 | -54.76704 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8245cd1b-1a48-3dcb-90a3-a1dc4598fd98 | -9.70718 | -48.30414 | 2025-09-03 00:50:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d4574ce3-0973-3a6c-a717-be2bafb66956 | -15.09032 | -48.12998 | 2025-09-03 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ae87bd60-18f1-3f96-a4fe-3cf633209476 | -11.04639 | -45.39986 | 2025-09-03 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 895cf1a4-e858-3c1e-863d-678b1265c861 | -11.60162 | -52.11166 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 273.2 |
| f6be12dd-0361-37c4-b2d7-516cfaa4047e | -8.19204 | -49.55481 | 2025-09-03 00:50:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f538fb37-38c8-3383-8afd-ea002eaa9910 | -6.83654 | -52.83973 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 6f37943b-8a70-3f5b-b052-9caffeb59f53 | -3.79449 | -49.43155 | 2025-09-03 00:52:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b15624f6-ca5f-33f3-93df-1c39a6f61604 | -8.14539 | -54.93831 | 2025-09-03 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1f9da96c-9605-39ad-93c8-9afd718fad43 | -3.37793 | -47.17326 | 2025-09-03 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 601399f7-e1ac-3a93-8505-e9febde3ffd7 | -5.9327 | -57.72564 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| de0f9ca8-d516-3d25-aba4-772220157490 | -5.60737 | -45.00361 | 2025-09-03 00:52:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 182.8 |
| d94e4de9-9caa-3031-bc85-951f51738470 | -5.86918 | -57.76886 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 311.9 |
| 9e83ec35-6a6f-3115-b43d-af882096d791 | -4.14669 | -46.77703 | 2025-09-03 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| e926e13c-f8d0-349f-ac34-1939bb0fce06 | -2.94179 | -54.80057 | 2025-09-03 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| af8ceb62-269c-3956-8600-88d8b3813edc | -3.19611 | -49.10447 | 2025-09-03 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 77db8c56-a8a5-31ce-923c-db1cf971da95 | -5.87111 | -57.7832 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| bf3ffb5b-1d0a-3129-a78e-a8df87203878 | -5.93084 | -57.71152 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| e44d4593-624a-3f61-81c7-4ded8d1e1839 | -5.03246 | -49.2304 | 2025-09-03 00:52:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c16c2ef5-a5ef-3060-96cb-c4e92b98efba | -6.33592 | -58.17943 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 4b13825c-3f45-37cc-8361-f31a8cd4a812 | -3.80714 | -52.27005 | 2025-09-03 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 725e4424-b37d-30ee-bf2d-1e546d7f7395 | -2.14659 | -53.64989 | 2025-09-03 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f7e26c25-59c3-39e8-9024-2de1d928c481 | -6.3339 | -58.16378 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4603f67a-eed5-36c6-ab75-611ab8d60bde | -4.16293 | -46.79613 | 2025-09-03 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 953a0659-056a-39eb-b94c-bd88361dc33d | -5.48483 | -51.22716 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 94b7a5af-d783-377b-a9f7-a09f6eda3435 | -6.69368 | -48.40164 | 2025-09-03 00:52:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 0290af9c-4141-3831-9eb0-ca794e1d008a | -5.60711 | -44.99673 | 2025-09-03 00:52:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| ba7e62b4-afbe-3945-a62f-7fe384580ba3 | -2.90468 | -48.30003 | 2025-09-03 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 31e4ce89-6048-3b0c-9d0a-654c9524b7d7 | -6.98139 | -56.47118 | 2025-09-03 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4e1f5430-74ad-3893-ab6f-9a4cb4b2f27b | -5.61152 | -45.02407 | 2025-09-03 00:52:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 329.6 |
| b3be6982-5087-3db2-b5c7-6ed6c2b92079 | -6.46589 | -49.51588 | 2025-09-03 00:52:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0f588d01-7f1e-3ccc-aa51-6c4c7bb3b6c5 | -5.69543 | -45.94682 | 2025-09-03 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 057345ef-c5c4-3d7a-8af0-ee0b829e9f27 | -6.80765 | -52.82586 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 355d6f3e-073e-3a8a-b216-c65107a176e1 | -6.47231 | -53.40806 | 2025-09-03 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |


[Clique aqui para ver as próximas entradas](README15.md)
