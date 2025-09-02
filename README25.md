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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29a7005b-821a-3dc6-93bf-53dcc156b056 | -7.49654 | -45.34854 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| feb9e02b-c04a-39fc-bb12-38a0ab86efc9 | -12.33976 | -45.67447 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ab41a2a-6086-39c6-a461-bc1d229d1073 | -7.98377 | -46.45959 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b4318fa3-7e72-3f71-bde2-4076008f8130 | -8.00062 | -44.04706 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17fd096a-e09c-3439-a5b3-96f7f80961d8 | -9.11427 | -46.0529 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96339df3-d7f9-35f4-ac56-922353c18c92 | -14.58461 | -48.06331 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c1033a1-d05e-366a-b7c5-5840084a7475 | -13.69802 | -46.94223 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 15b05bbf-4ddf-37a0-ac9b-83314b6c8972 | -13.89659 | -48.08931 | 2025-09-02 03:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61081060-98a0-3321-b9d6-06cf0d8460e3 | -11.93724 | -50.6154 | 2025-09-02 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aae53de0-c3a4-390c-bf64-d399b066ee52 | -13.29182 | -46.92876 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c92904ba-5d68-3dea-bed8-5660d21f665c | -11.10763 | -44.6401 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12b38779-a542-3ea6-a9c0-174da765650f | -11.6552 | -52.20585 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 3e63b86e-79b8-3c15-afd3-ef67e63ab11b | -8.70355 | -50.43769 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a913a8ae-2993-3d3a-99cf-14c01e048be0 | -12.76226 | -48.08286 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2a54e40-1243-3d95-8666-f14106fb8c83 | -13.49052 | -46.92465 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de6fe7ae-1f0b-32dd-aff4-e13184ed02c9 | -11.82148 | -51.54858 | 2025-09-02 03:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 79b64b52-8e60-33ca-a3e3-01a5e5b6578a | -13.53096 | -47.00065 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 655234d7-afe6-3013-8f44-35b495ad4f35 | -8.49429 | -44.63615 | 2025-09-02 03:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5dd8386b-f891-33e8-9317-31195e419abd | -14.21306 | -48.06702 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb76f84a-aea2-3e8a-992c-a653e4a25c62 | -11.81513 | -46.40262 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c556ac3d-e39a-3482-b47a-d8f7eda7d29f | -11.06512 | -46.91656 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb238c89-0dc5-3612-a8ab-bb786b9e4b89 | -8.81177 | -47.83258 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 683721ea-8347-38f4-8945-5f52e95e0249 | -12.92869 | -48.10391 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f066a051-bfa5-3441-b203-ff8d46f36b3c | -13.5315 | -41.84252 | 2025-09-02 03:51:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9fbfe9b6-889d-33cc-9c8e-d2834eae9a2d | -7.9804 | -46.47776 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1bef780a-9444-3031-bb73-fe3840949f04 | -7.72401 | -50.25484 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 650eb425-26a7-3465-b257-9d4c65b4fad4 | -8.01438 | -44.04976 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d06e5af8-c353-3b62-a953-7db768be844f | -10.26499 | -47.52351 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 646fb7f1-3a79-3613-af0b-206fdccbf934 | -7.71546 | -50.25816 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 946bc0a1-4f79-3d1c-a2df-7f9856358969 | -12.56218 | -44.78618 | 2025-09-02 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 556eb774-e942-310c-aaa7-108b1139f0f5 | -14.58992 | -48.06458 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5db5940a-500c-3699-88cf-f831f82d9c52 | -11.04293 | -45.14328 | 2025-09-02 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11b5bfbc-cd40-34ae-9459-1ac60b020836 | -9.47555 | -47.6041 | 2025-09-02 03:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e371857-a941-3bc9-87a6-095505e2491b | -11.67364 | -52.22527 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 8a57376f-b9ed-3cd5-a9c7-6add88ff8eb9 | -10.83293 | -47.4484 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bc783511-a183-31f5-9806-cee294ce5140 | -11.6649 | -52.23117 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| eee1e13b-0953-3266-bae9-6bb90a32e254 | -10.05163 | -48.11801 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 999c6581-d1e2-3f7c-8b3e-c3afd64f7cc7 | -11.09124 | -44.6534 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 68ad5aab-a222-304a-9c7d-cf3c7abb673e | -12.62088 | -48.19177 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b466f509-ab0c-31d1-9f3d-c6c77e1ff65d | -12.86075 | -48.04875 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4776e072-d9a9-3f46-9338-c4f132de0fe0 | -11.06105 | -45.3919 | 2025-09-02 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1353969b-0538-3f3d-b9df-bec3c69c5e76 | -7.9867 | -44.05312 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65c7e0a3-9260-353c-bcb2-6416c70ebe2d | -11.38543 | -43.62753 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 620a07f2-7305-3466-af68-5d38e7436bc2 | -11.6731 | -52.20141 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 3fab1590-1e4a-379e-b25b-234f9b286722 | -8.18986 | -46.78356 | 2025-09-02 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5cdeef7d-127b-3951-a068-978e63a26528 | -13.53839 | -46.98956 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2980ed3-6e9e-35ba-a9eb-1fe6f9d5130a | -11.10166 | -44.62134 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| dd75a4db-7606-3714-98d4-80574bdb4230 | -13.31248 | -43.79366 | 2025-09-02 03:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bbbeb7b-bd1b-35b9-bc04-60298789f246 | -12.76162 | -48.08606 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f2f07aba-4095-3ced-8f51-e36cbcc4acc4 | -8.85901 | -45.79214 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50f21650-8bdf-348f-9245-e986353969e9 | -10.58407 | -44.85766 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ada5ce54-9dec-379e-9abd-76affaffff6a | -11.97177 | -45.8632 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f85f956e-41e1-3b25-93f5-6277148aefc1 | -13.29242 | -46.92572 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f33cfa80-6e4d-3055-adde-0d00758c4ecf | -12.33204 | -45.714 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b43a4579-cf21-3fd4-a86c-10c712b6406a | -7.97947 | -46.4784 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d69c187d-066c-3bbf-87ed-5d0add4aced2 | -7.58037 | -45.21768 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d7a225c-e9a5-3a14-a075-388b75dd7392 | -7.88507 | -45.18061 | 2025-09-02 03:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75bd0ce0-a35e-3d63-a740-55319ac87ee0 | -14.04748 | -44.55098 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2599cf41-e490-3f58-875d-1a8beb3fb1c1 | -11.92183 | -50.62387 | 2025-09-02 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2e033c6-a545-3030-8e26-e9559aaf58fb | -9.83429 | -48.61262 | 2025-09-02 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eabca71e-a004-3475-8fcb-d31b06e47a63 | -7.97955 | -44.05862 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7296c92f-4826-398b-a23a-d98ad08db843 | -11.10083 | -44.62599 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 90fd721e-de70-3ee3-be4d-201d405e0738 | -11.66452 | -52.16148 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e72d1d6b-3d4b-3832-8751-3a994c484740 | -11.65475 | -52.1822 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| de567717-63fb-39ee-b2d0-2f52fb407ad4 | -8.12585 | -45.03465 | 2025-09-02 03:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5cdd04df-0699-3130-8023-6d97a50819a3 | -7.98911 | -46.46099 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 96f6a311-f959-307d-a5ed-866ef610c492 | -7.56808 | -45.22833 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ba02ba0-66a3-3264-a7e6-a61b0a1f3847 | -10.06095 | -48.13219 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba7c7c85-8c47-3e45-b8c8-de2b782d1ad7 | -11.66644 | -52.22378 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 5ad39ec0-6b4c-3a66-b60e-3f2d3580a782 | -10.0602 | -48.13604 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a4e8c527-c1dc-3b62-963a-e93a7bfdf704 | -12.62247 | -48.18384 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 811bdb63-36a1-310f-a274-e55c6b470f53 | -13.5509 | -46.97946 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af12f47e-3ef5-3c5a-84dd-913f8172a616 | -11.91869 | -46.4521 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6ecbec2-c44e-3eaa-885f-ea976827e466 | -13.28468 | -46.91141 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e372b0c-d0f1-3786-b480-87442779ddb3 | -7.91784 | -46.44741 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca999e08-6413-3902-8df1-e8ce77249b97 | -11.35924 | -43.52959 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7417f1f6-fc30-38e9-a37a-bb4a91edce0a | -12.95866 | -48.09727 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 450563be-4c17-32e7-93f1-a1b5804563be | -14.73849 | -46.75351 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b3e7e59-2868-3295-9b4b-5ed9ce4480c9 | -11.67117 | -52.20121 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| a16caaea-c276-324f-9a9a-75dbebe5d6b4 | -9.4823 | -46.50694 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fdadc574-186b-34e7-ad09-2cdddf805afd | -13.69037 | -46.92733 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50d87f51-92e3-3445-b224-709ac371ea55 | -11.3761 | -43.5569 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7baf1b1d-4734-3d5f-bb19-cb2104a5a6f1 | -11.09175 | -44.62434 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 45a95239-f200-3f21-aff7-f0a6a372ffb7 | -7.98395 | -46.4532 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d3a6ea1b-aa16-355b-bf5f-21e1764dbb0c | -11.9087 | -46.67353 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3c22a55-d788-3a22-b2d0-6610afd8fbd2 | -7.78963 | -45.45692 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 097d8a05-05c2-3dc4-a829-9ca6bc37ea1b | -7.70006 | -50.26862 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6df28b89-b077-395f-a711-47b9dbebb6af | -7.69819 | -50.2736 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a0a427a0-7577-3b25-8632-23e44239d091 | -10.05489 | -48.10126 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 153a807b-8284-3775-b045-9c4b2e0d1f41 | -14.04858 | -44.59427 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e61fc591-f5d8-3f8c-9e18-dbe766b71f56 | -9.12979 | -46.05575 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d734675d-3461-3346-86cc-b2f86639842e | -10.04751 | -48.14788 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5581925a-88c5-30c0-b25f-6f9e46873a70 | -14.25994 | -45.24779 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b0d7b5f-d8d0-3277-be15-2c8479932dd1 | -10.04685 | -48.11916 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e89492b5-83d9-3914-a3d3-cfd0a915be7f | -10.83707 | -47.28074 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bf8fb73-8ca3-35bc-910a-bbdb6db338f7 | -11.91374 | -46.675 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af734f71-23f4-38c5-9ada-349ef3bf8805 | -11.79974 | -46.4011 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 40851b93-c57a-3f2c-9c81-154ae839b9b6 | -14.2697 | -45.25289 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fd9fc697-b8e2-3185-bb31-b154af2fdec2 | -7.56047 | -45.71438 | 2025-09-02 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c491a9f-5528-368d-a58a-ec362e6b35c6 | -8.1519 | -42.4728 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README26.md)
