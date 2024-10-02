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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7da4c0b8-cc03-3b9e-98cd-b8aa0807c8c8 | -13.16303 | -51.24302 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3c530001-918c-3c99-bcb4-15f22de6302b | -13.16258 | -51.23872 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 94d926f9-7d90-3b82-bb28-10ddfe544e01 | -13.16193 | -51.24398 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 841289b7-87fb-39fa-be9d-91612fdb2c45 | -13.15893 | -51.23712 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 75cbda07-7650-31b6-a06b-080ddacc5093 | -13.15824 | -51.24237 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3b90f0c5-f86d-348b-a959-6ce2a4cfdbcd | -13.15779 | -51.23806 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fd9744ea-4241-36d8-9f72-7464e79eafd9 | -13.15345 | -51.24173 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2bad1d47-79b7-3b49-b3c2-d942f37f892a | -13.15299 | -51.23741 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c4dc3c7-7bce-3df4-a41c-aab8ac01db0f | -13.15234 | -51.24268 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21bde311-e8e6-3aaa-b15b-a2f9dc50ffb5 | -13.06863 | -51.373 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| cba4d115-6b5b-39be-925c-40a2a9b91182 | -13.06518 | -51.36207 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e85350c2-d81b-37e0-b6d0-5506e96e7bb8 | -13.06454 | -51.36721 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5521466b-ac58-3dc1-a302-bac39fbc866c | -13.06389 | -51.37235 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 37c41b4e-0c8e-38ed-a89d-fd7229899433 | -13.06324 | -51.37749 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e150ab03-71df-35d2-a4f0-52dab0ddfeda | -13.05914 | -51.3717 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 329800d0-9f97-3785-ac3f-2d2ebc12a41c | -13.05763 | -51.34531 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e75f7dac-c87c-383d-9dc7-8857c48c1962 | -17.22303 | -56.19007 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a47065b0-43e2-3908-9a23-14b012e3a117 | -13.05698 | -51.35047 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cf9615c-9900-3b72-b63f-3b9357d731df | -13.05591 | -51.39735 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b63cc219-ce8d-323c-a120-8dbbbb0ffb22 | -13.05526 | -51.40248 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5ee492b1-66f2-3de9-b144-6523da440e15 | -13.05452 | -51.32758 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6dc56e2-fd24-3d6d-bf93-36b902529727 | -13.05417 | -51.33434 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| daf04362-c123-3787-a97a-71d7a9ec9636 | -13.05383 | -51.33275 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea4eb92a-57ea-389f-bafa-5608ca1f9342 | -13.05352 | -51.3395 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0c051c2-91b6-37bc-8611-77a7c4463361 | -13.05315 | -51.3379 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ec944fd-20da-3828-8cb6-845c95325944 | -13.05246 | -51.34305 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b90e33b4-91b4-35f2-af90-14e0b6e8b5bf | -13.05182 | -51.39159 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94550216-3f60-3420-b86f-87a97f45e891 | -13.05134 | -51.31819 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3e37059-7969-3725-a884-ffea475bf04a | -13.05117 | -51.39671 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 832d5a86-e845-3866-b73a-e1d4f93c46c0 | -13.05112 | -51.31664 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d264384b-0afb-3809-8c15-70114ac19a61 | -13.0507 | -51.32335 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68ad7d1d-8c3b-3668-b169-a8113c8045a7 | -13.05053 | -51.40183 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| a6e15662-d280-35a0-9bd2-8b0773af2acf | -13.04989 | -51.40694 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 06c28490-46fc-382b-bed2-3bdab425ec93 | -13.04579 | -51.40118 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3a704a0e-e628-3c37-9638-42d231630343 | -13.04515 | -51.4063 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9124a2d5-deb6-3086-9010-e5220a455d56 | -13.04429 | -51.40458 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5ffeb183-00a6-309f-8b56-d9b06a351727 | -13.01361 | -51.50517 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 046c5836-0bc3-308a-8f83-dba8985b8cea | -13.012 | -51.50327 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4f19f1ce-48a6-396d-9d63-d17f6e7e6958 | -13.01134 | -51.50829 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3b2cb197-8c8d-304c-b446-41d950a74a88 | -13.00891 | -51.50452 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c369ab13-7503-3c8f-9a4d-df4676ef597c | -13.00731 | -51.50262 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 83a3ef39-190d-310f-95ba-167a3c921991 | -13.00665 | -51.50764 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ce47a8d8-bc60-391e-9c82-a3e0f6e93be6 | -15.67813 | -52.50935 | 2024-10-02 05:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4d95697-883c-3f6f-b88b-dce88643f10c | -15.67776 | -52.50755 | 2024-10-02 05:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 410962f6-2af2-3840-90aa-1e263cb271e3 | -15.67359 | -52.50864 | 2024-10-02 05:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 107ecd5f-b839-37ef-bb0f-aea7d3d8547a | -17.74379 | -53.19053 | 2024-10-02 05:12:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19b84eda-4550-3353-abd1-0de540f2c494 | -12.87437 | -54.01867 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7af58403-1337-38fe-8558-2cb3359b1270 | -12.75766 | -54.0002 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 18ee9338-1fd6-357a-b7f5-f78ba0d3a18e | -12.73892 | -54.01855 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2d78b9b-e317-3c64-a148-ef36425e6111 | -12.71037 | -54.1081 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cb76ee5-65c5-34a8-a5cc-cd039b3ff58b | -12.70967 | -54.11314 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f3ea9e2-d356-34d3-a446-f72195ca3a44 | -12.70643 | -54.10754 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05d5f303-51c3-3ebc-a43a-a1dd463c40f5 | -12.70319 | -54.10192 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99345abe-efdc-3a06-af72-b3259de639ab | -12.69996 | -54.09628 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1ee73ac-7375-33ae-9437-4dc002882eff | -12.68814 | -54.09452 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3047b402-a060-30b7-9f89-b002027cd3ad | -12.6849 | -54.08889 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cfff770-c872-3122-9a2a-fddb65f5c6e5 | -12.6784 | -54.07759 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae6106ac-9add-3fa2-adc1-168986c6ebad | -12.67487 | -54.08049 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 245e87b2-b6fc-3398-8e1e-42c4dbea9d59 | -12.67445 | -54.07703 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5464794-77b3-39a5-83ac-3d0b8831df5f | -12.67093 | -54.07994 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73fa8562-f627-315e-9d13-6d09bfae2a19 | -12.67051 | -54.07646 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d76e025a-5dbd-3023-a6bd-8081146d3056 | -12.6677 | -54.07432 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aed15c55-33a1-35fc-8337-21c779cae3e6 | -12.66698 | -54.07938 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7261acba-7ec3-3afa-9038-b3955fb6749c | -12.66657 | -54.07589 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6966554-20cc-367f-9c32-82fda493a014 | -12.66593 | -54.05851 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 38c34a4d-f73d-3898-8584-f477ed9258ce | -12.6652 | -54.0636 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01f732f1-4527-3ac0-ac9d-99de5918b053 | -12.66448 | -54.06868 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5c6d755-379e-34b7-bd7e-0c3f882f79af | -12.66376 | -54.07375 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91c7bd43-5910-3d5d-b35f-0fb8bbc68edf | -12.66126 | -54.06303 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3116ae61-bdfc-3397-8e2f-73c6a617fe83 | -12.66054 | -54.0681 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c182ad0a-e278-35c7-b77e-265dfb0eb559 | -12.65982 | -54.07317 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe0fc38e-6f62-3135-8309-b581d7bd8435 | -12.33415 | -54.09698 | 2024-10-02 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a39fb7b2-8704-36bf-97ae-cf06174a7810 | -12.33344 | -54.10198 | 2024-10-02 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd6d3292-cc0b-3d46-b878-a9b2d13cb467 | -12.33273 | -54.10699 | 2024-10-02 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa9a4acf-3c72-3919-909e-6a42c554c810 | -12.33024 | -54.09641 | 2024-10-02 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62255b0d-116e-3cc6-aa11-28298c569b72 | -12.32881 | -54.10642 | 2024-10-02 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14814209-6cce-359c-b1fc-f543aca3661d | -12.32632 | -54.09584 | 2024-10-02 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cd41b5d-3700-30a5-bb62-48629e96410d | -12.3256 | -54.10085 | 2024-10-02 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5321b179-24d3-3eaf-896a-d857dafd9471 | -12.32489 | -54.10585 | 2024-10-02 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f738094b-e951-3839-a697-36dd198fcf06 | -12.3224 | -54.09526 | 2024-10-02 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20b1b968-1fe5-3b62-a560-01f5af7bafc0 | -12.32169 | -54.10028 | 2024-10-02 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54c7ce82-e79f-359b-accd-3495036d8508 | -12.26826 | -53.99482 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47cd4b9c-3c48-3a01-9719-ea994d0b1622 | -12.26756 | -53.99989 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 292fad48-80a0-3de0-ba73-e38daacbdd83 | -12.26525 | -53.99277 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4accbe60-8cf1-398a-944e-01ae07ed9466 | -12.26452 | -53.99784 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c5b4f41e-fde0-343b-b79c-a116b4b4b77f | -12.26432 | -53.99419 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8140b837-16a7-3aaf-ab6f-149ac1914afe | -12.26379 | -54.0029 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b14f8a0e-05e9-3511-9a02-8d94434f8072 | -12.26363 | -53.99926 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| afaa1ce8-611a-35a2-842b-6c4cc5e80670 | -12.26293 | -54.00432 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 987c3a03-5543-39b4-8ee7-b6853cea1e7c | -12.25986 | -54.00226 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a02414b6-19d0-3b4d-a7f1-87846e356e48 | -12.2597 | -53.99862 | 2024-10-02 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 910bf4f5-40e5-3d30-817f-3ca645531bf1 | -12.259 | -54.00367 | 2024-10-02 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6e41e21-6d80-3853-b0f1-04bc8417ab9f | -11.89018 | -54.79948 | 2024-10-02 05:12:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5707e96e-035c-3fe7-a4b6-2b9ed4e1899a | -15.12467 | -55.83172 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5db8ed0f-d49a-3319-817b-aa8a331c8e87 | -15.12205 | -55.83353 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 832d74f8-948e-3f59-9208-92d9b816e798 | -15.12526 | -55.82744 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a898dcc1-c53d-36bc-a3d2-28d41f7dd96a | -15.13876 | -55.83828 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2bde79cf-4af5-364f-85cc-8a6debdf047c | -15.12834 | -55.83229 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7afcfb6a-4ca3-32f3-825b-01124f1527d0 | -17.22303 | -56.1623 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2bb5d7f4-dcf6-3e8d-8bd9-01c488aa994c | -15.12775 | -55.8365 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README140.md)
