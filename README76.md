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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7ed1ae8-6c84-3acd-875a-aed7907cabcc | -3.00805 | -54.18163 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a290ab54-c7b5-35d7-817a-727d63e956df | -3.04392 | -54.40636 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af1efc2a-3931-3563-b464-70f52edc81ea | -3.03542 | -51.33113 | 2026-09-23 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c4b5d1b-1442-3a5e-b904-a5f3fe82c683 | -3.03875 | -51.33165 | 2026-09-23 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6504abe8-8944-3e39-9b91-dc2a24299348 | -2.76682 | -57.03094 | 2026-09-23 05:01:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f600f7c5-7007-36eb-a489-9c53eb918bfc | -1.32737 | -54.66424 | 2026-09-23 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef0a4860-cd75-3b1f-84f9-0e2eaef3e46f | -3.37716 | -50.40714 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eed19d90-06c1-34c3-bf67-1ec8dcf97888 | 4.3051 | -59.94295 | 2026-09-23 05:01:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3301991-eaa9-301d-bf42-0a69c974a11e | -2.62462 | -59.37944 | 2026-09-23 05:01:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 98718fdd-0e2e-39cf-81dd-37bcd261aec5 | -2.97427 | -50.39339 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 732f201f-30f9-3019-98c6-25f5a5b518eb | -2.91316 | -54.18695 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f65519b2-a766-34cf-a900-26c6aa0dcc51 | 1.26605 | -50.84281 | 2026-09-23 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d38aed64-ddd4-33ff-98b1-7c7ddb50c06d | -3.44927 | -50.6131 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d2ffa9f-006c-3150-bae5-2b222e0b2879 | -2.9516 | -57.72433 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cb9f173-b918-338c-837c-e5d15187379c | -4.01343 | -48.95887 | 2026-09-23 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6cabee7-5c03-36f8-b119-16dfd775783f | -3.23091 | -46.94114 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d467d56-0aea-392f-9593-d40a5e00bd4f | 1.26937 | -50.84229 | 2026-09-23 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2221433b-b592-30a6-982d-fb9350e5e0e1 | -3.15074 | -48.0733 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e61cf30-4724-33fa-a6bd-7ee053002ae6 | 1.73472 | -50.89626 | 2026-09-23 05:01:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48fda928-27f0-3f64-bd38-e3a97e292b82 | -2.62222 | -59.37632 | 2026-09-23 05:01:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b955e3b8-4d1d-326b-8ac6-684ff9a8eb11 | -3.22593 | -53.95041 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb429387-120c-33d4-b683-53ec3fa96a34 | -3.22687 | -46.94058 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 99594a5b-ad0f-3b51-9e62-8996cdef31b4 | -3.72388 | -49.04423 | 2026-09-23 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9588d948-8a80-369d-9eb1-072bdab2734e | -3.04249 | -50.27014 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86527fe7-2e5c-38a4-b9c0-38f7e1d9b455 | -3.81981 | -52.39767 | 2026-09-23 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61f328d8-c686-3144-8e0d-c7f5fc8bb6b1 | -3.06759 | -54.3941 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dedea24e-7f79-3ad2-bf2f-d4e943de8715 | 2.06714 | -50.96393 | 2026-09-23 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9b983eae-ffc4-3b9e-9781-6ef6250281b5 | -3.06307 | -51.24287 | 2026-09-23 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38cb1e46-29dd-3e34-86e9-4c116d2ef82d | -1.82761 | -55.71402 | 2026-09-23 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd27757a-992c-30c7-9bff-9c44356e00ee | -2.88315 | -54.08366 | 2026-09-23 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b8d6cbf-58a7-365e-b13a-b9d1541b5140 | -3.85131 | -52.30677 | 2026-09-23 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e948a040-2a67-360c-bbdf-d2c968eeba04 | 2.32991 | -50.76683 | 2026-09-23 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 582dc73d-def7-3c26-a4fa-6e3f151110e8 | -2.97652 | -50.40111 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3073d0c1-be4a-3f0e-9499-692328eac705 | -3.04166 | -54.39792 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0137e143-6078-3a07-84b5-ae04b090a6a6 | -3.0647 | -54.38963 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 113a17e4-cca9-3d17-8d45-104dbbda7368 | -2.93667 | -57.78835 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 59b4eb80-4a4f-3503-b4c0-2ef127e629ad | -2.97031 | -50.39646 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec22264a-bc5b-3dda-892d-6c4f9cf0e9d5 | 1.44353 | -50.81095 | 2026-09-23 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72eb161e-504c-3697-b0aa-b2d10400f4ce | -3.28674 | -53.26454 | 2026-09-23 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47ca258a-2c7d-3903-ba19-d1b0642f06d1 | -1.40164 | -49.05157 | 2026-09-23 05:01:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cdd400c7-3b25-3fcd-b953-9191201f06b6 | -3.24454 | -47.25134 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77ad638f-580a-32bd-8cfb-4aaed7318b84 | -3.58666 | -50.02956 | 2026-09-23 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2530a8f6-b92a-3a8c-9270-2187ee6ec999 | -2.8687 | -57.79013 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70c31e87-6464-308b-a6ae-8319b6ea566e | -2.95118 | -54.08272 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a7b2057-90fa-3794-8e26-2c84e41f2204 | -2.16815 | -48.31902 | 2026-09-23 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a8871390-2d2a-3136-b4fd-4ff9889a6518 | -2.96381 | -52.14169 | 2026-09-23 05:01:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ced8a22-e88e-3d05-85a1-5ca321cab8f8 | -2.65447 | -59.68302 | 2026-09-23 05:01:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c264524f-9630-3dc7-b1e8-77d42c688ac3 | -4.45927 | -47.92406 | 2026-09-23 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| cee72c4a-4f0b-3966-9b00-79b7172d39b4 | -3.23284 | -53.95152 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93927b1c-a151-345f-8533-04b5f19aaa81 | -3.38056 | -50.40767 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd4bc73d-9dda-3b22-8a9a-49cc0ec071f8 | -3.39299 | -50.43914 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66fc3a51-517e-363c-9b3f-5947a4dcbedb | -2.54992 | -49.10413 | 2026-09-23 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4194a01c-f218-3a59-9b51-849f2675e688 | -2.63099 | -51.70314 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21107f4c-8f3f-3cb0-92b5-1e6441464cc3 | -3.77295 | -49.76825 | 2026-09-23 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27e7a153-5aa7-35cf-aa3c-5f99a49a4753 | -2.73596 | -49.46161 | 2026-09-23 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3c7341f-d60f-375c-92c0-0edc50bb7bc7 | 1.43853 | -50.82233 | 2026-09-23 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2058432-69fe-31ac-ac69-2dd545c3f357 | -3.25419 | -53.95103 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7895c04-abdd-36df-a04b-393ffe455331 | -2.86843 | -49.62651 | 2026-09-23 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eeef566e-cebc-3b87-af7d-c8767ea3e920 | -2.5058 | -47.04129 | 2026-09-23 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b75462a8-0b41-3243-9366-7f394c87687d | -3.6647 | -53.45696 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7601a162-440f-369e-8194-80bc09983341 | -3.51824 | -51.63408 | 2026-09-23 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64993b9a-55b7-3072-bb7b-6b9d2bc42126 | -2.95188 | -54.08614 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3825966-1420-32a8-aa0f-f7f76fb93bcb | -3.88956 | -51.95847 | 2026-09-23 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64eb88b0-272b-36e3-a560-9afb259fce39 | -2.88725 | -54.08039 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc29ba86-c304-3dc8-a922-8cd3ee4c3c28 | -2.99006 | -50.51667 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dab25b4-0509-3542-a09a-f13464b7a71b | -2.3215 | -49.20728 | 2026-09-23 05:01:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5102082-ab69-309a-bd99-8e2a63cf2f51 | -4.28284 | -48.61003 | 2026-09-23 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c9e4b70-3f2f-3152-8784-f0710cc54a7e | -3.22282 | -46.94005 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 13c3d81a-a2de-3448-8321-21cabcc3749f | -3.43409 | -50.66564 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25b19bed-983f-3c78-b649-36a81ccf04a0 | -2.94964 | -54.07796 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2823fb5-f296-351a-959c-424ac808c68c | -0.73327 | -48.536 | 2026-09-23 05:01:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39df778a-1e4b-3283-a47b-2343a60c7a89 | -2.95536 | -54.08669 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f84bd9ef-c49e-331f-9e10-696cb6ae39d6 | -1.94498 | -56.59302 | 2026-09-23 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e58fea0-c77d-35e1-85c8-9779cf486d16 | -2.89 | -57.28597 | 2026-09-23 05:01:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7ab6582-dc99-3cca-88ac-c7a35d81e472 | 2.33378 | -50.76976 | 2026-09-23 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 985f4858-cd01-3bd2-a163-f92885edb7d3 | -3.58607 | -50.03328 | 2026-09-23 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b61d1dc7-3170-388d-be60-161bb6e444b2 | -2.62705 | -59.37716 | 2026-09-23 05:01:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 483dbf80-934b-3954-a8cd-0b561b51c2ff | -4.45998 | -47.91929 | 2026-09-23 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5f96d765-1f90-30df-96b4-2dc15ea9dd92 | -3.95002 | -47.62053 | 2026-09-23 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65da3859-8f1d-3059-aa0d-674759f666ea | 2.06381 | -50.96445 | 2026-09-23 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6718fd18-c3e1-3203-9b3c-ee3aad246962 | -3.22129 | -53.95721 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 428fe04b-1650-3a15-b750-0ee6d17e445a | 0.7864 | -59.20329 | 2026-09-23 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bb25d8e-d661-3f9f-a33e-1cb2c47a87e8 | -2.7404 | -51.54698 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1c86159-811d-3044-b737-41875f85f143 | -2.86006 | -57.78872 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4e271b12-cf04-38b0-ac96-246c8f56b6f4 | -2.66347 | -48.33881 | 2026-09-23 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b3a3116-5159-3e90-bf4b-205fec94a121 | -2.9525 | -54.08232 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73dcd2dd-d752-389b-8e13-54f7e2516d2f | -3.06572 | -54.40577 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93f0fd28-9eeb-3017-aff3-df84da9b00a6 | 2.77555 | -60.228 | 2026-09-23 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c441102b-9e4a-3b9a-8a99-c4acd0a6efab | -3.36469 | -50.4644 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e1d9b4b-75e9-3e13-a718-320c992ee0ee | 2.34097 | -50.77216 | 2026-09-23 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c95bcde-21f9-3285-9453-76f1d12731c2 | -2.62137 | -59.38158 | 2026-09-23 05:01:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7431a37-0e76-3dd1-8f6d-a7eb2a9b7d3a | -2.96975 | -50.40006 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d631ccf-8875-39ba-ac86-2ff2083b5703 | -3.14733 | -48.07065 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9878cada-2e3f-3ab7-8ca3-8c5738425ca0 | -2.9484 | -54.08559 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c331085-0279-3721-bec0-886a72e30e4a | 1.43576 | -50.8263 | 2026-09-23 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4810b27-22c6-3462-9e58-96283f7cc592 | -3.06634 | -54.40189 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 235aa6c3-9ece-3ffa-9d21-0096797e6658 | -1.21789 | -54.55534 | 2026-09-23 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fab3d371-72df-3900-827d-1ba01c9cc1f2 | -3.80426 | -52.36678 | 2026-09-23 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c681a8e-6ca9-3b96-a159-86fb7e407004 | -2.97709 | -50.3975 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 63ecd9b7-e37f-30f7-87e9-1ff5f662dd0c | 0.18106 | -60.49076 | 2026-09-23 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README77.md)
