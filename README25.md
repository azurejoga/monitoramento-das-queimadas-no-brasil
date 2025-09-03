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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60e61197-77f7-3187-96b6-6c36a3eaebca | -10.73819 | -44.80614 | 2025-09-03 03:34:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da9d5ada-a6af-3ea1-8691-e5fc210d1c88 | -14.58204 | -48.04551 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4243c0d-9a69-384e-8f76-d7b1523a5a84 | -13.31637 | -46.82444 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0419cf2e-f6ec-3522-ac53-e21085d829f1 | -15.09994 | -48.12672 | 2025-09-03 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee369f0a-20c4-3259-9c10-680a451c0541 | -13.47968 | -46.82747 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 944df6f9-7aac-3863-aa80-c46e438af2f7 | -14.78022 | -48.14938 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0459b06-80d7-3cb0-926a-5113741729bd | -15.55381 | -48.37554 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 052cb7ed-ccfc-3f40-9fea-df440af0e719 | -14.77294 | -48.1487 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0292160-3ab9-35b0-ae9a-cc5aad91549e | -15.54428 | -48.35208 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 962cb0e7-c966-37fc-b48e-54f743be7e08 | -14.56059 | -48.06163 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 680d8d56-fa12-33ca-abf6-aed9e8fd09ea | -13.50638 | -46.93325 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac5dad57-1a29-3ff1-ae7d-3ded95cb0e43 | -11.12129 | -44.64126 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 50a5e49c-e6df-3d27-8523-68ff340d106a | -10.73536 | -44.80778 | 2025-09-03 03:34:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddbba771-7f62-3dc1-a071-5f98568ed7fc | -14.05879 | -44.56358 | 2025-09-03 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 679623e3-0df8-3d49-97f6-6c397cda5b47 | -12.92183 | -48.08835 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b6c3ac5-79de-3b42-8ccf-0d806dff7181 | -15.55558 | -48.36772 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b9b7354-4348-342c-8949-e0331b30da6d | -12.6771 | -44.75316 | 2025-09-03 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51dba9dc-3f72-3b6f-be81-ee91b8d1651a | -14.78033 | -47.51571 | 2025-09-03 03:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a12bce55-9e68-3596-a339-a3b6f73ac691 | -13.48749 | -46.82388 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54b0207a-414a-3e59-a128-fdf50b86ef28 | -11.91337 | -46.67279 | 2025-09-03 03:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3af0f67-07ad-3b31-b298-e71a45ea69b3 | -14.78913 | -47.50848 | 2025-09-03 03:34:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01e6df04-f82f-3038-a325-a3afa5658cf6 | -11.05789 | -45.40609 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca52b629-c676-3fd9-9a75-cbef27883a47 | -12.96214 | -48.07593 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0282d881-237d-3909-8fc5-c4e4bcd06396 | -11.89379 | -46.66706 | 2025-09-03 03:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0c2693a-6152-3741-85ea-258af1ecbbff | -15.55905 | -48.39791 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 910d2493-863a-32f8-a976-64b1f1b599a8 | -14.76515 | -48.13805 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10e59597-f768-375d-b5bf-7745e601654d | -11.11549 | -44.66241 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a0c909a-3476-350f-8783-1a6431d2e779 | -10.14654 | -46.26854 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb8ffe8d-a85b-3dda-b1be-b82f7d12b5bf | -10.73432 | -44.81305 | 2025-09-03 03:34:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 50711e87-ea4c-3f19-83c8-00b138086a37 | -15.54826 | -48.36724 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e937923-346b-3ee7-a63b-59f4997d5d89 | -13.50526 | -47.03846 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12ae07ef-dbaf-3a62-bd79-b4877e114738 | -15.56134 | -48.40807 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b084df22-79cc-3727-bacc-a92ac9cca431 | -10.1384 | -46.30425 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cb59cff-4937-3c69-bdfe-e2c1e96c3cee | -10.99304 | -46.83001 | 2025-09-03 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f83501e-09a8-31b6-ac98-7a57eee7891c | -15.55161 | -48.36594 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 72cf7924-65fc-32bd-8a11-3dcf0e800c4c | -15.56972 | -48.31987 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18fdf6d3-933d-3d2c-b047-75d084166a11 | -10.73186 | -44.80517 | 2025-09-03 03:34:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2762f002-aa9e-3c3f-b006-3eaef7785fd7 | -10.73638 | -44.80257 | 2025-09-03 03:34:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e50b0cfa-fdba-3114-9d64-1663433133ed | -14.58591 | -48.04755 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3ce0157-4970-3a9d-ad5d-1a3ff3b96434 | -13.5008 | -46.92628 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8096fbb6-8303-3cf6-8a17-7f3274358681 | -12.99699 | -48.09317 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81546584-d421-3160-b7a0-86813ef4472c | -10.13518 | -46.25354 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13cbd949-60ef-3f83-b170-83841f2a453e | -14.57873 | -48.04651 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c26e3ba-c8ed-30fb-b3c7-59f7e1cb2a59 | -15.55766 | -48.39142 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 37dbaf25-ea30-38e8-89f4-82c92bac58e3 | -12.84182 | -48.0346 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01d4c4f0-e722-3e85-ad0f-213347093f85 | -14.772 | -48.14064 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fabf33e-cb45-32eb-9dba-d2e444001f1a | -11.12362 | -44.66231 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18f85c92-10be-3482-9c05-30fd9f408467 | -11.05149 | -45.40443 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e6ee3dd-bdaa-3580-99b6-6f72b35290c4 | -15.57651 | -48.32257 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4915f4df-129e-34da-933e-c30557093b2a | -14.8008 | -48.22287 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b43ba56e-f49f-3cac-b5f9-2ccde54910e6 | -11.06076 | -46.89596 | 2025-09-03 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab84a452-b7d7-3d84-af5f-27b5ade1805a | -12.84205 | -48.03387 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 41fb0ffa-ffa4-380d-9f1a-d2adcb7ec115 | -14.78582 | -48.15742 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 50c1accd-a5fe-3bab-b76b-9bd3c9974c2a | -13.30862 | -46.82308 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 981afa6c-19d9-3e5c-bb1d-e57fd244f2a3 | -10.14005 | -46.26131 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 194dfba9-1db2-3e3d-a5fa-e9e038a2d108 | -10.73604 | -44.81673 | 2025-09-03 03:34:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cbfc394-d88d-3e01-8517-459525fa08dc | -14.77879 | -48.15564 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19e20124-de05-3ae9-aa5c-e298d7aefef6 | -17.19149 | -46.06634 | 2025-09-03 03:34:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdd067c0-2c2e-3a6d-a55b-5e479f909ac2 | -11.37965 | -43.61165 | 2025-09-03 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97d605de-e49f-3414-b9fb-1f58be5f8e1b | -15.5542 | -48.40675 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ee5e7896-2394-3f87-b2ff-387498e1b187 | -11.12264 | -44.65884 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20eb57fe-cf4b-3da0-9249-961dc1cdb56b | -15.55756 | -48.42491 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| bbfb4514-b459-38a9-a75a-87b44ba33c3d | -12.85169 | -48.0244 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14f8b479-a5ca-338a-a05a-8560dc5b37d7 | -13.90053 | -48.11683 | 2025-09-03 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c653e295-f459-34fd-ad36-880f5410124d | -15.55725 | -48.4057 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 025feff3-537b-353c-8ef0-8d60ff629636 | -13.9023 | -48.10902 | 2025-09-03 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b246a486-c671-3aaa-8b91-bf633602b1da | -11.11726 | -45.11671 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a76df0c-2b16-3f3a-ad16-f984f41b0e43 | -11.92164 | -46.66748 | 2025-09-03 03:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a29eb3ba-dced-3ff2-8354-2680e9eb4acc | -15.57307 | -48.32298 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3955bbb8-3850-3cb7-8e0f-9ea7e7cb40e3 | -13.33512 | -46.83122 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4435b09e-e277-3976-8cc0-619e335634f8 | -14.81023 | -48.2141 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7267eeb8-1d70-3784-b5fa-795fe398e75b | -11.38671 | -43.57533 | 2025-09-03 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b60b05a3-b17a-324c-a0d0-cde46c9b0c34 | -11.11825 | -45.11187 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2131b3a-9c47-3aa4-b737-1ff9d01f4503 | -13.50737 | -46.92863 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 379f7329-3425-32f0-9866-0877e9c7d600 | -10.99009 | -46.82778 | 2025-09-03 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b988dc3c-e8d2-3772-bd1f-9910d440bed4 | -15.72031 | -47.66613 | 2025-09-03 03:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e16f341e-488b-3279-9202-24acb857f0e3 | -11.38797 | -43.63053 | 2025-09-03 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ff8b936-f7b2-317d-b3c1-583f09aef567 | -15.10687 | -48.12872 | 2025-09-03 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f85910a-9b86-3240-945b-2f0a1a0c5e5f | -12.95386 | -48.07898 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d55d0be6-e03a-3836-a74f-7d0e4bc419a8 | -10.14567 | -46.26885 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7f3f7c0-1a53-31e2-af25-8853c2522817 | -15.54883 | -48.31417 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 51c1fa0c-49fb-3317-b139-ec48847e011a | -11.05035 | -45.40995 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55670458-4172-33e6-9596-c5efc2b6c73d | -14.76748 | -48.14004 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 118763a7-b0b3-3fe4-b909-c76907f1fb3c | -15.09145 | -48.13155 | 2025-09-03 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d6df0c65-eec6-3fc3-b3bc-3d3eab062b05 | -13.51482 | -47.02734 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84080ac5-b43d-34e4-85d0-4897c14d1f65 | -13.4932 | -47.02847 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2201dcf5-d7e4-3c71-b957-ed2a6f159492 | -11.05174 | -45.40705 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e19e07dd-86f0-3b02-b026-ae1e2ec1b504 | -15.56047 | -48.42392 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a6d87ac3-4054-345e-b5ec-544642de59f3 | -13.3231 | -46.82599 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d02e4b1-91a4-38f2-b962-0b9cffd84d1a | -15.55182 | -48.39701 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6ec8e90b-4dd4-3397-a728-8e53ef732013 | -13.90746 | -48.11345 | 2025-09-03 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de90b62b-753a-384e-8411-92ea6491629c | -11.12045 | -44.63784 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| de79e8ec-b30c-3c5e-b859-a06c228be047 | -11.11413 | -44.64503 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b22e1e71-d9a0-3a41-90b1-1fb49a479ba0 | -10.14519 | -46.27531 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a32b7c79-0ea7-3d25-ae42-00b6f6732373 | -10.14088 | -46.26093 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b4e00a6-46de-3fd5-be63-29682e32cb53 | -11.12357 | -45.11818 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc73aea0-bb75-3919-abde-f563b6a80f64 | -17.53929 | -46.62116 | 2025-09-03 03:34:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bff43f55-4669-3d42-9556-529928cd28ab | -12.85143 | -48.02565 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e87b1e2c-5407-358b-b171-14d872f1013c | -11.12296 | -45.11492 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cf5121aa-ecfd-30b2-892a-bef37927424a | -13.0092 | -48.10693 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README26.md)
