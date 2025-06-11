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
| 82e12768-3088-3776-ab06-3e1e832e5432 | -7.01598 | -44.60194 | 2025-06-11 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2673376c-4a4b-387a-9e5b-35514ba193c9 | -7.01349 | -44.59897 | 2025-06-11 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe28e20f-8f88-3ee1-81a7-00779b80cc67 | -5.77711 | -43.61684 | 2025-06-11 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 981f1f9e-3a4f-3877-9b0c-78d9faf25aea | -8.28598 | -44.95899 | 2025-06-11 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9dbbbf5-26f9-3922-8f94-64672afd408d | -7.86942 | -47.88488 | 2025-06-11 04:46:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3be5910b-84b3-30f7-aa86-24a05f5017d0 | -5.09861 | -44.79934 | 2025-06-11 04:46:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af196fd4-685f-33e5-a3ce-e45e0eaca8ab | -8.2719 | -44.96163 | 2025-06-11 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9087d5e-9f94-3d3b-b74b-c965aca9aa9a | -7.81497 | -46.56292 | 2025-06-11 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d44caae8-ef16-3703-92e7-ddef070ada82 | -5.02827 | -47.97303 | 2025-06-11 04:46:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a3503f7-ca67-37a5-9b1e-b8b542e59b1d | -4.12921 | -54.90078 | 2025-06-11 04:46:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1178d950-0bf0-3acb-ae5c-11295e974d70 | -5.77325 | -43.61239 | 2025-06-11 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca33da68-ed31-353c-aaf8-c690234637e2 | -4.55693 | -48.02005 | 2025-06-11 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ab33776-b53f-3794-bb1a-258898d3836f | -3.62297 | -47.51308 | 2025-06-11 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 861b3924-b714-39a7-99a7-8b64d3209d2e | -7.46542 | -45.51175 | 2025-06-11 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e37864f-37bd-3da8-9373-20eb103e87db | -4.81889 | -44.35355 | 2025-06-11 04:46:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7695dd3-4aab-3960-bf6f-e449ae66404a | -2.90949 | -48.24965 | 2025-06-11 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c7e7561-6d20-31f5-b3b9-9e665b12e8c3 | -2.91876 | -48.23573 | 2025-06-11 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a99e22f4-c15e-3c8e-98cb-1248293c3620 | -6.06043 | -48.1273 | 2025-06-11 04:46:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9ba4350-67c0-3780-a48c-bc62ee0af81e | -3.32494 | -48.7128 | 2025-06-11 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a14dd51-5b6d-30e3-8127-abd9f730d258 | -7.24132 | -49.53265 | 2025-06-11 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a95e7fe2-366e-3a52-99aa-e02c047eb13b | -3.62001 | -47.50845 | 2025-06-11 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb139dea-ed4f-3992-ad14-b68613f88ed4 | -10.86939 | -54.31978 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26acb2c7-4638-3ce1-bcec-f5e1802eaf9c | -12.51859 | -57.2335 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a9c8bbe9-7e13-3e0e-953b-a62869227107 | -10.88531 | -54.74559 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e08d7614-328b-34bd-9e72-79cfc27bd39a | -11.79075 | -54.77481 | 2025-06-11 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d71c28b-1b0c-349a-8019-678e0e2849b7 | -10.45528 | -49.57567 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24a59e87-3423-3dfb-8520-d0f66ae136e0 | -11.77734 | -47.39867 | 2025-06-11 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 665e4622-3616-3877-ac40-59324201fdd8 | -11.78039 | -54.37435 | 2025-06-11 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ced6084f-c967-3a6e-9a8b-e76f4e630ccc | -10.36336 | -57.50726 | 2025-06-11 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96c6d53e-c8de-3a0b-97f1-70987354c457 | -12.20454 | -49.62074 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6088399a-1a9b-32a9-98d4-f86c9349d00a | -11.91602 | -54.8236 | 2025-06-11 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2618a6f2-8d97-3b23-9593-bc30c22f251c | -12.05689 | -48.07824 | 2025-06-11 04:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fd19de6-6df8-3f1d-ac46-776a08e8237e | -10.69557 | -49.5093 | 2025-06-11 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37e0c15b-aee2-397c-89a9-bd1c2a912d9d | -9.38159 | -48.41727 | 2025-06-11 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fb35edf-0e6e-3ea0-b4b5-d3e8d826157b | -9.39737 | -48.43722 | 2025-06-11 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08b99c46-b905-31cb-87c4-c8545ae291f5 | -8.95413 | -47.28652 | 2025-06-11 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 798aaff5-8446-3ff3-b74e-4ed6500070ee | -10.19085 | -49.58859 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f58bf17-bd9b-36fa-886d-b8b6cb30b73b | -12.20915 | -49.62838 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7680673-8326-316d-9e9d-7adebf105c28 | -13.08533 | -47.43357 | 2025-06-11 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b2bb393-6744-36c7-8480-9dd801373bd5 | -12.52493 | -57.19781 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b6e2626-d766-31d1-8bab-72746584a16d | -12.27884 | -57.27051 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 686bbbe5-c8a5-318e-8022-925d91361c4e | -10.65392 | -49.4256 | 2025-06-11 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f368618a-031e-3bfe-b166-2203d3992d0b | -10.36884 | -57.50039 | 2025-06-11 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8dab417f-2bc1-316f-ac4c-215ffc80357a | -11.82467 | -43.78837 | 2025-06-11 04:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 421c0d06-35e6-3e55-b5e2-8e72cda18fd8 | -10.50771 | -53.63049 | 2025-06-11 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54d4e452-1c60-3fd2-bfd1-8e3c6cbd6618 | -12.13355 | -54.66586 | 2025-06-11 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b64f1d1-0749-321b-bb02-bf1796dd4953 | -12.26372 | -55.07663 | 2025-06-11 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 987a1970-b2bb-3dab-8f1c-f7cf92961c62 | -11.6268 | -41.83132 | 2025-06-11 04:49:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a5fd8157-e3a0-384d-b73d-189880d09726 | -12.21167 | -49.62179 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ade315e-cdc3-3ce7-94db-e14a5cd239cc | -14.25422 | -45.50064 | 2025-06-11 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e07aff5-6d9e-308a-8ef4-38a66642a73f | -14.53271 | -46.04315 | 2025-06-11 04:49:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7821f06-11b3-3725-abb0-20ca94434735 | -12.78653 | -48.73236 | 2025-06-11 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a7364b7-8b30-3d65-b6b7-b4c87c13baf0 | -12.26467 | -57.60587 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09cc2f31-30d1-38dd-b8bb-87281bbcdd78 | -8.55008 | -48.2572 | 2025-06-11 04:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e339e28-b3ee-3744-aab6-f2f371141351 | -9.29366 | -55.891 | 2025-06-11 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 710af4ae-2ee1-388f-8847-1b255b29f85d | -11.58934 | -51.3465 | 2025-06-11 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e316067b-7efd-39ae-a68f-f6474124ba02 | -12.52345 | -57.2291 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c71214db-9ee5-3029-9b19-59a9d7d69fe8 | -11.90835 | -54.82637 | 2025-06-11 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| df918ed6-28a0-3e83-bc7d-f580430e4227 | -11.14074 | -53.92364 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef5ea95a-c658-33d7-a64b-40049b9a80ac | -9.88921 | -47.81454 | 2025-06-11 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92bb4402-2064-35ac-a3e0-c24c6230cb2c | -10.24344 | -52.23191 | 2025-06-11 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df32237c-dc17-358c-a4ed-f4ae3805ad24 | -11.04971 | -55.03442 | 2025-06-11 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9412f716-b82a-3602-b412-8aba5432d571 | -10.36752 | -57.50801 | 2025-06-11 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a996ccd-1606-390e-b0f5-a71c331c328e | -14.24951 | -45.50003 | 2025-06-11 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4277b6cd-e24d-3e97-b8e8-d50e54e55fba | -11.88575 | -56.41322 | 2025-06-11 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 207e85d0-6649-37e0-a3a0-5c02a7120a6c | -10.51472 | -43.97885 | 2025-06-11 04:49:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6d58d1c-8036-3da7-8f11-6f60db68df79 | -12.26872 | -57.60662 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f951471-14e4-300d-bef1-318f376c8f12 | -14.25016 | -45.49492 | 2025-06-11 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 259a0f4e-add1-33fd-b481-90593de1d49e | -11.14135 | -53.91991 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0aae68ad-3af5-3cfd-bae4-5528b3c32332 | -10.36468 | -57.49963 | 2025-06-11 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f561b151-d160-3ab2-b737-218a0874e6e5 | -8.3148 | -47.9174 | 2025-06-11 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d54dfc92-244b-3022-83e3-a8c2a7f94dcf | -10.65627 | -49.43418 | 2025-06-11 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9a42b64-6af9-3eaf-8562-6f7b01b5bfeb | -9.88808 | -47.81164 | 2025-06-11 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b35d8e1b-921a-3dd5-a509-91a9fa8e3bcc | -13.89687 | -48.7335 | 2025-06-11 04:49:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 077aa05e-4d2c-322c-8e1a-1053ce5ff481 | -10.65746 | -49.42614 | 2025-06-11 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e264d002-6ef2-30b8-b4f3-ee6026b76408 | -10.19027 | -49.5925 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3dfdb5b8-89c2-3812-a61e-e9b0b3a54f0b | -10.87569 | -54.32481 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e19ca662-1ae0-306a-8864-88a47621761e | -13.07487 | -49.24252 | 2025-06-11 04:49:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a704c2ba-52b4-31e1-b7eb-1065ab011dae | -11.7794 | -47.40288 | 2025-06-11 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7384e0b1-ab33-3c07-a100-0cc9c0aabef9 | -13.52539 | -47.86356 | 2025-06-11 04:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46951212-f80d-3f39-9c1e-33a7683725c8 | -12.84033 | -47.38471 | 2025-06-11 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1db4621d-31c2-3639-b1b2-c6f02421c387 | -10.34741 | -57.50043 | 2025-06-11 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ec2890c-223c-35c7-8efc-a34f119f48da | -12.21044 | -49.62993 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f97a5b4-0d69-3d49-8afb-11249134ed2c | -12.51556 | -57.22766 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 39fa471d-9a6a-3039-a332-6058773ba5ea | -12.20974 | -49.62431 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b357343-31c9-3eb3-8337-ac3b46af5f7e | -9.40228 | -48.42924 | 2025-06-11 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aca68cd6-c1f4-30b9-b00b-002b46e06df1 | -12.84084 | -47.38107 | 2025-06-11 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fed82311-04f2-325c-b364-2930affe5487 | -9.39862 | -48.42867 | 2025-06-11 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d35f652-051c-330f-b63e-f92a5ea32127 | -9.84847 | -47.87993 | 2025-06-11 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64a7c5be-abdd-3a6b-8970-9a341a01de60 | -11.13765 | -53.94237 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 031580d4-cb56-3384-bf78-62507939fcf6 | -10.18866 | -47.31868 | 2025-06-11 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a76db7c-8ede-37f3-9ea5-f87b3eb87945 | -10.29783 | -57.14054 | 2025-06-11 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80e1461a-ed0b-3afc-8e60-43a01798c2e5 | -10.18677 | -49.59196 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 092290ef-42b2-34ff-a2f9-3c480129bb37 | -11.34504 | -45.21737 | 2025-06-11 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc8d18e6-807a-30b9-9896-ec78b602d560 | -11.77694 | -54.37375 | 2025-06-11 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 539078d6-27c7-3366-a0e2-6b6d211bb338 | -10.87403 | -54.74784 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 707afb91-947a-3994-9adb-5912c7c0571b | -13.89305 | -48.73305 | 2025-06-11 04:49:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35402781-1868-36e7-bf0d-2ad8e0d06c42 | -12.13419 | -54.66198 | 2025-06-11 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4e14642-4966-3094-8e73-52755a0c4799 | -10.19376 | -49.59303 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bbe83a1-c474-3e81-9e26-04b94ea4e63b | -8.54642 | -48.25667 | 2025-06-11 04:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README7.md)
