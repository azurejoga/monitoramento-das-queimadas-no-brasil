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
| c93fd58a-58cc-33a4-a4bd-051f958a7b38 | -11.20337 | -54.90518 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9be39be-4c1d-3c5c-8d07-95a30b209463 | -4.47284 | -55.4325 | 2026-08-05 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6279b219-0e66-3d9c-b6c0-b0acc6493f8d | -8.66014 | -54.97417 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35c0b490-5fbd-38c8-ac8c-1e056ceab709 | -6.00719 | -47.40026 | 2026-08-05 05:23:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 586a3719-b313-3738-8208-1ab24f47365f | -9.14287 | -49.66193 | 2026-08-05 05:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49ea67d6-eb02-338f-bb8c-919a613dd47c | -6.65163 | -56.41871 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79a2c83e-039c-311a-be7b-b8c89ffd7bd9 | -11.18403 | -54.87232 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dff78229-67af-3f1a-9ca1-d85d9736e9f5 | -6.55786 | -55.15086 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 947a48f8-a2c9-3b52-9c4b-54f6292f204b | -6.56536 | -55.17186 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca87c6fe-01b0-3316-aa65-d361971debd4 | -9.14246 | -49.66497 | 2026-08-05 05:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e5e3458-4577-3b61-bf61-9e4193c824b8 | -11.22857 | -54.8629 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21ae0cf9-c3c8-3c7e-943d-e444a83ba6c9 | -11.17043 | -54.89573 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 310d3185-0401-3cc2-96f9-cb51f5551d9a | -10.45515 | -50.22035 | 2026-08-05 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8b28e00-a2ee-365c-a966-48b33bae301e | -11.19592 | -54.90402 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f439219-9e27-3ae7-b57f-b9c2511001cb | -10.79036 | -47.70525 | 2026-08-05 05:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 074be4f6-36ed-3e0f-ba80-9fbbbe52c235 | -8.34709 | -45.97735 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c2203942-b624-308e-a3b1-21092374417d | -6.56769 | -56.52587 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05b5ebfe-b6ad-385c-b602-2321c8da9993 | -8.34167 | -45.97721 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 295b5eff-eeeb-34cb-8a61-d1d43ab6d093 | -11.56036 | -47.71131 | 2026-08-05 05:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9805b6e-eb90-3ce3-867e-d3807e4e7696 | -11.20775 | -54.90123 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f5e8b7d-4a2e-32c0-b756-1ce5cefa3458 | -11.18035 | -54.90633 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 68df0f5f-d3ea-3485-a5c9-67baba4d25a6 | -6.57005 | -55.16467 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f0b84d9-bac7-39ab-bba3-34e4670ffbff | -11.17363 | -54.91651 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ec65dc6-66b7-3136-97ba-85463da7d710 | -6.56186 | -55.17132 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 479aa316-2b44-307f-af12-e24d8d947c24 | -11.19836 | -54.91355 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82d761c5-dff3-386e-905a-d0a82eb2ec50 | -11.16536 | -54.86951 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf65b7c4-35e5-355f-8eb1-8c36bf74e5fa | -11.16882 | -54.8976 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 99e0f33d-1cb1-3de5-8b21-671755ae898e | -11.17189 | -54.9026 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1286b1fb-bc2d-34d0-af1f-0174371fab30 | -11.20954 | -54.91522 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c1cf633-b222-3da0-b308-72e6e842da78 | -7.62464 | -45.30997 | 2026-08-05 05:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee0ea4d8-040c-3e0e-8627-9ca2bd3b5a06 | -6.55428 | -55.17411 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51ecf1f9-99ef-3808-9c55-57f2edbc38f7 | -11.18614 | -54.86582 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b4a4088-dc7d-3bd2-a95a-608eca3eb10a | -6.01235 | -47.40498 | 2026-08-05 05:23:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4aee5005-986c-3f93-887e-8ec73f8c82d2 | -6.55376 | -55.15419 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62f0f344-7549-3d09-b416-ab7caf4342f9 | -6.55896 | -55.16692 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24e0484c-3877-33be-b64c-6aa2d0c67073 | -11.16469 | -54.87404 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 323f81de-2988-3cee-ac0a-234cd68e2427 | -11.17282 | -54.87068 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ede78f55-c43c-3da9-9fc5-febdd3b15be9 | -6.58606 | -52.21873 | 2026-08-05 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 27e1ec8b-963a-3d8f-9d5e-1816506343af | -11.21522 | -54.9023 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1df6628c-ac4d-3664-9064-dff3c4429273 | -5.37246 | -55.88454 | 2026-08-05 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 663856d2-01c8-3cdb-9829-4d478beed388 | -11.17234 | -54.88231 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 139b564c-3502-3716-bfe3-56be158db8fb | -6.09975 | -55.813 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86325a2d-29bd-3f93-8e37-5c804af56bf5 | -11.16991 | -54.91594 | 2026-08-05 05:23:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2d038f62-a36e-3ab3-8a30-c0a1eef15f6a | -11.20369 | -54.84992 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c250ea93-c2d2-378b-b68c-d504df67aac8 | -11.16775 | -54.87915 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59bcb79e-8644-3b3c-9c30-6324f0162af9 | -11.16751 | -54.90648 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 23ab85fe-6021-3020-ae4d-b32e2275854a | -6.56254 | -55.14371 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 917af974-9574-3267-a13e-6f499e47fdd7 | -11.18201 | -54.88584 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 715ad64f-6dee-35bf-ba16-9b0fc2701ff1 | -11.17607 | -54.88287 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13fbd730-715e-33ab-b9cc-266931adfb61 | -11.16378 | -54.90591 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 401fd711-c40b-3aff-914e-6ceb43edb3fd | -6.56596 | -55.168 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b352af2c-63d3-3dc9-b7e7-111b053f30ed | -11.18135 | -54.89032 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b652015-6952-32a3-bb94-bee2ca62f62c | -11.1878 | -54.90745 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 77dfce80-e0e2-39d1-b58a-a4389bf9eb9c | -11.16444 | -54.90147 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ed72a8d-4386-3b84-be57-3b4f55fc8841 | -6.54676 | -55.15313 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 62745da3-a69b-37b9-a38b-24dbe87ff3c7 | -11.18909 | -54.89847 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b06d1f2-1966-3679-8870-caf2c51673f1 | -9.61206 | -47.77376 | 2026-08-05 05:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac702c82-6da2-346d-aaa1-9449a605b25a | -4.95747 | -62.35587 | 2026-08-05 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d8a38e9-7872-3a0d-8a57-b6c7ce9dab86 | -6.72416 | -58.93176 | 2026-08-05 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 542f7b6b-013b-3026-be56-e1afb7b47797 | -8.38156 | -48.21523 | 2026-08-05 05:23:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9de8c01c-099e-3bd8-b2d6-b7ba5dc260b7 | -11.20144 | -54.91857 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5c4a0461-9bd8-3940-ad77-a525e0412c40 | -11.17521 | -54.88028 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2cfbaa7-9f50-3fd1-bb42-f6b820f1ca5e | -7.50479 | -49.74577 | 2026-08-05 05:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8df63251-4da2-302d-a6f6-77a31dcaa012 | -11.19771 | -54.918 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50f1b0eb-37fa-3bf2-80ec-0c42247ba7d8 | -11.19656 | -54.89954 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52eeb35f-f0f6-3da7-9726-999cff612cbf | -6.42339 | -55.79462 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 516420c5-a823-3e34-b1e4-f8fde6d466c6 | -6.72474 | -58.92816 | 2026-08-05 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ba29775-21c9-3502-a4d1-c2a2b61da498 | -11.18291 | -54.88842 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce66f6ee-b266-304d-a1c3-6f8a3d051701 | -11.17907 | -54.91527 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 754778fe-8f26-37ae-9cd1-39d37f43ed90 | -6.9556 | -52.80409 | 2026-08-05 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebe3131a-9128-3c5a-9625-55c445dcabfc | -11.17388 | -54.88925 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 399988e4-5308-392a-827e-377c0f9c5697 | -6.65254 | -43.90898 | 2026-08-05 05:23:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8710440-957f-3d0f-b07b-7f1e66b9ad18 | -11.55488 | -47.70602 | 2026-08-05 05:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9147fcf3-8b3c-37c8-a0d5-81fd1e0ba052 | -14.18514 | -54.41222 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37ae1f53-32fc-3c2e-9788-7e3795002a41 | -11.18163 | -54.89737 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7eb5ef4-0026-31c0-b6d5-4cfb1a04243f | -11.17828 | -54.88531 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6f5c9c3-9c51-3a6f-b300-d07e1f7df128 | -6.53568 | -55.15534 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c589e0e9-e1de-3d7a-a87a-2adb9ef4d44d | -11.21084 | -54.90628 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19d51015-86ab-3dcb-b7bf-efa8b03b41ae | -11.198 | -54.86296 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 997e28f0-01ca-3c76-8e88-eec308d6ceba | -6.53509 | -55.15922 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af525844-3780-351b-b4f3-0af6db7b16fc | -11.19347 | -54.89451 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9eb7022e-5bd2-30a8-9b6d-dcead958db63 | -6.55086 | -55.14975 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95a73e7d-a5cd-3c03-8642-703736a9073c | -11.20094 | -54.89563 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be58f411-791c-3edb-91b6-3bdd0685845c | -11.19476 | -54.88552 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94f4956c-5924-32eb-82e2-17e22c8dc12c | -11.20402 | -54.90069 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00b71fb5-2814-30f3-9bcd-899f9586a8f9 | -11.23914 | -54.03806 | 2026-08-05 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 836ec497-f365-3d0b-a7bc-5c1cc14ab83a | -6.22726 | -55.5951 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca4169cf-e57d-3106-9957-14f122367715 | -6.57295 | -55.16908 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cb23211-f438-31d6-9a0b-aceaa48d583f | -11.17562 | -54.90316 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e609a47e-94b4-30d4-8d0b-e96d4bf79d88 | -6.10371 | -55.80988 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32367b3c-9f80-33c8-8404-e879e1ff416f | -6.57415 | -55.16133 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 853063fc-8bda-34b8-8001-61d75ce0a208 | -17.97963 | -47.16328 | 2026-08-05 05:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d57e2f7e-37a4-3f98-a569-460e596f46e1 | -6.57704 | -55.16575 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a41d00cc-8323-3ff0-8897-8dfde0b6549a | -17.99411 | -47.15286 | 2026-08-05 05:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2942766f-705c-3fbe-90e2-64f3d0a55779 | -6.9534 | -52.80757 | 2026-08-05 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 897b5248-5284-3e97-b739-3f226036833e | -11.205 | -54.84077 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6f787fe-1892-3bf0-831c-e87f307cf418 | -14.19499 | -54.42948 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22c03021-6fdd-3886-bb23-b115c29131c9 | -7.36354 | -49.55348 | 2026-08-05 05:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 411dfe54-22db-3ff3-9ffb-32472a17c1f9 | -6.55488 | -55.17022 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 069a02fc-2e55-321f-b337-c2b94f7d785a | -6.58612 | -56.53967 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README24.md)
