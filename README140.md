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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d3831b6-b5cb-3328-9f44-abc3def080a7 | -12.46878 | -63.00365 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42a23d50-7aad-3c48-98c4-49d5fb950777 | -12.46821 | -63.00747 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2fc262ff-e881-3dc1-96ad-6204aa805aa5 | -12.46592 | -62.99931 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e958beb-6947-3d33-b563-31082a4674e8 | -12.46535 | -63.00312 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dea20060-d8f0-39c5-aa46-93b40c15cc94 | -12.46478 | -63.00693 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec97a395-a6f7-3ee2-881d-2965d162a3d4 | -12.46192 | -63.00259 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 29a9b6b8-e404-3661-995c-14a57c276701 | -12.46134 | -63.0064 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e69384fa-3552-3a9d-8046-2ca3c70e66d5 | -12.46077 | -63.01021 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 735f62ec-65ee-3751-b1ad-dbdbe6297a37 | -12.45848 | -63.00206 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 604b07c3-ad02-3451-9d5d-9962a5c19da3 | -12.45734 | -63.00968 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d99e9015-8552-3653-b005-f93f55e6e62c | -12.4133 | -63.02235 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ea0da48-f105-3fed-aee8-140ef0beacc7 | -12.40987 | -63.02183 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d262ba4d-d016-383d-90c3-afea3806f8a9 | -12.40414 | -63.01314 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aab5e11e-ac3d-3f87-8682-9a71aea051fe | -12.38574 | -62.97124 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b15e951c-1121-3007-9f62-92ea1a988f6e | -12.04891 | -64.72273 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66c29b4c-772e-3ca3-ad40-af12a8665fa8 | -12.0456 | -64.72221 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56926dc4-af70-36a7-9899-f4c5bb02443e | -11.89838 | -64.33411 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86553392-97dc-3e84-b225-83ce5f848fb9 | -11.89561 | -64.33005 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 314fbf65-a01b-3ba8-9d68-1068f5d3c8f5 | -11.89507 | -64.33358 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6b91b6b-0c06-335c-879c-442ef3ab22bf | -11.72655 | -64.14768 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01398c77-5b1c-3736-91ad-433a1930ac9f | -11.72078 | -64.03045 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32f7d62a-67b0-303e-b08a-a28cbc177e7e | -11.72046 | -64.1431 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfdfdec6-6725-3c2b-9c04-efd9b24702b9 | -11.7186 | -64.04462 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be8a981e-6231-34e9-bbe3-23c7be906bda | -11.69968 | -64.01256 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 120cff8e-e6a4-3682-81c5-8b5db0fd8192 | -11.69689 | -64.00849 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 89ec0833-33b9-3366-83f1-34026f942673 | -11.67091 | -64.24397 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee53d9d4-8ea2-391d-bd76-64062ed889d7 | -11.66843 | -64.01835 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ee8b806-ff43-32c1-8946-b8111f12e3b5 | -11.66706 | -64.24697 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d3cc224-f838-3180-8419-f16f83ac4790 | -11.66678 | -64.02906 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0e1fc11-cef3-371b-b238-017fc47c5311 | -11.65162 | -64.25896 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b22d007a-7911-3172-b7d8-10b54b2058aa | -11.65072 | -64.02277 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d89413c2-3982-39a2-9012-25c9b697df25 | -11.64831 | -64.25844 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adfcf72b-b388-3e7b-af55-fe6755818790 | -11.58356 | -64.19349 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c861808-d957-3942-a54a-306fd21e4c68 | -12.46955 | -64.0237 | 2024-10-10 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc9ed5bc-2d78-3fb7-9da5-5f960b69b87b | -12.46014 | -64.0406 | 2024-10-10 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf90b1cc-12bf-3c63-8e06-88ef9943032c | -11.94623 | -64.90038 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5ff47ad-cfa1-34c1-9d1f-75f709a94807 | -11.67777 | -65.17966 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41681903-b44f-3e2b-a686-89e6889068f0 | -11.675 | -65.2187 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a9a4fde-835c-37c5-98ed-ad1f225397bc | -11.67445 | -65.2222 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 561aad07-c5e9-30be-a743-be3bed619d86 | -11.53075 | -65.2062 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b83c41b-525a-3fd8-b36a-38b00efd0d25 | -11.52744 | -65.20566 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 904cae3f-ce98-318e-a5a3-33a789501b48 | -11.28891 | -64.90472 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e86fac3b-2349-3d35-a167-3eb7a57e3dac | -11.28616 | -64.90069 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b89f44df-d8bc-3e02-a8c7-c32fcf073c40 | -11.28561 | -64.90419 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07983355-a748-3308-9cfb-48e63fa05524 | -11.28506 | -64.90768 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ccbdd3b-cf6d-303d-983b-ab8c1779a100 | -11.28341 | -64.89667 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f7db4b4b-5532-3a86-892b-99ee188277b3 | -11.28286 | -64.90015 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8464d175-18c6-30bf-a607-076fdbe4886b | -11.28231 | -64.90366 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9603e6f6-8d25-3b70-86f8-ad4d6c6f3342 | -11.28176 | -64.90715 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24aa0398-a31d-361e-9ff0-abe30bc22d87 | -11.28121 | -64.91064 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 895fe9a0-8efc-306e-a9b7-9fb1983d5f07 | -11.28011 | -64.89613 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7f091f4e-bb01-3a64-81c4-07f51d64510f | -11.27956 | -64.89963 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a3676ad4-2e63-32c4-be27-e1bd592222c2 | -11.27901 | -64.90312 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 556afa5a-b625-37d0-a084-764f05ebc5fe | -11.27846 | -64.90662 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0413c6d6-6933-36ce-95e6-f0aacb1f5ed8 | -11.2168 | -64.82095 | 2024-10-10 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3259ca1b-96eb-3de3-b124-9cc04dfe45b8 | -3.01524 | -59.09859 | 2024-10-10 05:57:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc4faac1-560d-3cd7-b070-08772d0792da | -3.01466 | -59.10253 | 2024-10-10 05:57:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fbdab3d-8166-3e7d-9a55-34a75e8fbd28 | -3.01408 | -59.10641 | 2024-10-10 05:57:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05191340-1e4c-3ca4-be84-f9b41b92a78c | -3.0135 | -59.11023 | 2024-10-10 05:57:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5215ab69-f39d-371f-ba8f-1f680c0d55be | -3.00781 | -59.10933 | 2024-10-10 05:57:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 642f3834-6e15-3685-97dd-335961130676 | -3.96239 | -59.17582 | 2024-10-10 05:57:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9ed8191-82aa-3952-b0ad-42496e55ff44 | -3.63171 | -60.21005 | 2024-10-10 05:57:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60b4b208-dcf1-33a1-8498-b245e54a0916 | -3.63124 | -60.21338 | 2024-10-10 05:57:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6554aa8c-b238-36b4-979f-cb389c482716 | -3.6292 | -60.20998 | 2024-10-10 05:57:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da5fd49f-529b-3129-96fa-24232f6cfcf0 | -3.6287 | -60.2133 | 2024-10-10 05:57:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c667c19-4893-3021-96b9-83fa315244d4 | -3.04454 | -61.68131 | 2024-10-10 05:57:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8103355b-3166-3930-879f-d9cf3af0e655 | -3.04376 | -61.68647 | 2024-10-10 05:57:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5380e1d1-efac-3089-bc7e-a4df30fe1381 | -4.65955 | -56.10762 | 2024-10-10 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a19c9a73-dae3-3e57-9d2d-5d0d413e5f31 | -5.12663 | -56.00639 | 2024-10-10 05:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 013e7fec-29dc-3439-b636-1a84eb3a0997 | -5.12578 | -56.01256 | 2024-10-10 05:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83e14c7a-3497-3980-bdd8-391d0e0411c2 | -9.94827 | -58.11946 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2147c04-d1cb-3387-b65d-44999114cab8 | -9.94756 | -58.12525 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf08989e-fa3b-3af8-8a52-9ead6fe64544 | -9.9449 | -58.12486 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d027d97b-f07d-36cb-a0fc-0c07d196837d | -9.91532 | -57.47987 | 2024-10-10 05:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52fcfc03-a8cd-3f34-a1ec-a8731e992281 | -9.91449 | -57.47842 | 2024-10-10 05:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3d58e367-c62b-33d1-bc4f-27f24b8a14c3 | -9.91431 | -58.12063 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f57d7945-5159-3118-a2c8-3653af262632 | -9.9136 | -58.12645 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78d74012-3b80-3d86-8a83-06e37185ac3b | -9.90764 | -58.11986 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9307e039-61a8-3d20-b25f-13cca31f79e4 | -9.90693 | -58.12569 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 434b2fb6-38d5-31f0-9839-a8a98ea92696 | -9.90096 | -58.11917 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33da16b0-e47a-3021-87fd-86b6e6a5243a | -9.90026 | -58.12499 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bcf0853-a639-3c52-ad5b-a040d5aff5b9 | -9.89359 | -58.12426 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15c3c091-4ca2-3580-ab3f-19ece9ad3cdc | -9.8929 | -58.12999 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 28f12bbb-b678-355e-9ae9-c3243c5ecb8e | -10.22567 | -57.80737 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d11f05a1-d0bf-3428-b1a0-2722e15cb8f4 | -10.22493 | -57.81373 | 2024-10-10 05:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca1e5b62-8f66-3e73-bb5a-3e61ce67975e | -6.47538 | -58.43303 | 2024-10-10 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91b155bd-8741-33ba-8d4e-ed18a4adab51 | -6.47473 | -58.43787 | 2024-10-10 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e66be8b-b665-3104-b7c9-2e9b8bf266b3 | -6.81144 | -58.99031 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71a2c388-1954-3e47-a082-555740b1e84d | -6.52393 | -58.4044 | 2024-10-10 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6431e42f-256c-34a1-ba49-8125d52f35da | -6.51696 | -58.40864 | 2024-10-10 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35b9a963-7730-38d4-99a4-7f2fbfa28a31 | -6.48164 | -58.43385 | 2024-10-10 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ec035b6-44c3-338f-848c-34870beb267b | -9.18676 | -58.89173 | 2024-10-10 05:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5357451-b7a7-3def-8568-c965399daec4 | -9.18616 | -58.89645 | 2024-10-10 05:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e170f26-891c-3087-af62-984b17464768 | -9.17986 | -58.89572 | 2024-10-10 05:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2d10715-bca3-34f7-92f5-fc2c0bb2a815 | -8.1171 | -58.03539 | 2024-10-10 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54c66535-af85-341e-84bd-277254e92d99 | -8.11642 | -58.0407 | 2024-10-10 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0828bfaf-5217-326f-ae93-51ca806d64fc | -8.11575 | -58.04596 | 2024-10-10 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 55aad7a2-dbe4-337e-bf5e-a1825d76f982 | -8.11055 | -58.03456 | 2024-10-10 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6bf56209-f097-389b-91bc-c031f1d82e4d | -8.10989 | -58.03976 | 2024-10-10 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60f7fca6-f179-3b7d-8b8d-0e768d23da40 | -8.10923 | -58.04487 | 2024-10-10 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README141.md)
