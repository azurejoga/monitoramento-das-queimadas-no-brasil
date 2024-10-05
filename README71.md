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
| c47e7adf-f7e8-3176-a308-2b49f6109efe | -12.77725 | -50.56049 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27ac2c30-b2e2-31e1-a19e-f837c312e1ed | -12.77723 | -50.55262 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 04da7b00-bde3-3962-84b2-d7e92b820cf1 | -12.7765 | -50.55676 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 03e49b88-9a75-3ef6-a410-46fea7c231ec | -12.776 | -50.54317 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 569f22ed-0c76-3561-b0fe-fa19b0233b43 | -12.77577 | -50.56091 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d5c54567-c86c-38c7-93eb-a3c2ef8d4824 | -12.77524 | -50.54729 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7f85220-49f2-3f29-9abc-665eaffa5454 | -12.77504 | -50.56505 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86568b59-8181-39c8-ad1d-dc21c3a26d86 | -12.77448 | -50.55142 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| a512a7c1-8d2a-30f2-9530-b1a7df7a4ace | -12.7744 | -50.54354 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e522af8a-8bec-3489-8c10-3471abcc3d9f | -12.77372 | -50.55555 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 8747f242-c288-3011-8786-a2332ed8160f | -12.77367 | -50.54768 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b7ca635-74bb-336c-bfa2-fd848c26d0ac | -12.77296 | -50.55967 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| fe250561-d1c2-3f9f-a18c-0433b304597c | -12.7722 | -50.55595 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 175.1 |
| bef09c08-bedb-34d3-8dd8-2d74114165ab | -12.77219 | -50.56381 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| bd906789-88a9-33e2-b157-7a0e454a5f54 | -12.77171 | -50.54236 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ef46eec-397b-3e8f-ba3a-bdfcbbd1aa82 | -12.77147 | -50.56009 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a0c24524-7064-3ecb-b15a-bbe6f57c14ea | -12.77143 | -50.56795 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a52ef014-c491-3cb1-b010-cb6ab3744821 | -12.77095 | -50.54648 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 537a5e18-9d25-30fe-a0cd-d9892329ea16 | -12.77074 | -50.56423 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 518b65ee-870b-3b6a-bb21-2f3d2aba9877 | -12.77 | -50.56838 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e390d34-1ea1-3649-924d-f5ddd444fd80 | -12.76943 | -50.55474 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 450c574b-bf32-3b37-bc3f-7d99efdaf677 | -12.76938 | -50.54686 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 10de4d49-080b-3e9d-b2d2-66344ddab46c | -12.76866 | -50.55886 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| dd190b5a-55b7-350b-af3e-bef6d8e23742 | -12.76864 | -50.55099 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 4772b6b0-f04a-3a7f-8aab-00dc05c05cec | -12.76791 | -50.55513 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 175.1 |
| a40adc8a-7dda-3895-ae9f-e1a4682a4f87 | -12.7679 | -50.563 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 1d8464dd-3d5d-31fe-b671-769a2d00231e | -12.76718 | -50.55927 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 184b6418-49fa-34ae-ba33-bd809198908c | -12.76713 | -50.56713 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aaa1a83b-fdbf-3906-85f0-a3bb02539337 | -12.76644 | -50.56341 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a722a84b-a06b-3804-b9d0-ddf5aa14be3a | -12.76571 | -50.56756 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4689dc7-eae9-3b07-a37d-9de8b4eaf994 | -12.76435 | -50.55017 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 552bfdab-423c-323e-afa7-debc0043a4c5 | -12.76361 | -50.55431 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91c01301-62cb-32a9-8006-1c7b63f7257e | -12.76288 | -50.55845 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8b005c0e-f7f0-3755-a3fc-6da9c9f12fd6 | -12.76214 | -50.56259 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e00b0e06-5ed4-3bb6-a4a7-4bf06bf687da | -12.76141 | -50.56673 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fbe578af-c9a4-3d8f-94a3-f6c3ad85ec54 | -12.75711 | -50.56591 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1545991b-0ed7-3376-8dff-f7730e5b0eef | -12.75549 | -50.60003 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ca70658-ec10-3602-9485-3e2c474a7143 | -12.66093 | -54.03952 | 2024-10-05 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25abd725-4abe-304e-84be-cd70d65c634f | -12.66026 | -54.04306 | 2024-10-05 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b052e22a-9266-3c8e-84fc-5898458a4324 | -12.65484 | -54.04197 | 2024-10-05 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42a91c37-1489-3ee3-8908-d53ccc4a20e1 | -12.65412 | -54.07516 | 2024-10-05 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fd6afb4-d74f-3965-84a1-878b9893c383 | -12.65348 | -54.04907 | 2024-10-05 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b73a52be-7834-355c-9fa2-f7acc88cb4b2 | -12.65343 | -54.07878 | 2024-10-05 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95f06b74-aa3d-32b4-bc60-821bf7b94f82 | -12.6528 | -54.05262 | 2024-10-05 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc1bba26-90d1-3187-ae9c-8d44b39f2a42 | -12.63434 | -53.10871 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 066da779-a7a4-3b46-8341-deda232b0280 | -12.63374 | -53.11179 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a1ba8669-f0ff-3cc5-ba6d-38b53c298682 | -12.63315 | -53.11485 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5b64a525-18f2-33a5-93b8-458d95df78ad | -12.63256 | -53.1179 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 88f1ad8b-6e25-358b-a5a0-0bc171cf5fdd | -12.63221 | -53.10751 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67a0d972-6614-38bd-83e0-fb9e478c215e | -12.63196 | -53.12096 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |
| e5b51050-573e-35a9-a5c7-72d0e6bd92e2 | -12.63163 | -53.11061 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 21277a87-d85e-399d-be14-8f0fdfe1d3ad | -12.63137 | -53.12399 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| babec09a-2d5a-3f4a-bd3c-35b46afc8c55 | -12.63105 | -53.1137 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 7c9b46e9-8b62-3ab3-94e0-e03283c660b2 | -12.63048 | -53.11678 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a8e32765-0c6c-3363-845d-a4128be1578e | -12.62991 | -53.11985 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| b4ddf124-0204-3ce5-912a-aba5ce83d5c5 | -12.62986 | -53.10456 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b91791d-3073-30fc-b1d8-632a71e5c2bf | -12.62934 | -53.12291 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6eb4889a-1760-37c4-b8fe-b0ed40fa522a | -12.62925 | -53.10766 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0da183b-a020-30eb-aa00-fe105c644748 | -12.62877 | -53.12594 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3d502adf-b640-39a2-b597-8f0ffbe55b1d | -12.62865 | -53.11075 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 7eec4dac-95e5-3005-8ae8-795a7a42d442 | -12.6277 | -53.10332 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8f8206f-3990-32dd-8b28-024d06f86ddc | -12.62745 | -53.11691 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 2888a61d-f7d4-3c0e-b8f6-31eeb8d82014 | -12.62712 | -53.10643 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 560b7b84-c38f-3a3b-be49-2f3660dd7beb | -12.62686 | -53.11997 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 6d44d7eb-6dc6-38c7-93ef-ba7cf6febdcb | -12.62654 | -53.10955 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 0baaae92-0f2c-3ea0-91f5-da8381499f8d | -12.62627 | -53.123 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72885df2-22ca-3887-9af6-260f5ef1206b | -12.62568 | -53.12602 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96a2f4f9-0374-3890-938a-7b96702f3f7a | -12.62538 | -53.11575 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| dda7b0ad-6116-363b-b567-82c176c90eec | -12.62509 | -53.12904 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6940600-fb37-3ced-8295-53565c87d536 | -12.62481 | -53.11882 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| bf1fd97f-a2e4-3553-9304-f1d8ac2c093e | -12.62477 | -53.1035 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 362e2e67-9507-3175-91b3-d6da56012b27 | -12.62423 | -53.12188 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 42fc92d1-2af8-3c03-b8c5-c3c354e6c49c | -12.62417 | -53.10659 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c144e98c-e4f8-3b8a-888f-add5f9a8bed2 | -12.62367 | -53.12492 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4d58836a-b00d-3107-8637-92338c644c9d | -12.62356 | -53.1097 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 450e96c9-59ab-375d-8023-ebf8a9e3fb87 | -12.62333 | -53.49975 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f330e0ae-ba9a-3237-8326-e2108e86abf7 | -12.6231 | -53.12795 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d4978408-04e3-3de2-9225-5834a05df644 | -12.62295 | -53.11281 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 9073877d-821f-3cf6-803a-6764c7c008a0 | -12.6227 | -53.50305 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a36253fa-df38-3ade-abdb-7cc3b69330de | -12.62236 | -53.11588 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| c98b9ddd-8bca-3ec2-953e-378b51dd128a | -12.62204 | -53.10536 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad803fa9-22d6-3c96-932a-99b8368c8549 | -12.62176 | -53.11895 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 0f0836fd-179c-3fef-b49d-4fa40b97c3fc | -12.62145 | -53.10848 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5fd80541-ab0d-36eb-9743-c90bd102d561 | -12.62117 | -53.12199 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 7c36c4e7-f6cf-3f4e-ab86-c9f4b3ccc2c3 | -12.62086 | -53.11161 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0f9dee41-f023-3a33-8c76-91bc4a16a12c | -12.62057 | -53.12502 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| bb15c6fd-efdf-3ce3-9182-7790a046f2fd | -12.62029 | -53.11471 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| c7d7d0d6-c00c-3cdf-abaf-80e3c313c642 | -12.61998 | -53.12804 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e3fd544-286e-3350-a7f4-9e439f0dae84 | -12.61971 | -53.11778 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 6e7348b6-8dab-3215-8c4c-7d89582113f4 | -12.6194 | -53.13107 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8294318d-a0b9-3017-ab3d-b3e56d6d67e7 | -12.61913 | -53.12086 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 91cfbb80-a154-361b-b4a7-d8f8436a655c | -12.61856 | -53.12391 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| e21ab77f-4bfb-3bd4-9383-641407725717 | -12.61847 | -53.10865 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| efe47f15-f481-33cd-866f-51921a306e88 | -12.6181 | -53.4987 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 397cf1c7-853c-301f-b994-393e3c2851f9 | -12.61799 | -53.12696 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| adbd77e3-8ad0-315a-9059-1c8d05d8b64c | -12.61786 | -53.11177 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 7adf4a86-0e68-3b4f-b6fd-d3c1a9abb0b4 | -12.61747 | -53.50198 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 90cb3f00-48c2-3f86-9edb-097beb21e05f | -12.61742 | -53.13 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5f36858-bdcb-32d7-865a-5855a9015d98 | -12.61726 | -53.11485 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 01c1aa58-b09e-31f1-beac-551fb4bed59f | -12.61666 | -53.11791 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |


[Clique aqui para ver as próximas entradas](README72.md)
