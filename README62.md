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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ea1c2d5-3110-3c77-8256-0df67d3de839 | -14.4949 | -45.5949 | 2025-10-19 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| fe6a1277-426d-3069-ade5-3c71b882eec2 | -13.9317 | -45.6007 | 2025-10-19 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| d69d46de-c82e-3940-be8d-ed646ef7e105 | -14.4754 | -45.5984 | 2025-10-19 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| e7fcf4cf-7e44-32ef-b243-4c4b7d0e6aca | -7.22314 | -45.19063 | 2025-10-19 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7bcb6f6f-f84f-3178-858a-1aa0d0b0ace8 | -7.1648 | -45.61379 | 2025-10-19 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8d622664-460a-32ba-97c6-0cb6d3ea2d20 | -2.86813 | -50.7373 | 2025-10-19 12:17:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| b2fee06d-2c6b-35de-8de8-7090a2eca677 | -7.19984 | -42.19247 | 2025-10-19 12:17:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 5aa03cf8-1fad-38ae-aba7-6b0972247880 | -6.42054 | -41.47149 | 2025-10-19 12:17:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 2fecda39-1188-3e51-a594-465c4161acc4 | -8.03823 | -39.4672 | 2025-10-19 12:17:00 | TERRA_M-T | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 30.8 |
| c3f38650-b445-3c77-a0e8-b77e77ff6fb1 | -7.20008 | -41.00058 | 2025-10-19 12:17:00 | TERRA_M-T | CAMPO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202133 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 2366342e-b134-31ec-a448-33a85d9a4fe3 | -3.97917 | -42.51401 | 2025-10-19 12:17:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| efa075d3-f220-346b-b855-e733d9842c2e | -1.10524 | -48.9016 | 2025-10-19 12:17:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9f83afd6-fcbc-33f6-81c8-0464bdcdc792 | -7.36612 | -41.94948 | 2025-10-19 12:17:00 | TERRA_M-T | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 56.6 |
| 8b208de7-89ab-3314-b1d1-abdfedae51b3 | -7.188 | -42.19103 | 2025-10-19 12:17:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| f389f9b7-ac65-3e99-bc02-9cdba44a775c | -3.3739 | -41.49335 | 2025-10-19 12:17:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 3d075518-f982-3f85-9401-bec93fc7cd5d | -6.38171 | -45.74371 | 2025-10-19 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 32a12dbc-5191-32a8-b493-c152d069e968 | -3.7597 | -44.99194 | 2025-10-19 12:17:00 | TERRA_M-T | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 106cebfa-b7c9-3507-b704-1ffbe30fdb58 | -7.20206 | -42.17574 | 2025-10-19 12:17:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 206d3071-92ab-3294-9632-7b22b9e2ddfc | -6.3804 | -45.75317 | 2025-10-19 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| b630dc52-c8e5-3b07-a9a6-a9d34b871874 | -6.12842 | -44.22446 | 2025-10-19 12:17:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 06efea80-9667-3bc7-acbc-86915999e3c2 | -6.37172 | -45.75579 | 2025-10-19 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f070f530-d106-3894-878d-fcf0251855bf | -4.06981 | -39.8955 | 2025-10-19 12:17:00 | TERRA_M-T | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 84.0 |
| f0e5a665-7555-3fa0-9a1e-a6bf83463c4f | -6.38821 | -45.76408 | 2025-10-19 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 6cc72f8f-38f6-32dd-a4c8-ca8548ad8808 | -4.25267 | -48.56199 | 2025-10-19 12:17:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 30da36cf-8c29-3025-b37f-49fe9218e68c | -7.22455 | -45.18034 | 2025-10-19 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 81d49449-b2b9-3a4d-b5ac-6b4bad10df54 | -6.22597 | -42.4417 | 2025-10-19 12:17:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 48bf8d8f-d774-32ba-9770-88a919e908f9 | -4.21762 | -48.3602 | 2025-10-19 12:17:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d8b5d80c-160b-3ed5-a37d-22026a28c882 | -7.19018 | -42.17446 | 2025-10-19 12:17:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 220.5 |
| b80b76a2-37c4-3f8d-9167-611c607f70f3 | -5.60469 | -43.64284 | 2025-10-19 12:17:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 87c45d52-d4f0-31ef-a181-12c96ead2153 | -4.32263 | -48.08289 | 2025-10-19 12:17:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| a60b9beb-2fdc-34fd-9f0a-19c743c21a6d | -5.63789 | -43.9216 | 2025-10-19 12:17:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b438cdba-d802-301e-8a34-31dddf3fedee | -4.40182 | -43.33262 | 2025-10-19 12:17:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 936ba5cb-8928-3388-a5d7-479ed539bf81 | -4.40355 | -43.32034 | 2025-10-19 12:17:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 717286dd-50bc-3288-acb9-8a99ad1a6262 | -2.87001 | -50.72437 | 2025-10-19 12:17:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 82d6f711-4e82-3901-8111-393206fcf549 | -5.5401 | -47.19779 | 2025-10-19 12:17:00 | TERRA_M-T | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d01139fb-e43b-3339-b516-9a8d79009f5c | -3.76107 | -44.98223 | 2025-10-19 12:17:00 | TERRA_M-T | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d09ba454-43ec-305c-b8ef-fff3c1d2d4f2 | -7.03143 | -41.70322 | 2025-10-19 12:17:00 | TERRA_M-T | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 079dc369-b203-3d61-8c15-3db8933674e1 | -7.37821 | -41.95109 | 2025-10-19 12:17:00 | TERRA_M-T | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 7449fb01-3022-31c3-87fa-dacec71ea309 | -8.1601 | -38.71244 | 2025-10-19 12:17:00 | TERRA_M-T | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 40.2 |
| 05629791-c39e-3d95-bcdf-763c9f94e17f | -4.98273 | -43.85506 | 2025-10-19 12:17:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 190b448f-7878-39aa-abc6-29cf26797f9a | -8.11819 | -42.26983 | 2025-10-19 12:17:00 | TERRA_M-T | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| cf53d672-a4d8-3f44-ac2f-5591ac8ecd86 | -4.07758 | -39.90218 | 2025-10-19 12:17:00 | TERRA_M-T | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 95.1 |
| fc3a488d-248a-3d2f-b5b4-8f3a1aae9b40 | -3.51138 | -41.89608 | 2025-10-19 12:17:00 | TERRA_M-T | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 2a939b11-c806-360e-a0fb-fcf64df2108f | -3.38311 | -41.48422 | 2025-10-19 12:17:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 5fb23b69-a76d-3593-bf44-1781cad0845d | -8.03928 | -39.46078 | 2025-10-19 12:17:00 | TERRA_M-T | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 43.1 |
| c59ed5ce-039c-338f-8d69-4b803e8776e7 | -7.02824 | -41.69596 | 2025-10-19 12:17:00 | TERRA_M-T | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 33dde6c4-3560-37b0-81cd-31f110afd0b6 | -6.37908 | -45.76274 | 2025-10-19 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 93c97573-cd54-35a6-9f4d-3ff20a9bcafe | -4.32131 | -48.09193 | 2025-10-19 12:17:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 6118f41b-331b-396b-8a97-283a0b0e735c | -2.87023 | -46.76413 | 2025-10-19 12:17:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 747edfb2-bd64-371f-b8f0-5af7bdd1c076 | -7.16435 | -42.37024 | 2025-10-19 12:17:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| f628153d-e8e7-3f18-be3f-03c6b6fdeb53 | -6.41536 | -41.484 | 2025-10-19 12:17:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| a0d39145-1766-3fd7-8e74-74df23ee1902 | -4.64796 | -39.51326 | 2025-10-19 12:17:00 | TERRA_M-T | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 8d2432f5-0f8e-317f-a046-e6a993301d5c | -6.26315 | -42.68053 | 2025-10-19 12:17:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| a5180534-5c7c-3cbd-b733-12cc80c361c0 | -6.81824 | -46.37714 | 2025-10-19 12:17:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3ebd044d-b544-39f5-8c26-875e76fb0240 | -7.01918 | -41.70144 | 2025-10-19 12:17:00 | TERRA_M-T | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 99c6cfc3-7d9b-3e6d-a83d-3ccdc0aaa158 | -3.83689 | -41.78502 | 2025-10-19 12:17:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 1e6ccf7c-a63b-36e1-bfdd-90b64f77b756 | -8.01472 | -38.54769 | 2025-10-19 12:17:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 498afd82-c448-3c30-b6fa-4b2c1d755884 | -6.83436 | -47.36746 | 2025-10-19 12:17:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 140ba568-bca2-3b18-9130-9c366fbe8a69 | -1.17678 | -46.22314 | 2025-10-19 12:17:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4af3d565-6131-3b9c-9b94-e53a2d560f23 | -6.11358 | -44.7689 | 2025-10-19 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 61a9d928-c202-345d-875a-5258bf78eff5 | -5.1028 | -47.7948 | 2025-10-19 12:17:00 | TERRA_M-T | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 62e3ecd4-3843-39dc-9e30-487a2715093c | -10.85508 | -43.94265 | 2025-10-19 12:19:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 4e6f0e4a-2326-3f35-b2f8-15d955dfd5b5 | -10.56085 | -43.39225 | 2025-10-19 12:19:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 92e5c1a1-a07f-319c-94c8-e85aa2040ea3 | -13.04287 | -42.16341 | 2025-10-19 12:19:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 36.6 |
| f32fe359-69c0-3965-a766-3311120aa785 | -7.70437 | -47.85827 | 2025-10-19 12:19:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 70b8ace0-fb3c-3bf2-996c-eb865d1c3424 | -12.94029 | -47.34425 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 96ea2bbe-2bb1-3436-be64-29bca2bc8d44 | -12.96908 | -47.27027 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| d20bfb7f-c201-389c-aa45-44dca1fe223e | -13.93045 | -45.60376 | 2025-10-19 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 16df23ea-95cd-37f8-9b9e-a8630f7697cb | -8.58432 | -39.59007 | 2025-10-19 12:19:00 | TERRA_M-T | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 97bfd6d5-85db-3b9c-9cc8-05d776b07d7e | -14.71646 | -41.74074 | 2025-10-19 12:19:00 | TERRA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 61.1 |
| 9feab395-dd9d-3238-9f94-e53aaf49090b | -9.96157 | -45.27814 | 2025-10-19 12:19:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 075b9032-2076-3ae7-a805-8d0f4d0f2964 | -8.57977 | -41.01411 | 2025-10-19 12:19:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 222.7 |
| 6900e4c3-c7a5-3321-83ab-2988b792bb99 | -8.23278 | -43.30919 | 2025-10-19 12:19:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 44.7 |
| f2552d1b-bbd7-3de1-88b7-674330bc4532 | -12.97175 | -47.25102 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| be805e3b-c535-3bf1-9096-ed0e542084b4 | -10.56156 | -43.38293 | 2025-10-19 12:19:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 46bd04d9-bbda-3bb2-aab0-208b277013f2 | -10.86833 | -43.94991 | 2025-10-19 12:19:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| ffbab55e-a3c6-3507-9eb8-5a953d7b8aca | -13.87756 | -45.53518 | 2025-10-19 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| a8387d68-5cdf-372f-9335-85ed2d1b9dc3 | -12.94161 | -47.33471 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| f0593665-280d-326d-bb42-8dfdbf1e0759 | -13.66081 | -47.18885 | 2025-10-19 12:19:00 | TERRA_M-T | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 1e226cd1-3f9e-36ed-8d06-0cb34cc7cf03 | -14.48008 | -45.61456 | 2025-10-19 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| cc1116e2-2a2c-305e-964f-59bc98a16688 | -17.4977 | -42.06449 | 2025-10-19 12:19:00 | TERRA_M-T | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.3 |
| 85e0942e-b2fa-3238-a813-5af44f84797d | -8.5543 | -44.56954 | 2025-10-19 12:19:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 784f0f99-8253-3224-8fa6-091cbabb5124 | -10.85916 | -43.93479 | 2025-10-19 12:19:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 2bef4a17-79a3-31cc-a8ce-f46a8af7e24b | -10.57289 | -43.38444 | 2025-10-19 12:19:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 3c39493b-306e-341b-9f5f-c65c187b8ea7 | -8.86225 | -45.99336 | 2025-10-19 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b392a620-3942-3b48-a8cd-100867746e79 | -12.01488 | -41.48746 | 2025-10-19 12:19:00 | TERRA_M-T | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 178.4 |
| 45f8c778-c4d4-35f9-ab15-b025ab7fe656 | -13.16929 | -42.41796 | 2025-10-19 12:19:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 51.8 |
| 6992dd7b-c1d2-31cd-850c-ebc0c86fc7a3 | -13.88924 | -45.52446 | 2025-10-19 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8c0c9dfb-031d-32ad-a7d7-314d8a279a09 | -13.94053 | -45.60518 | 2025-10-19 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1efa72c1-2e7f-3e73-b941-f1fa38b9b50f | -15.6899 | -42.58897 | 2025-10-19 12:19:00 | TERRA_M-T | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 2feb50e0-6718-384d-9766-38cf57354bc6 | -12.96642 | -47.28942 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 5373e35e-0472-3212-b6a6-0117a351e29d | -12.97552 | -47.2907 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9198f188-2dce-354b-9263-eab0acc6fed3 | -12.97952 | -47.26194 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 0dc3ccbb-1088-3b4d-85ec-f186d33f4c9a | -8.30373 | -43.38235 | 2025-10-19 12:19:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.9 |
| 75c2eb23-eb85-3a58-bcb9-b95c562628c0 | -14.4898 | -45.60931 | 2025-10-19 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 2827f617-e89b-36cc-adbc-75eb190071dd | -12.30182 | -42.70481 | 2025-10-19 12:19:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 55.1 |
| 88938f16-c74e-3f6f-976b-7be3a0f95afd | -10.49482 | -43.36824 | 2025-10-19 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 30f14916-422f-3541-a73b-896628aa1de0 | -15.68953 | -42.57361 | 2025-10-19 12:19:00 | TERRA_M-T | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b0eef4a4-0844-3b84-9912-e3065d1d2d22 | -11.80136 | -42.72073 | 2025-10-19 12:19:00 | TERRA_M-T | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 34.9 |
| 36c0906a-dbcb-3293-86f5-25d39c90b5e8 | -10.85325 | -43.95641 | 2025-10-19 12:19:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |


[Clique aqui para ver as próximas entradas](README63.md)
