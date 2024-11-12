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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdcba780-12fa-3402-b884-e9cf1abe5184 | -20.32255 | -48.83227 | 2024-11-12 04:04:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5facddd-6907-3bae-a43b-a8df98fcc6c6 | -19.27573 | -39.89503 | 2024-11-12 04:04:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2a2d7ada-145d-3710-b5a0-0224c6dfdd09 | -20.39441 | -47.07797 | 2024-11-12 04:04:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 88ad06d8-98e0-3274-943d-87180da41535 | -21.32155 | -53.9241 | 2024-11-12 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f23e2f5-b95b-34cb-958c-3c95a0e67e60 | -20.52009 | -47.32763 | 2024-11-12 04:04:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95fa4215-e6ad-32a3-a84f-a3055b58a98c | -19.61911 | -54.15443 | 2024-11-12 04:04:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d2a07c6-84ce-3ecd-8ab4-5bfa8d5a3dcb | -20.04867 | -48.9884 | 2024-11-12 04:04:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1f3ecc3-06fb-3e48-be12-49c5b7271fb0 | -23.40365 | -46.55629 | 2024-11-12 04:04:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 45a87119-1072-359f-afe8-92403f1dd23f | -20.11125 | -49.18695 | 2024-11-12 04:04:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 85b64e54-9261-3239-b149-719872e1d1ca | -20.04924 | -48.98556 | 2024-11-12 04:04:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f18bda1-f081-393d-bc8c-bc7d4e0a4e51 | -17.67584 | -42.74277 | 2024-11-12 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00ec2f43-3849-39d1-9d28-39be0ed90fbb | -20.764 | -46.7679 | 2024-11-12 04:04:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c51eb93f-169e-3f13-ba87-620ade217904 | -20.5815 | -41.85798 | 2024-11-12 04:04:00 | NPP-375D | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8675ff9f-3126-3c3a-93d9-b2819989b20d | -18.34955 | -40.01244 | 2024-11-12 04:04:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| df892a92-aff9-3d02-8f9b-46ceddceff3e | -18.02088 | -44.09709 | 2024-11-12 04:04:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 755a8d45-812e-3f09-a078-c65cbfcae6c2 | -20.63518 | -48.83606 | 2024-11-12 04:04:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8bead472-9bce-37c1-be80-2e4fb58d659b | -18.03621 | -44.52725 | 2024-11-12 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c318eea4-aabe-39d9-9f56-04674d69e400 | -21.62796 | -43.46769 | 2024-11-12 04:04:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7ac2cb1b-cd60-3f06-b1a5-47540fcbd3ee | -21.31431 | -53.91807 | 2024-11-12 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27766086-5897-34b4-ac45-e855d0ee9090 | -23.59247 | -47.43876 | 2024-11-12 04:04:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dab61af4-3de0-3170-957a-a671ee4d1a39 | -21.31344 | -53.92191 | 2024-11-12 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a12a955f-966d-3d5a-a35d-3ab4f1b4f119 | -19.62694 | -54.15347 | 2024-11-12 04:04:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f30aac62-e295-3e88-8b4b-a18919bed005 | -19.17607 | -40.13633 | 2024-11-12 04:04:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ec03bb99-c4af-3262-a78a-5693d1864fff | -22.53958 | -48.81285 | 2024-11-12 04:04:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7460c0d5-1873-3b5e-9a3c-2c52777f5950 | -19.58688 | -43.99306 | 2024-11-12 04:04:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33d5f131-86b7-321b-a59c-c4cdbdb5f064 | -18.34897 | -40.01653 | 2024-11-12 04:04:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 681fc8ff-17a2-34d4-9ba3-d86a629b6c52 | -20.31113 | -45.58438 | 2024-11-12 04:04:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01c07478-3bf3-3cc7-8a1c-af5dc3030c68 | -22.85974 | -43.52335 | 2024-11-12 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bcf1e214-da25-33cb-a1f3-d8b02139e21d | -20.1125 | -49.19409 | 2024-11-12 04:04:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 50032524-a717-3c27-9960-89292ecfb824 | -20.11046 | -49.19115 | 2024-11-12 04:04:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| eda7a654-e657-329b-b92c-a4cfa6acd501 | -21.03478 | -48.65362 | 2024-11-12 04:04:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ec0974e-fbf0-35dd-9aa4-f4727c817f41 | -23.70665 | -46.47835 | 2024-11-12 04:04:00 | NPP-375D | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 41a74bb8-bf29-3873-98ca-aee6ca18b60e | -21.94147 | -42.27089 | 2024-11-12 04:04:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| abd7ad23-71ae-3c66-9210-3d2ac78751cd | -19.45572 | -39.75768 | 2024-11-12 04:04:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 2a8db600-341f-3b4e-9b40-74f5f2dceed0 | -22.11897 | -48.91328 | 2024-11-12 04:04:00 | NPP-375D | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7c0fefd2-b0e1-31bf-b44b-269573a6e382 | -19.17313 | -40.13163 | 2024-11-12 04:04:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 34f0816a-b864-367f-9100-29b47ba24ede | -21.31808 | -53.92727 | 2024-11-12 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9485900e-1723-3c28-ae19-a4340ad4a3cf | -20.31996 | -48.82342 | 2024-11-12 04:04:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cad95fd9-0c66-331c-aa19-216da31b6c58 | -21.3152 | -53.92641 | 2024-11-12 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6446ad13-66ad-3a59-9ff2-512cba430f4a | -20.11471 | -49.192 | 2024-11-12 04:04:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 82a3b104-584a-38e9-a66f-17ec42adfd27 | -23.34003 | -46.77364 | 2024-11-12 04:04:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 38c83ab7-db9f-3591-a2fa-2661f75a5651 | -20.39814 | -47.07872 | 2024-11-12 04:04:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f994041e-579b-3bab-8d4d-09aa873e4f28 | -17.70776 | -44.73302 | 2024-11-12 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a2b8747-2b14-342a-b317-a16599214242 | -18.90007 | -49.76989 | 2024-11-12 04:04:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5eb4ba98-e743-3d81-b21e-06020eb0c3a3 | -21.18018 | -43.9804 | 2024-11-12 04:04:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4b07da6a-e089-35e2-b395-f739eed9d859 | -22.36522 | -54.41856 | 2024-11-12 04:04:00 | NPP-375D | VICENTINA | MATO GROSSO DO SUL | Brasil | 5008404 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5802dee8-c675-31ac-a30c-28c5221ba826 | -20.11333 | -49.18991 | 2024-11-12 04:04:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b479be3e-d653-3ea6-a2c2-260700a62278 | -17.70844 | -44.72905 | 2024-11-12 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1dc30946-1ac7-3cf4-89d2-91682c88801b | -18.39807 | -45.97961 | 2024-11-12 04:04:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd04d2af-4402-375e-a4ed-ee4788a9bb81 | -23.40714 | -46.55708 | 2024-11-12 04:04:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b19a24c5-4b6d-372c-bf14-11dfd41b8b62 | -19.62495 | -54.15571 | 2024-11-12 04:04:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb24e2a2-9216-3c77-a699-7b83fa3f43f0 | -19.62593 | -54.1514 | 2024-11-12 04:04:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9baf75a5-bc74-3347-b9b6-e84bbcb1704e | -17.3793 | -42.48458 | 2024-11-12 04:04:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53747655-ce11-3bca-bb56-b7d641e3142f | -20.04948 | -48.98424 | 2024-11-12 04:04:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a29ff11d-071b-3d3b-a504-695024849e5b | -17.09419 | -43.80315 | 2024-11-12 04:04:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28992d53-b77a-322e-a003-c3762a348e28 | -22.3708 | -54.42002 | 2024-11-12 04:04:00 | NPP-375D | VICENTINA | MATO GROSSO DO SUL | Brasil | 5008404 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 3b150b24-6037-32d6-b9da-04d1b4279f23 | -20.22886 | -47.51458 | 2024-11-12 04:04:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a8cda2d-05cb-303d-adac-5077a4bab1ec | -23.70317 | -46.47765 | 2024-11-12 04:04:00 | NPP-375D | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 42f9c379-4164-3c6d-a80f-5dbdfa16cbc7 | -19.17666 | -40.13219 | 2024-11-12 04:04:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3f07fa1f-48f2-346b-b8e2-5615e53e7e2c | -22.78122 | -46.07682 | 2024-11-12 04:04:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9f756240-8ac2-33cf-bfb7-19a733735a29 | -20.6393 | -48.83689 | 2024-11-12 04:04:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b6b83d90-6b63-3fe1-92db-5a20c61fbd0c | -20.93097 | -47.43738 | 2024-11-12 04:04:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3434217-6a17-3fe6-b24c-bac739d2ee80 | -23.33648 | -46.77295 | 2024-11-12 04:04:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| aecc5b97-475b-3910-aac8-fc7b21a11b48 | -19.62015 | -54.15653 | 2024-11-12 04:04:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f2ee624-3655-37c3-aa95-9b2526338aaa | -20.10621 | -49.19028 | 2024-11-12 04:04:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| aeff3f21-406b-3973-a546-32a4d7d78931 | -20.32408 | -48.82433 | 2024-11-12 04:04:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62bd662f-1b9c-309e-a46a-212bfc887f57 | -18.85936 | -47.92826 | 2024-11-12 04:04:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a6e752de-b5fb-3136-94ce-c33375f4fe79 | -21.31894 | -53.92345 | 2024-11-12 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a6b6e8f0-2284-3001-bf0c-f78bc25c4309 | -18.90456 | -49.77087 | 2024-11-12 04:04:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a0e4ee31-1237-3028-8987-88d5ec87608c | -23.98646 | -48.91655 | 2024-11-12 04:06:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c9aca7a-9d29-3091-9ef5-c913f812cdfa | -25.20428 | -49.40192 | 2024-11-12 04:06:00 | NPP-375D | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 471c362b-0bda-3d5c-a954-f0986438cf67 | -23.95177 | -54.04145 | 2024-11-12 04:06:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c0192db3-4197-3496-a1b2-f4e270d63f9a | -25.19105 | -49.32763 | 2024-11-12 04:06:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e8c1f9aa-092f-316c-aad8-bbaf14b1a91b | -23.94445 | -48.90556 | 2024-11-12 04:06:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6726d98a-1877-35cb-8671-925790e3ff3b | -23.95258 | -54.03784 | 2024-11-12 04:06:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 15e00789-caf7-3649-a380-3f76de545d81 | -2.7737 | -50.2992 | 2024-11-12 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| e1aa42e4-f6a2-3c7b-a9a0-3bf21166f7c5 | -2.7922 | -50.2986 | 2024-11-12 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| e0b544a0-4312-3100-afc0-12857725b15f | -7.42909 | -35.2325 | 2024-11-12 04:16:00 | AQUA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 30.4 |
| 8e1c8365-e019-3849-8e1b-06a68cb44c7c | -2.7922 | -50.2986 | 2024-11-12 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 07619955-94f9-366a-b32c-eca5c3dbea33 | -2.7921 | -50.3196 | 2024-11-12 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 1989c4d1-f846-30c2-9303-d45045bf6a2f | -2.7737 | -50.2992 | 2024-11-12 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 5403d706-86d5-3cf9-8601-70c4a19d999f | -3.0689 | -50.3326 | 2024-11-12 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| ab84ec06-bb12-3677-8710-f396f3212123 | -3.0504 | -50.3332 | 2024-11-12 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 40adc6bd-04cc-3802-bf5a-f35a8993e014 | -2.1271 | -50.6912 | 2024-11-12 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| cc9035f4-2a05-35df-9950-ee9b4883a040 | -3.45138 | -49.122 | 2024-11-12 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0e1402e-55bd-3782-abe4-7ed078122cb0 | -3.65975 | -50.21332 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ceafdd9-8959-3850-8916-3b8fc3146652 | -3.43908 | -50.30886 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc52cd1a-f0e2-3452-a83e-cc95b9a0337d | -3.65489 | -54.65849 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f12774c9-e63c-33fc-b7c7-ea250a174c3f | -3.94929 | -49.00719 | 2024-11-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae7433c1-f542-3572-95a3-5de623fdb4d1 | -3.87216 | -50.16665 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b251a35-a00a-39eb-b124-fb0ded10530f | -3.91978 | -46.41016 | 2024-11-12 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc29463b-cff1-32cf-b312-f5164525e376 | -3.62908 | -54.71512 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dd068ce-4f8e-3ff8-98d5-a445d29d752d | -3.65956 | -54.66304 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5661f18-f29f-3d22-925c-fdeb1dec6870 | -4.06211 | -48.32193 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e1292e3-8247-37d9-bd8c-dafc89485deb | -7.42832 | -35.23991 | 2024-11-12 04:23:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| b11c0c2e-ba57-3707-b6e7-2a188245884c | -3.66678 | -50.21949 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d246ecbc-3b58-303b-ae58-e80d7d91b49c | -3.66053 | -50.20842 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7888592b-5c95-3b0f-9b13-ac46e08dacb6 | -3.82133 | -49.85637 | 2024-11-12 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caae3858-8c92-3991-b1d0-38543d62d739 | -3.95649 | -48.12264 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a6cfef9-b67f-3f55-b371-3bab3c8bbeee | -3.94634 | -49.00239 | 2024-11-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)
