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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b409b35-92fd-3623-912d-ffbfc4283da9 | -12.94605 | -46.64606 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f9684445-8283-3fda-96eb-c33bebe675f6 | -15.45287 | -49.07729 | 2026-09-29 04:17:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dccadc9d-7379-3252-9749-47b42be4903f | -13.34014 | -46.81581 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d9ed6335-dbc7-3e24-9510-7b02ad08b472 | -12.04093 | -50.95316 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c9e70ff-b111-33b1-bf0e-f9606de0aab2 | -9.28937 | -49.64525 | 2026-09-29 04:17:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e612ab3f-ce2a-3291-92e0-82745fd6acc8 | -18.87413 | -46.66812 | 2026-09-29 04:19:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5579402-0087-3087-a430-7ca13206e5ed | -18.10934 | -44.3583 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6b287e1-cac6-3912-aaa1-6a847bca5c9a | -17.86896 | -48.61478 | 2026-09-29 04:19:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90e6249b-1c48-3b3f-b63f-f1cc5f1c9e34 | -17.62215 | -46.66502 | 2026-09-29 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5cf276f3-186a-305c-bc8b-6baa70bacfd4 | -18.56336 | -48.4218 | 2026-09-29 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 88315232-f21a-3613-a479-26fa724a6e51 | -18.10313 | -44.3534 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9cd90131-64cf-32b4-8663-9fd5893f34e6 | -17.60538 | -43.71039 | 2026-09-29 04:19:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8dd9636-8f4f-3f9c-bffa-d8a44bc6257b | -19.36503 | -41.50338 | 2026-09-29 04:19:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b307b6ce-180f-3583-9775-86affb4b4764 | -18.08568 | -44.37807 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47e0f61d-cb12-338a-b7d9-c093e96b195e | -17.78425 | -44.37748 | 2026-09-29 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9049da7-850d-3097-8381-3b627e55dda3 | -16.76054 | -47.07 | 2026-09-29 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8df758d-cfd2-3268-9eca-cd65ada9143b | -17.5528 | -46.5452 | 2026-09-29 04:19:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfdc5c5c-360c-35c7-ab4f-98bc7acec55e | -18.6874 | -48.63 | 2026-09-29 04:19:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74521701-e4ea-392f-97e6-959628af81e2 | -18.10222 | -47.89818 | 2026-09-29 04:19:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d90e9991-e962-352d-b684-70544169b951 | -19.18631 | -45.2206 | 2026-09-29 04:19:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afe51d66-d049-31cb-adcb-2f1c76da7631 | -17.61167 | -43.71553 | 2026-09-29 04:19:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65dbf04e-fa30-34f0-8cec-64eb9adaa3b2 | -17.61073 | -43.71886 | 2026-09-29 04:19:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d9ccc8f-2b28-3188-83f0-81a80b564124 | -18.08401 | -44.38942 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7613659d-f70c-376e-88a9-ee961836abd3 | -18.40194 | -42.31367 | 2026-09-29 04:19:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| ae129b69-0555-3c2c-b3a9-963dfae16ac7 | -18.49656 | -45.13073 | 2026-09-29 04:19:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| faf8f364-3f6e-3522-997c-a84dc336d29f | -18.49045 | -45.12597 | 2026-09-29 04:19:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a015b0c-d072-31a2-aa49-e962688af5a8 | -17.90944 | -45.03903 | 2026-09-29 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 475e93c7-79a5-3c04-b543-ffc47a93860c | -18.68045 | -48.62876 | 2026-09-29 04:19:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51d7f6b2-801b-35d5-a766-2e778dd13075 | -19.65978 | -41.72831 | 2026-09-29 04:19:00 | NOAA-21 | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fb5d1a76-9c01-3cef-832e-f212ae5a1553 | -18.11272 | -44.35884 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a652d9b6-fea2-3583-b3af-30b767128999 | -17.9815 | -44.48912 | 2026-09-29 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f304991-dfe8-37a6-a000-68cacc6f2fe8 | -17.80734 | -44.43114 | 2026-09-29 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e41f91a0-e99c-35dd-914a-47c344916f7d | -16.81786 | -48.99646 | 2026-09-29 04:19:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ef33ae6-b212-3bc7-8332-b3aca0bb37a7 | -18.48748 | -45.12613 | 2026-09-29 04:19:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3391709d-ef4d-3aff-bd6a-0c364271ec6c | -16.75994 | -47.0737 | 2026-09-29 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96435f22-843b-36cd-ba82-8980b5f4ae8e | -19.15676 | -43.81905 | 2026-09-29 04:19:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d56fc90-a0d9-353c-b208-0f8c3c56b7da | -19.36897 | -41.5038 | 2026-09-29 04:19:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| db290e18-bfad-38e1-90a3-9c0b33756824 | -17.59791 | -43.71335 | 2026-09-29 04:19:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6498699d-c44c-326f-b8c4-d85c95f341b1 | -18.6846 | -48.62537 | 2026-09-29 04:19:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcfd0381-26c3-3048-b04c-ff672403aa6e | -18.48803 | -45.12247 | 2026-09-29 04:19:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af96e214-1272-3375-9438-08f3489e24b5 | -18.27073 | -42.20503 | 2026-09-29 04:19:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fc8de893-8b8b-3402-96ff-fc8bf325b979 | -18.1099 | -44.35445 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75538b23-ccf1-33c5-b237-2cb31b66ae50 | -17.77575 | -43.00799 | 2026-09-29 04:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68fc0937-7707-3b4a-890c-8b1de20022b9 | -18.16621 | -48.02065 | 2026-09-29 04:19:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 399b0659-3304-3efc-a22f-71b3f68ad597 | -19.53808 | -42.9265 | 2026-09-29 04:19:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.6 |
| 4d54d7d6-2d96-3fe4-8edd-7d64b36ce9b9 | -18.11611 | -44.35936 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 129345fc-9c03-3d4c-aec2-5e39521fa33e | -23.00965 | -48.61912 | 2026-09-29 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b04cccf9-07c1-3454-a852-d3b072861494 | -18.10708 | -44.35007 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb7bba45-edd7-36af-b845-1623207e85c8 | -19.46687 | -40.89426 | 2026-09-29 04:19:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0f380b57-5735-3c92-beb0-c65f8987fb3f | -19.5411 | -42.9315 | 2026-09-29 04:19:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c5d90e07-19a4-3732-8b23-666cdc033d2b | -18.76829 | -47.61673 | 2026-09-29 04:19:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19dfd6f4-dca6-303f-b0a3-592e4d96b54e | -18.11329 | -44.35498 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cd08c0c-7f79-3510-98b3-fd1aabf6e11d | -16.69852 | -51.83681 | 2026-09-29 04:19:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e931b98-7198-365f-9f0e-4f4f8a31f20b | -17.82751 | -44.38841 | 2026-09-29 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34d094e8-ad62-3d46-a05c-6f5360f8188e | -17.80397 | -44.43061 | 2026-09-29 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a45c8853-d7a8-3e23-9301-dfee32289166 | -23.00901 | -48.62298 | 2026-09-29 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27699e03-a83f-3cea-9228-c389c1d32c6f | -18.08909 | -44.40191 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a94e5f59-7bfc-3bd6-9d09-1a25c2fe876f | -18.56681 | -48.42244 | 2026-09-29 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a2c9babe-b957-3ff0-80aa-ca638f2cac8e | -18.57503 | -48.41575 | 2026-09-29 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a5c24175-f362-3755-8946-1a68e04b3b0b | -18.11047 | -44.35059 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 098d5bae-f3b6-33d2-98ef-c2de2e491b38 | -19.54171 | -42.92701 | 2026-09-29 04:19:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 855991fe-cad1-33a4-a8b0-c205abeba7c5 | -18.56957 | -48.4271 | 2026-09-29 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8ef0cbdc-45cc-3ec0-b144-02a946bcc4b2 | -18.68113 | -48.62474 | 2026-09-29 04:19:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc2c8222-d0a7-329a-8954-c01164801b93 | -18.57025 | -48.42307 | 2026-09-29 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2d108aed-86a6-35c8-ad86-ac9769351493 | -18.36457 | -44.57939 | 2026-09-29 04:19:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 793ca935-101e-3496-b71b-48f16c946602 | -15.63647 | -52.6938 | 2026-09-29 04:19:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 43ce293f-dbd4-3613-81ec-fe4e5291ea4b | -18.57437 | -48.41972 | 2026-09-29 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 37bf0767-c1ad-3db7-ad7d-44694c3359d2 | -18.84988 | -41.99558 | 2026-09-29 04:19:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e9756bb6-0de5-36e0-a31e-37c77bf2bd41 | -17.80506 | -43.8292 | 2026-09-29 04:19:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 893b137e-31de-389f-97b3-852f9e114cbf | -18.1628 | -48.02002 | 2026-09-29 04:19:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a358173a-7bc3-3d35-b3b9-97d9cd53725d | -18.10993 | -44.40123 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b414e203-3d53-36d6-94bc-daf1e0fc0682 | -18.11332 | -44.40169 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94ed437f-5bab-34a9-b400-04a357b9dd96 | -18.10802 | -42.63732 | 2026-09-29 04:19:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8a0da58b-89dc-328a-b7a7-7b00caf10a54 | -17.25993 | -48.28325 | 2026-09-29 04:19:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98dbca59-c920-3941-8dea-794d5b63f248 | -19.07056 | -46.28463 | 2026-09-29 04:19:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15950a65-535a-3d41-bfa9-9d33c4d422ae | -18.39409 | -43.43542 | 2026-09-29 04:19:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e7311bbc-5eed-3d19-a011-7381d72ae787 | -17.84116 | -46.72175 | 2026-09-29 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76884b3b-a1d5-3bab-94f3-44b7184ad265 | -18.76494 | -47.61612 | 2026-09-29 04:19:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ccd16a4-f4a6-3b22-94ac-626a567097b3 | -23.00566 | -48.62232 | 2026-09-29 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 900af648-b9e5-3f0f-bfbb-f4fb5e195dbb | -16.69776 | -51.8408 | 2026-09-29 04:19:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c90f367-fcb8-3c0e-a3f0-30861c4543b3 | -18.49323 | -45.13018 | 2026-09-29 04:19:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c456f4ba-bf6c-330d-a3d9-e1b6f1c55b28 | -16.69495 | -51.83722 | 2026-09-29 04:19:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b4ee793-b6f4-34fe-9301-7f30a7fd056f | -18.57369 | -48.42373 | 2026-09-29 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1782b278-6500-37b1-8242-9ccfa48735be | -17.65634 | -46.53658 | 2026-09-29 04:19:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83b2dd0e-53b4-375c-8590-51ae4528035e | -16.69916 | -51.8383 | 2026-09-29 04:19:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6adf0af6-242a-340b-a2bc-9c6bcdeeed97 | -18.84306 | -46.90622 | 2026-09-29 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f695980a-21c1-37e0-8ebd-42acb74782c0 | -18.10652 | -44.35392 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40838f88-a358-3882-a645-9bf74c015f73 | -18.40993 | -42.31037 | 2026-09-29 04:19:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 74093628-f091-3420-9d96-2890cad86d36 | -18.56613 | -48.42644 | 2026-09-29 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 736fa943-d79f-3eef-944f-34d338d41f3c | -18.4899 | -45.12965 | 2026-09-29 04:19:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb46c012-6ba7-3203-9ddb-c56d3b3e3ec8 | -17.79131 | -47.15769 | 2026-09-29 04:19:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d036813-0826-3b36-b1b6-b54f9d73a362 | -17.59731 | -43.71747 | 2026-09-29 04:19:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d52ed3bc-cc5f-3633-8e57-60798546266a | -18.27012 | -42.20964 | 2026-09-29 04:19:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c4554903-e818-3257-9759-d24df7717287 | -17.13963 | -47.72146 | 2026-09-29 04:19:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fde10f1-31f7-3981-baaf-a36b64cb1b43 | -15.6319 | -52.69287 | 2026-09-29 04:19:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a553e286-82c8-3da2-8c9e-5484d8f5e8ec | -17.97813 | -44.48857 | 2026-09-29 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ceb6b8a0-d92c-3722-8ee8-e62ce13958ee | -15.63742 | -52.6888 | 2026-09-29 04:19:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b64bce9a-4c10-3ca1-bc1d-135969cf9451 | -19.53747 | -42.93097 | 2026-09-29 04:19:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.6 |
| 5ec102ab-37c7-39c3-b4aa-35a4008e60e0 | -18.09975 | -44.35287 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 158c5276-1311-3d7d-bc2c-96bcd00bb0cc | -18.40623 | -42.30982 | 2026-09-29 04:19:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README34.md)
