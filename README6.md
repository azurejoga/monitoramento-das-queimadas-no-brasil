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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6e7b97f-2441-3e31-a321-8237e7849e4c | 2.17252 | -61.86076 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32b81242-00b9-3d4c-8541-71d819f729ff | 0.66936 | -59.59578 | 2025-01-16 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efe21fe1-8dc5-34ca-ae9b-a5a000d7b285 | 2.19763 | -61.80996 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bbd7d15e-4fcb-34de-b05f-310bda02ede9 | 2.10522 | -61.81924 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c9aa2dd-5e7c-32fb-9ac7-e7236c1d2cb3 | 2.09475 | -61.84645 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abbda5da-e575-3336-8bb3-b5d39007001a | 2.20257 | -61.81773 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0e09855-3592-3625-baca-c60978ab6670 | 2.11245 | -61.81814 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7a18cd5-2867-381b-b96f-eef87ca59772 | 2.18387 | -61.81643 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79a3d2f6-6bdd-3eb7-9e0a-effa84ee28a5 | 2.19829 | -61.81411 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 981522c9-cb8b-392e-a11e-18f4c550e28c | 2.09113 | -61.84699 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e7ace64-4da1-3f33-a99d-de737466491e | 2.16464 | -61.85774 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 997d069d-1a07-3dcf-97c2-f138b685ee52 | 1.17642 | -60.5 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3872427c-7862-3e21-b49f-29395b81fbc8 | 0.72636 | -60.11689 | 2025-01-16 05:44:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b8d15ef-398b-3824-8cac-f96d33c59eb1 | 3.82617 | -59.71572 | 2025-01-16 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6017f5eb-a6a2-3af4-8a18-c98b6a16b6d6 | 1.29035 | -60.43299 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 33150da4-1a43-3ab1-9f80-5204778ab0cf | 2.1154 | -61.8134 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59cea852-9daf-3420-9ab5-f39b094fdc0f | 0.72693 | -60.12052 | 2025-01-16 05:44:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 93c925fc-d7b0-3681-bc96-d3e9cb5b86fd | 3.92894 | -59.68131 | 2025-01-16 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02dd537e-57a2-35a9-b4c0-d197f6bf2f24 | 1.32177 | -60.03527 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d99c8f1c-855b-30d9-bbd2-174869e581f8 | 0.84746 | -59.54531 | 2025-01-16 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2eab6fb4-87bd-305f-ac1b-c2ea3b842424 | 1.12385 | -59.43261 | 2025-01-16 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8346da5c-644b-395b-ae2c-8802a44722c1 | 2.10949 | -61.82286 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f471deb6-cdc7-3e2f-af6b-3080fb657ceb | 0.92223 | -59.80001 | 2025-01-16 05:44:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8522d57-75b0-33e1-bd97-a305a898c6f0 | 1.17478 | -60.48994 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0805b98-5aee-3196-a872-df3a9127ac9b | 2.10883 | -61.81869 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43bce9b4-84a5-3eb2-aee3-8f92f632f7be | 1.17614 | -60.49165 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c2b85d6-e888-3da2-a297-7277c2405e4e | 2.10065 | -61.83706 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2f4edc9-c2ca-3965-aa6d-87c1c58d8097 | 1.17536 | -60.48661 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af7b017c-2231-3f59-9588-4211218b794d | 2.11377 | -61.82649 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 37c7a307-3e48-34b2-934e-258a237fc524 | 1.18268 | -60.48869 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 452de974-f2ce-3715-960d-bcc89b43227e | 1.17873 | -60.48931 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bb2f9c2-9131-39c4-9c47-dac0cad40a8f | 0.62195 | -60.6195 | 2025-01-16 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c797371c-91eb-3856-9473-dee2e4ef5f82 | 2.54492 | -60.58982 | 2025-01-16 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6d922930-41fb-359e-9562-ade8fbef4a5f | 2.54107 | -60.59044 | 2025-01-16 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7be44c13-e59c-3fb1-9fee-d532d0ff4ba1 | 2.14488 | -61.85972 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f80fc5f5-59e0-3642-a32a-6dd89cac3a3b | 1.32233 | -60.03884 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1037acd8-7432-3455-b4b0-607c6b739ce0 | 4.26914 | -60.29471 | 2025-01-16 05:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 960bf67e-3ed0-3983-a072-8e239c40c7bd | 2.16172 | -61.86246 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0a90b6a-74d4-3ec3-8124-a0868f2ebef9 | 2.54415 | -60.58504 | 2025-01-16 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9de08a6-2d05-319d-8aef-ece13324e51e | 1.35181 | -60.30723 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d0cc8e84-09c6-3d08-ad5b-c84fe48d59cf | 1.17771 | -60.50174 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d8ab12d-cc63-3ba9-b289-c3edf70023a0 | 1.32642 | -60.03844 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26583cb1-f92d-3444-9f25-82b921385736 | 2.16532 | -61.8619 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bfec2df7-afeb-325f-8455-0d3c844e8e6f | 2.53645 | -60.5863 | 2025-01-16 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2ad5e6d-1a5a-3a93-b283-841c89add5fb | 2.16104 | -61.85829 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ebc70b2-8a45-310b-befe-64add731394a | 2.11015 | -61.82701 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 337d6253-f851-364b-962a-31bc07d7192a | 2.10818 | -61.81455 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5ac6b2f-d492-3321-bafc-e9298c0f42d3 | 0.83861 | -60.27039 | 2025-01-16 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51303ec4-0bbd-3573-9a9b-3fd8fbedda4b | 4.41 | -60.59083 | 2025-01-16 05:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abf0bfe6-3b1f-3972-ae3d-6501944b45ea | 1.17693 | -60.4967 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b3a7d60-303a-3d32-81e8-d99d95c0aafa | 0.84683 | -59.54137 | 2025-01-16 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bccca514-439f-33fb-bccb-da86c04bd003 | 2.10095 | -61.81569 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72096cc1-450d-3cb2-87e1-e25073fd7407 | 2.15811 | -61.86298 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05318ea5-7d5a-3ba5-a61d-b1d365cff48d | 4.29581 | -60.12984 | 2025-01-16 05:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76de6524-13a7-3265-bba6-d2b8411dfdf5 | 0.55107 | -59.80275 | 2025-01-16 05:44:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 587ddc3a-4800-359f-a9e2-610d5f344aec | 2.14913 | -61.86332 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 945ff805-b98e-3045-93e1-3c2c0d5c9c28 | 2.19403 | -61.81055 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c81cc722-ae2e-3461-b41d-11ab85db6a67 | 2.1545 | -61.86351 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bda5ae5-379d-3038-8d83-51ed7668c3d9 | 0.63534 | -59.81339 | 2025-01-16 05:44:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6bd0ab4-b09b-3b49-be03-dfef8dd84ade | 2.11672 | -61.82178 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b7f3a0a-802f-3493-bead-0084ff72cc4a | 2.15635 | -61.86224 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05cb9a11-6fa1-3f10-8e7d-a7f4345fde59 | 2.54184 | -60.59523 | 2025-01-16 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| af5aecfb-969a-3d6b-87ff-3f876878db23 | 1.32235 | -60.03903 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9345a24f-a62e-30aa-88ab-dedae9a0235e | 2.10392 | -61.81107 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 777486bf-1e6f-3979-8a82-d3ebce42a225 | 2.5403 | -60.58566 | 2025-01-16 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16f711ad-0c78-3fd1-98f0-e86f13f16ae6 | 1.18009 | -60.49102 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7217201b-dc66-38fa-aa21-13847f3d2c37 | 1.17396 | -60.4849 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adb24f28-a226-30a2-9318-813856fe1c97 | 2.18681 | -61.81169 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57c03a07-9573-33ed-8864-817a1a3c7090 | 0.72751 | -60.12413 | 2025-01-16 05:44:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 709b3357-8b4f-3fbd-b5ab-727ed3d2400a | 4.26835 | -60.28981 | 2025-01-16 05:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 521f7637-f51b-3357-b8b6-2d0e15addded | 1.32526 | -60.03131 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e39ef172-ad5f-343d-87be-238b90a470ff | 2.1016 | -61.8198 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19180880-303b-3d7e-9eb0-c14e56c99272 | 2.11606 | -61.81759 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83c79906-4216-377a-bfc9-84732705fc28 | 2.19042 | -61.81112 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c62e3529-4e67-3a8c-9160-41a29e3592b4 | 1.01564 | -59.56833 | 2025-01-16 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97dc2e9b-b35a-31d3-85f1-574fea39c61b | 1.2943 | -60.43237 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 27924a30-e6d9-381e-aa28-9d3b95cc70d4 | 4.1473 | -60.0371 | 2025-01-16 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 580a1b68-5dba-3047-a277-de2a4837540f | 0.58641 | -59.2382 | 2025-01-16 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6eb1463-38c3-33e4-949e-abc6d291ab14 | 2.09733 | -61.81624 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c382be58-abc2-3518-8ec0-687208f9c2cc | 2.15089 | -61.86404 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e32593e1-63f5-3b34-9c24-82df3bd21f89 | 1.16903 | -60.49796 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85ee4bac-b914-3798-a741-b71b76d72dbb | 2.53722 | -60.59108 | 2025-01-16 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3ac930d-7641-3640-8b43-7d6db8acb1c3 | 0.63804 | -59.8123 | 2025-01-16 05:44:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44cbd9af-46fe-3f5e-a98e-bb63c03b24ab | 1.63631 | -60.28369 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e34bc1c3-57bd-363b-a9d4-b62f7a73e12f | 2.16825 | -61.85718 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 142fab84-f87e-3f0b-9128-a435533a4ccf | 2.10456 | -61.81514 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e38606f-5e32-3aa1-ab8d-0f56dcd480c3 | 2.17972 | -61.85961 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3c83f6b-8ac3-3fbb-ae26-a29d9e6ec9bc | 0.72578 | -60.11327 | 2025-01-16 05:44:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 543192e8-0301-3149-8692-f0cd5be4fd47 | 3.73528 | -59.72369 | 2025-01-16 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9551f0cf-f814-303f-b756-028759379d2d | 2.19896 | -61.81827 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e58e521-def5-387a-9c66-79a07bbe80c3 | 2.18331 | -61.85902 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 032b211e-5190-352b-823e-38d3fbfa1e14 | 1.32177 | -60.03547 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 426d12e3-f77c-3ece-82d9-94d87d82f44a | 0.83917 | -60.27388 | 2025-01-16 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bcabe64-8bf0-3ab2-904e-e67442f3efe8 | 2.14553 | -61.86386 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a5b9832-6c9d-3986-a0d1-5d7b511ecdb9 | 2.19469 | -61.81469 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb9fea1d-862e-334a-9bf2-62857467960a | 3.93294 | -59.68072 | 2025-01-16 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9881d2a6-6a89-349b-a053-34b1c1bd5baf | 2.11311 | -61.82231 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dd91bff5-e689-334f-b5cd-cf121df542c6 | 2.15022 | -61.85991 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 525fddd7-d349-392d-a438-78e40a923d07 | 2.16892 | -61.86133 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88677740-311f-3351-a8cd-040c9433b002 | 0.84323 | -59.546 | 2025-01-16 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README7.md)
