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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d68d2d7f-afc9-3db3-b300-098f11e9fdc6 | -8.2227 | -44.91957 | 2025-07-15 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2601201-bc1d-3e99-aa3a-633770c20f7e | -7.30232 | -46.26014 | 2025-07-15 04:10:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f22d85f-b3b3-352d-8e89-e86b8ab04e74 | -7.15706 | -43.1536 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 148845bc-de92-3a14-8c2d-086c0d22179f | -11.44326 | -45.1296 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 36b7f0f6-5880-300f-a610-4e0cbb8787f2 | -6.29593 | -44.23559 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 921be810-476c-3610-923f-677a11bb962c | -7.15251 | -43.16031 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3cf16965-7adc-30ce-9b5e-68f3041515ac | -6.80418 | -44.93665 | 2025-07-15 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cda9972-4526-3ed2-8e3d-e61152657c81 | -6.38727 | -43.72087 | 2025-07-15 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46ca295c-0d6e-38aa-ac25-37effed2c5d0 | -8.60538 | -47.43727 | 2025-07-15 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77a005a4-3395-3fc1-96bb-bae84cc42458 | -7.3052 | -45.35825 | 2025-07-15 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b54be06-b878-3871-b318-0f6cafbc06ad | -7.28244 | -44.03413 | 2025-07-15 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6366cefd-e85d-3871-8a1f-c762078ee2d1 | -13.65142 | -45.73381 | 2025-07-15 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c14dc171-962d-3b25-830e-e4b573bc3c98 | -13.04647 | -47.81638 | 2025-07-15 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dfab10d-7135-3ec9-b9d5-c864b9cfbf49 | -7.28593 | -44.03468 | 2025-07-15 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8e6c5f9-bd4b-32a1-b806-fcff17d3bc19 | -7.21298 | -45.33149 | 2025-07-15 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2504ca43-54f1-3da5-b685-95853e1fc15a | -8.68341 | -51.45914 | 2025-07-15 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e28da9d7-ed70-3463-87d5-a277bc989e2f | -13.65561 | -45.73041 | 2025-07-15 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 287e5a7a-bb42-3314-a0df-4f9f8fc5ff3f | -7.88976 | -44.49052 | 2025-07-15 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a96058c4-ab49-3ce5-b3cf-70aa8e0ee114 | -11.5253 | -48.96192 | 2025-07-15 04:10:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7db0647-4478-398e-8dfd-6d45148f4fb0 | -8.2263 | -44.92015 | 2025-07-15 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a96daf2-f7a0-3215-9f09-93814daa4c52 | -9.80384 | -47.74395 | 2025-07-15 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3cb8943d-d064-3af2-a274-c84d27d2647c | -6.36453 | -44.74768 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b89823cf-c92e-3a1b-986a-1005d6803ca6 | -11.4527 | -45.09478 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 45cdbe05-147f-36ee-9ca4-fa7d76d2e97f | -9.79558 | -47.74241 | 2025-07-15 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc55230f-9c91-39b3-915a-c4b06c3ad525 | -6.87799 | -50.2674 | 2025-07-15 04:10:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2916fd7-9e60-32cf-a284-7dc505e05894 | -7.09165 | -49.1788 | 2025-07-15 04:10:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61fe9587-b254-3b98-82c9-eccff8716c05 | -10.64401 | -45.22303 | 2025-07-15 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f794a4e0-a28b-38da-868f-8923797ddaf4 | -13.1079 | -47.28006 | 2025-07-15 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98b29047-66df-3836-b825-2fbcd5c05489 | -10.64912 | -46.62973 | 2025-07-15 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3859cdb-331f-3e2d-b9df-60b1a532a859 | -8.21911 | -44.91901 | 2025-07-15 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a38ea8b9-43c3-33e5-b41f-13b67da98e58 | -7.89263 | -44.49508 | 2025-07-15 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7534fcb5-67cc-3db9-a3dd-3f8c9c9dd15b | -9.49188 | -40.38614 | 2025-07-15 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6dea82bb-025d-39ee-8b3f-7d7699113d37 | -7.20927 | -45.33083 | 2025-07-15 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbe7beca-8a82-3326-b6d7-c9d16b61b573 | -12.34651 | -49.30806 | 2025-07-15 04:10:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70285483-c0d4-37ba-a122-9016de37d3dd | -13.03947 | -47.80991 | 2025-07-15 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8104beb-1778-3918-9c02-a7891b213d9d | -11.46962 | -47.31311 | 2025-07-15 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a151e92f-a87a-3096-872e-df03c150c47d | -6.38318 | -43.72412 | 2025-07-15 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb2a4d00-41ee-33ac-b577-650aeafc70e3 | -11.73068 | -47.05317 | 2025-07-15 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2009e7d8-5470-3558-8121-a54a92b93438 | -6.88945 | -47.02849 | 2025-07-15 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ad702c3-5f03-362c-9471-e543066f22e5 | -6.70524 | -47.8034 | 2025-07-15 04:10:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ad6a543-4537-397b-b623-dccc4a0f88d0 | -8.60124 | -47.43652 | 2025-07-15 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da197982-c3ac-3e13-bb85-65a44d2584f2 | -7.30817 | -45.36333 | 2025-07-15 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdbe808b-6718-3dd6-9562-9d7e202aa9f0 | -7.92667 | -42.88943 | 2025-07-15 04:10:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9632b843-3a06-34cd-94a0-70d6229814e9 | -10.56908 | -49.13934 | 2025-07-15 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 521d519b-0c76-38a9-be41-db492033c297 | -7.15963 | -42.96529 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 24e715c2-2e88-34ec-9eda-360d0d9633a5 | -7.64504 | -44.41914 | 2025-07-15 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0784baa-c4c2-3b43-942e-d0cc40aab20e | -12.46559 | -46.91643 | 2025-07-15 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60a14106-4762-36b5-b8e5-c97a1a0616b4 | -7.163 | -42.96584 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b021dbe7-cd34-36d8-a827-7f3582b04900 | -11.45837 | -45.10383 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 38b3776a-bccb-3365-a589-32d26110f436 | -6.29239 | -44.23498 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cee9c97e-fbbc-3e49-aa62-d0f51ea5246b | -7.99029 | -43.38314 | 2025-07-15 04:10:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 68246469-0613-3b97-b6af-19a74204de04 | -10.96736 | -49.25228 | 2025-07-15 04:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0bf94b1-d5ee-3e00-a930-59fcfdc37a95 | -9.49531 | -40.38666 | 2025-07-15 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c867249c-510f-3d57-8447-aae782dd5245 | -13.65979 | -45.72699 | 2025-07-15 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2720dc9b-e0f2-3873-a11d-bfc76cdfbb1a | -7.09642 | -49.17965 | 2025-07-15 04:10:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54961291-adf1-319a-b425-64928e0b5636 | -10.49883 | -53.57978 | 2025-07-15 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dd51478-bbec-3816-b9e0-d7df9b87b247 | -8.90714 | -47.34764 | 2025-07-15 04:10:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd7685c4-1390-308d-a470-010e7255c930 | -7.091 | -44.38755 | 2025-07-15 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15685baa-76ca-36f9-a90a-c20c408a5296 | -8.25905 | -46.36071 | 2025-07-15 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 657a77be-c11e-3111-93ae-073c4ba1673f | -7.09389 | -44.39223 | 2025-07-15 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fab7252-ed2d-3155-a17c-a02d4e4fe88c | -6.72762 | -44.33427 | 2025-07-15 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fe98223-fda6-380b-8c55-87b8c094d591 | -11.46187 | -45.10444 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 34eb336f-ff27-318f-910c-30af5765b535 | -10.86031 | -54.05603 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a4318de-c51e-3007-8f60-a0f7a465e5b2 | -10.69652 | -48.30121 | 2025-07-15 04:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b111fb5b-e80c-321d-bde2-732a26befa7a | -10.86644 | -54.05728 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ba220bf-5b80-3a70-8eb0-a2137b7cf1a0 | -9.40378 | -40.52836 | 2025-07-15 04:10:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ad72ce34-5915-39bf-b31e-6c22981c986e | -7.64086 | -44.4225 | 2025-07-15 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69387b87-1516-3525-9245-931cc3a2c4a3 | -7.14971 | -43.15613 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9d0fb9ff-545b-3733-8b09-638883252e45 | -12.69492 | -47.86991 | 2025-07-15 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0e3d354-c20a-38f9-925c-c1d77370b9c8 | -7.09973 | -43.50967 | 2025-07-15 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cdc9a9f-2960-3f1b-b512-5c57cf93ff29 | -6.72408 | -44.33369 | 2025-07-15 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d32298b-92ed-3fa9-b214-51e56e4f85bb | -9.4424 | -40.32172 | 2025-07-15 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b4dc640b-3a7f-3d47-9998-ef97fcef26e2 | -6.44032 | -43.81195 | 2025-07-15 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e464d6c5-907d-30eb-9d84-49f94a8d1390 | -10.96289 | -49.25134 | 2025-07-15 04:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb49ce04-1822-380f-9c28-85aa902f1390 | -6.91635 | -52.85553 | 2025-07-15 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9871dbdb-ef33-31e3-bd21-cb20092535c1 | -10.277 | -47.61292 | 2025-07-15 04:10:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0540cd1a-2df7-33b9-aaea-c6e0621ed401 | -8.81504 | -48.43672 | 2025-07-15 04:10:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f4f7af9-c587-3971-ad31-4c2040d9041c | -10.56748 | -49.14828 | 2025-07-15 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 826f9423-d3f4-3834-8a77-f65cc94a5e74 | -11.45969 | -45.09599 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| c5238c51-e4a1-3236-b4f7-4fb16c5b6057 | -9.40662 | -40.53258 | 2025-07-15 04:10:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 44989b82-b1b3-3649-8f55-17962973b491 | -6.46965 | -45.35795 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fdf49f2-5ab6-322c-a185-d1d87c27fcb6 | -9.52167 | -45.43985 | 2025-07-15 04:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfbfd061-4e98-3771-8af0-227a59de93d5 | -9.62184 | -49.02274 | 2025-07-15 04:10:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6946d34-264c-31f2-a579-d82a84b96de9 | -10.89501 | -49.20874 | 2025-07-15 04:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5cd83edd-451c-3efc-a211-b1c125cebaf6 | -7.89197 | -44.49908 | 2025-07-15 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cace7b52-b524-316f-9caa-c9c0e79b78f3 | -7.29019 | -43.04126 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6534ed5-9a98-33e9-bf79-2fc582f1647a | -9.15399 | -44.42197 | 2025-07-15 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a8372d6-2847-3e4b-a073-18c17002f64c | -11.46034 | -45.0921 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 5a69c6f5-a5d0-328f-87bc-dec21c29a05b | -10.62665 | -47.47132 | 2025-07-15 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7880d109-cab5-37e1-8a2f-48862c1b9693 | -12.06992 | -47.98256 | 2025-07-15 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98aaf5f5-aeba-31b4-9326-a9b6bc715362 | -11.44572 | -45.09357 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 8071728d-5788-3177-8357-1cb645f75d15 | -7.15905 | -42.96888 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6cfde02f-7372-3e37-a886-00d515642e72 | -11.46484 | -47.31744 | 2025-07-15 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6761322-5788-39e6-8328-cc8948453a58 | -11.46661 | -48.52791 | 2025-07-15 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fe77632-6266-3fbc-873e-671d09c4fcdd | -6.38442 | -43.71648 | 2025-07-15 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94d25b7c-16cb-350a-b1ee-a2a6a233e4fe | -11.44987 | -45.09026 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3bbb6089-e473-30b0-8561-0f473f862060 | -11.90472 | -46.75626 | 2025-07-15 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e878bde5-9b35-3807-9ca5-68e0f4c8f897 | -10.28107 | -47.61364 | 2025-07-15 04:10:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c43f0ed2-be29-3394-8cc5-d5f135070d6e | -7.19942 | -42.9975 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ab85011b-b78b-3a78-8a66-92c4581b37bc | -10.54877 | -54.25386 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README14.md)
