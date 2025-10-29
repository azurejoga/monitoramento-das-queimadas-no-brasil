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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a100905a-cafa-3d8b-808c-cb4b01951922 | -10.42592 | -45.05177 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34303cd5-4a1e-3fe3-ada2-b9ae8782a3a3 | -7.50078 | -46.74722 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a96a84eb-d187-3219-a352-864bfae7b644 | -5.61208 | -47.11763 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9f5c8f6-9d29-3d5b-893e-3b28fcaccbc7 | -7.79929 | -46.43459 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4700af66-b04e-3367-91dc-53253320b88a | -9.58331 | -46.6366 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c379e32f-4421-3c29-82f8-dc356712cfeb | -8.18781 | -47.31005 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe7ab857-fc23-386f-bbcb-92cce664f464 | -8.72136 | -50.01299 | 2025-10-29 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3388b6ce-413c-3c6a-8d2e-8bdc1bd266f1 | -8.5465 | -45.70586 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f76a450-fdc0-317e-b50c-e249a585dd3b | -8.00685 | -46.20636 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a0d8ef2-1411-3946-b1af-89b852c7a7a1 | -7.50354 | -46.27641 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2aef1f7-4bbd-3b07-a798-ef3670d9d8e3 | -7.15724 | -47.24984 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d9cc0ff-ad81-3674-adc4-6070d86a7702 | -6.43916 | -42.36366 | 2025-10-29 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 587bc36a-6d53-3556-9b45-4c47b61d3f3f | -9.49264 | -47.00581 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0876c1f8-ae3d-3674-9b30-e57055d02ad0 | -5.53977 | -48.12738 | 2025-10-29 04:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f52dca9-1565-34ec-9015-9448dbf40874 | -6.43856 | -42.36753 | 2025-10-29 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9c2b2327-6704-3d41-8162-d61953863d5e | -5.16751 | -46.1626 | 2025-10-29 04:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d28f045e-ff63-3a14-b3b8-42a0517b85d8 | -7.49115 | -47.03732 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 055321e9-8405-3ead-910b-a41f8a2620ec | -9.94621 | -47.09465 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1d6a45d1-37a4-33c7-9652-69112ed08f13 | -10.90837 | -48.00298 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3644f40-46f4-3b29-8c35-03756d0ac4d0 | -7.3646 | -47.63729 | 2025-10-29 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 02c5557c-416e-3594-8228-6c652b93a41f | -7.36508 | -41.59304 | 2025-10-29 04:23:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7684b930-662c-3b92-895a-34d6a606d682 | -6.14039 | -41.71187 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 01be583d-08cf-3d4b-b0d6-02ce764bfcdf | -9.92657 | -47.6675 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 071f3ecc-c165-3372-b2c7-65e17c9519fd | -7.06737 | -44.47125 | 2025-10-29 04:23:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6293cee9-8766-3a98-bb9c-7d71a5a8e8d3 | -9.37134 | -43.68233 | 2025-10-29 04:23:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5d9d1591-306c-3fa6-a29e-71121062527e | -4.96194 | -48.26164 | 2025-10-29 04:23:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b8f93a5-23a2-3bd9-bd93-ca8e0073210c | -8.55761 | -45.70045 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c750ffe-7418-3bfb-ae9d-717f69174cdd | -6.08963 | -41.77943 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ea4fd341-2b15-3003-9a7d-0f64ae541ab5 | -6.13759 | -41.71421 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f9c3d299-4944-3fe6-b2a5-bc740ae636f5 | -10.29013 | -47.27918 | 2025-10-29 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7382e888-4cf8-3052-960c-40ae19113c26 | -9.091 | -47.81042 | 2025-10-29 04:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10f25ab6-bc40-3a68-b122-869c3ea06580 | -10.42528 | -44.99009 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c1bbe744-091e-3f01-afb0-6adc59f7aefa | -6.10818 | -42.45193 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 534f9d8c-1917-3758-98e8-5bc1874c7263 | -10.7757 | -44.75809 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85b39ce2-f4b3-3393-9685-4d1a9d008991 | -7.93624 | -45.47641 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea450e8b-fe35-3d46-9ee3-af4e1f7b0463 | -9.53675 | -46.9267 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 095d9ff7-53c0-3190-9132-f22dbdd768c7 | -11.05362 | -45.3647 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 096b66fd-5049-369b-9566-66af0243e88d | -8.50142 | -45.58784 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f225fa75-8690-3547-9ef8-6de0997de020 | -8.19065 | -44.4476 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df3501da-157d-3bf4-a842-af74d34b24b2 | -6.13062 | -41.85806 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e4616750-3ae7-3977-a499-725df39520ff | -7.35402 | -47.63525 | 2025-10-29 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0fbfb2d-680e-3562-88ed-5506e9a19ad3 | -10.90109 | -45.10911 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15156fa3-11cc-321e-9b89-e1a849ce4f6a | -10.35193 | -47.56487 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d1cf78d-5946-3bb0-8013-3775362e73f4 | -9.48983 | -47.00158 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e50139b-abd5-3999-8a5f-e421d0c12d0c | -7.29546 | -46.26871 | 2025-10-29 04:23:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f63601ab-0f20-3fdf-ae0c-1020e2b46b2b | -10.90746 | -47.80256 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8a8e69c-cd31-37dd-9923-36b55e40273a | -6.62644 | -47.18329 | 2025-10-29 04:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 528d1dc7-98ba-38a7-9323-97e5b31bc731 | -6.1127 | -41.72472 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8a51d2cc-175b-315f-a504-c743199f9d55 | -5.85539 | -47.70008 | 2025-10-29 04:23:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad4fb5b6-f6e7-3064-b07f-8df3c4f31e3a | -9.50595 | -46.96663 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8223703d-227c-3ad0-9ea3-0522f055edce | -7.42988 | -41.85592 | 2025-10-29 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 62f4085f-584a-39f2-8b26-b08967e3c3fa | -7.95288 | -45.45759 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07ae0631-c4a1-3cc2-ae56-6caad6051aec | -7.06434 | -44.94098 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7deb894b-5c9d-37ac-8b49-1764054a9b7b | -5.20115 | -46.14919 | 2025-10-29 04:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e8a00e3-215f-35b0-a917-f1d60dfd9956 | -8.38301 | -47.74757 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9b5035d-059a-3fee-b699-c896d7bed633 | -6.84724 | -48.0019 | 2025-10-29 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 693dad1e-41d3-3d80-b074-048f40d48968 | -8.96906 | -48.65022 | 2025-10-29 04:23:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c8702b7-051d-3e8a-a819-a94dd52c3d68 | -6.59795 | -46.27956 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c372cffa-460c-3bc4-8572-4a4c904dadd6 | -9.96544 | -47.08628 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa20ca0b-6544-3f97-8b4b-3e41e41abcfe | -6.26417 | -41.81103 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6abfda81-52df-34f3-877c-c110fd4c669c | -8.51163 | -48.28225 | 2025-10-29 04:23:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 525b11ce-2dfe-3c22-b410-b380f684b44c | -9.34046 | -43.08604 | 2025-10-29 04:23:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 84f1ab66-0c1e-3048-8506-87c43ff2e454 | -7.81234 | -46.41822 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02b09106-4ffe-3782-823e-79bd19f119bb | -5.42281 | -44.43218 | 2025-10-29 04:23:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2223d39f-6d81-34cf-bf6d-5705ccdd67ef | -9.38936 | -54.60355 | 2025-10-29 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a19cd67-d739-31dc-b125-83da0ead01ef | -5.61978 | -47.11477 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 54d8970b-7ad3-3279-a895-10efd0e28129 | -7.96333 | -46.73763 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 780bff16-aeeb-3ec2-b596-4e2df44dba5a | -7.32275 | -44.74009 | 2025-10-29 04:23:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33f40aad-6bdf-3f55-8f57-80a59274c73e | -7.80193 | -46.46105 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aac95f02-e5ef-3f58-ae32-9f89c3cb0320 | -7.69652 | -46.90041 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34662fb5-92c7-378c-a1c1-9bc10c7224c1 | -7.98611 | -45.54891 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64b822c3-d22d-3483-a7d4-2c2b372f008b | -10.94363 | -47.81197 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21bfcd2b-47be-3472-ae5c-cc4d50acae46 | -10.50906 | -47.73352 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 85e21758-681c-3e97-b45e-b68f5b5a9093 | -5.66875 | -45.20757 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ea28d17-784b-38d2-bce8-ffbe072f1c32 | -10.51377 | -47.72647 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 641084a5-49f2-3960-b58d-1d16c652aa6b | -10.78074 | -44.76992 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76b4b174-9426-35f5-8b9b-b692d5923f1e | -6.97794 | -47.33042 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e5e3f0c-ce1e-3293-a66d-e6e21207eb26 | -6.96837 | -46.23812 | 2025-10-29 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d2ea296-ddbd-390d-b7fe-c94c15f14a97 | -6.26775 | -41.81159 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fee7cde2-b1f0-3dd1-828e-2e8d3fb18b4d | -7.07264 | -44.93161 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8dfc099-e378-3ba6-b153-bc52b23f0ef4 | -9.73438 | -44.06469 | 2025-10-29 04:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c39b298b-a73e-38bd-b43e-f1e0377a2d11 | -7.28003 | -46.89821 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 23ccd2ed-640c-31ef-8e83-6b629db12eea | -10.85609 | -47.89962 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc7d53fd-573f-347c-8974-76f4bc2aa35d | -7.8975 | -49.17803 | 2025-10-29 04:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34e7a602-6c20-3636-bc63-43eccd42fe69 | -11.01184 | -47.78458 | 2025-10-29 04:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 703effb6-c92e-3451-9ccc-14267e18d352 | -6.11284 | -42.4448 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6194af73-9ef9-3de4-9ead-5b58b60602c8 | -9.16189 | -50.1347 | 2025-10-29 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27d42f15-baea-3ea5-903b-66c890ec9108 | -10.50969 | -47.7297 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3cb0af5b-0bff-3abe-a871-752133f204fd | -6.8842 | -45.0336 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83d492d8-d4d2-3869-8348-cb4be4d5e5a3 | -6.65794 | -44.27823 | 2025-10-29 04:23:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26c70cf0-1f16-3b58-ba42-ff51ae5acb43 | -5.34015 | -45.5447 | 2025-10-29 04:23:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baa30fa5-65fb-3828-bcb4-91ac3c5ce426 | -7.89424 | -45.68467 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bad808a-7d7f-3301-8c95-ac60cea6fa58 | -8.54742 | -45.68484 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2528a0c5-2f66-3f38-be2e-2dea15e29dec | -8.14335 | -49.4807 | 2025-10-29 04:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 319c7f50-5929-37cc-b55b-e95ef88b3e91 | -6.13819 | -41.71014 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 38bf0c06-fef6-3ca4-9971-478bd0328468 | -6.48955 | -42.24638 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1de1c38a-0818-3a5a-a7ab-91a4d808dc94 | -5.61192 | -47.11861 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56f737d4-5649-3253-80fc-c6b47f043f08 | -7.20418 | -44.15953 | 2025-10-29 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5827ea73-fe9f-33ae-a795-0bb2b1d5dea7 | -7.30096 | -44.98597 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bc3c041-1b97-39e6-bfa7-039b5acc336b | -10.54167 | -45.04834 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README34.md)
