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

## Dados Diários - Página 232

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 108d903f-91be-352e-9852-e3a27c68c46b | -11.57661 | -42.81497 | 2026-10-09 11:21:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 0aab6d6d-f3c2-37c9-86d1-0ccadcf132f5 | -9.89911 | -44.79823 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| da8fdacd-ada4-3937-8776-33c5a908577b | -15.42349 | -41.02491 | 2026-10-09 11:21:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 5e69c2ca-d86a-3813-9c4b-cac0da421778 | -9.08062 | -45.1072 | 2026-10-09 11:21:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 490bd8a8-a6a9-3fb3-b0c7-2919a4195562 | -14.81502 | -41.66432 | 2026-10-09 11:21:00 | TERRA_M-M | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f0805178-2499-3baa-86bf-da139bc51779 | -14.21103 | -41.83899 | 2026-10-09 11:21:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 29.7 |
| d7be8e67-698c-37d3-af51-ee5611bf3005 | -11.78947 | -46.79466 | 2026-10-09 11:21:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 9b03661c-4e31-306b-a703-eda4c7699704 | -12.50285 | -42.13359 | 2026-10-09 11:21:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| bd3475ed-df33-3d8d-bae7-2259de242bfe | -13.35179 | -40.98196 | 2026-10-09 11:21:00 | TERRA_M-M | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e65482dc-df47-3a82-bf56-b7a3411d099c | -14.41216 | -41.85022 | 2026-10-09 11:21:00 | TERRA_M-M | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 856a3d67-1aa7-322c-be1a-a25556716b19 | -9.22383 | -45.65852 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 00ab1bfd-5225-37d2-9846-c58b0a3aa722 | -11.58318 | -43.65709 | 2026-10-09 11:21:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 501a7dd7-68c8-3288-8b1f-37ee5c97b624 | -9.29424 | -47.42345 | 2026-10-09 11:21:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 8f57a6eb-9cab-3bd9-9ae5-2610b7d84b19 | -11.83214 | -43.60076 | 2026-10-09 11:21:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 7b8acd0c-c10e-3de3-ba6d-0745caafc148 | -14.32052 | -42.38412 | 2026-10-09 11:21:00 | TERRA_M-M | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 8bd91146-3145-33df-99a9-51dd5ca20225 | -13.11033 | -46.33953 | 2026-10-09 11:21:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 125ab908-285d-36c3-a7fe-0724a45c7cf6 | -11.23739 | -44.87827 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| db90eb41-8ae7-3718-b702-fdd5cb178247 | -9.03707 | -44.38954 | 2026-10-09 11:21:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| fa1ae20b-4630-306a-9171-88b00a6126e8 | -11.01427 | -45.42548 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5dd5c73a-ba4e-3fb4-82af-5b527572f073 | -12.80543 | -42.47815 | 2026-10-09 11:21:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 1d08bac3-5bb8-35b6-96d8-72901a85a5c3 | -8.53526 | -46.89823 | 2026-10-09 11:21:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 9f59b5cf-512b-3ca7-af21-36e346aa4036 | -10.90804 | -45.51547 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| b0ee3343-5c8f-391f-9996-0f43a0fc0293 | -14.20068 | -41.84731 | 2026-10-09 11:21:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 5340c60d-f21c-30de-9951-b5af234f7111 | -12.80669 | -42.46914 | 2026-10-09 11:21:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 67ad6ca2-3234-30ae-8a9d-d776be2e0490 | -11.22537 | -45.31675 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9cd88074-6c99-391d-bb17-317dc447a358 | -10.89659 | -45.52521 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| abce43d5-ffe2-3d4f-9dc1-e4d6307be804 | -12.8246 | -44.44653 | 2026-10-09 11:21:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6ffce61e-b127-30d8-881e-12d91f4a1e09 | -9.31215 | -47.45882 | 2026-10-09 11:21:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0d6df5b6-ce37-331e-87fa-c94e30e2bf86 | -11.83479 | -43.58261 | 2026-10-09 11:21:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 849c650f-6a37-38d1-a5b4-3ea662b4040d | -15.82178 | -42.58439 | 2026-10-09 11:21:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 6f7cde6a-8480-3509-9b3c-745be7583d6b | -8.98234 | -45.89229 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 1281cb50-0336-3f3a-af36-b70480d81f89 | -9.92897 | -44.79203 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fe74482c-c93f-3ae4-afc1-901f8d1c8791 | -15.01365 | -46.25821 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 67612ff7-8d22-3cad-9038-523f49995372 | -13.3777 | -43.37477 | 2026-10-09 11:21:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| f167980f-ea3a-3e3c-a025-097afce4703e | -10.53519 | -47.31145 | 2026-10-09 11:21:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 18580cec-1493-3b2a-93f5-315b98e0b346 | -11.31854 | -46.64746 | 2026-10-09 11:21:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 96456309-9308-3af4-afe4-3aa9261128b3 | -15.95677 | -41.09034 | 2026-10-09 11:21:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 0fc03b60-70c3-3eca-a6cc-e4ddf5e9fff7 | -11.34378 | -46.69209 | 2026-10-09 11:21:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9923d18f-00d6-363a-b6b9-feb00277f618 | -11.87304 | -47.37795 | 2026-10-09 11:21:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 046c510d-9e7a-3a82-bbfd-c7880fe1bdca | -13.3671 | -40.43079 | 2026-10-09 11:21:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| f6d854e5-2612-3ae3-8e24-28ca0e5f4eed | -15.13613 | -42.01175 | 2026-10-09 11:21:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 9bad3045-6f6d-395c-bd71-2e9317ee897b | -10.9458 | -50.67509 | 2026-10-09 11:21:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| c4148d08-8c48-35e5-8de4-b2b37108e937 | -16.4187 | -40.342 | 2026-10-09 11:21:00 | TERRA_M-M | SANTO ANTÔNIO DO JACINTO | MINAS GERAIS | Brasil | 3160306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 079f43d7-a4ba-355d-ba11-55471165bc73 | -11.65366 | -43.6827 | 2026-10-09 11:21:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6c5de2e8-49f8-3e88-bceb-023cec35b7bd | -17.00783 | -41.15693 | 2026-10-09 11:21:00 | TERRA_M-M | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| bb10a89f-742e-3689-9b3c-5c1ee44fca47 | -10.87547 | -45.53312 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 5cf54958-b859-3093-8d99-d7bbccbb2842 | -12.1852 | -44.64893 | 2026-10-09 11:21:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5ac0d5e3-446a-3721-8fa1-6449ec06f7b3 | -12.90853 | -45.11785 | 2026-10-09 11:21:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 00cfa954-3825-3aa8-8a81-c143516c0980 | -14.81636 | -41.65443 | 2026-10-09 11:21:00 | TERRA_M-M | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b1e695df-b654-3c32-bf02-75488cf9560e | -14.41347 | -41.84058 | 2026-10-09 11:21:00 | TERRA_M-M | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 8d110753-afe7-3740-af08-e0ccff6cbb9a | -14.62681 | -46.94951 | 2026-10-09 11:21:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| aff9b565-52d6-36f8-982a-feea893934a6 | -10.93935 | -45.37517 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7048b165-a433-326c-9a34-b35c4766c780 | -16.47123 | -45.50495 | 2026-10-09 11:21:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 145eccf7-5bc8-3f07-8da5-bad979a40b8b | -8.92096 | -45.22319 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 284.1 |
| 0e5532db-21a8-3e67-a8da-5a6453ad90e3 | -11.66121 | -43.69317 | 2026-10-09 11:21:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d1e81385-d52a-367b-ace1-6e989a6e8bb4 | -8.97334 | -45.89704 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| ac090df0-e72d-35ef-8acc-839f614a49c3 | -11.26495 | -46.26195 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ef27a6c0-f27e-38ea-abe5-46733d0d02eb | -16.70418 | -43.79346 | 2026-10-09 11:21:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 797ac53a-9568-38a5-8996-fbe6dc929a3c | -9.86917 | -44.86791 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a3c716f4-ec70-37bc-87ea-dbc2316bf7b8 | -11.06147 | -44.06816 | 2026-10-09 11:21:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 51351722-fe3b-33c2-a92c-3214c1154ef7 | -8.97014 | -45.90315 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| bdac660b-f5a2-36b3-807f-a73d1a136c07 | -11.78441 | -46.80005 | 2026-10-09 11:21:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 2e350542-75db-3324-8078-98a7dfc58515 | -15.76265 | -42.87886 | 2026-10-09 11:21:00 | TERRA_M-M | SERRANÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3166956 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2737728d-4765-34f4-85a4-f9ba4faadec1 | -11.78813 | -45.58374 | 2026-10-09 11:21:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| b634b5d6-4ae1-336c-85f7-95df7776f59a | -16.70288 | -43.80259 | 2026-10-09 11:21:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 35a0f405-24c8-37c2-9da5-5e792e458a61 | -15.4276 | -41.69245 | 2026-10-09 11:21:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 76040ab0-e9f8-36e9-9de5-6c40a6519377 | -11.79479 | -46.80219 | 2026-10-09 11:21:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b6c37a3f-8530-3a95-ab3d-fadb042b47ed | -11.41608 | -46.68306 | 2026-10-09 11:21:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| c12e72d9-da9f-3b88-be4d-536776799012 | -11.25568 | -45.24533 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6cbb742f-99c7-3fe0-a2ee-ef7c336a053b | -14.84999 | -41.40503 | 2026-10-09 11:21:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 1125ec5e-ecef-3163-ad8b-2fc8cb5bb2e6 | -14.12856 | -40.67955 | 2026-10-09 11:21:00 | TERRA_M-M | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 314af90b-1694-337f-882c-9b365a33fa97 | -11.66891 | -46.76919 | 2026-10-09 11:21:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f7d5c9a5-992a-3026-ad27-f5d79ccb21d1 | -8.53516 | -46.90424 | 2026-10-09 11:21:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 916c1363-10bf-3875-bc95-2930d80944aa | -11.05522 | -44.04805 | 2026-10-09 11:21:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 30530beb-e12f-32cd-adb9-3a6641641625 | -15.13744 | -42.00214 | 2026-10-09 11:21:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| c4767a30-3daa-35e2-a06e-139eac6267c8 | -11.99833 | -43.46516 | 2026-10-09 11:21:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 860bbee7-dea6-34cc-83ff-28a0122dd694 | -11.05384 | -44.05743 | 2026-10-09 11:21:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 4c33b5aa-1d49-3441-a1e2-35a1a47eedf9 | -11.11693 | -45.68439 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| fd9a8aea-5ab5-3f3f-a9c4-1149ad3af6cd | -10.89835 | -45.51379 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1edf1808-c1db-3466-b1d1-27ea5737e634 | -11.99442 | -43.49211 | 2026-10-09 11:21:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| ced0b429-eb1f-370d-be1d-ae4a752f832e | -8.93077 | -45.22461 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 3e381bcb-e2e4-3430-b9b3-4f7260fee06d | -11.75477 | -45.47913 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5e2fb24a-9439-3a5a-bbd3-acd01ee268c7 | -13.70759 | -49.10275 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 35.8 |
| c498b175-473a-3583-9f59-b8235e1c4335 | -14.46302 | -40.85833 | 2026-10-09 11:21:00 | TERRA_M-M | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 44df6342-5fb3-3c71-adf4-208f79fb87c6 | -14.3711 | -40.71024 | 2026-10-09 11:21:00 | TERRA_M-M | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 4e333ee3-5798-35c8-afe9-0e0a823e0ad7 | -13.27804 | -46.97149 | 2026-10-09 11:21:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 109.6 |
| b78bd36a-f9e5-3f71-941d-ef490f18b311 | -14.59065 | -42.1592 | 2026-10-09 11:21:00 | TERRA_M-M | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1c42c9ee-4e81-3c4f-bd76-f96176b4dac2 | -11.41804 | -46.67033 | 2026-10-09 11:21:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| f75dd1b7-d935-3140-a999-9f2d3125e43f | -9.88966 | -44.79691 | 2026-10-09 11:21:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 84dfc06a-fc6d-305f-b124-89e0183fd400 | -14.20197 | -41.8378 | 2026-10-09 11:21:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 25.5 |
| e3dc3974-d8d0-328a-a4c0-ae368e29ad3b | -17.00641 | -41.16784 | 2026-10-09 11:21:00 | TERRA_M-M | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 31f047b9-3db6-3ebe-b0db-97fdc9bf249a | -10.87986 | -44.79903 | 2026-10-09 11:21:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 090bd25a-071c-3425-8c2c-74fa6fa17618 | -14.91973 | -41.43106 | 2026-10-09 11:21:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| ceab5a98-3ec8-34be-b256-c9cfa631b034 | -11.23818 | -45.29671 | 2026-10-09 11:21:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| ed36d828-ec65-379e-93d7-921cbe2b8ada | -13.79718 | -40.02126 | 2026-10-09 11:21:00 | TERRA_M-M | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 2ffa033f-262e-3a9a-b751-272d0f2d8a59 | -10.94748 | -50.68256 | 2026-10-09 11:21:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 5cfb047f-b737-3120-bdd2-01df768b2602 | -10.75042 | -46.60123 | 2026-10-09 11:21:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 559e5530-554f-3574-80ba-2a928a587796 | -9.09037 | -45.10835 | 2026-10-09 11:21:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| a146ecf5-e13e-3f2f-9e3a-ad7f9d9e02ca | -8.92265 | -45.21203 | 2026-10-09 11:21:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| abf91696-2790-369f-8fa8-3eeafac49073 | -11.84365 | -43.58391 | 2026-10-09 11:21:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |


[Clique aqui para ver as próximas entradas](README233.md)
