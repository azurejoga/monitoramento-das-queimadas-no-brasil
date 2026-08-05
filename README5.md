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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 936bbeb9-290e-3be0-888f-fed3387467aa | -11.19 | -54.89 | 2026-08-05 02:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1ebd0fd-eafd-3d86-9586-f0366d0fbc65 | -7.5068 | -49.7394 | 2026-08-05 02:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 108d2c15-a61f-3941-9bf0-14864879bede | -6.5514 | -55.1569 | 2026-08-05 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6ff5ddae-564d-3e2c-b5c0-1f9d03e53048 | -12.5947 | -46.9301 | 2026-08-05 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 39c0edd2-92cd-3c19-a373-f29bb5b29337 | -13.4488 | -43.6698 | 2026-08-05 02:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 8c71b225-8efc-3dd7-9d43-051139748842 | -12.5947 | -46.9301 | 2026-08-05 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 256bf5c8-fc28-322b-a9f7-8f3d43a73611 | -6.5514 | -55.1569 | 2026-08-05 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f4ca7606-3abb-326e-a5b4-4e570222ab2b | -13.4488 | -43.6698 | 2026-08-05 02:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6cd7c5f2-b5ef-313b-945a-e0b5a068c976 | -7.5068 | -49.7394 | 2026-08-05 02:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 9b7b5bc6-366e-371f-99ad-0ff2f66aad90 | -12.5942 | -46.9527 | 2026-08-05 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| e44d021c-b437-35f7-8b41-7fd6b28810f2 | -12.5947 | -46.9301 | 2026-08-05 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| b8f6e4a4-0e94-3e5a-bb50-e75a7e0a5b6e | -7.5068 | -49.7394 | 2026-08-05 02:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 0905396d-a8d3-344e-8a85-96ff17b9c936 | -13.4488 | -43.6698 | 2026-08-05 02:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 9f118214-249d-313e-89b9-3d76cec1a21c | -6.5514 | -55.1569 | 2026-08-05 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| ff0685d2-1463-39c7-956e-f23cf0078041 | -7.5068 | -49.7394 | 2026-08-05 02:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| fd7544f0-1459-36ed-92b2-947cbebdd7a5 | -12.5947 | -46.9301 | 2026-08-05 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7782eaf5-4773-3c18-ae7a-526f30462993 | -6.5514 | -55.1569 | 2026-08-05 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 041d7bc7-0e8d-309a-8d52-5a2502d5927c | -12.5947 | -46.9301 | 2026-08-05 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9bd1d189-d326-35e2-a92b-01a137a77b22 | -13.4488 | -43.6698 | 2026-08-05 03:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 9d906cb0-05c3-37b2-8814-e503c8c24204 | -7.5068 | -49.7394 | 2026-08-05 03:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 42572f6c-6151-38b1-bf5f-4e7e39706b82 | -12.82348 | -38.43777 | 2026-08-05 03:06:00 | NOAA-21 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| dcd51434-e495-3f89-822a-7856920415c2 | -12.82764 | -38.43565 | 2026-08-05 03:06:00 | NOAA-21 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 51dfd2d2-3b9a-3ef3-b705-e20a807d4bcb | -9.48109 | -40.37239 | 2026-08-05 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8d4aa34b-6770-3432-8b3e-b36a44d69a83 | -15.14124 | -42.15852 | 2026-08-05 03:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fcdf043c-d920-343d-87b2-46efd9c339b5 | -18.89043 | -43.34489 | 2026-08-05 03:08:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7682c8a5-876f-3723-88b5-5d2b32dec9f4 | -17.33615 | -42.62952 | 2026-08-05 03:08:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2fc7d777-4429-3e98-8965-71671a8b3ddc | -15.43871 | -41.37978 | 2026-08-05 03:08:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4b33587c-a585-3277-9de6-fd22fba02d50 | -17.33294 | -42.63305 | 2026-08-05 03:08:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5553984e-5f90-3865-b7ca-0b62248fd583 | -17.33988 | -42.63482 | 2026-08-05 03:08:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8ee68f57-1a0e-3f7b-aa7f-b2d95a7df679 | -17.33449 | -42.63672 | 2026-08-05 03:08:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ff31e6ea-0fa3-3b42-af31-173c0deeb96c | -18.35374 | -39.79654 | 2026-08-05 03:08:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a317e59c-355a-3e3c-975a-6499457bdb9e | -15.44536 | -41.38169 | 2026-08-05 03:08:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 28e9c4fa-efc8-3025-81a1-deef010d1841 | -15.44404 | -41.38039 | 2026-08-05 03:08:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 696f7978-299a-3965-85f5-ebf236769f35 | -18.35276 | -39.80102 | 2026-08-05 03:08:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| de80f272-4509-3614-bb0a-b2b96fb8c6db | -15.45065 | -41.38256 | 2026-08-05 03:08:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8466e693-4cfc-3bbd-9ec0-4758185973e9 | -7.5068 | -49.7394 | 2026-08-05 03:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 92fc7cac-3776-3a73-9b82-f43cf5463edc | -12.5947 | -46.9301 | 2026-08-05 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 451b107a-047b-3fec-b9d8-02bef3e3a921 | -22.77094 | -43.46382 | 2026-08-05 03:10:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 02b7033c-d8d3-3a8b-aa14-56b080cf4b3a | -20.88774 | -42.78386 | 2026-08-05 03:10:00 | NOAA-21 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 900f92b0-3e9a-3549-9927-5d73341a7f25 | -12.5947 | -46.9301 | 2026-08-05 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 431a5a07-8e9a-3440-810d-10ab20ac3929 | -13.4488 | -43.6698 | 2026-08-05 03:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| c3027b76-6c91-3663-a639-be7d6664c416 | -14.0294 | -54.0769 | 2026-08-05 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 5f815cea-313d-373d-8bea-56c3b272e0a0 | -7.5068 | -49.7394 | 2026-08-05 03:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 76b513f9-cf28-36fd-8589-db1f9e0e0a00 | -7.5068 | -49.7394 | 2026-08-05 03:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| fa63b841-39ca-30e0-a3e1-b766fd0a4f9c | -12.5947 | -46.9301 | 2026-08-05 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 392cb0f2-3514-39f7-a7c8-3e38470189b4 | -12.5947 | -46.9301 | 2026-08-05 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 18d2c6cf-2797-3348-a87b-82518595064e | -6.64624 | -43.90857 | 2026-08-05 03:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 09490a54-71bd-3fb6-a999-de251aeaae58 | -6.93564 | -41.92828 | 2026-08-05 03:40:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f0bdb26-df71-3704-adae-58df36d48d67 | -4.39121 | -40.43335 | 2026-08-05 03:40:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c9716014-a0fe-3604-bf8c-b160acce2d79 | -5.33053 | -37.3167 | 2026-08-05 03:40:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 14349696-7f06-35e2-a37f-eba92a742ebc | -6.65252 | -43.90969 | 2026-08-05 03:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14b87d36-1f7d-37e4-baa9-70a652da33d1 | -6.89268 | -42.41769 | 2026-08-05 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ed5a8f2d-7a68-39e8-94a0-d3f1617741d2 | -6.48058 | -42.22436 | 2026-08-05 03:40:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 319b3f0e-0bfd-30c3-9cfa-3fdb822fd69e | -6.65159 | -43.91475 | 2026-08-05 03:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd9f2f8f-fa8a-3c44-977d-20a7d78479cb | -3.0241 | -39.97223 | 2026-08-05 03:40:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7fa1f172-edcf-3295-bcf0-8c5586368c30 | -6.41729 | -39.3456 | 2026-08-05 03:40:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 431332c4-6a30-3cea-bedb-a1d69adfbcd5 | -6.89762 | -42.42284 | 2026-08-05 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| fa93b5ff-f8b9-3ee0-8f06-52449f69d606 | -6.50052 | -44.70332 | 2026-08-05 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 431a836e-ff54-3012-b785-513d2601fc7d | -6.93608 | -41.92967 | 2026-08-05 03:40:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 183080bf-1feb-341e-8fab-2d35b581b068 | -4.39597 | -40.4357 | 2026-08-05 03:40:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 79805d0f-e338-3a9d-81ab-0b4781d59b5a | -6.89835 | -42.4188 | 2026-08-05 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 2c4f16be-8e8b-345b-97df-a88049e3ab63 | -6.50538 | -44.70259 | 2026-08-05 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 111a738c-97a4-320d-b38c-bfdd02c117b0 | -4.3965 | -40.43254 | 2026-08-05 03:40:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8d8c9389-fb85-3732-b0c8-ce621c60c5ee | -6.41929 | -39.348 | 2026-08-05 03:40:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e9e98cd8-12b2-30a8-a0f3-2a70d2501cfc | -4.37789 | -43.39158 | 2026-08-05 03:40:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 374d065f-ee7d-3efb-98ff-937b74278115 | -6.30192 | -43.62606 | 2026-08-05 03:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc589dfb-cb66-3bdc-b2b8-3d2e170d4c38 | -7.48102 | -36.61842 | 2026-08-05 03:40:00 | NPP-375D | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cb0a166b-c6b5-3631-96a8-6fc4da821cac | -6.93065 | -41.92821 | 2026-08-05 03:40:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f60b2bd-e7ed-3e00-9b04-21506278ccc6 | -6.92955 | -41.93047 | 2026-08-05 03:40:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ff56054b-983d-39e1-8737-ac939c42aecc | -6.89908 | -42.41477 | 2026-08-05 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8e06545a-27e0-3117-ab50-ec031226c612 | -6.64535 | -43.91345 | 2026-08-05 03:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9320ca38-fa70-3047-bc4a-b44d9581bb0d | -4.39641 | -40.43422 | 2026-08-05 03:40:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 390f3fd3-dcb1-3740-9b65-199bcf837e39 | -6.8934 | -42.41371 | 2026-08-05 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 00391de6-0bcb-3f7b-97e0-97cdf6e89dc3 | -7.18137 | -40.17191 | 2026-08-05 03:40:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 0b05101a-f1b9-36f4-bef0-9f308d913891 | -3.02461 | -39.96916 | 2026-08-05 03:40:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9e1d4e06-3db9-3139-af70-52fe137c27d4 | -6.50703 | -44.70496 | 2026-08-05 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9998733d-e49a-3ebb-8e05-b4507dd220fa | -7.17649 | -40.1711 | 2026-08-05 03:40:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c38801c1-7147-35d7-b7ec-0ca738e158e3 | -6.47423 | -42.22719 | 2026-08-05 03:40:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 67180399-7309-3d1d-9a99-236df6895a50 | -6.90474 | -42.41593 | 2026-08-05 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 37b3901c-38ee-3baf-a981-bad68b1a78f0 | -6.89196 | -42.42169 | 2026-08-05 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e1715d65-b37f-3359-a635-e6f98b1c5aa7 | -6.30276 | -43.62137 | 2026-08-05 03:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6aa3e9b5-b1df-3710-8e6b-340873f193e5 | -6.50428 | -44.70837 | 2026-08-05 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d4c8c8c-9011-38ab-97fc-070ec9df83cb | -6.41646 | -39.35049 | 2026-08-05 03:40:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0a0a683c-d961-3ab4-9c69-346cd9646201 | -6.9005 | -42.40694 | 2026-08-05 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4bd27307-c344-316d-9446-8cd802317e12 | -6.89979 | -42.41082 | 2026-08-05 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e8b2bead-65ce-3c75-911f-df6286226b1a | -7.18041 | -40.17733 | 2026-08-05 03:40:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 31bc2bb3-fc32-3d82-aed4-9f43a244751a | -4.98129 | -37.23695 | 2026-08-05 03:40:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 554cbc50-b6b7-376d-a3fd-9c76a22e65ec | -6.4799 | -42.22808 | 2026-08-05 03:40:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a957da26-f1b4-3879-90a3-a6707a339ad2 | -12.58769 | -46.93895 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bc56207b-d66d-3a26-a549-29d6a9df581b | -9.47967 | -40.37211 | 2026-08-05 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ed57ac2b-1995-3ff6-9e07-6492f2ad0a4d | -8.34521 | -45.98433 | 2026-08-05 03:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02bff262-65e3-30ec-8685-8cfc5621f79d | -12.59738 | -46.92324 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54a5cf75-c9d9-3a35-906a-b35319bb48fd | -9.48544 | -40.36975 | 2026-08-05 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c694509a-777e-3f41-956e-664a26f1d8e6 | -12.58698 | -46.93909 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 380c2339-c5fa-3b86-8b80-76944de5eb4b | -11.52299 | -43.25055 | 2026-08-05 03:42:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 07c19814-2271-394d-bb63-aae9ab9de319 | -7.22537 | -43.3504 | 2026-08-05 03:42:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d0e0e39-eef5-33f5-bbfa-5bc62b36def0 | -7.22034 | -43.35441 | 2026-08-05 03:42:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a4ec60e0-317f-37a2-8e76-54115bff76fd | -12.59255 | -46.91655 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d50cb69-27ef-31eb-a696-964b08477b68 | -11.55581 | -47.70819 | 2026-08-05 03:42:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca41562a-54ce-3328-ae94-b8cfde946e55 | -7.6292 | -45.31823 | 2026-08-05 03:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README6.md)
