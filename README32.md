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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfff9700-fd19-32fc-97f8-e5b50eb32270 | -6.81271 | -43.34708 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 78e55eb9-d57c-3ebf-b4d5-9feae283d2bc | -10.8882 | -45.80676 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29a2efd7-16f8-3bdd-8014-bea0215a53a2 | -9.63047 | -47.81997 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a71a03c-77f7-38dc-af62-a24e1c62d290 | -7.95379 | -46.36259 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ab4a5e3-e913-3d0c-be5b-8b65ace4edf9 | -8.47636 | -45.17607 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94e8ca9c-f71a-30aa-9413-ac19acdb44fc | -6.29286 | -43.55669 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b2743dd-845a-3fdb-be48-7fcf32042f3e | -7.08719 | -44.34835 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 54b7cddd-f86a-37a6-9e3f-88819e7cbebb | -5.80445 | -42.55555 | 2025-09-01 04:10:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5cbce775-1114-3855-8932-bffc61ed388c | -11.3714 | -43.62782 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59f9deac-2883-3330-9fde-3ba84ea0fc85 | -5.32614 | -42.859 | 2025-09-01 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1972711d-7435-38c7-96fd-1594641dc5c2 | -6.8327 | -43.32672 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 1b02eb07-cac8-311e-9e25-c9b85cdc276e | -5.54746 | -43.74583 | 2025-09-01 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f246b103-2c94-3689-af41-f9e6ed421fab | -7.64315 | -44.77408 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c99e18ed-b4f3-3c06-8f4b-6275fa0e485e | -10.2368 | -51.1166 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d9398a3e-be9f-3d34-86b0-ac397c0d39c9 | -6.74611 | -43.78543 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e044f24-aa1d-394d-85b5-bdc899ddaab8 | -7.8806 | -46.98228 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 126cc660-cf88-3885-81bf-4fe8c6aea8b2 | -6.64434 | -44.26046 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dcfc1d1-ba64-3a7c-93ea-e818d031f754 | -6.418 | -43.96394 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07988024-85ac-352e-a367-6c1f0d6a3f34 | -4.7946 | -48.12469 | 2025-09-01 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bfd1025-433f-3b74-aefe-45ffbcfb3c05 | -6.2707 | -42.60768 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| adcd8645-883f-3ba1-88f1-bbd0b5a8da2f | -10.93602 | -48.24762 | 2025-09-01 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05a37686-5c00-33ef-97fa-94495c6d9048 | -7.57903 | -42.71017 | 2025-09-01 04:10:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f55dce49-bf9e-3a29-bedc-d8b33e8ee617 | -7.23553 | -45.42139 | 2025-09-01 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fb6b2e5-d5a8-3b53-87f8-fa9eaba6344d | -11.9134 | -46.44036 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19bd7a40-9a89-3e5d-a44c-64167841d0e7 | -5.96259 | -42.96315 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3f9bb5f5-2026-331e-9a69-172163fef315 | -6.63559 | -43.95803 | 2025-09-01 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c321d3b-71b7-36b7-a862-6a6e52c2eea9 | -11.87775 | -46.74253 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c4ac9a6-9e6d-326e-9216-f6d632439e54 | -6.14785 | -43.33319 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce8323ec-aece-343c-9d7e-8d1155e5079e | -10.57932 | -44.85089 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dee070e1-5589-3a28-9912-1ae420105cdc | -6.57259 | -43.70177 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dec54de0-c906-3627-b24f-e3425e534b78 | -5.73232 | -45.38221 | 2025-09-01 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65ec93f2-6f51-32ac-9f14-f6da798f3972 | -5.88106 | -42.99172 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 80833eb4-04e3-35a4-89ff-91496517ba7d | -9.02614 | -50.11889 | 2025-09-01 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17090d05-2e0b-3cac-ac71-1581577a4e7d | -6.14256 | -44.12879 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbd11bdd-3608-38fa-9ea0-b9940bab919f | -9.66935 | -47.82162 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0a0f0ebf-bc97-3ab7-b20e-010063d37297 | -6.82062 | -43.33617 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5405e3a0-a3d8-3e30-b3ee-c98cf2c95d53 | -7.06913 | -44.33364 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 10e063a2-1299-3d73-a3bb-2123ab5e866f | -9.66415 | -47.06064 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af6036df-7b7c-348b-bcbb-150000f822ed | -6.64791 | -44.26096 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be5ca23b-dcfb-35d4-8bc4-9366d66d2523 | -6.14501 | -43.32887 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f488dbc8-ecb4-395b-bef5-355345ecef4b | -5.8834 | -42.97703 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| daa2b7e2-66a3-386d-b862-f67efe7519cd | -6.30203 | -43.63218 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db2e2cec-0e62-39a9-a427-0ecd1000561a | -6.27812 | -44.49277 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fcf1580-8e63-3b82-8a8f-16940e7c6461 | -6.82182 | -43.32878 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dbf472e5-56c1-3682-936e-486e2e1a12ce | -10.7248 | -49.5719 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca1c7c6a-89e7-369e-b874-96112ea23746 | -8.9093 | -40.4399 | 2025-09-01 04:10:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c9d64fdb-02d1-307c-8bc3-1a2eefb8f5fa | -6.23753 | -43.38145 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fad78a50-338f-3d18-8a48-f92e8a990f65 | -6.81554 | -43.35138 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d4356a69-cba4-3039-8284-4076078f076f | -8.85507 | -47.22063 | 2025-09-01 04:10:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f97abe32-6c01-319a-b022-e9c45c4853b9 | -5.91773 | -43.4403 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83af3cb2-80aa-3402-ad7f-f76f8ecd931f | -7.7108 | -50.26544 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 635486e3-1739-3801-b3ba-9b6bf8432e1b | -9.63445 | -47.79673 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15d0d0aa-1b7f-3348-bb2a-4013fcc034de | -7.73868 | -50.25706 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a2f2b59-1bf8-3676-95ac-eb4e08127fa4 | -6.301 | -43.61644 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6b26322b-f50d-3996-8cfb-c60829c6d4d3 | -6.85732 | -52.81297 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d44d4f0b-4c84-31f6-9b20-d0a5ec77022a | -6.63972 | -43.95479 | 2025-09-01 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3034d54c-34a5-38c1-81a3-9b5341d2d894 | -7.08978 | -44.3413 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 57a96213-e5d2-35f0-9c87-58ac582dfdb9 | -6.34164 | -53.43963 | 2025-09-01 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 955639f8-5bd5-33e1-9d04-536ae429d24b | -11.06149 | -44.64566 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3cb5625-45d7-3a46-9cae-97312aa81a13 | -9.23941 | -47.06591 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d6fb589-71e0-36e6-ab5f-f0240eb46fbf | -11.89488 | -46.68724 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d41760f-559f-3976-998a-cc9126bab9ac | -6.37546 | -43.53848 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36f3ec0f-8039-3844-abbc-54a0529d1196 | -11.95711 | -45.84953 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a3c95b13-7f6f-3919-940f-876ce2534b3b | -11.38147 | -43.62951 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88244f36-6ef5-30b2-8e87-72a8f7e18eca | -7.10523 | -45.34657 | 2025-09-01 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79674f00-475b-3d95-8035-cc357deb96e3 | -5.93235 | -44.15033 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67aa9aef-b771-38be-9aae-9677c95cd4c2 | -7.10803 | -44.31069 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 71d3ad70-1876-3869-aee6-fa0b8bd029d8 | -6.82525 | -43.32932 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 133edbc5-7beb-3566-b740-6f62d5eb60cd | -7.67698 | -42.65691 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 802d9c7f-71a6-3c43-8a87-f3e4c50cfd89 | -11.37256 | -43.62062 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01684ca1-bf0a-31c6-b387-4cb2b2694289 | -6.47044 | -42.43193 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5146b4b9-2c2e-3ee9-b81c-e309218b2462 | -6.26763 | -43.53694 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f58cc533-535d-3028-b18c-e89d86aeebea | -10.57866 | -44.8548 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55237789-7b3e-3b75-8d7e-43dfc0f75abc | -6.36832 | -43.56049 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8e68b78-8ef3-3aeb-8c9e-0eaa13f4ab82 | -8.82412 | -47.8071 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14e487ce-f191-3f4f-901d-ec6db20242d9 | -11.37533 | -43.62478 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30c24a05-5643-3830-a452-0e3a7baac904 | -11.04557 | -46.89858 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27b8e1e7-15f3-35d2-accb-73099de65dad | -8.19331 | -42.29935 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96c76fe8-f894-352b-b97a-b16a174c2730 | -11.3752 | -43.64697 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3be9c2fa-450e-35a9-b3f4-f7e57c438b44 | -8.0773 | -49.94196 | 2025-09-01 04:10:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 074ede4e-4bf1-3001-a6d9-aabff7604d18 | -8.82906 | -47.80388 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d0ea695-1f23-3d3e-8379-cc421fcbabfa | -7.6297 | -46.54838 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 980a4f49-abda-319b-9abe-0f394b28d667 | -6.79966 | -52.81695 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88a88c36-2ca1-31d6-8de5-efef68c123b6 | -6.19535 | -43.33638 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 699d68bf-e34d-33d0-9ffa-ef3e93b97849 | -6.96002 | -44.33758 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83a8d656-be8d-36ad-8c72-49d37f34ac52 | -8.01334 | -44.05418 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1d0e0fe-5711-3049-916e-142adeaa6047 | -10.04024 | -48.12249 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbdd69f4-0efc-3f08-a455-23b9ba1a0925 | -11.89267 | -46.69469 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1e09687-f211-3bed-9f54-45ac9facc38d | -8.85915 | -47.22136 | 2025-09-01 04:10:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fe5cb3ca-af2c-3f0f-a3f8-54f09916e29a | -6.44518 | -43.95233 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bec0313f-2210-303b-9b36-bb5b4f8682aa | -7.08428 | -44.35283 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 28bcc570-b01e-3a11-ae95-f3660bc47474 | -6.24097 | -43.38203 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25847b24-f422-374d-96ca-b905b794a76b | -9.1457 | -47.94817 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6711c02f-e2fb-3891-bdc3-b46098eb9d47 | -5.99915 | -43.36344 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c9b27a93-4d4d-3f35-8266-d9a54d6fcb8f | -11.84997 | -46.79089 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c47d249-b225-3f5e-b9b2-1fae33d25008 | -6.54057 | -42.97219 | 2025-09-01 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9568844a-908b-3c32-bbde-b128e6a142dd | -6.76229 | -43.77906 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 49479218-3d38-3dc6-9e2b-dfc659218310 | -7.55506 | -45.94333 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6dde22a-d7c0-392f-b904-a7074da8f4a5 | -6.10016 | -43.19199 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d289f7b0-9ad0-307f-b728-e21097bd428c | -11.03891 | -45.14972 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |


[Clique aqui para ver as próximas entradas](README33.md)
