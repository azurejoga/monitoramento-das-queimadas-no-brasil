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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e545d59d-2f14-3efe-9330-045526d4f542 | -15.52868 | -42.66222 | 2026-09-22 04:04:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 859c8e8d-7dcb-3495-acc9-d68c4164a4bf | -18.73378 | -46.94658 | 2026-09-22 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b2909a3e-fbc4-38ad-8971-b8df5bb14f74 | -15.62066 | -48.32182 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75c481fe-2a94-3c02-97b7-d67bfc24395d | -14.17679 | -47.88025 | 2026-09-22 04:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 26a3e17a-f33f-3ed9-9a92-4698b26bcd7f | -12.93168 | -51.04441 | 2026-09-22 04:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60fbd0fb-c649-3a53-aa1f-15f2119669d8 | -16.67458 | -41.8482 | 2026-09-22 04:04:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c1490e0e-d7f2-32c3-887f-7f0cae602fae | -14.68972 | -45.67812 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f371b092-d276-3fbe-aa65-2018bca4f196 | -13.92938 | -48.56893 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cb957f95-9fb2-36b1-b93c-6ef3bcbabacc | -13.92414 | -48.57456 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8100ed03-45bd-3204-aac3-416dc0c39b93 | -16.67398 | -41.85187 | 2026-09-22 04:04:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bea6cc0a-66bc-3bde-813e-3523528cbfcb | -18.03747 | -50.92997 | 2026-09-22 04:04:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e264351-3a1a-3b8c-b292-835973465154 | -13.87918 | -48.5638 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0253e866-205f-3378-abb1-719b3f05c6e5 | -15.6068 | -48.31012 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e52c15dc-be83-37d5-83cc-65c0aff6bf8f | -12.39404 | -47.04995 | 2026-09-22 04:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4c941056-51a4-3729-91e8-fe33872036ae | -16.57761 | -46.98068 | 2026-09-22 04:04:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf49143b-2b06-3f7c-a9c0-31fb0287c4d8 | -18.8819 | -46.85057 | 2026-09-22 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bf148a7-c8d9-3f58-b66b-98ca03fcea0a | -18.88333 | -46.8429 | 2026-09-22 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e99a2ed-c5be-3a0d-ac2a-328d4bd1a0b8 | -12.31773 | -50.18775 | 2026-09-22 04:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 21fbce77-50d1-3a62-9c2e-2a9c46b3333c | -13.22268 | -46.93518 | 2026-09-22 04:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6373f5a-3ca2-3040-a6c5-25374b0f88fd | -14.9203 | -45.14545 | 2026-09-22 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c5bae1f-ef53-3da5-9a8f-2a8a20340b85 | -11.70236 | -51.00163 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72ce332f-41f6-3f75-bab1-d67479b14fee | -18.6546 | -52.15727 | 2026-09-22 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d87b478-3942-3c3d-9743-5fc69e4a7174 | -17.2597 | -45.64124 | 2026-09-22 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f1fa8dc-0536-30a8-89d2-c6434225b252 | -14.77015 | -48.44948 | 2026-09-22 04:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43bc0bfd-9a13-3ccc-ace2-871c1ddb09ac | -14.17796 | -47.88321 | 2026-09-22 04:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c7c30bc-4871-3722-861a-7a5f3190395d | -18.91491 | -46.85312 | 2026-09-22 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07a703e3-5547-37bd-8778-14fb7073a50d | -12.36194 | -50.20111 | 2026-09-22 04:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59271916-c6b8-31d2-b0c2-7be116d696a0 | -13.91955 | -48.56678 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e08e3d95-82c3-3875-b876-8d05971b7b7c | -17.86646 | -44.40697 | 2026-09-22 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22c6535c-3097-3418-bd50-c7eeab6fb58c | -18.97639 | -47.10912 | 2026-09-22 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bfde9df0-dd57-36be-96e6-999b74033916 | -14.67698 | -45.67701 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9aab9441-77de-330a-aa26-cd4c4ae94d9d | -15.75226 | -43.30412 | 2026-09-22 04:04:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1ae46e57-bb3f-38a5-b197-35bd8b6aa757 | -14.66556 | -45.67099 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5b49e73c-f44d-3dd4-95f6-5ad4e358575b | -12.66743 | -50.95938 | 2026-09-22 04:04:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 524297ad-8d69-32ed-8ce4-4588be425920 | -15.66471 | -43.91269 | 2026-09-22 04:04:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b737bd16-2e64-3584-8e77-ac99890db9df | -13.8649 | -48.58466 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95cf3de7-25e0-3a7a-b601-a7ff0c290a15 | -18.64813 | -52.15973 | 2026-09-22 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 358df2b0-c984-3f66-80bc-f141c34d2830 | -14.75283 | -48.43563 | 2026-09-22 04:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbdaeb2a-6b79-3c96-884b-193b24f8b856 | -13.21906 | -46.92964 | 2026-09-22 04:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03dd8342-1ffe-36dd-8379-f01c87956dcd | -12.36116 | -50.20502 | 2026-09-22 04:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3aec9d2-16da-3d36-9942-6c129ca054f1 | -15.98822 | -43.28272 | 2026-09-22 04:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| eb451472-4d44-373f-b981-d0c7dcc3e6dc | -13.92344 | -48.57326 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 73c32067-5dc3-37ae-9caf-a8ab5e09b971 | -11.69498 | -50.99801 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9138ecbd-6a1f-301c-8203-d3bf3e049f42 | -15.44082 | -48.4563 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8774e9b-e1c0-33fa-8e73-c46834774b16 | -13.87228 | -48.57296 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1972d62-e858-3822-b817-3593ad2c26d0 | -15.98453 | -43.00085 | 2026-09-22 04:04:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e1325f7-e8f6-3dda-ae42-d16408cfb07b | -15.84774 | -42.1815 | 2026-09-22 04:04:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| def767ae-ab09-3adf-aebd-71b1c605a2db | -14.04284 | -52.06516 | 2026-09-22 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 631badf6-1a94-34a5-a3e5-03c870b24f9b | -18.73523 | -46.93891 | 2026-09-22 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| a0c1c848-7642-3016-8697-9536f1813874 | -12.29416 | -50.72075 | 2026-09-22 04:04:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bb9a59a-bbbb-3fb4-b3e1-4e40479b3d0d | -13.87829 | -48.56841 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6175eaa0-5290-3263-9e49-6a7ade1047ff | -13.92526 | -48.56887 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 79d8f3f2-5ce9-3a6f-9720-2b630076544f | -11.31174 | -54.05312 | 2026-09-22 04:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d105c73c-127b-388b-af44-3ad7bdeab1ea | -18.03217 | -50.92876 | 2026-09-22 04:04:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b5e6c78-0b4d-359d-a333-c7be0fd8d206 | -13.79913 | -43.69063 | 2026-09-22 04:04:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f683e49-5df5-3f97-a5b6-e709150cd51a | -16.59486 | -41.73348 | 2026-09-22 04:04:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 15fcb70e-d0b0-3324-a605-45621d70e53a | -16.58771 | -41.84056 | 2026-09-22 04:04:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a24d4c08-96a9-3bdb-b40e-9739b443f905 | -12.35166 | -50.22342 | 2026-09-22 04:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fbdba60-302f-3229-b794-05300687727a | -18.02014 | -46.72704 | 2026-09-22 04:04:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc79e03e-bfaf-3471-a2db-2ddfe5f0a603 | -13.17988 | -43.40614 | 2026-09-22 04:04:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05111092-4a24-3482-a86f-b48d70db69dd | -14.66621 | -45.66734 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 219fb7ef-4dd9-3bb7-95c0-7bd61914864a | -17.09559 | -46.17936 | 2026-09-22 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c284599-983a-3df8-a6b9-9bf7c0b4f6f1 | -12.35652 | -50.22852 | 2026-09-22 04:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f91b3726-57c5-3f28-94d5-d9b3844e877f | -12.34603 | -50.22222 | 2026-09-22 04:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f31e99ad-0868-3b75-bdb2-9af0dcf1c52d | -14.6857 | -45.67733 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca9b89ae-452a-3510-90e6-698e10876c1e | -12.35089 | -50.22733 | 2026-09-22 04:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2081f24d-fd79-3d1f-96b4-a35db0a077f3 | -16.43888 | -43.46851 | 2026-09-22 04:04:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 822db810-0b1e-3626-83f7-4ea34a903e2f | -15.45097 | -53.124 | 2026-09-22 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d8ce9634-59ec-323a-b2f9-9e28bfcae247 | -11.69638 | -51.00038 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2193b04-be7b-3051-a083-a360b1418668 | -15.7235 | -41.57247 | 2026-09-22 04:04:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9871f0eb-1ff5-3f4d-a5a0-76ebf78d0fe0 | -11.75976 | -50.82547 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f7e5027-809f-3d43-a621-19894640d677 | -14.96436 | -48.75235 | 2026-09-22 04:04:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7cd9a1f-9bed-39a5-8c3d-9dfc82e12d9c | -11.75647 | -50.82685 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd885057-775b-3011-9b6e-415a8dc6fc28 | -15.26536 | -47.61497 | 2026-09-22 04:04:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33665ca1-e0cd-3d75-ab4c-736db6b4baa9 | -15.3583 | -48.11715 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25f972d0-21fe-3114-8b04-919166c8fde1 | -12.39592 | -47.06532 | 2026-09-22 04:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ffb07854-e795-3ea1-b7ec-ed458237b93f | -13.21736 | -46.93891 | 2026-09-22 04:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ca98944-1ffd-3064-acba-d42b0bc814ee | -18.7345 | -46.94273 | 2026-09-22 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cfd5b059-f5eb-32a9-9b21-c0e5a04f407d | -13.54108 | -42.24211 | 2026-09-22 04:04:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d17032c6-fc5f-34e2-a573-9d5d9f42d043 | -14.63541 | -45.67644 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cecf8587-4ba5-3293-883f-03f6c257e6a9 | -18.85118 | -47.4066 | 2026-09-22 04:04:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3730b568-b823-3449-9132-5e2e6803f2ea | -13.86727 | -48.57241 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86e7f8ac-3e9d-3ca4-8552-d663542e3d5b | -17.83974 | -45.78411 | 2026-09-22 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3909b35e-1419-32dc-90ab-f27dbd25c6b8 | -14.76645 | -48.44273 | 2026-09-22 04:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c28ee49a-3b64-30f1-84b8-de304c9b5c99 | -13.22183 | -46.93985 | 2026-09-22 04:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b0663a1-491d-3952-87b7-a882d0c1ae91 | -18.77055 | -45.11536 | 2026-09-22 04:04:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d17ed763-2224-3700-a4b2-ac51f0462931 | -13.85268 | -51.84965 | 2026-09-22 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4c52b550-8aa9-324c-8aad-b450cdb020dc | -15.2663 | -47.60995 | 2026-09-22 04:04:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a928334f-b97f-36e3-bce4-f026892df389 | -18.73929 | -46.93975 | 2026-09-22 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 08cd6faf-79df-315a-a743-e686c94ba867 | -15.437 | -48.45048 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2417ba13-8399-33a1-b161-61be1b872949 | -15.36395 | -48.11297 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd961ea3-90fb-3c7b-890a-4e45d8e5507d | -18.98047 | -47.11002 | 2026-09-22 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7db2e06b-7955-3b32-ad7d-2a037e33150f | -11.32199 | -54.0398 | 2026-09-22 04:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d1f1d164-371d-3743-bc94-860b65f1b3bb | -13.86383 | -51.85693 | 2026-09-22 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a87c255-adee-3248-8a40-a499687b1e27 | -13.89979 | -48.56312 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b4af18df-8acc-31d9-b449-372d0a7eff8c | -19.38858 | -45.21119 | 2026-09-22 04:04:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f88a1e7-0802-3cee-94e0-2f380ee77b00 | -15.45037 | -48.48243 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a63415cf-fbc3-35e9-8613-194bc3437970 | -14.75555 | -48.44741 | 2026-09-22 04:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8dac3f4-3d3b-3e89-81a8-e8b2e91141bc | -15.56709 | -42.64151 | 2026-09-22 04:04:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bdb72b8b-9734-3b92-b47c-3fa682b12eaf | -12.94951 | -50.92691 | 2026-09-22 04:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README41.md)
