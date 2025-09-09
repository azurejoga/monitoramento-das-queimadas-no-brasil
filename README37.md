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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 818a9ca9-4c69-35b4-ade0-fc039a5eefa9 | -13.75028 | -46.89788 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 348bb0b8-9b30-38a6-a138-6dc3624e62c1 | -11.45889 | -49.27032 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab92b97d-0dfd-3784-bcfd-9850ec3ffbd6 | -7.56766 | -44.65897 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f35baeb4-a89a-3c8e-838a-d13d28a3e0f5 | -11.5988 | -52.20932 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9615fd62-ab93-3bf0-9515-8433742c7535 | -12.55603 | -49.12786 | 2025-09-09 04:34:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c142760e-a902-36e1-b297-5bdf87a81de3 | -11.6073 | -52.20226 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 446b6f5d-cd12-3087-b448-99ea16c9cf58 | -7.40229 | -61.63352 | 2025-09-09 04:34:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 921e08ea-a1ae-3068-b9b7-1f25dc2bda3a | -7.56511 | -44.6563 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7bc47b5d-6eb5-3e46-9d9f-b5633cd8d5a7 | -9.14133 | -45.5774 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2badabd0-5586-3940-99ed-1787aa157bb7 | -11.30876 | -50.4076 | 2025-09-09 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| db10297a-1634-3332-8cd1-8f8d9360e466 | -11.98461 | -51.0302 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66857078-6281-3932-a441-778dd4e290b5 | -7.72085 | -44.73861 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9dbc2b9c-d0b6-3834-b8f1-46f0e19faea0 | -9.34896 | -46.59572 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e446a95-7deb-3377-a2b5-901e67c2d91c | -9.81829 | -45.40311 | 2025-09-09 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adf89449-0ed9-3b31-8cfa-1b991976cd02 | -12.20095 | -53.88932 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ad775272-4f54-3be9-8f3b-9deeb46b8352 | -9.72919 | -46.79491 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24d05fbe-2f06-3402-84e7-ae5177b248a4 | -10.57195 | -52.00222 | 2025-09-09 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe2bee54-d639-34c5-bbe2-90009c25360f | -14.3809 | -44.6491 | 2025-09-09 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6f3f4d4-20e0-3550-ae65-6ec14af70da6 | -7.74454 | -50.76092 | 2025-09-09 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0499c62-8f68-3513-8a04-081862316b19 | -7.44289 | -44.9243 | 2025-09-09 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57667c01-ca4d-3200-8fa7-42d9c53ae569 | -11.98921 | -51.02333 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2597652f-5932-351f-8602-c96912346049 | -7.09718 | -50.76723 | 2025-09-09 04:34:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b03bf07-f790-3721-a264-c488b3114375 | -13.01271 | -54.82226 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f52805f-a91d-3878-a381-0df3d78a9501 | -7.66573 | -47.96453 | 2025-09-09 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 535366b4-9cef-3d10-8063-e7d640558e70 | -10.17412 | -46.22656 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fb52dbb-b8a5-372f-899a-be2d0a48600c | -13.4809 | -43.50778 | 2025-09-09 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f885a34e-26b1-3f3c-ab04-f0529aab1076 | -8.0489 | -48.64935 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 584b8249-4a74-37f6-b4f7-84ef25979c0e | -12.62431 | -56.98486 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64ffce89-d039-3afd-b9c1-908480d4600b | -7.79671 | -46.07954 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4978eea0-e9ee-3b5c-9c23-20e8220303e6 | -13.95541 | -48.24498 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a18ca7c5-c889-3c94-8c34-8198d632089c | -7.67757 | -50.2859 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f023894c-13ce-3ae1-ac88-3260426e0ef7 | -7.55899 | -44.66687 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f18082e7-0207-3312-baa0-230df9897ef7 | -12.82494 | -52.94756 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7dfab92-b64c-3fb1-adcc-ad9d90b1a33f | -11.15029 | -45.27005 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7ad7807-0966-32ad-bbc7-3d9a425dfb5e | -8.04049 | -48.63389 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 137f3587-2701-334d-90d3-e4677a0e983d | -8.42966 | -49.61958 | 2025-09-09 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2986eb6-1570-39e4-bb37-1f1d63b82e15 | -8.40799 | -49.08842 | 2025-09-09 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37dba53c-afe6-3f8e-9df2-ea5985af8500 | -7.78522 | -46.08557 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 445866c5-1d45-312b-b1ea-66ecc31795f4 | -10.97188 | -45.11223 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 8127ea74-829c-372b-82b5-6e17712706f9 | -13.04277 | -48.02809 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04b8f052-9ae9-320f-985d-57492536e7b9 | -11.31037 | -50.41899 | 2025-09-09 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 960ea2bc-17ed-3013-a07b-ac52c058c514 | -12.89139 | -47.97956 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18e4e6d9-b250-3e13-af0a-8836c6dae076 | -11.31244 | -46.53086 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32795289-f560-3f19-bdb7-483ed71b8a40 | -9.23691 | -57.0648 | 2025-09-09 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4ef2067-01d0-37f5-8f79-8693891d50b7 | -12.62902 | -56.98571 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb62e26a-ab09-3629-965c-651c5b21e916 | -11.18027 | -46.12075 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2f7fa37-7858-3ef3-b1ff-1d3655ed71f1 | -9.47153 | -48.77469 | 2025-09-09 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46793e41-ccb0-3950-9e52-ba3e9bc5df00 | -9.85442 | -47.79572 | 2025-09-09 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 86154558-0f27-368a-bcd1-2c836ba79aa8 | -6.93968 | -47.03165 | 2025-09-09 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43538e9b-1b20-3138-b8d4-a5036262f03b | -12.6289 | -56.95957 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64b954bf-8021-3de6-b6fe-ea60aafdddcf | -11.65026 | -46.88379 | 2025-09-09 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b3715b3-460b-3ac7-935e-c5d0bf522461 | -12.82642 | -52.93893 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| da6d78f3-37f7-3af3-ba98-08ee0ad5fd7c | -9.21881 | -60.82148 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d333716f-e550-374d-96f9-630c4a5eb0df | -12.90043 | -47.98826 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e967be9-e501-3142-afda-201979915d02 | -8.40744 | -49.09191 | 2025-09-09 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 685c9c34-f66e-3c87-8d08-d33d7277661b | -8.22102 | -44.76862 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 09e25acc-4cc5-34ad-992e-709e620d1366 | -6.86857 | -47.90894 | 2025-09-09 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e2ece944-8d64-3eec-a7aa-66e99823f7ca | -7.79326 | -46.07901 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40d9d5cf-0df3-3489-9620-51f094a297cc | -11.84012 | -46.75531 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32aec9dc-cbb3-392e-be01-62651654b9ce | -8.061 | -48.6584 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2e8fd3d-7e65-3661-818a-1765306e21db | -8.0593 | -48.62618 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dd05c90b-8dd2-36e1-8d8e-25bb8e9a1385 | -8.37307 | -45.00738 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69757ca2-3b49-3488-be23-2ef2f6d61101 | -11.20763 | -54.99175 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cbbd3022-31c9-3b04-b217-1e919cde0ac9 | -10.42039 | -59.60082 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a3522f5-b8d9-3987-93c9-e0f87bb2daf0 | -13.24633 | -51.78341 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0abcaf3e-0585-3859-8b45-35a10184003a | -11.37222 | -45.59273 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99958aee-964d-397f-85f3-8349cc4346a5 | -11.43496 | -43.68372 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09d42b8f-0a48-3020-9605-461d48b17899 | -13.79898 | -46.25837 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 287eb919-aa98-33ea-a1cf-2ee74ef713eb | -11.84538 | -46.76813 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2bf749e8-cae0-38a8-b995-e7f24a8f47b4 | -11.21539 | -54.99718 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 84038d4a-a719-33c9-a9c8-0d1a80fa2b53 | -11.82555 | -46.75752 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9600cf2a-97be-3fb9-a955-27ac8e5ba9f4 | -7.43746 | -49.26418 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49d3e135-4ea4-3225-97d2-03cbe1fd3010 | -8.44296 | -47.29315 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8196da8e-a031-30a5-8246-b1361ed8275b | -9.44024 | -46.73616 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1ed2724-4188-358c-8d7d-dedfb791a296 | -11.20201 | -54.99895 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90b84aad-5516-3543-9c16-7c2c0765fe62 | -13.04749 | -47.14714 | 2025-09-09 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9631592-f4f9-389a-9804-0a0884122991 | -7.43802 | -49.26065 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3626c70-237b-387f-bb92-27024e5fe1c7 | -13.3012 | -51.72945 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6ecaff4-06b7-3bc6-9b95-2ccbf981ae5e | -12.64706 | -56.97579 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aee8e3ef-b1b7-309e-8d76-efd0c8b21b94 | -10.24097 | -48.20029 | 2025-09-09 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a44f572d-083a-3071-88d8-fc17361fdd99 | -9.47619 | -60.48236 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7ab4f1b-41b4-36e0-9bee-2991ec95dbe3 | -9.88249 | -46.52317 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be3b7199-d457-33ff-8501-d8479314730b | -12.62638 | -56.98219 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac4c65be-3f33-34f0-8c22-b1e60187385f | -9.47926 | -60.49016 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eae42e8d-ac03-3975-981d-6526aa278b13 | -9.69788 | -46.7938 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe519bbd-b7b4-304f-9f0c-f5590487d011 | -10.15499 | -46.20403 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ac70261-b191-3449-a35a-e33d6473bd22 | -11.13234 | -46.35112 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ffca958-8e64-33d9-8846-7e80d34d325d | -10.34065 | -47.72961 | 2025-09-09 04:34:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e6b8b9f-4d77-333a-8dc0-291adcd0d335 | -12.93413 | -54.79289 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fba2b002-479a-3b77-8fbc-a7ec440f8e39 | -12.63673 | -56.97897 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6dc8df7b-5536-3257-b419-b82f981372eb | -11.31913 | -55.12194 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94128f56-aa0b-3e0c-95a1-c19a79294c35 | -12.19707 | -53.88862 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 87abf585-a727-3fd1-adf8-4de53ed44f8f | -7.86129 | -44.80228 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60841b51-c96e-3aea-9d88-0f3cfc8d27ae | -11.81159 | -46.76827 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c79562ff-3112-3a63-85f4-df4c7653d29e | -9.81435 | -47.76771 | 2025-09-09 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6a3b7eb-ead5-390e-b7a1-15c5c46f8515 | -12.64142 | -56.9799 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e847f048-50bb-3b4f-a158-6a1780590fbf | -13.8362 | -46.23271 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0a61ba6a-dc98-3af8-b458-471524589030 | -13.00981 | -54.81432 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9b818f8-1fc8-3dac-89c8-bd856970a77d | -12.62924 | -56.96709 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d92069d-61ce-3fdd-8050-c132ae609306 | -13.79225 | -46.27945 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README38.md)
