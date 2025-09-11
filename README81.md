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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d025477-af5f-3e78-a464-e202c905a56a | -20.39723 | -46.28238 | 2025-09-11 04:25:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0d76f28-3edb-3474-be0c-7b9d5a8bfa28 | -19.71066 | -44.234 | 2025-09-11 04:25:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c282e6c7-0b39-30a5-b1eb-fe4c5f1e330c | -21.13205 | -45.42172 | 2025-09-11 04:25:00 | NPP-375D | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32983c23-fd1f-3eb1-9886-78a4fdbef2a1 | -18.01887 | -47.13491 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4ac9ff9-cc06-3746-9ff6-361bcb757937 | -18.44887 | -49.57374 | 2025-09-11 04:25:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1d1ff094-4086-3f26-b5b1-ca8e1db1d6d1 | -18.90645 | -47.89987 | 2025-09-11 04:25:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 571eccc8-2903-3e1d-a8b0-964cec8df7c8 | -17.37697 | -52.92391 | 2025-09-11 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a92e7b63-b465-36be-bd21-c72e814d0ec4 | -16.57056 | -49.73392 | 2025-09-11 04:25:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0eb41f8d-8837-3288-b2fa-d4d3882b670f | -20.00768 | -47.62613 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0114f2ca-8d36-33d3-80da-6f0d1afbb27a | -14.27726 | -54.74878 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b853840-8f22-39a6-a913-aba76b5140e5 | -18.97077 | -48.25795 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2dd6433d-6644-37a9-8756-c343fd30ff8a | -20.36215 | -46.65807 | 2025-09-11 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 756f36f9-34a6-39b7-a062-0b91a8e5df65 | -20.09422 | -47.35694 | 2025-09-11 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 242813db-02e0-3521-bcf6-e9bdb8aeb5a3 | -20.18581 | -44.45014 | 2025-09-11 04:25:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9172d51e-9a00-323f-a6c1-3bc295389c8e | -20.00435 | -47.62555 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88045dda-9b94-39db-85c9-6d5d4c86ac87 | -20.02188 | -44.56256 | 2025-09-11 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 115ed438-c43b-3560-9721-530f812e089d | -16.49033 | -51.97816 | 2025-09-11 04:25:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 804ea2c2-79af-35e1-8220-e614bd20771e | -15.79409 | -52.25747 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b15e866-ebf4-3ed5-ae77-ad3441f3cf78 | -20.01159 | -44.2375 | 2025-09-11 04:25:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 383e6467-21ed-3dd0-afb7-f1cc1ee9cf59 | -17.55815 | -44.54683 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f2dcc1b-0c8d-3500-87fe-d687f18dfcad | -18.12715 | -48.13777 | 2025-09-11 04:25:00 | NPP-375D | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ae4839a-e7e1-3a68-8a58-95dbc61d8f8d | -15.13425 | -52.43107 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f341a53-bb8a-3836-97a0-22b45333cde8 | -18.45097 | -49.58229 | 2025-09-11 04:25:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5a3e2462-3ea1-31aa-96d1-31200dab7a18 | -15.12999 | -52.43064 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cd558e8-9d01-338c-b564-d84e566342a2 | -17.93157 | -44.47844 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a50e6687-cae3-3e65-80bd-9acdf85d0d53 | -18.34293 | -49.33714 | 2025-09-11 04:25:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 180050be-8112-3865-9a2d-618b3efddae4 | -16.29892 | -50.0638 | 2025-09-11 04:25:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dabedb05-bfb2-3a7b-be7f-ede0ce24b1fe | -17.247 | -46.75635 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac8a453f-dea8-3261-90da-363ac812176e | -22.81897 | -47.04218 | 2025-09-11 04:25:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b0d56e24-5524-3543-971e-48c3cfec6d56 | -14.30798 | -54.74931 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b192c81-464d-3217-8004-a4acc107c59e | -15.56438 | -54.75959 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e3310989-0e2c-3cec-a6e7-94681cf97f14 | -19.03363 | -42.15165 | 2025-09-11 04:25:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 75d4c478-d903-385e-becf-d78e2a07d2fd | -19.98321 | -47.6294 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 617b4a3d-257d-3342-ab76-490780a485fb | -14.42459 | -52.94082 | 2025-09-11 04:25:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb8032d1-5c1c-3ce0-b12d-9da48ff7c248 | -20.07498 | -47.5243 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bec805e-150e-3b99-a5db-49ca482eeeb8 | -15.75929 | -48.04703 | 2025-09-11 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 75dde273-94a9-30e2-afb9-71c5720c5141 | -17.31768 | -46.75665 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e37b2844-8659-390d-be80-7500823ed10d | -21.64747 | -45.53603 | 2025-09-11 04:25:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fdb43609-45a5-3bda-bd3b-9f7544ccac67 | -22.90474 | -47.07596 | 2025-09-11 04:25:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6d1df828-7f47-3f1a-9e20-4dba61042979 | -18.54464 | -46.68964 | 2025-09-11 04:25:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22926751-55d8-3c40-9bf1-c833b014c7e5 | -19.95215 | -49.26847 | 2025-09-11 04:25:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0fc4b1f3-9708-3ef0-8a86-0e3d76d677f7 | -20.06754 | -44.65895 | 2025-09-11 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f116245-5eeb-35a9-b9bd-595c48363f29 | -19.2346 | -48.00571 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 927ce725-c650-3695-bb69-dadd7260045d | -19.95954 | -46.88089 | 2025-09-11 04:25:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c3a06cf-2879-3729-a41d-2daba2317660 | -20.70607 | -46.05484 | 2025-09-11 04:25:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3f7643c-d21e-35ee-9de3-289c47fb11ca | -15.80026 | -52.24669 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e6413a3-9ab6-3d89-b399-90b54ae23901 | -19.6637 | -45.85677 | 2025-09-11 04:25:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e548534f-4ff9-3307-809f-0c5dfa23ad95 | -14.7281 | -55.61554 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cf5e1cd-d704-3e9b-a285-ab220971e085 | -20.00789 | -44.237 | 2025-09-11 04:25:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 197b8587-5f13-3b81-bc41-b6544f006663 | -15.1331 | -52.41398 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fbe813c-8070-39fb-bc7e-5ca88da6c931 | -19.80646 | -47.16424 | 2025-09-11 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b38542d-54b4-34ab-9310-0487a87c7b16 | -17.84042 | -46.73843 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8c048bb-cdd0-36d4-9c75-871375df551d | -19.99263 | -47.63483 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f1795314-31ba-3f25-9140-683ae25d2f17 | -18.01612 | -47.13069 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1f90c3f-19bb-370d-bb81-61e6ee2e2a64 | -19.99436 | -47.62379 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aed68c11-9ab0-302d-8bf7-7c5724e48897 | -15.98522 | -42.97966 | 2025-09-11 04:25:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 437f383c-7c85-306f-962e-81588bd00aa6 | -18.32796 | -45.13589 | 2025-09-11 04:25:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b869acfa-7619-3d29-b9c4-2aeca892e87a | -18.60624 | -43.96429 | 2025-09-11 04:25:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4ba5ba7-3e8e-3a2a-9b19-7132ae418f74 | -15.52397 | -48.56631 | 2025-09-11 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a6568de-8ab9-3a92-855f-a02190651c4e | -16.62951 | -49.7682 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddd3932f-8c33-3e73-a4ef-0fbc891f519c | -14.88626 | -55.84859 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61e69f00-4c71-3443-95b1-77e91fc498de | -17.82706 | -46.7362 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35be5e4f-09b0-3cd7-8b8c-47eb4a71127c | -15.13475 | -52.45168 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1a57725-1e8e-30e3-8bb5-e2d3a90b9fab | -21.50118 | -45.50084 | 2025-09-11 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 84f1ed4b-9dc9-35ee-851f-dda90f3937f1 | -19.66428 | -45.85284 | 2025-09-11 04:25:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| efd4d33e-7d94-3a06-9d0d-769939053d4d | -21.43617 | -48.91261 | 2025-09-11 04:25:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60975826-7483-3ac2-a9ba-2bb41cc5fdf4 | -14.88801 | -55.84739 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2ef0489-8944-3761-adc3-74af3026646b | -14.51458 | -53.93307 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efcfec17-4d4b-388a-95e7-b0e901640e98 | -16.3012 | -50.05084 | 2025-09-11 04:25:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bb157d46-b92f-3709-b8f6-36f808fdca11 | -18.71292 | -47.1766 | 2025-09-11 04:25:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4277755b-dc75-3345-88f3-238bb108892b | -15.13563 | -48.60563 | 2025-09-11 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46a1dfae-349e-364a-b138-ccd9d167e87a | -17.84874 | -46.7511 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3963f5d0-e594-3ff2-ac27-9efd616fa62b | -15.62859 | -47.53733 | 2025-09-11 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f71ca4cd-0dd1-3652-a0f4-49bc104f9fd3 | -20.00493 | -47.62186 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41e10027-da62-32dc-9654-ab8ca5c379ee | -15.59108 | -49.39294 | 2025-09-11 04:25:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c893c27e-fb1d-364f-8df6-8dffde66df04 | -15.13555 | -52.44737 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9fc78791-a66b-38bf-a521-01ab9a963747 | -17.79727 | -44.40774 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5dfc286a-6702-358c-a87c-870431a7d536 | -15.10372 | -50.07128 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93c61b2d-af99-39c1-9c3d-cc3f62a682de | -19.9877 | -47.6226 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6915b71c-be99-3428-b8a4-48b349bd4233 | -17.27094 | -46.08159 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f16be490-b68b-3883-b2ea-d671877df12b | -18.29288 | -47.67403 | 2025-09-11 04:25:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f0125c32-9bae-31eb-a000-7400a65ac977 | -15.15965 | -52.43435 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a429959-b851-3e06-90da-29907be36d65 | -22.56315 | -46.04152 | 2025-09-11 04:25:00 | NPP-375D | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b3d614e9-f2d1-35be-9810-7af2bb2a3cdc | -21.12942 | -47.73087 | 2025-09-11 04:25:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21ced626-6ef8-3258-858f-9a331a4f9722 | -18.76504 | -48.54145 | 2025-09-11 04:25:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d13c3c14-a617-3f5b-a283-72e4c50b5ab7 | -17.2642 | -46.08052 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74311d2a-7a8e-38ac-8bac-190c783dd313 | -15.81035 | -52.22786 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67a77608-c813-3a6f-b09e-2a6e90f59b7d | -22.56571 | -46.04358 | 2025-09-11 04:25:00 | NPP-375D | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ee76885e-4680-3342-895f-33da09f97548 | -19.99378 | -47.62748 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e8b46b3-5278-357d-b0cb-eed498e6fb35 | -19.98988 | -47.63057 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 730d9a76-6155-3cb4-901b-b0102c984c9e | -21.40582 | -44.15127 | 2025-09-11 04:25:00 | NPP-375D | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6eeeb9ba-9967-3d48-85ef-3e53073e31a9 | -15.55195 | -54.74624 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a931514-2ce5-31e0-a40f-c6b81904c017 | -17.70783 | -44.4341 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8f58cce-1f7c-374b-8ff1-634852bcc9ab | -20.12257 | -47.69093 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec2d61ab-c5e6-357b-9c1b-9bab48ba0e52 | -16.61251 | -49.78226 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46655dee-0e8a-369a-b551-8924d82d099c | -20.15775 | -41.03343 | 2025-09-11 04:25:00 | NPP-375D | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a81086c1-bc61-3404-a70b-06769a87259f | -15.10312 | -50.11756 | 2025-09-11 04:25:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aea0dfd8-d08e-358e-ab5d-1d7a50c3397e | -21.81133 | -47.23456 | 2025-09-11 04:25:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0d3e55ff-bc91-3425-a92c-88d1ee60adfc | -21.06371 | -46.15037 | 2025-09-11 04:25:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d959bd3f-29c6-39f4-8740-c9f675da0127 | -19.37085 | -43.65099 | 2025-09-11 04:25:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README82.md)
