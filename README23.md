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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 487ee4f0-d6bd-3587-af5f-44f51e353d41 | -5.71816 | -44.2436 | 2025-10-04 03:51:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c36421b6-20ea-31ab-8280-0df09f317d81 | -5.23835 | -45.55106 | 2025-10-04 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5869fbf0-8b27-37e9-b13d-2e9a9d3ad8fa | -10.84324 | -47.20547 | 2025-10-04 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2807d3cd-83e5-30a8-a0e0-259fb04f0d73 | -9.34217 | -45.79343 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 55dd6ad5-e244-3bff-8952-e8d8d4891751 | -6.64846 | -41.9558 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e1459c86-d917-39e8-8fae-bbd7827f55bb | -8.91759 | -46.60912 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3f2802e-b782-347f-9b32-6175a99e41a6 | -5.83859 | -42.88404 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b210be73-cb8b-36c3-857d-4214eac506fb | -7.7232 | -42.57589 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 99324bcd-1867-355f-8d23-2d8947d74780 | -8.13678 | -44.08395 | 2025-10-04 03:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37caac0e-61c3-3512-866b-49dd3008b832 | -7.69694 | -42.57918 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f9043f9c-2606-3690-8bee-79183fcc0c79 | -7.56357 | -42.39499 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 67105d50-2be4-3bff-ba66-e76417e47c62 | -6.23646 | -45.351 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43de11b3-f921-32f8-aafc-b2429833c06c | -6.35115 | -43.44792 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e39fde57-55ed-36ce-aaf2-05396cd32246 | -6.34212 | -43.44642 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7f08278-9bfa-336c-9718-ec51925e621b | -7.89657 | -42.60058 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 85b29e09-7eea-38b0-9a22-9dfba602088a | -7.80206 | -42.5391 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 001cbba6-df56-34a4-bb73-73302747238a | -6.28138 | -45.07837 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8ff552b-6555-33ca-ae9b-c5e6c01aceb3 | -7.7943 | -42.5681 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 87beefcb-7912-3254-b50e-bfe475b9e943 | -4.66827 | -45.80353 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10cbc039-511e-34e2-9247-7d09ffe03e1d | -5.61042 | -43.22866 | 2025-10-04 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abca2707-8a75-31d7-8925-009fc04d0f8c | -7.57178 | -42.39656 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c7bb22c0-5e19-34d3-9ec6-e76849b9b8dc | -7.76789 | -42.51428 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5bba9f4c-3747-390b-83d2-f66bb2883ba8 | -5.43292 | -47.10067 | 2025-10-04 03:51:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01adc295-44bd-3cc7-b404-fdcef6830d0d | -6.28144 | -44.04625 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eca6ccf1-e245-318b-93ed-ebac9cfb7a12 | -5.63603 | -43.22149 | 2025-10-04 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 604bc75b-9e48-38fe-8f82-78571803c5bf | -6.34136 | -43.45093 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8cbcb56-3d1f-3e0a-83f7-135adef583b0 | -6.28526 | -44.05214 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96041c01-aea7-36ea-a5f2-d59ee2935cec | -11.11438 | -47.8985 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3c545f7-1df3-3a4a-bb68-ef8b3cbf0130 | -5.65684 | -42.73594 | 2025-10-04 03:51:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b5bce71f-f76d-367c-bb5c-a2dae3f71423 | -5.19379 | -45.0635 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f5631128-7b95-3442-a6e4-4d88473daf45 | -5.92819 | -44.18956 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 404c0224-0f56-3795-9c32-b1cdeeb5c09a | -4.67629 | -45.68327 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e19ec54-75d6-3f1e-b318-0df838b0c8e6 | -6.27874 | -43.62798 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b97888e9-b20e-3d69-b815-12501b625be4 | -5.96028 | -43.49048 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ed61b1e-4f16-3fc6-8e7c-0586c365b707 | -6.24631 | -45.34549 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ce3fa5c-549e-3ea1-8c96-28979c28b495 | -7.06562 | -43.23023 | 2025-10-04 03:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 62ca9da1-16a1-3acd-bca1-7b53b43ce046 | -6.07381 | -42.51398 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| c7830afc-fddf-31cd-805f-3de6d3eef5aa | -6.3681 | -42.89073 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9c506d3d-3943-319b-bb59-ac570f1483e3 | -11.44993 | -45.13883 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12590274-e3a7-3181-8886-51d24f1cea8a | -6.71467 | -42.81194 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f0291e9d-e21f-316f-a29a-0226c5db566a | -7.8033 | -42.53167 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7cbecab1-ae34-3be6-aac5-3be79fac4e8e | -8.97896 | -46.72686 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44676760-2989-3455-b53e-08a6f8dff10b | -7.71138 | -42.57 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0388ad84-adb4-3a65-8e9c-ea855af34e5e | -5.66117 | -42.73673 | 2025-10-04 03:51:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 67a4778b-3c2b-370e-9799-2c5ce7905a40 | -10.33598 | -50.33245 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ee52e2a4-42ae-34d0-ab53-d593e42b1e74 | -11.49873 | -45.00448 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b8443e4-faea-331c-8046-bd316fd9e63a | -4.31498 | -48.09779 | 2025-10-04 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d0c8ed54-7388-35a3-b64b-b0e963a6f1ea | -5.19222 | -45.07275 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 35ba834f-fe2d-39f6-8c36-4b7be2b96294 | -4.66198 | -45.80164 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df50eca3-4097-335f-9513-81656be1232f | -6.65524 | -42.81148 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a327ee83-9505-3eae-9ecc-58f60e9e7c1d | -11.488 | -44.98901 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 944263c7-cbca-3fea-9553-5a7e0c79f445 | -10.34004 | -48.16869 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd7ed9be-2cf0-3ed8-98d9-a4c797430ce1 | -7.70959 | -42.60513 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 250782f8-4270-328c-9d89-0a62d88a608a | -9.93891 | -50.24729 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ac3255f5-c462-31c5-9c16-7a74a214c1e2 | -6.99303 | -44.20815 | 2025-10-04 03:51:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88d96b84-11a3-374a-b3c5-4b9f3bc5ddd9 | -10.84386 | -47.20213 | 2025-10-04 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68e78ed8-32bd-3c66-80b8-ca1151338a5a | -11.62778 | -45.07027 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c0975f2-8d7c-37e0-8499-e6f2bb0f9dbc | -10.59974 | -48.70692 | 2025-10-04 03:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e59bb71-c060-3f64-a641-e69c790e1eb3 | -5.84858 | -42.79898 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6825018a-edfc-3bf7-9972-b07fe75fd086 | -6.66618 | -42.82541 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 83cfb8ab-0817-32d3-b801-3f913102675e | -4.70347 | -45.60227 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3d7187d-75a3-325c-ab2a-62a498662de8 | -7.78819 | -42.49487 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 54ec5184-bfb5-3a0e-ba74-27afc4409391 | -6.70965 | -42.15693 | 2025-10-04 03:51:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 631a8355-4b2e-3e3f-bc6a-1726b11b0eb6 | -5.26073 | -37.93147 | 2025-10-04 03:51:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e16ab56c-14b6-332b-91f6-582917f0e90b | -9.35118 | -45.80096 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 43995f52-836a-342e-83f0-367161435800 | -7.5547 | -42.39726 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6085127a-e4c0-3d3c-8688-d68d0924f86c | -6.09725 | -43.4826 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 54def8d5-565f-344e-946b-f312411d1f29 | -11.15409 | -43.39652 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c922a9d2-f621-3e28-96ed-2dcba414d07c | -5.90205 | -42.53621 | 2025-10-04 03:51:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 18963122-9a0c-309e-afd9-de8fec9a6f4e | -8.53953 | -47.21183 | 2025-10-04 03:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56b10c29-52ee-3347-8f28-8ef07f6722dc | -4.65711 | -45.79734 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c46f7d79-8b1b-3470-a5da-c92519d10ea2 | -7.1626 | -44.99164 | 2025-10-04 03:51:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b952b50-d1ce-3f35-8082-d8b36b06b8a5 | -7.74466 | -42.52558 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| d6ea2771-e42b-3eaa-9546-e4c3866bca88 | -8.17144 | -44.12884 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 556d6015-b75f-3278-819e-bad86f184758 | -4.67249 | -45.68412 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbe6b4f1-dae4-38f1-931d-2c218f01878d | -6.46369 | -44.58164 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 07c0bc1e-9822-321f-aa3b-659188b538f8 | -7.79759 | -42.54927 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5c98504e-9092-3737-bc01-f9f907579313 | -4.66276 | -45.80299 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 489194d6-5248-375e-b02b-730a7344f95a | -9.99642 | -48.27791 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b403622-e578-386a-bcdb-e227d9ade37d | -5.88137 | -42.5287 | 2025-10-04 03:51:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d7f55c3d-eab5-3e1d-bc34-5c3a46304f1c | -11.6784 | -44.27024 | 2025-10-04 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3919cfef-7ef2-31bd-afcd-dbe18ff4bba5 | -8.2279 | -46.81316 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c716992-73fb-3d1a-ab29-39200fded523 | -6.69207 | -42.84053 | 2025-10-04 03:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e532affe-2c39-367f-8ae7-224cbe460d58 | -6.34514 | -43.4561 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9bd4432-33cf-3d68-bb81-c5712bc8c9d8 | -6.88416 | -47.23706 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 125946ed-c0ac-3f27-861c-b74d71d66a64 | -8.87359 | -47.82084 | 2025-10-04 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1338a3ae-b454-3b10-ad07-768ce28d768a | -5.80123 | -42.89209 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f13d01a8-e60e-3b39-a29d-6190ec019406 | -9.91973 | -43.76969 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f2947e8e-ddec-3748-a1ec-1d3f05cf685b | -7.79561 | -42.56058 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c9bc5450-1bb9-3906-83ff-67fa29ea78f7 | -7.3458 | -44.34833 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27d6526d-784d-336f-b935-25a05e191225 | -10.3383 | -50.32114 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f3d3e6d9-3ef8-3751-9752-e2d0e080c936 | -5.24361 | -45.55216 | 2025-10-04 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c2b1b96-4be2-3499-8e8b-cf498fb2cf51 | -6.52788 | -43.37749 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| de9d892d-e621-367b-ae35-5f218579e78a | -6.34811 | -43.43837 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0deb664-15fa-33ca-bfa4-b7892ea5c6c0 | -7.32705 | -41.44532 | 2025-10-04 03:51:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b43533af-b884-39c5-879d-b4daf6dd9f42 | -10.59471 | -48.70115 | 2025-10-04 03:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7a7d2c6-a566-314a-90cb-74c145be1ab4 | -8.53324 | -47.21453 | 2025-10-04 03:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03874b16-e567-3ecc-bb48-c1762353880b | -6.38356 | -46.51171 | 2025-10-04 03:51:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d1bea77-dca5-3403-ae18-340a9c7be34b | -9.90637 | -45.96119 | 2025-10-04 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4bdb4ad-008f-344e-9e21-a995884230e8 | -6.59161 | -44.62354 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README24.md)
