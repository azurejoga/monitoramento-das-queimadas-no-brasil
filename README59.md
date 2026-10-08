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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a95c737-f061-33e9-a8c2-ec3928db38d3 | -11.39397 | -46.68655 | 2026-10-08 03:45:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e86b784e-fb2d-3e65-9eee-57c6c89989bc | -15.62465 | -42.99416 | 2026-10-08 03:45:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b9eb223-edbb-341c-8b5e-0aa39af0eb57 | -16.89084 | -40.89296 | 2026-10-08 03:45:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 35f7eceb-becd-3dea-9661-6e47c18bfac6 | -16.12978 | -46.88755 | 2026-10-08 03:45:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6226d431-19ac-3607-9aec-8a78240f0f26 | -12.23891 | -44.73027 | 2026-10-08 03:45:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a3e0b9f-65d5-3246-9542-3c6339bbd22a | -13.22996 | -43.40094 | 2026-10-08 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6068dc1e-e681-3228-9e79-0e33fc39b013 | -11.63179 | -43.69965 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 42189e78-6b67-35a4-9521-bc83b6714a24 | -10.44873 | -46.8439 | 2026-10-08 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 10c47cbd-e4a2-3c46-b6b4-78ede585e0e0 | -12.37197 | -41.48264 | 2026-10-08 03:45:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 824eaee6-34a4-3c3a-b60b-5fffcd4987f1 | -11.85032 | -43.53281 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ab66ad9-6167-39af-b28c-e0d76be78b06 | -10.76751 | -46.58449 | 2026-10-08 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 318522f4-794e-39a5-aec8-8e677f40b64f | -11.63011 | -43.70802 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 44b036ad-8f31-3340-8914-2ff522c225dd | -9.37148 | -45.93335 | 2026-10-08 03:45:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 326f812a-13d5-3b04-9429-e186dfee8ac8 | -16.97865 | -41.2277 | 2026-10-08 03:45:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0417d7ed-afe4-34b5-848b-33a3486d9ca1 | -10.76888 | -46.5779 | 2026-10-08 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 82581666-5e86-3905-b7d4-5a6e6fc49633 | -17.43339 | -41.36042 | 2026-10-08 03:45:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d88ddbee-c2a1-3575-ba53-15fe7bab48d7 | -14.54134 | -40.31968 | 2026-10-08 03:45:00 | NPP-375D | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eae2b067-35a1-37e3-aba9-997a41598fd7 | -15.11113 | -43.62794 | 2026-10-08 03:45:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a6b181e-1de6-352a-aabb-aaa562d6396c | -13.1932 | -47.87405 | 2026-10-08 03:45:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1d38e29c-9a5b-3123-b016-8d04f511b68b | -11.24385 | -44.87415 | 2026-10-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e6b408d-0c91-33af-97cd-755b3986e925 | -10.99967 | -45.42178 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a25bb02e-06fa-360c-80b6-81925c35a7f2 | -13.19799 | -47.87639 | 2026-10-08 03:45:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b4fadd4b-3bb5-36d7-ae32-c47659a1dd35 | -11.84444 | -43.53258 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6879bc94-eb4c-3a17-80f8-0e8a5531346d | -11.63094 | -43.70391 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7af41a7c-d03d-3905-a573-0d17dc0bb0ab | -13.50099 | -44.37025 | 2026-10-08 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 465611f6-e52c-3ad9-a9a4-00cd9b73a55c | -14.91425 | -48.12249 | 2026-10-08 03:45:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a57ffee4-2c60-3ffc-b26b-799e4fc501a2 | -11.63142 | -43.70644 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 30957007-0d71-3616-a4ad-32a2036065fa | -15.55672 | -42.97866 | 2026-10-08 03:45:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5660dc51-c59a-339b-bcf1-9101108ca1a6 | -11.63479 | -43.68898 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99112902-d377-3c30-8d97-21f05344c4b2 | -13.50673 | -44.37187 | 2026-10-08 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 278fe12a-d778-3f63-a2d2-0dd89782f574 | -16.12859 | -46.89283 | 2026-10-08 03:45:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fafacef5-f2b2-3298-bea2-c48925781051 | -12.23377 | -44.72429 | 2026-10-08 03:45:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e96b31bc-0193-3ed2-b75c-1fab048ee067 | -11.63391 | -43.69355 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24c51422-68f8-3a3b-a2bc-c43bbf3319f4 | -11.09952 | -44.01293 | 2026-10-08 03:45:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dbce9379-0d50-3b94-9f20-7f8e34030b26 | -11.71859 | -43.65503 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32315041-dc65-3642-b77d-50a97f96f085 | -13.19465 | -47.86763 | 2026-10-08 03:45:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e92ebd7-2883-3f65-a3dc-4ea708502b31 | -11.63878 | -43.69941 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 80229eec-c7c8-3d6c-8a09-566ea9e93b5a | -11.83728 | -43.56919 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d4982728-8e72-35a9-8f70-febc8cbc2d42 | -12.15616 | -44.76177 | 2026-10-08 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1855925-0782-3121-b82f-8deeb7d83aa9 | -14.91605 | -48.11435 | 2026-10-08 03:45:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea1042f1-e0e4-3787-9e5c-637dac53d1e8 | -13.50586 | -44.37618 | 2026-10-08 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f4ebab0-7ec9-3e2f-a2e0-4d1703c1c57e | -10.44731 | -46.85062 | 2026-10-08 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d366e7c1-edf4-3f77-87ea-13130b325e73 | -13.23145 | -43.39351 | 2026-10-08 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e951a2c6-8d74-3d51-a833-426ee27d19f6 | -11.74438 | -43.64694 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6654ff23-8985-36cb-ac63-feff07f7fb14 | -10.96498 | -45.39349 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7229b1ed-22a3-390a-a947-18e73647d41d | -11.38883 | -46.6766 | 2026-10-08 03:45:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a686ef15-fb88-30b8-adb6-3fdd70a2eb4d | -14.92565 | -48.08895 | 2026-10-08 03:45:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84bfc886-5876-39df-9be9-7402f6f93c76 | -14.93611 | -48.10806 | 2026-10-08 03:45:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab31d179-cb46-3225-9071-0683a6645ca4 | -17.50272 | -41.91749 | 2026-10-08 03:45:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 56b8ebf4-0666-37b9-909c-6b50ec913f83 | -15.55286 | -42.97832 | 2026-10-08 03:45:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6eefd816-c92f-32ba-9c8d-4236b094c558 | -16.85501 | -40.57953 | 2026-10-08 03:45:00 | NPP-375D | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bc4bf2e4-8027-3bbc-983b-1da0bb2ec1bb | -13.50008 | -44.37473 | 2026-10-08 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9776595b-532b-39f2-82fa-44a0245f8ecd | -11.23639 | -46.24726 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08ed6c04-3d7c-3b29-b752-9096a4d75f6e | -15.1104 | -43.63148 | 2026-10-08 03:45:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 776e943e-a808-3713-852a-277eaa5998a0 | -14.93411 | -48.11693 | 2026-10-08 03:45:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21587116-a04d-3e03-9484-a6af49c8908d | -16.90143 | -40.88505 | 2026-10-08 03:45:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 75edd16f-e21a-3455-92e5-4f608e88c9fc | -16.85586 | -40.57496 | 2026-10-08 03:45:00 | NPP-375D | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a6bb2e4d-774d-3206-b8dd-da1e31efac3c | -9.81658 | -44.77701 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2dbbf02-69eb-35e0-9672-59fba714dc6c | -14.91946 | -48.11622 | 2026-10-08 03:45:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c1e8bfc1-ffb7-3d3a-9793-72cfcec708da | -11.62572 | -43.7048 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5ce113b1-28a6-3d1c-a171-1b7fa98464a0 | -11.62527 | -43.70221 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 041056b6-d8c5-3655-b934-be024d8770ab | -17.50509 | -41.91594 | 2026-10-08 03:45:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 7705dca3-5bf6-383e-9ec2-ba1d83e4d6e7 | -12.04287 | -43.43887 | 2026-10-08 03:45:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 873fb9c6-57da-35f6-9b3d-78af414c8f1b | -17.50373 | -41.91243 | 2026-10-08 03:45:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c000e94b-b51d-38f3-8b18-9e01d7b87071 | -11.62654 | -43.7006 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 60e3e17f-f330-367b-996e-2569ca926b46 | -11.62304 | -43.68343 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9ae2098-6fe8-3cb1-b293-70af35f40c33 | -11.23409 | -46.25213 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a52a99d4-cf51-337e-95fa-90f9dee078a6 | -9.91373 | -44.79941 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d8a09ce-b320-3a16-ab1b-844ed5b069e1 | -9.89922 | -44.8015 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a03958b7-49e8-3beb-bf05-c1b29cc83fe6 | -16.89618 | -40.88875 | 2026-10-08 03:45:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c65801bf-ac00-3f0c-be87-057d54e18775 | -13.16271 | -43.28505 | 2026-10-08 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 66ffbdee-8705-3cd1-8ab9-d57e1b0d86a5 | -9.81126 | -44.77772 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ee523db-8f2a-31c3-9ca3-fb87b854965b | -11.6282 | -43.69201 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d497e15a-da12-3f73-a69c-0e191a58f862 | -11.46048 | -43.38651 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c9d0dda-7f2f-3aec-b5be-84a1fa11255a | -11.61877 | -43.67484 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 112ed2fb-e91d-35d8-adeb-be6316c12376 | -13.1587 | -43.27656 | 2026-10-08 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 282bdf51-b6f7-3e12-95c7-39db3b60d044 | -16.83929 | -41.04253 | 2026-10-08 03:45:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3243cdff-0cbd-3f5e-8e44-4f80353e5d3c | -16.82958 | -41.04515 | 2026-10-08 03:45:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 55a320f2-495e-3860-b775-84f06c2d1194 | -16.00926 | -43.60428 | 2026-10-08 03:45:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59f96f37-2fea-3e14-9485-186b0d250a00 | -11.46108 | -43.38889 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3edfbee7-ef69-3d68-8388-507c881cbc57 | -17.12054 | -41.3419 | 2026-10-08 03:45:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0ac4aa5a-3f90-3cae-a2a9-819b60c99d64 | -13.16343 | -43.28141 | 2026-10-08 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| bd32519d-ee0e-3e48-b107-9d24e6f93e42 | -11.63266 | -43.69533 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e637cdb7-c03a-3c78-bbe6-f28fc89a370a | -14.91767 | -48.12407 | 2026-10-08 03:45:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96197dc3-f4c6-35db-a1cd-b257c54da5a4 | -9.89725 | -44.81165 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3b16556b-d46c-3a12-b192-289875405eda | -13.19149 | -47.88163 | 2026-10-08 03:45:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e5911398-4237-3119-9dde-1f3b0d7298a2 | -11.2624 | -45.18364 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5fc5ac83-ba48-33e6-b5bd-5b5a64e8dfaf | -11.30137 | -44.83197 | 2026-10-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b050ef5-b2e7-3924-ab8b-1ce3a6913114 | -11.62704 | -41.83241 | 2026-10-08 03:45:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fe37c099-8d26-39f6-849f-bb014d712fa4 | -9.8166 | -44.78416 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1aa782cd-578f-371c-99c4-bdc84080d582 | -9.82195 | -44.78347 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 177f4367-fce3-3285-bcec-b5df6015fa8d | -11.77358 | -46.77627 | 2026-10-08 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 02f5a5da-f594-3456-a34f-fb2a035c94d4 | -16.15512 | -41.46327 | 2026-10-08 03:45:00 | NPP-375D | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 72d16a7e-aed1-3576-918a-4873f0194e53 | -12.37155 | -41.48133 | 2026-10-08 03:45:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 90f9986d-56e4-3f33-8f42-f453067bfb5d | -14.91449 | -48.1055 | 2026-10-08 03:45:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c2825aa-8853-3bc5-a7ef-b99220ea878c | -16.90392 | -40.89592 | 2026-10-08 03:45:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 21c5f4ef-c4fe-3749-8506-54e129b1dd0e | -10.30667 | -46.62295 | 2026-10-08 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05712a00-62ac-3cf0-a5b0-a4f689fead7c | -9.81557 | -44.78229 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b524076-5c36-373a-bc38-fa635c204d91 | -12.23281 | -44.72903 | 2026-10-08 03:45:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7974937b-963e-3d20-95a3-ac22842e33ff | -11.10039 | -44.00851 | 2026-10-08 03:45:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README60.md)
