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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d3647e0-f81d-3818-a267-f5770d25c8a5 | -13.22663 | -43.97478 | 2024-12-06 04:29:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 85fa3070-e84e-3c7e-8756-e41f51f8f92d | -12.85758 | -51.93795 | 2024-12-06 04:29:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f89a71ae-6716-3cd8-9228-d1a5c7361c41 | -12.37274 | -47.33079 | 2024-12-06 04:29:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 309e3acc-2f66-3f7c-8b34-f7e54dfb080b | -12.24154 | -52.45906 | 2024-12-06 04:29:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 531c2ea8-f870-309b-9462-e067b5a8d9c2 | -12.32643 | -48.00196 | 2024-12-06 04:29:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f35684f1-99d1-3b68-b2cf-9d6d41f2b5ea | -11.32473 | -54.04567 | 2024-12-06 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bffdf08d-ae17-35c8-acff-568c7f504a31 | -11.69007 | -45.38346 | 2024-12-06 04:29:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 404fe539-41a1-3785-9466-61dc1c94aee1 | -13.62024 | -44.08878 | 2024-12-06 04:29:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d06b5564-f084-3aa7-b702-c3bf156a203c | -16.6809 | -43.88371 | 2024-12-06 04:29:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbeff224-e056-3cc5-bbef-8d9a77da2db6 | -12.48389 | -46.91506 | 2024-12-06 04:29:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92259956-4e7e-33e8-9055-98e1d40dff90 | -11.32832 | -54.05081 | 2024-12-06 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2d61258-25c7-3138-8151-38f7eae9aa20 | -16.68283 | -43.88281 | 2024-12-06 04:29:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ada7d1d5-bb82-3582-a7dc-3da18a3075c7 | -12.24455 | -52.46477 | 2024-12-06 04:29:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9dbc627-8e60-3c98-b4a2-dada66726cd2 | -13.61959 | -44.09341 | 2024-12-06 04:29:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 846a373c-fbff-3488-abe1-db835436abb6 | -17.09635 | -43.80341 | 2024-12-06 04:29:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3eeedb7d-b794-3077-8f48-d89c7b39c586 | -13.23042 | -43.97535 | 2024-12-06 04:29:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 712a91c3-9002-3ab6-ac22-e202e3af5291 | -12.45565 | -46.9436 | 2024-12-06 04:29:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6abc65c0-8ed4-3826-8215-9c5586743581 | -11.85831 | -44.78182 | 2024-12-06 04:29:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6766cf8b-3acf-325c-a2d0-23b2c6019023 | -11.73454 | -54.3133 | 2024-12-06 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 72cfc863-f8d6-307f-b9eb-e6ad58886bb0 | -12.63291 | -47.47373 | 2024-12-06 04:29:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 771225fe-e676-30d3-8dbc-b3fe8f8701a7 | -13.09634 | -43.37229 | 2024-12-06 04:29:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7317751-92d7-3dc6-83ef-7b77fd5d5c51 | -11.73012 | -54.31253 | 2024-12-06 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8efb51b8-c97d-380b-af76-827b00d9d70f | -12.24066 | -52.46408 | 2024-12-06 04:29:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af93c139-6a85-39cc-ad1e-abc85ffb599d | -13.4122 | -41.33119 | 2024-12-06 04:29:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d307802f-74cf-34a2-8a77-ce3097f351c0 | -15.8989 | -46.00447 | 2024-12-06 04:29:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b598b70b-62b2-3271-aad8-d35c4130c63d | -12.24543 | -52.45975 | 2024-12-06 04:29:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7312725-63ed-3cd6-90b8-e16a0832f723 | -12.86158 | -46.6863 | 2024-12-06 04:29:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 869ec448-1e41-30e3-925a-a268ff629edf | -17.77973 | -42.80796 | 2024-12-06 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65696021-056b-3ac1-a2ee-ed3a56b2df76 | -16.35142 | -43.69593 | 2024-12-06 04:29:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 831e7adb-f610-3919-ac56-89131716bde6 | -13.02483 | -43.75549 | 2024-12-06 04:29:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 006e2936-fa56-3ba8-8bf4-1a929537aa35 | -11.73091 | -54.30812 | 2024-12-06 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 88ffad77-53a2-3fe2-98f6-01c746750065 | -15.57134 | -47.85529 | 2024-12-06 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c7bf724-adec-3ab1-b5ef-4a3fcfda02e8 | -11.73534 | -54.30888 | 2024-12-06 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2863013d-3cc3-379d-9d9f-12543e66ac48 | -12.02281 | -43.00407 | 2024-12-06 04:29:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0872013d-2515-3e07-8f36-2e2b9307f8a9 | -19.72003 | -40.35396 | 2024-12-06 04:31:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 286ec9a5-27fd-38be-9f57-d7ba3c77ea4b | -21.35951 | -57.64818 | 2024-12-06 04:31:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 202731d8-3c77-3964-b720-9d4fdabe2ca5 | -18.97596 | -42.38829 | 2024-12-06 04:31:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ce9e019b-0c50-33e3-978c-69e611e00818 | -23.34027 | -46.7729 | 2024-12-06 04:31:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dc7bf2fc-fe41-333e-b5b9-c1f16089997a | -18.9771 | -42.37861 | 2024-12-06 04:31:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dfd43a33-8f41-3a86-84f2-2847eef73561 | -18.97652 | -42.38351 | 2024-12-06 04:31:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f13c2a14-257f-34c5-88ce-b19b9a3fa8de | -19.59323 | -40.45008 | 2024-12-06 04:31:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 640c383e-dec6-370b-90c0-84528db51251 | -20.00617 | -45.4059 | 2024-12-06 04:31:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d65c103-9bbb-3fe8-8348-a9540bb0a5e9 | -18.1463 | -47.80004 | 2024-12-06 04:31:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb9b28b5-44ac-3c33-bf9b-29ed37079efb | -20.76537 | -46.77065 | 2024-12-06 04:31:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0e3406d7-0dfd-3ee0-a8ae-a198a1485c78 | -17.98108 | -44.57449 | 2024-12-06 04:31:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc9b78e0-8c76-3541-bc8d-59a1d14f9200 | -25.43719 | -52.8772 | 2024-12-06 04:33:00 | NOAA-21 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bf375761-5926-39f9-b87d-2d3f8aa8053f | -28.72552 | -52.85064 | 2024-12-06 04:33:00 | NOAA-21 | ESPUMOSO | RIO GRANDE DO SUL | Brasil | 4307500 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fc3f10cb-7d58-35c4-b690-bd0a9953810b | -17.8578 | -40.1263 | 2024-12-06 04:40:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| 762e314a-9a78-30f3-96a1-3608ec7e4ed8 | 3.81667 | -60.42124 | 2024-12-06 04:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7fad0af-7c1a-352e-acec-80c349f05b25 | 3.82183 | -60.41643 | 2024-12-06 04:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 249e1325-b343-362a-b8ca-e2a74f5ec2c1 | 4.3258 | -60.79835 | 2024-12-06 04:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a810f60-19dc-3b8d-aa95-ca4c38dd6f97 | 4.32519 | -60.79406 | 2024-12-06 04:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dadfea73-3082-3cc2-8f7d-4e76eaa5c8be | 3.82699 | -60.41163 | 2024-12-06 04:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fc277ca-35e4-386d-b2ff-37c6feb94f3e | 3.8224 | -60.42038 | 2024-12-06 04:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c524485-b7cb-3eb9-8e1b-37612f1fde61 | 3.81781 | -60.42917 | 2024-12-06 04:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96c5d6ca-3619-391d-ac96-5fa9ff290c61 | 3.81724 | -60.42519 | 2024-12-06 04:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1130aa90-f83f-39e2-b8af-84e24169d6fa | -6.26694 | -46.91809 | 2024-12-06 04:50:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee83880e-02af-3668-8d6a-7cc296312b75 | -2.3636 | -53.91605 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96a5b067-5392-3fc8-8d73-640726cdb51a | -1.68979 | -52.78755 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b13ffc65-ad49-3455-8c45-c0eefba10ab9 | -2.56969 | -53.95899 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 915a809f-3528-3498-a466-abdbc6e85188 | -1.67269 | -52.5606 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61ba7a76-567c-3f8a-8990-dc4d6595f7a9 | -2.52322 | -54.04988 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22804acf-482a-3010-9873-3b5203692a0e | -1.67829 | -52.56869 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aea14a07-42a1-34ba-bc97-19e7f8d589b3 | -1.67158 | -52.56764 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cb0f639-5415-3a0a-9ce4-4be725880ef5 | -3.09424 | -54.06207 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69e025a6-dd66-3381-a327-08222130f799 | -2.68285 | -54.27112 | 2024-12-06 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88741d18-4f79-3bcb-b35c-ac9f1bd4449d | -6.92736 | -42.83294 | 2024-12-06 04:50:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47c59e0e-5a89-3461-a8cb-a5db304d3383 | -3.56345 | -54.64901 | 2024-12-06 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49d8095f-a2c5-3c52-b923-41bf39bfafb6 | -3.09197 | -54.05393 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b7f174c-03de-365a-a0a7-362e35afb4ae | -1.67507 | -52.74203 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15d46216-bb46-38ad-a65f-28dccd7f343e | -1.74536 | -52.80716 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b39c12aa-c8a2-3d18-ac4c-b8c1e922c7dd | 2.4786 | -60.69105 | 2024-12-06 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 820ea235-1964-3ea5-aa93-073bc3304757 | -1.67493 | -52.56816 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 94a576b4-d2bc-39c4-a1dd-f48ce9d88c50 | -1.95072 | -51.2021 | 2024-12-06 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9329bbdf-2ced-3c04-adda-bc21de2f8b32 | -3.8241 | -54.75822 | 2024-12-06 04:50:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66ff8952-0d59-3da0-a227-088ec1304214 | -1.33044 | -52.56116 | 2024-12-06 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12b38ba1-b0f5-3d78-9504-dda15c078f56 | -2.36767 | -53.9128 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16bca003-4e9a-32ab-bec1-b66f4cf18e5c | -1.53786 | -52.68377 | 2024-12-06 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ebafe05-3957-3428-9d58-2164ceee22a6 | -1.64444 | -52.26871 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23bc6e51-1198-3f97-9919-15b9feab8bcf | -3.0885 | -54.05339 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53e9444f-3371-38f1-b446-f87b13583854 | -1.67904 | -52.7827 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb424700-9b57-3d19-be4c-4f71a0d6f9d1 | 3.24027 | -61.03661 | 2024-12-06 04:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12e66c35-b642-33af-b95f-3c7e33eae4db | -1.89335 | -52.84802 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30f344a9-4679-3493-8453-5dd8569524f8 | -3.39942 | -42.30125 | 2024-12-06 04:50:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6cd9146d-01df-3160-978a-1fd828bb3029 | -3.26319 | -53.8713 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d382d1d3-6093-31c1-ae02-ae17a9b6ba3f | -1.53505 | -52.67971 | 2024-12-06 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e90b4b25-a3f8-38d7-9526-3d61fb863b97 | -1.81769 | -52.73104 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7c7669d-8bd2-38a7-beaf-c95fbc6462d8 | -2.75101 | -54.15868 | 2024-12-06 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44216c97-73c3-35e5-91fe-3e6f140a2eab | -3.10466 | -54.06369 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 798a0274-719b-3842-bca7-2ec114434a54 | -1.68809 | -52.79821 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05776df9-02e5-3d2b-97c2-490f415373bb | -6.46086 | -46.34255 | 2024-12-06 04:50:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42f4943d-2a3b-31ce-ad26-e06f424b3e91 | 2.62415 | -60.41282 | 2024-12-06 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6419a847-a5db-3b1e-ae14-7388f33e4d8f | -1.53897 | -52.6767 | 2024-12-06 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15ef9539-8a0f-33a4-bb96-213fa66635b4 | -1.89728 | -52.84499 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea805020-ffc7-394b-a180-001a71b9ad18 | -7.22712 | -39.96257 | 2024-12-06 04:50:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3e836f50-f294-33a4-a56b-f0512835f433 | -3.22953 | -42.42884 | 2024-12-06 04:50:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6974b38-8392-3bd3-8fbb-a41abe00ad70 | -3.11057 | -54.06008 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a10bda39-ecd5-319e-9bb2-759a4dd9da4f | -2.13922 | -51.23494 | 2024-12-06 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 481ff34b-5706-3613-945a-0ca427d1252e | 2.42411 | -60.6506 | 2024-12-06 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45ed5f7f-b758-39e3-9442-789e6b21ae93 | -2.28808 | -53.78773 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
