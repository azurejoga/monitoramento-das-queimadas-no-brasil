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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4eda7e71-92ae-32fe-a275-ac9f8ccb66d4 | -10.29528 | -58.99656 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ba041e9-3682-3f8a-962a-762fab1cb528 | -10.29239 | -58.99212 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7539a4e0-11b3-3270-88ac-7846cd4912f8 | -10.22319 | -59.40271 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a261da1-19d8-3cfa-a478-7cabff884b44 | -10.21975 | -59.4022 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f556665-3e24-38bd-8a52-3df0c40cf782 | -10.04673 | -59.45968 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddf0859c-0e91-366c-8cbe-0b3d996bdffc | -10.0434 | -58.99893 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c2c7bb1-7087-369d-9d19-c39f6ff09b7c | -9.99387 | -59.53579 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e934d52a-a0b6-3964-9f52-8aa26b83408b | -9.9933 | -59.53948 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c06a400c-ffd8-34af-afa8-bf975b9d0eee | -9.99045 | -59.53528 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df48f36b-4dc8-3850-a787-bc295d504f07 | -9.98989 | -59.53899 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 916a10a1-b049-350d-8a08-0634ed737b49 | -9.95972 | -59.53074 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ceb94ad-96c3-3428-8a39-e37bbfa34d6f | -9.88972 | -59.50872 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2ea29ec-81fc-37f7-92ef-d1ba4ee6911e | -9.88631 | -59.50819 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d8cd438-1875-3b8e-93bc-61e1209365ea | -10.72418 | -58.5139 | 2024-10-12 05:25:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bcf2448-c6ea-3dbb-a944-9612ff90a1d4 | -10.7206 | -58.51336 | 2024-10-12 05:25:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf04bfed-29ef-380c-a52f-72c528900716 | -10.65587 | -58.40674 | 2024-10-12 05:25:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.1 |
| a408e861-ff19-3001-ab41-b1f86cadf0f3 | -10.65289 | -58.40204 | 2024-10-12 05:25:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4c59550-726b-399d-a7f6-2ac2e1932bc2 | -10.65228 | -58.40619 | 2024-10-12 05:25:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 22763da5-729b-3235-875b-73f38f007382 | -10.6493 | -58.40149 | 2024-10-12 05:25:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 238e654e-ff27-3bb1-b405-76431c7ff5a3 | -11.72132 | -59.28298 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de5c6da2-6e81-34da-92a1-5fabd2034de8 | -11.72075 | -59.28688 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2b84747-0e39-3ebd-9d29-fb9d711bbecc | -11.72017 | -59.29076 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e007d944-2b6f-39c4-965e-20845f9f3a80 | -11.7196 | -59.29464 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1684c2dd-e7a5-3562-8961-ea42958fadc4 | -11.71899 | -59.27462 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa11e877-f5b7-3ba1-9644-7dbe5c5296f3 | -11.71841 | -59.27853 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c607fbb8-50ea-3964-9271-c78fcac9d507 | -11.71784 | -59.28244 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fca9c414-3d7d-36cc-bb8e-47ced7b1f4c7 | -11.71726 | -59.28633 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38f8f337-0eea-3d95-9483-9dcf3c6651c5 | -11.71668 | -59.29022 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03d226b3-6aae-3489-8b34-b04843ba89ea | -11.71493 | -59.27798 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bec519ff-1c31-3d6e-857b-1423498004df | -11.71435 | -59.28189 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40942e1c-dce0-327b-99d8-5ceca741a63b | -11.66624 | -58.89802 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e55b9dd-7331-3413-9a0c-52cab7884c44 | -11.46649 | -58.98518 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e81d879-a956-34ac-814c-fa954955d72f | -11.38479 | -59.19822 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9b5e635-fc4d-3fb3-a3b6-81a84290df62 | -11.3813 | -59.19772 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 404586ea-6f98-3ae4-b413-455f998fb7fb | -11.38058 | -59.19804 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a280b842-959a-3f26-840c-00111b7f2caa | -11.3778 | -59.19718 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0474fed9-a4bc-3582-8405-32c384f5d114 | -11.3771 | -59.19748 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb6d90c1-4574-3949-8696-ae172cd4a7ed | -11.34459 | -58.98361 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6d5d1da-f0e0-3894-90d9-68e16e30b274 | -11.34284 | -58.99548 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eee20629-108f-39b4-bf12-481534f29c18 | -11.34107 | -58.98306 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 413fa572-2699-3504-a4ab-9a2eceeba714 | -11.33581 | -58.9943 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e4d897c-ed7f-34d1-80d6-d01cdf373550 | -11.27117 | -59.54689 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f71dfc22-acf8-395b-b186-26ec3b091aa8 | -11.17939 | -59.2953 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0f2721b-4eea-3978-bbdf-1e7323c7d094 | -11.04014 | -58.97272 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f48b9d04-5817-3f6e-a417-1cf08addb276 | -11.03956 | -58.97665 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06595ed6-05b5-3a45-9274-0d1ae613da6f | -10.99573 | -59.00607 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06f8ed12-d5c9-3aad-91c2-36cac9678d74 | -10.99515 | -59.00999 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3582d7a-eeed-334c-95b7-22e981ef75ec | -10.99457 | -59.01393 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0de5e890-33ed-3d97-999b-8f21ce434894 | -11.76863 | -59.94451 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b987e749-f927-3e43-b4ed-0cd120447abd | -11.76806 | -59.94823 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e1e8ed2-e5bb-3e5b-8dc7-11f96a66db5e | -11.7675 | -59.95194 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc348794-4728-34ff-bb02-ebd6e50fec71 | -11.76693 | -59.95565 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96f33a34-64cd-3057-a492-68c38c83a593 | -11.76353 | -59.95511 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 181d7b5d-fcee-31dd-a93c-814bc2e021ee | -11.76296 | -59.95882 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 091e1c37-0285-347b-aded-6a4114731f58 | -11.75899 | -59.962 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79458c12-5cf5-3b40-b993-25880b234df1 | -11.69511 | -59.90272 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e219e9c-c3fe-3b51-b514-e3d0810e3c42 | -11.67236 | -59.8915 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 636d50da-c612-378a-80e9-423d0a389346 | -11.66895 | -59.89097 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b6b45f2-438a-3183-89ab-ff8d21732cf5 | -11.66838 | -59.89471 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e33f423c-a4a6-3ed5-b4da-3e8ba77f8de8 | -11.66611 | -59.90965 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44a5bf36-6eff-3dd8-b7a7-9e0a1ceef798 | -11.66555 | -59.91337 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d072cad8-1a41-3aa7-8766-1d796de93dd5 | -11.66498 | -59.91709 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50e7f32f-a456-3f7a-a143-1dda4f402cde | -11.66497 | -59.89418 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6974ed11-3c26-37b1-a05b-37c706c83938 | -11.6644 | -59.89791 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96c0d703-86fc-3f01-a26f-32d1c31a8578 | -11.66384 | -59.90165 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3571025a-a6ca-37e6-86d3-a09398a5f12e | -11.66099 | -59.89737 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfe4c3e7-7c1c-348f-a491-13181af4a36a | -11.66043 | -59.9011 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e05854c0-ea1a-3670-82f0-6cedfe73cf81 | -11.58453 | -59.98808 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63a8a318-23a1-30c5-a6d5-bdb3b40863d9 | -11.58409 | -59.98851 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 353f6268-8552-3b89-a3af-69ceab176a58 | -11.58398 | -59.99178 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb9ae021-3348-3f2f-9375-5612c2050257 | -11.58353 | -59.9922 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c2f2275-1fff-38de-9c2a-13727e3647c9 | -11.58184 | -59.98051 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cf96b17-5d68-38b4-893c-d80de231a2c4 | -11.58126 | -59.98426 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0f4e66d-84c8-3b74-864e-f922a67ffd5e | -11.58069 | -59.98799 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 382bd644-f796-393f-8f6a-c97dbafbe377 | -11.58013 | -59.99167 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6539c285-3dc0-38f5-8913-eee84a4e5a4d | -11.57957 | -59.99533 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bfdb2af-52f5-3c1d-8200-3bc6eaa95033 | -11.57786 | -59.98373 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb92e9aa-8fff-3b98-998c-f15aa8cae565 | -11.57503 | -59.97944 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13e92917-c54c-3d99-82ee-09484151fb99 | -11.57446 | -59.98318 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52ccb460-302c-3133-92af-90703b673428 | -11.57163 | -59.9789 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d31d909a-86bf-30c7-b740-136206eb1431 | -11.57106 | -59.98262 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e03a0866-5e31-3c5e-bfba-cb0562da8824 | -11.56993 | -59.99004 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b471d1e3-d085-3264-8b63-500b759ecb71 | -11.56937 | -59.99372 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e9396f5-adad-3e80-b201-61c4ed68a733 | -11.56653 | -59.98949 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e119f2fa-cd57-34f6-a773-20debe9b524a | -12.33247 | -59.1617 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7052987-8148-377c-9af5-05f428d79b2c | -12.33188 | -59.1657 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80104df2-3231-3630-8129-92ef23ae6f4b | -12.31181 | -59.25206 | 2024-10-12 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c9d7755-5c40-3a6e-ac0a-dd809b984913 | -12.29958 | -59.16463 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66ffad49-2792-3953-ab1a-4dc354df31ba | -12.29899 | -59.16863 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7deb36a1-0c88-3ea1-b1fe-b9e101773c92 | -12.27139 | -59.20932 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae7b7ca8-4527-3c34-95eb-998f89679bd8 | -12.27081 | -59.21332 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93b120aa-e017-3a9e-a1c6-57dd4a79bb3b | -12.27022 | -59.21733 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27c00f75-0eaf-3ba0-a75d-1cbf7988c320 | -12.2667 | -59.21677 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ac2f639-db83-38cb-b1fc-665a52322a2a | -12.24658 | -58.91763 | 2024-10-12 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 758174fd-9751-3043-be72-be2ca07acd6e | -12.15259 | -59.71328 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 014e13d6-d22f-3564-8433-0186cc304a91 | -12.15201 | -59.71709 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60333a5d-ced3-347a-b0da-c45a51caed32 | -12.14914 | -59.71276 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f4d9ce9-1578-3de4-83e2-da2e301091f9 | -12.14569 | -59.71225 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27291bf9-5b83-33ff-bd4e-da79aa5f807e | -12.14454 | -59.74313 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd75e331-2d83-340c-a607-ea7847ba47d1 | -12.14397 | -59.74692 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README126.md)
