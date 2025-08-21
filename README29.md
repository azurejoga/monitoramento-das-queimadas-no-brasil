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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59ea49fa-c3e3-3801-b119-df636d625051 | -5.6841 | -43.86575 | 2025-08-21 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 193f9d0a-5784-3f25-aab4-e78a16163eb8 | -8.14522 | -47.34076 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9506dc71-d435-3679-9b1d-bd837b14b867 | -7.95129 | -42.64347 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3e2564b7-d255-3521-b561-6969d276eabf | -9.60165 | -45.50803 | 2025-08-21 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc0f241c-9a91-3449-aebf-a301a1e4dee7 | -7.63162 | -45.25112 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8e2e980-b042-393e-9af7-3febf4ab6ae8 | -5.97229 | -44.13795 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8172a702-638a-304c-a656-b5da3fb442a8 | -12.6408 | -46.8756 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 899c3a1e-c81c-3d52-a16e-f425a5b56627 | -11.17721 | -46.13553 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 43c63418-8eec-3dce-8689-f6e2b2ec5375 | -6.36469 | -43.32705 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6041efed-c9b5-3281-95c4-ec65b744496c | -13.01994 | -45.16088 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8805b66c-bcdc-3c86-b44a-83bb64e4d0a4 | -6.56269 | -42.99553 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 744c3cb3-4fcf-3c72-9f2b-2ed02b8e29d6 | -6.10978 | -45.42191 | 2025-08-21 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a714c57e-6afb-3d6c-a146-05e413ff0e70 | -5.9102 | -46.31604 | 2025-08-21 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 578f875a-4edb-32ba-904c-22c49491efe9 | -7.60313 | -44.38645 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2872098-1133-397d-8cf0-f47211bb7c66 | -12.63663 | -46.87896 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8765ab0b-32c2-3634-9f47-6053bbd612e4 | -11.29783 | -44.94331 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fb40d14-8f70-3ccc-a0f8-e0c6993d88a1 | -6.54547 | -45.5173 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3dbd586-408f-3e43-ad17-c05dbe060216 | -5.78775 | -45.07052 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2bec67f-0fa2-3924-a7db-cb22e25e40dd | -9.69759 | -47.94063 | 2025-08-21 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8964b94b-9d96-31ef-b64a-eb0e6a94ec69 | -7.64258 | -45.24896 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d3fa47d-11aa-3b94-a6d9-f796c90b03f7 | -6.5452 | -43.98421 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fad47713-72ea-399e-9c25-39b4d10bdfbe | -6.86122 | -44.41517 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4d64e2a-476b-3ceb-b3ce-774b344c6ab6 | -12.9868 | -45.21775 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ce9220b-44f8-368d-ac0c-8ab2f53b248c | -6.42136 | -44.67385 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bccccd29-1150-3c51-8eb5-f2995da975c7 | -13.02155 | -45.17216 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| b8208b31-ebae-3709-a342-1553886988b7 | -12.98461 | -45.21004 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a128c4a6-6e9c-3021-a9ed-8fbb6acf7b53 | -7.59977 | -44.38589 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c04bbfe5-646e-31dd-ae91-f3911260a5b7 | -5.99036 | -42.84831 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c76797db-7153-3c87-b1cb-6eaa0786737d | -6.81945 | -39.89622 | 2025-08-21 04:17:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2af11c04-b888-3662-be3a-cefd0d5dc644 | -7.15209 | -44.6473 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9e7b09a7-81f9-33cd-95c5-9adce6fae921 | -13.01868 | -45.19004 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c969af50-7677-3109-8a4d-f54c22a8a9c9 | -9.1037 | -45.17711 | 2025-08-21 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee3c1252-cdb8-369d-96d5-1731bd88fb58 | -6.02041 | -44.38585 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec55b770-6382-3879-a717-fb5257835787 | -5.78537 | -43.60681 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5b77104-ed84-3e46-a8a8-7329afcb9f18 | -6.44664 | -53.3792 | 2025-08-21 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f431cbf7-19b0-3587-8260-729a85412eb2 | -6.00579 | -42.81524 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 33c5ca09-c413-3e78-8546-64d0cfa8265e | -8.76146 | -45.47657 | 2025-08-21 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2fff77c-db1c-3759-bfce-d6be2d75e177 | -7.70295 | -44.02073 | 2025-08-21 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de3c4e8d-9d72-3c6f-97d6-18e89a29aed4 | -8.38198 | -44.60292 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce7a0c4d-0bc1-3fc9-b578-f24d701a2792 | -5.95765 | -44.14298 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18ec9ad8-214e-31a9-b7f0-4e4f961c3856 | -6.53191 | -45.46815 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3a7e06c-e7a8-3e4c-90d2-5679a640fd24 | -6.21283 | -43.32763 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5701b95-81ad-37d9-8206-c538c864fbd0 | -7.38197 | -47.04744 | 2025-08-21 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6484ee8c-bf07-3738-a143-fc05b1579e38 | -12.7206 | -44.78636 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5cdb2fa1-0de3-3816-be88-f805df9b0586 | -9.83056 | -45.96463 | 2025-08-21 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a667a83f-22ad-3fb3-ac3e-11d56ca7cc2a | -5.90414 | -46.05635 | 2025-08-21 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f19d3222-433a-349d-8a7d-b989e718bb86 | -6.42535 | -44.67076 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5e5af16-dda0-3021-9dff-4d1fdf275fcd | -12.66955 | -44.9641 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fb16d34-6d29-3af8-850c-4de3f93eaa59 | -5.96497 | -44.14046 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6916e20e-4002-3ac9-a058-d79744fbe976 | -6.26156 | -52.82148 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fa20369-151d-3b24-aba7-3dfa0ffc6bc3 | -5.9925 | -42.81315 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f3508c5c-0256-3f6b-b116-6da9219ef5d7 | -11.43405 | -47.31995 | 2025-08-21 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97b3c60b-9633-3116-834d-c60b5edc72c9 | -11.29505 | -44.93923 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73491b59-5d57-3e41-954a-de831e058e14 | -11.29391 | -44.9463 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e369096-88e3-37f8-a9ab-d5c85ef257ee | -6.26627 | -43.71533 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da8409aa-83e4-3cc8-ac66-17a6f15dcbdf | -6.58048 | -44.46316 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d223f3bf-699f-3577-b365-1e0f4b100926 | -7.02137 | -44.6147 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d898dbba-a8e8-3826-bee6-ebd05195dce1 | -5.95708 | -44.1466 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e6c933f-6581-322a-95ea-49804d1c9b5c | -7.8511 | -45.1892 | 2025-08-21 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d9d7a79-d2f6-37fc-9c27-8e01e637ecdb | -5.89299 | -42.86438 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6674f52e-ac30-3191-ac7b-8cd5965f67db | -7.01903 | -44.6292 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| e367d768-a7f6-3d6b-b36b-0dc1bfb73948 | -5.74847 | -42.75305 | 2025-08-21 04:17:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 985d0a49-4c86-336f-bb16-a7380460b15d | -6.10121 | -45.40953 | 2025-08-21 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23d31afb-43c9-314b-8869-3507b749f7a4 | -11.08888 | -44.8108 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5303ee87-a29c-36a6-9872-8a3910f38a04 | -8.16981 | -47.32792 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7feaa764-25da-30f7-b9d6-1cb5848ca027 | -5.95931 | -44.15431 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d25931b-008a-3457-80de-38f709fe8877 | -5.86656 | -43.44029 | 2025-08-21 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdf0c1f6-567e-3917-b057-6e637cbbfa46 | -6.42477 | -44.67442 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63fb5b31-243d-3a68-a582-e71a5c9e97cd | -8.84149 | -52.05618 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20cd17d1-c296-30f1-bdcf-26e225e7991b | -6.5134 | -43.41475 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc32b224-9feb-31bc-bbdc-96b15fd16fb3 | -11.67257 | -46.87791 | 2025-08-21 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2d0b4ce-b3cb-35d9-baaa-0177ceec3faa | -8.37299 | -54.99526 | 2025-08-21 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f40e2a2-1abc-34fb-ae57-cdf1cb338c07 | -6.49845 | -43.44448 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d7874fa-c9ff-3fe3-931a-4a7856ce4829 | -5.95823 | -44.13937 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2855f289-24f6-35b5-a9cb-a684803b8623 | -7.02814 | -44.61588 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ad73c3f-e875-399f-85af-1e75866f0297 | -8.07131 | -43.68431 | 2025-08-21 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a484e6c7-3b8c-3f57-8f13-3c9e1125de81 | -6.36231 | -44.64923 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8403e5e4-9b71-314c-980f-84ec0eeb771d | -6.36243 | -43.25542 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c95ec113-f762-35bf-b7bd-9857dc1b32e8 | -9.83119 | -45.9608 | 2025-08-21 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c20235af-c7d5-3f69-8a43-899fb5fdff85 | -6.29441 | -43.87548 | 2025-08-21 04:17:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8f02201-23ba-3d14-bed7-5cfe09b23213 | -10.71918 | -48.25142 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c92296e0-ddc3-38aa-b03e-d9afb0e49dc5 | -6.29776 | -43.87603 | 2025-08-21 04:17:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27bb41e5-c1bf-3688-86aa-e8bb2db1fc58 | -6.28715 | -43.87798 | 2025-08-21 04:17:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f7b396b-0bdf-3b92-b4ee-6c6b24ef228b | -5.99305 | -42.80969 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a967a6ba-b5ca-3c80-a10b-6a9844a2b3cb | -6.02787 | -44.36098 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eef33694-83a8-3e09-8d12-24e31c0cb079 | -8.16264 | -47.35318 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5add5339-6948-392d-80be-a60e52d28073 | -6.93927 | -44.38689 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcd65767-a506-3e30-bf40-9d7b2a4bd987 | -6.42836 | -45.48389 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6b0b21e-061a-385d-9b43-f0a528347ebe | -4.94548 | -48.39285 | 2025-08-21 04:17:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29095bd3-1cd3-391c-b12b-28920c756018 | -12.21056 | -45.4332 | 2025-08-21 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb086675-1b1d-3fa2-b8c8-edd2631cbfdf | -6.10617 | -44.3731 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4a25f56-ee8d-3139-bd32-8a3bc84a4c83 | -6.17698 | -44.73799 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ee48625-f1df-34d0-8d1f-875d96c4a678 | -8.83188 | -52.05095 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9940dd2d-9395-3fad-a787-e2f726ef7ab9 | -6.10058 | -45.41343 | 2025-08-21 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f59eb5f5-20a2-3ea7-a6be-9fd1290c9557 | -10.45792 | -48.80843 | 2025-08-21 04:17:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8faf0ebe-4abe-3195-b8a7-5ec428774d4d | -11.30118 | -44.94386 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f6c6aee-6a93-37bb-9896-e5cdc72e3079 | -7.65049 | -46.26629 | 2025-08-21 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1251ab4-8542-38a7-bd1b-5d57e46c067b | -6.0152 | -42.82027 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f6928b77-56ac-3f87-aaee-6daf990ec456 | -6.07431 | -44.1135 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6f62063-be9a-3abc-a475-e7e8996b5b79 | -7.02872 | -44.61229 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README30.md)
