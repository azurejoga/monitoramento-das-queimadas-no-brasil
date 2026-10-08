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

## Dados Diários - Página 288

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45df2a39-2d9e-3f79-8b91-eda25a6deea0 | -6.19232 | -37.86098 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 8697597e-9ae0-38d3-9be7-cfb6179060e2 | -5.68627 | -40.88971 | 2026-10-08 16:20:00 | NPP-375 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b5e329df-1cbd-3600-8e0c-8d7adce1469f | -2.74633 | -54.11705 | 2026-10-08 16:20:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a19c43d4-d740-30ca-b2d0-a15200c7e3d3 | -6.31801 | -37.75142 | 2026-10-08 16:20:00 | NPP-375 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 50d61c58-7f99-3de0-8cea-94c1b1c47ae5 | -2.99762 | -43.28275 | 2026-10-08 16:20:00 | NPP-375 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b851ad49-ffc7-3681-8009-c2d79241bad8 | -5.72889 | -45.23223 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a6356900-be0d-3dcb-bdfb-8e1dccf2c8ab | -6.14186 | -47.95477 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44ecbaeb-7ff3-3bf6-936c-0028d32d2020 | -3.89541 | -41.5946 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8045c266-869e-3c94-941b-e1201f30b956 | -5.24457 | -37.58002 | 2026-10-08 16:20:00 | NPP-375 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 65455f55-dbb5-3b88-8732-f86600607b17 | -3.38586 | -50.21939 | 2026-10-08 16:20:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 04b69645-a7b2-30d5-a01a-d352b2c0dd25 | -6.97758 | -47.67031 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 5cc15acb-89e2-3ae2-9d5f-a88cc1b5d65d | -6.05317 | -42.60436 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 5e31d2ea-4868-3fd3-959b-f857d616633a | -6.69262 | -45.29541 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 77a87d6d-2d33-3de2-96d7-b7e5f84f307d | -3.08392 | -53.9569 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 3d07b6c2-f94f-379f-8d7f-f8d988ec1b3e | -6.85223 | -39.46146 | 2026-10-08 16:20:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 272c674f-6562-3e29-a1ad-55ebafdcb55b | -5.96311 | -40.92466 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 9a4b81e8-36fb-3468-a8b0-054b187dba28 | -7.40524 | -44.44897 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0e6d115f-4a0e-3f0c-87da-96f6e35c390a | -7.16604 | -44.82427 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 807c4e38-1e09-3049-a7fd-d779fc4da566 | -7.02752 | -44.72583 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 8d8f60ae-e109-30de-b633-9aba2181485a | -3.30755 | -53.69563 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 751339b5-db1c-3576-982e-91a172428bca | -6.8403 | -39.55931 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4bf09268-6024-3e56-977c-cef187d54fde | -5.7496 | -41.72486 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 431.5 |
| cade9c09-98c9-37f2-ba2c-e99984717cd8 | -3.25552 | -43.5916 | 2026-10-08 16:20:00 | NPP-375 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 20354bf1-520d-3912-a30a-0be59ff7e13b | -7.34039 | -45.28817 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ded14b4b-238e-3edb-8314-6b5388865b37 | -3.39625 | -41.52162 | 2026-10-08 16:20:00 | NPP-375 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e331be9e-d038-38bd-bf32-d7fb53796596 | -5.76112 | -42.06472 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 12df2145-b83c-3873-8d2d-e86f27cb7b23 | -6.32282 | -35.12413 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 5b6dc8ac-0847-3827-9fc2-6383d1895c31 | -5.70266 | -53.44442 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 3425d491-7e74-3982-aa85-f8a9fc5001f1 | -5.95159 | -44.26571 | 2026-10-08 16:20:00 | NPP-375 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e555b102-68d3-3556-9aaf-f92935af981c | -6.16029 | -52.64898 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| ffbac93d-aa83-32db-86eb-ce5c9f24a5e9 | -3.81579 | -44.62243 | 2026-10-08 16:20:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ae4a6e3d-793c-3550-a8ac-c261d49c089a | -6.49966 | -44.70686 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7506474a-89cc-3cb7-92e4-bdd588089ae2 | -5.7084 | -53.4931 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 4d15dfe8-fdc7-3279-8e41-4b5a8329c744 | -2.92741 | -54.12207 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 0aeb85dd-da8b-3d17-be6e-0ed087ae1434 | -4.32287 | -41.23568 | 2026-10-08 16:20:00 | NPP-375 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 8e3ba3e5-f615-3c09-bd63-8aface8d796a | -6.67284 | -45.37391 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 878df807-4f10-3cea-afd5-fb9460bf4ba5 | -5.97571 | -41.35556 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d97a7c3a-8ff2-3738-bc58-26eafceb02a6 | -5.38639 | -44.18818 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 681b013f-6ed0-3f86-97b6-e29336840a67 | -6.154 | -39.42677 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 208c17c3-0e0a-31e8-9af2-dd50b26260bb | -7.22315 | -44.15974 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 31b52763-7e74-3d34-a9ec-0c07160162d0 | -6.72585 | -45.17841 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| af9ad807-36a5-35d4-9fe1-0051c27c4e3f | -7.25818 | -45.33858 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3e5ee644-7f78-3555-9807-9d92859d4051 | -6.31669 | -35.15915 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 715ddaa0-14bc-3bfb-8b66-06a1a0499605 | -3.25147 | -43.87625 | 2026-10-08 16:20:00 | NPP-375 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 03dd6ee3-60c3-3695-a019-9e0ed930236c | -6.40782 | -44.96105 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| abe18a8e-a3ca-3e80-b39b-a9ddbbccccd3 | -3.46815 | -43.07151 | 2026-10-08 16:20:00 | NPP-375 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 406b99ec-c82e-34bd-aa3f-12e4e3d40e14 | -4.38717 | -43.95533 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fc5e45ce-c1e1-3b47-9329-9a4ab1c35fb0 | -5.68305 | -42.59196 | 2026-10-08 16:20:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 60bcf5d9-78ad-3eff-b261-9836ebbff399 | -6.50203 | -44.20786 | 2026-10-08 16:20:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a569c197-171a-3087-aa31-c34c7f37b73a | -3.85626 | -44.11512 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e138f1d4-6d39-34ae-ba03-8c6fbd9391de | -5.40293 | -40.31014 | 2026-10-08 16:20:00 | NPP-375 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 8d88c6f1-bd55-3dc0-83d9-da6ae7173abe | -6.37104 | -42.90271 | 2026-10-08 16:20:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 45c42de6-09ae-3913-a959-8bb264b844cd | -5.69805 | -53.46574 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| e79777fa-1150-359e-9198-096c0f6055a8 | -6.22425 | -35.32692 | 2026-10-08 16:20:00 | NPP-375 | JUNDIÁ | RIO GRANDE DO NORTE | Brasil | 2406155 | 24 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 3f7b6187-606b-3c24-982b-1e7d548cefc1 | -2.74524 | -54.10973 | 2026-10-08 16:20:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| ac115ee8-7d02-325b-905c-3fba3c70613c | -5.7525 | -41.72052 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 83292fa8-0843-36ce-8f8a-a9ecc04f02de | -6.14843 | -38.34064 | 2026-10-08 16:20:00 | NPP-375 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 737d0ce9-43db-356f-8672-a5bbc2ff7556 | -6.18835 | -37.85785 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5443e8ad-c349-3a14-ad7d-8bc2ae19a673 | -6.92893 | -45.26032 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| aa0156a2-81d8-34b4-9971-d08930178cdc | -2.21955 | -53.69778 | 2026-10-08 16:20:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6566c80-9a03-3666-99cf-ab36a2abab8e | -5.38369 | -44.19102 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 402d6a41-805e-3123-84b6-6a667c37ab1c | -5.76759 | -42.05974 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| ede8f8d1-6a8e-3026-bc57-3fb9677572e0 | -6.0436 | -53.48652 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| bb34b14b-23f2-3800-94f0-298134755d44 | -1.29931 | -45.92976 | 2026-10-08 16:20:00 | NPP-375 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 584edb21-1b95-3446-b678-5975eb1014f8 | -5.27872 | -45.73207 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d285e6a4-ceac-3fa4-8154-37be6d9c6c6a | -4.38264 | -43.95115 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5cfa2dba-f29a-37dc-ac1b-bcdf00d9934e | -5.95689 | -40.9293 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 7b8f0f66-0dbe-3b5e-8daf-ac6b4f163fff | -1.87371 | -48.82817 | 2026-10-08 16:20:00 | NPP-375 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8fcc9060-8d6f-31e4-a68a-e601819718a8 | -4.3184 | -41.22898 | 2026-10-08 16:20:00 | NPP-375 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 3f33a4e2-4135-3f72-9238-9bd2b58960f2 | -6.55445 | -45.36059 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| f85aaf4c-67fe-3abb-9b1a-80eff088451f | -5.75133 | -41.73634 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| c953c05c-a73f-3892-a7e6-39a5efcb4a8e | -3.11252 | -41.16686 | 2026-10-08 16:20:00 | NPP-375 | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e19ae8bd-941b-3f66-8267-b61e7acf8871 | -5.23434 | -38.54807 | 2026-10-08 16:20:00 | NPP-375 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ddddb5d5-e17b-3528-a623-98363ae06f96 | -5.54273 | -43.22328 | 2026-10-08 16:20:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 05da916a-831c-3c0e-a976-69ca34250f27 | -3.28198 | -45.15293 | 2026-10-08 16:20:00 | NPP-375 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 9fa2000b-ce81-3c54-a9eb-422d6a385a84 | -2.83281 | -48.64795 | 2026-10-08 16:20:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 9a0941ac-79f8-3a7c-9519-1225d0827de2 | -6.31975 | -35.1295 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 36.8 |
| 9f61cb0e-48ed-3967-a6aa-23bf34c2d350 | -5.36755 | -45.72875 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fbce5e38-3c9e-34f9-aa5f-72f103f9e3af | -6.43102 | -43.82629 | 2026-10-08 16:20:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 143eb9f6-0900-3858-8e0a-f90cea17fe6b | -6.16438 | -53.43456 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 54a52e91-4fed-3e4e-b174-8f7564459023 | -5.71536 | -41.75739 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b8ff7209-4563-3267-8628-647e3638b148 | -6.64109 | -52.95963 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ad054c9a-d376-3f38-b4d5-bb2547730e79 | -6.13156 | -47.93282 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 933defb7-9a93-39b4-949b-d4a42514706c | -5.76877 | -42.06763 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| d4b7ed05-9eae-3a02-a570-81cabddb3b44 | -7.04538 | -44.33559 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6110fa0f-c895-3e29-85fc-7b47b02d9c30 | -6.2491 | -52.68178 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| da7dec40-415c-3242-9042-acfeb0a7e80f | -1.09433 | -48.05021 | 2026-10-08 16:20:00 | NPP-375 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2583f649-401e-39d5-b7d3-e48a6e1b6306 | -3.67643 | -39.10497 | 2026-10-08 16:20:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 25428e6a-f3a0-305b-ab25-5b823d50ee4a | -4.38143 | -43.95436 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8f142d5-fa9b-353e-bf74-c2723cd2c452 | -6.15612 | -39.44063 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 25ca7046-26ea-3752-b7a7-bbfcf669af05 | -7.81411 | -44.57266 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 00118759-6711-35da-8faa-f3058a6ec4ac | -7.59519 | -42.39336 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 33.0 |
| 016d2a65-1bc1-35c1-9587-8eb262279229 | -6.91811 | -45.88614 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c6b64a26-6a4c-3902-a1bf-8089d1349fdb | -3.44336 | -45.09226 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 71512aea-77ec-3ad1-bcde-55ce14563fdb | -6.20262 | -51.43207 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| bab0c1b3-79cb-31e9-b075-d1b1ca21b384 | -7.48351 | -42.8273 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 8e5ff401-7e16-37cc-9dc8-b4b333398e14 | -3.26205 | -42.95523 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f03f590e-f94a-3afb-b05b-eb6815b6f0b1 | -7.06133 | -40.94584 | 2026-10-08 16:20:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| ca7447c3-8280-3bd5-b35f-049c00922860 | -3.79541 | -41.66927 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 54c63068-4090-305d-8656-523a36a32ff8 | -3.78572 | -41.67448 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |


[Clique aqui para ver as próximas entradas](README289.md)
