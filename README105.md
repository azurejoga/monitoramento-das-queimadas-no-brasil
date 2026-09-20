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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa707467-8fd8-3f81-8a34-683da9f4078c | -10.88121 | -54.08502 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0500fa26-f286-31d5-9052-704cb18df6bb | -10.87329 | -54.09103 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dc0f9ec8-5e59-3532-866a-78b8eea413a4 | -11.20991 | -54.07919 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6a4594f9-e2ac-39a4-8574-50ce9d8a9de8 | -10.87505 | -56.22596 | 2026-09-20 06:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0818210e-bd40-3cb2-b47f-2010b5bd5ec3 | -9.66972 | -54.31894 | 2026-09-20 06:01:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc189697-7f43-3d42-b4a8-7e79f793543c | -8.76661 | -61.39033 | 2026-09-20 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc34c3fa-9568-341a-af1a-12af515d8522 | -9.94193 | -60.72845 | 2026-09-20 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4374618-f92b-306c-868f-4c30970cb31f | -10.86791 | -56.17893 | 2026-09-20 06:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7f6a7f2-8371-302c-88d0-8e43937e7a51 | -8.79583 | -60.80067 | 2026-09-20 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| eee324f5-3bbb-3c37-8683-c49d0d14dba3 | -8.22248 | -62.84087 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e77463e2-aa85-36c6-9e7d-6a324decece9 | -11.04334 | -54.17861 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12f3d17d-9824-3531-b014-60a05ad05e9c | -11.1095 | -54.02441 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 584b9e0e-4d53-3c4c-baf7-665f5e6b3960 | -10.87442 | -56.23113 | 2026-09-20 06:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb98e24a-3c60-35d8-819f-00568fbb502f | -8.61274 | -54.60329 | 2026-09-20 06:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bbd120d-0cd5-34b0-84a6-7030b2ed3464 | -11.22506 | -54.07393 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3584547c-d0ce-3dd2-988b-219d07f4a44c | -8.92373 | -68.58046 | 2026-09-20 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8aafdab0-112f-3369-a079-d97901ad81f7 | -11.09432 | -54.0295 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 6007f3e3-66ec-382f-bdd3-ae4b9c227ca7 | -9.18327 | -60.76291 | 2026-09-20 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7c48c24-f903-325a-af4d-70d53e24ef06 | -10.7499 | -56.00077 | 2026-09-20 06:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ebe3e289-84e3-3b60-b28c-b3206f83844f | -11.02381 | -54.13602 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 482431b3-1b6f-3c70-8a1e-ddc0d45ea309 | -8.79711 | -60.79161 | 2026-09-20 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4203577e-0cd8-3e97-9598-76b31ba50258 | -11.7276 | -54.55981 | 2026-09-20 06:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9745b5c4-ffb9-39bb-8798-c5f396e55de0 | -9.93732 | -60.72778 | 2026-09-20 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 243e64ac-3ff8-32b9-960f-ed09e3697475 | -10.86863 | -57.14394 | 2026-09-20 06:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 095d1f12-f34a-3b7b-87b0-3be400549467 | -10.20974 | -68.74923 | 2026-09-20 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 954c06cd-8cd8-3d5d-a4b3-f794fbf3a5c2 | -11.74166 | -54.56145 | 2026-09-20 06:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4d7d3c91-d915-3546-8845-fe43cf978e89 | -11.21345 | -54.08569 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8411e388-8941-3042-8bb9-76f83653054d | -11.10868 | -54.03136 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5fab560f-85a2-3cd0-ace4-162dc7be9f26 | -11.08908 | -54.02715 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| fd834c3a-a033-3de2-be4f-e7e4c46ca8cf | -9.93371 | -60.72548 | 2026-09-20 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e49d2046-bef7-35c8-9d98-9aff06c7e9b0 | -8.61446 | -54.60946 | 2026-09-20 06:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cea3bf3-05c2-366b-853e-7ae8d78aeee7 | -10.88573 | -54.08757 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2eadf3a2-6355-3cde-a0d9-b1e2c285a874 | -8.79197 | -60.79541 | 2026-09-20 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bdfe0ac6-924f-3a7f-96db-efbdbef860d9 | -8.61599 | -54.59706 | 2026-09-20 06:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d72fffc9-97f2-3dbc-abb9-8d02fe5f2539 | -9.19237 | -60.76425 | 2026-09-20 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65992606-d557-378b-a568-caf016d208b1 | -10.56834 | -68.66842 | 2026-09-20 06:01:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32586a8c-1afb-31af-811d-c4c33f849595 | -9.19301 | -60.75959 | 2026-09-20 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7f8effc-0076-3f2a-baa4-1b3879874957 | -8.86563 | -68.50526 | 2026-09-20 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b00fe638-d6dc-3e72-9ba2-c2c5fe958095 | -8.61434 | -54.59104 | 2026-09-20 06:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6b1b0a2-add1-3ecd-9ea1-451ebe9c1989 | 0.01411 | -60.60552 | 2026-09-20 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d70e488-7f65-38a8-8fda-49f66818adda | 0.00794 | -60.60655 | 2026-09-20 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84e29278-ecf2-3df9-b20f-cf2bd0860db8 | 0.69393 | -59.5507 | 2026-09-20 06:18:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4a4ef94-d0c1-30e5-9f66-0caa1137af01 | 2.31993 | -60.92241 | 2026-09-20 06:18:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2687b6f-506f-3007-94ae-f65040cbf60d | 0.69333 | -59.55239 | 2026-09-20 06:18:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c242c35-c4ae-3e04-8b84-40aa58fbcf51 | -14.0614 | -52.0788 | 2026-09-20 06:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 3728e439-6908-3fac-b490-64cd0b5b8891 | -8.7928 | -60.79642 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 565796e7-d793-31a3-9b0c-093edf1e2132 | -6.44652 | -59.98185 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 713ebd61-718f-3757-a35f-eda3812be171 | -8.19464 | -62.8566 | 2026-09-20 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae743d6a-89aa-3cb4-8454-30ddc4e684f5 | -8.79156 | -60.80083 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 566ef717-e04b-351c-b9c1-3b8d89c4e5c4 | -8.79965 | -60.79752 | 2026-09-20 06:20:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20689803-769f-3c2a-b139-7c7f567d1b01 | -6.64687 | -62.88145 | 2026-09-20 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b63507b6-dd2a-3ce7-9caa-008057da0428 | -6.43954 | -59.9806 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49c2855d-aa52-34b6-99f6-1a1b9bcced97 | -6.44925 | -59.97569 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c7fceb97-e850-3443-9838-fe451c79b69f | -8.20127 | -62.85294 | 2026-09-20 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af785d3d-bcc2-3b8d-b7d1-2b4a7d4c77d1 | -6.45348 | -59.98315 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c31bbc92-87f1-3c49-9e4d-b4a8da2808c0 | -8.79886 | -60.80394 | 2026-09-20 06:20:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7354e9d3-9169-3f50-9245-d473b85d7495 | -8.79841 | -60.80189 | 2026-09-20 06:20:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4fa1e9c3-c0e4-3839-828a-3febb848896d | -3.68595 | -60.61632 | 2026-09-20 06:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03289065-5686-313f-bad0-a22198ce2379 | -3.68676 | -60.61087 | 2026-09-20 06:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7076365c-12c4-3cad-af1d-87461ac7b652 | -6.13575 | -59.94465 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e79af10-78aa-3867-9537-824373ba2c3b | -9.94263 | -60.73138 | 2026-09-20 06:20:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b0ac397-69f8-332a-8d33-399f7818f583 | -3.69813 | -60.57892 | 2026-09-20 06:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7247130d-4d65-3439-b77b-72719bb59894 | -7.0441 | -62.95946 | 2026-09-20 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 449c4e85-1794-36da-ae70-13bb0dbc2d10 | -3.68515 | -60.62177 | 2026-09-20 06:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c11669e-7eed-303f-8336-3b1afeb2c723 | -3.69241 | -60.57248 | 2026-09-20 06:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 358c8048-b45c-327a-a67f-9564b03ad405 | -3.69569 | -60.5954 | 2026-09-20 06:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a853ae64-8fe5-3a89-a018-755b418c9e47 | -8.79239 | -60.79444 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f28df656-d662-3a09-8296-6acd3bcc31c5 | -8.01942 | -70.92439 | 2026-09-20 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ac11505-1bb0-32ed-a505-84f63abeded8 | -6.4553 | -59.98357 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22d35d2f-cfd9-31ce-85ba-41d6f09b4037 | -8.03236 | -71.14707 | 2026-09-20 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a490707a-7c78-3bbc-956b-8accd0fc014b | -6.44834 | -59.98236 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d0ad48b2-9ca3-33d7-8462-01e53bf8f48f | -8.1971 | -62.85241 | 2026-09-20 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 160b24a3-ac2f-3340-bc0b-8bd45f140267 | -6.94278 | -62.92039 | 2026-09-20 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d828721d-1da3-3093-8e81-e68e1bf4b667 | -6.13488 | -59.95121 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c394df37-de22-3708-807d-6e4e3e8d092f | -6.44039 | -59.9741 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d410b0b1-098d-3956-a7c5-c9fabc2eddb7 | -6.44226 | -59.97462 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 151dcebc-ee01-3a8b-a81a-1b9e27baf272 | -8.79925 | -60.79548 | 2026-09-20 06:20:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1d6b980-0c11-3921-9e9e-6e8822b7753d | -3.37809 | -61.30206 | 2026-09-20 06:20:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63e0e907-3f4d-3ce8-91e5-5bf33bf64c21 | -3.69322 | -60.56696 | 2026-09-20 06:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 676f473f-2df3-3986-b53a-e3af0dda9b23 | -3.68837 | -60.59994 | 2026-09-20 06:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ce919fd-4505-3e44-bb04-7df63965a568 | -8.20066 | -62.8574 | 2026-09-20 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 143404cf-6679-3592-a569-644a755bc4ae | -3.69085 | -60.62817 | 2026-09-20 06:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73b4965f-e3e7-3317-b762-b5daafada9ed | -6.44738 | -59.97524 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 650841d7-e723-3078-b1f2-72742514cc87 | -3.68756 | -60.60541 | 2026-09-20 06:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a45b99b-d3f6-3d6b-8905-bcba705ebbc3 | -8.00886 | -71.13547 | 2026-09-20 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1cb8af3-72cd-3afe-a922-19aa95b7d48a | -8.19652 | -62.85688 | 2026-09-20 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4444eb91-cf70-3eb3-a9df-fd7369fee7e4 | -8.0188 | -70.92345 | 2026-09-20 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b610844-8380-3f3b-88dc-7c63707a8c58 | -7.04467 | -62.95522 | 2026-09-20 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ad13618-20bf-366e-a476-77e757dc0902 | -8.03561 | -71.05376 | 2026-09-20 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a56cc2cb-c3da-3957-8575-5da2e804e999 | -9.93563 | -60.7305 | 2026-09-20 06:20:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c0e19d1-f155-3a55-bc70-620c2e77482a | -8.20312 | -62.85323 | 2026-09-20 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5669593f-b4b6-3bf5-8c17-899f8dab1498 | -6.44137 | -59.9811 | 2026-09-20 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 61d9901b-7088-3737-b980-819551eeca47 | -3.69404 | -60.56142 | 2026-09-20 06:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6831e910-7d98-3a1d-a25d-12d5ebe761e7 | -3.68917 | -60.59446 | 2026-09-20 06:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef57cb52-6f52-384c-9c85-788b295048a6 | -10.98534 | -68.45802 | 2026-09-20 06:22:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b93f6a6c-195c-381e-a152-f2b7a2a76202 | -10.56893 | -68.66853 | 2026-09-20 06:22:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 87de9d17-ac0d-32db-ac51-6cc43c38057d | -10.0568 | -68.44699 | 2026-09-20 06:22:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83da2e6f-dfde-36f9-8a98-4db69f42c432 | -10.20857 | -68.74916 | 2026-09-20 06:22:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7918126-9935-3cc7-bfa1-0c9b2ccd5f9b | -10.27901 | -50.23847 | 2026-09-20 06:25:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 2ab85a91-71f3-3dd4-bf01-1e5729b9ea40 | -6.39811 | -43.19372 | 2026-09-20 06:25:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README106.md)
