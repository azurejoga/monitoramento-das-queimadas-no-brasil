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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64d4afab-af22-31a6-8020-15c595b3dfff | -13.1569 | -44.64084 | 2025-10-04 03:25:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44d92794-1fb7-3795-a0e2-9e0db5ebf9e8 | -17.99384 | -45.01744 | 2025-10-04 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82ddae19-afa5-36d0-9a39-ddc82f87fb2a | -17.95638 | -44.25729 | 2025-10-04 03:25:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ae35f58-1860-31a8-bee8-b5acbe4b6e4a | -14.2306 | -46.08503 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 144a187b-b427-3571-b0b3-70603462d6ec | -11.72113 | -44.44467 | 2025-10-04 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cad0428b-dc2d-3231-9a10-2ddeedd5e0b4 | -12.93215 | -45.07037 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5575a308-7684-32b2-a197-b432f9563ce8 | -15.72563 | -46.28407 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cf1975bd-6ce4-3958-a6fa-76ee774e0e29 | -11.49871 | -44.99565 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5481f42a-f414-3d89-affd-49fa9591d1ad | -15.6217 | -46.93517 | 2025-10-04 03:25:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3318914d-f582-3dae-92eb-7a5db8f20e19 | -14.24323 | -46.09305 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 546320f2-921b-3511-94fb-3f126e816358 | -14.3553 | -46.10648 | 2025-10-04 03:25:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 24f2faa1-b91b-32cc-b330-146903fe8c39 | -14.92039 | -46.87918 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 15edc082-e0ce-3f9f-9b06-8fdecd522083 | -12.53058 | -45.97092 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dfede22a-1d71-3147-b3ef-06739fc61bda | -14.94365 | -46.85852 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3ade1b6a-d35d-32e4-88c5-38b48bdd7cfc | -21.28089 | -45.05907 | 2025-10-04 03:28:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f9ed6c28-9108-3712-9b4b-8cf37c505afe | -19.57531 | -48.0149 | 2025-10-04 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a1deea90-9966-3ffe-9446-271818239880 | -22.49047 | -44.07726 | 2025-10-04 03:28:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8282b9c4-5c7a-33df-996d-f421bf5fea70 | -20.41746 | -44.13417 | 2025-10-04 03:28:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a1943970-243b-3ede-983d-13704b1f100c | -21.34177 | -45.00057 | 2025-10-04 03:28:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a8bd0013-31f0-310b-843a-c7828780666d | -19.97531 | -43.70717 | 2025-10-04 03:28:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8d351b11-08e3-3900-b118-f8b347027225 | -20.13321 | -43.98776 | 2025-10-04 03:28:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 92125328-ca49-3498-b319-c77a04477458 | -20.46706 | -44.81953 | 2025-10-04 03:28:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ab0cd32b-0d3b-33e2-a4ef-4bde8fff3f27 | -20.0306 | -44.0644 | 2025-10-04 03:28:00 | NOAA-21 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 363d3457-a603-3ffa-a66d-b900f20d3c83 | -21.34978 | -45.79492 | 2025-10-04 03:28:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ed737d43-c3a0-3b58-b5dd-d01381f6367f | -21.59595 | -45.27823 | 2025-10-04 03:28:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b90e123b-ba00-3338-bc4f-f3ee534282a6 | -20.22408 | -44.17633 | 2025-10-04 03:28:00 | NOAA-21 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 4915d58f-065a-3701-8d47-fab91b6ebb6d | -19.96925 | -43.70913 | 2025-10-04 03:28:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 16fda368-07a3-3f9a-91b1-50d447eff732 | -22.57117 | -42.37883 | 2025-10-04 03:28:00 | NOAA-21 | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ff813a26-7348-3279-ba76-d8387e51ee6b | -20.14288 | -46.42459 | 2025-10-04 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 525c3041-c97f-3d7d-8ec4-82de31a0b399 | -21.78923 | -45.33382 | 2025-10-04 03:28:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4ea07e97-b99f-344e-926b-905d09849e79 | -22.76226 | -45.30423 | 2025-10-04 03:28:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 999ec842-5900-381a-addf-002dd6f1626b | -21.78823 | -45.33822 | 2025-10-04 03:28:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e1db6843-ad5a-3298-a5ad-3c8cd4c7f5ef | -19.58648 | -45.90451 | 2025-10-04 03:28:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d87fb6bd-0064-32dc-84be-989fedd196d7 | -19.52258 | -43.83698 | 2025-10-04 03:28:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8233d486-221c-3f57-addf-979d67758a39 | -22.28747 | -46.75614 | 2025-10-04 03:28:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b35fd6dd-730a-33f6-a225-bae8eb7f1ba7 | -20.4718 | -44.82513 | 2025-10-04 03:28:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| c15306f3-5168-34c9-b341-7699bf1a0456 | -21.19506 | -45.14233 | 2025-10-04 03:28:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 170b0572-03f6-35ef-b2d5-c4f4b90bb773 | -19.51827 | -43.83128 | 2025-10-04 03:28:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c57f07b9-a64a-3c97-8277-1f0537e93bef | -19.52287 | -43.83646 | 2025-10-04 03:28:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c015f4de-2786-37d9-8281-642531067f0c | -21.19408 | -45.1467 | 2025-10-04 03:28:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 09bd77c2-e038-3822-9497-87f3bba6b177 | -20.13798 | -46.41731 | 2025-10-04 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 213c9c0d-2760-3a8f-a8e8-de7337ced520 | -20.62845 | -44.24745 | 2025-10-04 03:28:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c5e831c1-4523-35e9-8c86-24feec081e63 | -19.80272 | -45.15588 | 2025-10-04 03:28:00 | NOAA-21 | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5edfa694-1c19-3c0d-a8f4-169762420c90 | -21.25834 | -45.18514 | 2025-10-04 03:28:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 37edb8b5-3ebd-3f9f-94d8-be682f8489d3 | -19.71245 | -44.12398 | 2025-10-04 03:28:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f38c70df-94e1-370f-ad6b-36860b93959d | -20.06932 | -43.75117 | 2025-10-04 03:28:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2a151a55-1123-32a3-8792-50fedc59f051 | -21.80772 | -45.65045 | 2025-10-04 03:28:00 | NOAA-21 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ba595d4d-c6ae-385f-8d26-6ba8dc948e03 | -19.57346 | -48.02243 | 2025-10-04 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d477d782-550b-326f-9060-1e7c512da47f | -19.45901 | -43.6499 | 2025-10-04 03:28:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c6b4c57-09fb-339c-a0a7-a488e1ae97b5 | -19.91796 | -42.92049 | 2025-10-04 03:28:00 | NOAA-21 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a66f04f2-2cbd-34e6-8108-fa853560baf9 | -21.49009 | -43.89452 | 2025-10-04 03:28:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6dc7b3de-24a8-365c-adf5-d5a4e14ee7ff | -20.94878 | -45.81353 | 2025-10-04 03:28:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 037e28b9-49d8-3bbc-b716-b7bdbb1fca1d | -21.34264 | -44.99667 | 2025-10-04 03:28:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| dd50f9e7-9285-347e-84fa-a3ee5ef4483e | -19.76834 | -43.78757 | 2025-10-04 03:28:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 448585ce-4694-337e-abaf-9938588a1df1 | -20.02974 | -44.06841 | 2025-10-04 03:28:00 | NOAA-21 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bee8e8dd-fae0-3488-8cda-d3c9c8d49795 | -21.19395 | -45.15016 | 2025-10-04 03:28:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 682683de-6a21-3f73-ae86-2fb3d4e72a2c | -19.52343 | -43.83298 | 2025-10-04 03:28:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 26dfe2a7-3091-356d-94cd-567ae67a99cc | -20.13987 | -46.42505 | 2025-10-04 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| a64ad0ed-03d3-38e5-ada8-31d43e756aa7 | -20.94663 | -45.81327 | 2025-10-04 03:28:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7d4fbb0d-b9ae-30fe-98cb-b815744f83d0 | -20.13728 | -43.99545 | 2025-10-04 03:28:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c8e726cc-9c5c-3986-aa74-14e15a89e021 | -19.46534 | -43.6468 | 2025-10-04 03:28:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ac7475b-1cee-32ec-94e8-fe87d1d88901 | -20.41196 | -44.13306 | 2025-10-04 03:28:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 91d205da-7e6d-38e4-87db-074a7a7871bf | -19.81664 | -46.06968 | 2025-10-04 03:28:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f1c30ca-cfdb-3757-a8fd-97da7c2032ba | -20.46803 | -44.81519 | 2025-10-04 03:28:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0651e01c-4f08-3857-8ad5-429f6451698f | -19.52374 | -43.83249 | 2025-10-04 03:28:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f1279ee9-c020-3207-991e-98e106aeadf6 | -19.58765 | -45.89936 | 2025-10-04 03:28:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3cb0400-edfe-3a39-992f-05578158b929 | -20.41666 | -44.13786 | 2025-10-04 03:28:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b5b57b7c-2d0c-34f7-bc55-60a51e779438 | -20.1322 | -43.99245 | 2025-10-04 03:28:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9d13dae3-adfc-3903-b819-4952a35e84ce | -19.7675 | -43.79155 | 2025-10-04 03:28:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 965def86-b152-34f1-b090-27740c80d4a7 | -20.22486 | -44.17285 | 2025-10-04 03:28:00 | NOAA-21 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a0a780f7-977c-3d2d-b14a-6d9f9b17bdbb | -21.55419 | -45.27323 | 2025-10-04 03:28:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| df188efc-9b7c-35b0-9bb2-ee955a1fb52b | -19.8153 | -46.0754 | 2025-10-04 03:28:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2db42101-2d17-3c9b-8228-37756c9c388f | -20.47372 | -44.81651 | 2025-10-04 03:28:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 6bc0e253-b98e-3804-a468-8df0f0f83c4e | -20.1412 | -46.41929 | 2025-10-04 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b2199041-d187-351b-92e6-d8780140f324 | -21.59509 | -45.279 | 2025-10-04 03:28:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9d000104-38f3-3ed4-bbe4-cfbbbf2389ce | -21.49174 | -43.89439 | 2025-10-04 03:28:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| df7e79e3-26a1-326d-a993-16490fb03933 | -20.12709 | -43.9896 | 2025-10-04 03:28:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2ef67b00-fabe-35bc-9467-75f7f28c1182 | -19.58036 | -48.0242 | 2025-10-04 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 68000519-b450-35f7-a79c-339f97750598 | -21.34494 | -44.99622 | 2025-10-04 03:28:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 191a12d1-8dfc-3d45-b993-04b59cc0a49b | -21.25928 | -45.18097 | 2025-10-04 03:28:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| be7aafee-1e0b-3e29-91e2-37041071cb3d | -22.76777 | -45.30595 | 2025-10-04 03:28:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 121330bb-b3a5-3df9-a466-6c84fb9b5ec7 | -22.07561 | -43.10451 | 2025-10-04 03:28:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b9b3b378-7a7d-3b8c-a88d-ef9bd3bc39e4 | -19.76871 | -43.78985 | 2025-10-04 03:28:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29a0b3b2-9ae5-3f9b-a5ad-a8ba7a212b7c | -19.91865 | -42.91724 | 2025-10-04 03:28:00 | NOAA-21 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 26e0e8d1-fc81-32d8-a8de-a39e8be2392f | -20.13663 | -46.42295 | 2025-10-04 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| fbdc7769-a5ec-34e4-a913-2d8e707e3d6a | -21.59955 | -45.28867 | 2025-10-04 03:28:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 87844557-2fb1-349c-95ba-1b7983607e58 | -19.51796 | -43.83176 | 2025-10-04 03:28:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac0892c2-c7d2-3a92-9cfc-b23de876bbff | -22.49125 | -44.07373 | 2025-10-04 03:28:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fe721e9d-51b1-30d4-a929-4762c5df8ee0 | -20.02998 | -44.06577 | 2025-10-04 03:28:00 | NOAA-21 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f06743ba-a095-34ce-bc45-272aca2ce1d4 | -22.07627 | -43.10138 | 2025-10-04 03:28:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 593fcc8b-b812-3fb3-b677-81fc151b8112 | -21.21499 | -45.82454 | 2025-10-04 03:28:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 148c84b5-8fcd-3f30-b36d-43a767156d47 | -21.1864 | -45.12724 | 2025-10-04 03:28:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 05a6c0ef-3d5a-34f5-b783-0d3d2c2c29b7 | -21.21387 | -45.8294 | 2025-10-04 03:28:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 49345d9f-4d89-35d9-868c-8582af88f2c8 | -21.49537 | -43.89572 | 2025-10-04 03:28:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4abb732e-121c-3327-91c4-c893d46d8c59 | -19.60086 | -44.62635 | 2025-10-04 03:28:00 | NOAA-21 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fb84323-c772-3a40-8153-d932e225b6fc | -21.27521 | -45.0577 | 2025-10-04 03:28:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 91aabf2b-ee40-34ba-9bca-f7523cb858ce | -21.59871 | -45.28966 | 2025-10-04 03:28:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e91fa714-4777-39fe-a6a7-5e7561f4e26d | -20.22513 | -44.17379 | 2025-10-04 03:28:00 | NOAA-21 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 3d634f9f-8b82-3a00-a72f-242e147d3386 | -20.47277 | -44.82076 | 2025-10-04 03:28:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| da0d29e9-c93b-345f-8a3e-ee47e0b75c26 | -22.76317 | -45.30025 | 2025-10-04 03:28:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README17.md)
