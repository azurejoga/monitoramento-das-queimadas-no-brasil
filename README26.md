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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ff2f1e8-fb2c-390a-9295-a2ee4b990cde | -4.28713 | -45.48207 | 2025-10-19 04:10:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e643a79-cd39-31c8-b44d-c5b36983c493 | -4.8292 | -43.0634 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8ab95da-857f-3ad5-8112-4c7bc177fd8b | -6.38731 | -39.74287 | 2025-10-19 04:10:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6975dc60-6415-3ae5-b738-b569c3f4a47a | -5.93354 | -42.25344 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f58dc8d4-1396-33ba-b276-5caefb7ea76b | -6.19215 | -41.56607 | 2025-10-19 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| eabab1c5-364d-3b78-9837-3d109a1c77ac | -3.11804 | -49.2196 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0c466f3-57db-3471-acd9-80728b042fc3 | -7.18825 | -42.21965 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 11b5ae1a-db9f-3423-ab62-a4d3b02f981f | -3.82028 | -48.65082 | 2025-10-19 04:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50ebb6a0-8666-3207-a406-bb722e45efc6 | -5.9987 | -43.11022 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 690da824-291f-3db8-8630-1452e6387146 | -5.36699 | -45.92847 | 2025-10-19 04:10:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4ccaa35-c997-3deb-b801-e171988ff09d | -5.67305 | -47.98978 | 2025-10-19 04:10:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be09a6ea-420e-3125-bbd8-11805cdf7f13 | -4.14375 | -47.66063 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44858613-36db-34ff-bb56-d12354616ab4 | -3.4702 | -47.68821 | 2025-10-19 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46f023a0-3081-30b6-bce6-51847a667497 | -7.31489 | -42.46262 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f66b4a5f-a516-3916-8c06-9642c43b6ea4 | -6.96368 | -39.64012 | 2025-10-19 04:10:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fa8ebbca-11a3-39f6-9d69-2676b3ed1e49 | -4.41399 | -43.95988 | 2025-10-19 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71f27460-f955-394e-a5b1-a8b5db411c18 | -4.2428 | -44.67431 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a819aadd-e513-3240-a175-ec13f583624f | -7.16216 | -42.36247 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 55da225e-9cf5-32fb-bb56-0795d6ca086b | -3.2144 | -50.21609 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc14d2b1-71e1-393a-b494-ceb2e6e933da | -3.59455 | -43.0475 | 2025-10-19 04:10:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b60079ca-4f7f-3185-9dd2-e757570f8000 | -7.41295 | -40.07861 | 2025-10-19 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a5471f84-9ea0-37ff-8a16-2d2987e9af85 | -4.42395 | -47.75232 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bf7d06e5-83c8-3608-8530-ea712daa20f3 | -3.83983 | -47.39755 | 2025-10-19 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68e6edcc-35d2-3b65-9562-fdca4236ddbd | -5.04482 | -49.64827 | 2025-10-19 04:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8925fd7-bc2b-3bf3-92d9-77423ee8ce26 | -5.8308 | -42.26266 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5b9cc06a-d9f1-3d66-b1cf-c37a330bf233 | -6.12905 | -44.2158 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae6f6920-306c-33b2-b909-ac4697416d25 | -4.82577 | -43.06286 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d27b5582-bd33-3bcb-b54e-d43c6af7090c | -7.65677 | -44.63311 | 2025-10-19 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6383957f-c33f-3b04-80f9-f3da9725ed96 | -6.44113 | -43.91832 | 2025-10-19 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 992c034f-3940-3e24-a8c2-69e3f6a7bdc9 | -4.28139 | -50.54443 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0cb748a-862a-3aa9-a367-f33021c23935 | -6.2505 | -42.32555 | 2025-10-19 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a4b02d3d-5496-3ed7-b7a5-d453fa68345f | -5.77255 | -46.5696 | 2025-10-19 04:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e815c6d7-8068-33ca-be97-908bc7538737 | -6.42019 | -43.91485 | 2025-10-19 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d5ac5753-2bce-313a-99bf-52427c940b64 | -4.21594 | -48.36187 | 2025-10-19 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4004635-9a2d-3557-a198-8db86f251068 | -7.18492 | -42.21912 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 23b3fa6a-9005-368c-80c6-19871e995850 | -7.74267 | -42.51688 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3926abe-2f73-30d6-8c26-d69f4aaa1170 | -4.58738 | -46.29672 | 2025-10-19 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bc853b7-b467-3245-ab94-528e6d894e51 | -5.55456 | -44.95457 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 99f75a39-4db0-3465-93c3-482fa0abd09f | -5.31554 | -44.84897 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cefd6935-9684-3a98-ad23-653369cb745e | -4.41755 | -43.96049 | 2025-10-19 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c9da19c-c3a1-3440-82e8-119c41126370 | -2.25036 | -51.91457 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c59b399b-9f53-3127-b48f-0da7a8c8a708 | -8.10886 | -41.0986 | 2025-10-19 04:10:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b62d5f19-7ee4-3b61-a865-630128c3ccfe | -4.78602 | -45.29854 | 2025-10-19 04:10:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d425ee5-317e-3db6-87c7-d65c7cb39941 | -7.02171 | -46.80473 | 2025-10-19 04:10:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b76e15be-5a80-3d37-88da-5867f678c4af | -6.70852 | -46.02654 | 2025-10-19 04:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bd6989c-7434-32d9-9a98-754cd1361ed4 | -5.37094 | -45.92904 | 2025-10-19 04:10:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc11eafc-143b-3993-b2e4-16a09ddf6f20 | -7.5871 | -43.0698 | 2025-10-19 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 974f6ae6-1cc4-3bd1-897b-39c4e0885947 | -7.76939 | -42.478 | 2025-10-19 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8e260d82-0434-340c-9887-08bee7858e04 | -7.16549 | -42.363 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 18a7e96d-66a5-32d3-8226-cf2560232aa8 | -5.27644 | -44.69617 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42f55b1b-9c99-37e6-88bf-d47dc13182be | -4.27115 | -43.61208 | 2025-10-19 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b03a0afb-d93a-30fc-9d13-195eca2222b3 | -7.33703 | -43.86688 | 2025-10-19 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 38fa392b-14c6-36c7-b1f6-32ed2b05d3c6 | -4.31555 | -43.02155 | 2025-10-19 04:10:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6dace8ea-6107-37ce-b172-94f6893d5cbf | -5.30837 | -45.0102 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d5efa6d-1791-3f37-9b83-0bd7d6c92d25 | -3.46943 | -47.69296 | 2025-10-19 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1cd70bf9-60dd-32f8-b003-27fc4f6c0987 | -6.00587 | -40.22381 | 2025-10-19 04:10:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bb025c5e-b7b2-3e47-a2f9-a4dac799895a | -4.13922 | -47.66003 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb2852c3-5700-3d38-a074-d22107cdf1b4 | -7.20146 | -42.19343 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 23da2a28-4f2e-3449-b136-d2cc69714810 | -7.49871 | -42.13687 | 2025-10-19 04:10:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cfca26e5-960f-3d11-a43b-806d93b53815 | -6.72168 | -46.3945 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8582fb5-75d3-371f-8fc0-1254138f6d35 | -4.14462 | -47.66274 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b077eaa5-20ea-38c8-9b42-afb7ae4d7619 | -5.92767 | -45.45047 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82619c45-30cc-3635-95ef-28b160060ed6 | -7.19812 | -42.21437 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fa745227-a105-39f1-b38a-dde738924c35 | -5.55316 | -44.95179 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c0b4df4-cffd-367b-9f44-6c2cbf2339ac | -7.15937 | -42.38001 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9986bc40-2f30-3764-a4e1-b7f5fc00a8d4 | -4.58465 | -45.64594 | 2025-10-19 04:10:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76d10198-64d7-379d-a16b-a094895152c6 | -3.89111 | -52.40513 | 2025-10-19 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ccd625f-9867-3598-8e77-8dfb11a10152 | -4.91872 | -45.70761 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56ced061-042a-335a-a302-84a8bb52a026 | -6.78999 | -46.47448 | 2025-10-19 04:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29019db0-f892-3012-b93a-ea94eca0937c | -5.71382 | -43.81789 | 2025-10-19 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3db25174-460a-39b4-a0a6-f624e7d98e9a | -5.60422 | -42.67693 | 2025-10-19 04:10:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 74043e34-69d6-3a64-82e4-27f3610809b7 | -6.53121 | -47.57179 | 2025-10-19 04:10:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d2046bb-8af5-3cba-b15b-63531312a90f | -4.15137 | -47.67752 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1e821b47-62e6-342f-be4e-f1b89ec333e7 | -2.70067 | -49.54403 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72444fe1-373d-31be-848e-94d46e00bfd8 | -7.49594 | -42.13285 | 2025-10-19 04:10:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 746d50a3-0155-3567-8e15-cae5f7b2273e | -7.1666 | -42.35603 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a01b24f1-efa9-3834-8529-c1c48d93488d | -6.09899 | -44.02441 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5788179-b7bf-36f6-8b59-594caa1888e0 | -6.25329 | -42.32959 | 2025-10-19 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 18e5c6d4-9f3d-3b0c-8759-3a24d5db69da | -4.14896 | -47.65696 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8d83c30-f595-3c70-9e5a-d3a615c9582a | -2.59538 | -49.49832 | 2025-10-19 04:10:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2949bb5e-a4a2-34b8-a061-23642824551f | -6.31219 | -44.31395 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd1bf88b-7c53-3dc3-9e83-ef211ebd1355 | -4.46475 | -44.97242 | 2025-10-19 04:10:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72ba31b6-0e37-33e2-87f8-65e564999615 | -5.3528 | -47.21788 | 2025-10-19 04:10:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25e09f15-4e98-3743-81ed-3cf855364fa4 | -7.18547 | -42.21562 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bbda9b82-925c-3824-bebe-05b0b1be57f3 | -4.14826 | -47.66129 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23d5a23b-83b1-38b7-b096-140fb73757c4 | -10.8429 | -43.94005 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dc41f47-c7b6-3168-9d33-1b393954248e | -10.73707 | -44.35467 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af998a63-82b2-30d6-8770-f070a6bdba4f | -10.67714 | -47.42673 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bb347a0-123b-3bd4-8fa0-0c1a3e0addbb | -9.67962 | -44.55675 | 2025-10-19 04:12:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff87372f-1f8e-31cc-bbd7-bbc566af6bb3 | -8.23626 | -43.3173 | 2025-10-19 04:12:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24a8c76a-2cff-3e15-a371-800011806c40 | -14.2818 | -42.33142 | 2025-10-19 04:12:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d1239172-9ee4-3ebf-a088-a373d58c9f8d | -10.69273 | -44.54033 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 483e870f-7d97-3b7c-a101-946426fe17e7 | -10.53394 | -44.50227 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67d58c0e-a5fc-377d-a2b1-7e90da3843c5 | -10.132 | -44.52685 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a286a0b7-31e8-308f-9649-4add483912ec | -13.89103 | -45.51349 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ce49aa1b-1d3a-3f81-84a4-aeadb96f6626 | -9.21534 | -46.06289 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce177b26-7b75-3a0c-a92b-a67012f058ea | -10.85364 | -43.93806 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63410253-c8f8-3b89-8f55-1f69d152688d | -9.67615 | -44.55616 | 2025-10-19 04:12:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0ea24283-e902-3e7d-a0d6-67251c478062 | -8.22451 | -43.30425 | 2025-10-19 04:12:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c8bcc8b-da32-3747-a9a8-8488233a9023 | -9.98494 | -47.05187 | 2025-10-19 04:12:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README27.md)
