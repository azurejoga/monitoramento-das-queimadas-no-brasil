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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d4cb7bb-5097-3410-840f-2cc6e25d6d4c | -10.87543 | -56.45177 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 224604ce-26f2-3c68-83be-ae80028b2475 | -11.1212 | -55.44584 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5a422cd-eb63-3b84-8b43-69d09edd697b | -10.08771 | -52.74663 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f60487a2-5748-34e2-8fe0-d846c68b4c30 | -10.8696 | -53.73629 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78ca084b-1065-3d0f-807e-0d80acec6dd4 | -10.1289 | -57.77761 | 2025-07-01 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 249ca637-4d9c-394a-b505-29447f899656 | -10.62335 | -51.79285 | 2025-07-01 05:14:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0fbd533-4622-3268-bdd1-89dd40652009 | -10.87462 | -53.75785 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 739de795-26b9-37d5-8ebe-44067e22ab6f | -10.87356 | -56.45503 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a7a80be-6eb5-3469-bb93-8f63fb5bb459 | -9.25564 | -58.75897 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6299db36-4c2e-3954-95d1-766f72a96c3c | -14.20305 | -45.51903 | 2025-07-01 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 209b8d9d-affe-3090-969d-12ef6f2dcdae | -10.08462 | -52.73847 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1a700665-06f3-3a5d-8131-2a7ce845820a | -10.8775 | -53.73745 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d440bcd-6df1-3c50-b34b-4a61d81f726e | -11.57255 | -48.1463 | 2025-07-01 05:14:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b4800e8-1d0a-3b8c-93d7-a9ce9a88759c | -10.94524 | -55.3096 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7391bbc6-dfc4-32db-bc15-7838577d35c8 | -10.35069 | -57.50214 | 2025-07-01 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 789459c1-13b7-3469-a58a-08d3c5be4f1b | -10.88252 | -53.75896 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98fb8cc0-e293-3c06-bc22-7b59d0b37a48 | -9.98079 | -48.24285 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dbde8686-ec06-364e-96bb-2003d24f318e | -12.62824 | -54.23161 | 2025-07-01 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8059e81c-1e1f-30ee-bec3-91cc76eb58de | -9.11743 | -59.05346 | 2025-07-01 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4d2cd12-c373-392f-97b7-5bc75505d720 | -9.23895 | -58.75628 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0867fe1f-0c1c-3328-a6cb-cc77bfd8c5a4 | -10.06391 | -49.65919 | 2025-07-01 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43e1c97f-8c14-3ebc-838c-8a39d55a9c99 | -10.303 | -57.13604 | 2025-07-01 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4298b9a0-3ff4-3217-8c14-197631c18cc2 | -9.24342 | -58.74976 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64207ca5-b1df-3bb1-b27a-835a5bd0ec79 | -11.57844 | -54.57038 | 2025-07-01 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d892f86-cee5-3c73-86cb-b24d47cf529d | -10.27764 | -52.83368 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c1fe8d4-43d5-3f45-bf7b-72a18e83cb6d | -10.81113 | -55.857 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df86b1e6-9aa6-3737-8f56-75c42e9347b8 | -11.77647 | -54.36723 | 2025-07-01 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4690b24d-305f-3b60-9c47-ba8e49455b80 | -9.97059 | -48.23306 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdb5d2a8-c4c6-3d67-b22f-f09a4ab2b7a6 | -11.20161 | -49.00329 | 2025-07-01 05:14:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b888a032-2aca-32cb-bd3f-6be35f9153e1 | -10.08825 | -52.74286 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c63ef9f-d72e-3be3-aeda-d396c61ab481 | -15.07962 | -48.94355 | 2025-07-01 05:14:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b4264ed-f089-3a73-8ae2-93198b530e5b | -9.1113 | -59.04879 | 2025-07-01 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c45bb5a2-b0e6-395f-bad5-31237d7be37e | -10.81172 | -55.85303 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80f7bb67-a276-3d91-bbc0-5f7a02296b85 | -10.87857 | -53.75841 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0f02408-bf6a-33f1-9f5d-806a87883c58 | -12.63032 | -54.21661 | 2025-07-01 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f0e58ae-de22-340a-845f-215db377dc43 | -13.00891 | -53.4186 | 2025-07-01 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61e87354-adf7-32c8-bd22-d80f069a7671 | -9.70598 | -56.18493 | 2025-07-01 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 11197240-d410-39c9-b312-323ee11fea61 | -14.20234 | -45.52574 | 2025-07-01 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94d3a522-7771-3988-806d-3ef0f9126d4a | -9.25009 | -58.75084 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c1fa49e-df5d-32ea-8d84-b14f4b5b54de | -9.9762 | -48.23405 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9ed92168-3339-3632-80e0-89a161b4a6d6 | -9.24172 | -58.76035 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ee1db67-7a16-3cff-aeb1-afa209ce99ef | -12.82822 | -47.37138 | 2025-07-01 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b81f42d-d1d6-3efb-846d-99d6a57ba808 | -10.30244 | -57.13963 | 2025-07-01 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c0febfc-226e-37a9-96ee-a52b7968ebb4 | -12.82878 | -47.3666 | 2025-07-01 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eee58e05-1f23-3c76-b107-cb90de081cbc | -11.83826 | -47.50824 | 2025-07-01 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd78a869-e83a-375b-b12d-636debb68492 | -9.97314 | -48.23649 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 96f4fb96-a10c-3fb8-8ca9-1a91ae8856fc | -9.70312 | -56.18062 | 2025-07-01 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bd4a6e03-9a46-39e9-8779-307e4cb0d58c | -10.54963 | -52.03733 | 2025-07-01 05:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd9e777f-67b5-32bc-93e0-efd047ad1857 | -11.19443 | -55.91587 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2eded6fd-4448-3f91-830a-7206e9dea6fe | -10.87659 | -56.44421 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b3d73ac1-2da4-3be2-aefd-ad3cf827a1b0 | -14.37895 | -50.32718 | 2025-07-01 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fdcfb5e-8ee2-32df-81f3-119f495ca67c | -10.86888 | -53.74144 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e16bb6ff-ae78-35cd-8dc8-984415970a30 | -10.87485 | -56.45555 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34d082df-02d8-3737-976c-4883b16afcb4 | -10.88158 | -56.44854 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 74ab7f40-f403-3160-9abb-a31e9f32a9bb | -9.23567 | -58.73404 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c01b1b9-b81f-3e7a-bcff-7e9ab502fc15 | -11.20147 | -55.91698 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af215d90-d319-3f71-b3c8-e09f474f2b68 | -12.01851 | -47.7636 | 2025-07-01 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd632ecf-4865-38ab-bf87-7c47018703be | -10.87249 | -53.77299 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90ffb5aa-55b2-33e9-9d0d-4785fff3d8d7 | -9.17309 | -61.40575 | 2025-07-01 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd2eb94e-c071-371f-ab57-9f611f91f30d | -9.24065 | -58.74569 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f2da51a-156f-30af-ac6c-05fcf6e3d23d | -10.12945 | -57.77409 | 2025-07-01 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85eeefae-5400-3aa0-99dc-a92eb2879e84 | -9.23177 | -58.73703 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 924e9051-b341-3d44-b450-6ead712be1d3 | -10.03934 | -59.3605 | 2025-07-01 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d1f3269a-cc74-3c43-a85f-d5cf758c3a89 | -11.58171 | -54.56799 | 2025-07-01 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81b749d8-8b50-3589-a584-6996e4cac7e6 | -10.13142 | -52.34523 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c773c73-fa42-3f37-8359-85c77de45944 | -9.23454 | -58.7411 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a921d19-a8e5-32f6-98b2-0ad4dded936d | -9.2523 | -58.75843 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df219435-9b9f-348b-bd19-81a37b4d1841 | -10.87572 | -53.77856 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 922a5288-000b-3da9-ac0a-4176268637df | -10.30075 | -57.12831 | 2025-07-01 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6814a8b6-49d6-3968-9e30-3665067fc8f4 | -10.87469 | -56.44745 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ea369577-b646-375b-8a41-1fc7d987b45c | -10.17421 | -51.65808 | 2025-07-01 05:14:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7956f1fa-a3aa-38ce-bb1d-ad4554aa286b | -9.02126 | -59.54167 | 2025-07-01 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17f7a8cb-9dc9-36f8-aea7-f38f1f9caea6 | -9.1135 | -59.05649 | 2025-07-01 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee8825c3-b955-3117-a8e9-e88348e2e7c2 | -12.28378 | -50.10898 | 2025-07-01 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a7a9267-830d-3883-9253-be3e2c1ea5ea | -9.65542 | -50.74627 | 2025-07-01 05:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a3dfd94-33b6-32af-8c36-88dea66b1f23 | -11.59836 | -65.1483 | 2025-07-01 05:14:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 312cf6f7-5023-3ddb-8732-e2dc3e7ebd55 | -9.23064 | -58.74408 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bb880ed-20b1-3813-bba4-24593c055a03 | -9.2562 | -58.75545 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f3f113e-5f6c-306b-a463-3a1b5900bf08 | -10.88846 | -56.4496 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03cb5923-0086-39de-8cef-72a3a9721487 | -11.19736 | -55.92043 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee134e53-68af-3566-80b2-ccc51ad7f3d7 | -10.55021 | -52.03304 | 2025-07-01 05:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acb8f4c3-a994-35c0-b248-92ce45245862 | -10.3001 | -57.04311 | 2025-07-01 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afaba138-87e1-3472-9571-be1488967297 | -10.87231 | -49.5456 | 2025-07-01 05:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6513592f-c274-384c-aaa2-9e870c3d3fdc | -9.34857 | -58.83545 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42d533d8-0e18-350f-be71-c7d38f3894e9 | -10.06946 | -49.65683 | 2025-07-01 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5681e0cf-0801-3e35-84c6-1c231f2f6f25 | -9.25174 | -58.76196 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8534f9a3-f7c5-3c31-8c70-a9cb288293d3 | -10.05877 | -49.65849 | 2025-07-01 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54f88e01-f0b3-3a51-b658-36c956a99c9c | -11.02854 | -56.25992 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40589748-b11e-3797-8a70-20cd82275ba3 | -9.97877 | -48.23747 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a2828db-5c61-3d3c-87c3-12a558b99504 | -10.87315 | -56.44366 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a66dcfc9-40a4-3c3b-9d78-7b16b983286d | -10.86602 | -53.7618 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fea0548-8db3-38e3-9c7f-dbfa54f3feb3 | -9.24619 | -58.75383 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9244a7d5-c866-31bd-855d-415f1fffcf83 | -11.83881 | -47.50365 | 2025-07-01 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be2a1f3c-4caa-3816-9cd6-bc8f0f59ae37 | -12.10106 | -54.57222 | 2025-07-01 05:14:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45f415a9-93d4-3428-a245-a4295a348956 | -9.97515 | -48.24206 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48f83a29-d3cf-3fd5-86cd-188c74e91881 | -17.93894 | -48.91985 | 2025-07-01 05:16:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3eca556-5582-34fb-b84a-a3d329f314b4 | -21.13355 | -48.59262 | 2025-07-01 05:16:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 375b4098-9bdc-3387-b958-005cb464f257 | -24.67578 | -49.59754 | 2025-07-01 05:16:00 | NPP-375D | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fd890ead-52f9-307f-9267-13a021d8e3cd | -21.13042 | -48.59172 | 2025-07-01 05:16:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3701bc6d-58c6-34a1-b4ed-f4a841b2a62b | -17.93298 | -48.91895 | 2025-07-01 05:16:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README17.md)
