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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24b7d7ac-c910-35e2-85a3-6e55f344149f | -14.38149 | -51.87044 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23c06788-b81c-37af-8f62-798c034fa714 | -10.50148 | -50.01322 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aaab546-5228-3979-9de8-81a55748da6e | -9.18342 | -60.80306 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d55c4b5-7b37-38d8-afe7-84907f9d274d | -10.50494 | -50.01375 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 539a7fc4-1102-3097-a91c-3fb584e664db | -11.28012 | -45.82204 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cdffe8d-f1c1-36ae-a94a-c2171f380397 | -14.4779 | -52.09055 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0c5e87c-6be6-33eb-9ffe-2ee10f5f20fc | -6.7743 | -59.77028 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ecff40c6-8252-3583-b87a-423f3652506e | -10.94253 | -57.15238 | 2026-08-17 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4d051244-b955-3121-834b-3194863dfe0d | -13.51054 | -46.23154 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 16e4a529-d32e-3e9a-86e4-d9f13672eb80 | -14.71632 | -52.88692 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb6df6d5-cf68-3c30-a8ea-85a9577464f7 | -6.70748 | -58.95866 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ca64721-97ce-31fa-a489-79fca49a7208 | -9.54554 | -56.79776 | 2026-08-17 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9f1ac3f-7e8a-3761-9674-7f9c59727777 | -11.21357 | -54.01758 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee1e2414-5d5b-3f79-9423-57d2ca5e5f28 | -8.95272 | -60.56426 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c834b290-c5a0-3ed1-98b3-399ca261c970 | -12.02266 | -46.50462 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b948c31e-3145-34a1-833b-63f7c701aa6f | -6.82714 | -56.45921 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85ed4202-71cc-3360-8aa9-22c5f84a5a05 | -12.37004 | -50.88741 | 2026-08-17 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 226b5aca-8751-32ac-8e0b-7d544664f024 | -13.41756 | -57.04902 | 2026-08-17 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02d2a067-c271-3f38-9e7e-dae2a88399e7 | -6.54705 | -58.50407 | 2026-08-17 04:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6094f7a4-8b62-3119-b9a3-7fda7d4195c6 | -6.6266 | -59.0597 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75762f4a-f894-3a8b-93f0-3cac875892e6 | -6.82839 | -56.45196 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6a0d333-e7a9-312f-a9cc-89363d1f8804 | -7.37394 | -55.50948 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fcf614e-df67-33d6-8163-429bd98a261d | -12.68925 | -48.51931 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 43adabae-17e9-3df8-a298-84b31663a9bf | -11.23857 | -54.01437 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67c4419b-64d9-3e9f-b412-aa05cad46e81 | -11.21268 | -54.81451 | 2026-08-17 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adf6171b-c47a-3894-b322-af70380e2e64 | -11.3939 | -46.39562 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64f369bd-d70d-32c4-840b-6a0a7933e0ed | -8.95153 | -60.57076 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b33ddb7d-5619-368f-a86c-a7cfabd0e58a | -6.86366 | -56.41732 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4118c1a7-3803-32d6-a016-60507f6d7eb0 | -6.85601 | -58.98111 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c59d847-576d-3487-b3a6-1d8b23402daf | -15.07538 | -48.72155 | 2026-08-17 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9fdcf191-ce90-3312-a610-64d28f3f2c65 | -11.70135 | -54.6161 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac903dfa-1338-3ac5-b0e0-db310cd3d854 | -11.32823 | -55.22667 | 2026-08-17 04:57:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b1cdbcc-abbb-32a4-8924-8a0555c481ec | -6.60693 | -58.97243 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5b35231e-f339-3665-9280-b089aedd180a | -11.1376 | -49.04099 | 2026-08-17 04:57:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a0d7d1c7-cc34-3e2b-b65b-1a3090e8b1b2 | -8.96823 | -60.5089 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 417741a8-7b61-3095-bd33-7f4f7f574bd7 | -11.32948 | -46.21246 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33df5c8c-487c-3a37-b751-108fe5ffff15 | -14.5013 | -53.09306 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6963be2d-95df-30fd-a66e-6e869ca97a19 | -14.32349 | -53.09995 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 199663d1-9064-3e0b-bc43-35c1711cba11 | -11.49644 | -46.58186 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75d9c898-53c2-33e2-b74b-c58c7d585f6b | -14.30566 | -53.11143 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7491e11d-ccf2-30bc-933d-4d3d37a54b3a | -15.02852 | -47.03576 | 2026-08-17 04:57:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a0efbd6-c759-3669-9173-3f0220917ebd | -8.95731 | -60.56851 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf718239-42c7-3c16-9c65-ef82eb02afa8 | -6.63886 | -58.96158 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a33fa1e4-7847-3e76-ad41-cea3059a33b5 | -11.55233 | -47.17229 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72372107-5a57-3154-9959-d52940e70db3 | -6.82589 | -56.44859 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa694582-749d-3a1d-af91-73a5eadca4f2 | -8.10574 | -51.65963 | 2026-08-17 04:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60de7e41-21a2-31e4-990f-47ab0641499c | -6.86179 | -58.97658 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcb9d9d4-4abd-3943-9299-4b3d75eca775 | -12.25007 | -43.14449 | 2026-08-17 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b52070ac-dc2c-3695-af12-53a90826ffa5 | -8.95503 | -60.52255 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b114ce68-b859-3d4d-a65f-9020a9201873 | -11.32051 | -46.30714 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33b61bd9-131e-3947-a580-c63e2dc9d00c | -13.43122 | -57.06134 | 2026-08-17 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4f90085-9d92-316e-91bc-10b58acef00c | -10.50954 | -50.00666 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edc857ae-97cd-35ad-8f42-8ed6219e25e2 | -14.4979 | -45.68105 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4c2f37b-90c4-38c0-a4b7-a173d8eae699 | -13.75658 | -53.43003 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e168c39f-583b-35a4-a659-09a6263bdc93 | -7.6135 | -60.9493 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73e5d5ae-8391-3494-9f8a-64b163b34a4d | -9.34785 | -50.33064 | 2026-08-17 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35e7868d-e556-3982-bc48-02c389ab6297 | -15.13597 | -50.05541 | 2026-08-17 04:57:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1ca1995-9ae6-3bb0-85bf-42d779673a99 | -11.79086 | -51.78644 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41b140bf-7b75-3b1c-9e95-27edc9ba9845 | -14.88387 | -46.64095 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21bc8c79-00b5-3589-9225-f4c7e91fd689 | -12.90229 | -52.8251 | 2026-08-17 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c3c83aa-deb5-3fc2-8cb0-6ad7dfc301ea | -7.55595 | -61.17288 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c182166-b32f-362b-99e0-f62ac381d18e | -14.44302 | -51.97326 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad3577bf-c0d9-3661-8453-75ede0401db5 | -8.95557 | -60.54873 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1b55efe-6aa6-302b-9a1e-899e442ff8bf | -13.63601 | -56.99418 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 35c32bcc-2990-32a0-8798-f7c2d9e2dcbc | -14.88954 | -46.63203 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6bfaa9b-e4e9-3a6c-95c2-a4b0dc8d3869 | -14.48852 | -45.67981 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90c4f13a-bdac-3f6c-af86-87844f3fd731 | -14.28588 | -53.06436 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2408de62-ccdd-3835-a2b4-749addab8ec7 | -7.37786 | -55.486 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aebc8830-5c17-38c7-8434-cc0d34097ce8 | -11.2238 | -54.01936 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16d22d38-7cac-39b7-bcd4-f18920719feb | -6.86712 | -56.4216 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad0a3254-1a1e-337b-a978-d0b88181c4d8 | -8.63553 | -54.72957 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e632d4ec-acdc-3494-b2fa-a4996a0cb9f4 | -6.54237 | -58.50312 | 2026-08-17 04:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a658ac9-7d67-3235-b85d-570d6794a10b | -14.07293 | -53.58891 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ab7e7e4d-21c7-3261-a514-e7bfc70d9d99 | -11.13538 | -46.49174 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 54194b00-47bb-3a26-a26b-c510db8dc645 | -13.42738 | -57.06068 | 2026-08-17 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89963258-e536-3462-9f73-db8a7f664b5a | -8.7353 | -45.30531 | 2026-08-17 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f96ae66-83fa-3e9d-8e68-16c6865121a4 | -12.00579 | -46.46848 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed1a9680-e39f-388d-8e32-4bcc53114dca | -6.97899 | -59.03786 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35e42c1c-10d5-355e-8135-48920595b252 | -10.5153 | -50.01536 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7e147e6-1727-386e-a4bf-3bbb2266d20a | -9.18868 | -60.80401 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e027062-4854-36c8-a3ea-4193b12ca780 | -8.21153 | -55.00711 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94d88293-e44f-3232-823a-e84f615d35f2 | -14.30622 | -53.10788 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41d367f3-55a0-3a63-9c9b-567da623c350 | -14.37926 | -51.86259 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45b00143-488c-31fb-a0fd-924755f22db5 | -13.81254 | -53.83733 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 469c4e61-6138-3198-a89d-4e356df7ba31 | -11.20851 | -54.81787 | 2026-08-17 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8a7eb42-3fad-3e17-9bbe-c0923d4f02cc | -8.98262 | -60.5179 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b40dd34-90de-3b0d-9c26-d5a20c6674c4 | -6.63792 | -58.9669 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8cd2bad5-2057-3591-88e4-22e0f7b22dd3 | -7.38626 | -55.48258 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 330854f9-1735-332b-a5c2-b036819056c2 | -7.56022 | -60.86814 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d7a0d1ab-ff94-327f-af3c-361051feed12 | -12.90505 | -52.82919 | 2026-08-17 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6f54133-ed40-3bf4-a467-6cb5985fea4b | -6.7802 | -59.4686 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8318c137-1346-3670-92fe-64c67c665bcb | -7.39386 | -60.00954 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba342b08-148b-3ac4-99cf-e584ff53e731 | -7.38245 | -55.48196 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1564650a-68c2-3ccf-b4cf-3bce1f9f3199 | -8.95561 | -60.51941 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47cab746-83fd-3269-ab14-cbb57f871622 | -14.30784 | -47.20103 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 702607d8-ddea-3bb3-a15f-b054ea882b64 | -9.11946 | -46.00981 | 2026-08-17 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a447178d-44bd-32df-9ee2-28686d719107 | -8.64122 | -54.71778 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34a6444f-6fbb-3fd5-a92d-f187c0cfccb3 | -8.37518 | -46.37391 | 2026-08-17 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9870e9e9-4070-3778-90e4-64f410a62b93 | -13.44342 | -43.84058 | 2026-08-17 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92a6aefc-d117-3365-8987-08aa4824180e | -7.55662 | -61.16921 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README31.md)
