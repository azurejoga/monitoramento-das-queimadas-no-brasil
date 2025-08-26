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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b7567fa-8783-37b1-adef-e3d645e6ee2c | -18.75331 | -45.36556 | 2025-08-26 04:25:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b200384-6117-3db1-afa6-9fbd66aae8ab | -19.18222 | -48.73458 | 2025-08-26 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3ee83c03-0fc6-35b4-ab2e-bdeeb2ea4b10 | -19.28244 | -43.73711 | 2025-08-26 04:25:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f9fb4c0-bf94-3e75-be77-a183f05bc5d0 | -18.98516 | -47.07955 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71896e34-34a9-3fe1-9104-1806fb7ea462 | -21.60975 | -49.69775 | 2025-08-26 04:25:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 10cddf71-456d-3ed8-a19a-1607d94a3b65 | -19.45476 | -45.30902 | 2025-08-26 04:25:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ff79d0b7-53de-3f82-a159-b70cc3139fd6 | -18.85646 | -47.01225 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f310b42d-86f6-30a8-8738-94ecac7edb9a | -18.87206 | -46.99992 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44702563-6825-3ea8-afa5-09202a07e656 | -18.71586 | -41.27494 | 2025-08-26 04:25:00 | NPP-375D | CENTRAL DE MINAS | MINAS GERAIS | Brasil | 3115706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f9587f0f-b427-369c-a685-374f08bde7a5 | -18.72012 | -41.27581 | 2025-08-26 04:25:00 | NPP-375D | CENTRAL DE MINAS | MINAS GERAIS | Brasil | 3115706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| be97093f-3d84-3073-8a24-4e22e0ec8cb4 | -21.58527 | -45.28099 | 2025-08-26 04:25:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1e62a052-f16c-3b94-95fd-2559e48d5c27 | -18.14385 | -44.43093 | 2025-08-26 04:25:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de45cf64-108e-3994-ae45-583ea58f9e1a | -19.48805 | -46.11882 | 2025-08-26 04:25:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6a66431-f3ce-317f-aa85-2534906c7f5a | -18.81152 | -47.5972 | 2025-08-26 04:25:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdea09ec-78f4-316e-b4ef-33045384b27e | -20.90854 | -48.47337 | 2025-08-26 04:25:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c290c3a-08d8-3fa5-a154-dcc49102be90 | -22.27237 | -46.45324 | 2025-08-26 04:25:00 | NPP-375D | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4362b2b0-8d08-34e1-8d84-42d01f371f0a | -21.6091 | -49.70161 | 2025-08-26 04:25:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b5277938-3b43-301e-80da-6db07313d8c1 | -22.55179 | -46.82417 | 2025-08-26 04:25:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0fa74871-8a0d-32f5-a4a5-5c715f8cea8b | -18.86816 | -47.00301 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7f973ea-f10f-33ac-b4f9-738f234ffd34 | -22.47602 | -48.99713 | 2025-08-26 04:25:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7955bfd0-f15a-3ff3-873d-4a3aaf91d619 | -18.85482 | -47.00076 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e405dd4e-aa3d-36da-9a2b-17a1928c18b9 | -23.32638 | -47.84074 | 2025-08-26 04:25:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 04f0ef8e-e930-33c2-a165-301850a3ceb0 | -21.0382 | -48.62996 | 2025-08-26 04:25:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e812ecee-1785-3901-a897-a7bdbc704dd9 | -20.98544 | -42.99823 | 2025-08-26 04:25:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 198e79b4-4304-34c3-ad46-cb5a3b8ea131 | -20.20694 | -47.01442 | 2025-08-26 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce8bc23b-d83e-3c7e-a2f5-39c2fccc85c5 | -18.14442 | -44.42687 | 2025-08-26 04:25:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cac58bae-8df3-3f8d-97e2-649cc2ea43c5 | -19.03311 | -46.91389 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 571fcb63-8459-330b-a5b2-9496451ced32 | -22.89927 | -49.05883 | 2025-08-26 04:25:00 | NPP-375D | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74612aaf-191d-3738-82a4-39ded710841b | -21.61249 | -49.70226 | 2025-08-26 04:25:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f71f19cb-3454-3e43-8842-510d2d0cda60 | -18.8121 | -47.59355 | 2025-08-26 04:25:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33daf08a-e8c9-34a3-a9d3-c8d4ac113a73 | -18.98459 | -47.08321 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2689978-ff6e-3157-aefc-af8a9703e27d | -17.60978 | -46.70371 | 2025-08-26 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ca199bd-7152-3366-976f-16a0f79f286b | -19.17619 | -44.51439 | 2025-08-26 04:25:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2397bba-07f3-31a2-bd38-d110d814ecc1 | -17.78048 | -44.48506 | 2025-08-26 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 204ef5f9-e9a0-3975-9e11-eb5b3f1910ab | -21.28997 | -43.33515 | 2025-08-26 04:25:00 | NPP-375D | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7cfddb3d-4f99-38a4-9e1c-84e79750b683 | -20.19122 | -44.57827 | 2025-08-26 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f49e0501-a585-3150-b1a6-d2b17ea8af87 | -20.88883 | -49.02759 | 2025-08-26 04:25:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ab1b8fc9-8723-3b5b-89cc-54f120059642 | -20.37947 | -42.19672 | 2025-08-26 04:25:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| b91e9e4a-a123-387f-aedd-bfa725ee61ea | -17.56763 | -49.75436 | 2025-08-26 04:25:00 | NPP-375D | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72b5f4be-624d-3f1f-bb5c-bfd272ac12e2 | -19.17947 | -48.73024 | 2025-08-26 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| be3a50dc-74c6-3003-8a62-5403c4063bf0 | -16.80909 | -51.91009 | 2025-08-26 04:25:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9614f2ff-87d6-33a0-9d27-acb07e8df82c | -20.18761 | -44.57763 | 2025-08-26 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d6925490-bdf2-31c4-bc30-41fbcea89f21 | -21.12684 | -45.87857 | 2025-08-26 04:25:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6db09bb4-fb5a-35ed-870c-d5d185bde36b | -19.03644 | -46.91447 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b53e75eb-ac3e-3eb7-a8db-5da391dcf88f | -21.42811 | -48.41631 | 2025-08-26 04:25:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f9d8d5d-3f9b-3fc1-9182-a7c857092350 | -18.81094 | -47.60084 | 2025-08-26 04:25:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c335946-366b-3206-9e8a-180bb3e81af4 | -19.79545 | -47.98552 | 2025-08-26 04:25:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 339837c5-5c96-35f7-b7d4-d4fea7844b21 | -21.63438 | -49.84291 | 2025-08-26 04:25:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a1339af0-29af-3fd2-9281-cee9d3fab356 | -20.1687 | -41.33974 | 2025-08-26 04:25:00 | NPP-375D | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c6748d04-0dfc-341e-b2f2-7c9c2a328e53 | -17.37604 | -48.08637 | 2025-08-26 04:25:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ee2c779-133b-3bd5-ba3a-569299b1aa8d | -20.4612 | -43.87366 | 2025-08-26 04:25:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| db4c5715-d66e-3990-86a0-1dce606feb1c | -19.12448 | -46.45057 | 2025-08-26 04:25:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c3f5f98-f94d-3d42-844b-c50e8e90ba9a | -21.57969 | -46.36039 | 2025-08-26 04:25:00 | NPP-375D | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 292ea8c9-970f-32ae-b26c-d0ec0f6ef243 | -20.45741 | -43.87345 | 2025-08-26 04:25:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b82a4f8f-4dc5-3983-9171-c1fd927ba7de | -17.60481 | -46.69167 | 2025-08-26 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 617d8fad-edf7-3ef7-b251-f2654b7c217c | -21.37293 | -45.53747 | 2025-08-26 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b6fcf942-1bca-3734-8a35-00cbf369eb95 | -21.28964 | -42.55432 | 2025-08-26 04:25:00 | NPP-375D | SANTANA DE CATAGUASES | MINAS GERAIS | Brasil | 3158409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d2ade30f-ec2f-388d-8baa-41d896f62a4f | -17.35281 | -47.85955 | 2025-08-26 04:25:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0bf37de-dc87-38e9-8093-f8150667b7cf | -18.86596 | -46.99513 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89d846b4-fc3e-30f5-889c-0bee2777be1a | -18.8398 | -47.00942 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38fcfdd1-5c00-3204-97e9-043df0ae2f78 | -19.17611 | -48.72963 | 2025-08-26 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a2baed8-3588-3398-ac9b-4bdcfc0d4bc0 | -20.88548 | -49.02695 | 2025-08-26 04:25:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 497ee3e4-1e48-3a4a-9d24-b1f4d182ae7d | -21.43154 | -45.47762 | 2025-08-26 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5a6e3c11-de38-3e5e-9c4f-f280b333f1fa | -17.6842 | -46.31123 | 2025-08-26 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b41fcb70-96b8-32c1-81ad-c07cb28e273d | -20.16439 | -41.33866 | 2025-08-26 04:25:00 | NPP-375D | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 50293214-19b7-3cb8-bfd3-5b0d6af96dbe | -21.72171 | -46.80859 | 2025-08-26 04:25:00 | NPP-375D | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 46374df3-46c0-38e6-a08e-faee34c5a3ab | -17.68756 | -46.31179 | 2025-08-26 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8594458f-61c3-359d-93aa-3e75a9c84811 | -17.60814 | -46.69224 | 2025-08-26 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb579f17-679b-30de-9625-8ab384b5522f | -18.87149 | -47.00357 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d21d4e74-638a-3b73-a731-0403aa039941 | -21.08905 | -43.41513 | 2025-08-26 04:25:00 | NPP-375D | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e25f7647-cc10-3159-b833-72f13f5a16c1 | -23.39991 | -51.19283 | 2025-08-26 04:25:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 2853c6e0-7ccc-3f45-9c6b-62280d98068c | -20.39068 | -46.71846 | 2025-08-26 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79cb70f9-3a5b-3ec4-9240-4a4a0ef6e846 | -20.04358 | -42.60701 | 2025-08-26 04:25:00 | NPP-375D | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d8798c17-5535-3dde-8bf2-09b8e05cfd5b | -18.71589 | -43.81507 | 2025-08-26 04:25:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8400e60d-393c-3eda-b612-794baea4bdc9 | -22.15424 | -48.76551 | 2025-08-26 04:25:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cae58e67-2c6d-3fdc-b866-a3568dac0365 | -19.83101 | -45.89174 | 2025-08-26 04:25:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1f9747e-ac3d-3edb-95dc-983e0db8ea6c | -20.187 | -44.58203 | 2025-08-26 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 75d8511a-21d7-349e-b8ad-acf1836abe5b | -21.61314 | -49.69839 | 2025-08-26 04:25:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f9250007-d445-38b6-8f39-2f102c97e83c | -21.38933 | -45.49642 | 2025-08-26 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7de957ab-a3bf-38f9-af73-8b901b927938 | -18.84979 | -47.01112 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25fc2708-3b68-300d-9f46-fff5e43576c8 | -21.19993 | -48.92503 | 2025-08-26 04:25:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 9ddc30ff-72ad-3773-98ca-9e80c9308949 | -21.42742 | -45.48131 | 2025-08-26 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9322bcb5-2670-3aa4-809c-5111a9735801 | -20.88821 | -49.03135 | 2025-08-26 04:25:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b2689a98-1c59-3879-89ab-ffc92df8fd0b | -17.78814 | -44.48211 | 2025-08-26 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0ebd15f-d053-3510-b8cb-dcc7924c3110 | -20.98615 | -42.99284 | 2025-08-26 04:25:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 494bc317-f7d4-39fc-8d42-5ee84258601c | -19.98675 | -42.21616 | 2025-08-26 04:25:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 72554529-bda1-34d0-bc19-f36553ecbe2f | -20.16921 | -41.33554 | 2025-08-26 04:25:00 | NPP-375D | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 672aa418-a1e4-3f15-aa7f-8e72528d34c3 | -21.64261 | -49.75219 | 2025-08-26 04:25:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 54c2d312-600b-3c32-9c14-75ee0ffb63c8 | -21.12243 | -45.87511 | 2025-08-26 04:25:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 72349a27-437d-3bf7-9ed0-8344c8c6e819 | -20.3799 | -42.19324 | 2025-08-26 04:25:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5ae31f85-94c3-39f0-9b23-67501d62c071 | -19.90972 | -44.63108 | 2025-08-26 04:25:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 68e0bf9c-98a1-3de0-b16d-59f35d947e2c | -20.3832 | -42.20052 | 2025-08-26 04:25:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7c2b090c-67fd-33e9-884b-f3d5399cc668 | -16.80415 | -51.9147 | 2025-08-26 04:25:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59d0e55e-1a5a-3ec7-9ea6-303b6669746b | -19.17977 | -44.51497 | 2025-08-26 04:25:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6dc9a2e6-0131-3e3a-8413-abb4af48f6cf | -19.03649 | -43.42799 | 2025-08-26 04:25:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8654f04b-531c-3f92-a115-f9f156956831 | -18.23923 | -51.27172 | 2025-08-26 04:25:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2614e0b0-5448-3b62-bd08-9afc6df3b09b | -19.12391 | -46.45432 | 2025-08-26 04:25:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ee77abd-1542-32d5-80b1-f6a6877dfd59 | -20.04694 | -44.46752 | 2025-08-26 04:25:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4e58ad7e-19f4-32ac-a856-02286ec70c9d | -22.8926 | -49.05759 | 2025-08-26 04:25:00 | NPP-375D | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c677463a-ca7b-31d3-9eab-09fcc2ec02ea | -18.52497 | -46.28824 | 2025-08-26 04:25:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README52.md)
