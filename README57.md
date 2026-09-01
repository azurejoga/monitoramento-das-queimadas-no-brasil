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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14ff39e9-34ad-3b5a-be28-d4a94e80e466 | -7.18666 | -60.68981 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 988b39d0-52cd-3637-b972-6d0acf6ac983 | -7.34569 | -60.58088 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 81fbfc9b-a67f-319f-9a61-e67160d19048 | -3.61577 | -59.06594 | 2026-09-01 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12b13130-2c65-38c6-9739-8bcf2991586d | -6.75719 | -59.15439 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88369ae5-f477-3672-b998-b532d96907b7 | -5.96165 | -53.61147 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 338a4b8a-05c4-38ca-be33-26a348b55410 | -4.58744 | -55.94489 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf60f021-b4a3-3a78-ad90-5235006f8697 | -10.45161 | -46.74125 | 2026-09-01 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a9628ad9-2288-3ce5-a268-47c7af734e60 | -11.20431 | -46.07933 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7e16cb1-3ab5-3dd7-8ca6-a17991a6dd96 | -8.50597 | -54.91221 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf5ef6ba-f082-3b26-828c-cf0f06352123 | -8.80278 | -62.50605 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4ded111-6331-317e-993c-8b5632160acd | -2.66673 | -59.37129 | 2026-09-01 05:16:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be808913-4aa9-37ad-8a28-81d5873ecc89 | -10.78621 | -50.50063 | 2026-09-01 05:16:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8202ea3b-7ae7-3c05-bc27-59c7440bd39d | -5.48669 | -57.15228 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9156924c-e4ff-3950-b0ad-3b5afa15b86b | -6.13359 | -55.64701 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b599ae46-4bb4-3662-bea7-2cf2dda0ccd9 | -5.88802 | -52.15321 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0fa61d89-383a-3533-8034-da409a3a702c | -6.91704 | -55.69992 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d087223-72f0-36f4-af13-b33aae77fdbc | -6.94631 | -55.64395 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14645552-375b-30e7-b12e-45775d3e1693 | -7.19706 | -60.67623 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2013d321-dae1-3ae0-8458-b1bfeda81a79 | -9.67539 | -55.06441 | 2026-09-01 05:16:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7027dc8e-a53c-3fcd-b6b9-b578c775a206 | -10.73281 | -47.95669 | 2026-09-01 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aee33abd-0ded-384d-ad49-62cc1a4779ef | -6.09009 | -57.72242 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35835a1f-af19-3382-9d7d-bf30e5580b2a | -9.38865 | -60.56762 | 2026-09-01 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 803342e5-68fb-350f-86f9-ca5a3a4c6ed0 | -8.84743 | -47.08319 | 2026-09-01 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae8ad58b-96e7-3194-8bb2-0d28e296a377 | -6.60917 | -58.59615 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 255bd3b2-4a72-3e44-9f75-512b924c3fd9 | -10.15108 | -45.69295 | 2026-09-01 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ff4e33f-fdea-3230-8c50-d0520fd016c9 | -6.09414 | -57.87309 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 557d04fa-5467-34a5-8f8f-525c1e34e645 | -11.31104 | -45.20153 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a212a375-bb75-30a6-8d7a-f86b8748f3ca | -4.95986 | -55.85837 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbfeded2-8036-352f-a2fd-6b8bb9a8a579 | -10.1624 | -45.76251 | 2026-09-01 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 26fe445c-801d-3553-a0ff-e4e62f10bc0d | -9.39244 | -60.56829 | 2026-09-01 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5d25ad4-1dd9-3e7d-82e0-f7ca34be8966 | -6.9597 | -56.4366 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71da5108-c2af-3fa9-a805-171d90b54285 | -5.94332 | -57.74055 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcf22f5f-6f4b-3a8a-b3cc-887c248a9cc9 | -9.39623 | -60.56895 | 2026-09-01 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a47dd84-ce63-30cb-955e-bf9a442f0f62 | -9.4464 | -51.56675 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d66c1296-062c-3eb4-9e33-2519c6b185a5 | -5.88749 | -57.76699 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f822b7e-ca5a-3326-a2de-7d00f0311454 | -6.21035 | -53.586 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03890add-aef2-370b-bba0-c7952d779c31 | -10.3237 | -49.11177 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6744217-8c7f-3de2-b916-3af23c8ef470 | -6.11412 | -57.63882 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 886b6187-2524-3448-b549-579a0e4317ab | -6.22633 | -55.49103 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dd88246-afec-3c01-9c54-c2c140181f18 | -4.96593 | -55.84158 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a457bff-94d5-3680-b907-f65778c1230b | -5.89215 | -57.75995 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75d0f2ac-7a99-3961-981c-d66a716c72e3 | -10.74977 | -47.99067 | 2026-09-01 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c70faf92-0dc3-35c6-a789-04c248d99faf | -7.35349 | -60.58221 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 17be9ea4-b316-3e25-ac3e-347dfc49c67c | -6.60144 | -58.59899 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 851fff72-e743-3fab-a7cb-df389cfd0b56 | -8.78992 | -62.47826 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77742351-9d7a-34a8-855a-f6bdd063fcb9 | -9.48472 | -57.02225 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c689e9e3-61a8-39c2-ba39-452989a7aaf3 | -4.79635 | -55.97128 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d78730d-d630-34fc-9ae7-736c9da4c28a | -10.03022 | -44.6997 | 2026-09-01 05:16:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ba3487f6-ad6c-369f-83b7-ab50f9af95bc | -8.62001 | -54.85109 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07acff7a-2ca4-37f0-85a3-c657d433b7aa | -7.0305 | -55.64646 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 138e34fa-4ee8-31be-add1-e284d324f1c3 | -9.40374 | -51.60464 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83bce790-523d-371b-949a-5c04b95b03a8 | -6.93744 | -55.63541 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a36aaa1b-4dd5-3b9c-b5c9-0720e03265b5 | -6.93079 | -55.63437 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8d13d13-a245-3bd5-9d9a-85221730131c | -7.61648 | -55.29364 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dabd5c5c-5559-316f-83af-e1c49c67e97d | -6.35706 | -51.75528 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 950d2a80-850c-358a-a997-838175d38532 | -6.26555 | -55.41532 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e777c073-2cfd-3fe4-bb94-c305c22e7c53 | -6.5992 | -58.59047 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bac40400-b331-39f6-a72f-cc21e942628c | -5.60428 | -44.00168 | 2026-09-01 05:16:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 44a5b99d-a3b1-3473-9179-7e309ad47b8c | -8.93197 | -62.36406 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0c94f5e-2cac-35b1-af7f-f6c2ce7d5e23 | -5.94026 | -57.69424 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6090451-30e1-39e6-9c7a-3f2f6f032040 | -7.41689 | -49.74008 | 2026-09-01 05:16:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c6cac14-de5a-3ffd-a536-dc4c2a208e61 | -8.42043 | -44.99631 | 2026-09-01 05:16:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2576c9aa-1953-3e06-bcdf-d28c862fb800 | -8.12069 | -54.96724 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| beff763d-00d2-3c17-906c-3f04597aa3f0 | -9.18359 | -51.55395 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51e9965b-d70b-3676-96f8-225aea6db60e | -7.62985 | -55.29576 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d3fe06d-1464-32fb-80eb-c0007ee508ea | -4.29907 | -49.09151 | 2026-09-01 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b93960c6-3e19-3e10-bc4f-fe4e3115bc6b | -7.5188 | -47.33477 | 2026-09-01 05:16:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ddb6f98-6e59-3cf8-8934-c581076dc677 | -10.02447 | -44.6932 | 2026-09-01 05:16:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f792e8e-281b-3862-a8f3-b885574036fe | -6.1633 | -52.637 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43849708-d214-31c0-b08a-b26eb2f7a393 | -7.35272 | -55.19106 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d056393-de2c-3280-bb1a-245c30ad6bb6 | -6.61207 | -58.60071 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2dcf6be-344f-3b04-b72a-d990a69870a6 | -8.57357 | -54.79148 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10d9d5ba-ea85-309f-956c-b971d534cb35 | -10.40351 | -48.23157 | 2026-09-01 05:16:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16ad835e-8503-3334-b5df-041dd7361595 | -9.19122 | -59.44829 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2736461-9315-38eb-bf0c-cf629a3f6fcf | -10.32964 | -49.94596 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 681921c7-4cbf-3782-8d45-628498107224 | -10.58907 | -50.38147 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee5a3ae9-91af-35c9-9c19-c934598ebfc9 | -5.97898 | -53.61412 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d00554bf-9685-3da6-a070-e8062c2aa310 | -10.32655 | -50.03692 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7fede5e-6f80-3681-8ae8-8323bf90e4fc | -6.03134 | -58.04213 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bd4162e-8e84-37ed-8f97-4797a275b3c5 | -7.35941 | -55.19209 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d7b657f-9570-379e-a04c-2b79831b9014 | -6.80056 | -59.45985 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa786c6c-2246-3bcc-900c-fe786f99ac3e | -5.95819 | -53.61089 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92f4809f-0e54-3a5c-bb43-3658c7081878 | -6.35671 | -55.86378 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff1d464d-1843-36ba-8845-38bd1d8e306b | -7.4916 | -55.31409 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00c9a92a-ca31-3133-a627-24194f9a6704 | -6.78216 | -59.78721 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb821d5a-5eb6-3268-b96f-4252528518f6 | -9.4836 | -57.02928 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e45bf38a-8561-323c-9b3c-b5b6a0cd2ec9 | -9.16762 | -59.36874 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 568e47b3-1c16-3db2-ba40-43aa09c2ba0b | -5.56496 | -60.18315 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4a4429c-f062-376f-a298-4fbd9692e76c | -6.13027 | -55.64649 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3fe60052-eb7a-3e78-ac3a-5314b78dc4e2 | -3.62429 | -60.55864 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a395fad-4826-3080-9e1b-6fc7abccbeb7 | -5.9443 | -57.69108 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f16c6ef3-f881-36c8-88fa-efbf3a2c7602 | -4.97148 | -55.84956 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56a9fb53-5977-377d-aaf0-e7579356e0a1 | -9.16125 | -59.54074 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c7506d2-58ae-3ad4-bebe-8bef78f692fd | -6.81515 | -59.43996 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8d4c0a8-97a5-362d-8da7-8dfa01e8cc09 | -9.13801 | -61.0966 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15102b93-c9a6-3078-bb1c-a4219b22df54 | -7.62816 | -55.28464 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 296717f2-f0eb-32a4-9959-3e8f8e41fd49 | -11.15275 | -45.04567 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49c4756c-f948-3316-be40-2e1abb0d8b2f | -5.88059 | -57.76591 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a5101fa-d6bd-3b79-a1c3-417c0ae05027 | -7.1875 | -60.68486 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c57872f5-1d73-3b77-a65d-b5929db95230 | -6.16411 | -52.63543 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README58.md)
