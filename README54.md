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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ee687de-1f90-3503-8eba-eac714c5ead2 | -18.91786 | -47.02167 | 2024-10-01 03:51:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 159c2663-04fb-30df-8195-f104e65d9cfc | -18.83927 | -46.79798 | 2024-10-01 03:51:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 210558c7-4857-3f6b-b96e-68becce02eb6 | -18.77966 | -46.93093 | 2024-10-01 03:51:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d4fe6ae-f84f-3483-a3fe-d8414b42668f | -18.77869 | -46.93584 | 2024-10-01 03:51:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 782a7c73-2bac-30cf-9e4c-44cb95cd08c4 | -18.64941 | -52.48835 | 2024-10-01 03:51:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a304fac-55f4-3a1a-b46f-b7c272b1b566 | -18.64882 | -52.48931 | 2024-10-01 03:51:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c96d9977-b19b-3e2a-9105-856df2e16da6 | -18.64312 | -52.48613 | 2024-10-01 03:51:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0d404df-f7b3-3d0c-8bda-028be3120632 | -18.64187 | -52.49162 | 2024-10-01 03:51:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a935b5c6-e96f-3a0b-a10d-651676f20380 | -18.64124 | -52.49265 | 2024-10-01 03:51:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99a4af61-7b29-3a9e-8820-00ee132af8ef | -18.63679 | -52.48412 | 2024-10-01 03:51:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f739a8a8-ef8e-3847-a13a-eb5407054b47 | -18.63618 | -52.48523 | 2024-10-01 03:51:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f1fb656-d2b2-3056-baeb-1d4c536673c5 | -18.59949 | -53.05645 | 2024-10-01 03:51:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4e89512f-75aa-3743-86d2-175620114677 | -18.5952 | -53.05449 | 2024-10-01 03:51:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| de3fa6c6-bb58-3cec-82d5-ab6b9ab8ff9c | -18.59376 | -53.06052 | 2024-10-01 03:51:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a194fdd9-cf9b-3a86-8844-c7c2db1b3830 | -18.59298 | -53.05427 | 2024-10-01 03:51:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f480560a-22cc-3ec5-9c1f-cfcbca60f421 | -18.59157 | -53.06032 | 2024-10-01 03:51:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62ba0370-358a-35c3-84e6-48ada099af32 | -18.38208 | -48.22301 | 2024-10-01 03:51:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 307c75f4-4ac1-3b83-9949-950f90856e44 | -18.38146 | -48.22601 | 2024-10-01 03:51:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5826b7d-84fe-30cd-bcc2-250d4b5c3aa6 | -18.38084 | -48.22897 | 2024-10-01 03:51:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fecec165-d105-3b2d-89b9-53038a442218 | -21.60801 | -47.83725 | 2024-10-01 03:51:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 768b0619-37cc-303a-8c8c-9b2b627d6a25 | -21.60632 | -47.83833 | 2024-10-01 03:51:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 957fc48f-e1a3-3b9e-98f7-5a93d29b0066 | -21.60547 | -47.82591 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 33.2 |
| c8f39200-a5e3-3740-9bc1-3da3134d08b9 | -21.60526 | -47.84342 | 2024-10-01 03:51:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dc2d0de0-0b78-3d29-ac08-e169c9e5c810 | -21.60444 | -47.83106 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 37e5dcd5-f974-373f-8cf3-0434ed3c5420 | -21.60386 | -47.82703 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e1a24496-90dc-3bbc-b0f2-0d74ecc3f3fd | -21.6035 | -47.78795 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55c5b59a-3609-3ad9-bcbe-49044dcc4443 | -21.60342 | -47.83615 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 82df6dad-076d-3bc6-b9fa-65003e0f6e2c | -21.60301 | -47.81428 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2649c388-97c1-3f90-ac90-b33a98119881 | -21.60279 | -47.83215 | 2024-10-01 03:51:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 33.7 |
| ff33173a-97ae-33bc-9d6a-890ffddcff1f | -21.6024 | -47.84125 | 2024-10-01 03:51:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 18ff6d59-83d0-33d4-a244-75cabca1ff3b | -21.60196 | -47.81949 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10c8d555-88b4-38a2-aa68-694dc7974b6f | -21.60173 | -47.83723 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 33.7 |
| dcfeeb8d-91a9-316f-bb50-42c36e74fbcc | -21.60144 | -47.7982 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0833b53-83a6-392f-b383-3aab057c2503 | -21.60091 | -47.8247 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 3d9544ca-9a31-3452-8073-41628939689a | -21.60067 | -47.84232 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6789b49c-d4cd-32eb-a9b3-92186c465bc1 | -21.59987 | -47.8299 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 78c9c3d4-6782-3f70-a1fc-d6ad9f895534 | -21.59883 | -47.83503 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 02af5f63-c318-36c1-a2a4-3fe6b30da35f | -21.59846 | -47.81301 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 804989da-caf1-3c9e-b0b9-3f66ebf2b155 | -21.59788 | -47.79205 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7fe23e6-a0a8-3257-b0b6-46124191852a | -21.59781 | -47.84014 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 4ff61de1-00bc-3389-81e8-af0310caf790 | -21.59741 | -47.81822 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 951e0fea-b4cb-3241-ae95-7131fbdada14 | -21.59686 | -47.79713 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cba5012-47aa-3f23-ae5c-a43d2f78acd5 | -21.59636 | -47.82345 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 4c46042a-5ab7-3bb5-ab3f-f3027a3fd358 | -21.5953 | -47.82866 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 406df57d-b2fa-32da-b0a7-32b0d7ea489b | -21.59426 | -47.83383 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d20cb4a5-2a29-3529-9dbe-dd2080b1dd43 | -21.5939 | -47.81178 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 45.2 |
| a9ef6054-8d1a-3085-bdb3-3d0f5e6339fd | -21.5933 | -47.79097 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9226551-e2e0-3738-9327-b108f0ef78f8 | -21.59322 | -47.839 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 8919bfc6-b2c2-3544-9fde-d3b86f6997ca | -21.59286 | -47.81693 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 50ef3cef-41aa-3a08-b74e-2a40746cecb5 | -21.59227 | -47.79607 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 478d8aec-c3d3-3f64-adc4-a7d80c2320fd | -21.59219 | -47.84411 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 971ba5f7-1129-3bb2-a6c9-2cdcce25c3e7 | -21.59181 | -47.82213 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 70373055-057c-3159-adee-e6263c7796c5 | -21.5913 | -47.80088 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| db2bc1b1-3af6-39b3-b34a-911144c18405 | -21.59077 | -47.8273 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 574caf68-279f-3a6b-9771-7d2178d7e63b | -21.59033 | -47.80568 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9099238b-33a7-37a3-b460-107734db120b | -21.58972 | -47.83252 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 68b2e7e1-e91d-32d8-9a0b-c4e8acf17e53 | -21.58934 | -47.81059 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 331c2767-1de1-32e6-bce0-6d134047d783 | -21.58865 | -47.83781 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4ea63e47-20b0-3c91-9645-072cf6744f86 | -21.58831 | -47.81565 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 27f2e212-83ba-36ac-a7a6-a5a93e61a0e3 | -21.58761 | -47.84297 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 04640c4e-b29a-3800-b5f1-285886da350d | -21.58727 | -47.82082 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d625086d-980a-3607-8cd2-bc1e1abbccc1 | -21.58672 | -47.79979 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b14a93e0-8338-3e59-9236-04288bcde564 | -21.58623 | -47.82597 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 45ab934e-e948-36c2-9631-7fdd4e5000a8 | -21.58576 | -47.80455 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 00319c64-e6ac-3ebc-9a5c-a20ea4588be8 | -21.58516 | -47.83124 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3576693-3d95-3ae5-b6a7-c8ac3974fdb9 | -21.58477 | -47.80941 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 95857716-beb6-3e0d-9975-30616b3625b8 | -21.58408 | -47.83659 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 42111d28-e009-3447-a128-8773a0930f25 | -21.58376 | -47.81441 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 03fce99c-12c3-3c57-9950-cfaef8d2685f | -21.58314 | -47.79379 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d874a4c8-eec2-3819-bae6-bf403549012f | -21.58304 | -47.84175 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7355d89-28e2-34a2-92bf-d36c78db9193 | -21.58271 | -47.81956 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f16e8c2b-7e4a-3556-aa40-54799606b003 | -21.58216 | -47.79861 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 7fd19803-f5e9-3042-a9ad-249c3dd52d51 | -21.58167 | -47.82475 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 49de789b-4f55-3d90-aaf4-4ebb8fe828ec | -21.58119 | -47.80334 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 68.3 |
| da9eef8d-214c-327d-bc1c-4806f478f335 | -21.5806 | -47.83002 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 92701a4b-c9af-38f8-b9ba-bf75ef304713 | -21.5802 | -47.80824 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b93098f1-3b3a-340f-ae2f-05133662edbe | -21.57951 | -47.83539 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 760b98de-f520-3521-acd5-a5cc3bb23b83 | -21.5792 | -47.8132 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ca44a70a-053f-3ed9-bc81-ccc632d89f39 | -21.57857 | -47.79263 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d2ce6e70-f638-3d2a-ba7b-c78d222e99cb | -21.57847 | -47.84056 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| feecdd7a-71f1-311a-ace4-9285524694f4 | -21.57815 | -47.81836 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c85ecdab-2c9c-3d96-9a5b-ddb6bec8cdb1 | -21.57759 | -47.79744 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 38d9faaf-ab05-34e6-9c9e-0010c86f7b71 | -21.57709 | -47.82358 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 49b8a053-c8e0-3698-823e-0d3a95aa2919 | -21.57662 | -47.8022 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 68.3 |
| caa5d3b3-5275-3441-ae6d-a1000f776bf7 | -21.57603 | -47.82885 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 949f9f76-f486-3350-b286-346dbdce25d9 | -21.57563 | -47.80709 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 9190ee5b-e931-3868-a700-6da1b075c06b | -21.57494 | -47.83421 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0f15aa6a-06cc-373b-8eb3-538d5b8e4e8f | -21.57461 | -47.81209 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| be466f41-672d-3ed4-8603-2b712e9f06bc | -21.574 | -47.79149 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ea4d0f76-2189-3644-af3f-83e174b7dc0d | -21.57388 | -47.83942 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e8c366e-ffd3-3b81-90e7-7b9fc6dbfdf8 | -21.57356 | -47.81726 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b32911e4-bb08-37b8-aaf4-cc657607310d | -21.57301 | -47.79633 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b14c0de9-809f-3fd6-8913-7f3cd2fde005 | -21.5725 | -47.82249 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| da3bc13a-e05e-35b9-aa05-e52da48532b7 | -21.57205 | -47.80109 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f265279a-9448-340e-952a-4fe8abdb76f7 | -21.57144 | -47.82772 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 82b23902-352c-30e2-b75b-85d34d9a1348 | -21.57105 | -47.80596 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ac5681c-25c4-32b4-821b-641d75af7600 | -21.57036 | -47.83305 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8a836aa1-7558-3874-ab9e-d9b140fd9542 | -21.57003 | -47.81101 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 809cc418-689f-3682-a378-291a96bc3295 | -21.5693 | -47.83829 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3bf8806a-7669-3c86-9290-90b45a76e8ef | -21.56898 | -47.81617 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README55.md)
