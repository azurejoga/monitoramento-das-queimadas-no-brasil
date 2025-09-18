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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 716b7bbe-126e-3945-94b4-14238497d092 | -10.07005 | -68.47291 | 2025-09-18 05:33:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0c96b1d-d35a-3be3-b0da-8cd9d02ad592 | -10.55523 | -60.70746 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ec2a3ba-4387-3090-bbab-c52e50c57f45 | -8.83784 | -62.36851 | 2025-09-18 05:33:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1faf8d9b-770d-330b-8495-c928a76fbe80 | -11.37343 | -50.83629 | 2025-09-18 05:33:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b75dcdd-f2f4-34e6-9a30-37926659dc3a | -15.31703 | -59.42107 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f7cc113-de32-3556-aff8-74967ab52692 | -13.29914 | -61.77697 | 2025-09-18 05:33:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a27020c7-c921-3734-aff5-16b2234c1e96 | -10.43047 | -67.73261 | 2025-09-18 05:33:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b3d469a-a907-3eb1-a87a-7e1f5cfc8a13 | -10.4178 | -61.20339 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bea9e782-01e7-3df6-a153-e1c22e3babeb | -10.40808 | -61.19806 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5cb5154a-6576-34d7-9a81-9efc6f98929e | -10.39607 | -61.2077 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6bf3c67-edc3-3bd4-bdb1-67352f6fa2fd | -8.94693 | -63.04866 | 2025-09-18 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 012999db-f13c-3f5a-a4c9-5b545184fe5c | -8.94748 | -63.04516 | 2025-09-18 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f76b61f-4b8f-38f2-b974-36d25863c806 | -10.40407 | -61.20128 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cbc6a20d-8ae9-35f8-8879-945e0debd255 | -12.66179 | -54.70219 | 2025-09-18 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 652731c1-90af-361a-b307-0d5fff4a26c9 | -12.81579 | -52.98288 | 2025-09-18 05:33:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 953826f5-27e9-36be-ae24-b3c5d6a33cb6 | -12.81424 | -52.98699 | 2025-09-18 05:33:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efe9aeb6-e7c2-3e4f-ad46-fbbffb42d553 | -15.81179 | -59.41627 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bef1f3b-4d31-3614-a309-6b72d0c15618 | -10.40292 | -61.20879 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f59767a-d1f0-38bb-b597-f0c507a8fc41 | -10.40007 | -61.20449 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4055a27-5f08-38ef-86de-d68ef084a7d4 | -9.76053 | -64.29736 | 2025-09-18 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00aa9073-6916-3ced-b297-13f678f0267c | -9.77538 | -67.94087 | 2025-09-18 05:33:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57906165-79a1-3cc9-8b30-4b6d9faff2eb | -10.26436 | -67.13511 | 2025-09-18 05:33:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f3e593c-20bb-3ac5-9011-a7b1b02a0246 | -9.93437 | -62.41943 | 2025-09-18 05:33:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 851ae3e1-8315-3c18-ad5e-131f3ffea320 | -8.83394 | -62.37152 | 2025-09-18 05:33:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e67d03f3-41f1-305d-89c2-824d5898a5c5 | -9.4234 | -67.61702 | 2025-09-18 05:33:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3e57f0c-6a31-3db5-9f90-1423061a69e3 | -8.67353 | -62.59322 | 2025-09-18 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bcca212-208d-385b-9c5d-d06820b81786 | -12.50528 | -57.6332 | 2025-09-18 05:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07e5ae48-0a2d-32b4-a490-e5238c2a5f5d | -10.40693 | -61.20556 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a306f77e-0690-3770-8eeb-222859e55dc0 | -12.82011 | -52.98769 | 2025-09-18 05:33:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0d0da35-f1fe-320a-8ed3-ea416ae1e80e | -10.4138 | -61.20662 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ef0da32a-c2ad-3a1a-860a-98438d4fee04 | -10.06656 | -68.46836 | 2025-09-18 05:33:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e0983e4-4f14-3ee9-9a79-5b772471148c | -9.15676 | -61.17581 | 2025-09-18 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bac0c5ea-ad1a-337b-9981-7f1515a28c6e | -14.7931 | -60.23333 | 2025-09-18 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74ba89b2-bebc-3922-a2fe-d0482f8877e9 | -10.39063 | -60.79841 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66c7ccae-c3cf-39f7-b018-6cebaa3503b3 | -10.04857 | -64.80212 | 2025-09-18 05:33:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c855505a-67c8-37c9-83b9-3471667b0735 | -9.46624 | -60.48519 | 2025-09-18 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a39c4eb-a450-3ffc-9da7-bca2e15627f9 | -11.38657 | -50.83804 | 2025-09-18 05:33:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a016e0f9-d153-336d-a7e4-081d2a5e3a48 | -15.32857 | -59.41008 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99ab1568-bc08-33d9-9241-839aae746830 | -10.53252 | -68.13335 | 2025-09-18 05:33:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27332032-d008-33c2-994b-dab6ca7c897c | -9.46742 | -61.01499 | 2025-09-18 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae0b6611-8e97-3e61-8878-39a729064876 | -10.3852 | -61.20984 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f470096e-d298-344a-9c76-8ff31f703819 | -14.75529 | -60.20239 | 2025-09-18 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 620dbb51-589d-3b10-b323-c36cf5c21439 | -12.81471 | -52.98283 | 2025-09-18 05:33:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3058aa9-811c-3cf9-94c0-e3a0eacbb71e | -15.3246 | -59.40955 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d9d51a2-e5d9-31e2-992d-2a72515441fd | -15.32064 | -59.40899 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25e274eb-532e-3bfe-93e4-7c1a1b546759 | -11.59744 | -49.81641 | 2025-09-18 05:33:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dc90db8-77e1-32ec-9ee3-820400a6917a | -15.81787 | -59.40145 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21dc5d23-ea88-389d-806f-072234603133 | -10.39815 | -60.79575 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49136b3d-ee38-3aad-91a7-a1025a5589ec | -9.46799 | -61.01126 | 2025-09-18 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d0f8c58-a315-33a1-9107-e8e4433053e5 | -14.78201 | -60.2298 | 2025-09-18 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5109cb4-5ed7-3757-b180-211fe7cda255 | -10.99586 | -68.45813 | 2025-09-18 05:33:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e29afbf2-59ac-3c98-84f5-75ed5fa65ca8 | -10.26972 | -67.28814 | 2025-09-18 05:33:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bd2e6ea-3dfe-354b-9e65-c55ee7837608 | -15.31769 | -59.4161 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06f294cd-fe8d-3bae-b78b-88a77b09cb56 | -15.31453 | -59.42382 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19bb7217-720d-32d6-92b2-1a4f70c62c9f | -15.33097 | -59.40731 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8813a154-162b-3221-85bf-823bb6f92f90 | -9.48928 | -63.46423 | 2025-09-18 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fb412e6-14a8-34fc-9889-1998cc0b74d5 | -11.38068 | -50.83148 | 2025-09-18 05:33:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 054e3c29-dabd-3673-bec3-f653068f715b | -10.38463 | -61.21359 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50f57bd8-8cc7-3fa6-af0d-02e630504709 | -12.509 | -57.63792 | 2025-09-18 05:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a64bedb4-a694-3f9f-ad6e-638df813c402 | -15.88041 | -59.43398 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 13308f7d-41a6-3589-baf7-29de5a1a5581 | -10.41151 | -61.1986 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d23bc63-e581-3b66-b263-df1e85c02019 | -8.85238 | -63.53528 | 2025-09-18 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 37094267-0f64-3765-92d0-aa661fa1a68f | -14.81116 | -60.24104 | 2025-09-18 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2513e98e-84a9-3ede-911a-81585f358add | -9.00162 | -63.67612 | 2025-09-18 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4654717d-5f63-35ac-8078-57bac421f141 | -10.39467 | -60.79523 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0205e220-e3bb-322c-8ab7-baf5cbbceda4 | -15.32235 | -59.41141 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 40ce27f4-8a0a-3d1c-9773-22babc99fddc | -14.77809 | -60.20343 | 2025-09-18 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab34bd99-9efe-3f6d-8ebb-d2322b92b3fe | -13.29686 | -61.79219 | 2025-09-18 05:33:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17b9105e-66bc-3ea3-9488-19210a4046cc | -10.41437 | -61.20286 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 119825d5-b7f4-346f-a88f-d400e17fdfb4 | -15.81455 | -59.39589 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f67db93-85ee-3e40-921a-5ac3055cae47 | -12.81529 | -52.98704 | 2025-09-18 05:33:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8fb6d04-0abb-3595-93f8-9de7bc04bce8 | -15.3127 | -59.40792 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0570273-e284-317c-a23d-9c637967fad0 | -9.14981 | -60.36061 | 2025-09-18 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4821fb1-d6e7-3901-af7a-943d53ec4d58 | -8.83061 | -62.371 | 2025-09-18 05:33:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52d362e4-8c70-39c1-850a-f6b510e40ddc | -9.42737 | -67.61775 | 2025-09-18 05:33:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af39089a-1fa0-3dfe-879f-bad9979babf1 | -15.31591 | -59.41389 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81b73577-33d4-3ecb-a3c9-7e82c16bfa65 | -8.67132 | -62.86136 | 2025-09-18 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed08e081-0be6-3eef-b95c-2f8605f3ccd6 | -9.76391 | -64.29792 | 2025-09-18 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c3f06ac-964d-300a-a04c-98f8e3697e59 | -14.75228 | -60.19659 | 2025-09-18 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a842c6de-dcba-3097-bba2-04509ce97f64 | -9.56358 | -63.65372 | 2025-09-18 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffd1e626-245b-373e-b19e-612810525012 | -8.85294 | -63.53173 | 2025-09-18 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 732347a2-8ee5-3437-a9c0-39b870dc51aa | -15.87093 | -59.37087 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f70c29bf-1cdd-3915-873c-9e0d3ddec125 | -15.31056 | -59.42336 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b09f000-d885-3f3a-b093-1c677d0e762a | -10.052 | -64.8027 | 2025-09-18 05:33:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ec2a154-65c0-3f6d-a368-24fdfa5d6ef7 | -10.40635 | -61.20933 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d21dcf0d-18a1-32d0-9523-7e05e2acf1ac | -10.3995 | -61.20825 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e07bb7c7-6e58-302d-bbd0-07ceb892db47 | -9.5346 | -64.56982 | 2025-09-18 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2393571f-0e1c-319d-87d5-e7f8ad8af418 | -15.81646 | -59.41179 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7464f428-857f-3220-94d9-ada9f12e6daa | -13.29513 | -61.78024 | 2025-09-18 05:33:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b202acc-ace6-3092-9329-b410426bcb9b | -9.15331 | -60.36117 | 2025-09-18 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 340780d4-a256-3abe-8e8e-d0b9f81ebde9 | -8.68131 | -66.57792 | 2025-09-18 05:33:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8df82088-cbaf-385b-8619-8bc466a243cc | -10.41208 | -61.19485 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 93364ad1-6844-34e8-8aa1-0a5f5d455b08 | -10.40522 | -61.19379 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 823dc6f4-4543-3a20-97a3-71ef482a96ac | -15.31523 | -59.41883 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de576420-6f6b-3a51-8c01-8bd3bf22bdeb | -11.37064 | -50.84807 | 2025-09-18 05:33:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e28d26d7-bd70-3f2e-bcd2-839758ad29b3 | -10.40578 | -61.21308 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17a2caab-f98b-388e-ba85-78971067e198 | -10.37036 | -61.26122 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae1b2c13-5952-345a-85be-160a004508e8 | -10.40865 | -61.19431 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 616edebe-94ea-368a-891c-50f038b8223c | -10.41094 | -61.20234 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d16fe3f-ec70-3d25-ae62-86b6ba13cd05 | -12.40837 | -63.88774 | 2025-09-18 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README30.md)
