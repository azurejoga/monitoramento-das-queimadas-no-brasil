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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7c2249f-f28f-3132-8362-74bc3fb73685 | -7.45056 | -42.6846 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4634f1db-1a25-3da7-bd67-2353d90ad22b | -6.36894 | -45.76121 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 998f27dc-1999-3085-9a9b-7d5b9fc380d2 | -7.12743 | -47.23419 | 2025-10-18 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25738bfa-517b-38e7-8aa6-4df2c747e597 | -7.47507 | -41.52029 | 2025-10-18 04:29:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e545f781-9a54-3e90-a3cc-81d76d00e12f | -10.15877 | -44.53003 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1137092b-d176-3b87-a9e8-8e95a2f2b9cc | -7.82388 | -40.20763 | 2025-10-18 04:29:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 966e1199-2d3a-3a35-aebf-4664b21c0e8c | -10.49688 | -43.45781 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 360303c9-a4de-3b4e-8089-6d661e9148c4 | -7.47639 | -42.74417 | 2025-10-18 04:29:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4024f532-9e7b-3fb4-9dcf-8b9fb6d06a59 | -5.34308 | -44.99997 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa065a73-a2f8-39b7-b725-ecbafd79e893 | -8.54051 | -49.52148 | 2025-10-18 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e0073ff-84bd-3feb-9448-7718ad34162e | -6.54244 | -44.46632 | 2025-10-18 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45c6d7eb-3cb3-3057-8b68-181bd80b03b2 | -8.10631 | -45.43261 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f5d01f6-60a5-3677-a25a-891fd921deaf | -9.72095 | -44.5686 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ad8bb431-7d11-35c4-a5f9-9e09e70e6469 | -9.91765 | -47.66074 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5e59670-548f-33bf-a98b-74ccd0e6b528 | -8.15869 | -49.29831 | 2025-10-18 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7c453d3-e2a4-37c0-88ff-d56a78fac166 | -10.07406 | -47.63901 | 2025-10-18 04:29:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7e8cda0-7b19-3cbf-844f-b2cce9ed45ca | -7.42805 | -46.89823 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33d94b29-5722-31ae-97e2-d1b12a70cb61 | -7.17449 | -42.17574 | 2025-10-18 04:29:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fc209295-5824-3e7b-8bb9-2574aa19f54d | -7.1792 | -46.9516 | 2025-10-18 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c892c62-bf87-3f2f-851a-d1ee447fa4b4 | -9.40272 | -49.0242 | 2025-10-18 04:29:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57c4c9da-f17f-3cab-8fa5-87d38b0f1ab8 | -10.69786 | -44.55774 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d11741fc-e1ab-35ca-ab08-95845bb4baba | -8.35249 | -49.95462 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26a98ae1-9353-344d-8db4-754a37c3461a | -10.71309 | -44.54681 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35c29452-b168-38b5-92b8-72290692498e | -10.33646 | -47.77183 | 2025-10-18 04:29:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f1309621-ca57-30b8-b13e-2c0553d85299 | -9.75045 | -43.95807 | 2025-10-18 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6c80a78-aaaf-3de0-9ca9-945c6e407444 | -10.55029 | -44.02972 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5697b7d5-20bb-3f2b-827d-ce6f9fa1352f | -4.94876 | -45.63113 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c1deb3e-3813-3f02-8828-dda90fee255e | -10.68512 | -45.33012 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c280ae0a-c014-32b8-a359-59962dcf8d8a | -9.66261 | -48.52547 | 2025-10-18 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98f429f7-4a1d-3bc3-9f5a-915e6f4a9e8d | -9.88101 | -49.11734 | 2025-10-18 04:29:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 236bd0f2-baf4-32fe-952d-58c4772e1dcd | -5.90693 | -44.7641 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b115159d-f162-3e8e-a6ab-df9017d1a466 | -7.22226 | -41.16471 | 2025-10-18 04:29:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fc79079d-2149-346c-a19b-970838b9254d | -8.3845 | -46.23892 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7392fe6d-e002-3076-8c0b-31fb85bd4d83 | -8.22113 | -43.30744 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8fb3457a-cea6-3356-875c-ae9237adfce6 | -10.17927 | -46.62649 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d92098f9-4f2e-3e57-a09e-070fe64b7176 | -7.39522 | -44.74975 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53401d69-21d1-37c6-8218-35c482d83bd5 | -10.62189 | -45.23478 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d8cfa10-9724-32d1-8b55-aff4b563e67d | -6.95439 | -44.87132 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3a0908b-d68e-3539-ab03-6e54f809ab0b | -5.54812 | -41.33612 | 2025-10-18 04:29:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1a111bdd-09ce-3302-a9aa-ab7313d9ce69 | -7.44206 | -44.74184 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43d3e69d-92ce-3581-a1cd-a5600ba185a7 | -8.415 | -44.72217 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3265c38-9e83-362e-a831-4672432ce206 | -7.36065 | -44.22649 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9089818-197a-342a-a7f0-49f569d490d1 | -4.97599 | -48.36702 | 2025-10-18 04:29:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3848fca4-2752-3257-aa0f-5a4c903743b8 | -7.36799 | -44.06062 | 2025-10-18 04:29:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60bd249f-8a8d-3f63-8858-8036807cf834 | -6.22466 | -44.42619 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3d14da7-5660-3583-9004-6b48b29f93da | -10.51533 | -43.41036 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07bcde5d-1e4b-3f4b-8f36-58c2ac840afb | -10.36961 | -48.05681 | 2025-10-18 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02584350-8ea0-3a9b-83ce-3fb8daf7a066 | -8.19148 | -43.31373 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f267610b-3075-3421-a60e-3163cdbda8c7 | -8.38505 | -46.23542 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b56c21d-e92d-34e2-9102-6ab883a090da | -8.87812 | -47.96929 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 637b227e-60ed-3f5a-85ef-c70056864044 | -4.97951 | -46.84578 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb070fe8-b148-3c23-9437-fe8694c1eb0d | -5.00906 | -46.0201 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4a0944c-1d75-3aa7-88f8-6dd5e963bb4e | -7.12408 | -47.23367 | 2025-10-18 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57701de3-a012-3f87-8e55-5f17b15ada53 | -10.50129 | -43.45388 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b496e3f-591b-32ef-a7cc-da3307d656f0 | -10.48419 | -40.50633 | 2025-10-18 04:29:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| da2da140-d297-34fd-a746-1b7dcb0f9ba9 | -11.20652 | -43.99385 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fbfda036-0dd0-3857-bf14-7d8b6ad45b65 | -6.67572 | -58.75155 | 2025-10-18 04:29:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24402781-d09b-35b4-b60d-5cb73aa9e35e | -7.45308 | -46.84122 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24d1334f-e360-3d98-b40c-04c6218fe61d | -7.45848 | -42.16811 | 2025-10-18 04:29:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| aedb4cf0-4f2d-3d63-9720-04b15d12c09a | -5.63591 | -46.39943 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00d637f1-3152-36a1-9d03-97c0629906fc | -8.09169 | -44.10453 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d0010685-ff1d-3d39-b014-16517da3ef72 | -7.45264 | -46.52759 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6724d5d5-63f5-3bb6-8ecc-d7e8291203cb | -4.96698 | -44.61673 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bbab5f8-2bf9-3171-965c-f29daa905759 | -7.18072 | -42.17968 | 2025-10-18 04:29:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 60eb1809-2715-3495-bb9e-ccc17cfeffbd | -4.87658 | -46.70382 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 046eedfa-7c5c-3866-82df-ae7021888ba9 | -5.91032 | -44.76463 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f0124c7-7a1a-3352-9404-5c0e37d63b67 | -6.8325 | -44.84902 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e54ffc49-6c26-3b72-93c1-c6f220eb9cf0 | -9.3829 | -47.00266 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ab3dd0a-4d83-30a4-9e60-fdda21441ff2 | -10.23953 | -44.04386 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b21072a2-7d0a-3fd3-a665-cdcc55a09c28 | -5.55671 | -44.14662 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ef7b418-8f8c-31f6-a7f0-5283d082eef8 | -10.50261 | -43.44482 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e7710c5-f83f-36ad-bf95-53580f0d5adb | -4.69198 | -48.62786 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37e7cda9-e27a-3360-b0f1-9553ab7fe9f2 | -5.59712 | -46.38618 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad860859-1721-3ab3-b8bc-c0ee3bc3a1f8 | -5.58752 | -49.03992 | 2025-10-18 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a4d0ccd-b047-3a3c-b3de-47ade6a910a1 | -9.11872 | -46.6207 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d41624e-bdce-3508-9537-45668a90f02c | -6.99448 | -45.19961 | 2025-10-18 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32ae6839-79c4-3574-beb9-85bf4255dc1e | -5.90637 | -44.76767 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71e2c216-4a19-37d3-b4a8-77ee9620613e | -7.01363 | -41.82655 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| bef38ab7-9a31-3157-be6a-a4919c894837 | -10.43824 | -45.01897 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e15fce82-b397-3d5c-9522-4b2677fb0a0c | -7.2067 | -45.06917 | 2025-10-18 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cfedb3f-7f6f-3ec4-b95f-a27a4d7ed400 | -9.07745 | -45.91623 | 2025-10-18 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7e72107-9a10-367d-b283-80894a1b1f80 | -9.17593 | -46.73375 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3eb41446-4571-3f1a-8b60-16425e460c1a | -4.30201 | -48.0664 | 2025-10-18 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| defb5c22-44ca-3094-afd2-81e7e02276fb | -6.18362 | -44.33245 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 123b0ebf-a05c-3036-86f5-e7d753761d68 | -6.02975 | -43.41007 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d08428b-2c44-3754-a49b-30e43c3c0d3d | -7.98723 | -44.15462 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 534d9c3d-1738-3c66-8e88-7ff84742b2e2 | -8.38299 | -49.72913 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c817464-6fba-39cc-bd7e-3853d4955913 | -6.33787 | -46.34378 | 2025-10-18 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea095174-f536-38bd-a47e-e11ee937fd62 | -5.33126 | -50.99943 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 583cc2f8-ce3d-3d31-9e0c-75600bb88a77 | -6.75776 | -45.41834 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cff739f-b6d3-3e39-b016-c1f6bcf123bc | -8.35681 | -49.72193 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27bacc5a-3cdc-3ead-b41d-d6fb5e3dcfa2 | -8.83074 | -49.6867 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11427ea5-08b3-32fe-8d56-dd5eb284adec | -7.36356 | -44.23083 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bba38d2-e01f-3df7-8d94-6af5291d3a52 | -10.2605 | -44.0278 | 2025-10-18 04:29:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6381d50a-71b8-379f-a580-2f8d6210afd6 | -5.59767 | -46.38271 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14caa8f5-d8bb-3c9c-8d97-9a2f81d462f3 | -11.84711 | -38.20164 | 2025-10-18 04:29:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9fef3c53-8731-33d1-9516-0846bacf2179 | -4.22292 | -48.3587 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f15a55d1-5584-32a8-bac2-95eef95a1b73 | -8.24984 | -44.0132 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19e19d4d-0ba6-33c5-a980-e647fb9ff67c | -9.71923 | -44.55624 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 78987df2-bde2-3b66-aeba-afc3fcc6a3dc | -10.62222 | -42.30087 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |


[Clique aqui para ver as próximas entradas](README44.md)
