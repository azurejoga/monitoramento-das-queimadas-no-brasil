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
| 2ee416b3-52aa-3283-b85b-a04e39a0de2e | -3.75263 | -54.65392 | 2024-12-02 06:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65de50d3-7350-3251-9e54-97225e39e83a | -3.17345 | -54.33031 | 2024-12-02 06:03:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1000173f-18f2-3b31-b6ae-ebe4418a10bb | -2.89256 | -55.22566 | 2024-12-02 06:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7367bdd9-e4cf-31ed-b4a1-97a922669a5c | -3.09593 | -53.28736 | 2024-12-02 06:03:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 71b5fdfc-ba5a-303a-a333-b563ad7e9d4d | -3.17546 | -53.63 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f5e07fd-7f8c-30de-a97b-a35a0f9aa215 | -3.06727 | -53.67721 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9ba74ac4-0bd6-381d-8ef5-5f69a336e236 | -3.33451 | -53.54476 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 967d61a7-a98a-3684-9f22-cc33fae6fad7 | -3.2904 | -53.67231 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d78ea61-d226-320e-a0f5-327efdec05c5 | -3.02378 | -51.53672 | 2024-12-02 06:03:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bf64b1dc-95a8-3ba7-9c40-84adfc6de718 | -3.24978 | -53.62666 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1659dd96-fe26-386f-9e89-bfb30d8ae9bf | -1.09661 | -53.64268 | 2024-12-02 06:03:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 492224b8-49ea-38b2-ade7-9a2618e2b9aa | -3.91936 | -53.65569 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be89ea53-6c9b-3f32-8737-660f73f1b412 | -1.028 | -53.54933 | 2024-12-02 06:03:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 6e21b727-ba92-3bb4-808f-cd3f7e7fad22 | -2.83904 | -54.09703 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0c066bda-d8cf-39ee-9018-742b3d0a4a04 | -1.38783 | -53.54876 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| acf443c5-fe84-3001-ac3a-8f3d96bda141 | -1.0266 | -53.55877 | 2024-12-02 06:03:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8b767294-a7a3-332e-8ee2-6b4d33895933 | -2.83766 | -54.10632 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2f9f4348-b260-3cde-a723-d6e1e8823d3d | -2.76155 | -54.11795 | 2024-12-02 06:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8d2b745c-802f-330b-b896-3d229c384514 | -3.74546 | -52.26488 | 2024-12-02 06:03:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c8e19465-73fd-3c0a-90a5-24ded1a0630d | -0.31534 | -51.77494 | 2024-12-02 06:03:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| da06ae44-bfe4-3c70-8fbe-ceda12a24598 | -1.62322 | -53.88874 | 2024-12-02 06:03:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 47ce0007-c1e6-36c8-a606-2f6acb0a2b74 | -4.19218 | -50.68548 | 2024-12-02 06:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c9325fde-3949-338d-81a6-9ff39820ae00 | -1.24937 | -54.54448 | 2024-12-02 06:03:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c1e166a6-12ae-3f7c-846c-e7b7193122d8 | -1.09522 | -53.65207 | 2024-12-02 06:03:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 04fbb59d-84d4-3d77-8a0a-581e4124dbb7 | -1.07089 | -53.44921 | 2024-12-02 06:03:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| cc91ee72-282e-3496-ba3e-3ccd6b42c686 | -3.25299 | -53.92226 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 580f7e7e-5ca2-3437-b7cb-f2aa2e28c89b | -2.4568 | -53.62527 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ec27f26d-1423-3708-bd08-8b1a349934f0 | -3.32516 | -53.54353 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2208c163-f844-3c90-af9a-308199639300 | -3.42356 | -53.89096 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cb05f8cd-8c22-3d33-a692-2f8159722087 | 1.09625 | -56.01708 | 2024-12-02 06:03:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 43be8ad1-94ce-357c-b7bf-72fcb2ad090a | -1.07229 | -53.43983 | 2024-12-02 06:03:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e949d7ac-9d29-38a6-a427-7c678f39c97b | -2.65602 | -54.08633 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 387e7d92-3872-3be8-a7d9-be2f36b6fb26 | -3.11365 | -53.98358 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 804c2903-9dc8-3f7d-9344-db0e414dd9aa | -1.56393 | -55.33326 | 2024-12-02 06:03:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7dbbc695-b9a9-3362-813a-5179f01bbbe2 | 1.00327 | -59.4649 | 2024-12-02 06:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42650c6a-1fde-37b7-92d3-6307740fba6a | 1.11822 | -55.99526 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12f79491-14cf-37c8-8d4a-8d48d95af827 | 1.09303 | -56.02176 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| faf68343-24db-383b-b9d6-760379c97997 | 1.09682 | -56.00819 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59880d0f-1666-3368-8c05-ce15898af885 | 1.09183 | -56.0146 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 21c7d661-7e21-3d18-ab40-0be5dc269ffb | 0.90616 | -59.44803 | 2024-12-02 06:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f5f5ea7-fe65-3aba-a215-05a3f8c183b7 | 0.91365 | -59.44874 | 2024-12-02 06:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71540ca6-bc7b-3f45-8340-9a3c92b4fc5b | 1.1303 | -55.97869 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfe42117-4a9c-3e1c-a589-a51dadd02853 | 1.12424 | -55.98686 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7acedb67-9ede-3572-a22b-f06e759fb32f | 1.21203 | -56.01065 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d559caa-7083-30a4-b7f1-f8f4fd15c141 | 3.18663 | -60.1832 | 2024-12-02 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aa03345-eac7-359b-be01-3fa31115967c | 1.10401 | -56.00692 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcf9bc65-4af6-30d2-94e0-c98d0fc6f38a | 0.9078 | -59.44982 | 2024-12-02 06:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 865ffe79-d52a-3eb3-ac9b-86c52e77d00a | 0.91199 | -59.44684 | 2024-12-02 06:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 248a3c82-2977-3ce3-9bed-e262c07f4b63 | 3.18182 | -60.1875 | 2024-12-02 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50c4e715-831a-3651-9ae9-9e10efc87bd2 | 0.86152 | -59.68377 | 2024-12-02 06:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93687424-1be1-3bb8-98e5-4dee4f680187 | 1.11702 | -55.98803 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b75f0be8-a735-37ea-9701-f7881477fc3c | 1.13748 | -55.97728 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01094873-69cb-3444-be82-3a1fb24e382b | 1.09076 | -56.01654 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fc4dd5b9-5571-3400-9450-beefa208d0c3 | 0.64981 | -59.65833 | 2024-12-02 06:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 711c829f-606c-3edc-940e-2867ed34be29 | 1.13145 | -55.98567 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b4673d9a-dd09-36f4-84ae-e3485b092918 | 3.18721 | -60.18664 | 2024-12-02 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13863adc-3726-3b6f-8982-0d9f63c514b4 | 1.09904 | -56.01346 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d339246e-a227-3b0b-be31-cb3d11603d0e | 1.20608 | -56.01926 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3353ecb7-f604-372f-9fda-e22520479030 | 1.1435 | -55.96883 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65c868a1-36c4-3a33-9be4-6968fc789ad1 | 1.09797 | -56.01536 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2f494154-e79c-3dcb-a041-8de62bc9c2b0 | 1.11004 | -55.99834 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbb2d97f-fd40-35ff-a90b-2b16ecbf3500 | 1.11102 | -55.99648 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5651b67-5463-3466-8dc4-521539ad9f94 | 1.09193 | -56.02375 | 2024-12-02 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 34b7b198-6ab7-3ba4-b327-335a7c43f49d | 1.00395 | -59.46901 | 2024-12-02 06:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| deb3de7c-21d7-3c34-a832-73706e03d415 | -13.5011 | -61.52471 | 2024-12-02 06:07:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eca79360-6f26-3f16-b5d3-941a923183f1 | -15.06816 | -59.64631 | 2024-12-02 06:07:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d31cfe31-902e-3f33-b47b-d219d94bf8d8 | -9.3476 | -58.22272 | 2024-12-02 06:07:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7d995bbe-4215-3810-a893-2ebe64ebcb2e | -15.08928 | -59.63007 | 2024-12-02 06:07:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 46c6c904-ff09-321a-90d2-3c248260a377 | -12.26839 | -64.3345 | 2024-12-02 06:07:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 467871b4-cbc7-3744-b6c0-b2fb6f92b58d | -12.25103 | -63.46321 | 2024-12-02 06:07:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f04173ac-c266-394c-bc2c-f662d0c4bfa8 | -9.88559 | -66.73447 | 2024-12-02 06:07:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3122d691-d851-3c84-81f0-bbac6d9bc501 | -9.29152 | -64.24696 | 2024-12-02 06:07:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2358d52-1cd8-3e91-a3dc-0e0e0bbffdca | -12.26876 | -64.33146 | 2024-12-02 06:07:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be3ffb2e-6d3e-3d5f-a069-af8cb6632911 | -12.25071 | -63.46061 | 2024-12-02 06:07:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d2b8e04-6780-39ae-9d9b-a02f9af26d68 | -12.25145 | -63.45964 | 2024-12-02 06:07:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 274a8c76-3034-34d9-a548-1d45d0cafeab | -13.50271 | -61.53027 | 2024-12-02 06:07:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c0cb5c6-bdcc-3d86-8cf1-380fd02f0005 | -12.25649 | -63.46382 | 2024-12-02 06:07:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9afd3da9-aa9c-3b89-9c90-5bc11f871cb0 | -13.50215 | -61.53524 | 2024-12-02 06:07:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a8db6fe-d2f4-3a11-9b28-bbf7deb6d075 | -12.25027 | -63.46417 | 2024-12-02 06:07:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cd05d956-6242-3432-a63f-432b44588b9b | -2.8197 | -53.0425 | 2024-12-02 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 495cdc41-de57-3943-9990-51ee942a3a30 | -3.2591 | -53.6186 | 2024-12-02 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 2e435d6d-c79a-31a6-ae04-7703a16edfc2 | -2.8013 | -53.043 | 2024-12-02 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 48cabf47-80f2-3331-bb58-f23269d10a3c | -5.5882 | -45.1412 | 2024-12-02 06:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a6dcbc2a-9b77-3b5b-aa6d-20b84a896f00 | -5.5882 | -45.1412 | 2024-12-02 06:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 2b18688d-4117-3383-a93a-91cc68a9f50e | -3.2591 | -53.6186 | 2024-12-02 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 84c7d5f9-8e3f-36d4-b624-5bac3aef3df5 | -3.259 | -53.6388 | 2024-12-02 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 17b5d233-006f-3946-a75f-bc5e72a1d0df | -5.5882 | -45.1412 | 2024-12-02 06:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 4b29cb6d-7311-34e4-8d09-3a95a5b67919 | -3.2591 | -53.6186 | 2024-12-02 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 70b9668c-42c3-356f-a341-935542422f11 | -5.5882 | -45.1412 | 2024-12-02 06:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| bb582927-5b3e-3480-9c4a-ab6fadc24727 | -3.2591 | -53.6186 | 2024-12-02 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8cd828c8-09ba-319f-901f-ce1b2d1a3136 | -2.8013 | -53.043 | 2024-12-02 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| aeb4586e-54d3-3ef6-a480-6b72f125dd07 | -5.5882 | -45.1412 | 2024-12-02 06:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 1a9d82e5-ab97-399c-b6cd-86ccad6fd3fa | -3.259 | -53.6388 | 2024-12-02 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 4a5b164b-2284-3ceb-96e3-0ca0716409bb | -3.2591 | -53.6186 | 2024-12-02 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 96f85819-e957-38fc-ba59-dd8a674cebbf | -2.8013 | -53.043 | 2024-12-02 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 592f528e-9890-391d-8399-f99c0b082bce | -5.5882 | -45.1412 | 2024-12-02 07:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 84c61206-77d7-3ec3-908b-57a7d71383e6 | -3.2591 | -53.6186 | 2024-12-02 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f9f56782-7ed7-3202-9f5f-efb6c0982c36 | -3.2591 | -53.6186 | 2024-12-02 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 06006585-1ef1-358b-8203-385c889e34ce | -3.2211 | -45.2024 | 2024-12-02 07:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 3ff2212c-0f92-3da4-afcd-1aaf9ab07188 | -3.2211 | -45.2024 | 2024-12-02 07:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |


[Clique aqui para ver as próximas entradas](README77.md)
