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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c0b9a14-b4a5-384f-aaf9-a9065e2c62b5 | 1.3221 | -60.0463 | 2025-01-14 05:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.4 |
| c48a6458-3201-39c1-8b66-d44c42a731a1 | 1.3221 | -60.0272 | 2025-01-14 05:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 44e9c6ff-1ffa-36a0-863d-b3eb0b14f033 | 1.3217 | -60.4262 | 2025-01-14 05:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.1 |
| ff5d446d-1b6e-3c1a-b404-b003fc7bb682 | 1.3403 | -60.0271 | 2025-01-14 05:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 73f2f626-6b2d-398a-b431-391e5ffe2b40 | 1.3221 | -60.0272 | 2025-01-14 05:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 46440231-0019-38e5-b6d4-02ca044f46f8 | 1.3217 | -60.4262 | 2025-01-14 05:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| b247c0d2-e550-3a33-b756-551423987cc4 | 1.3221 | -60.0463 | 2025-01-14 05:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.8 |
| ac10ac8d-fe8b-3d8d-babd-bb8bed43c3fb | 1.3221 | -60.0272 | 2025-01-14 05:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 9b766fad-7664-3a7b-b66a-d191b10035e0 | 1.3221 | -60.0463 | 2025-01-14 05:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 540d0e2d-8d56-37d4-bf2f-efa063f79d0b | 2.95632 | -60.17681 | 2025-01-14 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0e3f05f-a532-34eb-8d15-38cdd98a5890 | 4.07769 | -59.94397 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f5d8bcc-8c34-34b7-ab38-f65c51cd59f7 | 0.83277 | -59.96606 | 2025-01-14 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6f43ca1-fedd-36f9-9ca9-5820b124aecb | 0.85464 | -60.55305 | 2025-01-14 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6644622-a693-3b9f-a527-66482fc4b676 | 1.18215 | -60.49179 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac683256-e2c8-3310-9ee3-4fdda5482a78 | 3.23165 | -60.6042 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 006732f2-1399-3352-9eb5-1af0603e965d | 0.85127 | -60.55356 | 2025-01-14 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f26f1ae-9a40-3681-8baf-58f7a0851f7e | 3.58353 | -60.85194 | 2025-01-14 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c19bbc6-ea17-3266-86e0-99c6597bd7b5 | 2.94475 | -60.18208 | 2025-01-14 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 75d3b370-36f7-327f-9379-0f29ed054179 | 2.06755 | -61.84305 | 2025-01-14 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fde8a910-fc7d-369b-b17b-155f33f48873 | 4.03946 | -60.20131 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4020a2d6-8e64-3281-8648-f2479d141617 | 1.90277 | -60.57045 | 2025-01-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e54ff9cd-87c1-34ba-b81e-ee475d55a3a0 | 2.18477 | -61.8102 | 2025-01-14 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ee74094-41cc-3a16-a1c4-8a19b7191bd9 | 1.93802 | -60.40776 | 2025-01-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 989db31a-00e3-30df-92fc-ef62edeac2be | 1.31688 | -60.03049 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8c4c09c9-d82f-3344-b2d7-c6928ef586c2 | 2.06318 | -61.83671 | 2025-01-14 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b73b2b4d-2bc9-33a4-a71c-8ad4853e8205 | 1.12162 | -59.4611 | 2025-01-14 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8a5f294-b4b8-33ef-8eff-9426deeb81e5 | 1.32888 | -60.04002 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4371855c-2d23-32b7-be9e-b967093808a7 | 2.07743 | -61.84152 | 2025-01-14 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f2d412b-9ff2-3e93-ba08-07427b45ec9d | 3.04106 | -60.75565 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fd20302f-36a3-3e75-a21f-a892cd6e1fc9 | 4.07266 | -59.91202 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a717dec2-cb5b-3513-adfa-93339cf81a03 | 3.10192 | -60.73194 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8eafe06a-bb0b-3af9-8df4-8f2f5a833bfc | 2.07084 | -61.84254 | 2025-01-14 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7be9ec99-05d5-3f19-8aaf-b6312c1656ac | 3.60141 | -60.94471 | 2025-01-14 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a82329f4-a6ac-3aa2-8e05-56fa33740232 | 4.03891 | -60.19785 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d913383-a91f-33b7-9f45-cf55c7e737e6 | 1.11812 | -59.46165 | 2025-01-14 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bf14ca8-693e-3d37-a42d-179915c36916 | 3.10469 | -60.72794 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 736417ae-23cd-3adc-a872-c89c5f196311 | 2.05989 | -61.83722 | 2025-01-14 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4bf66b03-b86c-34f1-8452-0b9b17287227 | 1.33113 | -60.0321 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba36b962-a505-3593-85c5-f10eb4d17f6e | 2.94567 | -60.17484 | 2025-01-14 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ea6c91c-18b0-3ec3-81e8-a6e987998b24 | 1.31804 | -60.03788 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fa399945-d25e-33e4-b9b8-194294c2499c | 3.10082 | -60.72498 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ca71d8b5-6506-34bd-bbf9-e5e9e4efbc82 | 1.31529 | -60.42651 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d9df6cc7-f986-3254-96dc-c3b01a0ca779 | 1.17878 | -60.49231 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f035ab52-b0c0-3dbd-8c45-9a8dacd8692d | 3.1036 | -60.72098 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad9e965e-8864-3654-b514-6797a2396817 | 2.18531 | -61.81363 | 2025-01-14 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58d3d565-486a-310c-9db1-e43e18504abe | 2.94083 | -60.17903 | 2025-01-14 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 49154928-ad28-3531-b227-f108fcc0f27b | 1.93466 | -60.40826 | 2025-01-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e11afaac-42bc-3c7e-a23a-e83caf82ddc9 | 1.11751 | -59.45774 | 2025-01-14 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd0d0836-0b0a-3a6e-b9ff-56f55e2c4931 | 1.31862 | -60.04158 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a0d197bf-ebce-32f4-934b-250f043894e3 | 3.91231 | -60.84282 | 2025-01-14 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d8d735e-3ac6-317f-a97b-5cb85dc42da4 | 1.3203 | -60.02997 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 06778d85-262b-387f-97a1-2bc7425208b6 | 3.6877 | -60.05926 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19afef65-2e82-3607-ba19-275b833bfb1e | 3.59949 | -60.84188 | 2025-01-14 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 723da287-29fe-3683-baa7-ac06ebc078e8 | 3.11796 | -60.72587 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f03d311d-5509-3b33-9870-d0a9ef2d84db | 0.77703 | -60.53159 | 2025-01-14 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0597432c-4fb8-3be3-854e-876c972e3377 | 1.17541 | -60.49285 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8177473d-5921-38b2-89ce-6f6704773204 | 0.63675 | -59.94966 | 2025-01-14 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2f87450-5454-3350-ab90-bc73750a80c6 | 4.07322 | -59.91557 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac5709c9-1b71-34f3-80df-c4eacfe5b7f6 | 2.9442 | -60.17849 | 2025-01-14 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8fd884b9-9d6b-3023-a715-954dc8015d9d | 3.59702 | -60.9383 | 2025-01-14 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11948b05-1bb5-37f3-b129-61e1dffca096 | 1.17934 | -60.49591 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 591de000-fab7-3775-b0ac-0fe1ee4bd356 | 2.94681 | -60.18198 | 2025-01-14 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 90261655-ac0c-310b-b595-3e10e6c2321b | 1.3243 | -60.03314 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.3 |
| a51ce082-4a08-3acf-93c1-3e4d30c288b6 | 3.10414 | -60.72446 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9b40960c-6bec-3854-8e15-1884164fd8cc | 1.31472 | -60.4229 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7fe45832-39d5-3e48-9584-c1d75d4de993 | 2.18201 | -61.81413 | 2025-01-14 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08d7477f-495d-3daf-a638-615b095e5d5f | 3.11192 | -60.70898 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13453478-0c90-3257-8094-893f1226d75c | 2.96011 | -60.84656 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 417b96bb-020c-3d83-a05d-815d0116933d | 1.32146 | -60.03735 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6f84d88b-da2b-3dbb-bead-901e0cac0964 | 3.1086 | -60.7095 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b3eb201-ae65-3759-a0af-968028eacb74 | 1.3181 | -60.42238 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af8bb8bc-0c1d-32eb-82a3-ed68b4815a6d | 4.05527 | -61.14764 | 2025-01-14 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f767fe6-2a89-3904-b923-7f2a1936a52e | 4.04223 | -60.1972 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43c91ce2-042e-3111-ba08-96c501e00ec7 | 1.31585 | -60.43011 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6568bd0-a8d1-3e64-b868-9344ea67bbaf | 2.94531 | -60.18565 | 2025-01-14 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6fece571-c79e-30a4-ad21-378e5df16c27 | 1.31247 | -60.43063 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d3f0d87-3b28-3b4b-9226-28c946287c7f | 1.32546 | -60.04054 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c066d20b-323a-3ec0-82b1-8865a0ffd999 | 0.50772 | -59.34004 | 2025-01-14 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b6e0c46-b352-36f6-9d57-8eb44832f89c | 2.07031 | -61.83912 | 2025-01-14 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4047dbb3-75be-3f45-b676-41ec271c23aa | 1.04744 | -59.54417 | 2025-01-14 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76608e95-9457-3828-ad67-64da07e7ed06 | 1.32772 | -60.03262 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 589413f4-76b3-3ee0-a06f-4772bbe7d97b | 1.17373 | -60.50414 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa92f4d9-7590-3fd9-8bb4-290e91d2f0e1 | 1.32262 | -60.04474 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fb3d335e-0507-33bc-a45e-61f6048e9487 | 1.38703 | -60.79847 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8d75e71-71c0-3a80-aeb4-708523aa7f6a | 1.17822 | -60.48873 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e10e2488-82ca-30eb-9a9f-e2fa57717d5f | 3.74955 | -60.41231 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dc1f791d-8577-3ba1-9f01-36e6567b29bd | 0.77366 | -60.53214 | 2025-01-14 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbaadfca-b3e4-3da6-9158-7300d6ec1a2f | 1.81221 | -60.43129 | 2025-01-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f07d9b0-c7a0-3ae5-a5b5-36a27e50e5fc | 1.32713 | -60.02892 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c281d34-fe0b-3672-b466-e346940d02c7 | 3.10969 | -60.71646 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15c9d1fb-c803-367e-b589-29a83f8269fb | 4.08553 | -59.95006 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25cdaa6b-1d2c-31f6-a584-cfa35bfba179 | 1.33172 | -60.03583 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cdb9ab3-53f3-315a-ab85-c6a8a8c822a2 | 3.60033 | -60.93779 | 2025-01-14 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb03fd65-7d7d-3b99-b3a5-0db5034576be | 1.38369 | -60.79898 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ea982cb-f333-3371-a4d9-6d6d9fe076e5 | 1.31191 | -60.42703 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 00b600e6-e61d-3659-9d07-b3b529d9e138 | 3.59426 | -60.94227 | 2025-01-14 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5dd5ff0-326b-3d83-b064-846edafb3148 | 1.32088 | -60.03367 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 65c9b5a5-ec60-3d62-97b1-febf204e6380 | 0.99582 | -60.56033 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daf4765f-95a2-3b8e-890a-482827a2061e | 1.17654 | -60.50003 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e53ebef0-3282-3466-9b6a-4b23288f1c28 | 2.42896 | -60.65092 | 2025-01-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |


[Clique aqui para ver as próximas entradas](README6.md)
