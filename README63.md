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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 295f779c-568b-3335-a75f-e6a0c7d939e7 | -11.15191 | -47.74587 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d5dd4e2-e2a8-3faf-95ee-7179f5341b48 | -7.52283 | -44.09309 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbae8287-14a9-30ed-8234-b9d50bb0f50d | -11.78912 | -45.14124 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f072d1ee-bcb3-38e4-b38f-0ce9f17dcfde | -4.25676 | -48.54359 | 2025-10-08 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 591508fc-b51d-33fc-b92b-97f47d94f471 | -7.47456 | -43.09727 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| abc7de9a-8270-3ec9-a42b-c496d47e8bda | -8.55924 | -44.62751 | 2025-10-08 04:38:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1371060-3671-3c8e-81c1-55f55818429a | -11.79408 | -45.05434 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 478d1f3b-22d8-3f97-80a3-4d7e75b318f1 | -4.26121 | -48.55836 | 2025-10-08 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d53ff641-f2be-3e41-bb65-a95c6a808574 | -5.83155 | -35.48084 | 2025-10-08 04:38:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8d4b3bc4-4f11-3510-801d-a5aeaf2ab666 | -10.49908 | -49.14171 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5736d0d1-5c68-3515-bab5-f0df0bb49771 | -11.22127 | -47.76707 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8ca4296-a250-38c3-ae80-03dc12dbbade | -6.69709 | -58.81078 | 2025-10-08 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a54426d-fce7-3d5c-8257-68ce2dfd664a | -11.804 | -45.04383 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 230f0e64-6d1a-3aa9-9545-c20dc98ba999 | -8.23021 | -44.17756 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ecebf8a-83b9-38b0-acbf-a764e62b5243 | -8.37192 | -47.76102 | 2025-10-08 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9624a373-ebb5-3301-979a-4ed517554a63 | -4.96747 | -46.83276 | 2025-10-08 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c466ef86-6847-3d8f-b9e0-7b33c96f0e75 | -9.68604 | -49.93641 | 2025-10-08 04:38:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1f9acda-3857-367d-acea-cc71c0bcfda7 | -5.72986 | -43.61575 | 2025-10-08 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4dc19e02-53e7-3e24-b895-4fb3026c5fc5 | -8.78337 | -48.00153 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6fe8854-ff8a-3f0f-a2ab-bc954d6556d3 | -8.70553 | -47.86773 | 2025-10-08 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea18ed38-b7b2-3f86-abc9-c4ba583f706c | -5.75964 | -45.75351 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7f48150-8f6e-3282-a6b6-e5f650bc61db | -9.303 | -60.59895 | 2025-10-08 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb2d74ee-d178-3d5a-a3a5-5b9d670aa479 | -5.16011 | -46.923 | 2025-10-08 04:38:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b32c5897-d003-31ad-b623-602b0ce93479 | -5.69697 | -53.6378 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8242861a-6cdd-3712-8402-3aefccf4e8f3 | -7.80862 | -44.22252 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f49ae864-3ded-3713-a4c8-225ce8c724b6 | -4.74496 | -43.66744 | 2025-10-08 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f37a7ae4-4da0-3e86-850c-a153e5051b38 | -11.2229 | -40.47203 | 2025-10-08 04:38:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9a1231ac-73c9-31b8-adbe-ec25ba042ff0 | -6.45322 | -44.58374 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43edcd32-a0f8-37f2-a8db-4062092e414b | -9.66173 | -49.93969 | 2025-10-08 04:38:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab653674-0c9d-3062-9026-7c41bc5c8c9b | -11.46984 | -43.48676 | 2025-10-08 04:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cd90251-c727-3706-bf14-cd2252e9af1b | -9.77846 | -48.29176 | 2025-10-08 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9afdb2e5-e99e-3347-b9f0-c56babfb2bac | -11.22342 | -40.468 | 2025-10-08 04:38:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 551ba865-b7f6-32b9-9e2e-bd57c87ab87f | -10.36136 | -50.28411 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 845240f1-f79f-3d95-9799-d2edb5c1a084 | -4.86965 | -50.90317 | 2025-10-08 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bc2f575-d011-3517-9c98-395cfa9eee67 | -10.37006 | -48.13217 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 449f63f7-fd1b-3417-9be8-5d05402eca04 | -7.78212 | -42.40468 | 2025-10-08 04:38:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a147f5c7-816b-3a9d-b9ea-c4339062c2bf | -5.72626 | -43.61137 | 2025-10-08 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62577b6a-d11b-3fa3-ac94-1d0434663dda | -8.50617 | -44.21483 | 2025-10-08 04:38:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbe04383-4cef-314c-a58b-37110bd72fdd | -7.13839 | -45.92937 | 2025-10-08 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1245db0-1859-392e-80ee-e05894566c0a | -8.46893 | -47.20687 | 2025-10-08 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74b30c79-f9dd-3ffb-aced-f9d28dd3d86f | -7.35261 | -43.8629 | 2025-10-08 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2133f686-2f44-34f3-b98e-3e87e39f82a1 | -10.16344 | -52.62442 | 2025-10-08 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4d8816f-4c42-33d0-a650-0503821dba01 | -8.66646 | -44.71982 | 2025-10-08 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f48193e-bd7b-344b-921b-5ab11dcf93e1 | -8.99097 | -40.41988 | 2025-10-08 04:38:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6ca6ae75-d14d-3ac2-a132-cf7912fae285 | -9.45189 | -56.6569 | 2025-10-08 04:38:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70373189-8057-32cd-a608-f522b0d3453f | -11.05175 | -44.78643 | 2025-10-08 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76318cd9-d2d3-3534-9545-28b8aadea5a7 | -7.62711 | -46.55486 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf48f277-8e8f-38fc-ab2e-fcd269c7587b | -8.61953 | -54.99436 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d7a7da2-4deb-39ff-9fe5-448031702655 | -10.61922 | -48.65271 | 2025-10-08 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 733407c6-bd9d-3a8f-bee2-31300e649d1d | -11.05828 | -47.93378 | 2025-10-08 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63423865-fe8c-3e65-814a-fa7aa92421ec | -6.70992 | -42.14706 | 2025-10-08 04:38:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| db13cde4-a53f-3e81-8b48-b896c2ebe4a6 | -7.34733 | -43.86987 | 2025-10-08 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 962c06de-598e-3309-b56f-c01b77ccf4aa | -8.22273 | -44.19975 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abaed736-cf77-39a8-894e-1ddc3b8d03ea | -4.50544 | -46.35443 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4b9a13e4-6477-3d92-8fac-0747cac902f5 | -8.15786 | -50.16937 | 2025-10-08 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9abae2c4-48c4-3ebc-a3d8-c5981ffe7095 | -11.29751 | -48.26797 | 2025-10-08 04:38:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2bd8c9d-a28f-3c82-8324-5037efe44568 | -9.15903 | -50.56014 | 2025-10-08 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18bc89d0-02ca-3e5b-a6cc-02fdfc1273e8 | -9.18829 | -47.8008 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5567ce26-9523-3823-95de-77f0be241846 | -10.84048 | -47.55779 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35733d52-109c-3106-b1e9-ff457a6044e4 | -4.85653 | -45.79046 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35ef124b-e2cf-3710-9fea-a2ba5b1d5653 | -10.24219 | -52.69788 | 2025-10-08 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3fa26ec-2cf1-3d48-b2ee-b3daee69ba28 | -8.18855 | -44.1121 | 2025-10-08 04:38:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70e39a72-6b85-387b-bdca-26aa34dbdc9e | -8.67053 | -44.72021 | 2025-10-08 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c24da2cb-92a3-3c1c-9d5d-1a635eac74db | -9.4208 | -47.65115 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 276c2a2d-13d4-3e7f-85d9-9a090e925182 | -9.79077 | -47.74441 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1d54ee8-70d8-3f51-bba7-bce530d5b15e | -7.45659 | -43.03173 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 85f62bb3-388c-3ed4-aa4a-cbfe972feb7b | -9.32667 | -60.59745 | 2025-10-08 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25a8e1f9-9463-3569-8d21-0f47e8923351 | -4.96689 | -46.83651 | 2025-10-08 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b4d7d5c-d326-323d-9380-bc487d5b1cda | -4.42419 | -47.75771 | 2025-10-08 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa089808-97b7-3604-b1d5-2fcbcf39eb02 | -7.67503 | -42.40287 | 2025-10-08 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2fb1f620-380e-300d-a72c-ea473e5de1e6 | -5.72928 | -43.61964 | 2025-10-08 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4145cc10-5b1f-3e91-9623-d783ca9d3190 | -7.80999 | -44.24169 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29b14bae-a5f2-32f8-ab3d-ea873818211d | -5.13387 | -44.96929 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e938ad66-8c09-3b7f-900d-9b62db9582bc | -8.93245 | -46.59456 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d17f8b1-fe0d-372d-832a-04034c19e6c6 | -11.47427 | -43.48945 | 2025-10-08 04:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e05b461e-4f22-34ae-8479-f48fdc5709c1 | -5.9754 | -45.49104 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9f84e88-ba1f-30b7-a1b2-683415e53d66 | -5.23927 | -48.06057 | 2025-10-08 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 581dc196-6889-37f0-b4b0-d0ff463b2313 | -6.22557 | -44.33289 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bf297386-19c0-3115-af4b-12d6b8d9f625 | -6.71398 | -42.15217 | 2025-10-08 04:38:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3aa740f9-a87d-3b3a-9be6-9181eec3abc1 | -5.71078 | -45.68223 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da3b2b90-8d6c-3ac9-8ee8-2667d764f8a5 | -7.44072 | -43.14548 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 31b03cd6-b068-3dac-a9be-b8a375ab9de1 | -5.31874 | -45.25816 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d689448-e2da-313d-9b2c-1766b818858f | -10.42044 | -48.09676 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f1011ecb-d6fd-3e6f-a84e-df024588c03e | -3.75355 | -50.95005 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf801559-9646-3856-aa85-bc38cb54c990 | -4.50075 | -46.36161 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6365c933-afdf-36b5-a674-2ed4320873aa | -10.90365 | -51.01998 | 2025-10-08 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a0aaadd-24d0-33a1-8e52-c4c142b938dc | -11.77674 | -45.14714 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2bee8ed-b3bf-3eca-8a55-3053d897c1c1 | -11.81533 | -45.1334 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 309f8002-a10a-338b-923a-ff62654fe313 | -11.69715 | -46.37366 | 2025-10-08 04:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f79fa8b2-faa2-3e13-90f3-6eb9bb32966f | -9.24952 | -47.71617 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a09db1e6-8f40-35c4-ba66-f72cabb21b34 | -7.23363 | -47.17078 | 2025-10-08 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3acb14e4-f0e3-39d7-891a-5a6f7b28fb78 | -10.03717 | -48.29591 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8e03111-b013-3f72-8ec3-b513a66b95b0 | -11.79573 | -45.04268 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e5de9a8-91a9-3e0d-a598-dbf338f508e6 | -9.39445 | -45.9532 | 2025-10-08 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cf4c5b7-5b90-3372-8755-607f3cdce7c0 | -7.02669 | -49.52636 | 2025-10-08 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 833b294b-2981-3df9-8ced-aa62a7f1e003 | -10.46778 | -49.38811 | 2025-10-08 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0eec10da-bfba-36e1-887a-1c617038bfad | -7.29515 | -47.15181 | 2025-10-08 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37beb6d3-51ff-3889-af47-007be872a259 | -5.86351 | -42.78091 | 2025-10-08 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| eb3a1ce4-1bad-320d-bf8d-ad0a2d5c7d5d | -7.81627 | -44.14213 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d6dfaf0-b872-3470-ac26-336019300323 | -6.17407 | -44.68106 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README64.md)
