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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5023d7f-7041-3dad-88f6-a514f1e8a6ae | -22.45191 | -46.90029 | 2024-09-28 04:23:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc5578c4-db4e-33e5-a0e2-7169b5c0e2b9 | -22.43902 | -46.90704 | 2024-09-28 04:23:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e31bb35-5c6a-3b8a-81b2-edaa2db28441 | -22.86368 | -47.21775 | 2024-09-28 04:23:00 | NOAA-21 | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 298a0222-06a2-3ca0-a65c-9f42be261278 | -22.70838 | -46.30965 | 2024-09-28 04:23:00 | NOAA-21 | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 17e26c43-ea1d-3d14-9f68-a11d9fe9a206 | -22.6112 | -46.90739 | 2024-09-28 04:23:00 | NOAA-21 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2d9a525b-76c6-3769-aa8f-e9a8dd5d5bdc | -17.24389 | -46.28796 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e1ea57d-452e-3389-ad3e-1d8dc48b0c42 | -17.24056 | -46.28741 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acb73570-d317-3e91-bcda-3daf46a18756 | -17.01058 | -45.92383 | 2024-09-28 04:23:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2a64b22-7372-35c4-a6bc-1f0f0bd22d3a | -17.01002 | -45.9275 | 2024-09-28 04:23:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 998c4123-fdc1-3661-b0b8-ca1e685fe69f | -17.00723 | -45.92328 | 2024-09-28 04:23:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcdd501a-574b-3801-9005-371037a8dd4b | -17.00668 | -45.92696 | 2024-09-28 04:23:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1955115a-3093-3ea5-b995-76538875a3c1 | -16.98549 | -45.90842 | 2024-09-28 04:23:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 973a9c1e-51d0-308c-adad-2a15c5cdce81 | -16.98493 | -45.9121 | 2024-09-28 04:23:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4b8b2c1-7384-3eaa-a712-fa2f9ff7aa9b | -16.98438 | -45.91577 | 2024-09-28 04:23:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39b2abbf-7809-38bb-b1c3-6dd675db15d1 | -18.83497 | -46.68443 | 2024-09-28 04:23:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4afc680b-5ee0-3d85-ab63-8ab7a45ef9dc | -18.83441 | -46.6881 | 2024-09-28 04:23:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 899979c4-920d-3760-a544-b4b669d5dbb2 | -18.83385 | -46.69177 | 2024-09-28 04:23:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3674688a-2f67-316e-9581-b18ce19bf3c0 | -18.75815 | -47.20663 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a579318-2842-3aae-8ceb-869ebff5e72c | -18.75088 | -47.38405 | 2024-09-28 04:23:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53651cb8-e1d4-373f-b58f-5c299aba1374 | -18.56107 | -47.29262 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cd22089-309b-3c5d-8aab-5b9ea256ad31 | -18.55776 | -47.29206 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 291cb7af-8816-3f91-8daf-ecec50054774 | -18.55446 | -47.2915 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5f9bcfaa-3c34-34dd-a513-fb09fbcc7751 | -18.5535 | -47.25417 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9d89786-f39d-332d-9870-16eb0b0ae5f0 | -18.55124 | -47.26865 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8e0c625-2925-3b54-9048-a83234d3b6bc | -18.53697 | -47.07658 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1e62b58-4b32-33f0-a104-7041a926e4a1 | -18.5331 | -47.07965 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 353944b2-252d-3939-b26c-5625a3672311 | -18.503 | -47.09667 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3687229c-ed9a-3078-ba56-ea3354fadda6 | -18.4997 | -47.09611 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01715746-f7ba-3938-9214-153786de195d | -18.49801 | -47.10698 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63361a46-767f-3075-9d63-7ef782e766b4 | -18.49583 | -47.09916 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b70af7d-051a-3072-b698-7c23e6eea3f9 | -18.49527 | -47.10278 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f4e1db6-3522-369a-9c53-c4d74ba41eb8 | -18.49471 | -47.10641 | 2024-09-28 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9224f2b3-4de6-3838-9689-73f22b2555f9 | -18.33511 | -46.48605 | 2024-09-28 04:23:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0afb1a10-331d-3444-aa48-36bea165f59e | -20.52237 | -47.4504 | 2024-09-28 04:23:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 279e7d87-4941-36fc-855a-e5471fe9611c | -20.51994 | -47.35599 | 2024-09-28 04:23:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15ba322e-ed38-398f-9bbc-24e21a4daed6 | -19.82927 | -47.00499 | 2024-09-28 04:23:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa6fa40f-a51d-368a-a91e-dc825fedfb92 | -19.81786 | -46.99159 | 2024-09-28 04:23:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0e4d6c2-92be-3ff1-a077-cecdd4ba4d22 | -19.79182 | -47.00604 | 2024-09-28 04:23:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39d65a22-73cd-3c7b-b76d-baf9de30465f | -19.79125 | -47.00975 | 2024-09-28 04:23:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 021e5a0f-c3f0-3041-9532-2031b1787293 | -19.78906 | -47.00179 | 2024-09-28 04:23:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fa1e6953-1641-3243-93cc-77c850985e40 | -19.7885 | -47.00548 | 2024-09-28 04:23:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 832ce8ad-1241-3449-b2a5-561fc05bbf2c | -20.92312 | -46.95784 | 2024-09-28 04:23:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93b85637-d56f-3471-b1d7-b8e4298471eb | -20.92255 | -46.96162 | 2024-09-28 04:23:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 769e7905-3dc5-3dd3-a9d3-78eee7c98fe5 | -21.92557 | -48.46317 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39b90317-fac2-3e27-a0d8-14cb32790b0b | -21.92265 | -48.48166 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea641714-299e-3e6b-b309-9b584bcd1e66 | -21.92207 | -48.48536 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c397fb48-db75-37e8-be29-98976ca2f095 | -21.89386 | -48.4917 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ac78564-06c9-3e75-b994-2165ff238745 | -21.89328 | -48.4954 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| badb1906-6921-3469-9de1-af453c6e38a5 | -21.89269 | -48.4991 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b924abd8-de47-35f6-9c9e-8c7d72b0f24f | -21.89211 | -48.5028 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c1839c3-733d-3a81-b514-90030bbb5b18 | -21.89152 | -48.50651 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 248476e5-026f-3e55-a702-e14fcbee36fc | -21.89094 | -48.51021 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a803712d-85d2-39af-8f0d-21c3885e39e9 | -21.88998 | -48.4948 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ea7c4c0-fcf1-33f0-9ac1-963ff368d469 | -21.88939 | -48.4985 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ca52595-4c12-314f-b6e1-d06a7a7da9b6 | -21.88881 | -48.5022 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f47674e0-37e7-3070-887a-70dd5a67c322 | -21.88822 | -48.50591 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b0c1e0a-5c9c-3fcb-b8e1-ca58b5983a17 | -21.88667 | -48.4942 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60be2e51-139a-39b5-bc27-f96a35592e50 | -21.88609 | -48.4979 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc080168-a5a3-3147-b0be-1dbbe6840b8e | -21.8855 | -48.5016 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24585798-c04a-3ad1-bc6a-515425e9571b | -21.88491 | -48.50531 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 310ae7ed-8c50-3383-9373-05cf2e4fc3fb | -21.8491 | -48.21402 | 2024-09-28 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d4e9bfe-6310-37c0-a975-6aacfb352868 | -21.84852 | -48.21772 | 2024-09-28 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c0921df-8f14-3649-b1ed-2174140532b5 | -21.84637 | -48.20972 | 2024-09-28 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68c65b67-af9e-3a9a-8bca-4af0676d1dc5 | -21.84579 | -48.21343 | 2024-09-28 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ebec371-5249-3383-8ebd-0c0c6a00014a | -21.84521 | -48.21713 | 2024-09-28 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 100767d4-f22c-3311-b8e8-48881e987243 | -21.84367 | -48.20549 | 2024-09-28 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 384ffd4a-37b0-39fb-bb5f-0ff42d0dcb98 | -21.84249 | -48.21284 | 2024-09-28 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dff14877-7b01-3fc9-8880-013d16be5482 | -21.84191 | -48.21654 | 2024-09-28 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a74fd24-f8ca-3433-80da-2ac730cb6792 | -21.83921 | -48.2123 | 2024-09-28 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2758d948-7213-32bf-aa44-4cee18d26c99 | -21.8386 | -48.21595 | 2024-09-28 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67b467ee-0fce-3273-8190-95028308d0ce | -21.83591 | -48.21171 | 2024-09-28 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a587e01-c225-3bb4-abe7-90d50b21f705 | -21.83261 | -48.21112 | 2024-09-28 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05a52a15-05ee-3825-a4c9-cbf046e27d66 | -21.51091 | -48.071 | 2024-09-28 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 842dec54-0ff2-31ec-bd8f-d9ea69ed99e5 | -21.50748 | -48.07084 | 2024-09-28 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c0b555a-3327-3c8b-9b04-0d57b8879ebf | -22.22087 | -48.61888 | 2024-09-28 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c9c6c2ee-8b16-3b6a-a2da-8def9c3a1dfa | -22.21639 | -48.62569 | 2024-09-28 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 10ce8ff7-8a98-3738-bc99-7d5583c8b0e9 | -22.21309 | -48.6251 | 2024-09-28 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd27efdc-ad31-36b5-94d2-5a3e25586f1a | -22.19231 | -48.60603 | 2024-09-28 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 13d42cbd-7b4f-3bef-a36e-9bc01265d9c7 | -22.19172 | -48.60974 | 2024-09-28 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6397df94-7596-31ac-97b6-9061109a2f47 | -22.19113 | -48.61345 | 2024-09-28 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e687fd25-2a78-3372-b310-3ead833fa67b | -22.18782 | -48.61285 | 2024-09-28 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 808cde40-b403-34f2-80a9-b34e181393b7 | -22.18723 | -48.61656 | 2024-09-28 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0cf0b78b-fb0e-3a6f-a2d6-0597037bcce0 | -22.44201 | -47.1551 | 2024-09-28 04:23:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0be2aeb1-ffa6-3135-aed7-e3aa6f69aea3 | -22.35708 | -47.65302 | 2024-09-28 04:23:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 518a8e75-1427-30e2-a1a8-5cffe6882d99 | -22.35376 | -47.65244 | 2024-09-28 04:23:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d95e1c28-c9ea-3902-b552-51c8517c28a5 | -22.35044 | -47.65185 | 2024-09-28 04:23:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d258f45-db5d-3caf-a011-1a81ac764d94 | -21.62805 | -47.75362 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35ad72d4-8dd7-37fe-87e9-283de1fee546 | -21.62748 | -47.75732 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c8722b37-7390-3f02-82ec-a8890ee9abf2 | -21.62691 | -47.76103 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b4fddce6-83f7-3fe4-b196-194b2857b40b | -21.62474 | -47.75304 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ade5c213-3b38-34b9-aff0-1cfdde44662c | -21.62417 | -47.75674 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c3815982-d3b7-3b42-b962-50c69029c739 | -21.6236 | -47.76044 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eb368fb8-1513-3d8b-a13a-f1f286d7e25d | -21.62303 | -47.76414 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.8 |
| c067c931-2bc5-3509-a8bd-b008f3c9f82f | -21.622 | -47.74874 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a2e9e6e-b134-35ca-8ef9-7d41f1beb170 | -21.62143 | -47.75245 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a148de4-83c9-3b13-8335-8060aff0f2bf | -21.62086 | -47.75616 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| da547800-2111-35a2-b2d8-da09ad26b33f | -21.62029 | -47.75986 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 09c27ea0-01bb-31ce-8609-55a306382575 | -21.61812 | -47.75187 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eda01b2d-106c-3707-b070-a17fa55782e1 | -21.61755 | -47.75558 | 2024-09-28 04:23:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aa77a098-4e0b-3456-8e50-6286ecf6dc77 | -21.44054 | -47.80101 | 2024-09-28 04:23:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README65.md)
