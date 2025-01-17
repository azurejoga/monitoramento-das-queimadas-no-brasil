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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31abadf4-3292-3999-a603-ffc59c610e68 | 1.02959 | -59.48613 | 2025-01-17 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14b1d669-f7d9-3cce-bea0-7075b2c0743c | 1.13776 | -59.43666 | 2025-01-17 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0d2d81a-e791-37f0-bef7-2f4cfefc382b | 1.12489 | -59.43485 | 2025-01-17 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af26d26c-d12c-3543-8232-27e783e4c2b0 | 3.60131 | -60.09808 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f15f9a4-de5a-3136-b27a-bbf4817f87df | 1.13273 | -59.43766 | 2025-01-17 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 687261e9-54f1-3d83-b0c8-83a008ccf0ca | 2.18812 | -61.8181 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cbfbe2c-5613-3c7c-9209-19c6ccc675e9 | 3.59813 | -60.10746 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f11d4baf-9a20-3b65-9944-d052e36359ae | 1.90025 | -60.5718 | 2025-01-17 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0293c946-65fb-3f44-b790-a2ca5450168e | 2.17909 | -61.85815 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 44799e7a-52cf-35e6-b916-1c8510a1cacd | 2.18402 | -61.85746 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c0a8deb-80d5-3d8d-8e6a-442ed4753966 | 2.19303 | -61.8174 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d20ccb2d-59e9-3321-87cd-a9f8f6185bcb | 4.26742 | -60.15548 | 2025-01-17 05:01:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd9273f7-f5ea-3494-9983-cb72fd26c5bf | 1.13684 | -59.4371 | 2025-01-17 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25abf9cd-e79c-3e06-b97c-2d04835671aa | 1.17202 | -60.4958 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8071265a-ea1f-3218-b145-32500f887660 | 3.59999 | -60.10976 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fb13859-723b-3761-ace5-5b1f68bcadf0 | 1.17575 | -60.49088 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2937dfdb-b43e-3668-b453-5c0486d56b0f | 2.1922 | -61.81194 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a615dd0c-205d-3b27-ae85-1f1b6c261d6a | 4.85112 | -60.62903 | 2025-01-17 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab97479b-cd8b-3358-8c66-2ac68768637c | 2.29464 | -60.22045 | 2025-01-17 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89a8fa50-528f-3204-951d-c67e52b91b27 | 1.34708 | -60.03013 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 3ee9f867-1c3a-3772-9d8a-d0ff9a40f855 | 1.32337 | -60.03347 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 596c7247-a841-3742-820f-431ab1dd0970 | 1.32764 | -60.03277 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0268d2eb-3d71-31f0-9641-886234a831e1 | 2.16925 | -61.8596 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f4f5c5c-4d02-3c67-906f-ff8696e0f955 | 4.12535 | -60.02849 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4295773-2ca7-341c-886b-b14eea26f6e1 | 4.29403 | -60.37094 | 2025-01-17 05:01:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39f80c78-2f6a-39b6-80e9-79e6d75ae64a | 1.74134 | -60.63846 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8512204-e2be-3f74-a532-58142ee20e73 | 2.1619 | -61.8566 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ad4b0a8-2c20-36ca-970e-2b3857461f43 | 1.34648 | -60.02618 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 67f5ca28-6442-3e20-becb-27d37315b0af | 1.12546 | -59.43844 | 2025-01-17 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9bfa7e3-afb9-3a71-b90b-fca66b714c3d | 1.0322 | -59.48646 | 2025-01-17 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33b99a37-abfb-3afa-bddb-bfb03ae83032 | 3.74602 | -59.71778 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6e53880c-4572-30ed-af90-ad1c18914cb5 | 1.12955 | -59.4378 | 2025-01-17 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| def3d5c4-2bf8-39ff-8c00-1c6dcceb0f0d | 3.60194 | -60.10242 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 574e7c12-af82-30b3-915f-264ca4aebbce | 4.29334 | -60.36619 | 2025-01-17 05:01:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52622735-77ed-3157-8e91-7ef499bc1148 | 3.13947 | -60.70009 | 2025-01-17 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d0b0ca8-1a92-30bf-b2dd-8b833222f68a | 2.1873 | -61.81269 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47846d60-5356-3a9d-9626-9089a1dbb4ab | 3.59932 | -60.10541 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26fb9d5a-b9f2-314d-b742-0068c2bf2ff1 | 3.60258 | -60.10677 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f33e3afb-ba73-3754-93e5-41878e685550 | 3.60067 | -60.09373 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 316ce65a-2f93-31fb-b608-174e78801de8 | 4.12336 | -60.02999 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e076818-ff3d-3bef-8839-b6d90d48297e | 1.3428 | -60.03075 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e08953a-dce1-3418-a9c5-ca21b6dbee91 | 4.02656 | -59.67284 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc5a4455-8b66-3c38-bcb3-4557bd8a2c82 | 3.59732 | -60.09239 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1bbe76d-9dbe-342b-89c9-e366f9290ee6 | 4.33551 | -59.70307 | 2025-01-17 05:01:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13d137dc-9218-366a-a00e-5696b31d2319 | 2.17417 | -61.85886 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d49d55de-bb0f-3c49-877b-f54f0a49814f | 1.16762 | -60.49649 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4b7511e-162f-3984-a551-65061ebd7d51 | 2.29024 | -60.22108 | 2025-01-17 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56f5de27-9649-30de-a22e-56a5d20c7225 | 3.60243 | -60.09605 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 013bffac-258a-3ae5-8801-7cd0e61d17af | 0.63426 | -60.0387 | 2025-01-17 05:03:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f48a9315-2b2d-3da8-849e-c117e59a62d2 | 0.72784 | -60.11742 | 2025-01-17 05:03:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 607c32c9-bfe6-3fae-8df3-82a70d337b0e | 0.66618 | -59.99397 | 2025-01-17 05:03:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 917078c6-a42c-3071-b75e-d7d79037b9fe | 0.71641 | -60.01502 | 2025-01-17 05:03:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9697ad29-9cfc-319c-b5af-5eb0e40006e4 | 0.72064 | -60.01439 | 2025-01-17 05:03:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa3d5f21-5970-305c-bd3e-813da3e0cb73 | 0.93041 | -60.32915 | 2025-01-17 05:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4862a2a-30d3-3eb4-b582-f84f603c0617 | -0.15519 | -60.87344 | 2025-01-17 05:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c118ae79-4515-3c20-8ccd-c4f8924f5677 | 0.72906 | -60.1253 | 2025-01-17 05:03:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07761fb4-36f9-3dfa-9b2e-6d73ed2d2ee9 | 0.84662 | -59.5444 | 2025-01-17 05:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbcd3f57-f96e-3af7-a53c-9612a7e51ba8 | 0.82457 | -59.71339 | 2025-01-17 05:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 232084d3-6678-3dab-820c-49e984ef8f38 | 0.67948 | -59.5854 | 2025-01-17 05:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59a17f50-f54d-35d4-82c0-886afb6d5961 | 0.84196 | -59.5414 | 2025-01-17 05:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31e5919b-b828-3768-af62-a5e793226529 | 0.8375 | -60.27248 | 2025-01-17 05:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11aecccf-0308-3d4c-9cc4-d02eec17a3c5 | -0.15452 | -60.87165 | 2025-01-17 05:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bcf97449-7477-31e2-83c1-862d127b4123 | -1.52325 | -54.93634 | 2025-01-17 05:03:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f8c21af-b908-3315-a93c-173d967ba038 | 0.72845 | -60.12135 | 2025-01-17 05:03:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae84feeb-e7a0-33a6-be92-2852139a383c | 0.66978 | -59.98944 | 2025-01-17 05:03:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 228f8b21-0a9e-35e3-b878-f41988468e95 | 0.85074 | -59.54381 | 2025-01-17 05:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f5bf26a-fdcc-3715-9f1b-8f2b58c3852c | -0.15894 | -60.87234 | 2025-01-17 05:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7ee2a6f-d95a-3ac4-bc99-9c5653b2acef | -0.3581 | -62.75122 | 2025-01-17 05:03:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3bdf96a-03f0-3c92-b613-1f544bdfc6e1 | 0.85018 | -59.5402 | 2025-01-17 05:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45783411-74c6-3731-88c3-289c72d4cc85 | 0.67039 | -59.99329 | 2025-01-17 05:03:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fb200d1-50e9-36ed-8f71-b5c6417d1252 | -2.75176 | -54.59351 | 2025-01-17 05:03:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbe1713e-c3be-387e-bcf5-f14fe5701715 | -1.35877 | -55.21083 | 2025-01-17 05:03:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b362077-d27c-3b61-835f-3227c7f9a800 | 0.58942 | -60.44271 | 2025-01-17 05:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7d7a6db-ab49-366d-8829-19f37158321a | -0.15584 | -60.86914 | 2025-01-17 05:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2288bd9b-47b0-3067-8e0f-fe233499c2a9 | 0.82515 | -59.71712 | 2025-01-17 05:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98e57cca-e15a-3750-8506-820af79fb692 | -2.53403 | -53.95683 | 2025-01-17 05:03:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3cdcf0a-7071-30e4-ba99-d26acef66b0d | 0.84607 | -59.54079 | 2025-01-17 05:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4968068-bd80-3745-9212-17347c1f1c1e | 0.84251 | -59.54502 | 2025-01-17 05:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae371bcd-453e-3d32-af41-50348ca260cd | 0.7248 | -60.12599 | 2025-01-17 05:03:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbd9d720-5af9-33d0-abdb-e5d94e8625e2 | 0.66829 | -59.59457 | 2025-01-17 05:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 186b0498-3812-3962-8ccf-045e93fad2b0 | 0.86511 | -59.69268 | 2025-01-17 05:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fa154f6-f707-3710-bfc3-368306969cd7 | 0.16556 | -60.65734 | 2025-01-17 05:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 319c419c-2a1a-332d-99ca-d656c896aea7 | -16.22751 | -60.12782 | 2025-01-17 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9974d233-691a-3db3-89ab-1fe04541f1c3 | -16.11663 | -58.17884 | 2025-01-17 05:08:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6c2f1fe8-fb15-35e3-8310-9581eded6896 | -20.38251 | -55.92292 | 2025-01-17 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c8b951c8-c615-39ff-891c-ea2e300e5067 | -15.55566 | -58.98144 | 2025-01-17 05:08:00 | NPP-375D | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5bab65b-ef98-33e3-9a5f-5542d6610afc | -15.82839 | -58.07995 | 2025-01-17 05:08:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 764e669a-b512-3b75-9015-cf71da15386b | -15.80423 | -58.52562 | 2025-01-17 05:08:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7d47c88e-e2bc-38ca-a1da-2a07d0f8f578 | -16.15248 | -59.24469 | 2025-01-17 05:08:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dcd9668-30f0-3f9a-a843-9b05c9659d23 | -20.20687 | -56.6219 | 2025-01-17 05:08:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 927f0963-70b1-35d5-aeba-a7e0a16f3b33 | 1.3403 | -60.0271 | 2025-01-17 05:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2d7a94bc-80e3-3c70-9095-e8da6b739cd8 | -24.00088 | -52.36171 | 2025-01-17 05:10:00 | NPP-375D | CAMPO MOURÃO | PARANÁ | Brasil | 4104303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 904e6b16-313d-388e-88d0-fc4b7f01a99d | -29.6422 | -53.3587 | 2025-01-17 05:12:00 | NPP-375D | RESTINGA SÊCA | RIO GRANDE DO SUL | Brasil | 4315503 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 74214094-cb8f-3bc4-84ba-f944aca3f6ca | -29.78077 | -51.17645 | 2025-01-17 05:12:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| b243c23d-7589-3622-aad0-6374ac2cc345 | -29.77534 | -51.17587 | 2025-01-17 05:12:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| eec66d51-3a5d-351c-951d-dd9ab9cd9785 | 1.3403 | -60.0271 | 2025-01-17 05:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a6edcf9a-1b8b-30b5-8f53-ec5bebc7b934 | 4.84998 | -60.60288 | 2025-01-17 05:25:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4f38517-1e66-33dc-a221-20154e425dbe | 4.85433 | -60.63093 | 2025-01-17 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a0def15-ceb1-39de-9a9e-8d0fcdba4919 | 4.85052 | -60.60638 | 2025-01-17 05:25:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d7090da-9fd3-3018-bb14-ace6f74c5c2c | 4.72641 | -60.7011 | 2025-01-17 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README4.md)
