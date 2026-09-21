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
| f251c724-b654-3311-a5d4-a5293efab0b5 | -8.754 | -44.2589 | 2026-09-21 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 15026e57-1da8-357a-b195-d96b766875d3 | -10.3914 | -48.9133 | 2026-09-21 13:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| ce91e363-18cf-3f20-bb49-4bcd676bd778 | -6.8263 | -55.5421 | 2026-09-21 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 66c58924-e4cc-343b-87ed-62580313af4c | -8.7267 | -44.8836 | 2026-09-21 13:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 349b4fbf-4d2d-31ca-a634-fc6ef90957d6 | -11.8014 | -49.8129 | 2026-09-21 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 73efdddc-861c-3309-b33d-8bd6e74200e4 | -4.6835 | -46.4074 | 2026-09-21 13:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 6b2d5d53-d49b-34ce-b299-d28429074656 | -10.4675 | -50.2624 | 2026-09-21 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ab941227-7863-3c5e-9daf-388b82efda67 | -7.4092 | -44.7885 | 2026-09-21 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 4ccc155d-a1e4-3fde-9da5-3868b29afba2 | -9.831 | -48.4292 | 2026-09-21 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f469d175-b365-3cba-b45e-5467aa8eff99 | -7.428 | -44.7867 | 2026-09-21 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 78a34f84-ad23-319d-8c0c-0faeab7373b3 | -11.8495 | -46.833 | 2026-09-21 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 10137dd6-22cd-306b-ad9e-96a649356b16 | -12.2914 | -50.1633 | 2026-09-21 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 248.2 |
| 68ce8b76-877a-3516-8c24-b6e5f5c11f81 | -10.744 | -50.7876 | 2026-09-21 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 6c2de766-41e0-3e2b-9564-baf83a07534c | -10.8002 | -50.8243 | 2026-09-21 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| aa3f320f-dd8a-3a44-95be-551c6bc8a2d8 | -8.7729 | -44.2568 | 2026-09-21 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| a7aa23bd-e443-36f8-a6ff-954bccfd2be7 | -12.4204 | -47.0228 | 2026-09-21 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 5fb98b64-5276-34d9-b8ff-0e39e431f534 | -7.4126 | -49.8317 | 2026-09-21 13:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 9f89b5bd-587d-30c5-a95b-401e2963a332 | -11.9967 | -58.0821 | 2026-09-21 13:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 538e1dec-a41a-38b9-ba26-1579a9892e3e | -10.8472 | -50.1581 | 2026-09-21 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 63f858e0-fa4f-3bd7-ae41-61834d03d684 | -6.5761 | -45.5194 | 2026-09-21 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 9a69e606-64b1-39c3-b5cb-f1b952df8efd | -3.753 | -59.419 | 2026-09-21 13:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 3f2bb46b-31a1-3305-b9f1-dfc8e2c0dd15 | -4.9533 | -45.16 | 2026-09-21 13:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| fd105028-6627-31f7-9fdc-40b1c03114a1 | -8.7911 | -48.7502 | 2026-09-21 13:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a67ebb89-2dee-3acd-91bc-8c5fafb5e003 | -13.2794 | -51.7524 | 2026-09-21 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 19c322e2-78ad-342e-8a90-3547f8d95c78 | -10.8662 | -50.156 | 2026-09-21 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 77b5743f-3ddb-3766-a7e1-2d5bc00e6630 | -8.7726 | -44.28 | 2026-09-21 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 56deb840-1747-3fd0-9532-a34b1bf8de4d | -11.0412 | -54.1362 | 2026-09-21 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 25c19717-9d68-359b-aa91-9367e0756638 | -9.8307 | -48.451 | 2026-09-21 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 1b5a3ac2-2135-366a-90ed-8c452f33c78f | -6.1841 | -57.7786 | 2026-09-21 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d716449d-1463-37ff-9b2d-8395c506a80c | -10.8096 | -50.1407 | 2026-09-21 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 1428f5b6-a169-3ca6-9aea-e55a17455b2a | -3.753 | -59.419 | 2026-09-21 13:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 8abfb856-426a-3811-9867-1a594cad2a8e | -10.0898 | -50.2795 | 2026-09-21 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 9dd4a342-f950-3dc3-a01b-f1db04c65459 | -6.4486 | -59.9717 | 2026-09-21 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 45b6cb04-9ef3-35dc-b39c-2352c9a211ae | -5.9151 | -59.9522 | 2026-09-21 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 369df3cd-26bd-320a-9e9a-5590ccc531e0 | -13.2787 | -51.795 | 2026-09-21 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 4e814db4-085c-3b42-a203-7278a27bb3f3 | -10.3917 | -48.8915 | 2026-09-21 13:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 693d6894-285e-3294-879f-7a5216474e04 | -11.9969 | -58.0622 | 2026-09-21 13:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ff43e1ce-f52c-31de-939c-6051d49a383d | -6.0033 | -44.7247 | 2026-09-21 13:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 8b83f98e-ff06-3e59-9796-195c5c8fe656 | -6.7464 | -59.4223 | 2026-09-21 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| bdcd89f4-7ed6-33ce-9f8d-5af959e4a68d | -10.8093 | -50.1621 | 2026-09-21 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 81cf077c-0a6c-33bd-8ab6-0f8b1162a1b5 | -11.8014 | -49.8129 | 2026-09-21 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| ad2363a1-d6f9-38dc-aba7-5244806ce579 | -5.841 | -53.5205 | 2026-09-21 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0c56b7d6-3414-3c93-a0bb-4e219689acdb | -8.7537 | -44.2821 | 2026-09-21 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| a5625b5f-18cc-38c3-b1aa-18ee2d165614 | -11.9507 | -46.5033 | 2026-09-21 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ef857644-deb9-3882-b93b-ca38960d7cac | -6.392 | -45.1948 | 2026-09-21 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 301a8576-144e-3e58-9c19-137a9ffd1adb | -9.8307 | -48.451 | 2026-09-21 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 264.1 |
| fb902798-b7d1-3952-a1e9-c1a85d5f9ce0 | -10.4297 | -50.2663 | 2026-09-21 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 6e2b0586-d34e-3258-9874-e5c9b17aae74 | -6.8264 | -55.5222 | 2026-09-21 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| acbc34a2-2317-3b2a-934d-3bed30b77ea1 | -4.9533 | -45.16 | 2026-09-21 13:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 6d8d5cea-6434-30f9-8736-6cea46ef5b65 | -9.831 | -48.4292 | 2026-09-21 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| b4967800-63c5-36d9-89c8-4d3f3f60e5db | -10.8282 | -50.1601 | 2026-09-21 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| c7e54d1c-732e-3fa2-a397-c424526947f5 | -6.4107 | -45.1934 | 2026-09-21 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 446d5420-b310-3d24-8611-f29b08b25ffb | -7.5059 | -46.2269 | 2026-09-21 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| c3388fd3-834a-3951-864e-5dbb8bb31e3a | -11.8715 | -48.9792 | 2026-09-21 13:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| f3c652de-cc20-33cd-92b2-a02c46e6fab1 | -10.0526 | -50.2406 | 2026-09-21 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 6712c735-80e6-3233-8278-3990bad3c1a5 | -5.9335 | -59.9515 | 2026-09-21 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 8b149aa6-e31b-3537-b76e-bad92e97febf | -9.0227 | -49.8262 | 2026-09-21 13:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| f487380a-e804-3cd2-b7a2-62dbbeeb52fb | -11.041 | -54.1567 | 2026-09-21 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 94b4be43-6a17-31dd-a03d-0ede9cfdcbe7 | -8.7723 | -44.3031 | 2026-09-21 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 8526ee8f-9d1d-3a78-979b-9c2c508a92e3 | -6.8448 | -55.5411 | 2026-09-21 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 178.7 |
| 4d89cef7-5d68-340c-a0ab-6c5bc3a341ca | -12.42 | -47.0453 | 2026-09-21 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 378.0 |
| aa77497d-9b5d-3867-9707-abd63d45134e | -10.3914 | -48.9133 | 2026-09-21 13:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 633df4dd-7135-373d-afa6-c7dfc713d44a | -9.4567 | -45.4178 | 2026-09-21 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 534d3608-71f6-3ae6-b2fb-d0dbce7abaf0 | -10.3728 | -48.8936 | 2026-09-21 13:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4a35d8e9-911f-35b8-879a-2906fa5bcb6a | -12.3102 | -50.1826 | 2026-09-21 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| fc161413-09a7-3459-94a7-715841665bf9 | -10.4486 | -50.2644 | 2026-09-21 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| d4f1e450-4505-3dec-8fbd-0a458ef7400b | -9.257 | -46.1873 | 2026-09-21 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 6c4576c3-83fc-31e1-b5b5-21fcd64707d6 | -7.3289 | -55.2155 | 2026-09-21 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 95b7af37-3209-3287-af8e-d1d6641bd265 | -14.0421 | -52.0812 | 2026-09-21 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 02410a6a-be93-3b3f-bb5d-677b9688853b | -11.1183 | -54.0062 | 2026-09-21 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 971318f5-cdf2-345f-be9f-61afa51a7788 | -8.7726 | -44.28 | 2026-09-21 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 190.9 |
| 2b4bd542-dd43-37fb-8cec-775d53bb9865 | -10.7999 | -50.8455 | 2026-09-21 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| da457895-bf94-398c-9c3c-345d683d3b0b | -8.7911 | -48.7502 | 2026-09-21 13:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 99d9a4c1-3d6e-3fa6-b46c-de56e4514e98 | -12.4204 | -47.0228 | 2026-09-21 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 204.1 |
| d597d87a-39d8-394c-9503-0f805fb826ce | -6.8034 | -59.1307 | 2026-09-21 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6f06629d-919e-38d1-8a76-7e918369d63a | -13.2794 | -51.7524 | 2026-09-21 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 61da2fd4-97ca-3425-ba44-fcae5bf95e93 | -7.4124 | -49.853 | 2026-09-21 13:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 86c5da1d-3660-3603-a980-b2dff0da9246 | -13.3443 | -51.2973 | 2026-09-21 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 131.6 |
| dd0d2fbb-858d-332d-9518-2d754d045be4 | -10.8472 | -50.1581 | 2026-09-21 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 5c26e1d2-8aea-3284-89d6-34ef2e8215db | -12.3105 | -50.161 | 2026-09-21 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| bf7d5fcf-7496-378a-9ac7-b92d28b4cd5f | -7.4092 | -44.7885 | 2026-09-21 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 5370a45e-f48d-3595-a922-788002444d4b | -6.5571 | -45.5434 | 2026-09-21 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 728adde4-931f-36d3-bcf4-daa78c0edf22 | -6.8263 | -55.5421 | 2026-09-21 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 32556d8d-cc34-389c-a814-6247ea0f2eb5 | -12.4012 | -47.0255 | 2026-09-21 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 91fefcee-6e20-3683-903c-870918672aaa | -12.2723 | -50.1657 | 2026-09-21 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| f3185b59-37ee-336f-8eb6-f5b3e346bd03 | -11.3419 | -51.3606 | 2026-09-21 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| dbb9f638-45d0-3dd3-9ff9-2bdc0e9e91e3 | -10.4672 | -50.2838 | 2026-09-21 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9a047cc2-8ff3-34ee-948e-ba3bc2038dec | -13.2596 | -51.7973 | 2026-09-21 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 3ae90d35-e236-3b4b-bfa3-c076d3aca9f0 | -10.279 | -50.2391 | 2026-09-21 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| af5569db-cdd4-3593-8de5-33d95fb479f3 | -10.3549 | -50.2099 | 2026-09-21 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| a190813d-4380-3528-9ac2-60dc04fd233c | -6.4485 | -59.9909 | 2026-09-21 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 35e6bab1-35c5-3630-961b-115fb9d820d9 | -6.9414 | -42.907 | 2026-09-21 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 5fa6bd74-80ad-38e8-ba73-e1b3c3b5b658 | -7.428 | -44.7867 | 2026-09-21 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f06fdcf4-4ecd-3157-893b-be5f876fea3f | -7.3291 | -55.1955 | 2026-09-21 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8e5ee7f0-f0c8-322f-8ff2-ecdb32daefa1 | -6.728 | -59.423 | 2026-09-21 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 4e2f5a7b-553e-3c76-8ed6-a9e5f3e68801 | -6.5569 | -45.566 | 2026-09-21 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 515d886e-0c7e-3b7d-831b-52d68d00f11f | -10.8011 | -50.7604 | 2026-09-21 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| b4332211-78d9-3cb6-a978-503e67a30da7 | -13.2791 | -51.7737 | 2026-09-21 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 9179748a-f03c-3487-873a-abb519f2022d | -10.3924 | -50.2275 | 2026-09-21 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 4cd6118f-fcb5-32a0-ab54-a36dff9009bf | -10.8662 | -50.156 | 2026-09-21 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |


[Clique aqui para ver as próximas entradas](README118.md)
