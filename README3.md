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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 841ef31e-83a9-3e12-a366-9e28e864c816 | -23.237 | -51.28313 | 2025-01-07 04:31:00 | NOAA-21 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 32e01ba5-2bc7-3aa7-a8d7-282c4b977832 | -20.71602 | -55.56123 | 2025-01-07 04:31:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 485a14c6-86e2-3cfb-b0be-579e893e60aa | -22.54786 | -47.31331 | 2025-01-07 04:31:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03f3b342-bf6f-3126-a943-01df4f9c3645 | -24.08325 | -51.01945 | 2025-01-07 04:31:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 409c1514-0099-3abe-9f10-c73df46517a0 | -20.96503 | -49.75698 | 2025-01-07 04:31:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 647827e1-753c-310a-8db8-fb9f4ba28945 | -24.08265 | -51.02322 | 2025-01-07 04:31:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1f3af387-2b8e-33f5-a23e-73cf0742ca8f | -21.83806 | -56.39413 | 2025-01-07 04:31:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0d89749-9d83-3322-81c8-d449d7c0e3b7 | -20.95817 | -49.75628 | 2025-01-07 04:31:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3fb5bbfd-e01e-39d5-b6f5-37440da1e215 | -20.70561 | -55.32322 | 2025-01-07 04:31:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6813e6d7-5f92-3933-9dbc-5787b3ceb9c4 | -23.34005 | -46.77271 | 2025-01-07 04:31:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 36c23bc6-fbb7-3af1-aa8a-71980dcf807d | -21.26035 | -48.59451 | 2025-01-07 04:31:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c2d262c4-81f0-3e13-be91-540dca2a2ab6 | -27.37643 | -51.64962 | 2025-01-07 04:31:00 | NOAA-21 | CAPINZAL | SANTA CATARINA | Brasil | 4203907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e120e460-16c2-3997-8534-a4249161f102 | -21.257 | -48.59393 | 2025-01-07 04:31:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7df88577-a1f7-3c4c-a7fe-35f0a5f2009e | -27.08802 | -52.59118 | 2025-01-07 04:31:00 | NOAA-21 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 78b8b617-27e3-3a16-9fc2-60d012c470b9 | -21.56273 | -54.2005 | 2025-01-07 04:31:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 59b2fd2c-464f-3795-8611-b86361d45775 | -21.2503 | -48.61609 | 2025-01-07 04:31:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7636f8a6-9733-310b-b096-45cc150f02b2 | -20.76421 | -46.76983 | 2025-01-07 04:31:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2cf9c93f-65c6-3997-8bc7-c25394d2c3ad | -20.72013 | -55.56211 | 2025-01-07 04:31:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c86ca38-d6b1-3965-ad03-1d8150446354 | -21.2961 | -54.39698 | 2025-01-07 04:31:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f115c9df-a38d-3991-a3f9-84a60d94b629 | -22.27285 | -49.63161 | 2025-01-07 04:31:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e198298f-c1a8-391d-8f49-6fce6d328f99 | -21.19451 | -44.93906 | 2025-01-07 04:31:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a874249e-f728-3feb-b047-a23cc8e71913 | -20.71819 | -55.56097 | 2025-01-07 04:31:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2f4bdf6-0cb1-35e0-8144-0c4728956eed | -21.55897 | -54.19975 | 2025-01-07 04:31:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 25b9acfa-e4e0-33f1-a015-73ee9ae5f376 | -20.96172 | -49.7564 | 2025-01-07 04:31:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d9deddcc-37b3-3b2e-a7e3-e761c58f38ce | -21.55521 | -54.199 | 2025-01-07 04:31:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82e48adc-3699-3695-a01d-f9409021f41f | -23.34053 | -46.77074 | 2025-01-07 04:31:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fabffcba-c257-3b6a-95e0-72789fad6f13 | -21.54392 | -48.63385 | 2025-01-07 04:31:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5eed68a6-9726-317d-b369-ecd23996e44e | -23.5948 | -47.43867 | 2025-01-07 04:31:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ca247141-fa34-3f41-ad0c-e17644711608 | -20.47883 | -53.67598 | 2025-01-07 04:31:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63d9c3d5-9b47-363d-9bb1-9b183073d612 | -27.37582 | -51.6535 | 2025-01-07 04:31:00 | NOAA-21 | CAPINZAL | SANTA CATARINA | Brasil | 4203907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5ceac09d-a349-3088-97de-ee06b913e49e | -24.08385 | -51.01568 | 2025-01-07 04:31:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3653b827-bff5-3efd-9f53-86f0b464ef7b | -21.56559 | -54.20619 | 2025-01-07 04:31:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c25a5a2-6c10-30b6-ad8d-1755fd916292 | -20.81749 | -47.59323 | 2025-01-07 04:31:00 | NOAA-21 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fce6162-02c2-3e3a-8a08-a6b1f7599998 | -22.54144 | -48.81318 | 2025-01-07 04:31:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ba3a1e4-78b8-332d-835a-930a7b73e446 | -21.37312 | -48.56664 | 2025-01-07 04:31:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| be031bd1-6d43-3986-ae5b-32c87c76e956 | -21.83381 | -56.39322 | 2025-01-07 04:31:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca9b1df4-f052-35fa-af52-7fbb4a1959f4 | -21.37282 | -49.07232 | 2025-01-07 04:31:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b3c2414d-4681-3996-8dc2-12ef8d25077d | -20.95875 | -49.7526 | 2025-01-07 04:31:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4766c28b-5016-33e9-8284-a19088e97482 | -29.6214 | -51.95876 | 2025-01-07 04:33:00 | NOAA-21 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 240fc53c-fc21-322d-9d77-548e9e807e66 | -27.47282 | -52.90203 | 2025-01-07 04:33:00 | NOAA-21 | TRINDADE DO SUL | RIO GRANDE DO SUL | Brasil | 4321956 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0818976d-726f-3319-b969-ab0f657c760e | -28.13699 | -55.46753 | 2025-01-07 04:33:00 | NOAA-21 | GARRUCHOS | RIO GRANDE DO SUL | Brasil | 4308656 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 42f080fa-be66-385b-a5fe-97d0395123f7 | -30.46651 | -56.39132 | 2025-01-07 04:33:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 177563eb-9f22-3744-a1c4-373c4a8c13a6 | 4.11565 | -60.51194 | 2025-01-07 04:50:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b81a26b4-b4ba-35eb-b6d7-46d518d2c158 | 4.34771 | -60.88332 | 2025-01-07 04:50:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b0e65772-c62c-39d7-9c04-ba83677797f5 | 4.35288 | -60.87748 | 2025-01-07 04:50:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 749799c5-3d1b-3f64-b272-e93f55029189 | -1.41661 | -48.00978 | 2025-01-07 04:50:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 871ded61-d3fb-37dc-a0a6-78ee11f0b282 | 2.03083 | -60.88128 | 2025-01-07 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65fb0aa1-c74a-37e8-9f89-e8aeeee0ffa7 | 2.02919 | -60.88262 | 2025-01-07 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0025b8a5-4cc6-3fee-b297-e38555cd3550 | 4.34065 | -60.87613 | 2025-01-07 04:50:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53c5fbdf-26a9-3482-99b4-3cf063394f5e | 2.02859 | -60.87877 | 2025-01-07 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe73de19-cf85-31c2-8849-4dd96f11ca37 | 4.34699 | -60.87839 | 2025-01-07 04:50:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fcc60e49-58c5-3009-b776-9e066362fcb5 | 4.35887 | -60.87733 | 2025-01-07 04:50:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5113739-4f63-3967-9acb-300df8259e59 | 2.03026 | -60.87741 | 2025-01-07 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 029c03b7-3ae9-31c5-96d4-2ed3ba95cc74 | -9.28165 | -56.89148 | 2025-01-07 04:53:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fa141a3-7edd-38c3-bbe5-8222394996d2 | -9.28533 | -56.89206 | 2025-01-07 04:53:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26a34584-b03b-3ae9-8254-b59673b589ad | -4.06285 | -54.70745 | 2025-01-07 04:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16328502-f238-3a35-9919-eea47ba3b030 | -20.70578 | -55.32381 | 2025-01-07 04:55:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a11ccef4-ca7e-32f5-b0cb-a20fad2e77e0 | -10.0959 | -55.40924 | 2025-01-07 04:55:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ca8e294-5fe0-3fac-af9d-6516d6239c09 | -23.29995 | -53.24107 | 2025-01-07 04:55:00 | NPP-375D | DOURADINA | PARANÁ | Brasil | 4107256 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9e8a01a8-2355-3617-b84f-04d0b50c58c6 | -21.83747 | -56.39421 | 2025-01-07 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b675d982-f98f-3737-8be9-ca4ab0632469 | -21.55792 | -54.20414 | 2025-01-07 04:55:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2161ae07-da10-37a0-a72c-7d34a7278d26 | -19.33549 | -54.17179 | 2025-01-07 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 09137361-691d-34ba-bb04-507e52b1b1da | -21.88123 | -56.1145 | 2025-01-07 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a20bb32-595e-3f11-9a66-9d249fe3c019 | -12.36692 | -52.49055 | 2025-01-07 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a063e71-6646-3d1f-97a6-e24ebea49a3f | -21.8308 | -56.39301 | 2025-01-07 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5aa7b1f9-42df-3ff2-8575-53da43aedaa2 | -12.36748 | -52.48682 | 2025-01-07 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 058c5a9f-760b-366c-9f95-5f29abdbfd29 | -12.37033 | -52.49108 | 2025-01-07 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f3cf905-e8d2-3ee0-b79a-bffb54e6e596 | -19.58518 | -49.3714 | 2025-01-07 04:55:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 90d82a89-9130-3aaf-a45b-5d08b93345f8 | -21.10331 | -51.20576 | 2025-01-07 04:55:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 41cb65cd-95eb-3093-8493-4cf350e5144e | -12.37374 | -52.49162 | 2025-01-07 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bea831e-b9f3-3907-b80a-f7fdb1b4fe47 | -19.33208 | -54.1712 | 2025-01-07 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4eb7baeb-a000-3b89-9ff0-f1bac82e33f7 | -21.83413 | -56.39361 | 2025-01-07 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63c09f03-c4e9-3a4f-bc05-08916ec34b43 | -24.24282 | -50.74102 | 2025-01-07 04:55:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4467c06e-2b6f-3c70-a4b7-61805181476f | -21.56197 | -54.2007 | 2025-01-07 04:55:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8622ca04-eece-308f-b148-6610559280ca | -20.72383 | -55.56442 | 2025-01-07 04:55:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a04ea206-f73d-3af2-9a94-fd1e7fbce5ea | -21.29681 | -54.39555 | 2025-01-07 04:55:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c3f5b52-3784-392c-b9a6-153a7104834e | -19.5808 | -49.37075 | 2025-01-07 04:55:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8cf3f0e-cab4-3dc4-987d-18b81e391833 | -12.36065 | -52.48576 | 2025-01-07 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0eff9113-f4df-3ee6-aea3-e8399086da87 | -21.55563 | -54.19551 | 2025-01-07 04:55:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d0d65657-0e27-34cc-bc1f-f8e5507ceaed | -12.35668 | -52.48895 | 2025-01-07 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4191f0d7-ad3a-3c3a-8194-4de502b228e9 | -19.33949 | -54.16768 | 2025-01-07 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72d9dc2c-ee87-35ac-971b-3439452dbdce | -10.09309 | -55.40494 | 2025-01-07 04:55:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe4adbe9-96f9-3d12-95d1-98cabcb7df1c | -23.58002 | -51.44995 | 2025-01-07 04:55:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f66a8fbb-74eb-3fe8-ac48-15728a0eba8a | -19.33947 | -54.16853 | 2025-01-07 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3228c42a-ee1c-3ff8-8fa1-5ad925419019 | -12.35363 | -52.48921 | 2025-01-07 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79225462-e558-351f-abbc-e6e393fa3646 | -21.5683 | -54.20586 | 2025-01-07 04:55:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 221d4ef5-26e1-3054-89b4-af42912d8bac | -20.95762 | -49.75434 | 2025-01-07 04:55:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0b2ce188-9aef-33e5-9727-a11238f1d318 | -21.65453 | -55.59111 | 2025-01-07 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 437b3958-35eb-3078-ac30-834c420534db | -20.477 | -53.67573 | 2025-01-07 04:55:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03f4c6c7-8fa3-3ef7-9f77-a1a9af48d9c6 | -22.10566 | -57.22 | 2025-01-07 04:55:00 | NPP-375D | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8644c0af-c17f-3177-ac81-743f0ad81c5c | -12.36406 | -52.48629 | 2025-01-07 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f05ddeab-60dd-3009-bd36-5a96b6ab5675 | -10.09248 | -55.40868 | 2025-01-07 04:55:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a833425c-4aae-3d70-8d64-cda00132f134 | -19.33892 | -54.17152 | 2025-01-07 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 716b9269-5541-3171-9b1b-4edae75289e8 | -12.37089 | -52.48736 | 2025-01-07 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fa4635d-0f76-352f-bd8b-7630bd4e976f | -21.56255 | -54.19667 | 2025-01-07 04:55:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dda3e562-70db-31e6-bc65-7938cbfcff7d | -21.25635 | -48.59415 | 2025-01-07 04:55:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 430ce09d-d200-356f-8ff9-f785a6d95e30 | -12.35704 | -52.48975 | 2025-01-07 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d7e13ae-6290-35d0-a805-a5af44a3b74c | -12.36009 | -52.48948 | 2025-01-07 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2e41eeef-8b72-371c-ad6c-e4a92bfdd0e5 | -20.71772 | -55.55954 | 2025-01-07 04:55:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dedf22d7-022f-3550-937e-219379900407 | -21.55909 | -54.19609 | 2025-01-07 04:55:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README4.md)
