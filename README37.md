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
| 8991a91b-bf4c-3f5d-8534-c5a7fbf6c641 | -13.73976 | -52.01293 | 2025-08-20 04:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16880e40-5545-3090-b8f3-baac4307c9b4 | -11.44417 | -47.31355 | 2025-08-20 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8421a8cc-5934-3b1c-b1a4-03340ee35a6d | -11.97424 | -46.77634 | 2025-08-20 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4529398-7f22-34c6-a28c-53918b41404c | -11.01211 | -45.6233 | 2025-08-20 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8be6dc2a-9a8f-3e2d-afba-db9cdf0edb80 | -11.19293 | -55.91989 | 2025-08-20 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f3fe652-955d-374f-86b7-dda64712fef9 | -14.87997 | -48.07779 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| acfd143e-20c9-3b85-8138-3ad790c3b5b0 | -14.35846 | -52.00629 | 2025-08-20 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fa272ba-a8ea-37d6-a130-32583892ac1d | -13.08515 | -46.82805 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8f7b9f0-cbe9-3c6d-8d5b-5e18d608154c | -10.12534 | -47.43469 | 2025-08-20 04:36:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8729c21-64d3-36c1-9965-12300599a5ae | -9.1944 | -59.6273 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66722f77-bebd-3831-8b8b-a89e32def649 | -8.87694 | -62.39267 | 2025-08-20 04:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73586a17-6800-34a3-aa9d-4135fc1de9ef | -9.24073 | -59.61443 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbfd1462-da98-3688-88aa-fdb87cecd1f2 | -12.99376 | -45.20502 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac735177-0cce-3cf7-9f4e-6ee73d4ed347 | -14.64229 | -54.8857 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2830f5a-024b-321b-8c82-79594a06d807 | -13.18653 | -46.87103 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52c9984e-7d7d-33c7-aae8-930bdf70f0af | -12.10888 | -47.91657 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e533158e-1e37-3543-abd6-94655a36739a | -13.61977 | -46.88495 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91bc9182-0bb8-3b0f-8b29-376d650ea46e | -14.54424 | -53.18129 | 2025-08-20 04:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7784c040-9d1a-3f38-94cd-ba6ad0cfb66d | -13.0268 | -46.81128 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8222d238-d502-3a5a-abf5-066028f25eb7 | -12.81092 | -48.56379 | 2025-08-20 04:36:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69967360-f7b6-39d9-bff1-aa5cfc4771f6 | -14.32133 | -51.99133 | 2025-08-20 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2cf7d5f-2c11-3d67-86c4-f98e1020016c | -13.16176 | -54.93982 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3dae97d-1b68-3fbe-aa88-a8a1837f8df7 | -11.66645 | -60.18789 | 2025-08-20 04:36:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f344873-ab30-384e-b3de-81cc5e268f02 | -13.02594 | -46.81153 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd1833b9-929a-3356-ad18-a3da8eee3ec2 | -11.74295 | -58.32606 | 2025-08-20 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20209af5-c6c1-392f-a01f-5792cfa25212 | -13.63372 | -46.88768 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca01e040-9223-3637-9301-20d06113f5c1 | -13.18242 | -46.89869 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 071aa5f8-88ab-3e99-a6c6-f80d0181f5fc | -13.02652 | -46.80769 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 068864c8-29cb-369f-b888-7528f0634543 | -14.17958 | -48.71587 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 245bf471-95f4-3a74-b940-fc426e768aa6 | -11.74957 | -48.19013 | 2025-08-20 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f3b3e0ef-8f32-3dff-816b-905afe3ad61e | -13.4881 | -47.07013 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42aa6616-f0b0-3de3-a788-443db73b1dcd | -10.01093 | -47.80667 | 2025-08-20 04:36:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25a39c67-c831-397a-a1ec-aada5c19c1a5 | -12.43091 | -48.69912 | 2025-08-20 04:36:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89a88f73-665e-3d1d-a794-be8a454e255f | -12.37032 | -54.16747 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f66494e-a500-3bee-aa5a-52472e9f3537 | -13.56328 | -47.00105 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24d48e98-b745-3129-820f-579785ef96e5 | -14.45688 | -48.47506 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91f2d29e-e674-346f-b5af-ab82d6959f48 | -13.20016 | -50.74211 | 2025-08-20 04:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b877241-e690-395a-9cc5-e8624a2dce27 | -13.39662 | -47.49301 | 2025-08-20 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65003029-ba9b-3d52-a1f1-5c644a77e8c0 | -13.87028 | -45.55974 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71455069-beb2-3ec5-a8ab-afa7e80057d7 | -11.75162 | -55.84127 | 2025-08-20 04:36:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 919dd13e-45e1-3820-8caa-4b40780f03d5 | -13.02999 | -46.80837 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ba13b36-21db-3fcb-bbe3-6f99dc34835c | -13.03011 | -46.78383 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 565d9e5d-78c9-3ce9-baa0-e48c5425abc3 | -11.31512 | -55.12703 | 2025-08-20 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 308fe043-3d8e-3d4c-9cba-6a585be346fd | -12.09422 | -47.91475 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c52a4d9-6658-3365-a054-65c95bf49536 | -13.0277 | -56.84961 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84e00bfb-dcec-3560-81a3-8b81edb8bebc | -11.75346 | -48.1871 | 2025-08-20 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7b9fd84-a756-3f51-896c-1cc1dc6af9b3 | -15.5728 | -50.31127 | 2025-08-20 04:36:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21b33896-a67f-3b1c-90f6-9f25d6558c95 | -13.02831 | -46.79578 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 247d651f-dacd-387d-93ff-77daee91ec83 | -11.31137 | -44.92281 | 2025-08-20 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e49ff00-dc00-3918-a74f-62b73b99f83d | -9.21249 | -59.69919 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f05d55cf-582f-3490-8f76-7d55e4b235c6 | -13.61629 | -46.88423 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5928909e-08e8-3586-a3b4-559bc07f8293 | -10.89371 | -48.49927 | 2025-08-20 04:36:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30abfaeb-85d0-3090-9a70-e56c7fd66acd | -9.17784 | -59.61491 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5347c9e-cbc8-3cdf-bfae-6b5172a407a0 | -9.18655 | -59.60216 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4facea17-c875-3cd5-99d9-721e5eae97c0 | -13.13791 | -57.16014 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0f7fec8-6f1a-3ef2-94f7-6749b9bb9a6b | -8.88262 | -62.40144 | 2025-08-20 04:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9ac17b7-f0cd-3396-ac1e-d30dea7a5fcb | -13.58132 | -47.02394 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 528bacbd-a26e-3982-b58b-eed0adf45f31 | -12.4952 | -44.78993 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a9ed140-4eec-3b64-8f6b-08139e41017f | -9.20738 | -59.62526 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f4cb3a3e-c5bf-38d3-bbdb-a1f1b420c2f4 | -10.01148 | -47.80314 | 2025-08-20 04:36:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f98ccb59-1b46-35dd-b900-3acdb0e503b0 | -13.40217 | -46.36535 | 2025-08-20 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e0912d6-e12a-3466-a000-d8cf58d63b7f | -10.89427 | -48.49576 | 2025-08-20 04:36:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41142432-5d42-3199-81b2-8d40da21e48c | -11.13142 | -46.98579 | 2025-08-20 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4239bd1b-1e9d-3296-98fe-5fe0f32559f7 | -14.16489 | -45.29548 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59533ed7-b0ce-3586-899b-67203b9cb474 | -14.35197 | -51.98045 | 2025-08-20 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e85d50f7-430d-3307-b6de-44204ebab3ed | -13.67266 | -44.22374 | 2025-08-20 04:36:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afe21d98-470f-36fd-b780-5de3dff5951a | -12.97244 | -56.85843 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c83974e3-e3c7-35ab-a2df-72af8915b61f | -13.16105 | -54.94378 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eefa92d9-cae9-391f-9e0d-6e662b7f0ede | -13.40157 | -46.36945 | 2025-08-20 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c27e9da-9b35-382c-9798-66b4f10f1120 | -12.1862 | -47.22516 | 2025-08-20 04:36:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd3ccd2b-9fe6-3867-b931-56a6a34912f1 | -14.6585 | -54.88898 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b8d6d285-a504-363d-bde4-4d21ac5fea16 | -11.09678 | -44.81062 | 2025-08-20 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b4da1510-ec86-358d-a15e-ae8bd0629339 | -14.40913 | -50.41558 | 2025-08-20 04:36:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30f42651-aba1-35d7-9a16-b38431eb6c76 | -13.02736 | -46.80742 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6af4b15-f0b2-33b4-b5ea-88f18908b1f4 | -11.47019 | -47.30249 | 2025-08-20 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1680de50-88ff-34c8-9582-4ec1f02ddd34 | -12.47801 | -46.92115 | 2025-08-20 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35bb15fb-91dc-3b0c-b532-771328c19262 | -11.13657 | -46.97499 | 2025-08-20 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5cff39e-f34b-3067-a18b-89cc658acdde | -8.87277 | -62.40625 | 2025-08-20 04:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01ed0295-f86e-3d59-ac17-5c7982fbf1b4 | -8.65378 | -54.58393 | 2025-08-20 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa86e6ed-2f96-34d5-9972-8ae14e12a6fa | -14.98777 | -49.56006 | 2025-08-20 04:36:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa3a973c-bee8-390c-8a87-bd6b7a69d3c1 | -14.62166 | -54.88906 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1657e94-c779-3209-9b40-91a2d772899c | -14.18293 | -48.71642 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7c6f6b9-06e9-38a3-95da-f0fe87439ad4 | -12.97052 | -56.86889 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5782eb53-e670-35a6-b4de-7487b961e4be | -12.11163 | -47.89861 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03169bdd-77ca-3520-9445-a3d97a934c3e | -22.69397 | -47.34214 | 2025-08-20 04:38:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85afecd9-9ed9-36a7-85b4-95a57f7b789a | -22.26828 | -48.49784 | 2025-08-20 04:38:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39e3a5e7-c3e6-3410-bce5-7b0418b0119c | -19.35738 | -47.93945 | 2025-08-20 04:38:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dc573764-b532-3d46-b439-739cf418579a | -15.65036 | -52.68377 | 2025-08-20 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04908db8-550a-36d9-bddf-524e4e4c83e7 | -23.69571 | -47.4519 | 2025-08-20 04:38:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 822c3374-a031-3a78-b87a-3de49e2c5749 | -17.63678 | -52.20112 | 2025-08-20 04:38:00 | NPP-375D | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 007b88c0-a270-3252-8bc5-7203ec254be8 | -16.48959 | -52.72126 | 2025-08-20 04:38:00 | NPP-375D | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1cb609d-97a9-3330-9f08-8538de39320b | -19.01157 | -46.65193 | 2025-08-20 04:38:00 | NPP-375D | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e236d7be-ac4b-34df-afc7-52727145346b | -19.11808 | -46.60329 | 2025-08-20 04:38:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c48c2df-a37b-3238-92f7-d49d56ec9528 | -21.00249 | -47.6586 | 2025-08-20 04:38:00 | NPP-375D | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 44075f05-071b-32e9-b187-1161a78e2849 | -15.01617 | -54.82735 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0433aeb9-d6a9-3134-b347-aee7f3fffcee | -18.17841 | -47.89514 | 2025-08-20 04:38:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d5f8f09-0e03-32c2-b1ad-dce2c41b828e | -20.9526 | -46.10026 | 2025-08-20 04:38:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1086633-0339-34a2-914b-b9f1558de91c | -21.71395 | -48.15482 | 2025-08-20 04:38:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c54988f0-f900-34fb-9f80-80d8a4db5e63 | -21.89623 | -47.23081 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| db19afb0-80b9-3ac0-a8ca-0708416dd769 | -20.81506 | -51.68303 | 2025-08-20 04:38:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README38.md)
