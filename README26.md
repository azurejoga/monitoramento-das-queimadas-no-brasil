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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92f60fd2-9c84-31ca-8b51-5b994cc831ff | -6.82356 | -39.30838 | 2026-10-06 04:19:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ba6d3773-42b1-36fc-9fce-fa6b09841b52 | -10.97134 | -45.41446 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 847de494-3c41-3a9a-87f8-4c8fa19fe517 | -5.8382 | -45.01558 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 5022ce0b-8b3c-3cff-86d2-650280fc82f4 | -7.24725 | -45.25983 | 2026-10-06 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0fc0e80-5d47-3234-8866-80cb56fdf912 | -7.47819 | -42.81241 | 2026-10-06 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2f9bd64-9ffe-376c-8644-5d0cf0de9649 | -3.09283 | -54.16047 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2a73828-d768-3727-abe6-68d2d8e99fdb | -6.85524 | -41.79688 | 2026-10-06 04:19:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ced53864-4e99-3b80-83be-3c99983e5f51 | -11.26878 | -45.52625 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 295f27e6-1d92-3304-b593-a15e5699f5fd | -6.17384 | -44.28771 | 2026-10-06 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cc85b0b-ed1d-3449-bcd0-457a8db98170 | -3.10715 | -53.76402 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a4c6d96-75ac-3b58-a549-2d163dadb530 | -5.67177 | -53.49922 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| daf9306c-7284-3e34-90e0-7747d4385b5d | -5.8352 | -45.01048 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 7b6eecca-6c9b-3cea-b102-8e8a763204b9 | -3.27055 | -50.40153 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b7b6715-27ea-32df-8533-1a723c49a813 | -2.78634 | -51.66804 | 2026-10-06 04:19:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4587f71f-3ca4-3560-880f-7b25de6dfd5d | -11.27381 | -45.52555 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| bfe0e5d9-e123-3661-aa21-0095a4af09a2 | -3.2346 | -53.88292 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a4f7848-f7c7-327d-97c7-ac27d419b663 | -8.70416 | -45.21169 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2126c2f-dc98-3bb5-8eb3-4d294141c78a | -5.68584 | -53.49551 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9c31dd4-fd85-323e-8de3-708c853ec486 | -11.23222 | -45.26351 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c68bebf-db7c-35e4-bcdf-b763ad1fdf23 | -3.46733 | -50.10728 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 878615a3-ce74-376d-b03f-5080bde8d712 | -4.29124 | -54.80707 | 2026-10-06 04:19:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6424a088-cc75-3942-8f8b-c696c1b30c21 | -11.64232 | -43.6548 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 981d77e3-8077-3f53-a895-e31369b89e55 | -4.2559 | -50.79867 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dc8f3e7-6be2-35ad-81e7-45ead09fec54 | -3.80412 | -49.11245 | 2026-10-06 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d47aa8ac-d540-30de-9dc9-37a22e4b250b | -7.87946 | -44.19106 | 2026-10-06 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77ec6b10-d3bb-360f-a500-42137707de50 | -5.41222 | -44.35126 | 2026-10-06 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0465000c-aee1-3602-bdfd-a8f898b5e34c | -6.89842 | -43.67696 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3841ef7-d8cc-3dbf-b53d-e470053c98c1 | -6.34875 | -45.81436 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48931870-c370-34fc-9545-f3f3e04f9e0c | -6.35952 | -42.54192 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c2d6e2af-c5ea-30b6-8592-9875e80334ed | -3.2219 | -53.87426 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95c05351-1140-381e-9ff9-9fb8188aae98 | -2.78439 | -51.67527 | 2026-10-06 04:19:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c59fac49-3f90-3036-9f83-ce54caf63e40 | -4.06079 | -54.04913 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab6b400a-072c-38c1-ae40-f29f6912368e | -2.87945 | -54.12921 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 674ac829-8b78-31e3-8b5b-3a0c81a446f0 | -2.77333 | -54.09137 | 2026-10-06 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad30a219-1473-3cec-b635-398fc8b9f5c7 | -7.47597 | -42.80472 | 2026-10-06 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6a9d6093-6fed-3ea7-b756-d7ff85027ce1 | -11.63251 | -43.60902 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ca04f6c-597d-35da-8312-c8e61aad061d | -5.08972 | -46.04442 | 2026-10-06 04:19:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22125a84-7fb6-3e0a-b805-3430f49b6e56 | -3.0022 | -54.13045 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fb9834f2-8d5b-385d-8ff5-2ce173266a18 | -4.36061 | -47.78056 | 2026-10-06 04:19:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4b156d90-d416-39e1-baf8-8eed697c832b | -6.31742 | -43.34209 | 2026-10-06 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61a02a52-d460-344f-81ea-c7e24fab7ffc | -3.07962 | -54.25542 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8fe0111e-6579-34f8-9ee4-2d4e09f20a84 | -6.59341 | -41.57316 | 2026-10-06 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 13b78448-ab7d-39b7-b098-6e973391f464 | -11.28451 | -45.50618 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 6af5737e-1c99-33d0-b0b0-b79a005e3daf | -3.07234 | -54.17118 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9dd6864b-6e09-3160-93e2-ad31a9a0f431 | -9.8167 | -44.7897 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94b448ff-cd00-31db-9e5f-aaa9bc58bc01 | -4.26619 | -48.6269 | 2026-10-06 04:19:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6abb5d45-0523-3e37-9329-a933bfd9e5cc | -3.04905 | -54.22203 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 907c2123-6a0e-3da6-89c0-9243bb46adc0 | -3.0749 | -54.24061 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1befc4d-1001-342a-9f52-b2e7b0986b2e | -6.18784 | -44.85976 | 2026-10-06 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17ad0d66-b48b-319c-87f0-02db135c0276 | -10.98359 | -45.45067 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72db8d12-41ad-3651-8bf8-165e3f0e88cc | -3.07627 | -54.25346 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 005e5572-64e0-3547-b972-49fe912b8614 | -3.10825 | -53.75771 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df3172fa-e76b-385e-87a6-d54048ab8be2 | -2.8786 | -54.15219 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dfb3c86d-f05f-3794-8313-cf3b76a92389 | -11.28228 | -45.51158 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 376a610c-735c-3e4e-8e17-9e1ca9bc87e2 | -11.28093 | -45.50554 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| c3c14fd0-b8f7-3eaa-a721-77c3829c59de | -6.19153 | -44.86034 | 2026-10-06 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dbc90902-9bef-3898-8c61-0e2a9c4f78ee | -5.9762 | -41.32587 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a6ce15ab-fa29-367c-831d-89eb3369e9c3 | -7.48384 | -42.79869 | 2026-10-06 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 79f026b9-7fb4-37aa-88fb-399d5f778f70 | -6.93617 | -43.67541 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e764c889-437b-3180-830e-fb4ec25efbb9 | -6.36001 | -43.29089 | 2026-10-06 04:19:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5441e65-c91d-377d-8db5-92a7fadb9ae3 | -5.43444 | -43.4476 | 2026-10-06 04:19:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1e8a712-c280-30c3-aaac-9b3be751ad09 | -6.17557 | -44.28935 | 2026-10-06 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8bd9764-30ce-3946-9880-f6119836a082 | -3.10248 | -53.75028 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9a5d455-9c39-3a78-a63b-2f3e8ad2b39c | -6.92514 | -43.67754 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 260c6109-9f93-3054-8521-a3238737523e | -7.09159 | -42.54244 | 2026-10-06 04:19:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10cc4c6e-eaaa-3e39-8f4e-9696b8e62a9e | -10.36475 | -45.03388 | 2026-10-06 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22251373-e98f-3de5-89d5-9707282e6632 | -11.27735 | -45.50491 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 19f8a9e0-8979-3e43-b405-094ad3789228 | -5.84914 | -45.02445 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| cae1fee0-0416-3479-8916-22318e1a25d4 | 2.4558 | -50.84864 | 2026-10-06 04:19:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da1104b9-ee73-3451-891e-e67c1b6311eb | -2.87123 | -54.1347 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53f52415-bcf5-3efe-ac04-75ebf7c9227d | -2.95657 | -54.14354 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1099eeed-6215-3911-aa7c-52fd29f8ba5f | -7.38207 | -39.63667 | 2026-10-06 04:19:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b8e76045-4df5-3534-a09a-4dafed6de046 | -10.49678 | -44.41696 | 2026-10-06 04:19:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d19db9e-013e-37bc-9824-f8c85a64cdfe | -7.10558 | -42.54107 | 2026-10-06 04:19:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aa225da6-f31f-3055-9c14-82de6beb9639 | -4.45676 | -54.97713 | 2026-10-06 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2b7b28a0-14e2-345e-96e8-d77b456ec4ca | -2.78004 | -54.10948 | 2026-10-06 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88afac4f-5e54-3324-9eb3-58e05c4c5c24 | -11.28006 | -45.5027 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 31629072-820b-3562-bcd3-100ef747e679 | -9.7731 | -44.79169 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bf36ece-59bf-378e-aa78-886ef25c2d9d | -2.98108 | -54.12724 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1c67162f-dc9e-3f89-98d2-f3906824b15a | -11.28022 | -45.52398 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 370e48d2-bf39-33be-8d36-58acfec04ce8 | -2.8693 | -54.16419 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2912fef8-d548-3900-a4db-12f88cb06189 | -10.94375 | -45.39309 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc794c7d-20fd-32f3-8ceb-16bf19b19ba9 | -11.2809 | -45.51984 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| e6efdbe7-8ffa-38d7-b3bc-cd68a5ad2343 | -6.37298 | -42.54409 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6dd170a8-baf6-3596-8e6a-09efa466cef4 | -3.27549 | -50.40611 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2594bb94-9a5a-31c9-be9e-ce9dabfbd12e | -6.81433 | -39.29899 | 2026-10-06 04:19:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 534feb97-638d-38c1-82cb-ccde8944f893 | -5.6845 | -53.49939 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b3aacb1-a2a8-33a1-8396-460fb098d1c4 | -5.46882 | -41.24203 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 38e274d2-2cfc-38c8-a8f9-ffbe4da23156 | -4.28896 | -54.80887 | 2026-10-06 04:19:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2cc06e8a-279e-3b66-ac4f-1a5d3c62a364 | -6.49203 | -41.71726 | 2026-10-06 04:19:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3773a5df-c6a4-384f-8f6b-78b25fe6b0e6 | -3.28165 | -50.40347 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b9c9e94-8270-3128-8eb0-cea3c6e5ae35 | -3.07165 | -54.23858 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93734d3c-6479-3623-b026-0208258b48de | -6.92675 | -43.67777 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b4d041c5-d17a-3537-8247-6800c4d0300e | -6.92923 | -43.67431 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e63c8eaa-0edb-3ab1-b933-986d30bb31b0 | -2.9496 | -54.14203 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff293d03-02f5-3114-8bd7-676c58ef0505 | -3.73639 | -48.87815 | 2026-10-06 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2eddc67c-6608-3d28-8815-d2cbf078f1c6 | -3.05725 | -54.21659 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8bd2b765-6bb5-3a71-993f-8ee850d21da3 | -6.85801 | -41.8009 | 2026-10-06 04:19:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 71dc5a18-1fb8-3951-a317-d827faacc1a5 | -11.2781 | -45.52205 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 7ebabb1b-243c-33bb-955d-9e7e3e333d79 | -3.08705 | -53.71444 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README27.md)
