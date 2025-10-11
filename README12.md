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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 909872fd-6ad2-33a0-9cc4-b3733bc99b67 | -12.63381 | -48.31694 | 2025-10-11 03:42:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1d9d6772-6cbb-3f0d-a297-16d1763bddbc | -12.22002 | -43.79756 | 2025-10-11 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 299cd60c-1a59-34b3-ac36-205d50a5c1a5 | -13.38116 | -44.34663 | 2025-10-11 03:42:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e95fa8d-b969-3fab-9328-627c3073cf8f | -10.19073 | -44.61546 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06b8e662-e1bd-3868-86d0-7c790810a5d9 | -7.34769 | -43.86129 | 2025-10-11 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1870082c-9498-33ed-ab54-43703aefaa26 | -10.15294 | -44.5904 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1ad8db5-b014-3946-b696-f87ecc701d89 | -11.44874 | -43.47841 | 2025-10-11 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e870e0ff-a072-3449-8353-1a7cadaf8c64 | -11.75558 | -43.31601 | 2025-10-11 03:42:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 379a30a0-26d6-3b89-91b5-f357662448cd | -8.0423 | -44.11928 | 2025-10-11 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a44ce119-dac3-3352-a3af-02caf389e939 | -7.80203 | -42.40585 | 2025-10-11 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 65a6b89d-2aad-3501-a2c0-6294e1820368 | -7.45678 | -46.86596 | 2025-10-11 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a99f483f-d3a2-3e9a-b233-972b63a6a286 | -7.86924 | -44.45329 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aff8095-6929-3839-ba76-17c864dde04b | -13.20626 | -42.3356 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 91ae8de3-d1d2-3b41-8e88-92d9a9974b59 | -9.34184 | -40.33919 | 2025-10-11 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 50863663-0702-36b9-8bb3-c022439eceee | -7.65796 | -42.58521 | 2025-10-11 03:42:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c8b57865-e9f8-3577-ad7d-d0a494525fa4 | -11.74058 | -46.39539 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 052c5c23-f866-3c95-a515-6da508eb9a8c | -10.15161 | -44.55749 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fff0b6c-1c84-32bd-8894-e50396fb4db1 | -8.19981 | -43.32872 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 212357d3-6d5a-3fc7-97de-94d75ba4f7b6 | -13.37641 | -44.34561 | 2025-10-11 03:42:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aace05b4-d5e2-30b3-9792-caae80c54327 | -8.19762 | -43.32697 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 779bd77a-cd69-3949-8089-291df2d67b7b | -11.75891 | -46.3737 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cb7515b-61ad-3e91-b361-a6142db4818a | -12.91965 | -45.05643 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 505be9f6-f04e-3f8e-b9f9-ab97d83fb015 | -11.76103 | -43.3121 | 2025-10-11 03:42:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9838adff-4334-3c63-b0f7-a2252517db21 | -8.20845 | -43.3514 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f3701c31-f8f3-3946-9592-59cd84adb7b1 | -10.87405 | -44.18855 | 2025-10-11 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1ffa8b3d-956b-31e3-ae0f-3317069bc3ec | -10.19699 | -44.61032 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 264bef8e-8777-3f3e-9ce5-9a0f68f199bc | -12.2249 | -43.79739 | 2025-10-11 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2a41718-3d31-3c63-8c61-79f06339ab4d | -7.79405 | -44.1203 | 2025-10-11 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7530e0fb-aa52-3e6b-9a2f-0655acf65bf9 | -7.77562 | -42.42095 | 2025-10-11 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e74bfaa-1df4-37ec-b441-a8791cc2b5ad | -7.85927 | -44.47844 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fe25759-aac1-395c-bfaa-0fb42f780c70 | -7.85155 | -44.49099 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0ebd81f-5d21-3384-a185-e0453afacced | -7.85332 | -44.48114 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5552b601-9d6e-3563-ae5a-385e74a12685 | -7.79364 | -42.39944 | 2025-10-11 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9de26197-7e8c-3ef9-a439-3c4b3a9ecf49 | -7.52814 | -44.61357 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4f7429b-3eb3-37ea-9ffd-3e9dd9736825 | -10.65193 | -45.10142 | 2025-10-11 03:42:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec70cd6b-7366-3430-bc53-083557b9e5ff | -11.76045 | -46.3656 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc9a8d9f-b634-33b6-979d-f245bdbd1e95 | -8.08524 | -43.90714 | 2025-10-11 03:42:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 542e92ab-0b13-3ad5-b345-f6e1e1bf29b0 | -7.34878 | -43.85505 | 2025-10-11 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3f718c3-5c67-33c8-bc9f-dc1e03c8cbe9 | -7.41296 | -42.97833 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2b4b684a-c2a6-3db9-85ec-959c849725ad | -8.20545 | -43.33973 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 5c185bff-50f7-30ff-a351-871ed9dede03 | -11.84122 | -42.46991 | 2025-10-11 03:42:00 | NOAA-20 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26034f07-e241-30c2-af27-44437f0a5be9 | -10.87791 | -44.19515 | 2025-10-11 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f6c793f-9c72-3e34-8929-09141eb7eff9 | -7.66989 | -42.57201 | 2025-10-11 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6c375c5a-cc8c-3eaf-a604-b885b343474b | -10.42246 | -44.99736 | 2025-10-11 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 39d0338b-4781-3db7-ac84-26f5c309f822 | -11.76432 | -46.37577 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e95ca82-86e2-3266-98ca-894a82ec8d31 | -8.21934 | -43.37574 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6588d2e6-0114-32d6-a91e-a86b259dd423 | -7.41164 | -42.97816 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0c8e30c7-2617-3ef0-925a-93801b4f0e7c | -11.8771 | -45.4902 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e33a2bc-61fd-32b0-b74e-a8dbce025486 | -8.01229 | -44.4646 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2254f68f-92f4-38c3-831f-0a3e99efbb21 | -8.58182 | -44.89007 | 2025-10-11 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29446f43-a53f-3c5c-932b-593cbe46ee70 | -7.25302 | -44.09492 | 2025-10-11 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0749af45-a38c-3057-8152-c8933154b9ff | -10.16242 | -44.55626 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 213e3fed-f340-3d50-8ff5-2bfa30a95493 | -8.01006 | -44.45283 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f910bab9-19be-3313-837e-99da2b17e168 | -13.2076 | -42.35206 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51518acb-9e30-3fdd-9aa0-3d8dfadf816e | -7.06856 | -45.21565 | 2025-10-11 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54b589ad-2276-3fe1-90a6-da60606a696f | -10.15051 | -44.59284 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8ca16f2-b9a9-3690-9d49-2d8592ec594f | -9.33426 | -46.11148 | 2025-10-11 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 586e1608-b77a-3b9d-9f30-d0c4ce88d850 | -7.46388 | -46.86223 | 2025-10-11 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c6dce5bd-dd84-3d5d-a1e0-8ed18daff46f | -8.58069 | -44.8961 | 2025-10-11 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce09c25d-e423-3bf7-979b-fb7a39e63bb0 | -9.10199 | -45.02864 | 2025-10-11 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 348acd29-d4b1-3080-aa4f-a1f759c01985 | -13.21809 | -42.3419 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 71.0 |
| b69f2f8c-fe3e-3d9b-b205-10ad2e19a55e | -7.75016 | -44.21463 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b7f96e9-1544-320e-819e-8486c2bdb6a5 | -10.42184 | -45.00064 | 2025-10-11 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ebb6c397-dc07-3ea8-ad11-b8477032e7a9 | -13.46937 | -42.25014 | 2025-10-11 03:42:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0fc3111b-eb5a-30a9-870f-1cf8f630c151 | -12.99016 | -45.22663 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdc8664a-5b2f-3edf-8d7d-99ce002c8910 | -11.77237 | -46.38178 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f983362-e439-3c69-a714-8df1f45c55d6 | -11.75847 | -46.36396 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0fa99df-3e32-3a81-9cf1-64347cf6ea9d | -11.4462 | -43.47977 | 2025-10-11 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b772985-2e35-343a-a8e7-5ecb0434b71b | -10.8778 | -44.18965 | 2025-10-11 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c1e620e5-0192-3998-b85d-b36300d68bf8 | -7.40584 | -42.98276 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cb5e0148-65d2-338c-b1e9-b96e86b8a31e | -7.33061 | -43.86821 | 2025-10-11 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b2e82b9-8d7c-3c06-973e-8237efebede2 | -13.2132 | -42.34501 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 26a970ff-4677-3bcd-8c6e-4e479e2b1a29 | -10.15429 | -44.55518 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24566269-a3ed-3d63-a1d2-7604b2aa4de9 | -11.77875 | -46.37894 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03af97f9-9f7f-3703-8952-95757aae032f | -10.20269 | -44.60822 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ed35d80-4398-3483-8e14-75515e72f1ba | -11.44786 | -43.48335 | 2025-10-11 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77a30009-d707-3325-83e3-cfc329410627 | -8.20756 | -43.34142 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| d77163b1-7353-3817-ba9e-7958c18f0a29 | -7.85512 | -44.47108 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0529ff1-6fa6-3fb6-aed2-15aa9af795a5 | -8.08014 | -43.90632 | 2025-10-11 03:42:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ec21241b-21c1-339a-b303-db88264dc940 | -10.19132 | -44.61227 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0f5ac00-a181-3efd-834e-364efdbd3eab | -8.19371 | -43.32054 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 0979f8f4-dce6-3a48-a314-b83c5b682401 | -8.67985 | -40.4229 | 2025-10-11 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fe7c1fa1-742c-376b-a080-49e918b19452 | -10.13372 | -45.77049 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5297e52b-58c1-332f-bd07-06cf82ed9e7e | -12.91907 | -45.05944 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f78d5776-f5df-30d4-b7c6-c9efd2962300 | -9.3341 | -46.10747 | 2025-10-11 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 218b9f22-4f7c-3269-a94f-642de0183833 | -9.11036 | -45.04332 | 2025-10-11 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12acd005-48cc-375e-bebd-8cb4b550b950 | -7.40628 | -45.9197 | 2025-10-11 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ff653ee-2118-3494-afd6-516d5586b7e6 | -15.00969 | -41.8199 | 2025-10-11 03:45:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2ad3b392-74fa-3dd4-9cf3-a6d0e0c5f1f9 | -15.69011 | -46.63846 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2188445c-2d3c-33e8-90d2-b9a104473dab | -19.73335 | -43.92702 | 2025-10-11 03:45:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4df6cf36-5400-353d-bb4d-ec7f1c0dd4d3 | -14.95989 | -41.68974 | 2025-10-11 03:45:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f64f94f4-3d69-3139-b687-730b847d7f5c | -16.1298 | -42.72346 | 2025-10-11 03:45:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31acfb3a-4994-3e52-a92e-297ae38303d1 | -16.30778 | -47.14637 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7af3df0-48a9-32b1-ad24-6463700cc385 | -15.83169 | -42.02591 | 2025-10-11 03:45:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d1142c26-8495-39ce-8ffa-1eaccf8af15a | -16.30323 | -47.16837 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0a5ad48e-9918-39af-afa7-8ae43f63016a | -13.30708 | -47.12019 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 123f2b27-9541-3325-838c-99f66f5d686b | -14.94221 | -46.75088 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aa9be424-1fe0-38c6-9243-c896588c2ab0 | -13.25048 | -46.48662 | 2025-10-11 03:45:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f81559fd-ebd3-39e9-8bde-bb8c89028dcd | -16.83942 | -43.18398 | 2025-10-11 03:45:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6036334a-8b6a-35cb-a588-cc04324cf378 | -17.39805 | -46.86886 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README13.md)
