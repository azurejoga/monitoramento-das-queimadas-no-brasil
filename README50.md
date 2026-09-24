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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f6683dd-a705-3189-b0c2-445721085434 | -11.79553 | -50.98603 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35ff28f9-a073-3a52-92f1-d429817084e7 | -10.62034 | -53.99962 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fb951ee-8977-3fd8-89b9-6d244ffb596d | -10.10304 | -46.06783 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9229c85a-9eb9-30ad-ad82-43e3d7530a62 | -8.30641 | -46.88025 | 2026-09-24 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49b5fc2b-9dc8-3975-9ac3-9b7c8652d0f3 | -8.14216 | -46.81826 | 2026-09-24 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b49c3f0d-38e8-33fd-98e2-06aa08ae93cd | -9.54547 | -45.3653 | 2026-09-24 04:46:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ccf1da2c-c39e-3972-944e-8591db240cf3 | -8.45659 | -48.69509 | 2026-09-24 04:46:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8581a5e8-1d5d-36f7-a4d0-c3790a4e356e | -13.99285 | -44.0713 | 2026-09-24 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52d47914-f22c-31e7-bb1c-2167bb7ba132 | -6.10158 | -57.67097 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd127e8e-c627-3b86-b54e-ffd86711d36b | -11.23139 | -51.37616 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 473aad1e-4ea7-372c-aad4-d5932a113212 | -5.91565 | -59.92706 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8ca6675-451c-38d6-802a-969cab66a3e3 | -12.14497 | -50.75609 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a92de99-cb9a-3d43-8ce5-2dfe6e51bac6 | -11.91527 | -50.72913 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d06df91c-92d6-3977-8ee3-c0413601f0f3 | -11.48624 | -47.33618 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ada94fc9-9b07-30a0-bd3b-a08a563bfa12 | -11.9317 | -50.73574 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68d3ffb9-71cd-359d-ab79-0400b1ad5306 | -6.63322 | -59.94067 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6105bce1-7d3b-3a22-b8e9-5f386be3b43b | -11.11299 | -48.3012 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c86e05a4-6269-331c-9e43-1bfc74cca3fe | -11.48336 | -47.35484 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eb4bf192-a75d-3c46-b512-3119a82f4510 | -6.88319 | -59.21652 | 2026-09-24 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c587760e-f0c7-3cca-a3ce-a6d2d129e8e0 | -8.09057 | -44.34382 | 2026-09-24 04:46:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 423de4e6-268f-3657-9f97-2096c0b41451 | -10.65205 | -51.32141 | 2026-09-24 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 770a4aa3-fc04-33e4-bd0d-de785b679fad | -12.16688 | -47.37464 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85c64ddf-0b0a-3944-8e8a-da572d0c002e | -9.84726 | -48.49924 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df465a6f-5030-3083-8ad8-ec291816e8b6 | -11.43377 | -47.40493 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7390077c-3336-3bd8-99e1-3237b2df76c2 | -11.22636 | -51.36317 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52398de8-64d6-3c67-8e87-0905095fde87 | -8.09505 | -54.98896 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 204ff1dd-67ff-3d72-a85e-d97a525dd9a3 | -11.39402 | -47.36825 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7536129-5e78-3f5f-bd44-5aead824d72e | -11.22723 | -51.37949 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a51f4c18-0a36-36d3-abae-44b2d0b6a884 | -10.43909 | -46.27517 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 565966a1-8728-39ac-8539-0543562f744b | -10.82577 | -48.46858 | 2026-09-24 04:46:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9761a201-f41e-31de-9b69-7f4f74e10dae | -11.23116 | -51.35592 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b8f54bb-7aa5-39ca-9933-4eafe11c4a0b | -11.2844 | -51.31669 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a4ddf61-d89b-3f0c-83d8-4aa29cc9672c | -10.90541 | -53.94293 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6798afa-801d-3e94-ad6f-ed9b2514a1f0 | -8.27629 | -54.75526 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 712363bc-c588-38e6-8ee3-72607ae1af55 | -11.12577 | -48.32876 | 2026-09-24 04:46:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bddddaa-9a65-3fcc-b1c6-9177fb231699 | -10.08243 | -46.01174 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 304626a2-7e45-31e5-a93e-60ad9580ab16 | -10.09361 | -46.05838 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 829bc480-da44-3258-853f-a086e0c4a2ca | -8.14627 | -49.54684 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 039c219f-1e49-33fa-a780-2c45187cd600 | -8.26436 | -54.77105 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d656273b-ccc1-3aa4-9bef-bd897890858b | -10.10954 | -50.18941 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4d289386-7ad7-35a0-a293-291a23f1dfc8 | -10.84955 | -43.24758 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0a3050b8-34b6-3a24-982b-34550445d622 | -11.12968 | -48.3039 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ceac933-5019-3929-b44b-5440cd0d1f46 | -10.61627 | -53.9989 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3342d575-698b-3e00-92ee-2340bd9f6096 | -7.5844 | -57.66063 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a975664-5f60-30f3-94fd-091e1d9934be | -12.1376 | -45.63527 | 2026-09-24 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3822aac3-ba21-35c9-8839-c5a4a9bf2d30 | -8.72631 | -47.61128 | 2026-09-24 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f653fb3c-8d33-3910-8d92-3fa6f6b1e1bb | -8.09125 | -54.763 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a7a4439-6701-39f5-9001-7f36b4c1508a | -12.41956 | -46.95498 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9a80af6-2e19-3a93-9847-f95e1dd834f8 | -11.20596 | -54.12704 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02c6f304-35b1-3776-bd4f-4bc26813d77c | -6.12605 | -57.76102 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 598419d7-4f96-3434-8b57-ec83794ab785 | -6.64074 | -59.93351 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 93c3410a-2116-35f5-a0bc-f85af65797ab | -11.40709 | -47.39698 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2534cf71-6694-3f3e-86b2-b26b2b61370a | -11.22789 | -51.37556 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 05a4316c-6989-3a63-9d6a-e3cf650640ee | -10.0777 | -46.01928 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 208d1343-9ac0-3c26-a901-846a1dced6a4 | -6.67959 | -55.05678 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fe8e7e7-dbf6-38fd-bae5-7895773ac71e | -12.13318 | -50.74264 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a1857842-4229-35cc-8f26-f7f5ed0b5f76 | -8.79309 | -45.64301 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dde9ae27-f53c-3da1-af29-30529c9b615c | -9.23843 | -47.37485 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 499c0236-551a-3ed7-bc81-7c27c60c90ee | -8.13821 | -46.82136 | 2026-09-24 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78b59b4a-cbef-36a9-9918-e0ea92124214 | -10.71649 | -48.73626 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fbe01eb-1ae2-3ef7-bb20-542633fbccfe | -12.33399 | -44.20822 | 2026-09-24 04:46:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6bea9b8-9bf7-38d2-9286-9481f8166c4a | -11.66105 | -43.49381 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| a4fa5542-f19f-320c-88a6-90317ff92f61 | -10.72537 | -48.74492 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40ccfc1f-eedb-3573-8d87-9761402c428c | -7.41915 | -49.8687 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05c738b3-6065-3b50-bf05-5ca9f3354f15 | -11.40313 | -47.4001 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2beab398-32d7-3028-9053-6b067c66573d | -12.12297 | -50.74091 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 2d60d300-1d25-3c8a-9d8c-39ec49ffa70f | -6.67547 | -58.58579 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce9a8584-e1bf-3752-bb86-efc5d09e42e2 | -9.14942 | -40.11398 | 2026-09-24 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7d9d7443-6642-36c8-99b6-b39258c9b46d | -11.46448 | -47.38667 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 785d2a02-2daa-365d-a78f-facee2bf1f6a | -11.6309 | -50.60971 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3622d24-d6d0-3956-af94-00029bc53a14 | -8.78107 | -45.8409 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eb32bfe-594d-3f87-b4f6-741991ec7706 | -6.60975 | -59.92191 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbc6d1bc-221e-3fbf-b3f2-cd6159ae3ea8 | -11.99371 | -52.46109 | 2026-09-24 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3de08022-66d2-3844-af25-bb0eb8fd5c2e | -9.47402 | -40.33969 | 2026-09-24 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 7f68dcbb-81ff-3289-bc8c-05425221998b | -11.39685 | -47.37262 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 084af71e-1e2d-347c-85d3-cb7f08189fcc | -6.08811 | -57.62966 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| add25191-c87f-341b-97eb-3372dcb15ce4 | -11.47872 | -47.38488 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86af9f3b-0470-3a0b-9137-5a0204209481 | -14.63664 | -50.60139 | 2026-09-24 04:46:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a22d38aa-dfae-370b-981a-18884d1a10ba | -7.43552 | -49.83319 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b82c9e29-461f-3a6c-ae51-2c125d9eb7e2 | -11.29231 | -51.31715 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| acd12bb6-f50c-37bf-8b9f-4d6faefcb764 | -11.49192 | -47.34468 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b8c0d0a-c1d7-3811-a4aa-c5ae8cefa234 | -11.43746 | -44.03052 | 2026-09-24 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 474c6023-4891-36c9-89ff-87a76cd4e49f | -8.14555 | -46.81878 | 2026-09-24 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9833bd41-9b38-37a6-8c9b-2aee0b28060b | -10.39072 | -46.56973 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 563ffc14-3e19-34a2-9ac2-53de3b1f3cab | -13.45863 | -46.25969 | 2026-09-24 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| db3cf6c3-b9e1-3a6c-adff-8857b8bd2e15 | -7.55476 | -55.01713 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6310e6df-549d-3f9c-abc5-9134873ea9e1 | -10.90757 | -53.95437 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91d4a5f3-be3e-3fbb-bee6-11001ef61a87 | -11.92769 | -50.73888 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5f63739-087c-35ae-8119-e839bdf0b482 | -11.4173 | -47.39864 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d401bc2-5f7d-3eec-8bba-7210716fc3f2 | -6.11505 | -59.89265 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18409b61-7246-3aca-988f-05099a2f1e97 | -10.14331 | -50.21765 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be5923a7-074d-3151-a136-88b6f488d7bc | -6.10403 | -59.87993 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 469369d7-84f8-3495-925d-708fff6d8f85 | -12.14539 | -50.75165 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 169a6ec9-28c5-3774-bb5a-0a753488be67 | -10.69875 | -48.71897 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0072046-0052-3765-bef2-c1d47c1ec7a8 | -7.89403 | -61.17883 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 618fc8cb-653b-3842-b3e4-1cdfcf6459c1 | -10.70429 | -48.72708 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07952b42-98ea-3e90-898f-bb2ef2b184e4 | -10.45385 | -51.29697 | 2026-09-24 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fde63a2-61b0-377f-b7b8-86fa6b361ab8 | -7.8806 | -61.18161 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86b4cec6-43e8-32c8-9a86-97b64d207995 | -7.88853 | -61.17694 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a0c92dd-741c-3cd1-9e09-4328dda2b48b | -11.79073 | -50.05667 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README51.md)
