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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07b87d80-747e-36fd-ab54-227c0a8f8980 | -13.15244 | -51.1962 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff403cbc-b5d7-312c-baf1-1edf8d36b1f1 | -13.15162 | -51.20068 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7aca23c4-323a-3847-b653-5400e8f7b35d | -13.14964 | -51.18636 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 00ddb86d-6438-3045-9ca2-88db44225b19 | -13.14882 | -51.19085 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 41a10fcf-7533-345f-975f-a3981d8874f5 | -13.14799 | -51.19533 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f36b2b1-4730-3cf9-918f-1aa90edd9264 | -13.14717 | -51.19981 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f43bda6-e14d-38fe-8dfe-94c33868ccff | -13.14602 | -51.18102 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d38849ba-830f-3e3e-8672-1dbb6905f9ea | -13.14519 | -51.1855 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09c78cd6-15ee-3419-b67a-fcad7737c181 | -13.14486 | -51.16229 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64d553cb-cce9-33e3-b258-e56df283d1d2 | -13.14437 | -51.18999 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 785c04de-2034-3a27-922b-4019719afaa4 | -13.14404 | -51.16675 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0a6e050-e940-39ec-9292-64cce2f5254e | -13.14354 | -51.19447 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b3620fe-7787-351d-ac20-26161db44e12 | -13.14075 | -51.18463 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdb8de76-e7a6-3950-a085-b4da97f6a48e | -13.14042 | -51.16141 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec7d72aa-1669-30de-856b-ea21142567f4 | -13.1396 | -51.16586 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5bc7a9a-37f6-38de-bda7-b9e5ac787c56 | -13.13878 | -51.17033 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b428e66-c845-3e58-857a-c6521397f705 | -13.1368 | -51.1561 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d051ca6f-dc08-3fc3-80b5-13f6632a71af | -13.1363 | -51.18377 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5b42fd2-1d15-3a88-a8b6-f7a46da6bfe6 | -13.13599 | -51.16053 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c5cb7a3-27c9-39db-b0a4-f7e15c8b7445 | -13.13401 | -51.14633 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cf2ea2e-5c1e-3e74-ae0e-f9d3e7bc780d | -13.13122 | -51.13658 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66ee1771-c68f-3e4b-b5e8-45ad496b132c | -13.1304 | -51.14102 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d538d8f-905c-3801-8670-26bf869007ed | -13.12958 | -51.14546 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 192e25d3-e3c0-3312-8f3b-fe142d9b5027 | -13.12679 | -51.13572 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 62b07e7a-a024-30ad-9759-2e573006eb5d | -13.12597 | -51.14016 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b46a1393-7f22-3e6c-aab8-469f01a901f9 | -13.12236 | -51.13484 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 20ab4097-7731-3bb2-8802-5e686589170a | -13.12153 | -51.13931 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5e69d733-6802-34e0-a5ac-7f5b44a509cf | -13.10383 | -48.1988 | 2024-10-05 04:14:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bd3f58d-7626-35d9-865e-d2312b937122 | -13.10089 | -48.1937 | 2024-10-05 04:14:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1d0b827-51d1-3409-b6fb-3e1c40cc6451 | -13.10012 | -48.19817 | 2024-10-05 04:14:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8690bb73-c6e5-3e93-914c-9504a578e8da | -13.05925 | -51.11488 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 504532ad-eb23-3e9a-8021-67ac88097e63 | -13.05843 | -51.11933 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7defef5-0668-3ed4-875c-cf2f97e20dd0 | -13.05482 | -51.11402 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62431e70-b564-3946-8912-c6c9c752c2e0 | -13.054 | -51.11848 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c6c168d-6795-369c-ab3c-a0e16c5d68ad | -12.9961 | -51.11867 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a3a30d8-b313-3bd7-9c49-7f3746c2b505 | -12.9953 | -51.12313 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c03e245-ff93-3bb3-ac05-752cfe6ae124 | -12.99468 | -51.11628 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 017d5acf-224e-30a9-928a-08d3131ce1bd | -12.9945 | -51.12759 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 895c99f7-3588-3c08-bf41-235fd236033e | -12.99385 | -51.12073 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f622ef9f-7da8-371f-818e-288bd26dd88e | -12.99302 | -51.12516 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63120309-e078-318e-a44f-90c5ab3e3a4e | -12.99166 | -51.11781 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 873a0323-c31e-3d19-84c9-5815d33779aa | -12.99086 | -51.12227 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 528f9e5b-048b-3d94-a4f3-59a167a1a157 | -12.99006 | -51.12671 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4052679-fe3b-3c5a-bcb5-44ddb62f6a26 | -12.98941 | -51.11987 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27b21739-ed92-30cd-bd72-bd2bc02c265c | -12.97754 | -51.11966 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dccfe7d6-aa0d-354f-83ed-59979b2d06b0 | -12.9339 | -51.46464 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc18dc86-432a-359c-9314-838b51012006 | -12.93336 | -51.46717 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4126b21-9870-3f41-a8ac-4deb9e6303d5 | -12.93302 | -51.46933 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 538de856-acf9-35fc-bb1b-00273911096b | -12.85197 | -47.4631 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee5a1fcb-df4a-3f3b-a3c4-d1f22f9d4766 | -12.85128 | -47.46727 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23bc1c26-036b-3fd3-8ec7-e5b6b6ee392c | -12.842 | -47.47855 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7f41c90-fbfd-3f3b-8cfc-177fc3c767de | -12.8413 | -47.48273 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd36d554-023f-3f49-b176-34e566ae1644 | -12.83842 | -47.47792 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1003ab8-6ef4-380e-a1c6-a5951f782ab3 | -12.83772 | -47.48209 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e3396f6-36d3-3a41-9592-3811c770c5e3 | -12.83483 | -47.47729 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88752269-0722-37dd-bba6-93ba9c29af9e | -12.83118 | -47.45519 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ac46a50-a9aa-3419-a3fd-6b8b2596e4d1 | -12.83048 | -47.45936 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fa7318e-1d6c-3cd9-8040-aef21e7f23e1 | -12.82748 | -50.55293 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ec9f7546-6ea2-3689-98c5-28a056fad9f2 | -12.82673 | -50.55706 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8910b378-4739-3d83-b6df-011aaad57e00 | -12.82599 | -50.56119 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 79d52cd6-a36e-3bef-b675-5e5c49c4cdd5 | -12.82319 | -50.55212 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6d6ebcc7-3151-352c-b74d-36313744454e | -12.82244 | -50.55624 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7ec7126d-bf4c-3bb5-97b2-f512b021842e | -12.8217 | -50.56038 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bbf72d3c-c6ba-3433-a021-d65b4b5ad36d | -12.8174 | -50.55956 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a6a9042-91dc-3999-9703-578232d07cf5 | -12.81461 | -50.55049 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f492426-060e-3e02-bca4-0afee9b6d841 | -12.81386 | -50.55461 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77603281-0a1f-37a2-aaf5-c0d832a6a1da | -12.81032 | -50.54967 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5261fc06-e77f-3b07-88ef-a6503a60808a | -12.80957 | -50.5538 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6c2520b9-32db-3b9d-b5f1-4af443d4ea5b | -12.80882 | -50.55793 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 26a2b00c-9611-35a3-9294-9840c9508ba3 | -12.80807 | -50.56206 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e60cfe21-5536-317d-bfc1-28983202f423 | -12.80528 | -50.55298 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9daef97c-8553-3bc9-86c4-932360a1f15d | -12.80453 | -50.55711 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1d51d266-039b-3176-84ff-d5226590f16f | -12.80377 | -50.56124 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e730b55e-1f71-3c8a-a59f-98d2c8fcb018 | -12.80099 | -50.55217 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a631b911-d94d-3a77-9384-86bd224c335c | -12.80024 | -50.55629 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 4231c754-89ac-3ee5-af9c-1d01fb373ec5 | -12.79948 | -50.56043 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| c9db6312-b84f-3fe9-adff-abacf7d7ef58 | -12.79014 | -50.56293 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2a581f1e-6ef9-37af-8c8e-94bc55db2b67 | -12.78584 | -50.56212 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| adb6d12b-3ea8-35b8-8b07-aa3713f3fdf3 | -12.78459 | -50.54478 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 20cf39ae-a0d8-3021-bf40-2047ae097d25 | -12.78383 | -50.54891 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| d91a2b70-e3c2-3622-b9cc-e4cc69593d00 | -12.78371 | -50.54104 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 033dd11d-3443-3b06-8fb4-752f099e8b3f | -12.78307 | -50.55304 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 6f5374a2-f961-3fa8-a13d-33655ecadd7d | -12.78298 | -50.54518 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 8a8d7a8c-1867-3e07-a455-1ca8a86cc467 | -12.78246 | -47.43812 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7228f35-9b9e-316e-a4bb-11c977ec32db | -12.78226 | -50.54931 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 9a761aaf-9341-3139-85ea-f5fd9b259cd1 | -12.78152 | -50.55344 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 76cd754d-670d-3f9f-84c3-5dfb00351e61 | -12.78131 | -47.435 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2bf3e780-636c-3d6f-9c0a-69ef23cca325 | -12.78105 | -50.53986 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 862c5852-86be-3408-848d-e3eb55636d44 | -12.7808 | -50.55759 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 71357418-551b-3fa2-870c-142348acce1e | -12.78079 | -50.56543 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b0ef9db-c7b3-3439-a902-4c3e4f7047ee | -12.78061 | -47.43917 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 347eff47-e12a-368f-8da8-1e509c7b5ee4 | -12.78029 | -50.54398 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| cae7bf7a-78d4-36c4-b4aa-51094952cee2 | -12.77959 | -47.43333 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29d9e2bd-e7bb-3d4a-9778-67a3fded7753 | -12.77953 | -50.54811 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 2a20cf02-7abd-3491-8702-7816451d8205 | -12.77942 | -50.54022 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0cf424f7-6bf1-3f26-a960-7f5ad02e75bb | -12.77888 | -47.43749 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cfe0aab-f9e1-3f3d-876c-44607e43b310 | -12.77878 | -50.55223 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 17558bb3-3335-3587-8bce-43085fd0931c | -12.77869 | -50.54436 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 89935ab1-2759-3cfe-8eed-719387d1cc1e | -12.77801 | -50.55635 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 997b3890-a8ef-31a4-89b5-ff8ea991cb5d | -12.77796 | -50.5485 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |


[Clique aqui para ver as próximas entradas](README71.md)
