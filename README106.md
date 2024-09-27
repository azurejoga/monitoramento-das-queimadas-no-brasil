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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 161881d6-7974-36b3-aa78-b6372a3697bc | -16.08345 | -51.99034 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4f8bb31-385a-3725-afff-8b0657e981a1 | -15.94762 | -52.37292 | 2024-09-27 04:42:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e827dae3-e7b6-302f-8b15-a548edfd52b6 | -15.94704 | -52.37652 | 2024-09-27 04:42:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a66d9944-198a-3bc4-8479-4b72d65adc3b | -15.94372 | -52.37596 | 2024-09-27 04:42:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 999c3fb4-3832-375e-84ca-01c0e7ec08b8 | -17.90969 | -53.67053 | 2024-09-27 04:42:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1bbd478-eb4f-3f9b-9f3d-b3282a3a8936 | -17.90693 | -53.66618 | 2024-09-27 04:42:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d81dc132-3478-3227-889f-f7f66c39060b | -17.90631 | -53.66996 | 2024-09-27 04:42:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3aa80b58-4dcc-39ce-acf6-db607ed0ef7e | -17.1856 | -53.45382 | 2024-09-27 04:42:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7fa9068a-93aa-35e0-ba49-474c5bf42139 | -18.65823 | -52.47062 | 2024-09-27 04:42:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 419bb3f3-3631-3997-8d81-6f2ffc9909f7 | -18.6555 | -52.46642 | 2024-09-27 04:42:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 189b67e7-5dbd-378b-85c4-232c08c105f4 | -18.65277 | -52.46222 | 2024-09-27 04:42:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8035b5b-8178-3b52-b4fa-c185f7f35f38 | -12.83379 | -54.01323 | 2024-09-27 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 07b47529-3303-37b4-80b0-12863f230205 | -12.83021 | -54.0126 | 2024-09-27 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 08d6bdc2-f63a-390e-9746-543b830cf43c | -12.82663 | -54.01197 | 2024-09-27 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f7be6430-db5a-38f2-ac4c-32fa145c3597 | -12.8116 | -54.01366 | 2024-09-27 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c54aabcc-f97e-3426-b38c-29a76019471f | -12.80443 | -54.01245 | 2024-09-27 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 112dfe28-52d1-31eb-9d90-81946b231e76 | -12.80014 | -54.016 | 2024-09-27 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ff5135e6-4a45-31fc-855f-43181168a191 | -14.97892 | -53.61375 | 2024-09-27 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32566b54-7dd3-392c-95ad-729c81e0f04b | -14.96794 | -53.61583 | 2024-09-27 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80f8277d-6c24-3e9e-973d-388b54212699 | -14.96491 | -53.65536 | 2024-09-27 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 862bc3c8-2661-3152-acd3-395a767d50dd | -14.9645 | -53.61522 | 2024-09-27 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cef7b126-7114-3b2e-97b3-0cf13854a436 | -14.96147 | -53.65475 | 2024-09-27 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0983fff3-9c0f-3d4a-94ca-c112f4014e54 | -14.95195 | -53.66925 | 2024-09-27 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c9be57d-e116-3330-8f7f-f1fb48325d7c | -14.9513 | -53.67316 | 2024-09-27 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a13560f-c70c-3861-8f4f-23f9b8e722e5 | -14.9485 | -53.66864 | 2024-09-27 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 059e0642-6074-3418-b019-6c88ab3d94c5 | -14.82014 | -53.87 | 2024-09-27 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a1001bc-2bd2-3c33-9925-8d07eabd0e08 | -15.48841 | -53.38481 | 2024-09-27 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e43be85-ce57-3323-8eae-683d833f739b | -18.83783 | -54.51886 | 2024-09-27 04:42:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22f810a5-6911-360d-ad61-41d329b839c0 | -18.83298 | -54.50562 | 2024-09-27 04:42:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 362472a8-63d3-30e1-a418-6ece99a57a12 | -18.8124 | -54.5017 | 2024-09-27 04:42:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 722f640f-7db1-3957-9e8b-01f7e7f1abf7 | -18.17224 | -39.81891 | 2024-09-27 04:44:00 | AQUA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 69f0bdc1-830a-36d9-89c8-2d430b4e8b4c | -17.4219 | -39.34851 | 2024-09-27 04:44:00 | AQUA_M-M | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 7c8dd4bf-415b-34ef-83f4-7edd573b132d | -17.0726 | -41.1402 | 2024-09-27 04:44:00 | AQUA_M-M | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 686944eb-551c-33e8-be26-ebf9e5a56e71 | -17.07108 | -41.14982 | 2024-09-27 04:44:00 | AQUA_M-M | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| c0223421-265c-3df9-969f-5ca642001483 | -17.06345 | -41.13858 | 2024-09-27 04:44:00 | AQUA_M-M | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| b85a1984-4c88-3ae4-ac3c-6569e721564c | -17.0619 | -41.14834 | 2024-09-27 04:44:00 | AQUA_M-M | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| baec505a-7f77-329c-b424-8522842a3bc7 | -16.85585 | -47.74026 | 2024-09-27 04:44:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| f642e695-0fa3-3b12-814d-71de7fcdae47 | -16.85016 | -47.76915 | 2024-09-27 04:44:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 5c2be424-22ed-3f9a-a515-d5c53a35501c | -16.84816 | -47.76331 | 2024-09-27 04:44:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 90df8d28-71e2-3131-b1a3-712cb036f94c | -16.82484 | -47.72777 | 2024-09-27 04:44:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 33fffbe2-57f6-3a21-88c4-cb6e862bbc37 | -13.43463 | -44.01424 | 2024-09-27 04:44:00 | AQUA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 3f4943ab-a919-3f0e-893c-0662e7d52766 | -11.19505 | -45.54629 | 2024-09-27 04:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| d697f6c6-d5ea-3993-970b-3496c5c7cd89 | -11.18818 | -45.55106 | 2024-09-27 04:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| fb43fd03-505c-35cb-8c65-fe16e3bbab79 | -7.25742 | -44.94317 | 2024-09-27 04:44:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| bbaa04ba-1141-317b-8b64-c0921bc3523d | -7.25319 | -44.96801 | 2024-09-27 04:44:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 4ad6fc47-7ed0-3611-976d-5eddc9ecf356 | -7.25273 | -44.93697 | 2024-09-27 04:44:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e3c5b7ac-2583-3a24-851c-328750999448 | -7.24868 | -44.96181 | 2024-09-27 04:44:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 3251ec77-395e-3b77-895e-6adb2bd4e767 | -11.24191 | -47.11726 | 2024-09-27 04:44:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| f8bfd73f-9d26-3627-816e-71fdad063680 | -11.25372 | -47.12491 | 2024-09-27 04:44:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 8de6317c-4394-31a6-a373-5078e4421dce | -20.90157 | -41.36482 | 2024-09-27 04:44:00 | NOAA-21 | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e95234d5-9994-3388-8dfe-548ce056cae8 | -21.74465 | -41.36893 | 2024-09-27 04:44:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ed947514-8750-3708-b33b-20c9e4355780 | -21.74426 | -41.37371 | 2024-09-27 04:44:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 00828aaa-5b99-3b1b-911c-86ee6c775908 | -22.87674 | -42.48282 | 2024-09-27 04:44:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 3f387865-32e3-39ba-9a7a-b9bf5f1f0f33 | -20.97788 | -42.40948 | 2024-09-27 04:44:00 | NOAA-21 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 876bb3ab-25d0-3f8b-9e87-e1fcf4da3d11 | -20.84513 | -42.63236 | 2024-09-27 04:44:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7a594049-d46c-34a6-8e73-e7061a1e74ec | -20.63126 | -42.29398 | 2024-09-27 04:44:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6f7c3b20-6e82-321e-8690-94e8ac492cd6 | -20.6232 | -42.89996 | 2024-09-27 04:44:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1e909a35-c92f-32c4-91ed-c756c64c0764 | -20.6178 | -42.8993 | 2024-09-27 04:44:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2c5a4ebd-5003-3a77-8488-d9bb71d85367 | -20.97833 | -42.40462 | 2024-09-27 04:44:00 | NOAA-21 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5ac43741-5743-3c4f-b9eb-dba605682025 | -20.61815 | -42.89576 | 2024-09-27 04:44:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| d9606ee8-d73e-34c0-a42b-63ab68c58bf8 | -20.61744 | -42.90284 | 2024-09-27 04:44:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7035830d-b5dc-3b70-a435-5ccf0fae10a3 | -20.60557 | -43.07614 | 2024-09-27 04:44:00 | NOAA-21 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| adad5c02-ba12-3eae-918c-2efe87e20d63 | -20.50046 | -43.48808 | 2024-09-27 04:44:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6010ac7c-f26d-3f1e-a979-87669d26341f | -20.50011 | -43.49165 | 2024-09-27 04:44:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 38fdb112-1194-378b-b630-31e9a82f194d | -20.49942 | -43.48569 | 2024-09-27 04:44:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 718078fd-5999-3e67-8b0d-b87451ca9b89 | -20.49906 | -43.48912 | 2024-09-27 04:44:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bd53d735-3b13-355c-96e7-a6e3ab40daa7 | -20.49868 | -43.49265 | 2024-09-27 04:44:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8c8c1d99-3c90-3900-bf13-93446e28dddc | -20.62563 | -43.0385 | 2024-09-27 04:44:00 | NOAA-21 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 357b8196-06e4-3b80-8aee-3cae8cae1d11 | -20.62524 | -43.04232 | 2024-09-27 04:44:00 | NOAA-21 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d3a9c92a-b548-3127-a6ce-f7c395f08900 | -20.6006 | -43.07178 | 2024-09-27 04:44:00 | NOAA-21 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b2549d17-b82f-3746-bdfd-58aab694712d | -21.42103 | -42.97911 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 8a20eebb-0e47-33d2-ba78-3fd5a8eb2012 | -21.41364 | -42.97917 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 18d8115a-62c9-34c1-81aa-1476700e1c38 | -21.41035 | -42.97588 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 04e07e74-6166-3cac-b7cf-6410d985b19e | -21.41006 | -42.97897 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7a3c365c-0e1b-311c-8df3-cadbc17fa1fd | -21.40264 | -42.97924 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9a2fd107-ca1e-314b-bbd4-69e8c4729671 | -21.39993 | -42.96992 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6193850b-31bc-3fbd-894a-41eb758d686e | -21.39966 | -42.97287 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9659e005-9dfd-3a5b-9772-b2268bb80dd0 | -21.39749 | -42.97586 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4189fe89-a4df-3a47-b561-079bc49796e1 | -21.39422 | -42.97226 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 620e6288-29a1-3f52-8923-13a397b43232 | -21.39292 | -42.96664 | 2024-09-27 04:44:00 | NOAA-21 | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 216afdf3-c4c0-3386-8c7d-2a01a786f8a8 | -21.02569 | -42.67074 | 2024-09-27 04:44:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1635771f-2ede-3491-adba-9492d0d09686 | -21.41094 | -42.96965 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 4e16cd28-3f4d-3dbe-a556-0ca195001ac7 | -21.41064 | -42.97284 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| ef52daaf-02c7-307f-9734-b3eacdb9647f | -21.3991 | -42.97875 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 315250cc-ba26-3cc0-a41c-6c6acc11bd84 | -21.39386 | -42.95719 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 444da1dc-a82f-362f-b520-60ba46078a47 | -21.3932 | -42.96384 | 2024-09-27 04:44:00 | NOAA-21 | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f40156f7-2fe5-36f8-b704-6ec78df1280e | -21.00955 | -42.66434 | 2024-09-27 04:44:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 050ff26b-204e-32cb-8e49-34da73f86198 | -21.00906 | -42.66695 | 2024-09-27 04:44:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 69f3551d-7c0c-3d30-ba83-92fba1b837ad | -21.41555 | -42.97894 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 55b10b82-3a5a-3bd0-8320-71778183123d | -21.41522 | -42.98252 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 34f180f0-9d2e-31a7-a764-ccb0f20a6d8b | -21.40844 | -42.97618 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 514d2635-d69b-3ec4-b002-b3ec6a358469 | -21.40813 | -42.97927 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b738c055-24bc-31d1-9f74-eb42bc4e3031 | -21.40485 | -42.97604 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9a2051ee-fa43-34bf-a543-94d00bc811d4 | -21.40456 | -42.97906 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 75581ef7-3f47-3c1c-b741-0a76f6125dcd | -21.40295 | -42.97623 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 1b52d883-b9c2-32d4-94bc-1fd1d5df0981 | -21.39939 | -42.97576 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| a9c92c64-6b03-3bc5-971a-0cbe11784797 | -21.39807 | -42.97006 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e0b6b0bc-a5f1-39bc-9c4f-2284ff872dd0 | -21.39778 | -42.97296 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fc370b44-49c7-3ca4-82eb-c6fa40e7c75f | -21.39475 | -42.96666 | 2024-09-27 04:44:00 | NOAA-21 | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8fb8e60f-21aa-3a59-a78c-9ba280136020 | -21.01968 | -42.67228 | 2024-09-27 04:44:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README107.md)
