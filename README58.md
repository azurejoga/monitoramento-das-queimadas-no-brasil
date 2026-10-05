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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f7b3853-a6dd-3ccd-89fa-fb28b284f7c8 | -9.16582 | -68.26199 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f73b5784-4fc4-3ebd-a40f-00539256a01a | -10.01732 | -64.97372 | 2026-10-05 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0eb88d36-39df-3d00-9373-50370369f728 | -9.22914 | -67.87408 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d07d0e8-6aa8-3533-937c-d0bdf6334a5e | -11.04779 | -62.57447 | 2026-10-05 05:44:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0afd00c7-9a53-3f4c-aff6-85e050e93345 | -9.03269 | -67.47279 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69e9a79d-e29a-30de-8769-7f2de5b68be4 | -8.62806 | -64.11563 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed0b7984-0356-34b0-a6ea-617b01b41d6d | -10.95865 | -60.90812 | 2026-10-05 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b4cb3dd-9623-3333-bf30-53ad43b51cbb | -9.16239 | -68.26143 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acb17218-a479-321d-b0dc-b6fe18440935 | -9.19724 | -63.15209 | 2026-10-05 05:44:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba8117fc-fb89-3c97-89fc-a254bb29cbc9 | -9.11743 | -64.35949 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82d96e51-d97b-38c1-bc13-e5b010fd5679 | -8.34552 | -62.82481 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c146455-eecc-3cf1-8c06-7a0d27e4ccf2 | -8.56928 | -67.13396 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd9059b6-7771-30b2-b4fb-1c42bb90a752 | -10.6193 | -67.91942 | 2026-10-05 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd30e919-baea-34ff-a315-c0491d63f15c | -9.1083 | -65.36387 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 871e3849-5cc8-354a-aded-ab910c34e73c | -10.89586 | -57.08532 | 2026-10-05 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c340110-5f9e-3bcf-91db-1ba9fd92f05c | -9.21572 | -65.59266 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab85c75b-3022-3bbb-bacd-b07503b222df | -10.86109 | -68.68723 | 2026-10-05 05:44:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b495c32c-e256-3113-9d72-78a098206d34 | -8.77392 | -69.5346 | 2026-10-05 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f395d4ab-69ae-3d42-8f0b-029c832d96ff | -9.47553 | -67.10587 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8528965-6a76-3c59-a076-431b9d930200 | -9.54532 | -68.52641 | 2026-10-05 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4023b294-6e3c-34b4-aae4-9eddfe0eb005 | -9.10884 | -65.36036 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c51d2a8a-85fa-3300-ad87-59edd29eb78e | -9.50472 | -68.49216 | 2026-10-05 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9fbdacd-fd63-3760-90bd-3dc3f8751b5a | -10.87768 | -61.40886 | 2026-10-05 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7010230e-e8c5-3f6e-8758-a9cb0327af55 | -8.66706 | -63.41042 | 2026-10-05 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c232ecf-4d6e-3eec-9da7-267f36be50ab | -9.26216 | -65.44587 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89079607-9441-34f7-8326-63738be61a68 | -9.09555 | -64.38303 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4eaa2a94-191b-3358-bff6-997a8cb006ea | -9.11006 | -68.30411 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7800817-9eec-3cc2-9b32-e7dbd2d4bc25 | -10.64365 | -68.59792 | 2026-10-05 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8361d90b-98bb-388a-886f-9f916d92653a | -10.90085 | -57.0895 | 2026-10-05 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f291f6c0-b543-327a-a18c-50aa6b13cdfc | -9.15241 | -68.26028 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86e0d057-afcf-3b55-aa03-9e0f73980775 | -9.71691 | -65.09664 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57436225-4dd6-348c-aa48-b4110d970811 | -7.66565 | -72.43217 | 2026-10-05 05:44:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 632cc4d2-1d70-3cb2-a080-ad93356bd0c8 | -9.0054 | -65.7197 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b0417e7-76fe-355a-b36e-ef01da1fce0c | -8.96313 | -62.34558 | 2026-10-05 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9d622d9-88cb-355a-99aa-44df74fd32d1 | -9.23313 | -67.87096 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a830a17e-d907-3c4a-9386-2d727c4f651a | -9.16171 | -68.24622 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 367bd155-9998-3621-9ed4-c1ff17c0fcb3 | -7.45623 | -63.56248 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3951b73d-efcf-32c6-b303-5fcd6f1ece3a | -9.16645 | -68.25819 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0017cd33-afdb-3074-a23f-e5e11915d531 | -9.22014 | -68.16631 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89799781-87eb-3dd8-ae31-cabf4661262c | -7.66182 | -69.93083 | 2026-10-05 05:44:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60c7cf01-fab6-39b3-bd69-3f515b5b697b | -6.89577 | -43.67107 | 2026-10-05 06:03:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| f1db1105-6672-3bbf-b2af-cfd82621faab | -6.90646 | -43.65381 | 2026-10-05 06:03:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6f60ce32-080d-36ad-b4f2-2ebb53326e22 | -6.90961 | -43.67353 | 2026-10-05 06:03:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 31d74443-14a0-3d10-9421-fac3896cf8bd | -6.9024 | -43.67744 | 2026-10-05 06:03:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 7d3e5ade-3788-3803-96a1-4c5e126286e0 | -16.67669 | -41.84715 | 2026-10-05 06:08:00 | AQUA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 58fe348f-20b9-3d66-8500-f06c755aecca | 1.72956 | -55.65673 | 2026-10-05 06:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 68c89663-d884-3bf4-a2c4-5e60e49d4dec | 1.72834 | -55.64951 | 2026-10-05 06:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 751139b4-231f-3584-969b-16ec1c7ac6e0 | 1.87504 | -55.76525 | 2026-10-05 06:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 891d590c-e9ac-3fc1-8cac-ac0466d4133a | 1.87761 | -55.76659 | 2026-10-05 06:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb227558-27af-3612-b9ad-15e51b13b56a | 3.08789 | -60.59213 | 2026-10-05 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a9703ae-cdbc-332d-87c2-fda05600b7a9 | 1.72227 | -55.65785 | 2026-10-05 06:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 396d19e0-02c4-3aee-844f-c19e0c45e38c | 3.10051 | -60.60312 | 2026-10-05 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ce39649-563f-3d14-85b2-d5213cebd67d | 3.09313 | -60.59126 | 2026-10-05 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 271b401e-b9f8-3370-b506-e28f6653c415 | 3.09153 | -60.5817 | 2026-10-05 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 712851de-577d-3432-b43b-0e389472f144 | 1.60919 | -55.79725 | 2026-10-05 06:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6427b986-43eb-313e-a27b-4066b0ea6634 | 3.0926 | -60.58807 | 2026-10-05 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67aa30c3-7261-3bb4-b60f-39e736d4ac6c | 1.86904 | -55.77363 | 2026-10-05 06:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4103fea7-e32c-305b-9f6f-47be1ef696b8 | 1.87164 | -55.77491 | 2026-10-05 06:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0872bffa-a5ca-31d2-8846-4a63b5a66f32 | 3.08736 | -60.58896 | 2026-10-05 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb63ce3d-c7f3-34e2-a7e0-acec593c6f18 | 1.87626 | -55.7725 | 2026-10-05 06:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d38d92c-8add-3f2e-9fe8-dd2415d79e19 | 3.09838 | -60.59038 | 2026-10-05 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 902effb1-8532-39c2-aafd-335c8b2ac49e | 3.09207 | -60.58488 | 2026-10-05 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9653d800-1d0c-397c-bd1b-552de6f20bc1 | 3.091 | -60.57852 | 2026-10-05 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4351acf-812a-3e31-b7ee-1387c5021bcd | 1.87887 | -55.77381 | 2026-10-05 06:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e181c56-50ca-32bd-8f67-08ab20fd6e68 | 3.09997 | -60.59993 | 2026-10-05 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49f52b89-a2f4-3684-8d4e-28bf86d14d10 | 3.09891 | -60.59355 | 2026-10-05 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4809c65a-2b02-3be3-afcd-c035cb6436c4 | 0.44084 | -60.53746 | 2026-10-05 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 81475cb9-fe8d-3ef0-844f-21d81067325b | -2.95296 | -59.15771 | 2026-10-05 06:18:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d6efc09-34dd-3327-8a0a-5d3c757145f6 | 0.44521 | -60.52946 | 2026-10-05 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d76a9197-95cb-3e54-83a3-1f17c8fa447e | 0.44577 | -60.533 | 2026-10-05 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 29ff9ea5-6f15-33e9-979f-9d81020bd31a | 0.44534 | -60.53403 | 2026-10-05 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fb14947-0467-3a69-9262-1ffe364a0bca | 0.44476 | -60.5305 | 2026-10-05 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08f39ed2-7f43-3079-b48b-d2cf16ca4f24 | 0.44592 | -60.53756 | 2026-10-05 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55ee567f-2dce-39dc-a9fd-bd4510eca169 | -2.95412 | -59.16422 | 2026-10-05 06:18:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a198f17d-c287-34f4-90c1-3ac9645c44b7 | 0.43972 | -60.53041 | 2026-10-05 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cea99c97-25d9-351e-bf5c-76ee35a60437 | -2.95218 | -59.16283 | 2026-10-05 06:18:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cc5f097-dee3-37fe-95f3-90fcf180d19c | 0.44744 | -60.54362 | 2026-10-05 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a7ca8293-4237-3fd9-9ca3-5a706e1f3bd0 | 0.44028 | -60.53394 | 2026-10-05 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e0b50c0-a290-322f-ad97-f389ffc903e2 | -2.95488 | -59.15901 | 2026-10-05 06:18:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0d1ae7e-4466-36f6-b1d1-983a1e88c880 | -8.3578 | -62.83801 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c43ebf02-e1b8-37b5-954e-ca061fa4617e | -9.16506 | -68.25946 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c6140a1-e32a-330e-af99-fd7dad85c4b3 | -8.67053 | -70.04212 | 2026-10-05 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2acd1bcf-196e-3806-a327-5506ab5734e3 | -8.5207 | -67.00671 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf1eb3a7-2af9-38af-9fc0-2fd44ca545bb | -10.4039 | -69.15677 | 2026-10-05 06:20:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84050afe-6028-3576-89b4-a5427beb9e7f | -9.12499 | -68.21555 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff0df279-a689-3317-847e-d743f4aba974 | -9.50413 | -68.49284 | 2026-10-05 06:20:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91d5dcd3-29a5-381b-8d25-a24a805d61c1 | -9.23443 | -67.86842 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af3534a0-9e08-3cea-8606-61168b63e199 | -9.15682 | -68.2629 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e2cdde3-047d-3dfe-b53c-c82dc536ac62 | -10.08458 | -68.46996 | 2026-10-05 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7067888e-2e74-3b78-87d4-b4f67866ec68 | -8.43798 | -70.10416 | 2026-10-05 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbe74c75-f095-3198-8019-65f337d91a41 | -8.36107 | -62.81435 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aca3eb7-fa48-3678-a489-59cbd57793fa | -7.44096 | -63.57043 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94781784-e415-372e-b0fe-3c07d4b25b41 | -8.34752 | -62.83315 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee214e4e-eb1c-30cb-9e25-98034aa516a7 | -9.16195 | -68.25429 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f7757cf-8970-3535-b554-b5311b015c1d | -8.45134 | -62.72873 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80e717d7-a928-34bb-aad9-eee0763a5eb0 | -9.66983 | -66.8306 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e399ff1c-baca-3f2b-b6aa-9f3b4728b20f | -8.44189 | -62.71686 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 872ff545-80d2-3741-9327-2a838992e96c | -8.87525 | -66.64705 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7acc132-5cc4-3743-b2e9-bb87b11c3378 | -9.40793 | -65.89198 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edd33f44-bbb1-3adc-bf0a-29fe7d62ef5b | -9.10536 | -65.36241 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README59.md)
