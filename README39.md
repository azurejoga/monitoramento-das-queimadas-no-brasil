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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7191d245-f108-32eb-bc00-2150ae972a7e | -28.72033 | -55.65832 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 96f46ad1-3993-3c18-8b2b-17f12a0c4baf | -29.02822 | -52.36923 | 2025-08-30 04:25:00 | NOAA-21 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5fd14c84-fe01-3dde-b399-29cafde9f9d5 | -24.37884 | -50.73273 | 2025-08-30 04:25:00 | NOAA-21 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e7831c49-49ce-3f33-9cbc-0de122aa8d94 | -22.84603 | -47.48969 | 2025-08-30 04:25:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| a364e5f6-d049-3387-96cc-ca7f6d3d40f9 | -28.72424 | -55.6593 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 214c9020-51ac-3d79-916a-e3723cac6831 | -28.71039 | -55.58432 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| ce07502c-d028-3853-88de-a9ecfc5a7190 | -29.9516 | -51.61779 | 2025-08-30 04:27:00 | NOAA-21 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| defa265e-0494-35be-9e7d-b937fb132f74 | -6.1853 | -43.3257 | 2025-08-30 04:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f12881aa-1cb0-3e14-a00a-76a3e585d63b | -9.462 | -60.549 | 2025-08-30 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f6d71cc9-6a6c-3a3a-b53b-dca2d1ce4098 | -9.0799 | -65.4349 | 2025-08-30 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 60360dce-20fe-305c-9dfd-5bba2d8662aa | -9.1155 | -65.7699 | 2025-08-30 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| eefd0ffe-2fbf-356e-9e25-2063ebc1a472 | -9.4433 | -60.5499 | 2025-08-30 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 81dc1cc9-f27b-36e5-8397-6746061fc367 | -9.0614 | -65.4355 | 2025-08-30 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 91aae1fa-e0d0-3ea8-bde0-e086ce15a3ed | -6.1665 | -43.3273 | 2025-08-30 04:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| fe448b2e-8a05-3017-8c43-aa1fe92237cd | -9.4432 | -60.5692 | 2025-08-30 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d1dba581-4aa5-331a-b868-85e22070b754 | -9.1156 | -65.7513 | 2025-08-30 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| a3944947-c98a-3702-a4c6-8c45ad99b5cb | -9.4435 | -60.5307 | 2025-08-30 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 7c2b680f-cc06-3ba0-b50b-8909dd363617 | -8.9126 | -62.1058 | 2025-08-30 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| de126207-9818-3a2d-8987-ebc42bfdeeaa | -9.462 | -60.549 | 2025-08-30 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| cf96bbbf-4100-3508-a106-e33d1f088df3 | -9.4432 | -60.5692 | 2025-08-30 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e19b6cf7-f205-3381-ae61-2068adf99e2f | -9.4435 | -60.5307 | 2025-08-30 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 60c73a8c-fcac-3d2d-9d86-9cb7540a1038 | -9.1156 | -65.7513 | 2025-08-30 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e4c8ec75-0810-3ac1-84df-875bca869236 | -9.0614 | -65.4355 | 2025-08-30 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 84144c2d-f72b-32f2-8641-42b8f0ad647a | -9.4433 | -60.5499 | 2025-08-30 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 6dbe9c58-3763-334e-bc35-72c7ac1d3469 | -6.76531 | -43.78806 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f0f6e10-2fa8-366e-8b83-ceb38dd23309 | -6.2358 | -41.81378 | 2025-08-30 04:46:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 089613c0-a290-3723-8afe-ca78b9dfa69a | -3.85128 | -49.28806 | 2025-08-30 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bf6baf1-6c7f-362a-b53e-0f9a92492d8d | -6.17387 | -43.32436 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 991b34f9-daa2-30ef-a9f7-c8159dfe87d8 | -6.56452 | -44.21775 | 2025-08-30 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f5b4a65-b09f-3064-91e9-1e87179874e3 | -6.16871 | -47.28251 | 2025-08-30 04:46:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a30720e-d12a-325f-b1ca-1b9009bce8a0 | -6.4525 | -44.63866 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c2cf8b0-e2aa-36cc-a481-ae61b50f8cdd | -6.5023 | -43.54594 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20f12ba7-ad49-30b7-859c-78552703f86d | -5.87805 | -42.96522 | 2025-08-30 04:46:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c15c1e11-4a1e-3f85-a80c-f54d65410c14 | -5.72596 | -45.53708 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8eecf96-8fa5-3b0f-89fc-d6c3c345e069 | -6.18511 | -44.7866 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e70a0db9-e634-3b39-8b3d-dbe010beac41 | -5.69541 | -45.96108 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3de7f030-4749-3b7a-8bb4-c50c6a8d160f | -6.77542 | -43.78444 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8c7f6444-38e7-3382-bac1-5e8d8e0d0c42 | -5.42941 | -45.52005 | 2025-08-30 04:46:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 869ad5ca-e22d-3532-bf05-8b4de9b4be94 | -6.56691 | -43.67691 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8c81c21-ac49-3415-bb66-aa15abf7ba33 | -6.48556 | -44.41046 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ef8b790-9576-316b-bc0a-a21be9c2d261 | -6.54711 | -44.43974 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c1d6fc8-0640-3d32-bf11-055f796c927e | -2.89337 | -49.4806 | 2025-08-30 04:46:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64acd2c5-568d-347c-a4c7-708df1a8e83f | -6.49985 | -43.52903 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d446c91-43a1-3b74-9e57-7e685f236482 | -4.37776 | -48.06935 | 2025-08-30 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e611fa7-6604-3047-83ea-b638826f48da | -5.77512 | -45.3892 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f350d247-c94c-3ff0-8e30-a3749b082e52 | -6.24178 | -42.40724 | 2025-08-30 04:46:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 92babfe6-658e-3612-b86a-2728344bb52d | -2.31035 | -46.99459 | 2025-08-30 04:46:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cba7db1-b553-3d31-849c-b5da95261061 | -6.66002 | -43.94095 | 2025-08-30 04:46:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eb8c607-a6a1-304f-8008-614cf6c479b1 | -5.87686 | -42.96455 | 2025-08-30 04:46:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 905f8df9-846c-3c03-a1bf-84c9ba78d4d0 | -5.69617 | -45.95592 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be3527ab-dca9-35ac-8440-bd59a7e1bed2 | -6.2366 | -42.40685 | 2025-08-30 04:46:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 375acaf0-bf02-3c79-af84-3a333eff9389 | -5.55215 | -42.63934 | 2025-08-30 04:46:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c3769e22-efe0-3eb2-b576-aea4df792b67 | -6.41094 | -45.59902 | 2025-08-30 04:46:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf3d767e-a3a0-3d02-8cea-202f8756eeb0 | -2.98432 | -48.60635 | 2025-08-30 04:46:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a523bd1-bd8b-3e29-b802-395bdce8387f | -6.66139 | -43.93145 | 2025-08-30 04:46:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba558582-602d-3f11-8f09-edcb3ef75dcd | -6.10126 | -43.18284 | 2025-08-30 04:46:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.9 |
| dab89fd9-b9df-3ed2-9278-35c0d23de6b4 | -6.18276 | -43.33101 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 350a8ef6-808e-3293-a60b-3dc446177bbf | -6.49284 | -43.54413 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15d2b2f3-46ac-301d-8bb8-ae7366439e9a | -6.56475 | -44.21593 | 2025-08-30 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b16f289e-069c-38e6-8923-972ec19deb98 | -4.41749 | -47.60587 | 2025-08-30 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 681826b2-8ba7-3467-88e0-ae985f6594ba | 0.89658 | -60.43415 | 2025-08-30 04:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 744339b2-93a7-3f68-b6bb-2ac3182dc6fe | -6.76461 | -43.79301 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 258de409-7ce5-3a7e-9af4-b9519bb3c357 | -3.36213 | -43.37381 | 2025-08-30 04:46:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf43173c-afcc-351a-b430-dd0cf72de3e5 | -6.24069 | -41.81773 | 2025-08-30 04:46:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 065c8e91-4d21-3447-8a3a-9775e309ac53 | -4.89947 | -55.84531 | 2025-08-30 04:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a19bbd49-fc0c-3778-84df-1e33f637edfe | -6.5622 | -43.67605 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b579d5a8-a630-35c7-b217-666869316169 | -4.89886 | -55.84902 | 2025-08-30 04:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dd6f30c-228a-3ca7-89f0-94dac650d589 | -6.66156 | -44.37844 | 2025-08-30 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96f75cd6-49b3-3e75-8320-2601dee6bf56 | -6.17462 | -43.31907 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adf2c294-7fd5-3700-ab1c-ecd1a4692cd9 | -6.00216 | -44.72027 | 2025-08-30 04:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de0d8a00-a82f-34b1-acd9-b15a80b2325d | -6.54036 | -43.10258 | 2025-08-30 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a3ab14c-74fe-30c6-bb17-3cbfa40c2200 | -6.56153 | -43.68081 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b08f2d27-6a3e-3c36-9634-83a180922505 | -6.17945 | -43.31964 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 020615ec-edd8-3da7-8dd6-dc127922b7c4 | -6.36152 | -44.46077 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17732391-8b80-3234-8a90-404b257acefd | -4.87375 | -46.8504 | 2025-08-30 04:46:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e202a875-1d8b-3e42-88a5-ab22a4dfb82f | 0.89045 | -60.43513 | 2025-08-30 04:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8283e70f-300c-3f18-b4c6-e20e9847b92a | -3.85326 | -48.98949 | 2025-08-30 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8b050782-f9ac-38cc-95ac-79e77d946f42 | -6.23153 | -42.40568 | 2025-08-30 04:46:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d79c072-598f-3d14-ab68-ba9de357cdd4 | -6.5964 | -43.63931 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 69578d6c-7515-3d96-83d4-169e02f13f99 | -5.61656 | -45.00175 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b9ff5ac-da24-3e4c-a0b6-6cc5c39e771e | -3.42564 | -49.04456 | 2025-08-30 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53278eb5-bc31-3129-a3a8-9347776334ac | -3.06986 | -49.45768 | 2025-08-30 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1267afe1-3713-3cb1-a753-f4eb81802fd2 | -3.42227 | -49.04404 | 2025-08-30 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03d389fe-e6c3-315b-b429-6920bc5ea2c5 | -4.37511 | -48.06872 | 2025-08-30 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f647479b-e63a-359c-aa79-382571cb9832 | -3.49389 | -48.94511 | 2025-08-30 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c542fce-1a7b-35ff-aa05-543397053b5c | -6.42098 | -44.17693 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2c1dfa56-8eb3-383e-bce3-054868dfef9b | -6.00156 | -44.72441 | 2025-08-30 04:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2008b3c9-8149-3315-8bdc-0b69de39a79e | -5.82387 | -46.36238 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4797ac46-cebf-392a-a497-0d749b123719 | -5.99781 | -44.71961 | 2025-08-30 04:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cdf197ca-dd12-3871-b5c6-1255b6d72486 | -6.41563 | -45.59584 | 2025-08-30 04:46:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 669f01b7-431e-38f6-b9e0-04517c0b9887 | -6.52688 | -44.86367 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 290cc6f3-981b-3952-87ea-16a25499829a | -6.06144 | -44.95837 | 2025-08-30 04:46:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67b4f7f8-ca4e-383f-8725-c900d26500bb | -1.29455 | -55.74931 | 2025-08-30 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13a48da3-b8ff-3106-b462-2117d012b6e1 | -5.69142 | -45.96049 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f9f7932d-beb5-3eec-a07d-03edd0ac75ec | -6.77471 | -43.78942 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94259cb3-08da-3926-953f-19e5cf24c41d | -3.64406 | -48.45117 | 2025-08-30 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a38df0ab-6a70-3bd9-80ce-1a0880cdbef2 | -6.17314 | -43.32961 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 437ab860-a59f-31f4-8dfa-58b0ac4c1743 | -4.87001 | -46.84982 | 2025-08-30 04:46:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3aaca688-bbfc-3d79-8305-53a71ce3e733 | -5.82345 | -46.36397 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cb9e8eaf-6bf0-3940-b242-6234be24bc9d | -6.56084 | -43.68569 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README40.md)
