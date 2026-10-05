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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddc74fa6-1977-3f8c-8212-1f46e126dc47 | -6.90708 | -43.66272 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 59463fa7-0167-324e-860d-d5ace2133871 | -6.80341 | -39.29464 | 2026-10-05 15:54:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b73c4875-188f-3985-bf6e-38aed69c891f | -6.85833 | -38.6818 | 2026-10-05 15:54:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 171460ca-61ad-3ddd-8562-5473e2b58ad5 | -7.16925 | -42.00059 | 2026-10-05 15:54:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 74a50f8b-5145-31c0-977c-fdb4aeaf92f9 | -9.15591 | -41.41329 | 2026-10-05 15:54:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 53d581fd-7080-329c-b129-96d7cde7783c | -8.41905 | -35.01548 | 2026-10-05 15:54:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 101d2e4d-701b-3021-a235-9dbe8c912267 | -6.54427 | -35.56129 | 2026-10-05 15:54:00 | NOAA-20 | RIACHÃO | PARAÍBA | Brasil | 2512747 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 299beded-7600-3bef-a4d6-e6a4e613ae9b | -9.03117 | -45.17134 | 2026-10-05 15:54:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 01329955-9e74-3f09-a0bd-2a20eb5692bc | -7.17676 | -42.00675 | 2026-10-05 15:54:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 0b54333e-293a-3a75-b400-0ae9a346bed0 | -9.79913 | -47.77831 | 2026-10-05 15:54:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6875564-b6d2-36b6-a08a-7c07b22ad3b4 | -6.69217 | -45.22372 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 226.9 |
| a99a7eb6-52d4-3e27-a3f2-2fec46f7120a | -6.88248 | -43.67921 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9ab332bf-e288-3b02-83f7-7872d00b45a7 | -6.61169 | -37.88706 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 43b9078d-5e88-3616-af42-d8d76338e810 | -9.4482 | -45.80561 | 2026-10-05 15:54:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6181b5be-8b34-3552-bfa5-da9964089f71 | -7.83067 | -45.29961 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ce227e3e-449a-3faf-b60b-394f0c9b0d62 | -7.14824 | -44.69485 | 2026-10-05 15:54:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f872f9a7-dca7-3ec6-a994-e5ed02602bf7 | -8.78623 | -47.55419 | 2026-10-05 15:54:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| ac357d48-a178-3f53-a9c7-18ec2554bc93 | -6.89783 | -43.67358 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| b0f9d6d4-df06-36e2-8da9-3a592e09b4e3 | -7.90598 | -44.18839 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 176a7444-2995-35c3-a7f9-e2aab8a1cb82 | -7.28664 | -42.41547 | 2026-10-05 15:54:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 5c8397c4-b52c-3efa-bb84-b141be8e6001 | -6.55642 | -35.50878 | 2026-10-05 15:54:00 | NOAA-20 | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4ecce311-0b89-3244-87b0-599132353283 | -7.24272 | -44.01449 | 2026-10-05 15:54:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f835bae3-7851-3087-b68b-8352b79e04f1 | -8.43277 | -39.54404 | 2026-10-05 15:54:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 21cd3345-f7ee-3cf8-9f63-fc6c055e68e5 | -9.03061 | -45.16695 | 2026-10-05 15:54:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 35fda00e-8ae3-3445-a7b0-7a8e1270b424 | -6.8209 | -38.52969 | 2026-10-05 15:54:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3b144908-b496-3b12-ab13-616bd6c69618 | -6.7167 | -43.13125 | 2026-10-05 15:54:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c7c94fa1-9e5c-3f70-8fe3-e66798f6d1ac | -6.60536 | -41.55784 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 6a4e3f91-e10a-3a1a-882f-ca2778757523 | -10.2103 | -46.68434 | 2026-10-05 15:54:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6d5e657e-e50b-3bf1-86b5-94cab05fdaa1 | -7.48378 | -42.80639 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 65718b69-c1e9-34f9-a322-058b24341d2b | -8.78702 | -47.56061 | 2026-10-05 15:54:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 780925fb-ef81-331e-813d-244be05a0b7a | -6.53801 | -39.5096 | 2026-10-05 15:54:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 52.2 |
| 8b88dd5c-3c3c-34d2-96e0-7f24b10fdeec | -6.6073 | -41.5717 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 162.2 |
| 365405bc-303c-3e0e-97ea-e2761bb95df8 | -7.85439 | -44.13905 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ac7ff437-640a-3a8c-9a81-dc2d2f2e517c | -6.88204 | -43.67596 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cd65a9ce-8b62-3105-afe2-ea0f14968000 | -10.39558 | -47.53325 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 262fc678-a91f-39bb-a19a-2e5271fdf351 | -5.98844 | -40.91116 | 2026-10-05 15:54:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 44.0 |
| c98ab47d-a6e3-34ef-a744-1a69e0df2633 | -7.90192 | -44.20052 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fbee494-2f47-3038-be26-f958bc1739ab | -6.69852 | -45.2268 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 88bc4170-6d47-3a5c-8d9f-e1153f8a9744 | -7.884 | -44.19265 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7fe399f6-a916-34a9-9365-fb6c1cc7bfc8 | -6.70434 | -45.22599 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c6ef2910-3fb7-3021-9f8a-7e83814719c5 | -6.90839 | -43.67229 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2ec46d38-695c-3f35-a583-109ca4813565 | -7.83121 | -45.30386 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 092ecf1c-602b-33e6-bfcd-fc346070e923 | -9.94553 | -45.50373 | 2026-10-05 15:54:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d458abc-84bc-3646-b4e1-37d2c1d92e50 | -9.42235 | -47.30033 | 2026-10-05 15:54:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c27952d0-d25b-3cdd-a5be-b0e975512e91 | -7.66223 | -44.38134 | 2026-10-05 15:54:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 263a3b08-980a-3cb8-87bf-050a0c129c29 | -6.69269 | -45.22753 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 210b3cea-efa5-30ec-b336-20cccb5a37fe | -7.88066 | -40.20576 | 2026-10-05 15:54:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 74cb2adf-e364-39a9-b905-aaacd45ade87 | -6.61468 | -37.88243 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 1a322d60-6059-3399-9ed8-37385185de08 | -6.60921 | -37.89523 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 56.7 |
| 415477ec-b1f9-320d-bd3a-b17b78fbe6b9 | -9.38115 | -41.1416 | 2026-10-05 15:54:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 0cb3c475-ac16-3445-971e-1f63533b6ad8 | -9.80291 | -44.79128 | 2026-10-05 15:54:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d8979d0d-fb88-3ed8-be99-e61cb9c77bce | -7.48333 | -42.80452 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| b4500ae7-edbb-3e37-9af2-452dab015f92 | -6.88775 | -43.67842 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 6d536b1c-141e-3a24-b83f-93677ebfe8c8 | -7.82422 | -45.32411 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| db5d171b-d71d-3f49-9b34-c8624d7d7031 | -10.21373 | -46.68277 | 2026-10-05 15:54:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 493bd215-a4ec-3d52-b563-66fefda2d720 | -7.48373 | -42.80739 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| fd80ad1a-c1c6-37a9-af74-bd60e53dc6d5 | -6.80731 | -39.29404 | 2026-10-05 15:54:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 21.1 |
| e8ae2ce8-043b-3af2-921a-056d856195c3 | -7.82689 | -45.31742 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 5895c814-eafd-345e-b4e2-fb65b64c2ce5 | -6.379 | -43.63656 | 2026-10-05 15:54:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ba6bad6e-e087-315b-832a-6b66c692491b | -7.49816 | -44.41882 | 2026-10-05 15:54:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| edec87f1-1b01-3989-8b0c-1fa83dc777dc | -7.82364 | -45.31981 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 976a7cd9-66d7-3973-ac63-273f4194fd5e | -6.60795 | -41.57632 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 162.2 |
| 21e3b034-d09c-374c-b0bf-aaf12fea01b8 | -7.90002 | -44.18586 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| da34ebfb-af12-306a-83a1-702eecfd8cad | -10.39398 | -47.53477 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0400423f-4554-38b8-8f78-a0c15fe338e8 | -7.4783 | -42.80505 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 854f7773-d72b-3628-bdf4-24b2ab9bb3f2 | -8.30342 | -39.15263 | 2026-10-05 15:54:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 4b2435b9-98f6-37ab-b683-f925dad25ea3 | -7.83018 | -45.32342 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a3d5f6d0-4d52-37a2-bb75-4d54cf6ff0f5 | -6.8873 | -43.67514 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3aeeef03-c8e9-3d61-8150-70c4e0e7020e | -9.03006 | -45.16256 | 2026-10-05 15:54:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 23bfec2e-e98c-348e-bc36-33935a45a229 | -6.91237 | -43.66218 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cab688ff-fa73-3aa4-9837-4d04f7942bf1 | -6.926 | -43.68324 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| c995215a-14e5-31f1-8ad5-e86ddd5dc514 | -6.60472 | -41.55326 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 38cb265e-d73d-3c3a-9851-304c9bf32047 | -7.18547 | -42.00011 | 2026-10-05 15:54:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| e5b96b13-8d7c-3565-bbc0-624220712792 | -6.88292 | -43.68242 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| da2b94f4-3021-329c-98e0-de337694ae8e | -7.02548 | -43.43549 | 2026-10-05 15:54:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f43b3de8-e02d-3446-bcbd-7abf981c3995 | -6.68103 | -45.22902 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 4afb86f4-908d-3fcd-9ce5-bb9793f23009 | -6.53728 | -39.50459 | 2026-10-05 15:54:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 52.2 |
| 3e5bd4c7-7342-3595-9bc9-3e2ef534ac35 | -6.60147 | -41.56309 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 758e4341-7199-33d1-933c-3f4648ac995a | -9.81631 | -44.80252 | 2026-10-05 15:54:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 012121de-38bb-3ca5-9518-e5e7d9a73900 | -6.60749 | -37.88352 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 24.6 |
| fcc9efc2-9da9-3f07-858a-20f0a218aacf | -7.65617 | -44.37849 | 2026-10-05 15:54:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5c570f4d-616b-3fcc-922e-b87c50aea2a2 | -6.64992 | -43.77408 | 2026-10-05 15:54:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 75ff58ac-0bbf-3f33-bf46-bffea08cfe57 | -8.43266 | -39.54285 | 2026-10-05 15:54:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 0f7e8942-7263-3000-a672-de5d5a2e8312 | -6.61573 | -41.56585 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 15a2eb54-21d6-379d-8762-eea170b9524d | -7.90645 | -44.19206 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8b659710-0407-3ddf-9a29-6e1e222df905 | -6.59823 | -41.57296 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 917d632b-c6e2-38ba-aa8e-45108eb30409 | -6.31792 | -43.34814 | 2026-10-05 15:54:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 86b1ff52-b3cb-364e-860a-c1ba48136e67 | -9.03608 | -45.16208 | 2026-10-05 15:54:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dfb5786d-fb13-3378-8700-70ac37e07014 | -10.39319 | -47.52764 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7827db57-4882-3ce5-aaa7-9153cf357f75 | -6.2861 | -43.0817 | 2026-10-05 15:54:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9dc5aa15-5695-3de9-8b96-fd3d00c3f2ba | -10.40257 | -47.53211 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d867d3b2-57ac-3cd6-b492-3d2ed6213704 | -9.15597 | -45.12492 | 2026-10-05 15:54:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b1f4e856-64b6-3b72-aed8-4fba8271947c | -7.90788 | -44.20301 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 17cebe69-1ef3-3045-9a28-9477e9874ff7 | -6.60341 | -41.57693 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 703c7162-b04b-3a28-8108-1f1bbfded812 | -8.35928 | -35.33824 | 2026-10-05 15:54:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| db064659-5a05-3f3a-9649-ae2b2cb7a974 | -6.8027 | -39.2897 | 2026-10-05 15:54:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| a47744b9-4282-367d-82c1-ad50274144eb | -6.33371 | -42.54874 | 2026-10-05 15:54:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 72e57f64-5cd9-32dc-8db0-a8eb5b44c4b8 | -6.61528 | -37.88651 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 26.7 |
| ce8f4565-e503-3be6-9309-3d79a20d3998 | -7.5222 | -44.8833 | 2026-10-05 15:54:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 67daea03-fcb1-3537-af91-305e642db472 | -6.72919 | -44.92327 | 2026-10-05 15:54:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README75.md)
