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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6cc6656-7ef2-3785-99ca-9c6d9321666f | -8.77055 | -50.07858 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a7f4c9bc-b324-390c-8f25-0e551dc9db60 | -5.88443 | -57.75428 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3d89dd5-4edd-3ad8-8cdd-9887a45fc212 | -6.91397 | -44.94998 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df148e12-a4c4-3841-9b36-ff009ff31a7c | -10.32253 | -49.96413 | 2026-08-29 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e22bbc16-9d86-3121-bf85-42dc96e5ee24 | -5.31589 | -47.04498 | 2026-08-29 04:32:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fa091d5-48b2-3eed-ad00-d58173df5363 | -7.07285 | -42.20858 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 837cc765-71a7-3c03-85ac-e2eaae4189e0 | -6.3396 | -44.08618 | 2026-08-29 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5855b2c3-3b62-3026-a8fa-3f8f0f404436 | -10.31915 | -49.98336 | 2026-08-29 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb4e6674-535b-3169-94cf-94c12a77722c | -6.37227 | -54.95599 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76d0cc62-ecdb-3e5b-b044-a562ec1208ed | -6.87248 | -42.87923 | 2026-08-29 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5efedc3c-602a-32b3-b657-712ef8d28d8e | -5.40819 | -43.18728 | 2026-08-29 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6520f18e-8e8e-3f3f-b79b-c0ecad6e794d | -6.76768 | -55.66572 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e24804d2-c941-315d-a3d6-a3c95fcd1fc4 | -11.36618 | -45.15998 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b9b46410-d997-3203-af7a-fa82e72df614 | -9.42641 | -50.43385 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74185ea4-7125-3081-a5a4-79ef5314fff0 | -6.75656 | -55.65956 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b59eed43-3d5d-3918-8edc-69b3e69b91c8 | -10.69511 | -48.21756 | 2026-08-29 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 528e4ee1-f35a-3444-9080-fd963b90eeee | -8.98483 | -52.38494 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0212c823-c8a5-304b-80fe-0dbc337c428f | -4.84558 | -45.39626 | 2026-08-29 04:32:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc7688cc-78d6-3d28-8e8d-7ed5c91627c8 | -4.56416 | -44.05969 | 2026-08-29 04:32:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49f311bc-0834-383f-adbc-641de940003f | -6.77447 | -55.66212 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 38e0ebc5-3e01-361e-b9dd-e7c8191c9d9b | -9.21118 | -51.53893 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca2369b5-016f-31e4-b4dc-b660ed78be2d | -9.60037 | -55.10818 | 2026-08-29 04:32:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| decb904f-7c64-313c-b5f8-e34e04c6bf3d | -7.10198 | -42.18441 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c84ee54d-d441-3039-a03a-341b926ceb4a | -5.47841 | -45.1235 | 2026-08-29 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81d67248-d525-3a2f-9b8d-28d086f036d8 | -7.21593 | -42.75602 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e7124520-9158-3931-8e14-aa39883f72d7 | -9.61406 | -55.12582 | 2026-08-29 04:32:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94fd322b-2128-30c5-92fe-278087f5af22 | -9.61339 | -55.12944 | 2026-08-29 04:32:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d9b5d48-9d46-312f-befa-42c7b04525df | -8.58859 | -54.7982 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6d1f278-7aa8-3e42-aa39-8c404d63c705 | -8.59156 | -54.77742 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 949dfe14-3e81-3967-b8bb-41bcdf21a557 | -7.51446 | -55.29659 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1cbc886f-28f2-3589-ab2d-7ffbb6dbf4a9 | -10.53443 | -50.47665 | 2026-08-29 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9010b5b-57b6-3b2c-8ee6-150360fc9209 | -9.46357 | -51.58698 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7768bb0c-beb3-37b1-a08a-f5857b9c2d90 | -7.30149 | -49.54285 | 2026-08-29 04:32:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28dd7113-b7c8-3326-9a95-27a4c13412a0 | -11.21473 | -45.0517 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d428d39c-d620-3166-afe2-9b5daaeda337 | -9.42782 | -51.68866 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90b0e4be-9915-358d-b1bd-2fe221ac39d5 | -3.82899 | -52.41064 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af09f1c1-be09-3710-b876-f47e3cef6e4d | -11.37338 | -45.13572 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bfeede6f-6b1e-3f6a-8094-0e5624599007 | -9.26379 | -45.64394 | 2026-08-29 04:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b01ad82e-8571-3434-82b2-4cce179a1e8c | -3.75631 | -53.35603 | 2026-08-29 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c245b1b6-b9e1-3910-95fb-259692ae59fb | -9.15668 | -43.28477 | 2026-08-29 04:32:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e54525b0-0dbd-3eae-a8e1-902ee2b952b6 | -5.89803 | -57.75706 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4e4b5ff5-8263-329e-92cb-c3859ad0a1c2 | -9.60866 | -55.12666 | 2026-08-29 04:32:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 303e0b14-7d26-3708-9b3f-84b7da3160ba | -2.93667 | -51.48348 | 2026-08-29 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba9ee028-418b-38d6-9723-0e4d55c1df61 | -6.94433 | -58.95457 | 2026-08-29 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 88f4cff2-4e0f-3586-912e-ef8c4b18ef70 | -5.29151 | -50.9387 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33d0ab52-f177-3bf0-abf2-e5cf250b8568 | -6.75814 | -55.65092 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c820151d-7e1c-3bfc-bd53-2bf20817d52e | -8.99315 | -50.7896 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdb49a75-92d5-3ebc-ab70-e49d405e3bc2 | -7.31354 | -42.96061 | 2026-08-29 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 02632fb9-106f-39e1-9eee-c9dd8c690f71 | -8.60408 | -54.77569 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bcfce64-a3c0-34dd-bfa9-5226fb100738 | -6.71267 | -44.42375 | 2026-08-29 04:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 432d295c-7142-3159-a09c-8266ff29148a | -8.16654 | -46.17315 | 2026-08-29 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4431673d-a264-3ae4-8d1b-e84dac066b6d | -11.37728 | -45.13269 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccb48d60-f16e-35c4-93f6-b541f1539f50 | -7.44804 | -50.91981 | 2026-08-29 04:32:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bf1a6d3-d6f3-3173-aa9d-0d2005bbd7b9 | -7.29048 | -49.9491 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54b207fd-e95c-381d-bb28-6145c0bbfc0d | -11.36673 | -45.15643 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fd7397ff-f6d5-3a9e-a23a-e4c85e20108e | -8.60343 | -54.77916 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94f89ead-3f55-38e1-b8e3-bc119ec9e58b | -9.25755 | -57.0726 | 2026-08-29 04:32:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a8eb3d9-7ecf-30f9-b389-e4b6b5fedf7a | -6.93358 | -58.96003 | 2026-08-29 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a53015e5-3749-30c3-9f04-7db0d0f16095 | -8.9925 | -50.79326 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98ef8774-17d1-342a-ac33-57321e5ce593 | -6.76329 | -55.65628 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41734ff0-a414-3e9f-a91a-7901b50e539f | -9.1529 | -49.97189 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d538ac93-f7f5-3c1a-92a4-d7668222414e | -8.11386 | -45.46993 | 2026-08-29 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 515e303d-21b9-3046-884d-43a461aee571 | -4.56749 | -44.06021 | 2026-08-29 04:32:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e9a17f3-0dc6-3261-bbf8-2a7294d7e0bc | -7.05693 | -42.1938 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 509748c5-4965-3b53-ac96-608050ca74d3 | -8.32171 | -47.62802 | 2026-08-29 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8551afa-3a96-3d74-a541-0be96a2aa29e | -5.94219 | -44.78109 | 2026-08-29 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77791758-0613-33ab-a52c-1207d6c4c324 | -7.49803 | -55.2894 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f4c2496-f80c-34b5-8ff1-7d0ce3abbb88 | -8.58932 | -54.75882 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aebb14d6-884f-3e54-b536-55b969aabb88 | -4.6262 | -48.0401 | 2026-08-29 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e9edc9b-f622-3703-821b-8d90b096da1e | -7.25555 | -45.85983 | 2026-08-29 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18fa7ff8-c23c-310c-91f8-d8f1d4212db2 | -5.89856 | -57.75762 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1eef9d9-d73d-3815-b232-7140c98fc52f | -6.63063 | -43.74136 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d2802d46-ac6d-356b-b3c6-45ff0191a5d9 | -11.24654 | -45.07839 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1543cf9-ad41-3f8a-8ef1-9bd62ef306a1 | -3.18409 | -48.02446 | 2026-08-29 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 930c3b09-1dfb-367e-ad69-4195ae655190 | -9.63128 | -48.33268 | 2026-08-29 04:32:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46930558-e1be-37fc-ade8-f54bb97d88c6 | -9.26435 | -45.64044 | 2026-08-29 04:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7bf2403-9a1e-3e1c-8a84-4e4deacef28f | -10.45585 | -45.1453 | 2026-08-29 04:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbaca71e-587b-3607-9fd9-56a1e96c3472 | -9.69112 | -46.55162 | 2026-08-29 04:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3847a307-3cc0-37bb-8ce9-ca809129ba26 | -7.60881 | -47.28529 | 2026-08-29 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18fdf54a-137a-395f-8cca-be3cc3f2b5b1 | -6.90234 | -43.6523 | 2026-08-29 04:32:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9937943-b0e7-3ade-99e9-6c4300c58272 | -5.88087 | -57.77373 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e5e100d-66ee-395a-bca4-e2054d7f1723 | -6.42606 | -55.52469 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b4e0478-bb6d-302e-8474-1d76f466261b | -11.25657 | -45.07998 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 484a9e1b-c62a-35ce-a0be-a04936ae00d6 | -6.58257 | -55.43962 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d79dac9d-e5e9-3e60-a473-948a288d94b5 | -5.88126 | -57.77433 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6b06bfb2-a859-3851-a91f-4de316d81ffb | -5.88495 | -57.75491 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f7dd686d-1e1f-3da0-93c6-f80ef4475a16 | -6.76089 | -55.66932 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0afea193-b043-396a-85f9-7be38c749752 | -6.74701 | -52.45214 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 56fc8d81-c601-3459-98df-4ed1a9f27c02 | -8.0132 | -48.01138 | 2026-08-29 04:32:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9b61c30e-e52f-3d43-b2c1-5370c26e7211 | -8.95063 | -50.80507 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ec80962-5e28-3e51-9e49-6a2066cc6e7d | -6.35286 | -46.10573 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b491a892-ecf4-30d1-bae7-38cef2370714 | -6.75015 | -52.45524 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0477ea41-e3cf-3718-a794-1fdd04ac343e | -6.62616 | -43.74793 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eaf04994-51ff-3bee-8384-729a07ef9629 | -11.36894 | -45.14227 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 556a078e-f19e-3c32-86dc-00ae898d1bb8 | -7.0362 | -45.54369 | 2026-08-29 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 375715fb-1dbc-3d4b-9b0f-7b6913c195a6 | -9.61481 | -55.12411 | 2026-08-29 04:32:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6ee5c99-e282-3447-9fea-6d6d9af058a5 | -9.60583 | -55.10919 | 2026-08-29 04:32:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bffd76be-843e-3a3b-bc7a-bd4aff6df8db | -7.52565 | -40.11552 | 2026-08-29 04:32:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b3bef189-11dc-3325-926e-f0a23b726673 | -8.01386 | -48.00734 | 2026-08-29 04:32:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7eb0b435-9fc7-3986-96d6-fb08a8728afb | -7.12146 | -43.16434 | 2026-08-29 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README31.md)
