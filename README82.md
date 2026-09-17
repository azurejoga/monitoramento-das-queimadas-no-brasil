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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90b1cced-2ff2-33a2-86d0-c994abd010fc | -12.34 | -50.8 | 2026-09-17 08:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a15867a7-2290-3df8-857a-cf23f7f1aa53 | -9.112 | -45.7294 | 2026-09-17 08:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| f47acfd6-5a3e-31a9-8890-a2e2f6464685 | -9.8694 | -48.3814 | 2026-09-17 08:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| b3a93d9e-c819-388a-a433-13bc59b690f1 | -9.8697 | -48.3595 | 2026-09-17 08:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 3227f2ee-ebed-3979-a452-95988fac0e0a | -11.3161 | -46.7699 | 2026-09-17 08:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9a5f3649-a842-383d-84c4-bb3d8a96b1aa | -9.8697 | -48.3595 | 2026-09-17 08:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 73c39b74-3fc7-3ce4-a011-e1e58f052b45 | -9.8694 | -48.3814 | 2026-09-17 08:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c92632b8-f67a-3a8e-9ba4-de4f998ba91b | -12.5118 | -50.7164 | 2026-09-17 08:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 43df3fea-52e3-3543-8010-1685cafd9382 | -12.5121 | -50.6949 | 2026-09-17 08:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| f7e0e497-efd7-3240-b6f2-68e078d12f7f | -12.34 | -50.8 | 2026-09-17 09:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e8fa199-6d06-3d75-97ba-a59f056f5442 | -12.34 | -50.86 | 2026-09-17 09:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4186506-4abb-387f-b16b-2fc05395835a | -12.3384 | -50.8228 | 2026-09-17 09:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 29aeec3e-7b5d-32e3-b6fb-9a0c68420132 | -12.3568 | -50.8634 | 2026-09-17 09:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| eb7f0c19-d70d-3f9f-8e15-f9578168dbf6 | -12.3387 | -50.8014 | 2026-09-17 09:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 155ed8d4-94e5-3160-abfb-e4f41be7fbe4 | -12.3568 | -50.8634 | 2026-09-17 09:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 24f0c278-e029-3483-9b5d-5214406d94ae | -12.3377 | -50.8656 | 2026-09-17 09:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 556b13bc-39cd-35ac-8616-0573912c8974 | -7.0164 | -44.6413 | 2026-09-17 09:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 3f6e7621-194d-30ea-bd97-d965bdbb1251 | -12.5118 | -50.7164 | 2026-09-17 10:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 132.8 |
| caa4a32b-3698-3400-947c-d3955f433ac5 | -7.0161 | -44.6642 | 2026-09-17 10:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 32ef2343-9f57-3d07-896f-67238a0eeab0 | -7.0164 | -44.6413 | 2026-09-17 10:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 01d5a8d6-9cc3-387e-972a-197b8a6614ee | -12.3377 | -50.8656 | 2026-09-17 10:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 594bbfc8-1c39-3c63-8418-e182d0c0ecbc | -12.3568 | -50.8634 | 2026-09-17 10:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| a4d1b9cb-ed34-395e-8aff-64f6f88f4b93 | -12.5118 | -50.7164 | 2026-09-17 10:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 271f356f-e8e4-340d-96aa-02cd68eba69f | -7.0161 | -44.6642 | 2026-09-17 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 107c88a8-dd8b-3383-9e78-380d1d13d30f | -12.3568 | -50.8634 | 2026-09-17 10:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 152de819-cdf3-3f99-af45-8008f74afc28 | -7.0164 | -44.6413 | 2026-09-17 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 0d3ed3bc-af59-3709-83a2-0f9b3ac1d2de | -12.3377 | -50.8656 | 2026-09-17 10:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| be573da3-4a85-3c87-a2b9-6399062e6fd2 | -7.0164 | -44.6413 | 2026-09-17 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| b249f2c5-c940-33a7-a105-ac21c7e5c48e | -7.0161 | -44.6642 | 2026-09-17 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| f54b043d-d7dc-3246-a9f6-9ca793615506 | -10.8308 | -46.1569 | 2026-09-17 10:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 8f930904-2a74-395c-8914-b5ec2fbb3585 | -10.8305 | -46.1796 | 2026-09-17 10:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 213ba818-2d7f-306e-b141-e01ce048e3b3 | -12.5118 | -50.7164 | 2026-09-17 10:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| c59c99e8-502e-3566-9c30-28092f3a555e | -10.8305 | -46.1796 | 2026-09-17 10:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| ed42fb36-06d5-34c8-b8d4-7f6a7bc0cdb5 | -10.8308 | -46.1569 | 2026-09-17 10:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| c84667aa-f717-3dcc-bf8e-3ad7fdce45a4 | -12.4151 | -50.7923 | 2026-09-17 10:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 6649dfdd-bf3d-334c-aba7-5b38009a3103 | -7.0164 | -44.6413 | 2026-09-17 10:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 456c84dd-0032-3ba9-a8f6-ced3be468ab0 | -12.3568 | -50.8634 | 2026-09-17 10:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 96804f2d-a57d-3cd6-aff1-965ef0f861d3 | -7.0161 | -44.6642 | 2026-09-17 10:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 88d8ece8-9380-304f-b203-539875a60f66 | -10.8308 | -46.1569 | 2026-09-17 10:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 305deb34-85f7-3df7-85e3-f41e1e8c893a | -7.0161 | -44.6642 | 2026-09-17 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 07682c7d-9bea-3dd2-b2f5-ed957dc5157f | -12.5118 | -50.7164 | 2026-09-17 10:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| a3f3e577-91de-31b9-bd47-0959adf09708 | -10.8305 | -46.1796 | 2026-09-17 10:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 1e50fdc3-0b49-3a90-917b-0f76345c18de | -12.4343 | -50.79 | 2026-09-17 10:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 5b3e7529-88db-3e5b-878e-02dc0da8728f | -11.875 | -47.5902 | 2026-09-17 10:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 61d3ce6f-d763-3287-a41c-1bb7eaa8e7f6 | -10.8118 | -46.1594 | 2026-09-17 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 75591350-b402-3cf0-b83c-7880e1c215bb | -12.5118 | -50.7164 | 2026-09-17 10:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 961cc161-d8e0-3ad8-80e2-c4bed3045eff | -10.8305 | -46.1796 | 2026-09-17 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| b0306984-11d7-3d6b-9bc5-8bebd201ba36 | -7.0161 | -44.6642 | 2026-09-17 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 8e5b07eb-f382-3182-b241-c49f2d6e6a8d | -11.8941 | -47.5876 | 2026-09-17 10:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 7e7fa3e2-c8bc-326e-9b28-c61af4be3acd | -10.8308 | -46.1569 | 2026-09-17 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.4 |
| a633fad5-7b28-3671-80e0-5f2776aa57d8 | -12.4926 | -50.7187 | 2026-09-17 10:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 2c354898-e363-3122-afce-50fe25ac6cbf | -12.4151 | -50.7923 | 2026-09-17 10:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 161.8 |
| fced915a-5402-371a-8551-bafd41fcad49 | -7.0804 | -47.5031 | 2026-09-17 10:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| e656c680-ba26-338d-afd4-8e4a7b92b5f4 | -12.4343 | -50.79 | 2026-09-17 11:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| cebc31ff-4f27-376f-addf-bb904a16a00f | -10.8308 | -46.1569 | 2026-09-17 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.4 |
| c00f5438-52a5-35f0-bb7a-0921ebc756a8 | -12.5118 | -50.7164 | 2026-09-17 11:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 1591e4c3-1ae8-3c51-9511-0024610f725e | -10.8305 | -46.1796 | 2026-09-17 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.2 |
| aa0cf42a-b3f9-33dc-b90c-58593a8d9ef2 | -11.875 | -47.5902 | 2026-09-17 11:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 62ae6a85-3281-37a5-9131-e47f61d820f3 | -12.4343 | -50.79 | 2026-09-17 11:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 8e5343ca-d3f8-36b2-8b6e-4ad8b144ad0c | -12.4151 | -50.7923 | 2026-09-17 11:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 350aad78-5ece-34b5-9fd1-49ac4a8fc0e8 | -10.8308 | -46.1569 | 2026-09-17 11:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 3015eaef-e2ca-35b7-874f-963b448d62b0 | -10.8305 | -46.1796 | 2026-09-17 11:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| bb0ee1e5-864f-36c3-a6ac-748bd400dea6 | -12.5118 | -50.7164 | 2026-09-17 11:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 161.0 |
| cfa5cabc-67b6-378a-a984-9fd96a90d92b | -11.8941 | -47.5876 | 2026-09-17 11:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5fb8687d-86d2-3722-ac04-c9f572d91c86 | -7.0161 | -44.6642 | 2026-09-17 11:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| e26f6dc4-6356-3b6b-8a09-e971066f9352 | -7.0161 | -44.6642 | 2026-09-17 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| b4e194e1-48a4-3390-a6cd-4c5d014cd7fe | -8.5239 | -44.5153 | 2026-09-17 11:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e92f80c4-8aa7-34b9-9446-f6ccdf83c928 | -10.8308 | -46.1569 | 2026-09-17 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 239.3 |
| eba9491d-c4c4-3c42-8095-af688a6e2d6c | -9.8319 | -48.3636 | 2026-09-17 11:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| f9cb4b49-fe9a-3bcf-883e-3b1dffa60de3 | -12.5118 | -50.7164 | 2026-09-17 11:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| cf2ff5c8-a578-367c-a9b8-b58665f8a26b | -10.8305 | -46.1796 | 2026-09-17 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| f8abc280-7bc2-39e5-bdd7-99aa92888862 | -7.6402 | -44.3303 | 2026-09-17 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 9a752971-cb30-3f95-8ab9-f35db242ce91 | -12.4151 | -50.7923 | 2026-09-17 11:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 1cfa33b6-8d5b-3426-890c-f19c20f7f376 | -7.6591 | -44.3284 | 2026-09-17 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| ef81c131-f293-3f24-93e1-2c1bd4ddfb70 | -7.0164 | -44.6413 | 2026-09-17 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d216febf-8bf2-3104-801d-4954627df393 | -12.4343 | -50.79 | 2026-09-17 11:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b11623fc-b323-3697-b9d8-346084dc8637 | -12.5118 | -50.7164 | 2026-09-17 11:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 146.7 |
| f61e96d1-a566-3773-b5e7-78729de518c4 | -9.8319 | -48.3636 | 2026-09-17 11:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 321.2 |
| 83f45741-1d5c-3603-8fcb-6a698c81a816 | -9.8322 | -48.3417 | 2026-09-17 11:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 233.3 |
| 9bb1fa87-9ee0-3944-92df-1a49c8f4e822 | -12.5121 | -50.6949 | 2026-09-17 11:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 114c96b0-afb8-3d86-a487-5fae0d842205 | -8.5239 | -44.5153 | 2026-09-17 11:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 1b682160-5153-3ccb-81a8-ea280b1e152b | -10.8495 | -46.1771 | 2026-09-17 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| c99c2728-90c0-3b52-bc09-de5893ad1609 | -10.8499 | -46.1544 | 2026-09-17 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 92c8c0fd-7391-357a-93d1-c84804bc8fb1 | -11.8941 | -47.5876 | 2026-09-17 11:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8949420c-cb9a-3666-be5a-d8a2c077ba4b | -7.0164 | -44.6413 | 2026-09-17 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 06e26204-6380-3697-8d88-70a05e033636 | -10.8308 | -46.1569 | 2026-09-17 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 261.0 |
| 52ca313f-4b8b-344b-addf-2a724540a7df | -10.8305 | -46.1796 | 2026-09-17 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 5d07a985-c7a5-3424-8101-291fc78d00a6 | -11.8937 | -47.6099 | 2026-09-17 11:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 218733f6-c891-34f3-8050-c81fac199942 | -12.493 | -50.6972 | 2026-09-17 11:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 2144bf14-bad0-38e5-a124-b6042f833adf | -9.8694 | -48.3814 | 2026-09-17 11:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ec34aa36-2f42-36a6-8706-0e96cd8c4e54 | -9.8697 | -48.3595 | 2026-09-17 11:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 16f52545-e895-3c00-b99f-275befde6a28 | -10.8118 | -46.1594 | 2026-09-17 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 537379c9-043a-3291-a420-f92ddc2045af | -7.0161 | -44.6642 | 2026-09-17 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 150.0 |
| c8f698c0-9c4f-36f3-83f5-f92f8efea3f0 | -9.8319 | -48.3636 | 2026-09-17 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 17a85d53-e4a8-31f2-93f4-f6fa417c243f | -10.8308 | -46.1569 | 2026-09-17 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 11d49c43-0e27-315b-9cc3-351ff918f44b | -7.0804 | -47.5031 | 2026-09-17 11:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| cf3c7e4f-d09c-3a68-ad20-69a17c7f35b0 | -9.8697 | -48.3595 | 2026-09-17 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| d04ad627-1e9e-3152-a56e-2e09b6981482 | -12.5121 | -50.6949 | 2026-09-17 11:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 958fd3d3-c903-3031-b5fb-96afa38c32ef | -9.9143 | -46.5172 | 2026-09-17 11:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1593e6c8-e5b3-3e75-844c-bde650afcf56 | -9.8322 | -48.3417 | 2026-09-17 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |


[Clique aqui para ver as próximas entradas](README83.md)
