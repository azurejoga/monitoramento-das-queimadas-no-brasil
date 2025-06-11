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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c104671e-8445-36dd-81e8-d49dc0ab8f01 | -10.6681 | -49.4246 | 2025-06-11 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 06313290-407c-398d-a447-e48fa4eaef53 | -7.4763 | -45.5099 | 2025-06-11 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 3beb4118-ad84-34d8-8f72-92a90b5825cb | -7.4575 | -45.5116 | 2025-06-11 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| c433efa7-421d-325f-a889-43653e68088b | -7.4765 | -45.4872 | 2025-06-11 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 26871559-e8f1-38a5-9ec6-90ead679769a | -12.5175 | -57.2231 | 2025-06-11 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ce4f0833-79bc-33f6-9f88-2c1741f542c8 | -10.8832 | -54.742 | 2025-06-11 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 212fd213-26ef-389e-9728-0893a9b27796 | -10.6492 | -49.4267 | 2025-06-11 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| a0e05b90-1fe2-3d1d-b15f-d3befd26a307 | -10.6681 | -49.4246 | 2025-06-11 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 77f28650-2e6e-384e-a94b-06188b1f00f4 | -10.6492 | -49.4267 | 2025-06-11 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 88b9b51e-2dd4-37dc-a80a-401bc1dbaf2e | -10.1933 | -49.5833 | 2025-06-11 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 264b82e2-2610-3805-9d1d-f04973ed4125 | -7.4763 | -45.5099 | 2025-06-11 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| a9a60ba0-08cf-3456-977d-ca5a8bc8152d | -10.8832 | -54.742 | 2025-06-11 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 73a53bb6-55a4-3568-a95f-a9e86fba81ca | -7.4765 | -45.4872 | 2025-06-11 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 435227a9-ec47-3864-ac1b-6f78092916a2 | -7.4575 | -45.5116 | 2025-06-11 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ed43ab2e-1868-3bb6-b78e-b3b1df505e58 | -3.6244 | -47.503399 | 2025-06-11 00:14:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 420e9748-8ce6-3d2a-b37b-d4c5e7474d19 | -5.9113 | -43.4501 | 2025-06-11 00:14:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e6ff5e4-a668-3d4c-a9f9-acef629f924e | -10.5175 | -53.616901 | 2025-06-11 00:14:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76ea3c7b-1176-35b9-806c-845763b461bf | -10.0738 | -52.739799 | 2025-06-11 00:14:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28508b85-c9be-363d-bf19-a2f5ada1fa2d | -12.2163 | -49.6255 | 2025-06-11 00:14:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d1e9a05-848b-302a-b9ae-cfb861a9e190 | -8.694 | -49.845001 | 2025-06-11 00:14:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fc1384c-d53b-3bfb-b3a9-ae9a09693d8c | -18.172701 | -46.941898 | 2025-06-11 00:14:00 | METOP-B | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 08af5159-d6c4-338d-a570-8bbaa49a5967 | -11.5893 | -51.3297 | 2025-06-11 00:14:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ca2d0537-aec3-3da4-8804-73c9ff6eab90 | -10.7032 | -49.500198 | 2025-06-11 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe4832ab-8127-38e0-8695-71ace5acf69e | -9.3876 | -48.407299 | 2025-06-11 00:14:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92485c0c-aa83-3dae-bcad-b0450de880f0 | -10.1981 | -49.584801 | 2025-06-11 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2252d6ad-c426-3509-a9f5-4a5ff9d6882e | -9.4037 | -48.433701 | 2025-06-11 00:14:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 278a7ab0-4680-3e51-aab5-b290d22a844c | -12.0686 | -47.312199 | 2025-06-11 00:14:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca806fcd-a6d5-34c5-9a73-d0492f8e9c0f | -5.7742 | -43.613602 | 2025-06-11 00:14:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05b764e0-197e-3ffe-afc1-0bcc9a05da17 | -8.7189 | -47.848301 | 2025-06-11 00:14:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad324fa3-95c2-360a-814b-171e360faeb4 | -16.586201 | -43.639198 | 2025-06-11 00:14:00 | METOP-B | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cebd4e34-e9fd-37a3-867b-a0757ccb0af6 | -13.0584 | -41.429298 | 2025-06-11 00:14:00 | METOP-B | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dd6f8c6f-e693-3bee-b69a-366354f4dd6a | -7.4215 | -47.7103 | 2025-06-11 00:14:00 | METOP-B | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58b696f0-0082-3e05-83db-51e7bb617b6c | -8.5508 | -48.251301 | 2025-06-11 00:14:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4e1b7fa-abe0-3534-b0f4-ea7dc8efbadc | -10.8689 | -54.304699 | 2025-06-11 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66a792b8-1272-37b6-9748-a84933dc76bd | -17.399401 | -48.058102 | 2025-06-11 00:14:00 | METOP-B | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25a2d163-63a9-3dcf-b1b8-1aec3c314aa3 | -9.8565 | -47.8731 | 2025-06-11 00:14:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e32fe0c6-5544-3218-8472-c72d1a3c059e | -14.2491 | -45.485401 | 2025-06-11 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 44c37fc8-472d-37f3-bf6e-261a349cd2de | -13.0609 | -41.439602 | 2025-06-11 00:14:00 | METOP-B | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f362744d-d2e6-36d1-bb7e-3a570665b5c9 | -12.5225 | -57.2005 | 2025-06-11 00:14:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 266e2247-485f-3a23-9b8a-034ec7a4b23b | -12.8452 | -47.383701 | 2025-06-11 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a95780d1-e2f6-3e37-85eb-e95d65ec50d1 | -7.4699 | -45.508301 | 2025-06-11 00:14:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3670c5a7-a29d-3fe7-bd7f-1b4c6e5bba0d | -11.3414 | -45.209499 | 2025-06-11 00:14:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 173f6a0e-1268-3e14-8840-840cf646c702 | -7.0086 | -44.6236 | 2025-06-11 00:14:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b678a95-332c-3971-b309-9c6ab48069b9 | -10.6666 | -49.425301 | 2025-06-11 00:14:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a34209ce-69b0-385d-a2ba-8bd01da90e69 | -12.7847 | -48.726299 | 2025-06-11 00:14:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2070d6a0-50ff-39b1-bc98-d77537561454 | -12.0701 | -47.319199 | 2025-06-11 00:14:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 742eb8c9-83b3-3008-be9b-88e26a2b0b2c | -12.2128 | -49.6087 | 2025-06-11 00:14:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7748071c-cac1-3029-b9ee-feeceaa435b5 | -6.9524 | -44.5588 | 2025-06-11 00:14:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 379cdb12-9965-391f-a6eb-4c98999b7ec7 | -10.8833 | -54.735401 | 2025-06-11 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 204ac95e-0f02-396b-9605-02e08141b1f4 | -7.74 | -44.174301 | 2025-06-11 00:14:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0a74ad2-6103-3451-934d-b7464bed648a | -3.5757 | -49.487801 | 2025-06-11 00:14:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef5c470f-3b3b-3167-9d26-ea8a09526069 | -14.2589 | -45.483101 | 2025-06-11 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fdb161bd-584f-38e2-b0fd-9ed086bc67cd | -5.9136 | -43.459801 | 2025-06-11 00:14:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99b4ac4f-3ac7-3dc3-a166-f5629172e4c6 | -10.6568 | -49.427399 | 2025-06-11 00:14:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04600d60-7a2b-3f92-85b1-905c44990dc3 | -11.623 | -41.82 | 2025-06-11 00:14:00 | METOP-B | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4dea5ecd-c2d7-3e57-9a0a-5cffc34c6410 | -7.4716 | -45.5158 | 2025-06-11 00:14:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99790446-5adf-348a-9c38-6aa10a9ed293 | -12.203 | -49.610802 | 2025-06-11 00:14:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ccfb2a3-0900-3ce3-aae6-52f6b60d9cec | -9.7714 | -48.188 | 2025-06-11 00:14:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 723aede3-9b80-3fd4-807f-c6d192d90727 | -13.903 | -48.729801 | 2025-06-11 00:14:00 | METOP-B | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 790be045-3926-3ca3-8736-3c5dd7960510 | -6.4953 | -47.484901 | 2025-06-11 00:14:00 | METOP-B | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7ed8a9c-7bda-3de3-954d-d947272a6a29 | -8.2797 | -44.947201 | 2025-06-11 00:14:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6cb6d86f-dda1-37a6-9b0c-01745c935d18 | -5.6481 | -43.6026 | 2025-06-11 00:14:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c41f3968-20bf-3680-83dc-70191752439f | -8.2832 | -44.962601 | 2025-06-11 00:14:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9873dab0-91bd-3f9a-904b-1acf65b2e1b4 | -9.4021 | -48.426498 | 2025-06-11 00:14:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3bd50552-b162-3a2e-92e2-88f273d84174 | -10.6633 | -49.4095 | 2025-06-11 00:14:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f92ede73-e073-38e1-8fb0-872e43e6591a | -7.6867 | -49.513 | 2025-06-11 00:14:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06069fd4-bcf9-345d-a9bd-60f05c55ccc4 | -11.3431 | -45.216702 | 2025-06-11 00:14:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3995d58-10bf-37f6-a95f-2003614fa45b | -11.6255 | -41.8302 | 2025-06-11 00:14:00 | METOP-B | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ac6db4cc-e34a-30da-a9fb-1beea4b2f7a9 | -8.1708 | -46.5051 | 2025-06-11 00:14:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 550468dd-ea7e-33b1-9023-07d7874712df | -7.8708 | -47.877499 | 2025-06-11 00:14:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef04fa5f-e2e6-350a-b3c6-021d1f5a2ae7 | -6.991 | -47.077599 | 2025-06-11 00:14:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e38c678-4b7c-3692-b326-a6278cc26540 | -12.1703 | -43.476501 | 2025-06-11 00:14:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03d2005e-8015-3677-8adc-b9c76a268fbd | -12.783 | -48.718498 | 2025-06-11 00:14:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d571f5b3-b78d-31b7-a772-7769dae8d064 | -8.2815 | -44.955002 | 2025-06-11 00:14:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a7000ef-f7e4-379b-8982-98aa19406587 | -14.2604 | -45.4902 | 2025-06-11 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 611b4148-12d9-32fa-91a6-a49d47b2b172 | -7.4584 | -45.503101 | 2025-06-11 00:14:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58f51c1c-442a-3d52-96e6-de6d95fd3a75 | -18.174299 | -46.9496 | 2025-06-11 00:14:00 | METOP-B | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 591baffa-ba1c-3574-8634-b730aa32adb6 | -2.9225 | -48.229198 | 2025-06-11 00:14:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27a1de80-675a-3edf-b6ee-d9a072d6a246 | -10.7066 | -49.516102 | 2025-06-11 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18afbbc8-a434-3198-9c78-b07438b0064f | -14.2507 | -45.4925 | 2025-06-11 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad6d42dd-ebcd-3d48-907c-98d39d330290 | -17.387899 | -48.052101 | 2025-06-11 00:14:00 | METOP-B | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 38ba433b-073d-3dd7-ab15-5c4d0d171a00 | -11.0104 | -44.350399 | 2025-06-11 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94c6d16e-39c5-385e-8e07-3a1a36459512 | -6.4938 | -47.478001 | 2025-06-11 00:14:00 | METOP-B | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 838c72f4-6b80-306c-b060-01fedcb8e4e1 | -12.5178 | -57.1745 | 2025-06-11 00:14:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad03ea3-29bf-3c3b-9ed1-3298de374235 | -14.2523 | -45.4995 | 2025-06-11 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 298d1273-f611-342d-9a8a-5469c731ec18 | -10.6552 | -49.419498 | 2025-06-11 00:14:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17a26e2c-0fa0-3d02-9355-9f90044f058f | -4.4937 | -43.777699 | 2025-06-11 00:14:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d576bd0e-687b-33a3-8f26-64c810aaa178 | -4.1594 | -46.181 | 2025-06-11 00:14:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31fe5728-b543-329e-aac3-01952efacaf8 | -20.7598 | -48.526199 | 2025-06-11 00:14:00 | METOP-B | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 924f7712-8e61-3922-b544-b987bc0d3999 | -11.0086 | -44.342602 | 2025-06-11 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90bce1af-d71e-37c4-9b56-a8c49e397b78 | -10.665 | -49.4174 | 2025-06-11 00:14:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f3820ae-34da-3352-b6fc-60823471dded | -8.1692 | -46.4981 | 2025-06-11 00:14:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae31b453-cd75-313d-b32d-3879f39b1c14 | -10.0484 | -48.655399 | 2025-06-11 00:14:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34297fae-5a1a-339f-831b-5f9974ecdc1a | -4.4914 | -43.768002 | 2025-06-11 00:14:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa1c3ade-f601-3cc8-a47b-894898f71b51 | -10.19 | -49.594898 | 2025-06-11 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04fb7a2b-cea0-3e2e-a2cb-fd8ca14a2f8f | -9.8931 | -47.806099 | 2025-06-11 00:14:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afdc4f4e-965f-3fcd-85e1-d0604cce521e | -2.924 | -48.236099 | 2025-06-11 00:14:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ebd6ee9-4a5a-3986-a485-bbd00417242c | -9.5368 | -47.498402 | 2025-06-11 00:14:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06471333-87db-3e14-b943-5741a58f2e29 | -10.7049 | -49.508202 | 2025-06-11 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71828afc-954c-331d-91df-d6571543b459 | -4.5701 | -43.087101 | 2025-06-11 00:14:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
