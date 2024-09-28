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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0f1cc5b-c1dd-31f4-97e5-2edb60cc21e2 | -20.22244 | -42.86956 | 2024-09-28 04:23:00 | NOAA-21 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f848b7e7-494f-3a18-9856-25511d344efb | -19.99843 | -42.40734 | 2024-09-28 04:23:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a171a4e2-a93d-3613-b249-ff81652bd4ff | -19.99796 | -42.41097 | 2024-09-28 04:23:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5afae620-5cc8-3a5b-acfa-c520694579fb | -19.99749 | -42.41473 | 2024-09-28 04:23:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ee1419d0-4e24-3415-9efa-54b655c8c748 | -19.99342 | -42.41418 | 2024-09-28 04:23:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f1db0b05-eab2-319d-9160-7d43b90615c0 | -19.87971 | -42.16342 | 2024-09-28 04:23:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1be8a42e-0912-30fa-9372-9e1488fde2f0 | -19.87557 | -42.16304 | 2024-09-28 04:23:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8bd95506-e494-3cf1-9f3e-5816efeee2a7 | -19.87157 | -43.17589 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 13551e1f-f221-3cd1-9a47-880046a442a9 | -19.86732 | -42.16203 | 2024-09-28 04:23:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 83b95654-77b5-39f2-b2b6-21c7b0d276e5 | -19.86408 | -42.35671 | 2024-09-28 04:23:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4c282d68-d253-304a-8c57-bebbbe7bc2b2 | -19.82484 | -42.40634 | 2024-09-28 04:23:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7f56fe8e-e429-3d58-8188-dd970aaa21df | -19.6753 | -42.43933 | 2024-09-28 04:23:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ab39cc53-362d-337e-8eb6-7074ca9bd736 | -19.64521 | -42.85394 | 2024-09-28 04:23:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ea2e203c-b00d-3521-90b7-2c7fa325152d | -19.62678 | -42.84539 | 2024-09-28 04:23:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c80ad455-2efb-3f46-ae7c-0fdfdcf6e713 | -19.51698 | -42.88952 | 2024-09-28 04:23:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| df194532-3f7d-3a1e-a511-781bada6817a | -20.67229 | -43.32219 | 2024-09-28 04:23:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 6e5c87be-d7ad-386f-8d23-e222a73b83c2 | -20.67147 | -43.3199 | 2024-09-28 04:23:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2f0541ab-d411-36be-964b-a72ab703a05d | -20.67079 | -43.32499 | 2024-09-28 04:23:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| def3fe82-f716-3a40-be7e-f3576e57f354 | -20.66839 | -43.32178 | 2024-09-28 04:23:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| b2db3193-6a6a-38f4-b64c-3b6ce1ed4232 | -20.6378 | -42.25951 | 2024-09-28 04:23:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 6fb3b284-0209-365e-9b3b-25c9c7011410 | -20.63732 | -42.26345 | 2024-09-28 04:23:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 77c1fdc9-4328-337f-aa97-59aef9060bbd | -20.61536 | -42.89413 | 2024-09-28 04:23:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 63012eaf-8bae-30a4-bdcb-8d946d5a1292 | -20.61467 | -42.8995 | 2024-09-28 04:23:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f9d3c957-5b45-37ca-9c39-db94ceb736dc | -20.61385 | -42.89471 | 2024-09-28 04:23:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7d3a721a-9e8d-3893-b76a-b27015c2e0b0 | -20.50705 | -43.50855 | 2024-09-28 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1acced47-6ba4-3fb9-b04a-aee4a1b9d0a8 | -20.49589 | -42.16125 | 2024-09-28 04:23:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ba3eb634-041d-3d4c-b6d1-967b07d70028 | -20.49541 | -42.16531 | 2024-09-28 04:23:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 5743b3d9-507a-3923-8016-2146ae06b9ea | -20.49495 | -42.16914 | 2024-09-28 04:23:00 | NOAA-21 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| e1c6307e-a682-3563-bb22-d493fe9412ae | -20.49379 | -42.16175 | 2024-09-28 04:23:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 0990801a-d35a-39e8-b058-ad87b737d1ab | -20.49329 | -42.16571 | 2024-09-28 04:23:00 | NOAA-21 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 3df2c764-aa30-3036-97f8-5829a48cd080 | -20.49174 | -42.16058 | 2024-09-28 04:23:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cef5d441-c6d3-34fd-8dcf-e868b2e44965 | -20.49126 | -42.16462 | 2024-09-28 04:23:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9ed152af-1698-3594-98bd-fc91ce9c6e1f | -20.45599 | -42.91847 | 2024-09-28 04:23:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 861ea57d-40a9-3d9e-aa9b-69a03fa48439 | -20.45531 | -42.92384 | 2024-09-28 04:23:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 05cc3d3b-9ab7-3ea2-b85e-a678f7054ba0 | -20.45204 | -42.91782 | 2024-09-28 04:23:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e9e1155-2110-3550-817c-493cf9a576d0 | -20.45135 | -42.92321 | 2024-09-28 04:23:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| bb81a05f-f0f6-39a5-8749-132d7def0ff1 | -20.87653 | -43.22041 | 2024-09-28 04:23:00 | NOAA-21 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 56a3bd64-e96a-3bcf-86ad-3d70f3703eb7 | -20.81944 | -43.32438 | 2024-09-28 04:23:00 | NOAA-21 | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3d2a808e-5750-3c31-9671-e0ec69ab87e4 | -21.8905 | -42.6753 | 2024-09-28 04:23:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bb309336-7f00-3516-a25e-6fe83698fc19 | -21.88688 | -42.67078 | 2024-09-28 04:23:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0787788e-87b7-3ea5-b1af-a9f9a9880c45 | -21.63922 | -42.80022 | 2024-09-28 04:23:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7c00d128-cf8f-34e0-aeb9-07507a535f94 | -21.63296 | -42.81763 | 2024-09-28 04:23:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| accec863-52dd-3f40-8f08-d3320020fde6 | -21.39509 | -42.96793 | 2024-09-28 04:23:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f0c59214-6e27-3ba7-b42f-20a8265c599c | -21.3911 | -42.96728 | 2024-09-28 04:23:00 | NOAA-21 | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| af15f794-dccf-34d0-908a-13973f105e9d | -21.13819 | -42.25388 | 2024-09-28 04:23:00 | NOAA-21 | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6819ab1a-b8a6-38a2-b2e2-298b4e01f3c5 | -21.13774 | -42.2577 | 2024-09-28 04:23:00 | NOAA-21 | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 795ea9b4-552e-3937-ba24-31c049582d5b | -21.10895 | -42.7695 | 2024-09-28 04:23:00 | NOAA-21 | GUIDOVAL | MINAS GERAIS | Brasil | 3128808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 72f717ab-6fe9-30f1-86cf-2317f6052e36 | -21.10848 | -42.77325 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 849072bc-c706-3e85-b7e6-e95786bfc1c3 | -21.03841 | -42.6691 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 868a6f60-8077-3e26-8f21-976e09f0e037 | -21.03798 | -42.67255 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 7e6ec22f-6d5c-3791-a116-8f7333cbc130 | -21.03754 | -42.67601 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| bedf7233-3e65-310a-839b-67d9f9ee71bd | -21.0357 | -42.65781 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| ef28be9a-0258-37be-92aa-5f7ba45a5656 | -21.03525 | -42.66138 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 5a1c88bf-653f-3ff8-9665-294f9bc6dca8 | -21.03481 | -42.66488 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 5a81038c-e7b0-37cb-ab26-5219fa7db683 | -21.03438 | -42.66835 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ed2aeb8a-98d0-3dd1-9bac-588d9cfaddb6 | -21.03393 | -42.67188 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8d826ae5-7341-3f16-9c2e-51ac2e749857 | -21.03349 | -42.67541 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 20a8f432-ca20-383b-8bbb-a4ad2889b8bd | -21.03304 | -42.67897 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1c969b53-e226-3b56-8f0a-81a7faaa9c6a | -21.0308 | -42.66394 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 451b9f07-b4e5-3687-9c99-bd57174aece9 | -21.03034 | -42.66759 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f54aa84f-5233-3823-bd8e-79138c5d5a0b | -21.02989 | -42.67125 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 24068d21-5f79-3ff6-a922-facd1e22da0a | -21.02944 | -42.67484 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1a3c8b58-6d5f-38fd-8082-b9b3b324c075 | -21.02899 | -42.67842 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a578c1e2-1701-37b9-9bee-27aef4ebe99a | -21.02631 | -42.66683 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 914e90cf-15ee-376e-90b4-885e32a9fb1a | -21.01729 | -42.673 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| a92d2c37-1dc9-3403-9967-55da9f6edb29 | -21.01686 | -42.67646 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| a4d2f599-c434-3c3e-9de4-68bc0d27fabf | -21.01369 | -42.66882 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a1824a12-87db-3233-97ac-b6e35a62baa3 | -21.01323 | -42.6725 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| c790ab47-57f6-3f78-aff1-18a7ec79f073 | -21.01281 | -42.67588 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| d861d5e0-b7e4-3fa8-954f-66726f69ee7c | -21.00966 | -42.66802 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ba1ad0cd-639a-3c61-9750-365a9d275e07 | -21.0092 | -42.67171 | 2024-09-28 04:23:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| faf4b800-ed5d-3aee-8f24-95115300ea08 | -20.99495 | -42.85226 | 2024-09-28 04:23:00 | NOAA-21 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ca8cd1b8-f69c-3560-86d6-6c3588d017bf | -20.99095 | -42.85165 | 2024-09-28 04:23:00 | NOAA-21 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7012ab29-82d7-3097-94fe-86895fdb2b05 | -17.83491 | -44.44998 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 004f70fb-cb9a-3e9b-8346-b025685039f6 | -17.82143 | -44.46889 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e681977-2567-3e2a-bd4a-0910258863e7 | -17.81438 | -44.46765 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9874cf29-8734-3ce5-bb54-71a135b0fbc7 | -17.83665 | -44.43757 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04cfd215-07cd-341b-bd67-6b587ace5981 | -17.83255 | -44.44108 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a072bf6-99db-354a-b17d-7f1445d428f7 | -17.83607 | -44.4417 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00fd8a28-e430-3910-a9e4-6e63b2216de5 | -17.96385 | -44.24953 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73cbe958-47ec-33f7-ba78-ccef42ff5ed0 | -17.96028 | -44.249 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b5477ee-8e6f-3017-85cc-dcd3be044e2f | -17.95969 | -44.25323 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 843e2211-8659-3518-8a0f-cb2203408826 | -17.95671 | -44.24844 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b246a44-afc8-387b-b249-56265b1f63a0 | -17.95612 | -44.25274 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f72eae01-90e3-36bd-acce-e07b286bd78e | -17.94957 | -44.24728 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71470713-43af-320c-b4b6-bc510d213561 | -17.947 | -44.24812 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7c5af4b-6745-3690-9f4a-4378fee46dd0 | -17.946 | -44.2467 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cfb32e0-7ad7-3248-8228-84c52d5289e4 | -17.94342 | -44.2476 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 64503740-a29e-345c-a27a-450a4ec20867 | -17.84262 | -44.47213 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4bb16a11-8f9c-393e-a3ce-af9e97aed537 | -17.83549 | -44.44584 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1184f9cf-3930-36e0-8afe-1ae63679e9b6 | -17.8179 | -44.46828 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c06b0e6-8721-3af0-a5fd-9ed2ab9e1acc | -17.75975 | -44.34211 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17434fd8-f30d-3809-a08b-3c425294c9ad | -17.75621 | -44.34151 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37aa78a2-28fc-31c1-aa31-cc5cda88c7f5 | -17.73891 | -44.25747 | 2024-09-28 04:23:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0263192f-34df-31fc-b1c4-878ec4859990 | -17.69277 | -44.20415 | 2024-09-28 04:23:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7b30348-cdcb-3c82-af3c-ea4e9852d9d7 | -17.68921 | -44.20355 | 2024-09-28 04:23:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| de1c8d62-17e2-3d8c-b76c-2385f497151f | -17.51956 | -43.62676 | 2024-09-28 04:23:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c796f9b-dd1f-3923-b7a8-d84915f89786 | -17.51652 | -43.62162 | 2024-09-28 04:23:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67822deb-8676-3bcc-8fa9-2d34dcc9d0d0 | -17.5138 | -44.31876 | 2024-09-28 04:23:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f8b9f7a-0f30-3408-a44f-7b2f9d08ed99 | -17.79929 | -43.2707 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 73.2 |


[Clique aqui para ver as próximas entradas](README62.md)
