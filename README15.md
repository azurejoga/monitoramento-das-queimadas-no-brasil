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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29d04a0a-681f-3cc9-8e6b-f061aa0fff4c | -4.81683 | -45.64203 | 2025-09-26 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14e3d259-40ab-385d-a717-c7007bffc818 | -5.63232 | -43.92742 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| dd414c7f-7559-3730-befd-31a969dcc28a | -5.32016 | -43.14359 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b80b982-97a0-34a6-a3f5-23dd2289651f | -5.71942 | -44.96717 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ef9314d-8b35-38e6-abfa-aeb9a3f8e0d2 | -6.99475 | -42.59378 | 2025-09-26 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b86dbe6-2e5f-358c-87eb-d5a6dcf262c9 | -5.82328 | -43.90424 | 2025-09-26 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 343c6076-3539-3fc4-8d83-f885f746787b | -5.683 | -43.06361 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2410a76e-f1b8-3da7-8acd-930bafaee732 | -9.52761 | -51.31111 | 2025-09-26 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13625ef3-3d7b-3aad-b14d-294340d9221a | -7.12855 | -42.19059 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 577a8104-c7cb-39a2-ab52-7f8ac8b816f7 | -7.81897 | -46.89801 | 2025-09-26 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f93a908-2bd0-356f-85a2-6b73aaf01497 | -7.04294 | -46.41653 | 2025-09-26 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83e4cd37-e8f2-30e8-97e8-26c8912919bb | -3.33286 | -50.20332 | 2025-09-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a17b763b-d741-3543-b530-a51daa0e90db | -5.0539 | -40.82469 | 2025-09-26 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 09a47f29-e51f-36f2-925e-50ff52b14e93 | -8.06988 | -42.9448 | 2025-09-26 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b1672e38-85fe-37ec-b527-598779c85e38 | -5.74 | -44.94767 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ecffbeeb-1505-3efd-88e8-d63792deedeb | -3.44655 | -44.12513 | 2025-09-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 38c9698a-e73e-38df-bff1-bde6315556f7 | -9.47152 | -48.2355 | 2025-09-26 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d77d8c0-8b27-3561-933f-7289df82a3e3 | -8.26614 | -44.81452 | 2025-09-26 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37f1559a-a983-3ccd-8898-cb93f9f9a98c | -5.75014 | -44.97196 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4ac9ad79-961e-3dd0-a970-33eb182192e6 | -7.49938 | -45.41551 | 2025-09-26 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97b2f859-78b7-39f0-a9df-1b605a9210ed | -6.59491 | -41.92278 | 2025-09-26 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0230f6b2-0db4-3df5-ab23-3839023f5f02 | -10.59074 | -44.06242 | 2025-09-26 04:14:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 132113c4-57ff-3acc-bd4e-e38f228b6dd0 | -5.46181 | -43.06361 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7fa10737-a3d6-3373-8be4-68827344e257 | -5.43162 | -45.14059 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35cbd2ec-3f3b-397d-9144-0a35ed052911 | -7.93871 | -45.19831 | 2025-09-26 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec8c3464-aaa6-3b73-8f68-268135963810 | -7.10017 | -44.48232 | 2025-09-26 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| caa9a3e9-9fa3-3963-9d01-e6d4736a01ba | -5.74168 | -42.55783 | 2025-09-26 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| df931eb3-310b-37c3-9255-3cf0caec4424 | -6.26265 | -42.4907 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 91b44ad2-60a8-3bf8-bf7c-d8f180e513a8 | -5.4717 | -43.06516 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0480d3b7-0185-3677-8e6a-09c04ce2035f | -5.79252 | -42.86578 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 625ba8d3-54f9-3ed0-8ec9-d506382f24fe | -10.18558 | -44.83867 | 2025-09-26 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1db729bc-f5ea-3808-9f6a-f2f1d98c7aa6 | -8.51118 | -44.62171 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b70acf2-2924-343a-9c5f-c3f8ef6ebe7e | -5.6863 | -43.06413 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c5ebee30-af79-30f7-afd6-95bff7e71fc8 | -5.74444 | -42.5618 | 2025-09-26 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8374d55e-4b99-3199-bd94-c1a10358591c | -5.73825 | -44.95872 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 49c3a909-f63c-370c-abfc-fc18ea870d97 | -6.31563 | -41.88326 | 2025-09-26 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 00005bf5-f6d7-37a7-8188-cfeac53155d7 | -6.93558 | -44.6379 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ccda6c1a-4ed4-356c-b8f2-22fbcc48bb5b | -5.77342 | -42.90154 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 376d7c01-24a6-32e2-bfe6-2dbcfc215f80 | -5.53417 | -44.39365 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b513ccdc-9f15-37cc-aa50-fb46ddc9f1a0 | -7.57725 | -42.41156 | 2025-09-26 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| faedafdb-4961-3118-9b70-5c45c524fa32 | -7.37335 | -47.03035 | 2025-09-26 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2d71d059-bc93-391e-92df-2b6624339f48 | -5.73708 | -44.9661 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| a484945a-0570-38aa-965d-0ce8b269d2a6 | -5.54117 | -42.81538 | 2025-09-26 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9fe5dc18-ccb8-30a9-a60c-8737ba844098 | -4.77368 | -41.05121 | 2025-09-26 04:14:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d3d8fd17-1226-3128-b2ad-8e547394a7e7 | -6.27417 | -42.19524 | 2025-09-26 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 05c79d99-8a9b-38fa-af74-49ff1d68a361 | -5.3989 | -42.26656 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 150dde4e-ea79-3b18-b388-daa336da0d7e | -10.59571 | -44.07392 | 2025-09-26 04:14:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 910a1d38-bec7-31b7-9705-85d04d51747b | -3.80156 | -47.58342 | 2025-09-26 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1cd7cb6-c7b7-3ec3-bd2a-0cf1137613d1 | -6.88213 | -44.5052 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a83f43d2-5403-3fa0-b29f-b783c8b5b9e9 | -7.7994 | -46.014 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 374c3768-0067-3e1f-a820-b52e06329b5c | -5.7399 | -44.97034 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| fcdcdf1b-4376-3d75-a79f-2ded016b45e5 | -5.79481 | -43.82486 | 2025-09-26 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd7bcd93-a1b5-30df-bc1b-146d9e42fa93 | -10.4081 | -46.16318 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfb2b439-f52d-3604-aa19-3175733ad7c5 | -9.24897 | -44.26352 | 2025-09-26 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e47d9db9-bbf0-3213-9e29-b4099fa5fd5d | -10.81218 | -44.42706 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 909e7300-1c9c-3227-a1dc-084a09234ab1 | -5.47116 | -43.0686 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8b294d7f-81be-35f7-ba71-9e7a4ab147c2 | -6.99957 | -42.80517 | 2025-09-26 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 00ae8416-31f3-38af-9642-5639d1c15a84 | -9.8729 | -45.91083 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97d1dfc1-2934-36d1-9b07-f3a014917a70 | -9.8872 | -45.7379 | 2025-09-26 04:14:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cefb1069-0843-35b2-8b48-b4ac971c30b8 | -8.69633 | -44.03184 | 2025-09-26 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5978be0d-30c5-3367-bd53-7c7b328da463 | -5.72953 | -44.99163 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 050e33ab-d67d-3d7e-967e-796cad321dec | -5.24442 | -43.08246 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28d69080-0a7f-34fa-aafe-9ed136296899 | -7.70375 | -47.67518 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 564d8e6a-e296-30de-b96e-9bf3c3be58be | -5.72002 | -44.96346 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a50e8ba0-7777-3262-a661-1ffce675f0e3 | -9.97762 | -46.70722 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e1eb949-6019-3bde-903a-5805a8387eb0 | -10.39688 | -46.14583 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 19889109-faa8-3cb9-b6fe-92f8ee3c629e | -9.94616 | -46.27951 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cc9c6b9-81a4-3183-bdd3-f48f58b8092d | -7.11628 | -42.18145 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 93449a52-ae31-38d8-829f-86b3d95fe8fc | -10.18502 | -44.84219 | 2025-09-26 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dcfe328-9c71-3bdb-9ec3-1e8a538d2c61 | -5.73695 | -44.98898 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ccb78d0-4ae5-3e90-b671-a1fafeeff63e | -5.74037 | -44.98953 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 247d1a88-ac37-3887-84fc-fddfb9f18533 | -5.80273 | -42.8004 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| ea08e133-c594-331f-9d1f-7f757d8541dc | -3.80556 | -47.58411 | 2025-09-26 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 283bd3a2-3bc4-3fd1-bce1-9c981bfd7958 | -4.88374 | -44.96303 | 2025-09-26 04:14:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77b38c7e-3389-3c2c-b808-e1f716725c18 | -7.10815 | -43.74196 | 2025-09-26 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6febbb7b-878b-39f8-bf09-3fa7db75eba5 | -5.08188 | -44.07121 | 2025-09-26 04:14:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32513160-1391-3028-a638-39e4ad4612e8 | -5.38934 | -45.85231 | 2025-09-26 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fbd646a-b25e-3038-a95b-a5222ba55070 | -8.6677 | -43.99886 | 2025-09-26 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c27ab240-eb34-38fb-98f3-1ed389e48ac0 | -9.85365 | -49.16648 | 2025-09-26 04:14:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42a342ff-7843-373b-adb9-32abc26ce613 | -4.32262 | -44.29137 | 2025-09-26 04:14:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2bb1cf0-09a1-3391-8229-0cf2cc3fee7a | -4.82036 | -45.64261 | 2025-09-26 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e2b5d99-b14a-3a3c-b75e-7d3d0016f5c6 | -5.12539 | -45.50252 | 2025-09-26 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1391010a-4be0-3782-948a-7ea2ac3da81a | -10.92974 | -44.28518 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 850bb951-bcb7-367b-9fc2-6e7aa4eb4536 | -7.31625 | -45.76702 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39966ca0-1b22-3da3-9d1e-bbb01b40d5fd | -6.96891 | -42.29935 | 2025-09-26 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bec254c1-43d5-35ed-8534-b2a8b5ed0b2c | -4.79293 | -42.8172 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 90ccfca6-b330-3ecd-9a3a-4f169b49d459 | -9.42634 | -45.58376 | 2025-09-26 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b57b5ab9-3a21-3acf-904c-c6f5102e07d4 | -4.81517 | -42.73976 | 2025-09-26 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 294c574c-29a7-39dc-916e-fd2215536785 | -5.00208 | -44.88221 | 2025-09-26 04:14:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17221cb8-2ea4-3fb6-9fda-efb82e28d0ca | -8.85723 | -46.20891 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1d12c59-7f2f-3c60-b27c-fae4d0037962 | -5.61704 | -43.46251 | 2025-09-26 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9788e992-d840-349e-bfc8-2383ba32fb5d | -7.1297 | -42.20529 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72428fee-c3e1-3cfa-ba31-ecce2dacf522 | -8.77525 | -43.04523 | 2025-09-26 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 39efc7eb-0e87-327a-98bd-3b9faaba9ea5 | -10.40968 | -46.17505 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cbb8dcd-21b5-35f4-a797-d302014756e0 | -4.79805 | -43.04315 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87f6ba6d-d99a-3e4a-b974-a311b27f930e | -4.79983 | -47.28006 | 2025-09-26 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acb3dd46-6a6b-3f4c-800d-a714446afcd2 | -7.11914 | -43.7366 | 2025-09-26 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c013829-d64b-31ad-a77b-82f1894c4021 | -6.64197 | -43.82768 | 2025-09-26 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5819a27d-cf4f-310f-9c21-d8762177f08f | -5.63571 | -44.72102 | 2025-09-26 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 926c0067-d8d5-3fd9-b99e-a73788f0278c | -10.31728 | -48.18308 | 2025-09-26 04:14:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README16.md)
