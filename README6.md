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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5df1b7bd-3484-3d88-93d6-20083e4ef8b7 | -15.35579 | -47.97232 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9ce7b898-29cf-38dc-a63e-e53c3ceaed49 | -12.29022 | -49.20338 | 2025-10-05 00:33:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8ab5a9c5-70e1-352a-9aa9-0c4ff5d528f0 | -14.88941 | -48.27375 | 2025-10-05 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f7903ee9-315c-319a-a83b-4e263675f114 | -14.80289 | -44.90458 | 2025-10-05 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f9ea307b-9470-3ff8-8766-0309d240dfa5 | -12.28898 | -49.19409 | 2025-10-05 00:33:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3dab9455-3db7-31e0-9a4f-ae9b16a1c515 | -13.64814 | -47.29078 | 2025-10-05 00:33:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d0863411-ed06-326e-a41b-c8c713d8ac66 | -10.80193 | -48.82673 | 2025-10-05 00:33:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1deeac52-0ca6-39b7-b8ed-ad30941783b5 | -15.44482 | -44.28885 | 2025-10-05 00:33:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 7834b73a-ba44-3706-8c0c-1cc7553c5c71 | -13.14648 | -47.98212 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| efe047c5-02a6-3949-ac91-58e416435145 | -16.07933 | -51.06787 | 2025-10-05 00:33:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ff46504f-afc5-332d-b6f4-26c2ab5075e2 | -13.91949 | -48.17896 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 907e8f09-77ef-3e88-bfd3-c3986aab9605 | -14.6622 | -48.35698 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8ab2427c-b351-3d86-b794-a0bcceb3e134 | -13.27161 | -47.62075 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 6381a618-6dfc-3aa4-a1a1-6988868ba057 | -15.3261 | -46.37606 | 2025-10-05 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a0ba43cf-8cc2-3bc2-91df-8777cbfc875e | -13.1161 | -44.08541 | 2025-10-05 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 713347eb-d517-39b9-8023-d60ac1882f5d | -13.5195 | -47.28853 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| db4d0434-b6b2-3a89-b98a-c3abeca38473 | -11.85188 | -44.93318 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c9d9cb5e-7854-3230-bffd-43f49dad695a | -10.81076 | -48.82545 | 2025-10-05 00:33:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2d81b790-b4bc-3c18-b10a-33e073f0e1ea | -13.16213 | -50.89078 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e0052fc4-90e6-36b6-92e8-2b9aa405dfb1 | -12.40291 | -51.10535 | 2025-10-05 00:33:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6ae7dc6f-dde5-37ed-afa8-99430cb3ef07 | -10.39346 | -45.3889 | 2025-10-05 00:33:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ceb8d84c-7a26-3783-ac2c-9dbbd024fd9a | -12.27116 | -49.20247 | 2025-10-05 00:33:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 11337362-0fe9-3ac1-ba66-f3961618da9e | -11.05257 | -47.78097 | 2025-10-05 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 998fafa9-7ca1-33e8-aae4-cf331491a390 | -12.99867 | -43.99355 | 2025-10-05 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 68883405-4296-3aa2-9661-bc8a0516b1bd | -11.86694 | -44.96013 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a0fa25c6-7ab6-3f11-9889-ebfe6080b3fb | -10.39692 | -45.41211 | 2025-10-05 00:33:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 6c52f7a3-adcd-3f07-9a72-343831deb8cb | -11.85531 | -44.95042 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| addfc7ee-8557-391f-bb1c-164220cdda4b | -12.706 | -45.86061 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aa3ece2a-3177-3b60-9e2d-646c1161f584 | -13.45152 | -47.26761 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 83282768-d226-31e9-a739-3b6d544f2262 | -15.5257 | -46.87743 | 2025-10-05 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 45197527-c502-3220-b8fd-9f3989710883 | -13.86088 | -43.98976 | 2025-10-05 00:33:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 20c07cc2-9714-3a7e-9173-a62fd1cea151 | -15.91006 | -48.8181 | 2025-10-05 00:33:00 | TERRA_M-M | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a23b5781-fb2c-35d2-8f11-8fc1967f1d6a | -11.23781 | -47.78729 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3085084c-d3e6-335a-9e55-1d445af78f02 | -13.74234 | -47.96811 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 909bd570-0dc0-393a-8340-6d4dbf196e29 | -13.28798 | -47.60909 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 21aedecb-6a3c-3e98-b570-307e136e1a6a | -16.26801 | -47.10677 | 2025-10-05 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7584c00e-233e-32df-a77a-5182fe5c6fa7 | -10.67955 | -49.27966 | 2025-10-05 00:33:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fdd79ab9-f44d-393b-8073-c2718a3a141f | -10.60185 | -54.37231 | 2025-10-05 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 3007127e-356c-33f5-bb05-8caf808e4653 | -11.76175 | -44.7416 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 8c26e60f-21d6-3726-a39d-7369593496bd | -12.82323 | -46.86592 | 2025-10-05 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3cf10cd6-09dd-3225-b16d-7902a8ac4031 | -9.95538 | -48.76633 | 2025-10-05 00:33:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b554af07-13d9-3f22-bd5d-4310b2b10cce | -13.31885 | -47.17331 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8d470d0c-492c-3027-bc27-3c57f06391a4 | -8.8577 | -46.80288 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dd9a7c8c-a9a0-3d99-a52f-0b276b08ad07 | -10.45695 | -57.50019 | 2025-10-05 00:33:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 9b43aa28-40eb-3dfc-b525-f61123b498b5 | -8.79516 | -40.58318 | 2025-10-05 00:33:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 9c7a8b1f-a287-3c80-a60f-12f679d8e53b | -12.47011 | -45.50896 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e51f91db-0a5a-31d4-a4b2-195a596c1914 | -9.95415 | -48.75745 | 2025-10-05 00:33:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 68ddc345-e6d4-3366-b145-2ec890bfe624 | -15.55618 | -46.96616 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 78f97a2f-2ea0-3c64-8751-7f3c14a4934f | -12.26584 | -55.12268 | 2025-10-05 00:33:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| b6500ce7-0d9a-3a3e-8c40-239bfefad8fa | -13.91314 | -48.19851 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2eb17389-b86f-3020-8d4b-7e5f493abb2f | -15.30555 | -47.94868 | 2025-10-05 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f4823a2d-33dd-39d4-9696-a14f1467e36a | -15.13735 | -49.51411 | 2025-10-05 00:33:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 51.9 |
| bff0adc6-0c66-377f-9bf7-cff53f68c93a | -9.05962 | -46.9897 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b4919f27-6b7a-3bcc-91fc-ad92edf9173c | -13.081 | -47.91553 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 91693f2d-285c-346e-826b-7d6eae055e71 | -15.8545 | -46.26611 | 2025-10-05 00:33:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 31405963-9e22-3c64-ad08-ab34b7a9353e | -14.67996 | -48.35432 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 4998f7a9-f670-3119-8967-971de271eb4b | -11.67517 | -43.89536 | 2025-10-05 00:33:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 1a03e8ad-a60b-31a0-a070-798a78de14a3 | -10.40504 | -45.39912 | 2025-10-05 00:33:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5ca91f56-87d6-3f86-be8c-4d23eaea60f8 | -14.93077 | -46.83709 | 2025-10-05 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c841f39-9ef5-3cd9-938a-dc246eba0a94 | -14.8732 | -48.15448 | 2025-10-05 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bfcf2082-068d-3dee-be1b-6500d4b38453 | -15.40004 | -47.9658 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 829f9195-dd7d-321b-bd34-a43454da59ec | -13.30624 | -48.08149 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3b7522a5-dc4b-3af6-a0b1-6ac27a094896 | -13.25497 | -47.84089 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5568ee7f-86fc-399a-9a58-2b0aebcb5bbd | -13.45406 | -47.28569 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ea1fcbeb-e02a-3c52-acdb-50d0f404e78e | -13.73227 | -47.96037 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 832bbe24-f7b0-3f67-90db-0c8090aed8a0 | -15.11513 | -45.75216 | 2025-10-05 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 53f3b787-1d77-33b0-95c4-e7ab6953e321 | -11.81801 | -46.86657 | 2025-10-05 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3eb53d9e-be8e-303d-8811-9d32361b9c4f | -8.56774 | -46.27581 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d20b286d-9014-388d-9413-068f08b23f8d | -14.67646 | -48.26145 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58d1e5cd-6f9e-3172-af50-1acc90fc9820 | -15.3068 | -47.95784 | 2025-10-05 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 760d9a87-29c1-3b97-9e03-db6769d2fdbe | -11.10732 | -49.8576 | 2025-10-05 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7de30b0b-7b7e-3bac-9993-e973a4b752f3 | -11.67716 | -47.49204 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ea25e2d4-8f87-3785-9c13-b1422d306386 | -9.9799 | -48.02079 | 2025-10-05 00:33:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 076d1382-f8dd-36ac-bb47-436a4a2342ab | -9.29572 | -46.00803 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b7f936dc-3554-3a10-a138-4214cb8fcf11 | -11.48679 | -45.0267 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 217732a3-e16f-3949-8175-b4d167e1c3ff | -15.71378 | -46.25258 | 2025-10-05 00:33:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5fa503ee-8d86-3ac2-b66f-245250613967 | -10.57675 | -48.72546 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3f09edb1-f011-3c3e-b2b8-e11ee2d703ee | -12.82058 | -46.84735 | 2025-10-05 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bb00d3e5-5140-32a0-9cd1-307fc0040bac | -9.15555 | -50.06299 | 2025-10-05 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1d6830d8-8c9d-320d-bbef-82db26ab5c79 | -15.23734 | -49.30291 | 2025-10-05 00:33:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f0b13cb6-f085-3237-b5c3-1d9a13278dca | -12.24965 | -47.83636 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8d8c867c-1cab-3beb-8b5a-7c06ecaf36e7 | -10.45877 | -47.81307 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3a5481a1-2ab8-3a1c-9b7d-23341bd3e4bb | -11.45666 | -49.71658 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d812ba38-dd7b-3ba3-a0df-e3d85e5fb708 | -11.4412 | -43.49661 | 2025-10-05 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 183c88f8-616b-3717-a6b5-d8a2bc2b1b22 | -13.34973 | -47.58495 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 26.9 |
| d9bdf635-d1d4-3a96-be09-fce66f681e55 | -8.57389 | -46.31767 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b43ebe9d-dd80-3f19-b77e-0820b75638d6 | -10.3952 | -45.40062 | 2025-10-05 00:33:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| e81c7e67-c28a-3cdb-a5b1-e60d225d9c0c | -10.46712 | -57.49237 | 2025-10-05 00:33:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| df762cf1-9598-3d4f-9578-934ad259aa14 | -13.50056 | -47.28223 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e36e6c76-dd81-3e49-8e95-bdb18506f6e4 | -15.50416 | -46.85268 | 2025-10-05 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d380f89d-ef17-31ab-ab86-065681ec6840 | -15.2281 | -49.2899 | 2025-10-05 00:33:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 985d07ce-104b-32c1-9aa7-908f0f0179c6 | -13.25233 | -47.22649 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9beb1c26-2416-3613-a91d-f6b2bca610a3 | -14.27619 | -45.87636 | 2025-10-05 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9b12af4f-4ba7-3a91-8744-7435eca4fa1a | -12.99282 | -44.00027 | 2025-10-05 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 09b2fdf9-1048-3ba6-aae2-89e99c37b9fc | -15.98837 | -50.9064 | 2025-10-05 00:33:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9b841a96-c0a7-34eb-8396-64655fcb4ba0 | -8.56622 | -46.26547 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| b692f572-52df-34ff-bae4-d1b60af95dd6 | -8.86478 | -46.8521 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| caf52e30-b5c0-3324-b117-5bf6be5c5767 | -13.35855 | -47.58365 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c1c9308c-472d-38dd-8396-6e91d287afc4 | -14.2541 | -46.10804 | 2025-10-05 00:33:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e3e0bd1b-adad-302b-b542-74c8cb81a337 | -12.46217 | -45.52103 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 218.8 |


[Clique aqui para ver as próximas entradas](README7.md)
