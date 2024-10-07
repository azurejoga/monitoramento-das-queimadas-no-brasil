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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7c7d99b-9659-3ae0-80dc-13ad972b44e3 | -21.08073 | -47.22842 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 700627bb-1290-3614-95f5-2f114d469424 | -21.07872 | -47.23766 | 2024-10-07 03:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54760f93-2898-3557-9455-a34e75ac62d9 | -21.07726 | -47.23973 | 2024-10-07 03:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4a6c522-142e-3d2a-a140-0f9105d629b4 | -21.07524 | -47.22724 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0d731a6-dd66-348b-9084-55b3f6a642c6 | -21.07387 | -47.22921 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2eeba10d-05f5-3cb5-86be-5af33a894488 | -21.07158 | -47.24401 | 2024-10-07 03:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36d80909-004e-3db6-b003-06ae5a90b59d | -21.06893 | -47.22981 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a46d43b5-3b99-350d-a89b-50de509e9465 | -21.06815 | -47.23335 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 034cdb3b-e8d1-39d4-8c41-bd56fd863e38 | -21.06737 | -47.23693 | 2024-10-07 03:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a21c2faf-02ac-3928-b007-b68b42e8a6c1 | -21.06639 | -47.24141 | 2024-10-07 03:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 184e2fb3-3be1-3e8b-920b-97788b8d1278 | -21.59907 | -47.72778 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f9a5098-3a9e-3ada-99a8-cc506d37c8a2 | -21.59814 | -47.73191 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cb4e2fd-63e6-31a3-86d0-dc49b932759c | -21.59721 | -47.73613 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0aa5f70d-26e6-3012-9c9f-0e3099f7cb9e | -21.59632 | -47.71378 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a0f562f5-a71d-36b5-a65c-b35f26d7bd7c | -21.59462 | -47.72136 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dea16322-595b-3f43-854b-6a732b6e4c88 | -21.59366 | -47.72566 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 179dc7f5-98e9-324c-b0e6-ce13a81d25aa | -21.59268 | -47.73008 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ca1e5a0f-da4e-3f05-901c-fa8bfedeb1f8 | -21.59091 | -47.71172 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b4cbca4-f789-3b66-ab4d-403b85414e99 | -21.58923 | -47.71922 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d03a1fb3-1245-3dcf-ae12-a97088cc7783 | -21.5818 | -47.72616 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b3631bf-cb37-32ae-a11b-a5c6d6f7c3b4 | -21.57736 | -47.71977 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2a53274-626e-3eac-9e90-2226f8e291bc | -21.57534 | -47.72879 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7207b360-0af3-3af6-9767-a28aa1c4a1bc | -21.56771 | -47.7366 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ca56c1c0-5dbf-3b64-9beb-d4a6b162b28f | -21.56316 | -47.73067 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5f2ede97-011c-3167-b70e-8743ef204eb2 | -21.35506 | -47.66361 | 2024-10-07 03:40:00 | NPP-375D | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f4ff24b-5ec1-3b20-a6c5-0c8a3e148cfe | -21.32414 | -47.60319 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0fba5b07-a874-3494-a7e5-7bddfe7e9a97 | -21.31685 | -47.60966 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 85fc81c9-c05d-3fc9-85ba-62b6c46601ce | -21.31585 | -47.61422 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 90469167-edae-3321-95de-c4948ef344c8 | -21.31336 | -47.59894 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d31723f-6398-37ba-b405-700848ec86d5 | -21.66549 | -47.73197 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f11cffeb-5e9e-3e3f-84f2-118065474858 | -21.66461 | -47.73587 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e019291d-28a5-324f-b1e1-3f23a5a1bbc3 | -21.66 | -47.73028 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 318cc085-0eda-3be2-8ffe-0d9e3a7f3b87 | -21.6591 | -47.73428 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ac12ab8-9bce-3941-be82-b124bc208c52 | -21.65547 | -47.72436 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| efd0a6ee-5187-3a2a-9bca-ac79967d3997 | -21.65455 | -47.72844 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01276f73-9c37-37c9-8129-a820ba5b0bcc | -21.65362 | -47.73253 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 698678fe-9f66-3f6f-8724-adbae9cf994d | -21.65 | -47.72262 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f747de2-de52-3760-b698-36a4097220c7 | -21.64909 | -47.72663 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59323335-f9ce-3de7-a5db-83e1b811f4ea | -21.64817 | -47.73066 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 300c90be-4e9c-376a-8238-e6c6779cfdf2 | -21.64725 | -47.73474 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94af9b0f-4ae1-3a18-a87c-0ba05d31d06c | -21.64449 | -47.72105 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cff94464-38e2-3def-8a2e-ecb262809f34 | -21.64357 | -47.72504 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ba196e5-f8a0-3f30-897e-27cf8ec1b9f7 | -21.64265 | -47.72912 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b79b23d-ec70-3813-ade8-f235cfce5d9c | -21.6414 | -47.7221 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7d0bb1c-620c-3b6a-abf1-5e27299b9ebc | -21.6405 | -47.72616 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f839cec7-e68b-32cb-b5c9-e9ca50444aaf | -21.63891 | -47.71976 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d607b8a3-8c49-3dfd-a27f-38618cb696dc | -21.63799 | -47.72377 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a1c003f-ee10-38e9-b4ee-bdd90847d12b | -21.63581 | -47.72087 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9341cf7-8aae-3792-afba-7042ead83f6a | -21.63331 | -47.71857 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b37cbe6-a43e-3eec-824a-92c6b1980e76 | -21.60621 | -47.72206 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07f4f61d-94d8-3c20-8a3a-0eb217323a08 | -21.60082 | -47.71992 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d923ce24-60d0-3e8b-88bc-e83e67e83f58 | -21.59171 | -47.70815 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7299b6a4-7a71-34d7-b588-a237686466e5 | -21.58827 | -47.7235 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 58c7d317-5cb9-3e9e-95d4-3fff2d192ec6 | -21.58623 | -47.73263 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 5f6245de-d58c-352d-ac3d-f2188142d9f7 | -21.58285 | -47.72147 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82985d62-dcc8-311c-aacf-4dd9bd4ddec3 | -21.57978 | -47.73518 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d65f893a-56ef-314a-a25b-9c2b88544c56 | -21.57429 | -47.73348 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 88c811d9-b27f-3394-ac1d-b1af0a093b54 | -21.56986 | -47.72701 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f82ee4ac-ef2a-3764-9ae2-487051a31592 | -21.55853 | -47.72512 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a9ef500-3e6a-3737-a65d-dc53fcc10862 | -21.55759 | -47.72926 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 00b0a507-93d4-3090-8028-6964dfc23427 | -21.35597 | -47.65957 | 2024-10-07 03:40:00 | NPP-375D | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3218b18e-54f2-3293-be60-3bc992491969 | -21.32321 | -47.60741 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a289549c-aadd-307f-b7a8-c140aba0b7f7 | -21.3198 | -47.61181 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c25bda34-ca78-3604-a307-f08f978b5453 | -21.31639 | -47.60102 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c5df7671-1361-3a35-9175-958da426faaf | -21.31549 | -47.60498 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 900b345f-e445-3e1a-82b9-2af8bd151c00 | -21.3144 | -47.60975 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 90342538-e484-3080-ba17-33071b7d7e56 | -21.31253 | -47.60268 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 158aaf6a-cae6-375a-b0e0-d3d05aa31b0b | -21.08025 | -47.22646 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 326a87d6-3aaf-3b46-ba2f-3298d51c9a8a | -21.07972 | -47.23304 | 2024-10-07 03:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1a81d7e-169a-3dcf-9718-f7a4fbd16f85 | -21.07778 | -47.24197 | 2024-10-07 03:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8582db67-3fd4-3183-843f-fb0deb8b378c | -21.07353 | -47.23504 | 2024-10-07 03:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bef65ebb-a364-3a82-89f3-3283e06e81d2 | -21.07301 | -47.23305 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba34782f-d92b-3480-ba93-adf57fb46429 | -21.07263 | -47.23922 | 2024-10-07 03:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 859aba55-876d-36d1-85d7-2e963983eec8 | -21.0711 | -47.2415 | 2024-10-07 03:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dc377900-1490-3c6e-a062-2d86f1699a1d | -21.28329 | -47.39423 | 2024-10-07 03:40:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2931436a-4f49-355e-a0c9-568beee6bfb5 | -21.27876 | -47.39518 | 2024-10-07 03:40:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3dd179b0-f043-38a2-a7d1-b204c91a4070 | -21.07928 | -47.23076 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7ea4894-b8f2-3895-aa8a-07db41ff079b | -21.07824 | -47.23537 | 2024-10-07 03:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0edf73cf-4883-3572-ae75-2e39ec441e86 | -21.07439 | -47.2311 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c22e195-7f49-3b5f-8ade-b285530aaac6 | -21.07213 | -47.23694 | 2024-10-07 03:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf00149d-ebec-3748-92f0-5530b840cb93 | -21.58988 | -47.95525 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dedac617-91a6-3046-ba5a-122a6825c8a5 | -21.58866 | -47.93973 | 2024-10-07 03:40:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce963a82-4110-34f6-8c23-9c559c3889e1 | -21.58491 | -47.95609 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 65577305-dc6b-3757-9955-a4a808c616ea | -21.58434 | -47.74111 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 39fa900a-d430-31d8-9f87-0f4faac68600 | -21.57743 | -47.93677 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93de5261-dc34-3baf-a7ff-7ef27991a135 | -21.57669 | -47.93427 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42b43d9e-1bda-3164-9398-56d4e0da051b | -21.57324 | -47.73816 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c904d7dd-b301-3f00-9095-c9a0360440b8 | -21.57275 | -47.93121 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 392ac2f1-9e61-31cd-bf70-a425c6381082 | -21.56943 | -47.75512 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 939aa6ad-6d9d-3e54-ac35-8f2019f7a2dd | -21.56762 | -47.76319 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3ea1318f-de8c-375a-93a6-2580e3f39ab0 | -21.56671 | -47.74102 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d3b6cefa-1a12-32d8-8713-b57af5089a2b | -21.56574 | -47.74535 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24728ce6-cb8d-3e86-969c-80a5fb7e148e | -21.65182 | -47.74048 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da93ec6e-24c1-3a56-9b68-832de825d3d6 | -21.59613 | -47.95916 | 2024-10-07 03:40:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9d133831-28b5-3bdd-9119-89d18bd35996 | -21.5924 | -47.94944 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bd13eda-f0de-3a2d-87b4-658f2c31a74a | -21.59078 | -47.73858 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 289849ac-6e9d-3e4b-bc91-fa02a406b032 | -21.58585 | -47.95201 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ae03a629-ca39-3234-89ac-3ea9902c1d83 | -21.58429 | -47.95363 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eec85b91-8915-3cee-a871-cc1bad6dcefc | -21.58339 | -47.74534 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96fa614e-bb02-35f6-89e6-25c83cef6003 | -21.58139 | -47.93988 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README51.md)
