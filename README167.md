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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 443f6584-5ada-33ce-9b2f-108560b5d474 | -2.8247 | -57.606 | 2026-10-10 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a4c681c4-2f54-335a-afed-3cfb99c322da | -13.7657 | -48.1224 | 2026-10-10 15:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| dfa66b82-eefa-3bea-8568-40d31f0d6d09 | -10.9388 | -45.3687 | 2026-10-10 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 501.3 |
| dcf81fa2-abdd-3ad2-89fc-f2df2a72367f | -2.4259 | -55.9901 | 2026-10-10 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 674a284d-6547-31a5-8f19-f9b999e6da8a | -10.7777 | -48.3895 | 2026-10-10 15:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 4926fc2c-7cab-3735-af3c-8c76e8134d25 | -1.6395 | -55.1914 | 2026-10-10 15:30:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| bc5fe43e-6de4-3af4-9249-33b28344a728 | -2.7613 | -54.0941 | 2026-10-10 15:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 429555fa-2701-350a-9acb-e028f46c8379 | -1.5123 | -54.5161 | 2026-10-10 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| b946cac6-525c-39b0-8ebe-7c546b0fdfb8 | -2.5689 | -57.4163 | 2026-10-10 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 3b51a097-3741-3e4d-9e34-022701f306a1 | -6.5519 | -61.4177 | 2026-10-10 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| d14225db-ee66-30e6-8f8f-dda921c1b7a1 | -10.8401 | -50.6712 | 2026-10-10 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 549926f6-57cd-3e8e-ad77-501fc322d84e | -3.331 | -59.8292 | 2026-10-10 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 709b3f59-0cfc-3e2f-bc5e-6c5af31c1c7b | -3.037 | -54.0474 | 2026-10-10 15:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2b86aae9-353d-3d6e-b4cd-54ada5aaedf1 | -17.73402 | -40.80509 | 2026-10-10 15:37:00 | NPP-375 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.1 |
| cbfbd96e-1d07-30e8-babf-864061e13d3f | -15.37205 | -41.93048 | 2026-10-10 15:37:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 3296a7a3-ebe3-35db-a874-7324613cbb17 | -17.73506 | -40.81767 | 2026-10-10 15:37:00 | NPP-375 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| 817bf8bb-1a11-3b30-a5d5-a14930dc99b2 | -18.6477 | -41.3345 | 2026-10-10 15:37:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.3 |
| 5354ff54-a284-37a5-9bfb-57bdcb1fb480 | -18.65017 | -41.33327 | 2026-10-10 15:37:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| dd128eb5-9e34-3a2e-a0aa-23dc7eea8d59 | -16.74583 | -41.2534 | 2026-10-10 15:37:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| fed5d17d-9d7f-3cea-86e6-72e92ebbc76a | -15.64823 | -40.42433 | 2026-10-10 15:37:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f0c2a95a-0091-37a0-8074-bdfbe40728ca | -16.82505 | -41.03271 | 2026-10-10 15:37:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 80965b81-5e80-37fb-82a2-9434bdf28851 | -18.64401 | -41.34746 | 2026-10-10 15:37:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.7 |
| a67b2bb4-554e-389c-94d8-3fa3784ca902 | -15.4457 | -40.94055 | 2026-10-10 15:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 60c5d483-b148-3841-b54f-17a4fa8697db | -15.37775 | -41.91309 | 2026-10-10 15:37:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 282.0 |
| f69ecd12-ccbd-390d-bfcb-4362e0ab8344 | -19.64628 | -40.2675 | 2026-10-10 15:37:00 | NPP-375 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 40cfb5d9-8076-3c70-b12e-563393667aee | -17.02846 | -40.37473 | 2026-10-10 15:37:00 | NPP-375 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 7dad2efb-8e84-3729-b536-ecdf47622232 | -18.6416 | -41.34833 | 2026-10-10 15:37:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| a114c39e-f523-3d49-93f9-b4957ee81826 | -16.81829 | -40.6667 | 2026-10-10 15:37:00 | NPP-375 | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 209e84f3-83de-35c7-ae47-d725d984ddc7 | -16.00131 | -40.6492 | 2026-10-10 15:37:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| abba5860-0dc0-3ced-94bf-9fdaa0ecc454 | -15.99646 | -40.6689 | 2026-10-10 15:37:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.5 |
| 1916dac5-5a85-36f1-9eac-2eea85203b3b | -19.80464 | -40.0773 | 2026-10-10 15:37:00 | NPP-375 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| cc4433d8-9e61-3972-97d3-08523493bf2e | -18.64347 | -41.3405 | 2026-10-10 15:37:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.0 |
| 7313c2c8-1555-37ef-a67a-17b5030d2731 | -16.86994 | -41.4108 | 2026-10-10 15:37:00 | NPP-375 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 96a8c05b-686c-39cf-8b86-fe3965a9d054 | -16.69649 | -40.17094 | 2026-10-10 15:37:00 | NPP-375 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fc791f7f-e5c4-3545-ac70-b07752929025 | -15.37133 | -41.92257 | 2026-10-10 15:37:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 1f98bcc9-830d-35e7-9b39-03566073b846 | -18.64829 | -41.3415 | 2026-10-10 15:37:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| dadfd8c4-dbe2-3fe2-a721-2306110f5d84 | -15.39882 | -41.90475 | 2026-10-10 15:37:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 401f3368-553e-313c-82ea-b764d84d90b0 | -15.60514 | -40.50784 | 2026-10-10 15:37:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b5bdc050-00c1-3639-aaa7-6de3ba2e4d91 | -17.14366 | -41.34264 | 2026-10-10 15:37:00 | NPP-375 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 99f323c3-a735-3942-b278-519dd4aed41a | -17.73475 | -40.80879 | 2026-10-10 15:37:00 | NPP-375 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.7 |
| 088b7454-70c4-3d35-9cdd-f8ebfa6a339d | -15.99741 | -40.66159 | 2026-10-10 15:37:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| 3df7b64f-705d-368d-ac48-95bd9e21a814 | -16.8235 | -41.03492 | 2026-10-10 15:37:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 89cefc79-e17a-3da3-8906-b984b0cc3d6d | -16.64701 | -40.5453 | 2026-10-10 15:37:00 | NPP-375 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| fbc45237-0eb0-34f1-b873-9897b6d05d9f | -15.65072 | -40.42625 | 2026-10-10 15:37:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 4616d429-4e6f-336d-930b-891f25c158fb | -15.50259 | -39.02835 | 2026-10-10 15:37:00 | NPP-375 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 0d79ec8f-1d7f-3055-878d-06f7f887aa53 | -15.37064 | -41.91496 | 2026-10-10 15:37:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| b6e79181-cff8-3eb2-becd-95e151b8ebec | -18.63603 | -41.36866 | 2026-10-10 15:37:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| eb814298-7f4a-38d4-8a88-67d65e228030 | -18.64295 | -41.33385 | 2026-10-10 15:37:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.0 |
| fe4eabf4-578d-325f-a5f8-baea2a60fd17 | -16.00231 | -40.65913 | 2026-10-10 15:37:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 9ec187b3-5756-39ff-93b1-e8aa3d7b0df2 | -21.53046 | -41.19139 | 2026-10-10 15:37:00 | NPP-375 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 09db1d9b-fc5f-3e84-a69e-c4ef9224a885 | -15.60106 | -40.53472 | 2026-10-10 15:37:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| e8626168-23ec-3b95-93b2-9aacbf30639b | -17.74146 | -40.81034 | 2026-10-10 15:37:00 | NPP-375 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| 3feff76b-150f-3c0d-bf60-b882f4375993 | -17.14234 | -40.39855 | 2026-10-10 15:37:00 | NPP-375 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| e9534bb5-1585-34a4-adfa-c2e3c572e6e7 | -15.99591 | -40.66344 | 2026-10-10 15:37:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.5 |
| 61c3d687-81f7-380d-82ed-35d995e8cb2f | -15.24553 | -40.31436 | 2026-10-10 15:37:00 | NPP-375 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 7a884c3c-cc74-3843-859b-b1c9a33e6ef7 | -21.5299 | -41.19146 | 2026-10-10 15:37:00 | NPP-375 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 5a3010e9-49f1-3796-bff1-6d1c6106967f | -18.64892 | -41.34888 | 2026-10-10 15:37:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| 79160581-9a76-384a-a3c1-6439e1746339 | -15.9979 | -40.66684 | 2026-10-10 15:37:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| fd8aad6b-bc75-39b6-a149-765241786ae8 | -15.60057 | -40.52978 | 2026-10-10 15:37:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| f5ffc880-5977-374f-b5dd-c4f07d93aa10 | -15.43231 | -41.01571 | 2026-10-10 15:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| a23cf124-dedc-3188-9d8b-34573804e645 | -16.81904 | -40.66795 | 2026-10-10 15:37:00 | NPP-375 | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| a702c87c-7e3e-3fa7-bc68-f3366f8e0948 | -18.65073 | -41.34041 | 2026-10-10 15:37:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 675bf9e6-d2cd-3f81-8525-3d35db9dd799 | -15.99863 | -40.67449 | 2026-10-10 15:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| a2aa7084-5d04-3a7a-a86e-c917976b55f4 | -17.73452 | -40.81112 | 2026-10-10 15:37:00 | NPP-375 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| 2e7fdce1-b3a9-3ceb-b7a4-b4001e58e40d | -18.64102 | -41.34141 | 2026-10-10 15:37:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 71ce4474-654e-307c-8e5f-96a53f35550d | -18.64048 | -41.33493 | 2026-10-10 15:37:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| eff8fb93-c2c4-3065-bfb9-5dc34596ad19 | -15.92386 | -38.96456 | 2026-10-10 15:37:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 247468e6-c037-3093-aec7-a5a4399796b4 | -8.39905 | -38.85432 | 2026-10-10 15:39:00 | NPP-375 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5e81375b-7926-3fbb-9529-108635619fc0 | -12.80022 | -42.46884 | 2026-10-10 15:39:00 | NPP-375 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 68b274cf-8942-3518-9605-de982ccb1c74 | -10.64981 | -39.92561 | 2026-10-10 15:39:00 | NPP-375 | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 28e231ae-39bb-381d-bd7f-ceb0d9d7c141 | -8.77762 | -41.12211 | 2026-10-10 15:39:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 106.5 |
| cef8680a-5ccc-390d-b63f-0df9e0815f43 | -10.64981 | -39.92942 | 2026-10-10 15:39:00 | NPP-375 | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 34b750e0-dbcb-3263-9bf4-290a3fca1cf7 | -8.39937 | -38.85528 | 2026-10-10 15:39:00 | NPP-375 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9c1cd3a0-be09-385c-91e2-ef80d2d69b3c | -9.84588 | -38.92805 | 2026-10-10 15:39:00 | NPP-375 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| a98a95b0-8579-3bf7-b8ea-5916051bda0d | -14.75304 | -40.9697 | 2026-10-10 15:39:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| fff09a3d-86d5-3958-a15c-fcef44053748 | -10.76138 | -37.11267 | 2026-10-10 15:39:00 | NPP-375 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| f5e70274-4649-32b3-8ec3-04db17790a76 | -10.43969 | -39.63165 | 2026-10-10 15:39:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 30f2104f-52a5-326e-ba56-b53bee79766b | -8.78095 | -41.11377 | 2026-10-10 15:39:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 150.8 |
| 93cdb2d2-e356-36b6-a414-c5fc31da54ff | -7.17982 | -35.19599 | 2026-10-10 15:39:00 | NPP-375 | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 46af687e-e5dd-38b8-bd9d-e7ead0df1e8e | -9.55705 | -38.37878 | 2026-10-10 15:39:00 | NPP-375 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 57e23c58-7697-38c7-84f8-2142fdb41689 | -8.78027 | -41.10844 | 2026-10-10 15:39:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 78803901-0ba6-3167-a5fe-41f0885aaa5a | -8.03505 | -39.50533 | 2026-10-10 15:39:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f4e2d452-4679-3d8c-b530-b375b6f9c80e | -10.18725 | -39.30085 | 2026-10-10 15:39:00 | NPP-375 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e2503140-24c0-3e20-b5a7-164ca419d629 | -14.8016 | -41.24768 | 2026-10-10 15:39:00 | NPP-375 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 3eafd8a0-3ecd-3810-86ed-57f9f43ab821 | -13.02181 | -41.81723 | 2026-10-10 15:39:00 | NPP-375 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 202.1 |
| 1b545121-3ddf-345e-abc9-7611d71d4564 | -7.99225 | -40.97408 | 2026-10-10 15:39:00 | NPP-375 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 988fdbd0-f14c-34b1-a55d-dbeee6a118b4 | -10.1202 | -37.40008 | 2026-10-10 15:39:00 | NPP-375 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b220f32b-340b-3bd0-87ff-7092f844501d | -14.93777 | -41.07929 | 2026-10-10 15:39:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 57f2342a-e9a6-3f99-9580-086e29fd1267 | -9.90088 | -40.67082 | 2026-10-10 15:39:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0acf2735-4d2f-3b2d-b2ed-49bd98e6b57b | -11.40823 | -42.03217 | 2026-10-10 15:39:00 | NPP-375 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 81e026ad-828e-3ac1-a972-88c90c24639d | -13.74765 | -40.83438 | 2026-10-10 15:39:00 | NPP-375 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 5068b921-0030-35fc-bf3d-2b0e1ca781f0 | -12.45497 | -42.20088 | 2026-10-10 15:39:00 | NPP-375 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 31.7 |
| 4b33125f-6fa9-3688-9a5b-49d917fea7c8 | -14.14682 | -40.90662 | 2026-10-10 15:39:00 | NPP-375 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| ab02db5d-83d5-3e59-bb64-75554649aa5f | -15.05357 | -41.81273 | 2026-10-10 15:39:00 | NPP-375 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| 5660ec91-7b1d-31d6-9064-0854a008c3c7 | -14.86059 | -40.71835 | 2026-10-10 15:39:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 4026f9ce-4b7a-3a78-ac8d-1a05b92b094e | -13.36803 | -41.99142 | 2026-10-10 15:39:00 | NPP-375 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| dbd3335f-b303-3863-a957-65c4ceec2bda | -14.36644 | -41.3513 | 2026-10-10 15:39:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ec6242ae-f7cb-366f-b418-d64db033f30f | -14.97091 | -41.70325 | 2026-10-10 15:39:00 | NPP-375 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f7d718e0-5dcf-3165-8ceb-519d66a3a93d | -14.46519 | -41.3699 | 2026-10-10 15:39:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 56.4 |
| a8307b0f-d3cf-3def-8943-1a349512b921 | -14.66924 | -40.76167 | 2026-10-10 15:39:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |


[Clique aqui para ver as próximas entradas](README168.md)
