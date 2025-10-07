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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92da93bd-37a4-3816-921c-4b832e24cdfd | -14.63316 | -52.50189 | 2025-10-07 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14f284d4-7faa-3f9f-8fc9-f28a93e6b2fc | -14.6204 | -52.48526 | 2025-10-07 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4b5f8af-3553-3c3f-89f0-a176cf624975 | -15.88555 | -46.24817 | 2025-10-07 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7561dbc9-9678-3d01-9cb1-8aaa697bc0a7 | -13.9912 | -53.91553 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7a346003-da4a-3066-966d-3aa7c3d8cbe4 | -13.31724 | -47.76702 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fa61db7-da1f-302a-a408-5126ecdab330 | -13.24582 | -48.06435 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04f924ad-f468-3b3e-a5c5-8ea6adfa06ab | -12.17885 | -50.92804 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6b56b2fe-7729-3b66-8512-fb1ac38cefe9 | -13.32936 | -47.55737 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0f4dc1f-6001-3083-817f-a97abdbbea6e | -15.58694 | -52.55275 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae8d9e90-e3fe-35f8-8593-e42b590ae348 | -18.11052 | -53.34695 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0762c376-812f-3da6-920c-841f76366868 | -18.67564 | -44.04118 | 2025-10-07 04:10:00 | NOAA-21 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e2d36aa-1d04-3a76-a331-12588e6e58bd | -13.37603 | -48.03598 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 939addb0-c90a-305d-a743-cef52a2d03a0 | -14.738 | -46.02283 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 1468b2f6-7abc-3878-9ecc-6cef0d5afeb8 | -16.00237 | -50.95873 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8f7a5b9e-1a02-3f8f-9808-1ebb97d6a24f | -14.61838 | -52.48732 | 2025-10-07 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7db0a74-4ca8-39ab-8549-c4b722f8c961 | -16.06146 | -50.92107 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c72ce5a9-a2fd-33ca-921b-a6261b2c0dcd | -13.07898 | -47.88488 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0331d4be-e0fb-3211-b619-6ac6d99244f2 | -12.2362 | -47.85564 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f32cef7a-4e00-3145-835c-7cb8dd0b3034 | -14.73384 | -46.02623 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e91b9541-49c8-3c2d-8652-675810d3c1e5 | -13.78904 | -45.78559 | 2025-10-07 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d80294b-4e1b-37c6-a894-6b2567d2beb8 | -14.6416 | -52.54043 | 2025-10-07 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba133d73-cda2-327a-aca9-92614714e557 | -20.55994 | -41.70342 | 2025-10-07 04:10:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d8d2ab3a-db8f-386b-88c4-d1d8c45f1ae2 | -15.9124 | -47.79573 | 2025-10-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 086a2657-357e-33dd-b2ea-5397f59af053 | -16.20179 | -43.65621 | 2025-10-07 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28d9e513-0b46-3249-9228-1ac8dce7c8ce | -13.26746 | -47.57193 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44987384-a4b9-3eb8-95de-f72b3176a69d | -17.56496 | -46.07763 | 2025-10-07 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de357479-cf59-3f77-9915-a5797f911411 | -18.45178 | -49.43073 | 2025-10-07 04:10:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2085f2ad-68cf-3950-9aff-c63f9ba83c7f | -14.7119 | -43.95545 | 2025-10-07 04:10:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e010e3e2-dde3-3463-9a41-686052a5bd38 | -18.11508 | -53.35072 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ac122944-dffe-3049-9e26-af600246feb2 | -13.01352 | -46.65276 | 2025-10-07 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6d56d8f-93ab-3bb4-896a-41d06217b6f5 | -14.92523 | -51.44869 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a9c4d53d-93c7-3ce5-8229-e6d97cca3c22 | -14.53906 | -46.63812 | 2025-10-07 04:10:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aad4244a-3f58-3646-b9a8-135fead2bfcd | -12.98997 | -46.79065 | 2025-10-07 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dab8597f-e468-32c9-b24b-af0841b723f1 | -15.60325 | -47.29676 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b19e8164-517c-31c4-9d9d-152c243bddba | -15.37149 | -47.30918 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9df11b18-b8f0-391c-9c8f-7f2d43615540 | -14.7672 | -46.01966 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 43aac86d-f299-3b2c-8752-9c0a1a7ce5f1 | -15.97217 | -50.84154 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cc19a4cf-cb06-3a05-9967-2e73f8d0d822 | -20.11778 | -44.41324 | 2025-10-07 04:10:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7b851354-f234-34d1-a1bf-d63514028929 | -13.08625 | -47.8667 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fac7992e-d12d-3a86-ac2e-09db1fc9d432 | -12.89923 | -54.74816 | 2025-10-07 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 65a912ea-89da-3cac-b282-b209fab4f36c | -13.08781 | -47.81131 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b293203b-3c2a-3823-9186-2c0b7b424256 | -13.36748 | -50.46443 | 2025-10-07 04:10:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d81bdea1-1fc0-3a3d-b8dd-5ed3909387d0 | -14.75474 | -46.02987 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69d8cad3-e798-3839-bfd3-1cc9e2772e29 | -12.40193 | -51.13795 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5cddc983-8957-3add-82fc-0b349ed8bd3c | -18.88438 | -48.03588 | 2025-10-07 04:10:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 89b9f2a4-a206-36e3-ad82-506735ab9fea | -13.25072 | -48.05963 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adf63641-a835-3692-9376-7056cc0712e2 | -17.61026 | -46.68925 | 2025-10-07 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d2f5768-da79-3324-b872-54ab9f38f3bb | -13.03183 | -51.02774 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ccbb4f9-1c39-3304-bf6d-fb7da6f4890a | -12.98637 | -51.03022 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4656fe7b-2db8-3bfe-a18d-289dfeb5e5f0 | -16.11387 | -48.94514 | 2025-10-07 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6a198319-ca33-3803-86bc-36c19a53ab82 | -12.976 | -46.7835 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f32f6f2-121e-3f43-a840-539ca414160f | -14.76587 | -46.02765 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f63ca5d8-dbc0-367b-86ea-4cdb4cf6aae4 | -16.34919 | -48.1284 | 2025-10-07 04:10:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39891f3e-567c-3e1d-9b23-7d8b3a25ce77 | -12.93776 | -46.7925 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4076ab8-d314-3e73-9d0c-544f6631a3e3 | -14.9134 | -46.82695 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0869c6bc-dedd-3cf2-a9b3-40958f55dcbf | -18.1084 | -53.35737 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ace040b-af71-3608-8177-57f99cd1b8f4 | -15.59891 | -52.5722 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b48f5f76-4b31-33ea-9aaf-0f7870356ce3 | -16.19794 | -43.65923 | 2025-10-07 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18d53f2a-e48c-3d35-b713-b9374c50d4c4 | -15.90865 | -47.79504 | 2025-10-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 60434980-a522-3c76-a10c-decf0225b7bf | -15.05474 | -42.33599 | 2025-10-07 04:10:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6227ea06-671a-342d-812e-0cc8145a43f0 | -15.19953 | -56.82129 | 2025-10-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a704b2f2-c5d2-3c34-b07b-fcef1c981621 | -13.271 | -48.0767 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf4af030-10fc-3d9b-995d-5c56c285ac46 | -18.60253 | -46.79713 | 2025-10-07 04:10:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ffd7c69-a91a-3e34-807b-6a23987dd05b | -15.99878 | -50.94962 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5854f7f2-0145-3653-84da-c9d7ac7c930a | -19.59272 | -47.20377 | 2025-10-07 04:10:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21e4ca11-b945-36b2-b4bd-b746658db0c6 | -15.32325 | -46.3049 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b085896-b624-39ed-98f0-21450b9d25e8 | -13.29552 | -48.05371 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87aacf3e-171d-37fb-8756-d393ab07bde6 | -19.39686 | -44.39074 | 2025-10-07 04:10:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 440f5908-18fc-3ae4-a919-b97accb2a149 | -14.77232 | -46.05344 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 27f55715-1072-3802-9dc7-6e0c7d9ab423 | -16.10653 | -48.94006 | 2025-10-07 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1545fed2-8717-36a2-a8db-288a4ca5e283 | -15.3707 | -47.31371 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c424b69-efa3-37c1-9cb2-870aa7af8744 | -14.66121 | -48.39221 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ee569cb-23d8-365b-8604-84617f72581f | -14.91921 | -51.45101 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c33750d6-eb7f-3eed-8f1f-0f121c0502bf | -18.92224 | -49.48718 | 2025-10-07 04:10:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 43daef78-584c-3795-8713-37145f4c62ff | -15.3505 | -47.32541 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e5c8194-f5d3-3ba9-a3bb-0282b004221c | -13.37831 | -44.30891 | 2025-10-07 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67be4d9f-5fd0-3d43-aa0d-e9e737452b49 | -16.0029 | -50.82756 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e5af870-87c4-34b6-ba54-be94196c2b52 | -17.98138 | -44.99243 | 2025-10-07 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e08efec-26b8-35ba-bf08-ff110d71193b | -18.28346 | -45.46024 | 2025-10-07 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 13774aad-321a-397a-b44b-717aaa70999b | -13.38627 | -47.53942 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 70fcac82-bf41-382f-bd96-6194d6a17fa4 | -13.31787 | -47.76906 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 535efcf9-c2e5-380e-84af-12930e0aac9a | -13.07496 | -47.88466 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aaebd7bd-a708-3b58-9d97-015ba6c9acfa | -10.88045 | -56.06826 | 2025-10-07 04:10:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 08891a51-8601-3688-b2f9-3947dfb7f87b | -18.52561 | -43.42166 | 2025-10-07 04:10:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 584f9834-7bcf-3c78-9759-e6bb47e900f1 | -18.93008 | -49.48895 | 2025-10-07 04:10:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 036d07f2-10ba-3b1f-9e2c-783e200f253c | -13.27981 | -48.47079 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e4d6744-b55c-3081-9f08-d89ace289646 | -14.93132 | -51.41634 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 87362252-8dac-3cd0-bc5e-c09b3ebc6525 | -14.76965 | -46.06945 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| c3274828-4321-3862-a61b-74b70b64f61f | -15.44005 | -49.09867 | 2025-10-07 04:10:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 227009bb-97a3-3bea-8656-7b272387db5a | -15.26973 | -48.0617 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10d03999-7b29-39b6-99b2-dd2b61482e1a | -13.98973 | -53.91605 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 25e8e912-1b40-38ef-8b58-be6e7b6669a2 | -12.72562 | -47.93908 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 700b5058-7850-32d5-a927-bfa1bfa7f386 | -15.51586 | -46.84083 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ac29a80-3fa4-38d2-9681-be17aaa31400 | -15.57979 | -52.56194 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d46a4f91-6a30-3c93-a322-23775bd277b4 | -20.21353 | -43.92056 | 2025-10-07 04:10:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9f906252-4094-321e-83f3-dee76241a98d | -12.41175 | -51.13987 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31231560-4ef2-3927-907b-dc25709bd9f9 | -14.93892 | -46.80824 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91557348-eb24-39b7-9dc9-e5a06c78f532 | -18.10911 | -53.35387 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ebae7bb1-ee27-3495-95e5-254d8e2e8527 | -20.10471 | -44.18884 | 2025-10-07 04:10:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c19ce805-9626-3acc-8463-1a78504448fc | -14.76682 | -46.06486 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README39.md)
