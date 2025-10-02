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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3607e186-0c01-39d2-9ada-61b3ad6f3d93 | -13.75746 | -47.99225 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75469516-3fba-35b3-bb4a-ecd2e39fe934 | -11.5933 | -47.22897 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0432dcd3-1848-3926-8b71-81c92c26bbb5 | -13.75729 | -48.00761 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2cdb3337-9bc9-3dd5-b5a6-3339c4ad830d | -10.82307 | -46.61691 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 47eb7903-cd93-3bc3-8d5c-b7b9814f7fa1 | -10.94593 | -48.55904 | 2025-10-02 04:51:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 454fb788-71f1-3b41-959e-91b6ff2ad68a | -13.68556 | -48.06923 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12b65d1d-770a-30bb-bf86-4da243ce53df | -11.06746 | -47.81911 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 980e3c65-dfb8-3f56-8b10-7f9b0ad4caf5 | -13.75681 | -47.96466 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1c1adef7-37d1-34f7-bda1-78acc5352420 | -14.31878 | -45.98354 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ddf3dad-6d11-32d0-9993-eae2b315da82 | -15.14857 | -48.38938 | 2025-10-02 04:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2c81321-73f3-3f59-a87d-533995be9291 | -11.85815 | -48.08572 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 444678a0-a532-36c0-ba42-675c2e9729db | -14.8862 | -48.31602 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4eb5ed3-0e13-32b0-ae57-a65ea1659217 | -12.76309 | -50.59285 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a0236db-19be-3cd3-8e7a-f600c852baec | -11.6215 | -45.05356 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0d8c5c4-4ace-3460-8222-6e4d135ab068 | -16.03841 | -50.89651 | 2025-10-02 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c31e6f63-e272-3994-8c03-0378bd6d6054 | -14.31311 | -45.9885 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 613a18ef-21de-325d-b912-0e728c6870f3 | -13.13075 | -47.42152 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03029304-2d2b-3d1e-8cb2-2d439310bb3e | -14.59248 | -48.33274 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c89cf99d-918d-3be4-baa9-a1e55e7af80d | -14.18439 | -46.66053 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38b61eb6-9812-32c9-8976-cbbb5deae573 | -14.68784 | -48.1082 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2177e175-284d-3672-83b8-8829f4023493 | -12.92167 | -54.72964 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ce56165-ff39-3ef2-ab4f-1aef03790009 | -10.82046 | -46.60228 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a9e56ba-3b66-380b-96c8-42be34dd7794 | -10.82228 | -47.96802 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28bf1845-9d0e-3a55-9faf-ee9e67fb7eb0 | -12.42587 | -44.09789 | 2025-10-02 04:51:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dafed2b-61f4-3aca-88b6-bcb5180a5d44 | -12.46305 | -54.3266 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 443094e9-81c0-3856-99ea-fd7e2b1f9cd9 | -11.57467 | -50.16936 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b131cc4e-cb78-3196-8740-dacd0feea3d8 | -13.74592 | -48.70655 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 507d9590-1605-38fe-b4df-3054e8920e31 | -11.07999 | -47.85203 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe4d8fac-c35a-32ec-ae2e-d7a307066ba5 | -9.42125 | -47.3566 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4c366ea6-5b3e-3ac6-91f4-fe9468a512e2 | -13.17347 | -47.81116 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41508014-dd73-33b3-b3b7-276871ae3d42 | -13.79656 | -48.04383 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 039a6558-017a-3245-ab42-af8a000c7008 | -14.89103 | -48.31248 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d58e968c-bfb2-3ecf-aaee-bd7cfc3db8a4 | -10.7574 | -46.14172 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79635a91-2494-37ef-bb9d-2050143507ab | -11.45562 | -44.96627 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dfff014f-fb59-394b-9274-b41e420905b0 | -14.87356 | -48.29583 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22bcf0ce-43ad-378e-9d17-70a6d6c370d0 | -12.90436 | -54.75235 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc683bcf-2cce-3bc8-a484-9233cac2d380 | -10.82242 | -46.62156 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 40ffd455-93f5-3770-b581-0d7fef48df52 | -14.70241 | -48.21018 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 56fdf36c-1a07-351d-946e-e8c05be8c9c8 | -15.93643 | -43.34313 | 2025-10-02 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2cef4913-2e40-39ce-a852-80995ce87b50 | -16.04271 | -50.89295 | 2025-10-02 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c05f6171-d118-328c-afd2-dde4743e25a0 | -15.26403 | -49.30254 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ea4d419-0a4a-3d89-8011-12a2c380fa14 | -14.40654 | -46.10307 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4859b7ff-313b-3e43-912c-907100cc5c3d | -11.16302 | -47.26611 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c524297e-f1a6-36a2-a744-e9d84d9ee570 | -14.8983 | -48.30766 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37b25e93-b219-3e56-9f21-4b4669a0404a | -13.36539 | -46.62742 | 2025-10-02 04:51:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4247217-fbbb-395f-b621-13cc0efcb792 | -13.16329 | -47.85476 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8a253eec-ea63-3282-a17f-1c9b6aea0640 | -13.42093 | -47.80078 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9f47df1e-f628-33b9-af02-ea35b9778e79 | -14.31392 | -45.98194 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0a554d4d-e95e-3536-8aaf-90fe5e26ec99 | -14.42434 | -46.1231 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a17ef6e5-65e2-39ad-9ff4-2f6f80ee64e3 | -14.41284 | -46.09243 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e5ccfe3b-0234-3cdc-8218-e914e4f0680d | -13.40081 | -47.78485 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| b428cc25-4641-338f-b231-ddef2451295c | -15.93082 | -43.33799 | 2025-10-02 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 64076710-ac24-3492-a00e-cdd1a567d25c | -12.85476 | -47.0359 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9331097c-7293-3ef0-8d62-70620f2b54a7 | -11.18057 | -47.26836 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7ea9915e-5ac1-317d-bd56-4f85560e6c30 | -15.27784 | -56.77384 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20ae89e8-ccfc-3582-afb8-704d3750d234 | -11.08182 | -47.80882 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05777d98-1503-3fbf-b481-4d087691ae71 | -11.86732 | -45.00788 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45b480df-1cfe-3a59-8795-04bed59d8921 | -15.15627 | -52.79491 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51570572-5ffe-3ac1-ba55-004c2602ffee | -9.39893 | -63.69551 | 2025-10-02 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 352826d1-6fe8-3422-a7a7-6dc068ccee23 | -14.22158 | -46.11628 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f474cace-37aa-3233-b3c1-949203d3aa9d | -10.24279 | -50.31575 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c8f62344-78d5-3209-bfa1-4bfba65e7cbc | -13.37533 | -47.2994 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c878a61e-fb5b-3684-8516-34adf5d24f2a | -14.43165 | -46.35223 | 2025-10-02 04:51:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6f17417-f90b-3edc-988d-f4429bb9d6d5 | -14.65932 | -48.12304 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cea777d-c4bf-33db-8de9-dab8d36f7d79 | -15.50654 | -45.90382 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5177dc89-2749-3569-9978-63daa0a3af0a | -15.27937 | -49.31135 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04e0f516-0524-3211-a57c-f04448fca910 | -15.60263 | -46.91535 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71b8486a-b2af-31fb-8dae-4f6fc33713f0 | -11.4659 | -44.9678 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cc025df-ae31-3496-b407-6688d552b3ab | -11.78179 | -47.39651 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c7a6364-0f2a-394d-bc50-4ca900983225 | -16.0399 | -50.85907 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 61807c27-f02d-36cd-aede-1698a43b606f | -11.09252 | -47.82546 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9abdcd05-7ee4-3028-a34a-437470ced64e | -12.92499 | -54.73019 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2ed66d6-b4d3-3cf2-b54a-80e00789cbb4 | -13.69925 | -48.61499 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2bfb7f7-abff-3b1d-b4bd-aa47bb9927e9 | -14.48725 | -48.41455 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c5151c1-f7c1-3d9d-8e30-382a1b251a08 | -15.20446 | -48.16355 | 2025-10-02 04:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df37b365-22f6-37d7-9668-61fe866516f6 | -9.92908 | -43.71183 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cfdf31f-91ad-3cf5-ba8a-760b4e333df7 | -10.64375 | -47.45601 | 2025-10-02 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5591dfa9-774a-3523-b85c-71d2e2caaf2d | -12.83823 | -46.94791 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b21f2a98-782c-3786-915c-c4ab0aed7192 | -16.03922 | -50.86384 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4be651b4-f263-3e4a-bb0b-0c749dcad8b6 | -14.30463 | -45.89259 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 000d1d02-805d-3b91-aec6-6cf24e4ca1b0 | -11.43795 | -43.88554 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a030130d-de5d-3b39-b7e4-b3465ab7dad8 | -12.84901 | -46.93671 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa14c1dd-85fb-3bc2-8dcc-3b0b785f864a | -14.69356 | -49.62255 | 2025-10-02 04:51:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38183f3f-c4ec-3afb-86f3-43c19219c79f | -11.79875 | -44.96828 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20867dcf-b816-3525-8e83-f18febf900aa | -14.18374 | -46.66573 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cb8b06f-a427-31cb-8236-1d257b7164de | -9.94466 | -43.72095 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c5bd911d-3fd6-3b13-8a76-f567e5cee901 | -12.6882 | -46.91811 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99e7e152-5ce8-313b-bc8e-4ea643c12c7c | -12.4263 | -44.09419 | 2025-10-02 04:51:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eaed15b0-1fdc-33bd-b79e-0e64bd3cee62 | -11.0336 | -47.81541 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47b90959-2b3c-3a79-a2c5-b23b35d85627 | -14.47869 | -48.4138 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21a23ebf-a106-3a12-ac6b-3f81b75c4946 | -11.21864 | -48.21592 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78cd5506-8713-3fd0-a0a5-070733f5f1b9 | -15.2699 | -47.90401 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99ff79da-3a5f-3efc-97a5-13467466b676 | -13.75022 | -47.99411 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 95d44f97-af45-3d42-a299-52ed43698553 | -11.67487 | -47.49455 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f46ef716-b8f0-34c5-a194-7c0958685433 | -11.47986 | -44.99729 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 786c2a54-2989-3c16-8c4d-2ab8b33d2ad1 | -13.22728 | -48.43642 | 2025-10-02 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf912c1f-73bb-3af9-a703-9d8e3c2eafc8 | -10.83462 | -46.63871 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f8d80a1-1e84-3165-abfa-4155365336dc | -9.92461 | -50.48875 | 2025-10-02 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 039fbb5f-5496-3707-be88-5c6658308749 | -11.79025 | -47.56759 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7ffaaf5-477f-32ae-b0a1-33e702e905a2 | -10.9929 | -46.60695 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |


[Clique aqui para ver as próximas entradas](README118.md)
