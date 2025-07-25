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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3df59785-32e4-3f8e-b202-99000b6f8292 | -12.25509 | -44.58406 | 2025-07-25 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e2e2bf3-0a8e-37f6-94be-e5c9253bd599 | -15.59998 | -46.52851 | 2025-07-25 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7adfa3e0-9382-3f9b-9ecf-d57a29c8760b | -13.7135 | -45.67507 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9248e4ae-681c-3f4f-8d5f-325bae4deda5 | -15.26934 | -47.1414 | 2025-07-25 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d96e2ce-133d-36c1-b1c4-29bf2a239a67 | -13.71184 | -45.68579 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97ae4f47-fd28-33ea-9a41-a4f3f768c4c6 | -14.94641 | -46.98076 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a78d992a-3498-3bfa-b30a-507b26bfc8ad | -16.6168 | -43.36099 | 2025-07-25 04:23:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a54a3cac-ae4e-3851-a016-23b698e278e2 | -13.40428 | -46.80524 | 2025-07-25 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 318a9295-4225-3cf8-89da-3c53f15d33e5 | -15.56785 | -44.75931 | 2025-07-25 04:23:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d9da0d6-6033-3f60-ae59-933fb3e891c9 | -10.04737 | -59.10443 | 2025-07-25 04:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c1a7047c-372e-3075-a8c2-4a14a7486ab5 | -14.95191 | -46.98905 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3df6f70f-ed78-393c-97ca-e6599e62def6 | -12.73553 | -46.98776 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 761f733a-e5bc-332d-851a-ae73727a8272 | -14.65171 | -46.83307 | 2025-07-25 04:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b39acd69-f4c0-3783-a64f-0f7f11ae5d61 | -14.95696 | -46.97877 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49951315-bfb5-3e28-ac8a-085fd603d5d8 | -16.0915 | -45.17025 | 2025-07-25 04:23:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d11df22-83a5-33b1-a1fa-2e7facffcada | -14.3077 | -43.79638 | 2025-07-25 04:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c153ed8-5a82-347d-a4ef-030115857714 | -12.42878 | -45.37541 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d602a642-21d1-3b48-9e77-d7223fd1c00f | -13.64845 | -46.82035 | 2025-07-25 04:23:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5e51a35-7c48-31fb-b7e8-93e95682f450 | -13.7003 | -45.68061 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23ca976f-be69-3996-93c9-e6f7da93eea0 | -13.71627 | -45.67918 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0cb2a33-93c3-3ca9-90cc-3ecaef8aea5c | -12.04477 | -45.42639 | 2025-07-25 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc3b5691-b4eb-34bd-a2d8-d0e298145325 | -13.70961 | -45.6781 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db1c0b12-4a84-3644-9071-ada2d78e9f8b | -12.70267 | -46.97872 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b5b0cce-1894-3c6d-a8b3-b8e9d73213fb | -12.65593 | -45.04065 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cc59a29-7337-395d-a7f9-a0bb52ffe2b5 | -12.04699 | -45.434 | 2025-07-25 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3459cf05-31c4-3ff7-bff1-c2c333f6995b | -15.59062 | -44.53607 | 2025-07-25 04:23:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91dc7414-d100-35f2-8dcb-af9cec9fde2e | -12.25325 | -44.7778 | 2025-07-25 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1574c50a-08da-3909-8c45-901177a8eb5f | -12.70209 | -46.9823 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f34ebdd-f720-39d4-aaef-687a23a5fa3e | -11.87708 | -48.62072 | 2025-07-25 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2186eb6-34c4-3516-a962-a124aaa0f2c8 | -11.9487 | -58.76088 | 2025-07-25 04:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d08a30df-631a-3691-aa27-a0431d191d90 | -13.71239 | -45.68221 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d79ffc6-457d-3b23-87ae-76d0c638d3d1 | -14.3071 | -43.80043 | 2025-07-25 04:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a755025b-adc2-359a-b5a7-d5ddeab69e38 | -12.69759 | -46.98891 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42239476-84de-388f-92ce-a77af2dc6157 | -15.59778 | -46.52079 | 2025-07-25 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c5c1b99-1273-38f7-9ba2-3647d19bdaf6 | -14.59716 | -52.5259 | 2025-07-25 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17e198b2-855a-30f5-9c0c-42334b54d16d | -12.73219 | -46.98719 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17b497b5-e448-30e3-9780-e8b9526a891c | -12.73611 | -46.98416 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 558b4e99-6ce7-3005-b4fb-14809d80cfc0 | -14.94308 | -46.98022 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d6b8316-e7bc-3343-b239-c5325cc75201 | -11.31571 | -55.21778 | 2025-07-25 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dabbba9-2995-3c83-a7bc-60c9dd7049f0 | -16.60446 | -47.96968 | 2025-07-25 04:23:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80dc0234-0207-3ab2-ae4f-ef87c5955c95 | -12.7296 | -46.30426 | 2025-07-25 04:23:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3856253-a8bb-327a-9eca-70e51eb34c0b | -12.69979 | -46.99662 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a14e8e4-a3e9-394a-8b21-a246be1f8e5f | -16.81758 | -47.59883 | 2025-07-25 04:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94b942b9-4791-3abc-ad52-5c644757bd60 | -16.69472 | -41.01671 | 2025-07-25 04:23:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 62633588-16ff-3737-959e-103e73d27cf2 | -16.60781 | -47.97026 | 2025-07-25 04:23:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1ed2a54-b783-3d8d-ab00-c254ba3bdd95 | -17.34566 | -45.70597 | 2025-07-25 04:23:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35fb2643-8bcf-3fec-b4c5-985ccef7f41e | -17.68775 | -46.84428 | 2025-07-25 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f5b5b44-1586-3061-ada4-8b0f0d4f41e0 | -11.31504 | -55.22124 | 2025-07-25 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47eae4a5-b444-321b-9d0a-713333a0901d | -14.17057 | -45.34972 | 2025-07-25 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 448a2be1-3083-3da5-99a6-fcdbf0fe66fe | -13.69919 | -45.68775 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a421b96b-04e1-3d37-9481-c1b500b23a6f | -16.56084 | -49.05538 | 2025-07-25 04:23:00 | NPP-375D | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4cae55d6-ce26-3d94-867d-e9ee582dfd8a | -12.43434 | -45.38359 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d80c28a-6f65-3f1b-8aab-224fd1f0a839 | -11.94737 | -58.76735 | 2025-07-25 04:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f04bceb4-24cd-3006-8533-f3e52d76a61d | -12.25551 | -44.78558 | 2025-07-25 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db51b17c-c3ff-3e45-a492-e4281bb8b201 | -15.04929 | -47.68649 | 2025-07-25 04:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 637bb47d-0dd1-3f7a-b45b-9f0c4b164748 | -15.33778 | -49.42397 | 2025-07-25 04:23:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77e0a758-2d8f-30e7-a1f7-541a2c50e99c | -14.17336 | -45.3539 | 2025-07-25 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9fce342-fff1-3567-a280-158d6e53503f | -15.27494 | -47.12773 | 2025-07-25 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d882e04-5570-39d0-a7cc-428e2e3f3c90 | -13.71683 | -45.6756 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b6ca6ef-a1de-3c7b-bd04-a3335ecd4607 | -13.71072 | -45.67095 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d465417f-d34c-3cb5-b8ad-c8eda7b36d18 | -13.64902 | -46.81678 | 2025-07-25 04:23:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d23c2687-31f2-3f96-a2ff-012c85dff991 | -14.17001 | -45.35336 | 2025-07-25 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc9642a3-26c1-37fc-a3ea-8b7c9531265c | -10.62843 | -55.30878 | 2025-07-25 04:23:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09312214-e3da-386c-86ae-f4bc823c03f0 | -13.70696 | -45.68169 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3908e821-9c7b-3c10-b31f-8b305907b9c4 | -12.43156 | -45.37951 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2132a89c-5076-3f48-8212-f878ee438bfb | -14.95523 | -46.98961 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9efbd58f-7a2f-3013-8e08-95153fea0770 | -12.69817 | -46.98535 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b409068-3744-3f26-a01c-645c3e6f114b | -17.70155 | -44.30686 | 2025-07-25 04:23:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d3e861a-85be-3036-bfd3-ddc8418e805a | -12.26241 | -44.58144 | 2025-07-25 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 209bb40d-5f1f-3876-a076-34b0b106ddc3 | -13.64701 | -45.71587 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c01b6eb-dbd9-35a3-a7bc-423925e9312e | -13.71405 | -45.67149 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd57c06f-4589-363a-bd12-0f6040749e29 | -11.38476 | -48.19192 | 2025-07-25 04:23:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fad8c1da-d54b-3439-82d4-b7bdfaefa7f7 | -17.26993 | -48.06608 | 2025-07-25 04:23:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8d1e33b3-f145-338b-8881-ddb5616a0da1 | -13.71572 | -45.68276 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 054ad80e-4932-3483-be95-0a8fec8e26ff | -14.95638 | -46.98238 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4ddabd3-be20-34e6-b193-eb1a9fdd27da | -14.95306 | -46.98182 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 184af40d-18e1-3e76-8e82-0c372d580b4d | -14.95364 | -46.9782 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2a25c6c-8551-3241-b604-3615c70a23a1 | -13.71905 | -45.6833 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04dc52b6-20f0-3482-89a5-f478d1bb01f2 | -13.64146 | -45.70765 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b995c7d-1044-320b-bf1f-802fe8da6984 | -13.72128 | -45.69098 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50e494a6-b7e4-3a1e-b4c7-55ded23c6c38 | -14.75961 | -48.23675 | 2025-07-25 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30d747d7-3919-3d9d-9b50-a7a0d9f8758d | -15.27827 | -47.12828 | 2025-07-25 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd2cd2b5-b80a-33d3-b602-e790b6edf7a1 | -12.25606 | -44.78196 | 2025-07-25 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f27eb6f-38c5-3512-b526-ba3fa15b97f0 | -10.04601 | -59.11116 | 2025-07-25 04:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4bdc0596-3f7b-3999-be34-c8b8f2848137 | -14.95581 | -46.986 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96d1b207-0b68-3381-bb29-4453b94827dc | -12.70544 | -46.98281 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9ff63f7-1168-3c66-a510-1ad9ef602bb5 | -13.71016 | -45.67452 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c4afdeb-f8bd-389d-82b0-801ad32a5922 | -13.64368 | -45.71532 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 818a7a87-e290-3dad-af8a-c91ad29d7741 | -14.9386 | -46.98685 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cadab8b8-2dcc-39d4-bd19-5768cdf5ab49 | -13.71795 | -45.69045 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d02ffc26-c30e-35a6-bdaa-c54a0bb3ca4b | -16.82091 | -47.59941 | 2025-07-25 04:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0794fba8-6b82-36bc-b547-6bd1bdab53d4 | -12.05087 | -45.431 | 2025-07-25 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9acefb22-e57b-3f1e-aeee-92769209b9f3 | -12.42545 | -45.37488 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e88ebce5-2ae6-3ae8-bffd-f4d9cbbf6e89 | -15.59666 | -46.52795 | 2025-07-25 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac1c063d-a0a8-3e41-8ee1-c4d21d308e1f | -12.69644 | -46.99605 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8087a9c-6c64-35e0-899d-c208da41b57a | -15.26658 | -47.13731 | 2025-07-25 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a2148b4-cc14-33a6-87b6-f085d78bb1ce | -12.40529 | -44.21317 | 2025-07-25 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34a9fcd9-dc9c-3ecc-a747-37abb826ffce | -15.58691 | -49.85132 | 2025-07-25 04:23:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 34a09103-b492-35bd-ad0e-a10af2d57260 | -13.21027 | -51.11731 | 2025-07-25 04:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f35fa9bf-1c98-3cb4-96d2-99c933e1c451 | -12.25214 | -44.78505 | 2025-07-25 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README19.md)
