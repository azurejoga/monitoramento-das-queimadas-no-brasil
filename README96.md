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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b70bc175-e34d-3759-983b-5512528e0068 | -19.65812 | -44.1751 | 2025-10-04 04:17:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae496ccc-1ea6-353a-899a-aa19731b7b9e | -16.01785 | -50.94224 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2856a1f-3e1f-3a9f-b970-046430e6ad01 | -18.7283 | -41.61639 | 2025-10-04 04:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 899543d3-f7ee-344d-9e2e-1421508c3a88 | -18.59548 | -51.17456 | 2025-10-04 04:17:00 | NOAA-20 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11025d26-f90e-3ba7-aaa7-dab06b137cf5 | -15.34708 | -47.82545 | 2025-10-04 04:17:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43342f78-f4da-386e-97eb-fd6dd7269bbc | -15.58998 | -52.46363 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb8e0fd0-a229-3935-a0dd-69f8db66fd94 | -20.71805 | -49.61231 | 2025-10-04 04:17:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8866a648-6abf-3e8e-98f3-756dfe79aea5 | -20.10738 | -44.63312 | 2025-10-04 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffecd0d5-b872-35a5-9503-c510bc9b4351 | -17.63343 | -44.44843 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56d668c0-28e1-3210-94bb-c3c4e89abc2e | -14.93727 | -49.98378 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9f6338b-9efe-3cca-9766-276ff41f793f | -21.68787 | -50.06208 | 2025-10-04 04:17:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 594d5e4b-42c5-3046-939d-3dd2e07317bf | -15.73603 | -46.26892 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e41e583-8ce9-3c7d-8e23-a112d91131a1 | -20.94453 | -45.81368 | 2025-10-04 04:17:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55c77864-24af-35e0-a058-ab708550cb51 | -15.60762 | -46.93568 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 787b9929-bd43-3ff8-84f8-1500f577e703 | -19.49799 | -43.62558 | 2025-10-04 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fb4e235-efde-367b-9019-6a21736fa5cb | -17.07908 | -46.24815 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3d8e754-1eb9-3395-a782-beddccc4fcb1 | -16.34066 | -47.10926 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e57ea3b-4115-395c-87ee-9bcc99402b89 | -22.28464 | -46.75587 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 118b966d-b5cd-3622-b8cc-4d74ce29c8cd | -18.46255 | -49.44384 | 2025-10-04 04:17:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d55b14ea-bd7f-33aa-93a7-70110fa17da2 | -17.58543 | -44.49337 | 2025-10-04 04:17:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f75c6d8a-8435-35a6-80aa-d18c0f1310e4 | -15.24541 | -48.18601 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ae53456-43b3-348c-bd74-57ad89307366 | -19.97447 | -43.70411 | 2025-10-04 04:17:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6dbf1293-58a6-35c8-b7a8-4bf8dc7b7837 | -16.38935 | -52.16467 | 2025-10-04 04:17:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6d6ce1cc-94ae-32ed-bebc-16fbb3dce073 | -15.2636 | -49.32971 | 2025-10-04 04:17:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9ebb8b3-8b1f-3997-a13b-a6c0bcd55dcd | -18.71369 | -45.1669 | 2025-10-04 04:17:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70357fb9-76e5-37b0-850e-aef6e757e3b3 | -15.33418 | -47.33738 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4c87ce1-0cc5-34f4-9295-a13d777d6540 | -22.28133 | -46.75526 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 099382be-0bf0-3ce3-93a5-b049f18b0981 | -15.33832 | -47.33389 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cae4601-e777-3ac6-be14-273ce3b42a95 | -17.15831 | -47.02889 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd1f4645-7e24-318f-a720-b6e139fca9bd | -19.69816 | -44.44637 | 2025-10-04 04:17:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 604140e2-585c-31cb-9133-3a7a62ad9d01 | -14.58188 | -52.49265 | 2025-10-04 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1dbbe67d-5cdb-3af2-b095-3064a486a501 | -19.72902 | -44.45487 | 2025-10-04 04:17:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dafa8f0-f116-3f19-98b6-2d6a1d72bb46 | -17.15893 | -47.02512 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ccb44dc-5ca5-317c-9d86-a308187b5242 | -20.22431 | -44.17493 | 2025-10-04 04:17:00 | NOAA-20 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| e0967365-4f43-3e90-9a6d-3f7c98ba6973 | -18.17118 | -53.3465 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6f10f056-db6c-385d-8f28-51d6ab700070 | -16.02136 | -50.84357 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 988e2d8a-8cf1-3f84-9cba-6628663d6a49 | -19.97739 | -43.70857 | 2025-10-04 04:17:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 24fdfb1f-41b3-379e-bb27-4b9648d01149 | -21.59271 | -45.27666 | 2025-10-04 04:17:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 68c38d8b-e264-3da7-adc6-4c7b6bf41c29 | -16.04404 | -51.00973 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4685bbc-fed5-3761-b7eb-0284266e180a | -15.52918 | -46.83666 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f0e64f97-0c98-3177-a36d-121e8b75d34f | -17.95929 | -44.26393 | 2025-10-04 04:17:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 160a2038-dfe4-3741-8afa-a451c25a20b5 | -15.6658 | -48.14585 | 2025-10-04 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22ee0694-85ab-3e07-8142-8b9b935a4b61 | -18.63627 | -48.46183 | 2025-10-04 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 005b33b0-d094-3f50-871c-2e18a90fb22f | -17.15768 | -47.03268 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b61da069-4615-36c9-a199-e803e5b640ad | -21.93519 | -46.6016 | 2025-10-04 04:17:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eef83fb7-698f-332c-bc99-203a3ed45f75 | -21.02213 | -45.94867 | 2025-10-04 04:17:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0c6e9bff-952a-3366-b9d0-2488db7acc8c | -14.93264 | -49.98663 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7535992a-a747-321e-8ad3-5a4e7ac44beb | -14.9827 | -49.97039 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 70cad7e1-933b-323b-a465-836e03a83372 | -15.60273 | -52.48864 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 63796150-a90f-3629-a5b4-e33aa1180f34 | -18.4557 | -49.44442 | 2025-10-04 04:17:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15bb43a2-5ba1-3c26-a162-8d2904bda97f | -21.93578 | -46.59789 | 2025-10-04 04:17:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 66c1a51f-0ffc-34a0-83ed-41db55dc8ded | -19.24641 | -45.99448 | 2025-10-04 04:17:00 | NOAA-20 | MATUTINA | MINAS GERAIS | Brasil | 3141207 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17a9b309-78c7-3159-b32a-644c8e55329b | -20.716 | -49.6099 | 2025-10-04 04:17:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a993f28-8ff2-3072-a9b6-f64bcd435674 | -21.6959 | -50.05907 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 02d77fdb-4ce8-346f-a1ed-c6c83dd7d0d9 | -15.68915 | -46.26848 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6f4ec924-4322-3bb5-ac5e-f7ad5c17de13 | -19.58357 | -45.90252 | 2025-10-04 04:17:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e515e20-f55e-3a79-bf6a-5a62acc664ee | -15.60373 | -52.48354 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ed1b3f2b-bc37-3db1-8254-b9acad497f0f | -17.04709 | -46.959 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20049882-6fdd-3db1-a41a-511d2fca8c95 | -15.3363 | -47.3372 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cc85017-e5e1-3966-921e-e776247c6209 | -18.46304 | -49.44579 | 2025-10-04 04:17:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5ccff16-5c68-3bd1-8d86-dbe4cf4ccde9 | -20.59018 | -42.09372 | 2025-10-04 04:17:00 | NOAA-20 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 40a72e90-024b-358e-9631-a56353d8d432 | -15.7287 | -46.27924 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1e59dd3-dd6e-3d2f-9643-0f85de2386ca | -21.27608 | -45.05641 | 2025-10-04 04:17:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1a31f71c-ce26-32c6-a2b9-3016411bcca4 | -16.75308 | -43.96226 | 2025-10-04 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9c55fe6-2502-351b-a38c-51730a6696e6 | -16.01314 | -50.92153 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4eb1a144-e7a5-3ca2-913d-8b5d96d69424 | -16.02276 | -50.84764 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5dcc6a8f-9a73-31d8-9419-faee4cd7fbfb | -20.72086 | -49.61747 | 2025-10-04 04:17:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d25d5946-09e1-3865-8195-f1fe9858caa5 | -21.58935 | -45.2761 | 2025-10-04 04:17:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5402cc63-fc4d-39c1-85ce-b7f5204fe5bb | -21.69873 | -50.06428 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0d882c4c-61e0-31ae-9eee-5885ccc74b29 | -15.12878 | -48.49208 | 2025-10-04 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 360acffb-a2d3-3464-abed-f73d5688dbda | -15.95863 | -43.32965 | 2025-10-04 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e03c4c9-8581-3d50-b0e4-26326107d42f | -21.49396 | -43.89706 | 2025-10-04 04:17:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cfa5f8f4-c336-32f6-b7ce-e6f433f09253 | -17.58154 | -44.4964 | 2025-10-04 04:17:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b89b6a1-4ea9-35ef-97c4-21a2b9f7f22c | -17.55662 | -46.76071 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8da4493-ff05-3dde-a7c1-05aa226d4d27 | -16.35555 | -49.40157 | 2025-10-04 04:17:00 | NOAA-20 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d4c5287d-ec8f-3582-98b9-f57b4b38b0fd | -16.06375 | -50.90335 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 159bbb8c-e3ed-32d3-8210-9d27160b1bb7 | -21.78359 | -45.3353 | 2025-10-04 04:17:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8d6a4097-4072-335b-bac8-d22940ea4543 | -17.58488 | -44.49701 | 2025-10-04 04:17:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66af4e39-1be2-3c74-8c0f-68eb1cbc427b | -17.69946 | -47.08873 | 2025-10-04 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ce3d8de1-ef0e-3bbe-95b6-11b3117a7137 | -18.17928 | -53.35449 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 101892e6-3b7a-3fec-b863-90f87cd1e970 | -19.70656 | -44.13091 | 2025-10-04 04:17:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53f3a00f-54d2-348c-bfd3-40d7e3ade77c | -16.08519 | -51.06817 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b516fd5f-7c16-36ae-9155-6ce4349fadf0 | -21.34024 | -44.99692 | 2025-10-04 04:17:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 374dad11-8020-3c02-bc6a-c7bd0915d44a | -18.97777 | -46.97184 | 2025-10-04 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75a0d181-5aaa-3150-9602-ed7b428fe9b2 | -17.29742 | -49.27317 | 2025-10-04 04:17:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c8c7861-83c1-3b38-8123-9317838b7aa0 | -17.99264 | -51.63534 | 2025-10-04 04:17:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6717528a-f0a0-3ce3-a11b-e7f7e38e0d89 | -22.28777 | -46.71436 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 464061b3-46fb-34a4-ab14-fa432b187bfb | -21.84314 | -41.37271 | 2025-10-04 04:17:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fbbd2247-82ae-3093-93be-368aab9bb210 | -15.35957 | -47.96273 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae40a771-a861-3072-97ae-80c54dcc4531 | -16.7587 | -43.97078 | 2025-10-04 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a697fd4-4290-331e-b4ff-a8586f0c382b | -15.73146 | -46.27581 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 57397338-c132-3b34-853b-a934ab041285 | -21.59829 | -45.28537 | 2025-10-04 04:17:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 03e041a8-4519-3da8-bc2a-04110f23b6bd | -15.58014 | -46.9112 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68427157-af2d-3018-b41a-ae1bda296065 | -21.93246 | -46.59729 | 2025-10-04 04:17:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 924e8c37-0ccc-30a1-b75b-0cdf8a3b4667 | -21.08786 | -47.76452 | 2025-10-04 04:17:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2b3b8c99-2255-35d6-babf-3fec427816ac | -15.61594 | -46.94901 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f838482-f5a5-38b5-8a64-03a4b15d5458 | -19.51947 | -43.83209 | 2025-10-04 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4bc9d08-6937-3ee5-aa91-fa702d256075 | -18.63857 | -43.88286 | 2025-10-04 04:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ef5c596-9308-3bc3-9207-3d4abb11c24b | -21.32144 | -46.70237 | 2025-10-04 04:17:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 803a6ea1-eb17-38c8-9b96-d3e4877da023 | -15.2454 | -56.77273 | 2025-10-04 04:17:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README97.md)
