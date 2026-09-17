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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 700874d7-e783-3cda-a7a1-eaa29f1ba528 | -12.3143 | -47.95785 | 2026-09-17 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f3acedb-ae5d-301c-8630-db518e42202b | -12.37411 | -48.4613 | 2026-09-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b480fb6-ca32-380e-bb8c-bbd19ebede9b | -11.3452 | -44.00681 | 2026-09-17 03:55:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28335864-bdd0-36c9-8a51-e55429588599 | -12.49928 | -50.70251 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ba8725d2-ec38-38d4-8e25-a433aac885b6 | -12.47438 | -50.9187 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63bb0301-6f7f-3f8e-8bd0-a1127731b2c1 | -7.03091 | -42.06321 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5529cf83-b955-3fa8-97b5-de9ba1b24cb2 | -7.14425 | -42.09251 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c1cf1653-c9c2-33c5-bf41-258cddd9cbeb | -7.14024 | -42.09182 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| da9e7c21-4b66-3004-a758-2e39f7d5896e | -12.59139 | -44.16031 | 2026-09-17 03:55:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7faf8c1-8a0f-3edb-a140-92297738165b | -12.43608 | -50.87568 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aeb67450-35e4-3dcf-b743-be25eb16069f | -8.4689 | -44.56663 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 692c6b07-618f-39b4-9322-5cc98cfa7460 | -11.35508 | -44.02527 | 2026-09-17 03:55:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cce73c2a-4198-3591-945f-5f27ffc178c6 | -12.44809 | -50.84964 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70411a8d-284d-35bc-a554-e186c9b8c764 | -7.64717 | -44.33779 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b539ff1e-a448-3c14-a2d5-902cef1eb683 | -12.50733 | -50.85701 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f66ad0c-8fa9-3dca-9af9-6e2c43f25349 | -11.2246 | -43.45526 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86ac4ac5-dc22-36d4-a785-b5a371794dc9 | -7.01223 | -43.34378 | 2026-09-17 03:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eab067f5-4a4a-3d85-aa70-c5bc05295ad2 | -9.61342 | -45.3498 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0edbf058-ba4b-3a9c-bf85-fec6908f0fc6 | -11.26859 | -43.46327 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 338c42b4-b781-328b-ab53-5c4050f26531 | -12.4372 | -50.87018 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de5f121d-ea53-3780-9ace-f073dea7c6a5 | -11.9148 | -44.19829 | 2026-09-17 03:55:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf2c6c47-708a-303c-973f-2f0321924e89 | -11.57195 | -46.88639 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e1bf489-629c-3c2f-88f2-26468a00a695 | -6.77812 | -48.66735 | 2026-09-17 03:55:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd5cc266-2129-371e-9e17-49affcd1c468 | -7.97681 | -44.04021 | 2026-09-17 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 663c2d59-ee99-3623-abc6-51baea1a4b0d | -9.61668 | -45.3584 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43357864-5324-33ac-b4e8-f1e3d5924c95 | -9.9902 | -45.44479 | 2026-09-17 03:55:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1353b97-3247-3e4e-87ca-47e2e61a5866 | -9.2787 | -44.3881 | 2026-09-17 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| af62352d-4646-3ad7-bc05-61f0947c9886 | -7.72211 | -42.49611 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 0a40aa76-57c6-3493-b0d7-0bd80674efc2 | -11.52664 | -46.87389 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e666d8d4-503a-3377-a6eb-4b884f62333c | -12.44893 | -50.81543 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 8ff9d7bb-b215-3bb9-9e02-705faae56ae0 | -8.53624 | -44.53559 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a79b1e24-a32d-3088-adc0-afa99b277baa | -12.45372 | -50.8565 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 37a34ca4-f0aa-3c32-a92b-2e4a16ebb50e | -12.31292 | -47.96492 | 2026-09-17 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf0a3c3a-fd05-3979-813f-bd9d973c7f1b | -7.07835 | -41.77571 | 2026-09-17 03:55:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fa92c96d-b0f0-3bf6-986d-232174d069b4 | -11.48431 | -45.73884 | 2026-09-17 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd25d34c-04cb-3308-8456-fc7f9468fd2b | -12.49564 | -50.84866 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| d97fe940-cf3d-3893-aedb-73b885e1448c | -12.51072 | -50.84061 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 401b1f08-8ed1-3205-bf76-4eb288433509 | -9.59808 | -46.65144 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49e5f941-d4bf-32bb-95d3-44a39a9167cd | -12.99035 | -44.83421 | 2026-09-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 025f5df0-f0fd-305a-89ec-4f8c880d5f64 | -7.36803 | -44.48744 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 425ac4da-28ee-3f1b-819e-1b8b153776e2 | -9.75942 | -46.09366 | 2026-09-17 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13c40578-e51d-3311-8644-691de5991143 | -10.83127 | -46.15318 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86c44631-6af1-3ccc-bd4c-6a8ef50b28f2 | -8.85726 | -46.98137 | 2026-09-17 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c9c575b-9d8c-3a72-a593-ce66f0387767 | -11.21315 | -46.40347 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f7c9592-823c-365b-bcb7-cf17c6d580a9 | -9.61947 | -45.37009 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 9811ced5-4b57-3018-806e-2325fcd4d851 | -12.44279 | -50.84271 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 58e9ffe6-05f9-3186-8b10-7323cd085820 | -11.5414 | -46.87985 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49981d9d-7867-3d40-a6cb-55e4045b532e | -12.46887 | -50.7802 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| c5dd8c9f-0050-3b6f-9216-67aac85f8b17 | -11.52779 | -46.86785 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88a8b309-95e0-38ae-b24c-e844d147b158 | -12.46777 | -50.78563 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 69d9e470-4cbf-34b1-aeec-ba25d5180e28 | -9.83081 | -46.50843 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d898cd2e-8878-3144-bf57-b9b64f9a05e6 | -10.5444 | -44.85182 | 2026-09-17 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 71b8ed5f-077e-31d8-9e0a-b29a8135d3d1 | -9.58772 | -46.64915 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96d989e2-7739-333d-9d2c-4125ef20f3e8 | -8.26555 | -42.17557 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cc58c791-12ed-3c99-95ba-7ad47ce0d6e4 | -11.58208 | -46.88885 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| db366de3-8383-351f-9576-4f10db3b49ff | -6.65739 | -43.64338 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c2920af-d8a7-3148-b9bb-0ac927379f5e | -12.43496 | -50.88118 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a3cdaecb-ebc5-3b74-9383-224ffa80fd3d | -8.55806 | -44.54105 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16e2b410-4f03-362c-a103-616b07986a4f | -8.55935 | -44.53925 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 33356671-6a10-3c84-b627-521503a01fca | -8.47147 | -44.55225 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6cd58d51-2ad3-3db7-a368-63c1c589d663 | -12.45464 | -50.78827 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 48db4118-0232-3e42-863c-0d8dbb964a67 | -6.95752 | -42.56884 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ce342e3e-3c9c-3c60-af77-27b350ef0fb9 | -8.5647 | -44.47814 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1459ef0d-6aef-355f-96b1-44e3838e5be4 | -10.55207 | -43.67433 | 2026-09-17 03:55:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c2e8a5a-6e59-319c-9e47-9bd148be2c2d | -7.09285 | -42.0949 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8374e7c7-a171-3ea3-b893-daf7c59c9713 | -8.47516 | -44.55822 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6453c0f-d310-34c7-8a30-ba52a6d620ec | -7.72084 | -42.5034 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 62270958-ea8f-34c7-9772-a10e7bcf4f9b | -8.42327 | -47.75619 | 2026-09-17 03:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5863d298-178e-3d6a-a5b0-38d3ac8c2baa | -6.70185 | -44.14088 | 2026-09-17 03:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03665755-2242-3a23-93e5-05adea7c84b6 | -12.56692 | -47.10225 | 2026-09-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 796cae82-a206-3e34-8fff-14d333f7cd20 | -9.10971 | -45.72311 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 2361a8af-48ed-3b95-b259-2b8535ff896f | -9.87875 | -48.38681 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e48db747-9f20-37ff-aa3d-71d8f8b18111 | -12.4599 | -50.79511 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| fe81123c-9a97-3442-9db7-898f9d8298bb | -6.96166 | -42.56958 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a9e627c9-afa2-3f10-9784-e9fa1a00e8b9 | -10.76386 | -46.20916 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a5be287-e296-3ac3-96c3-886258f65167 | -8.47682 | -46.89493 | 2026-09-17 03:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61693dda-4f32-3e44-b88e-a7ced5d7ea05 | -11.58386 | -46.87932 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 095fa79f-3767-38ca-a0b0-277c4195af7b | -12.45697 | -50.80592 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 762cc958-3b8f-3eb3-8ce3-598949d033d6 | -7.72148 | -42.49974 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 93b4ddc5-c8b7-36ff-aafc-8b82028364d8 | -11.17396 | -42.83952 | 2026-09-17 03:55:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 92094176-069c-3bec-aaf1-373609854bfd | -8.429 | -47.75713 | 2026-09-17 03:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28e33b51-6d85-3081-ac11-457634882cef | -8.58076 | -44.57349 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f329b55-92c2-3b52-9a85-5d81fe52e853 | -6.96102 | -42.57329 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 09cf5514-aa84-32ac-947d-6c6e28aa2983 | -7.14017 | -42.16424 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e4e668a3-b217-34c9-afe0-873dfed43763 | -11.26991 | -43.45584 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d53ba22-1ab6-3e60-a5dd-4ff4229e2135 | -8.88137 | -36.5895 | 2026-09-17 03:55:00 | NOAA-20 | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3bc4b193-cc5b-3222-810b-7ffd190964d5 | -7.96793 | -44.83378 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 14c6421c-c234-3fd7-a12d-45d5c7074210 | -8.48334 | -44.7008 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa0d35e8-0510-3b1b-9185-720f285a31fe | -7.65306 | -45.8401 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85f7ac64-3413-30ad-b66c-15d3bd487dea | -12.47668 | -50.90764 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c447af2d-36ae-38eb-84f3-160c41423818 | -12.43077 | -50.86873 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f813f852-fa67-391e-a05b-08d542692545 | -7.08885 | -42.09419 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c8ba62fc-96d3-3141-9250-08622fe3da42 | -11.88547 | -47.59411 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0040abb3-4c39-36fe-a276-581f51a09e4c | -14.13667 | -44.0131 | 2026-09-17 03:55:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9521e28c-362a-3e23-a18c-8362a43934c9 | -7.16824 | -42.09674 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 294e7cc7-f884-3006-9374-a29dfd8a7acc | -8.55558 | -44.47893 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cead5866-3615-3539-b71f-e80aa4aa228e | -7.14139 | -42.15714 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8f675209-9718-3a86-9169-b54c7d63b6e8 | -12.46138 | -50.78417 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 8d3ae3f1-ee0f-3de1-8129-a237ca077758 | -10.59747 | -38.41096 | 2026-09-17 03:55:00 | NOAA-20 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 72889918-c583-3c6e-9cb6-8143cb27f399 | -7.08941 | -43.47388 | 2026-09-17 03:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |


[Clique aqui para ver as próximas entradas](README29.md)
