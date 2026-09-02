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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56d2efef-c829-35c7-8d7c-7a6b999e4aa8 | -10.9565 | -50.467 | 2026-09-02 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 4c93c26c-1b51-390c-bdd1-d6dc27bc1c8b | -10.5788 | -47.7306 | 2026-09-02 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 6bcace39-da90-3d0b-88e7-d516fe8ac7a3 | -7.9614 | -44.2519 | 2026-09-02 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| fc526643-be97-38fd-b9ff-3abef1b95651 | -11.5483 | -45.4446 | 2026-09-02 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 9a9949b5-8798-365e-bce8-c5be33d9bbdd | -11.8435 | -46.0649 | 2026-09-02 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| f7ebd69a-3a87-3a39-807c-dbcb97608651 | -10.3196 | -50.0211 | 2026-09-02 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 48406189-9aa4-3eea-9063-b4b15183cf7f | -11.8623 | -46.085 | 2026-09-02 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 1ac01e60-1fcd-31de-8804-55744d810e5d | -6.6765 | -58.7492 | 2026-09-02 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 855e0860-05fa-314f-bae0-6d1bffb0c171 | -11.8623 | -46.085 | 2026-09-02 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 207.1 |
| 07f2d353-33c6-3579-949b-166055acff0d | -8.7613 | -62.5869 | 2026-09-02 13:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| d6266ac0-2741-325d-8c66-8d1b6f6fcc2e | -11.3052 | -45.1344 | 2026-09-02 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| bc42aad3-55f2-3452-b9f9-9d4a7135b36a | -6.1474 | -57.7605 | 2026-09-02 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| e36086a3-5a4c-3e1a-9415-b6c7be3f2b61 | -6.1475 | -57.741 | 2026-09-02 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 482034f2-6342-35ca-afd8-85f0dfe4d635 | -12.3818 | -48.1433 | 2026-09-02 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 1a961bc7-3d34-3698-82aa-1f1e4ec9a9d2 | -12.1312 | -47.1309 | 2026-09-02 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 028b8e9a-7511-3fb5-86ac-4a2520c084fa | -11.3239 | -45.1548 | 2026-09-02 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 07b0b3f9-3b37-31a2-9d57-44d026131f30 | -7.9614 | -44.2519 | 2026-09-02 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| df4d2576-910a-341a-abd9-09028c00f1c2 | -3.2455 | -47.9187 | 2026-09-02 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 659ab249-77b4-39f1-b658-6840de6a67ef | -6.6764 | -58.7686 | 2026-09-02 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 6d143f54-bab8-3902-9fef-8fcc2cd0bbc7 | -6.6948 | -58.7678 | 2026-09-02 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 851024a7-05e2-39df-bdaf-fbc67fd9f0d7 | -8.4235 | -44.9849 | 2026-09-02 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| f2d01449-128f-36f3-a193-48b1c929c649 | -11.5483 | -45.4446 | 2026-09-02 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 71c9197f-b6d3-3fd9-94aa-b4949b7ca3fa | -10.9565 | -50.467 | 2026-09-02 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 24c60ae9-99e9-31fd-932c-408a9dc89c72 | -6.6949 | -58.7485 | 2026-09-02 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7e762d70-96a7-3bbe-8508-871adfe95076 | -10.3196 | -50.0211 | 2026-09-02 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 5f52b01c-705b-3815-9ce7-35d50c246d60 | -7.2255 | -42.7616 | 2026-09-02 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 6d53e084-b186-3656-91d8-b2d078ecd3d9 | -12.0936 | -47.0913 | 2026-09-02 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| e170b705-cd6c-386a-9908-98abeea0e6b7 | -11.3771 | -45.4 | 2026-09-02 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 7ab7b91c-4601-3d5a-ba09-2e5efde78bc3 | -11.3575 | -45.4257 | 2026-09-02 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 10e84f4b-d02e-3fc8-aa49-745224d38aa9 | -6.1659 | -57.7403 | 2026-09-02 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 8dd65c9c-7b4d-397c-99e6-5049cc62709e | -11.3767 | -45.423 | 2026-09-02 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 0aaf4a09-43a0-3ed7-a8ff-fe0e539fdc71 | -12.0741 | -47.1164 | 2026-09-02 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 97ff8ae7-b7e2-3a7e-9e30-df77e5a39e70 | -13.5724 | -59.7362 | 2026-09-02 13:00:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| d7106722-1182-383a-8ce6-a52f57bbeac9 | -11.3579 | -45.4027 | 2026-09-02 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 4436b995-83d3-345b-a413-48c33dc5e89c | -12.3622 | -48.1681 | 2026-09-02 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 196.2 |
| e682b633-bb31-3250-afd8-95aa7cf4df49 | -5.5833 | -60.1924 | 2026-09-02 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a28627bc-4e5f-3e90-8231-35d463b911da | -12.3626 | -48.1459 | 2026-09-02 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 183.0 |
| ca4ee981-6958-322e-89ad-e7d136e72489 | -12.1504 | -47.1283 | 2026-09-02 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 4414e67e-66f8-39da-bb73-04dd7ead639f | -11.8435 | -46.0649 | 2026-09-02 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 5e7cf3f8-5e74-3df9-95e8-c0cd3ed18fae | -10.9562 | -50.4884 | 2026-09-02 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 532f585c-b081-32de-b401-b136ffa65bfe | -12.3814 | -48.1655 | 2026-09-02 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| aa22cb5f-3c38-385c-a5a8-bbc6ddd28666 | -10.5788 | -47.7306 | 2026-09-02 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 2a594378-8340-3f75-a5b4-0fb54e121273 | -10.3193 | -50.0425 | 2026-09-02 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 22b851e5-8188-3a9b-afeb-e259dc5512aa | -11.3048 | -45.1575 | 2026-09-02 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 86681766-1e7f-3cc7-8065-16ce9edcd13a | -11.3044 | -45.1805 | 2026-09-02 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| eaf1b71e-464d-3f77-be47-a2bbe0c6706d | -11.3575 | -45.4257 | 2026-09-02 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 5ee4ff85-7a41-34ab-8f72-348f3e8d785f | -11.5483 | -45.4446 | 2026-09-02 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f473b1fc-272a-3ad9-bd8b-2dc93b4c0093 | -12.1312 | -47.1309 | 2026-09-02 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 7d264b8c-cccb-329f-9bda-c0e7282b2e73 | -13.9662 | -58.6936 | 2026-09-02 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 65d55b19-29a4-3504-b78e-f3c1c7e038b5 | -12.3626 | -48.1459 | 2026-09-02 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 2c6d448b-708d-3e8b-893d-84aefa1725a4 | -6.6948 | -58.7678 | 2026-09-02 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| a6a71106-6e50-3b61-82f2-cea1c067a36f | -12.1504 | -47.1283 | 2026-09-02 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| eeab9795-77f6-3d7c-8c5f-028f0fba160c | -7.3487 | -60.5883 | 2026-09-02 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0202c920-6593-36cd-b2eb-24c749757758 | -5.5833 | -60.1924 | 2026-09-02 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 76ad19b1-5c6b-354c-b9dc-1b748ab867a8 | -11.3771 | -45.4 | 2026-09-02 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 316.4 |
| 8dabd842-9cae-3e24-850d-aa1fe7c4e18f | -7.9614 | -44.2519 | 2026-09-02 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 431c3e5c-2359-3988-ac6c-4c21c37b01e1 | -12.0741 | -47.1164 | 2026-09-02 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 73b6f25e-4dc1-3210-8de9-314656727688 | -10.3007 | -50.023 | 2026-09-02 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 984849dc-832d-3a7e-9139-10a3e5d798a0 | -6.6541 | -59.4452 | 2026-09-02 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ae28238e-42fc-3994-914b-a78d39e9e18d | -8.4673 | -54.6833 | 2026-09-02 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 0da32635-cc24-32d1-8ae7-e177f5399255 | -14.1083 | -45.5008 | 2026-09-02 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 02846b3b-8b17-3192-a0f9-d2cddc314f0f | -10.3193 | -50.0425 | 2026-09-02 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d83187db-2efa-3c6b-89ca-15cb12c4995d | -7.3671 | -60.6067 | 2026-09-02 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 187.7 |
| f68b74a5-6285-337b-94e7-eaf00659a02c | -8.4298 | -54.706 | 2026-09-02 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 2e86dd3d-4743-3eb5-9314-e4ba00304d62 | -6.1475 | -57.741 | 2026-09-02 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f286d4ad-c84a-36f8-a252-58f86c48a4b3 | -10.8891 | -47.294 | 2026-09-02 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| ad837226-be0e-30c6-a827-26064787c8bc | -10.3004 | -50.0445 | 2026-09-02 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| d39a0510-7682-33d3-8c43-ac7620ade930 | -8.4485 | -54.7048 | 2026-09-02 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 152.4 |
| 333e8bc7-4c2a-3388-ac35-7127074426bf | -10.7774 | -44.7463 | 2026-09-02 13:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e88a2869-72ec-34aa-80f4-75215f08cb45 | -8.4483 | -54.725 | 2026-09-02 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| bcdf2180-8e9b-33e3-a6c6-6501a8e97fd2 | -6.6949 | -58.7485 | 2026-09-02 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 44c7dc87-818f-3955-9951-50eeae34edaf | -7.2255 | -42.7616 | 2026-09-02 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 82f49626-1fac-3726-89f2-86f3dc21afb4 | -12.1132 | -47.0661 | 2026-09-02 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| f2f5fce3-409e-350f-a59d-64a023847433 | -10.9562 | -50.4884 | 2026-09-02 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| aa4ed543-5acf-307f-be66-0cf249cec3f7 | -5.5832 | -60.2116 | 2026-09-02 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 874f783c-e881-38ea-baa2-93021ac24711 | -10.5788 | -47.7306 | 2026-09-02 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5c7cffb4-df97-3b79-91fc-f6f2c0199667 | -11.8435 | -46.0649 | 2026-09-02 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 1019dca4-fa92-3abe-9a50-285520c2e4ea | -10.4145 | -49.9898 | 2026-09-02 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 8626dfa7-2b06-3244-af1e-d61484459213 | -6.6764 | -58.7686 | 2026-09-02 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 93e617d9-5b31-35bb-b73e-154643c0caad | -13.0708 | -45.1429 | 2026-09-02 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| dac5914d-e5bb-3415-8786-c02c46083a30 | -7.3486 | -60.6074 | 2026-09-02 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 9576035e-e7b7-348e-86ee-2d3048c090a6 | -12.1128 | -47.0886 | 2026-09-02 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| f28f3607-2e0b-34d3-bf8c-c216878c651a | -11.3048 | -45.1575 | 2026-09-02 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| f6cd98c6-7481-3124-b9e5-94c4db48d925 | -12.3622 | -48.1681 | 2026-09-02 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| e8bb72c0-2839-3c3a-8397-d6e76f18baff | -6.1474 | -57.7605 | 2026-09-02 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 1da93112-4e9c-3d8c-9a32-6c96664db136 | -11.3044 | -45.1805 | 2026-09-02 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 39e99a05-c959-3bf3-a9af-513b22c6bc38 | -8.4671 | -54.7035 | 2026-09-02 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 610.7 |
| 0f988235-1781-3f61-9e6a-748bffcda059 | -8.4669 | -54.7237 | 2026-09-02 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 267.7 |
| 31263a3b-e790-3f30-8267-4efab2f52e45 | -11.3767 | -45.423 | 2026-09-02 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 358.5 |
| b5817399-7422-3927-b890-831f22eaf607 | -8.7613 | -62.5869 | 2026-09-02 13:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 95b1e95f-14c7-3bf8-8278-069452aca729 | -6.6542 | -59.426 | 2026-09-02 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| efd392df-d4cc-33d9-aba3-f8bfe41b5a18 | -8.7819 | -46.4399 | 2026-09-02 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| e81f39f9-9e05-3c9d-b00e-7561f6ee1397 | -10.9565 | -50.467 | 2026-09-02 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e56961a6-48aa-3d62-9c05-4adb170a44c8 | -11.3579 | -45.4027 | 2026-09-02 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 94bcd009-d1f2-3d92-9dd6-c8d04a0d4615 | -3.2455 | -47.9187 | 2026-09-02 13:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| fcd4574b-593d-3e98-bff6-489e396973de | -6.6765 | -58.7492 | 2026-09-02 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ae7c2c3a-84d9-341c-97c1-a41e12755be6 | -10.3196 | -50.0211 | 2026-09-02 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 6e5fee44-949b-35b7-8d76-b70ab5dc1deb | -11.3239 | -45.1548 | 2026-09-02 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 5500476a-4486-36ad-a51a-f8c7e7f503da | -12.1324 | -47.0635 | 2026-09-02 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ac42fa5e-e82d-3f2d-aabe-5190011bf2fb | -8.48 | -54.7 | 2026-09-02 13:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README72.md)
