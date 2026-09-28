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

## Dados Diários - Página 178

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd440ad4-070e-3505-a0e6-3f32754d14be | -12.588 | -51.9617 | 2026-09-28 19:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 47c2c0d5-56b1-3581-9492-52c00518fdf6 | -11.6096 | -44.1382 | 2026-09-28 19:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 541.5 |
| a3399d2a-d3d6-3013-9773-7c4b3f3e28af | -9.9787 | -50.1198 | 2026-09-28 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| cd19d3dc-7235-35f9-8a19-0d20b0d2a029 | -10.2067 | -49.9898 | 2026-09-28 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 88597170-dff0-3c97-b671-c4c157bb2c77 | -11.1771 | -44.8064 | 2026-09-28 19:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 182.4 |
| d3120463-558d-3413-8a49-ba1ba141aff3 | -20.0484 | -48.0568 | 2026-09-28 19:00:00 | GOES-19 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 272.9 |
| e72270a4-4124-3574-b91a-21b5ac6d7d4a | -12.3857 | -50.2379 | 2026-09-28 19:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 92f151e7-aeb4-3165-b2f6-62ffbcbba920 | -12.8061 | -54.0048 | 2026-09-28 19:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| c78ff752-2769-38dc-b24a-af182c541c43 | -12.1359 | -50.3543 | 2026-09-28 19:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| a45e73f3-b581-35af-b802-7600c5d464dd | -9.1337 | -49.9656 | 2026-09-28 19:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| e9767a30-ea7a-3cb8-aba7-6e5ad5f30d54 | -7.2181 | -45.0797 | 2026-09-28 19:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 4f33eec5-dbd2-30fb-878a-1d31b18a0b2e | -12.7871 | -54.0069 | 2026-09-28 19:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 155.4 |
| e446d7ce-0e6d-39c8-b8f8-b581e822a0ce | -7.0675 | -55.4697 | 2026-09-28 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 189.9 |
| 3b3d1c0f-80a3-348a-892d-7010058e1779 | -8.6451 | -45.3489 | 2026-09-28 19:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 40544b27-b5cc-3d17-9d8e-e212489db842 | -13.3272 | -43.9285 | 2026-09-28 19:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 816f1bcf-7681-32bf-806d-eb03415e0207 | -12.6071 | -51.9595 | 2026-09-28 19:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| ff8b33ba-4068-3704-a379-d45e35aa2d23 | -11.1514 | -50.0818 | 2026-09-28 19:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 2c5488a6-55e6-3217-80c9-4334e0458dfe | -10.9637 | -43.8821 | 2026-09-28 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| d3075a9d-1296-3d02-8b17-3b1d62293f49 | -7.6851 | -54.7734 | 2026-09-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| c5ec36e3-f53b-37ed-87db-236eae5c8a53 | 1.8403 | -55.6046 | 2026-09-28 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| ba582cd7-35cb-3fc5-bb66-171597be42b7 | -9.6864 | -58.1258 | 2026-09-28 19:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 169.8 |
| 123fd5bd-9563-3985-8b85-0be6daf6b57e | -12.7677 | -54.0296 | 2026-09-28 19:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| a65b5ab4-3146-373b-8dfc-69321c0a7b60 | -8.9823 | -44.1633 | 2026-09-28 19:10:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| aa0a50e3-5cb2-3a91-a8e7-aa89f1308edb | 1.8587 | -55.5846 | 2026-09-28 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| dbb3d382-8b2b-3e83-9e7b-459e5a31d5dd | -7.7037 | -54.7722 | 2026-09-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| bff83bdc-9d54-3ef9-8c49-b062f9b2b0e9 | -14.7295 | -45.5527 | 2026-09-28 19:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 258.7 |
| afa3213c-94eb-3813-a23f-0fcb91f2341b | -9.0783 | -49.8853 | 2026-09-28 19:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 1203d29b-b1e7-3ddb-ab60-e7b4ce08a238 | -14.7289 | -45.576 | 2026-09-28 19:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 64d6cd85-cc00-3b29-85bd-b50aece3151a | -7.4974 | -55.0256 | 2026-09-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 170.3 |
| fc2d290c-a683-33bb-b0ba-d280437acf66 | -11.1327 | -50.0624 | 2026-09-28 19:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 96b9caa7-2cc2-39b8-ab63-cc835d793667 | -0.4889 | -49.1327 | 2026-09-28 19:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 98f36e19-82e9-32db-a4b1-90f353bdab28 | -7.9082 | -54.7597 | 2026-09-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| cb7aed90-5b3e-36e4-bd75-f4e2b38aed33 | -9.9266 | -60.7171 | 2026-09-28 19:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 265.0 |
| 0124f172-8974-3888-a7e2-250c92e9ed71 | -9.0971 | -49.8836 | 2026-09-28 19:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| c31a6020-1544-3c5a-a411-f509874f2823 | -10.6505 | -50.7123 | 2026-09-28 19:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 0613a584-3e7e-3275-aa26-e9e2f5bac6c2 | -10.7056 | -50.8341 | 2026-09-28 19:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 223.9 |
| c219e914-ab3b-33e6-9d83-b403e5cf3030 | -9.1525 | -49.9639 | 2026-09-28 19:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 1ce31fc9-58d4-33f7-80ac-621051248dcc | -7.4185 | -55.6301 | 2026-09-28 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 192.9 |
| 95e8c077-c235-34a8-96ea-7182f2f4dfd9 | -8.664 | -45.3469 | 2026-09-28 19:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 8f069788-398f-3435-9420-711dd7c4482e | -11.5157 | -47.3926 | 2026-09-28 19:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 5fb3679a-49c0-3c2d-a16e-3ec648a084fa | -11.7178 | -43.4623 | 2026-09-28 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 45c42b14-a413-3c14-96ac-36b8b9453d88 | -13.3267 | -43.9523 | 2026-09-28 19:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 209.0 |
| f65425e2-df9e-3e47-8f87-ea93f50ef464 | -11.983 | -57.6066 | 2026-09-28 19:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| e8c94b73-2bd7-3a8b-874e-cb769ab12017 | -13.8822 | -53.6571 | 2026-09-28 19:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 33f6f4a0-254c-31a2-b36f-46d90fb09bd1 | -9.0786 | -49.8639 | 2026-09-28 19:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 1566c3ec-dcca-3b07-aaa3-aa37d29695ed | -12.1204 | -57.1567 | 2026-09-28 19:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 35d144f5-fa7e-31d5-8740-b4a333560601 | -11.6209 | -46.7967 | 2026-09-28 19:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 64b5289e-07e7-33c8-a91a-8910ebd9c635 | -15.081 | -54.5964 | 2026-09-28 19:10:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 170.6 |
| ae6908a0-75d0-3f24-8a4d-0faf84eed083 | -10.9912 | -50.6978 | 2026-09-28 19:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 8aa4df72-7009-398f-9e69-c3c6c701cd87 | -10.2257 | -49.9879 | 2026-09-28 19:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 4ce64d2d-344c-3c7c-bca7-94ebf14a17cc | -11.6994 | -43.4178 | 2026-09-28 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 272ac754-06b0-3205-be59-4c5aaa4e49f8 | -7.6852 | -54.7532 | 2026-09-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| db95bcea-3307-37c9-8fb3-e5b4891cc218 | -10.8238 | -60.744 | 2026-09-28 19:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 397.2 |
| bd2e509c-2c44-31ab-b300-fe35260ddbbd | -10.2067 | -49.9898 | 2026-09-28 19:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 328370e3-e095-3c91-a38a-3d075868fe70 | -11.1966 | -44.7805 | 2026-09-28 19:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 47b5d560-a000-3884-8dba-8b10b78407e6 | -12.9456 | -46.652 | 2026-09-28 19:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 276.7 |
| 56544898-2777-3f8c-80bc-1a7795474a3d | -11.1962 | -44.8037 | 2026-09-28 19:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 3fa1dd6d-57f9-39aa-958a-7e09c07e4406 | -13.6866 | -56.6131 | 2026-09-28 19:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 8f407f9b-7fc0-3778-8559-4b9fd5438aaf | -7.5159 | -55.0245 | 2026-09-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 74df3710-4bcb-382b-a474-f7ccff3468ca | -8.2479 | -45.4583 | 2026-09-28 19:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b23939b6-9ad4-30cd-94cf-33d7280b2739 | -13.9012 | -53.6757 | 2026-09-28 19:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 3e5cabba-4ce0-3fd4-bd7d-fcb43ee769ec | -12.7871 | -54.0069 | 2026-09-28 19:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 196749a5-5967-3246-a1a2-abec8a031fe6 | -8.2994 | -54.7146 | 2026-09-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 134.7 |
| f55db2ac-ebbd-3c01-8255-2e32d6d4cfa2 | -12.0466 | -46.4897 | 2026-09-28 19:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| e7b8b0ac-f98b-3297-9441-895a67e3960d | -11.6096 | -44.1382 | 2026-09-28 19:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 261.6 |
| 85b37dec-fdce-36fb-af4e-feaa4c652114 | -11.4601 | -49.7452 | 2026-09-28 19:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| ea7c2a23-520a-320b-afd2-12b863461063 | -9.1523 | -49.9853 | 2026-09-28 19:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 174.2 |
| 32340d6e-5e71-3b9c-b725-8a521ae0a91b | -11.0796 | -46.079 | 2026-09-28 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 017f8ca7-66e1-357b-9445-441b4a6ec47d | -11.3436 | -54.1086 | 2026-09-28 19:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 289.1 |
| fe7d1722-cc04-3ba2-a421-3c5da2aab4ed | -12.7868 | -54.0275 | 2026-09-28 19:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 177.6 |
| 424ff244-96f3-3cf7-978c-58dfeb344173 | -10.215 | -46.6836 | 2026-09-28 19:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c7648667-8249-3776-99fc-5f6eef873929 | -13.9015 | -53.6548 | 2026-09-28 19:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 251.0 |
| c7aa6114-f268-38f6-bccd-c5f07606a3e9 | -8.1546 | -46.9693 | 2026-09-28 19:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 296f7cea-2242-3f5b-ae56-63047f5b6a0e | -9.9396 | -50.2304 | 2026-09-28 19:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 2df76866-425d-365d-ba8b-f8f7aadae477 | -10.9725 | -50.6785 | 2026-09-28 19:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| ef561f41-9cef-3246-bf46-4ed68929ba2d | -12.9461 | -51.0481 | 2026-09-28 19:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 34b0af3a-115d-3b17-97d8-8f756fa25e96 | -14.5171 | -52.4864 | 2026-09-28 19:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 68f5d3d1-2be2-354f-bd1c-ba6516628994 | -7.437 | -55.6291 | 2026-09-28 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 300.2 |
| 44db3372-fb60-3bcf-8e24-1aef994dbb3e | 1.6749 | -55.9225 | 2026-09-28 19:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 5281d5b8-0a83-3cb0-b55d-b4a1402e818f | -10.7726 | -48.7399 | 2026-09-28 19:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 1cd5cfc0-0d2c-3103-9a06-20410166dd84 | -7.6034 | -55.6995 | 2026-09-28 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 5d46875b-46b1-32e5-9c70-f9ad6d48c195 | -11.5904 | -44.1411 | 2026-09-28 19:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 5f0bdb14-e947-33e3-8c52-4ee8fa5019fd | -10.0148 | -50.2443 | 2026-09-28 19:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 189.6 |
| f621ae23-3336-3f65-80e3-28957b7abfc4 | -9.6263 | -46.8185 | 2026-09-28 19:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 6f6e2e4b-380d-33a0-8936-517cff14be77 | -5.4762 | -45.1262 | 2026-09-28 19:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 89d74374-7780-3551-b551-6f47e4950fb1 | -8.6451 | -45.3489 | 2026-09-28 19:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 46012fe7-e644-3cb0-9b0e-725e5e899a70 | -10.9538 | -50.6592 | 2026-09-28 19:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| c0a56461-2bd6-3680-948b-b68bd87c2faf | -15.0616 | -54.5988 | 2026-09-28 19:10:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 3224c9cf-8259-3e9b-a58f-f823c722a500 | -10.8184 | -61.4191 | 2026-09-28 19:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 52059478-cfa5-3a9d-b588-27c24b95c977 | -12.1391 | -57.1751 | 2026-09-28 19:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 6dcd6964-3474-3efe-bd9b-81dec5b9483e | -8.2806 | -54.736 | 2026-09-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 19626343-2e02-3ac0-8d41-0abd4fdcd147 | -5.7388 | -45.0172 | 2026-09-28 19:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 0fa7142d-5ad7-34fd-b47a-a899b5fc3bc9 | -0.5073 | -49.1326 | 2026-09-28 19:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 46f78a43-102d-37f8-892f-ae61cb600fe1 | -9.1337 | -49.9656 | 2026-09-28 19:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 62553e8d-4137-32ad-a24f-1ada1b27c119 | -12.1363 | -61.1669 | 2026-09-28 19:10:00 | GOES-19 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 4a4c2b51-13ae-36fd-92c6-78f95534b71a | -5.7384 | -45.0626 | 2026-09-28 19:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 85ee8f6c-7873-3c57-a905-b563d2b058b0 | -12.8061 | -54.0048 | 2026-09-28 19:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 898a1cb7-7c0f-3fb6-9a5c-0260c59e4dd6 | -8.2807 | -54.7158 | 2026-09-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 185.2 |
| 011f8b82-b3f6-3c0e-b4f9-87f767c1ad7e | -9.5192 | -46.3604 | 2026-09-28 19:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 740bdb2d-e8ad-347f-ae15-750929406430 | -12.0019 | -57.6051 | 2026-09-28 19:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |


[Clique aqui para ver as próximas entradas](README179.md)
