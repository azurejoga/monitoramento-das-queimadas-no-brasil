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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a217c6d-4baf-31de-bb57-fa7a20a6d6b0 | -13.77476 | -47.97947 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c17046ae-4c8b-3882-a8d7-a88c4eff197f | -13.97558 | -45.06408 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 692aedda-d1aa-3950-aa44-289dd7446325 | -17.67897 | -47.26234 | 2025-10-01 05:12:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18841a3c-4f10-398c-9cdf-1910f1c89f3f | -16.37922 | -47.05484 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b91d05d1-2a15-37c3-a60e-b77161a090db | -13.80636 | -47.49703 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 000d326d-3c21-3a33-9a88-8c0c1fec4d44 | -14.89189 | -48.13542 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41bbf517-b366-37b4-99b8-8f05b20cf240 | -15.47948 | -48.55128 | 2025-10-01 05:12:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8c8db87-a655-3ee5-aa10-1079bed6f522 | -13.68101 | -51.22822 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34d6fd3b-2e4d-320a-8aa8-488956cbf5e1 | -14.96301 | -46.88852 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b6d3cf01-f99b-36e0-9503-0418789b4b52 | -15.84145 | -59.59735 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dba2f65e-da4b-319f-aa25-e1a79deb0f29 | -13.66862 | -48.06468 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 41a0f736-1a43-3211-8d26-c93918da256c | -13.7047 | -48.63194 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aea62bf1-6221-3eaa-bc26-2ce2c3419981 | -15.80422 | -59.5103 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e34e8cf-92f4-3bcc-824a-ab2d572d4369 | -14.71684 | -48.15845 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 393b6598-806d-344d-8474-4a127c4fd851 | -15.23876 | -56.8056 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a5357d5c-24c2-30e6-b11e-36b492ab32ed | -14.76187 | -45.75811 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19e4a554-bfca-339d-931b-29a6bb13a1a2 | -13.81766 | -47.5079 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b8c9d83-acf3-348b-9452-69c3cfa6c1fd | -16.25896 | -50.93504 | 2025-10-01 05:12:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 08ea4254-c410-3ca8-ab31-bed337f7ed20 | -15.26542 | -51.47982 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2658612-3252-3962-bb91-8460f5b9e980 | -13.75844 | -47.93889 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29c96f83-2aeb-3e88-b83d-8d592c429ff0 | -15.37894 | -49.1992 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d715cd9-8d9b-31f4-aff4-68c6dc481b35 | -14.69386 | -48.12119 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 331bdace-6fb9-337c-b85f-75d8f13d2e45 | -15.29987 | -46.1947 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 057ede7a-5231-38b4-99e5-9e8ed1647a03 | -14.62907 | -46.98399 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddea41b7-cfd3-3d69-a930-5c52504f0c98 | -16.24846 | -50.93675 | 2025-10-01 05:12:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cff5dfe7-53e4-3353-bdee-e2f52a7cb407 | -13.6642 | -48.05059 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bb73bed-e744-3c86-a6eb-796490d93892 | -15.31388 | -46.40069 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 415a1a31-ceaa-36b7-88dc-6b1aee7294a0 | -15.16797 | -49.08575 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f677ddfd-2fd4-386d-a787-1dfc68f69e94 | -15.55363 | -48.18753 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5d730347-e9b3-3865-b4ca-770bb97c40ad | -13.75951 | -48.40788 | 2025-10-01 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 697d58a2-e4b5-3170-8c6a-589e94833ed2 | -15.23528 | -56.805 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 191b2eb4-2f97-36f4-8d2d-0028ae58e82c | -14.75484 | -45.75745 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d19bb7aa-76de-3c27-af5a-1b99252f9b56 | -15.93848 | -48.12535 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3f623fd7-5d5a-372f-86fe-8d2175d43ee9 | -16.19638 | -49.99122 | 2025-10-01 05:12:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 91e97025-1c54-3412-931b-9ba41c5a9e2a | -13.29625 | -50.66035 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4393dcb7-74c2-3ce5-a183-48582bf5de21 | -15.85195 | -59.59545 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62bd4ad7-30fb-3005-81d0-3486b45259a3 | -14.68545 | -48.24759 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fca1b35-afab-3c29-b840-22ac35e16a68 | -14.89278 | -48.12745 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8c01e62-497d-3e5b-8642-376476813816 | -14.19035 | -46.12387 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5189469b-2b87-3c07-a454-36db57bce070 | -12.92938 | -54.72589 | 2025-10-01 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9fd208c-20b3-3306-bab1-74942bad5f76 | -15.87503 | -54.23498 | 2025-10-01 05:12:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f3887a7-b255-3f72-a7ee-f82173ea3d86 | -13.94158 | -48.10785 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c30db813-0c85-3cff-95f7-dc0572fa3b9b | -14.9271 | -47.82414 | 2025-10-01 05:12:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db7cf8b7-fc19-315e-9044-e71960b60ca3 | -14.98089 | -50.783 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f69690d-e2f6-3690-9a44-177a081e48df | -14.70856 | -48.12331 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99ea0c2a-bef9-30f7-b017-0498edf4922c | -14.7881 | -45.77436 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d9a08f2-8354-3dc4-a9eb-1fe833f73a84 | -15.30717 | -46.4002 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c85f181-7513-31a7-b653-42f5fbe74af2 | -13.93901 | -48.11354 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d50a8214-a782-308e-bd32-a1f18867dc0f | -15.26973 | -56.78942 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99e6ca54-9e47-3eb2-930e-44c8dd9b59d8 | -13.76697 | -47.97141 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0b63e4c-82d2-3886-a8ba-0e0854bbbaf8 | -14.90971 | -51.67523 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e8f75a2-3a43-37ee-88fe-3f1d8eb92093 | -14.95601 | -46.88476 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77f3bd59-9ab6-303c-9e62-9f2ff860e001 | -13.29976 | -50.67245 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 83374e05-e58c-32f9-9b32-e510ae6047c8 | -14.68207 | -48.11852 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 939db3b5-b916-3932-8214-36ffff379864 | -14.18741 | -46.12078 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bfd10bb8-8073-30e4-870c-5f8930ffeaf8 | -14.06084 | -45.04051 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3a79926a-5fef-3a13-8c66-4cb81e7704d0 | -14.98774 | -50.76863 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 702be58b-ce60-3ef8-93bd-2be9f3e52fc2 | -17.67195 | -47.26709 | 2025-10-01 05:12:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 037001cf-9e01-31ec-91ab-2ae461149f64 | -13.98411 | -45.0514 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f4a85f4-8738-3fb8-a89d-e3dd23e18f1c | -13.71753 | -54.71819 | 2025-10-01 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffae2546-a046-3de8-a93a-d6e3144a2fed | -13.76537 | -51.21772 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a1da5fc5-74ec-3575-be68-25a2545babab | -17.93209 | -57.57097 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| e097c6db-ee57-3076-9166-40e266a3ddb0 | -15.55124 | -48.18953 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b3391469-020e-357f-b5d9-f1024c2f244c | -14.98894 | -46.95296 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1aaa9526-0155-39dd-8056-e03df690e1fa | -14.35822 | -47.14451 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e070e250-0fc7-36aa-a7be-5a2ca7cf9695 | -15.12547 | -46.45418 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6fd155b-93a1-3b37-b179-ce5c3baed328 | -15.25105 | -56.84362 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 861dff3c-5750-3704-b8c3-c6ee2564b95e | -13.97631 | -45.05711 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 316b7525-1e70-348d-b93a-a490d5f67521 | -14.58941 | -48.30306 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 186a7f2c-fdef-3711-8c31-d75784d0ef64 | -16.37861 | -47.05874 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db310634-70bd-3a98-ba7b-c1edc6ebaa9d | -14.36179 | -47.14378 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d88317dd-187a-3648-97b9-2a70a29e360b | -16.37976 | -47.04904 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a887046-b1da-371d-acb8-15ba18c88c42 | -15.24492 | -49.72937 | 2025-10-01 05:12:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8cd8319-784d-393e-a7c2-487e400e4fc7 | -15.25685 | -56.77969 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5d27c26-712c-31d5-9df7-06cb381213b5 | -15.84088 | -59.60092 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b75685f5-b99c-3411-8e96-29c14c11f6f7 | -13.97965 | -45.0604 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8506d762-388e-3b86-998b-4417de3c1649 | -15.28377 | -56.79131 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e902e296-e662-3d33-ada7-a6357a35e322 | -15.487 | -45.91317 | 2025-10-01 05:12:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 38d7dcec-868b-3b65-bec3-27a88d665ed6 | -13.94075 | -48.11506 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25766832-b6f4-3e79-b2ac-15ee2ff6bbf2 | -15.94603 | -48.12321 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e729201-f4b2-3e42-ab7c-f5f3668ed724 | -13.69557 | -48.64225 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e431bb8-bef8-3caa-a2e4-089de5c825f1 | -16.91643 | -49.79238 | 2025-10-01 05:12:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 50774c93-72ad-3455-8f3e-ba65980a2a08 | -13.76413 | -47.96711 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efcdb563-4df5-32da-96ba-66c441e5b0fa | -15.27324 | -56.78987 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d9de4a4-412f-3a70-b8e8-d06396ec66c9 | -15.1866 | -53.86499 | 2025-10-01 05:12:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2847b537-9f54-3328-a431-9da72eee80fb | -13.72946 | -48.81572 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 385a7f95-14fc-343b-9a8f-b2adb622f950 | -13.80654 | -47.4957 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25e1f254-61d5-3d9c-b332-6c48cb530275 | -17.39988 | -47.15909 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3deeb465-44aa-35b1-8168-4504c6a836f1 | -15.33618 | -47.94498 | 2025-10-01 05:12:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e763546-f423-3ecc-8e10-f945ec7a629c | -14.09293 | -49.74764 | 2025-10-01 05:12:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6fb97ef7-677c-341f-a683-b8a3f14508c4 | -14.14252 | -49.2005 | 2025-10-01 05:12:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c8c6eee-1545-30b1-917f-61be27c74132 | -15.48638 | -45.91959 | 2025-10-01 05:12:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ccccaa7-6c19-3a4f-8acd-2497d1137871 | -14.17704 | -46.12148 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbbecc00-1985-3922-8e19-59f170b635e7 | -17.89907 | -57.5782 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 908faa66-ad91-3700-ad42-ef35dddef225 | -14.0503 | -47.98043 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 293b8436-207f-3114-83cd-22f5f2939c46 | -16.19325 | -49.99826 | 2025-10-01 05:12:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d918cb35-2229-399c-9688-a806e37c1948 | -15.23423 | -48.75398 | 2025-10-01 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a5d30aba-0ff7-3b72-8044-550bc3a6a3ba | -14.10131 | -49.75227 | 2025-10-01 05:12:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91a64cc3-feae-3322-8131-6fac7f26a6eb | -13.70341 | -48.64324 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73fe9947-b862-3836-8c9c-b87cff54e75a | -16.19366 | -49.99479 | 2025-10-01 05:12:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README134.md)
