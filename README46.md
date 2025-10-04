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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77a2409f-29d3-3b89-99a7-dcf438317288 | -13.50423 | -47.27011 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c779f728-1408-3ad2-ac5f-468cf62bd1df | -17.63841 | -44.45302 | 2025-10-04 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a178d39-1d35-316b-9741-e7b1d75a4182 | -11.86366 | -44.96265 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49e85f3b-4805-3c97-97cd-c46abd013249 | -14.66598 | -48.24737 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a45a356-b120-331a-ab17-d495f3b92a07 | -14.5829 | -52.48626 | 2025-10-04 03:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 81b52677-ddcb-3970-aa4f-5f128fa76ffc | -13.10149 | -47.88844 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cdb31484-667f-397c-ba44-a0b8b43db822 | -15.27824 | -47.14402 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3729ed16-cb0c-3dd1-b6f8-5273b8f50606 | -18.71972 | -40.00412 | 2025-10-04 03:53:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5ebef804-6996-3a56-b0f6-a8f49095d36e | -14.88972 | -48.29219 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f860ce9-5d35-336e-9a39-a90deb0d6725 | -13.32345 | -48.11286 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3e443166-3794-3f89-a99e-865a77414fc8 | -11.8342 | -44.91867 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd19b791-fb2a-3bc7-bf97-e8feef34234a | -12.11057 | -43.44938 | 2025-10-04 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eae6aef1-ba3c-3305-b9e7-4cd0b7ae49f4 | -14.23316 | -46.07603 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9fa59441-f6de-3e94-b974-fb9c774802e6 | -15.61537 | -46.94751 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d932cd8-0a87-326a-a6fc-5ca5918cc07f | -15.3471 | -47.81937 | 2025-10-04 03:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b3a78c6c-2157-3639-9aea-d2076c6e28d1 | -13.33244 | -48.09597 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c983509-0e1b-3d68-9d23-2f0ca0e32dea | -14.23749 | -46.1044 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| d3df67aa-d39f-3479-b695-47e5417378ee | -13.27718 | -47.21713 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 411294ff-42b9-3d12-9fc5-2c93282ce8e5 | -14.92431 | -46.90028 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3205b96b-40a3-304d-aa2a-514d25798b4d | -14.89432 | -48.35249 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9faf7de-df71-3832-906b-453524d45e8a | -12.8932 | -47.16404 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5331fd67-39b1-363b-a1e7-6612147e6c6a | -12.71108 | -48.57349 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67365ec5-614a-39e8-af70-b5826ebbf21a | -14.92195 | -46.87973 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58ab35b8-d034-3768-8641-973458a3be12 | -16.01284 | -50.94184 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d61dc6da-fae3-347c-8d40-4fd468c69dcc | -14.63663 | -48.25442 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| caf8eac8-efc5-3754-b053-92d0d2561f54 | -14.85131 | -48.2892 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 27f0ee4b-a6d4-3ffb-85e3-18e104adac74 | -13.22004 | -47.82456 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6bb6a8f4-8b87-3c61-82cf-91b1a72c2fee | -13.77897 | -47.82427 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ecba4b7-dd13-315f-bc7f-16ca9868c8e2 | -12.72143 | -48.55087 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f82e785d-b9c5-3b81-981d-733112345e0b | -13.14245 | -47.93649 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d182d36-2e98-33d0-93c7-ebb8a3d6991b | -17.15724 | -47.04399 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 34d916fb-f806-3ca0-8f98-2244e88df5da | -11.91422 | -46.38385 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| f548c32a-26c6-3bc4-acdc-9b0e48ad6ea4 | -14.22262 | -46.08027 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 49c866c3-ee55-3c5a-a045-c8444f645c5c | -14.68289 | -48.06709 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 359716e4-d65b-3413-88a6-f3046d6bc1f8 | -15.57121 | -48.18473 | 2025-10-04 03:53:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25c7f876-fc85-352c-b1a0-1553a4289029 | -13.93085 | -48.17336 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a6d3d8a5-19c0-3172-b6b0-547c82c6cc69 | -13.22138 | -47.82705 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77e04605-cd08-3adf-b571-9a267c4379dd | -14.68545 | -48.0691 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c425a7e5-d959-34cb-94ba-ed1580a642e7 | -12.95098 | -42.41972 | 2025-10-04 03:53:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1ed3292a-41b6-38c1-a4ad-8da7905234a7 | -14.3082 | -43.86074 | 2025-10-04 03:53:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b5bb6fe-d091-3b3e-9804-530940183d7a | -13.99171 | -48.20701 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81bf5ef4-8dca-3361-bb60-05c07b50136f | -14.3007 | -45.87271 | 2025-10-04 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 250a4df4-730d-3051-8f07-c9204938a840 | -11.2787 | -47.80417 | 2025-10-04 03:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d53d5fc-98d9-3812-9227-d190a80ac522 | -13.10281 | -47.88183 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63e97dc9-08ec-3988-8f81-632208e76c67 | -13.3494 | -47.20766 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af078dc5-f7f5-3fe6-8820-2fc3c28f4567 | -15.36809 | -47.95798 | 2025-10-04 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 281dc2dd-e95b-3517-bc8b-cc6fa03c9497 | -12.36779 | -46.51642 | 2025-10-04 03:53:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f783b66d-a983-3714-9937-8e7543ea64c7 | -16.01805 | -50.94763 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49f59ffe-0574-3f04-a5ab-fb97d298b607 | -13.27062 | -46.47638 | 2025-10-04 03:53:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd720d6f-5bc9-32a1-8256-bc5dce2f2b27 | -12.7255 | -48.56991 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22f67f57-3eba-3a1d-9de5-8abf4b298abe | -13.31762 | -47.25706 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 697019dc-12f8-3994-ba84-febd306bd0e8 | -13.33114 | -50.94636 | 2025-10-04 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c485d67d-8e6f-32e7-b471-0b9cea66f058 | -12.52736 | -45.96901 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7596c269-0c33-3477-b027-59eca873cdc1 | -13.562 | -44.09819 | 2025-10-04 03:53:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b1ed0c3-d494-39fb-a63a-3aa7994c8629 | -14.32661 | -45.86217 | 2025-10-04 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b87ba03c-e87f-35c9-a9e2-bf7b5772e3c4 | -13.33173 | -48.09958 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1b0c368-1762-348e-a21c-68a10ec24ae5 | -13.53102 | -47.2417 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a969829-04cb-3a40-949b-01a5b030547f | -13.16234 | -44.64126 | 2025-10-04 03:53:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66338728-817e-3480-afc6-52a3aeb00a71 | -11.91086 | -46.40163 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |
| bea3a228-e803-327b-bcb1-2f4f99e80da7 | -22.36895 | -47.05805 | 2025-10-04 03:55:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c33aa890-091a-36e1-8ec7-c85ab6e32045 | -18.54551 | -45.04868 | 2025-10-04 03:55:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f9c23fa1-e7cf-3a2b-a552-9cbafab6d1fa | -22.2793 | -46.76253 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 139bb11f-3ec8-3be8-be3f-33482641be2d | -20.46869 | -44.8163 | 2025-10-04 03:55:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8c65335e-c0a4-3708-8544-9aa10879ff7c | -21.34504 | -44.9942 | 2025-10-04 03:55:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d296d383-e23a-3fc8-bc6d-d83ad40f73ad | -22.48957 | -44.07496 | 2025-10-04 03:55:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fec23490-e869-3dac-ada8-74ffbf6609bf | -18.59737 | -51.17603 | 2025-10-04 03:55:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92ec7a58-6bb7-324d-81de-4563e708ccf5 | -19.96023 | -43.65007 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6b8b72b6-1346-3a71-8669-cb3d8bbc6003 | -18.46117 | -49.44743 | 2025-10-04 03:55:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 4dc277b6-4e09-354b-a0d8-c8635c889032 | -21.08971 | -47.76276 | 2025-10-04 03:55:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4436ad20-4b50-32a2-bce9-1496fb24a0cc | -22.12226 | -42.91563 | 2025-10-04 03:55:00 | NPP-375D | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d01f5d24-997f-3654-b573-1210fe493b6b | -21.49093 | -44.63988 | 2025-10-04 03:55:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fd5f1a2e-4aef-3d98-b0f0-3ce147ccb3ae | -22.49439 | -43.39225 | 2025-10-04 03:55:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9516f38d-caa2-3bbb-8a5c-f745ab6b571b | -20.76136 | -48.04441 | 2025-10-04 03:55:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afda229f-edbd-3ed6-ab25-783127fc7f05 | -18.58805 | -43.46867 | 2025-10-04 03:55:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c0265a8f-6b02-3755-86e8-f98fecb762bd | -22.36592 | -47.06131 | 2025-10-04 03:55:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| acb3ef55-4548-313f-9786-707c7fbf086d | -21.34524 | -44.99606 | 2025-10-04 03:55:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f8dd831c-2b2c-34b1-b7a4-c89aac7d6480 | -19.70002 | -44.44464 | 2025-10-04 03:55:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9dfaffec-5543-3b98-adc5-2be5bb7139f2 | -19.79672 | -42.08788 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c47e5aa1-a1f6-3f40-837e-8fe6fe67d8f5 | -21.85212 | -41.37236 | 2025-10-04 03:55:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e1834e5e-2894-3bf7-a495-b4d29cddaaba | -21.18721 | -45.12806 | 2025-10-04 03:55:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d03a9be7-98f7-33cd-8d57-f1c68d66935d | -19.28882 | -43.73014 | 2025-10-04 03:55:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d37911a-98b0-3a7e-9ac2-0dde43deb3bd | -18.64093 | -43.88337 | 2025-10-04 03:55:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d21fc17-cd3d-34c7-8886-a3809e24c479 | -20.43954 | -44.16727 | 2025-10-04 03:55:00 | NPP-375D | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6db8d52a-e4fd-3ee1-81fa-6a6b410870e8 | -19.59865 | -44.62501 | 2025-10-04 03:55:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7c7aed9-64e6-3498-932c-2b73b2ef5843 | -21.19605 | -45.14613 | 2025-10-04 03:55:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 83956907-65a9-3f17-afea-a9592ac8bef5 | -21.3443 | -45.00101 | 2025-10-04 03:55:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 863acb03-997d-3ee0-b0f4-0cb64ed5e27c | -20.59247 | -42.09285 | 2025-10-04 03:55:00 | NPP-375D | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5336ee30-0293-3bb8-bd4d-ea623442d4f5 | -21.66649 | -45.32239 | 2025-10-04 03:55:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4dffc2e0-4a21-3842-b362-508999988345 | -19.6004 | -43.8103 | 2025-10-04 03:55:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c1b8ce57-c2ed-3022-9788-247d4aa7d9ef | -21.25747 | -45.18342 | 2025-10-04 03:55:00 | NPP-375D | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e94c827e-c930-34b7-a0b1-a297ecb5d8af | -21.84877 | -41.37173 | 2025-10-04 03:55:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 73a23c19-b379-365c-8f17-6bbe2ea406c6 | -18.17339 | -53.36212 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 58000151-c01c-318b-81f4-b7e264866e66 | -19.96215 | -43.64784 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 68f2fc27-c60a-37b9-b60c-02ded2003bc7 | -17.16339 | -53.04445 | 2025-10-04 03:55:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95ad9661-bd12-3659-bd37-4209e9ecc704 | -19.00281 | -43.01632 | 2025-10-04 03:55:00 | NPP-375D | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 776c7ed8-fe54-3520-92f9-5c76b2a28974 | -20.38562 | -44.46034 | 2025-10-04 03:55:00 | NPP-375D | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 52ffe113-1ba3-319b-9105-939cc32a2c24 | -19.7965 | -42.09914 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7cf083b7-7a2a-34f2-a581-17041b902417 | -20.13145 | -43.98678 | 2025-10-04 03:55:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 72dbaa47-8af4-31b0-a4d2-df044af8d585 | -19.10758 | -44.70838 | 2025-10-04 03:55:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd8ed184-58a1-311e-a5e6-1cb71893077a | -19.96394 | -43.65062 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README47.md)
