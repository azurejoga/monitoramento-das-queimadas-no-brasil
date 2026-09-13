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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d5370df-0c76-3e9f-9edb-18ac7b792c3b | -11.34933 | -46.79023 | 2026-09-13 04:17:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 931c6fde-4f84-3768-a679-e64bce679102 | -12.49108 | -47.15563 | 2026-09-13 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 988e8637-cd86-3759-b5ed-9c7117ed4642 | -8.11246 | -54.79737 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d566790-007e-36e3-8602-80936e6f614b | -8.05413 | -54.8434 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 741fab8f-2af7-3ea1-be35-e3b8f0d170de | -11.72645 | -46.73608 | 2026-09-13 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2ee7f29-6425-3182-a605-e561eed3fc80 | -10.64413 | -46.00435 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb243e77-cbba-33fc-8d91-5374c7dea00b | -10.55461 | -51.33215 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cbc764e-922f-32ec-bf4d-ad0c3493ff80 | -9.59883 | -46.72858 | 2026-09-13 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7c96f2f-f26e-31cb-9e3f-afa855ae133e | -13.45127 | -48.49193 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9e304132-482a-32a3-9834-1e967b796277 | -10.68339 | -54.16197 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 360b00b7-bd06-379f-a399-06b6c819c6c8 | -11.81726 | -46.39901 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8196d3ef-dc29-3e71-a5e9-89648195ff13 | -13.46878 | -48.52249 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83f12593-2f45-3c1c-90da-b13352194a2d | -10.33775 | -46.4678 | 2026-09-13 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac0edcb9-6bb5-3b6b-905f-52039549e77b | -15.63478 | -43.32794 | 2026-09-13 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d4782ed5-d03e-3ca1-a1ce-367500ed4c0c | -7.87247 | -54.72869 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 181f3d0b-017b-3a7e-9f50-443f6602ed2c | -13.29667 | -43.67591 | 2026-09-13 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4a5cd5c-db6b-3556-97f5-f14f9bd14646 | -8.81481 | -46.90493 | 2026-09-13 04:17:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdabe888-b688-3746-b6d1-976777561516 | -11.1885 | -42.79543 | 2026-09-13 04:17:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 335a487e-7021-30ca-8d52-db86428896fc | -10.65235 | -48.91138 | 2026-09-13 04:17:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a6872fb-c894-3ef1-8774-8c9cdfe19cd4 | -15.16732 | -41.71488 | 2026-09-13 04:17:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| afcb7928-24f4-3154-9625-8a7003f582a0 | -15.57201 | -53.7889 | 2026-09-13 04:19:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3bf184c-f9ca-34c5-845a-31ce2f89ca26 | -15.55388 | -53.80302 | 2026-09-13 04:19:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c097de35-8402-3665-823e-971f431ea4fd | -15.56305 | -53.83534 | 2026-09-13 04:19:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 307a06a4-5824-3818-ae54-188e247c722c | -19.0472 | -40.40048 | 2026-09-13 04:19:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3cf9e757-1f49-3268-b972-5648bbff3d40 | -19.04585 | -40.40112 | 2026-09-13 04:19:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6602d406-eb64-389b-9cd1-ee3d1f9e4789 | -18.41207 | -46.409 | 2026-09-13 04:19:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da8e50c1-86cf-3ace-a1d1-c86e021503aa | -18.91233 | -47.02819 | 2026-09-13 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5adca15d-144b-3452-acae-5672dd597898 | -18.64405 | -41.99263 | 2026-09-13 04:19:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 88a12c9f-c58b-3826-bb6d-425b002d62d7 | -16.26577 | -50.23074 | 2026-09-13 04:19:00 | NOAA-21 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1b4b9a27-40f2-3483-9538-5ef60406861a | -15.57311 | -53.78318 | 2026-09-13 04:19:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49bafe82-d4f0-3090-8fd9-a7ed4ea0d627 | -18.48491 | -42.81488 | 2026-09-13 04:19:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d86c1be6-1b29-3242-9a4f-2b1bf21ab3eb | -17.32222 | -46.92581 | 2026-09-13 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f47303d-9596-377c-a974-7e4e611c9399 | -15.57354 | -53.78634 | 2026-09-13 04:19:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c33251e0-a8bb-3a75-8a03-0762bfb4efcf | -18.41842 | -43.41359 | 2026-09-13 04:19:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84b2a763-eea5-3e19-b088-de8046ffd9a7 | -18.49211 | -42.81604 | 2026-09-13 04:19:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c74b9855-e34f-3c8b-90d2-ae5557dffca9 | -15.57697 | -53.78981 | 2026-09-13 04:19:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fc4ae6f-cb98-3164-9d1e-f92858fef90a | -16.97062 | -45.69023 | 2026-09-13 04:19:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a436a2c0-517a-3c27-a28f-c23f92b0c5fe | -18.72845 | -43.7306 | 2026-09-13 04:19:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77ee0355-0d8e-3c83-a6ce-5cd8db41509e | -15.55608 | -53.79169 | 2026-09-13 04:19:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cc860e4-d0cf-3cf0-95fc-55157b1dd853 | -18.48131 | -42.81428 | 2026-09-13 04:19:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c7cfe8a6-b69f-369d-b84b-8c5f50e0ee85 | -18.48911 | -42.81112 | 2026-09-13 04:19:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fb048169-c595-3872-93c2-7fe9f67d9473 | -18.54186 | -42.48463 | 2026-09-13 04:19:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0e667228-30db-3990-8ebb-4bf46333d16e | -18.60659 | -48.65761 | 2026-09-13 04:19:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f6ed58cf-9f67-3cc8-afc2-aed85168a8c6 | -15.56818 | -53.78218 | 2026-09-13 04:19:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39dffbcc-4631-3215-87d6-3a83d98401cb | -15.55499 | -53.79734 | 2026-09-13 04:19:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa353c59-f069-31a0-921c-b50467df05da | -18.60939 | -48.66226 | 2026-09-13 04:19:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 956ac865-d58b-338e-a3a4-855932f8ac17 | -15.5686 | -53.78539 | 2026-09-13 04:19:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63fae37e-8b34-330f-890e-db47fccec6ae | -18.6059 | -48.66164 | 2026-09-13 04:19:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 998c0466-2281-3a4b-9eb6-0c5e064b9823 | -16.2667 | -50.22562 | 2026-09-13 04:19:00 | NOAA-21 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b7e0bfca-fe7f-3356-b35c-ee2789b84f4c | -15.55114 | -53.79074 | 2026-09-13 04:19:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf7e5685-6429-3ae7-a0db-10c18e32b683 | 2.51148 | -50.85001 | 2026-09-13 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 990e2f1e-2fdb-33b0-9117-d08c380c9fce | 2.51448 | -50.84516 | 2026-09-13 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d54c65d9-80a0-393a-a7ef-b6e85b027a50 | 2.6704 | -51.04247 | 2026-09-13 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78b97757-0c33-3d5c-bb1b-54ba181694a5 | 2.51515 | -50.84943 | 2026-09-13 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a298c46-5634-38de-bee9-1adf51d208a9 | 2.51582 | -50.8537 | 2026-09-13 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3949dc0-21f8-3239-b767-7f2e8c764e70 | 2.51081 | -50.84575 | 2026-09-13 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f870cc28-05e9-3a33-9b10-caac14cc64bf | 2.66876 | -51.04049 | 2026-09-13 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2280de60-7dce-3f03-94de-d038688fcb5d | -5.55388 | -43.43912 | 2026-09-13 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d514b155-97e5-330d-bcad-478d30f3538f | -3.40455 | -59.24753 | 2026-09-13 04:49:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cc615398-4724-390c-8acf-0aad88f329e8 | -4.86338 | -56.001 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79efcb95-7dc3-3ee6-af44-5b91405e4c5d | -3.16143 | -48.61323 | 2026-09-13 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cd9ae97-9329-3bb4-8cc5-2d7407f3bc98 | -2.95177 | -50.4103 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac7f2eba-5632-35f1-b280-ba4a4af3f9bd | -5.12655 | -55.96999 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aadbe877-29fa-3db9-8244-6fcb4107f59f | -3.87283 | -51.18122 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17e7e0b9-7456-325f-bcd7-893748259aeb | -2.67293 | -57.53156 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c177b1a7-d818-3018-96c0-456f5ea987b9 | 0.14851 | -51.46227 | 2026-09-13 04:49:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38b77503-4246-3178-9816-06653ffa0ade | -7.38189 | -45.34949 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84d43789-8fff-3d6d-8e39-752259bb4db3 | -6.23321 | -51.69697 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bc34ce6-a6bd-3f92-a43b-181890172d57 | -3.85184 | -50.6146 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01dd0a63-7b43-3419-ab03-cd7fc48cdec3 | -7.02202 | -44.62761 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b43a9048-9caf-3e2c-8dcc-80bfe2de2881 | -5.18272 | -49.35087 | 2026-09-13 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a948d55b-f61c-3d7e-8ae6-3d8c9d50622e | -2.67928 | -57.52602 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 650a0058-b7c0-31d4-ba9e-ce68f4f0cafd | -7.01695 | -44.63401 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a8d6b5cd-8ca4-3add-8edb-b341fd0b18a0 | -5.76806 | -45.09421 | 2026-09-13 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0f95433-b8d6-3e17-9fbc-ddf0f8e3b5d7 | -6.23509 | -51.68548 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59708270-ac52-33c0-8726-a3b98a70d46a | -4.10897 | -54.90329 | 2026-09-13 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47e0d6ac-fe32-3371-b6fb-1f060fd4481a | -3.2164 | -48.97216 | 2026-09-13 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 208a127c-c443-3a5f-8efc-a9b0547d89d9 | -6.72887 | -45.41461 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b7cfeaf-3265-361f-89ba-6f7f5cf9aa3e | -1.65964 | -55.18398 | 2026-09-13 04:49:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dede19fe-1acd-33a4-8eb7-ea2c2da7e5e2 | -2.6824 | -57.53978 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0f695ee6-662e-3654-9eeb-cec13b201cbc | -6.76038 | -45.456 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2d1139f-a385-363c-bfd8-a2cbf0c7421d | -6.69412 | -45.90299 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 20ab793f-a9ac-38cb-aa3d-22d14aa495e7 | -3.59985 | -59.07523 | 2026-09-13 04:49:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62215fac-3c33-3c9a-85ea-60d6a6193e8f | -6.22688 | -51.692 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12db352a-46bd-3f76-99ab-8a226d40514c | -0.73469 | -48.04051 | 2026-09-13 04:49:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13c64d12-0494-3afb-b7b7-592b4ec95466 | -5.74151 | -46.15078 | 2026-09-13 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dbf8a54-3877-3996-b2c2-8c3289616cbe | -2.9138 | -54.11464 | 2026-09-13 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a2ef407-5895-3c7c-a8c7-67d24eb6fe8d | -3.9545 | -47.61507 | 2026-09-13 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cda01fe-7746-31b7-a81d-da9646588cb9 | -3.04614 | -51.25318 | 2026-09-13 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ec73839-d8a9-3dc4-8fe3-bc28235e6d0a | -4.4022 | -42.33645 | 2026-09-13 04:49:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b64fdc4a-0f0a-323f-8487-2ee235347da5 | -1.7364 | -55.84798 | 2026-09-13 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9710e3f-d4bf-33d1-8311-cc6655acfa77 | -4.60635 | -46.31641 | 2026-09-13 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12c9993b-fcbd-30bf-b513-a86ad0d95d35 | -3.91055 | -55.735 | 2026-09-13 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f16d043-6153-3481-a61d-74481e40708b | -2.93871 | -50.49113 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e178d56-ab77-3782-b273-110f6f823732 | -6.85924 | -47.42529 | 2026-09-13 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65085fc6-4dbf-3ff2-8201-879847ea1c50 | -2.71971 | -57.64302 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3c9225a-5fa8-3471-8ac2-c4152a3091dd | -2.96261 | -50.40826 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b937008-4d34-397e-98af-71c425ee07bf | -5.81903 | -53.80725 | 2026-09-13 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98aca0b0-3aac-3454-9300-89fdb4023a7c | -2.82207 | -51.34413 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62d8a427-e03d-3f74-a687-c9efdd6cb8f0 | -1.20695 | -47.60427 | 2026-09-13 04:49:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README29.md)
