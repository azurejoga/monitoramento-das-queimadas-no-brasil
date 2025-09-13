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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 473ad3b6-ce38-37e6-b99f-09c9e053e7ec | -17.43372 | -49.22056 | 2025-09-13 05:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfdef55d-399e-35d3-91e4-e91bf87c8326 | -16.49731 | -55.14474 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 600d1a38-8ad6-38b9-86dc-a72800730055 | -15.76933 | -52.23951 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c0cd16e-6d3c-3812-852d-1bc64ed0be28 | -13.23909 | -51.73208 | 2025-09-13 05:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47d4c9e5-f6fb-3159-8440-08cb90eee5fe | -10.66289 | -65.19953 | 2025-09-13 05:27:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1bcfdb9-62fb-352b-befe-42120db70d45 | -16.87908 | -49.34741 | 2025-09-13 05:27:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc121025-4323-341d-bc4f-04996f1f26f4 | -15.78827 | -52.22781 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ea1748f-b243-34ad-bfb4-2484c2291268 | -15.80759 | -52.21135 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29f9c9fc-570b-3212-b18f-8288d5193a93 | -15.11277 | -52.50464 | 2025-09-13 05:27:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bbb2483-5382-36db-9bf9-9a93ec745084 | -16.40789 | -49.03968 | 2025-09-13 05:27:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fda7213c-38ca-37a4-ad60-69e91d7dc715 | -17.37279 | -52.9113 | 2025-09-13 05:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7f403ec-3682-305b-a571-81ce5d3d8791 | -18.15705 | -49.19813 | 2025-09-13 05:27:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 823650c4-f943-3b0d-b567-5ebdda156eed | -13.11841 | -56.80231 | 2025-09-13 05:27:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cb022db-bfe2-3381-8a9e-4e05decf1b46 | -11.36899 | -59.13914 | 2025-09-13 05:27:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d063033a-3b01-31ba-9c83-203edf341443 | -16.36402 | -51.53846 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff68ac0d-c50d-31b7-8432-cd6fabd7d547 | -17.309 | -48.74126 | 2025-09-13 05:27:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9915b67-7735-3df8-ab22-e07f41bad601 | -13.25602 | -57.33102 | 2025-09-13 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb65e33f-9295-3acc-bcc5-1a942e8bb5ec | -15.37355 | -52.10741 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baa15d95-a94d-3e6b-b10d-fbcbf14c8acf | -15.68124 | -49.89616 | 2025-09-13 05:27:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 680a1df2-963f-3703-9b70-44f3bcf7a16e | -12.86353 | -62.12359 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53cc7c38-51ac-3f66-9830-56f91f012ece | -15.57555 | -54.77274 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b54c0896-7891-38da-9e71-f2a392a91ac7 | -16.41103 | -49.23614 | 2025-09-13 05:27:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e5eea50-1b04-3b58-8f25-bf92f2f50403 | -12.85964 | -62.12659 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1095f540-0d9d-38af-94e7-e41374167366 | -17.41543 | -49.24618 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3bcc7396-eec8-335f-9c53-d6369775a0f9 | -16.37057 | -51.53427 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b52a3ffa-9eac-30b4-94d8-d9498c1fd6b9 | -17.41638 | -49.25463 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97f4a035-3d0f-30df-a2c7-1fd152a8b7f4 | -14.38991 | -60.28763 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c266b6e-a3dc-3ebe-8160-4577a9478f5a | -9.96363 | -64.96361 | 2025-09-13 05:27:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec123033-4178-38d7-9ad8-f485ce919764 | -18.15399 | -49.19037 | 2025-09-13 05:27:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 86b1a9f6-3b04-3e82-9a8a-818d4f32efa9 | -10.63591 | -64.97598 | 2025-09-13 05:27:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 011ad98d-5d58-3204-aad0-9d7355f6f3ce | -17.41568 | -49.26224 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3470ca49-c5c5-381d-b09a-f2ad4d33ea69 | -17.43805 | -49.25015 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af3aca8d-1af5-397c-b9d8-677b6a128a51 | -15.69868 | -50.58396 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53f69e9f-765a-3009-9b20-956fd999ce2e | -14.46781 | -55.95979 | 2025-09-13 05:27:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf8047b3-027c-3db2-af76-76774f79a7bc | -15.23182 | -56.3269 | 2025-09-13 05:27:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f98b6b5-5f14-3002-b8ae-a15c4e6b610d | -12.86293 | -62.14891 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bead19bb-9e63-3f19-9b6d-339db31eb468 | -15.16499 | -52.496 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5834c93b-3631-36fa-b22b-ef1ce75f052d | -15.68296 | -49.9032 | 2025-09-13 05:27:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e8323927-91a0-3992-b7ee-7cd199f7d93d | -11.87679 | -62.76925 | 2025-09-13 05:27:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7238a44-8dd1-35ba-9269-c29c55214bd7 | -15.14309 | -52.48819 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 610c7096-4ef5-33ff-82fa-21183f98168b | -16.34062 | -51.52729 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1013e7bc-9a4f-34d9-8550-cd828d61276f | -15.58902 | -54.76976 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ab03c047-9d00-3fcd-82a2-c720ac083b3f | -16.50061 | -55.11669 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bf58498e-f660-35a0-ad48-db9e7f5cdd6e | -12.94727 | -48.00537 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a1a0df5-dada-365d-890d-318cb4ea6404 | -17.31624 | -48.74163 | 2025-09-13 05:27:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 419fe532-0031-3648-9b41-a9f1bf29a468 | -14.38641 | -60.31153 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49972edb-b2af-3da8-b3f2-ca107ebff789 | -16.53559 | -51.74068 | 2025-09-13 05:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f8f6154-6b43-3a7a-bb6d-62a40f4ac08b | -13.90654 | -48.21194 | 2025-09-13 05:27:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f97df9ee-4c9d-38bc-9310-5b6d961ba0a3 | -16.55836 | -49.22132 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a993bd55-a71e-3a23-b706-d9b90f8d58a1 | -16.56338 | -49.24249 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56150032-4675-339f-ae48-fe4a69f33319 | -11.774 | -64.94144 | 2025-09-13 05:27:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71d4da98-dd85-36da-a4e9-df907d518e8f | -10.66365 | -65.19501 | 2025-09-13 05:27:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb408413-6190-33eb-8459-f60f0c358c77 | -16.79039 | -51.35661 | 2025-09-13 05:27:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca31625e-f6a7-34e9-abe3-da6dc1d17d4d | -15.77371 | -52.25464 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 168f565a-81cb-3ed2-a853-e118e619f151 | -13.25929 | -51.70988 | 2025-09-13 05:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb9c1653-899d-3574-aefc-f34571fc6885 | -11.93604 | -51.13395 | 2025-09-13 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 421e50e9-e497-3693-8857-e7521c2d4deb | -13.4565 | -51.78057 | 2025-09-13 05:27:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0db443e-f4f9-35a6-a019-e94d287d71d8 | -15.17008 | -52.50122 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3b612e3-bf95-3299-a0d2-8257b918ac5d | -14.39006 | -60.29704 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f166f8d-98a2-3ce3-88de-e4ad71767787 | -12.94072 | -47.99818 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 04b25937-52fe-31ea-9f3a-08a1f72f904e | -15.76997 | -52.23523 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 778c48b8-2296-38c4-8841-39a9b4ab8485 | -16.33773 | -51.54107 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8faeed94-b028-34c0-b6da-c4f071037839 | -15.57904 | -54.74507 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 67bf69cd-23dd-35dd-98fc-50364147d2e5 | -14.73505 | -60.23594 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 770759c5-eacf-35b3-ac5e-43f8b30e99c6 | -17.41059 | -49.24065 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d652165d-d837-3700-b559-46549ad66f5c | -15.77569 | -52.23631 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8db55dff-6524-3c0f-a4fc-8a131958968f | -16.64558 | -49.77805 | 2025-09-13 05:27:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 836d742f-8bec-3805-9a95-981e027e1626 | -12.85908 | -62.13013 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db543a32-937b-3add-ba15-b3309d0d0374 | -13.27137 | -51.70685 | 2025-09-13 05:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03abf69f-3724-3d6b-8756-400d23bf4e34 | -15.77624 | -52.23114 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd439124-6646-337e-bd85-73b7d0438548 | -12.41674 | -63.88572 | 2025-09-13 05:27:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0161e84c-d78a-34bc-9910-3eee9b1cb285 | -17.23275 | -50.23273 | 2025-09-13 05:27:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d6ea548a-0ce7-3faa-9c00-24411c0daa9e | -15.67581 | -49.90738 | 2025-09-13 05:27:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 3be7eb60-a2b1-30b8-a4d3-3f2c03f07d26 | -15.78251 | -52.22712 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e659cfdb-17c8-35ff-a79e-f41eb03f7cb3 | -17.30235 | -48.73413 | 2025-09-13 05:27:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2c3d10f-829e-37b6-b826-27f5f4a2f353 | -12.17093 | -61.84068 | 2025-09-13 05:27:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1fbf5f3-961a-307c-a2f3-4de1ebee8141 | -15.77941 | -52.25579 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e092385f-5455-3c81-a152-9970324dc641 | -13.88708 | -48.26147 | 2025-09-13 05:27:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 00ebdb85-268f-35d5-b86f-5b4e0b22b6f7 | -16.56305 | -49.23831 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 763af372-a60a-3c0d-ab85-e560858b665c | -15.70562 | -50.57905 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4628fb00-051e-3f89-85fc-7d957a4839f1 | -15.11417 | -52.49208 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d97de02-f75f-3519-b7dd-dd3f8841ed5c | -13.47952 | -48.45272 | 2025-09-13 05:27:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2a87a3e-6fa0-36f7-a235-5ceb196d0fdb | -17.44411 | -49.24233 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc927c4e-fa96-3f3d-b5c0-1863d703c14f | -15.37978 | -52.10397 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a203d0ce-9b21-3d0e-bbe7-8592d3c785fa | -15.28592 | -53.77786 | 2025-09-13 05:27:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d940e7b9-ec3d-311d-9546-805f5d144fa5 | -12.38693 | -62.20532 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 588ba1ec-62f8-34d5-a98d-5ade2b855859 | -15.29038 | -53.78463 | 2025-09-13 05:27:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d26ccfe6-ccfe-360c-bdb5-bee97f090b46 | -17.43647 | -49.24863 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03d3383a-3f7c-364f-bc88-c59f49ffc6c6 | -15.17346 | -52.32105 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35c0b3fe-565e-3330-aff8-ca949dcf38a6 | -15.2211 | -56.69293 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8570ab4-ab51-3ee5-b1e0-f0409adbcef5 | -16.49364 | -55.14325 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3a3d6fee-8ad9-3079-b58b-0212031f8b58 | -15.59941 | -54.7654 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 907e628f-a55e-3a49-b041-e2a729c9ee0b | -15.77034 | -52.2307 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ee29faa-e6ab-3c22-a34a-f6fac3b0bc07 | -17.41667 | -49.23183 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cffb10e-e051-33c5-9874-6798c0b46d1b | -15.76978 | -52.23555 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba21dd8b-d7a2-3aa1-98ec-d8f51661577c | -15.20276 | -56.67844 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc91e1f8-4067-3562-ba24-4727b3c27afb | -17.42249 | -49.24649 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de0be6db-1880-3478-b5e1-fa1c59c2c0bd | -16.40897 | -49.04752 | 2025-09-13 05:27:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efef3a0b-c0d1-3610-bafe-6d09ff514f7f | -15.68012 | -49.90776 | 2025-09-13 05:27:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 93d5d5bf-7cf9-32e4-8c9a-d71332cf3fcd | -16.41022 | -49.03471 | 2025-09-13 05:27:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README111.md)
