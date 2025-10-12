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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 544a8a8c-beba-32fb-8f6b-c6b3f30ea2ea | -11.67591 | -43.7749 | 2025-10-12 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 8b457e77-3323-31c4-92b4-02b738ed650a | -13.54161 | -43.73591 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3a528a4b-bbaa-38f4-9609-b2c5cd813083 | -13.67882 | -43.86815 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f1b91dd7-727e-3cec-b7c1-3dc946bb1d19 | -14.29061 | -43.49426 | 2025-10-12 00:11:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 098d9dbb-5c72-3d24-b020-e0a77d8797d8 | -12.995 | -45.23566 | 2025-10-12 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3c4b46cc-82d6-3ccd-abd8-2668e6aef6bb | -14.83898 | -42.39056 | 2025-10-12 00:11:00 | TERRA_M-M | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 18034dd8-25e9-39eb-8aff-4d9040330979 | -14.58997 | -42.77992 | 2025-10-12 00:11:00 | TERRA_M-M | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 47591a26-a7b6-3557-a357-bd6b811a373f | -13.41738 | -47.23629 | 2025-10-12 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d84d96c9-26c9-32ce-8057-60b0fb1fa415 | -12.50949 | -47.436 | 2025-10-12 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 6f9e4baa-10d1-3fc6-8822-d082f8cdcaca | -13.0231 | -47.87825 | 2025-10-12 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| da0cd93a-b41d-37dd-a875-a75fe2cbedd9 | -13.67782 | -43.05707 | 2025-10-12 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| aa7ce211-7206-3d97-acf4-5600c3290cb4 | -18.56585 | -50.5924 | 2025-10-12 00:11:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| c85a17ca-f93f-3338-a4a0-7bd7c9f51827 | -13.54285 | -43.74503 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e18fab83-f098-320d-b386-99c87860101c | -13.04291 | -47.94698 | 2025-10-12 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 78bd9a6c-68c5-37f7-b705-4b3f59468348 | -17.55271 | -44.16103 | 2025-10-12 00:11:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a8f1c74-6509-37e2-9248-b7db92165aff | -13.8455 | -42.8725 | 2025-10-12 00:11:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 641a36ee-3d70-365f-96c3-6e9e0b6ed693 | -17.55525 | -44.18096 | 2025-10-12 00:11:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3c22a2ef-29c9-34d1-bb0f-69c6229c99cf | -14.02111 | -43.47741 | 2025-10-12 00:11:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| be0da4ca-9cc6-30f4-9351-cc4b2e804b49 | -14.31626 | -47.31248 | 2025-10-12 00:11:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f89cdc00-ff50-36fa-b6a0-f7da7531ae44 | -13.41114 | -47.2289 | 2025-10-12 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fdd4b3b6-e517-3ccc-b280-2a19bc1172a0 | -14.51318 | -42.16913 | 2025-10-12 00:11:00 | TERRA_M-M | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f4af81c6-9d70-3a4a-9dde-db50a73d1fdc | -12.01993 | -45.22603 | 2025-10-12 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c41ce54-b30a-3884-955d-90ab85c542cd | -17.01895 | -42.96721 | 2025-10-12 00:11:00 | TERRA_M-M | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 06f00267-6b8c-3532-8997-87121fa620f3 | -14.96673 | -45.11571 | 2025-10-12 00:11:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 42c5722e-621d-35ef-be8b-2989d55890dd | -12.5078 | -47.42261 | 2025-10-12 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 16fb166a-e53c-3ce1-b4a4-9fe08e12c1c2 | -16.73899 | -43.97744 | 2025-10-12 00:11:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| efdec865-f97f-3630-bc2e-0fe749689a9d | -12.58657 | -41.27871 | 2025-10-12 00:11:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 5d002c95-0652-3e32-bb0a-e1e361717553 | -11.95068 | -44.84436 | 2025-10-12 00:11:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| c1566040-aa97-3f9e-a816-424ef4648e4f | -13.40575 | -43.75857 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 0f167141-8bb7-315d-8c8e-1f413aae8ed0 | -15.47128 | -40.82193 | 2025-10-12 00:11:00 | TERRA_M-M | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 83ee5887-233a-3f00-a7f1-8b161262ca00 | -14.52205 | -42.16777 | 2025-10-12 00:11:00 | TERRA_M-M | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b0fd6968-e41b-3d88-bf71-0f2748ced556 | -13.29955 | -43.31218 | 2025-10-12 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d19ed599-5e69-397a-b6bc-f2ba6e1085f8 | -15.18872 | -44.50246 | 2025-10-12 00:11:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2fe11b3e-32b9-3beb-93ca-3154dba7e58b | -16.3504 | -42.39817 | 2025-10-12 00:11:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d146fadc-5429-32b0-82a4-8dfab98de0e3 | -18.5506 | -46.95224 | 2025-10-12 00:11:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d2413f6a-1182-3300-be25-afa091d0d627 | -17.55397 | -44.17094 | 2025-10-12 00:11:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| da2cc6e8-3b0e-3258-bf01-7e8867632de9 | -14.9681 | -45.12623 | 2025-10-12 00:11:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b58871f7-9264-393d-ba8a-d610b056642f | -18.56183 | -46.95076 | 2025-10-12 00:11:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b426e0f4-06d0-3888-9d9c-86b71a51e586 | -13.4045 | -43.74945 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 88c796a8-ca69-3811-a085-f8d099a47318 | -10.87576 | -44.18312 | 2025-10-12 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0ff76f06-2f99-36e6-aabe-43000ce4254b | -16.34031 | -42.39038 | 2025-10-12 00:11:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8d8f8ad4-094d-375e-b80e-a6d81f47739c | -15.1977 | -43.39362 | 2025-10-12 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f86f411e-fad7-3198-90ea-3703a9ea40d5 | -13.70431 | -43.64434 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4265e93d-7b13-3446-904b-950982fbce73 | -13.65979 | -43.86153 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| d7f69984-fa82-3edd-8510-ab6737ea3746 | -15.74701 | -43.84826 | 2025-10-12 00:11:00 | TERRA_M-M | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 1596a250-3cf3-3f9f-b13e-8640b9872104 | -14.03121 | -43.48522 | 2025-10-12 00:11:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b63f85be-2592-3da3-9c17-e468e939124f | -12.23712 | -45.33477 | 2025-10-12 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 8317b5c3-bbc5-384a-b5ad-209edc093774 | -13.04328 | -47.94059 | 2025-10-12 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| b9562a93-1aa3-38a8-b91a-b671fe94edc6 | -11.87896 | -45.47975 | 2025-10-12 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 6042e91d-e5b3-36b3-a293-bf38a2f2be2d | -13.38707 | -41.33361 | 2025-10-12 00:11:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 7b22efc3-deeb-39fc-8f70-3f5c74e04d24 | -10.18115 | -39.83604 | 2025-10-12 00:11:00 | TERRA_M-M | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 4f572fdb-fbac-3d0e-b316-db5a053d2344 | -15.64517 | -44.47934 | 2025-10-12 00:11:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5ef0655f-0ab2-3d0c-acb3-d3783bd2a7dd | -15.66358 | -44.47666 | 2025-10-12 00:11:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b2629116-9931-384b-bfe8-a99484d63bac | -13.41477 | -43.69225 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 79de2186-b548-3996-af6c-ee0a8b0d6a8d | -13.69014 | -44.29313 | 2025-10-12 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4bf76c7c-fd3c-3426-a55b-7e61f77e8264 | -17.5831 | -42.44296 | 2025-10-12 00:11:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 81064f3e-5fa3-3afd-a24f-541b4077dc61 | -11.07213 | -47.12267 | 2025-10-12 00:11:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0fe6ad94-6453-37f5-ad31-5e05c22e7202 | -18.21886 | -42.37848 | 2025-10-12 00:11:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| edc9dcb6-9cd1-3e43-b9f5-23b1c459a5b9 | -15.76752 | -43.86469 | 2025-10-12 00:11:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 2c3099e2-dacb-3300-b233-df63b9fef2bc | -15.43083 | -44.17199 | 2025-10-12 00:11:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 986daa50-eaf1-3024-b7e8-5aeaac7c3acf | -12.49887 | -47.43739 | 2025-10-12 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 243de647-5807-34d6-94bb-f160965dc6fe | -11.95627 | -41.31911 | 2025-10-12 00:11:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 337651cc-90b7-3f88-a1e3-a9e1bd0c6994 | -14.58871 | -42.77086 | 2025-10-12 00:11:00 | TERRA_M-M | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| d537d30a-77c5-3224-95be-c7152890e7ee | -13.65855 | -43.85236 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b3bf7111-225d-3934-bcee-54cf5d8bc463 | -10.18647 | -39.82909 | 2025-10-12 00:11:00 | TERRA_M-M | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 18cddca1-6a4b-33f4-a674-ed0f6afaba2f | -15.64212 | -40.98348 | 2025-10-12 00:11:00 | TERRA_M-M | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 6e13e269-63f5-348d-bbee-8635117fc40c | -15.11648 | -42.01189 | 2025-10-12 00:11:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| e7f822b6-b3d9-3607-a123-e16a5e2a46ea | -12.23843 | -45.3447 | 2025-10-12 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 297ad586-f300-305c-a352-a938d56c5ed2 | -10.877 | -44.19211 | 2025-10-12 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fbd0099a-df4d-393f-81ad-869e7be7dfad | -13.66992 | -43.86942 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 219.9 |
| baad58da-ddb0-30e2-8bb3-bda641097c82 | -17.58184 | -42.43373 | 2025-10-12 00:11:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 94.4 |
| b1a77359-09ec-351b-9bf2-ae891d4a8182 | -10.1792 | -39.82292 | 2025-10-12 00:11:00 | TERRA_M-M | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 85ef4c4e-1cbc-3c9f-b57b-b7cea722499b | -11.67715 | -43.78387 | 2025-10-12 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 805e61e2-6403-362c-a7ff-fc3af1f913c3 | -12.01073 | -45.22731 | 2025-10-12 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0e776ece-8922-3fbe-b7b1-6e10261daf9d | -17.0202 | -42.97646 | 2025-10-12 00:11:00 | TERRA_M-M | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5d09c8eb-ff36-33c5-b408-3c7b9c10f567 | -14.60618 | -42.1115 | 2025-10-12 00:11:00 | TERRA_M-M | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 66070c06-f906-34d8-870b-546b133be39b | -12.64128 | -44.23117 | 2025-10-12 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 179a891c-1f73-3809-8538-b325b127d366 | -11.91561 | -44.17897 | 2025-10-12 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| e2d07022-f2c5-3b10-9a1d-b907b7e757dc | -15.67677 | -46.62769 | 2025-10-12 00:11:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d7b1495c-ecdc-3aba-91ae-03558c8ce717 | -15.46357 | -40.83332 | 2025-10-12 00:11:00 | TERRA_M-M | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 170d67d1-12ba-3586-99ae-d6deddf573e9 | -12.73985 | -48.64825 | 2025-10-12 00:11:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 97f7a020-3114-3b7f-9807-0a96bc5febce | -13.66744 | -43.85108 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 179179e6-1d1c-3c98-a57a-a269c37d41e0 | -13.41461 | -43.75728 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 36616c50-ebf0-326a-b0b1-639c5fd278b1 | -13.67758 | -43.859 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| cea648d0-a92f-3ac6-9554-19fc682380fb | -13.42178 | -47.22772 | 2025-10-12 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d251dc96-11b1-3d0d-9409-9c24ed1a7e9e | -14.28937 | -43.48513 | 2025-10-12 00:11:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 39af8531-30af-3924-a335-d0ff966d4b42 | -15.64354 | -40.99314 | 2025-10-12 00:11:00 | TERRA_M-M | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| cb64c185-6d8e-3c46-a2fb-e09fd6872a49 | -16.34913 | -42.38904 | 2025-10-12 00:11:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7400fcb7-8996-3a45-8282-aca67501e1b4 | -4.68223 | -43.25812 | 2025-10-12 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b1f55e2c-b80d-3a91-ba41-b5f117bc54a3 | -5.25808 | -46.14977 | 2025-10-12 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c69352c1-8004-3d3e-83ba-3e561593789e | -5.94006 | -43.94448 | 2025-10-12 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 71bbe249-7927-35ca-96ab-30383310b15f | -8.53152 | -45.43093 | 2025-10-12 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| eaddede1-512e-3b35-b620-2097be95d2e6 | -8.48286 | -46.23042 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 79db77c6-1c86-3817-83ae-c3024edc5036 | -8.19361 | -43.3204 | 2025-10-12 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| d4d279ed-d532-37d7-99f3-7a3cf8c6ca2b | -5.16537 | -44.59773 | 2025-10-12 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 357cdbf9-c2f5-362b-9d36-574ccc2bcddd | -7.0441 | -45.26268 | 2025-10-12 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59a3d2cd-429d-3de6-af80-c071a38bf68d | -7.5673 | -46.19746 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 19fcd312-bb8c-3b0b-b5c5-50ef52a01310 | -9.30717 | -40.22832 | 2025-10-12 00:13:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 6ecf2e16-d34b-3467-8086-6ca53f9b734f | -5.81274 | -44.02944 | 2025-10-12 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b8d83f8b-9ba2-3529-9088-abdadad583b0 | -8.21711 | -43.34767 | 2025-10-12 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |


[Clique aqui para ver as próximas entradas](README3.md)
