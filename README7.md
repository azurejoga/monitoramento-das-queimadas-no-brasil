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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fb59dcc-27df-30e8-a088-91dd10f5d52f | 3.17485 | -60.6889 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 882c49d6-4d3f-318e-a26a-a937608ad4d6 | 1.85925 | -60.39647 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 7d10da51-2a9f-3157-98f7-2ef49a698a2d | 0.05484 | -60.97999 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fbf527b7-9da4-38a4-9c9e-023857369765 | 0.64703 | -60.66134 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3977cf8-54ce-354f-a95a-de919275d8d5 | 1.49566 | -59.93099 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae383b69-2b6a-3123-aa66-6b2d4dd1d1b7 | 1.54964 | -61.02274 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f8ec045-e3dd-31ea-94d3-d82bd6bda063 | 2.32158 | -60.38329 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d987e92d-65d1-3271-bff8-359357202bc4 | 0.4588 | -60.39581 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 275daca7-0546-390d-be16-ceefdd12db1d | 3.42015 | -60.82561 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90c47dbb-dc31-3f70-b50b-c6f9fad3b9a0 | 2.67388 | -60.42379 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4c928e81-9e64-3b02-8c9a-e7386ad0219f | 0.64308 | -60.65828 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 399bfc64-fdac-3e8b-9575-1852613d5207 | 1.49911 | -59.93046 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfa9aabe-9014-3a71-b165-6ab216535fe3 | 0.70131 | -59.97048 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e76c435-c9d5-3ae9-9137-39bdce88f9bc | 2.8485 | -60.84385 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b35e6d5-1579-3e40-8804-5ec35ba61a61 | 1.33747 | -60.06181 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce5bed3e-b28a-3447-8756-34bdd9099a6d | 1.50768 | -59.91762 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 70c67fa3-5035-37c7-94e9-0633d95fb6bd | 0.09338 | -60.62382 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e212227f-31a7-3ed6-a39f-4a4b2d58cb53 | 0.18662 | -60.44117 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03890289-5f57-353e-9287-6a2e09faf233 | 0.19462 | -60.44746 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1063e39b-81d4-3dba-82a7-8e4a704524ee | 0.91916 | -60.52729 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b146977-1773-3e21-a882-cd197827b96f | 3.03828 | -60.67442 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a055b089-6706-351f-9db3-11ad7ad0bb90 | 1.1732 | -60.36566 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dff9227-e041-3159-b00c-42d923052390 | 0.09169 | -60.63525 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 922e0e62-ddc0-3dc2-b18d-1262b6158ac9 | 0.45479 | -60.39267 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 631816cc-4654-32df-b405-5dc30c99c978 | 1.4996 | -59.9112 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4046ae67-2891-3689-b384-b8246e1d3d4c | 1.48579 | -59.91331 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe6e6fc2-2974-3c12-b45c-f59a253456c7 | 3.16873 | -60.69342 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2dd8c59c-afd7-355a-a8a8-2a35d225277c | 1.50944 | -59.92882 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52ea4ca7-3a42-39d6-82d9-d12577c6c155 | 1.49211 | -59.90854 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5f07738f-6d14-371a-8412-cf3982a74b75 | 1.08081 | -59.2455 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10433092-4313-3657-9638-2e8045ea321b | 1.51113 | -59.91712 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c7078641-4de8-3b93-a5fb-e9e28f27ae0f | 0.55687 | -60.39999 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8d28245-5ba5-3f96-a142-bef732ce8bcf | 1.86774 | -60.4062 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8792905-5636-37c6-92b2-36e9d3bd92af | 1.09455 | -60.17853 | 2026-03-02 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 030ad294-17c1-3b46-9452-bd5a02d4b9ce | 2.8604 | -60.83842 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50622688-e32c-3d78-9e8f-b4382458c2f9 | 4.25452 | -59.90243 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d86e7ac-d42a-3459-97d7-6c088f9106b1 | 0.49554 | -60.51741 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fec4a590-4848-35e2-b027-86adfb6923e4 | 1.93506 | -60.80764 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 401494b5-1e0d-34fb-8513-ca55e0fd3eae | 1.49901 | -59.90747 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3c9c835-43dd-3fad-b5dc-0b33880d5492 | 1.08563 | -59.25298 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17da4199-d670-3030-8ada-901882255a7f | 1.86264 | -60.39594 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48400a0e-66d7-3aec-9b2b-ab6bacc336a6 | 1.50541 | -59.92564 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9146be81-b8b8-38e0-8ddf-d993df842da7 | 1.50364 | -59.91441 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 96d1abb2-3bd7-3e69-8460-34f83ca0f85d | 4.37658 | -60.62141 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d362bc92-47a8-3414-b63d-927babdaedc5 | 2.84684 | -60.83337 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 60f86674-a9d0-31fc-b0fd-68553e38d08a | 1.49329 | -59.91599 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 90781025-646a-3991-aed4-29a705d39284 | 3.16538 | -60.69392 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc161328-9f5a-3227-9481-441edafbc680 | 0.05933 | -60.98656 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5074bf3b-3a20-320f-87fd-afb7f52c8104 | 3.60934 | -61.65308 | 2026-03-02 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9c75532-e505-384a-92b8-acef3afe09e2 | 1.87757 | -60.91016 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8ca3064-a797-3665-bc27-3080f569a68e | 1.49507 | -59.92724 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4fe1526-e8da-3446-8088-10f927b3c695 | 3.61044 | -61.65998 | 2026-03-02 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1b9a1382-ce5b-3a47-876c-14dd2d9cd905 | 3.60712 | -61.6605 | 2026-03-02 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 72c7a350-a140-35e4-ab23-c3ed9f4ada6d | 1.47498 | -59.93422 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 886d58ee-cc7a-3102-bc5d-c41c0af34250 | 0.23302 | -60.51329 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26c9336e-f9f8-3847-a87e-9b39ad7f1fa7 | 3.61266 | -61.65257 | 2026-03-02 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39e26f90-c150-3971-9c6e-28d56fd876bc | 0.09509 | -60.63472 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e4fa4e0-cf7a-3666-a84c-021984b6d9ad | 2.09859 | -61.53783 | 2026-03-02 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ba5c3a8-a614-30cc-873c-895d68b57824 | 1.07851 | -59.25408 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e982b23b-7535-3c87-89ad-bfb93b421b5a | 1.48069 | -59.9257 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 136c01f4-dd8a-30bc-834e-b96b061eac20 | 3.60657 | -61.65705 | 2026-03-02 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81a92c01-c46d-3f22-9f6e-7642dc74203f | 3.60435 | -61.66446 | 2026-03-02 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0fe50b8f-54be-3312-972c-d1355598a2d8 | 0.2296 | -60.51382 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da2c84bf-4656-3175-87c8-9621195b9f95 | 1.06427 | -59.25631 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db009d1d-26af-31ea-a222-b54ab149386f | 1.50137 | -59.9224 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4431f5f2-2cf3-3e63-8a1e-18a2aeec4e23 | 1.49447 | -59.92347 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8530cfda-6c7c-3905-9a6b-fa0165775e9b | 1.82679 | -60.84968 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02d02890-dd16-3448-806c-1cec6bee2334 | 0.64647 | -60.65774 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ee59969-eed5-35a7-8d06-6c369e1051dc | 0.46564 | -60.39473 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4760fc3-ccf2-3de9-9f9e-e71d6026fbdc | 1.48698 | -59.92082 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dcc8aec-cc05-36bb-86e6-29445fb24860 | 1.085 | -59.24895 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d15b63d5-6045-39f0-b371-a5268d443c5c | 3.00762 | -60.69722 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f7f64d9-a346-3330-8b23-a3035785e31f | 4.44421 | -60.72501 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2d3d02c-e379-3259-be7e-3b8686d01e2a | 1.51171 | -59.92082 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 72e0ee30-1ce1-3358-821b-9e13fa332e5a | 0.92198 | -60.52314 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a0def7b-0c11-3726-a841-bd2a6b0bed9d | 1.50885 | -59.92508 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b2e6e9e-73f6-3d12-82c5-61ae4c146805 | 1.09798 | -60.17799 | 2026-03-02 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f3cf5e4-d960-37dd-a8c6-f0bae1ccd71b | 1.86321 | -60.39953 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ada1b9ac-8db1-3a6a-95fd-4e4e54938699 | 0.65164 | -60.31421 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89d0a513-265e-35c0-95ba-5b34fa6d5728 | 1.48533 | -59.93264 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86990dc8-a535-37b9-a514-8881dc7f628a | 1.49556 | -59.908 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 59095dc7-b358-331a-9f19-6b6d526231cc | 3.17262 | -60.69634 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73f0802a-8af0-3e5c-bf7c-3f1d2f45829d | 1.16997 | -60.82954 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba2caa4d-da04-3806-8a09-bed1b219f900 | 3.03215 | -60.67898 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c92c577-f22c-3e95-8a8d-6a8e8deb630e | 1.49103 | -59.92403 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3d9d675-6ee6-367c-8272-c43252774d4c | 3.02323 | -60.68757 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e5b586a-5452-33fe-b8fb-c415b6876bbf | 2.85872 | -60.82794 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18e69160-4cd3-3259-b95e-0c43e3268a25 | 1.77897 | -60.61417 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9ba595f-fd78-3057-9c5b-7faa026166fa | 1.93977 | -60.37299 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0748ee95-4d04-3d97-926c-1377b70c2d3a | 2.85239 | -60.84682 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 308166bb-45bc-3632-9726-41091bbcc7c9 | 1.48639 | -59.91707 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72c58603-05e9-38f2-9b1a-80e7faefeee4 | 0.09395 | -60.62745 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2617713c-7dce-319c-898a-6b5af77e8a59 | 2.85073 | -60.83634 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d67079d4-12f3-3932-a5db-b33371151708 | 4.37269 | -60.61845 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c76e4d5b-e813-3a9f-836a-fb4fb8f6b4db | 3.42126 | -60.83258 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08c75419-2819-37e8-ac63-e234ac344ace | 0.1912 | -60.44799 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78764001-e715-3fb1-b9bb-7c8894d2a3fa | 1.45513 | -60.07463 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfd4ff57-a7ba-32cc-a801-b604a14aa6d3 | 0.3063 | -60.44551 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73fd0aa0-d0fe-352e-af77-c4edcd562d1b | 0.55629 | -60.39632 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ab7a298-6304-3ed0-9756-435012098666 | 1.09708 | -60.68408 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README8.md)
