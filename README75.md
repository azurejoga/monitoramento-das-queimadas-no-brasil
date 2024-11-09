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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cf16258-03f1-3c8a-bce6-6f46e2302251 | -5.45112 | -44.82259 | 2024-11-09 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43930c97-9e1a-3a19-95a8-9628c29f0194 | -1.34494 | -51.41078 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d12a9b91-ae8e-3d04-9eb5-4564bc411bdf | -2.80533 | -51.49374 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18ccb228-b69b-3ed0-af5c-ac9f62f2b182 | -2.77325 | -52.86746 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca7b4220-de25-34d0-ab8b-a25691cd73c8 | -2.84145 | -52.90991 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9673ee0c-e0f4-374c-8d01-1e229248a8b5 | -3.51354 | -51.67572 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49c6ac32-a1db-3a79-b40a-a78f28c4a5dc | -1.75996 | -52.68471 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c890ed0c-0b9e-3900-a8d1-21fb644aad7c | -3.10996 | -51.28933 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 571c47bf-2719-3485-853a-4d1896de8b7b | -2.24897 | -48.22551 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 516b3925-54c8-3627-9d56-ff47aa159c31 | -2.69464 | -51.69014 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b01d8d2-b16b-3192-8674-9be30bd874cb | -3.35607 | -50.12501 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0e482f2-a17f-3e8c-8937-d9022b6085bb | -1.59524 | -52.48508 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16d6c371-34d2-310b-a60a-34cc6a792d1b | -3.24634 | -50.71857 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 505f16cf-b772-341e-b36f-a2edb64de527 | -1.51398 | -52.18447 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ed57f591-8888-306e-8462-d6d2e8393667 | -0.04467 | -50.79912 | 2024-11-09 04:55:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10bae1da-a4b1-3902-956a-04088678bc6c | -3.07153 | -50.56799 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e58470f3-8ac8-308d-a297-4d7dcab9c3ba | -3.35351 | -50.26191 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0e1db3e9-d68b-3261-980b-fc0fda97304c | -2.18501 | -53.64133 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cc536a18-4432-3c45-8e65-2e4e6fa34748 | -3.56112 | -43.5742 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 541cedaf-41b4-3a00-8daa-c05d1b44e36c | -2.58457 | -53.98504 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43b57307-e900-33c8-b5c4-a26e3752553c | -0.93753 | -51.78332 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39e995bb-0aa5-35df-9e68-8206cac3c3a5 | -2.31328 | -50.66766 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 702b22fa-1ae9-309b-8dce-6288cdb37457 | -2.23492 | -50.52442 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c00b06ca-5164-37d3-ae14-351b8a703e30 | -2.42304 | -48.94021 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8aee4cc-d362-3b01-84b8-7a7d61776ae3 | -3.73802 | -50.45081 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 625bce90-cd60-3d8f-81e0-fab50b0bf6c8 | -1.23881 | -51.77853 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| beb68adf-f3f6-35c6-9f0a-9bde5d121c89 | -3.10952 | -51.35372 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfa598a9-f603-3148-a7cd-31cdfcddcfcc | -3.6986 | -54.61583 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c8e54fa-3f66-39cb-8c46-db4b9d7553cf | -3.28755 | -50.18344 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b994ad7c-430d-3827-bb66-ac79789d8626 | -2.63496 | -46.03239 | 2024-11-09 04:55:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b8f8fe1-bfbf-3959-9afa-ce861b333a31 | 1.00948 | -52.217 | 2024-11-09 04:55:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa28db42-7d92-3028-a3fe-2917e6fb02e1 | -2.23762 | -53.7773 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94185cd8-178d-31aa-80cb-90894be33c88 | -3.54902 | -43.56207 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4d8c8b02-8873-34cb-9aee-52d676dc83ac | -6.18469 | -45.44184 | 2024-11-09 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fbb1cf48-a0a3-3fc6-a5a9-8cf0b982808a | -3.4409 | -51.11354 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eaaeac5b-e917-3aa3-b4f5-981d24525c18 | -2.18783 | -53.25642 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b995ccd-624f-3ec7-bdba-6f96cd3d2890 | -1.48432 | -51.74758 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e4d1e015-d427-3d65-bcae-d13f91dc186c | -3.40677 | -50.01529 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 018289a8-dc2a-355d-8acd-0165ec850ada | -4.11209 | -50.44328 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2afe9c8-8ab6-3a6a-a832-198247f584ec | -4.21081 | -48.68563 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f865bfd0-2767-36e2-8c40-0e2a470335a4 | -2.23361 | -46.50212 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5119c38-d8fb-396a-b9c2-73f584598245 | -1.24732 | -53.3845 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff66f948-a4fc-3e86-95a0-ba45098b3fd8 | -4.49251 | -48.49312 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b331a94-0f63-371d-9d81-59d3f1cd82b0 | -1.22813 | -51.75876 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 06d1c5b7-bfc0-31fe-bd06-8c05e48edfcc | -3.15676 | -54.47704 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b640a4a9-2053-3bdb-86cd-2a90312a1921 | -4.54013 | -48.64197 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97c20635-d612-3165-93f6-10bb30fe3e3a | -2.76994 | -54.05302 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 949a257b-a954-3a83-b1a2-6b72abeaab11 | -3.07864 | -50.5691 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 53ed8c37-be3e-3ce3-94d9-b510b46cdddc | -1.51732 | -52.18499 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 31859b2c-e110-31c4-b794-9f073f92a284 | -1.42447 | -53.91074 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f792903c-853d-364b-9ad0-510e5e355890 | -2.19084 | -49.12526 | 2024-11-09 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f28b8e22-8d58-3256-85bd-214245a2d7e7 | -2.09939 | -51.09626 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2004be9-53e4-3526-9254-9beecc3df7ee | -2.94082 | -51.49987 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 286c20a8-c621-3b4b-9213-626ac1f4aa1d | -2.83426 | -52.91235 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbe23840-95c0-3eaf-8482-8a0be0f1a3a6 | -2.28347 | -50.65109 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33357e18-1346-310e-a0af-d41245623c95 | -2.42735 | -50.51534 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73a7f885-17ee-3544-8d16-d0baabfc7ac8 | -4.09011 | -48.85083 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1470ee83-c0ba-3723-9727-32bced19a3c6 | -1.23596 | -51.75272 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6eebef46-d6fd-3365-a436-f162a0910527 | -3.59004 | -47.34983 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 0b5d8bfb-d5e4-3e68-bd2b-2567aa160f87 | -3.26524 | -46.31562 | 2024-11-09 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 558c34fa-f4d3-324b-96fc-eb8bda77b354 | -3.6121 | -48.92004 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ab27f357-f36d-31c4-8529-12f5f95c12e3 | -3.15574 | -51.12154 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dad6b523-e72c-3d41-98ae-89c5cac178c7 | -2.27164 | -50.68113 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48a6e285-1cd7-3283-b2b0-2e3225d7d578 | -3.66837 | -50.22431 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6fccd606-949d-3327-a47c-6b28e85fb32f | -2.81285 | -52.96203 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4a08d79-701a-319e-8092-e3e46889d461 | -3.64389 | -49.87983 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d5535f7-924f-3221-a463-8a73771a0fcd | -3.83963 | -50.03484 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45a505bb-e108-3c9c-8815-da64773b66d4 | -3.83594 | -50.0343 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b52e020-543b-3218-8df7-3515330a892d | -3.09078 | -50.95533 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9b6def1-1b61-3268-b056-3a6c20fe17a3 | -3.96229 | -48.12954 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9365014-f43a-3972-a9b5-ec400223cf64 | -2.26592 | -47.86904 | 2024-11-09 04:55:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 619e9ad8-9876-3891-9cc1-20085613ae75 | -0.91215 | -51.65992 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c6a16a3-baad-3ad4-afe8-193d7b31419a | -2.42041 | -50.48991 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d1dd121-bc57-3b3f-b7ce-267aaf2b36b2 | -4.29535 | -48.64559 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ec7c38d1-a2fc-3fa8-aeb3-1aac10c0de30 | -3.97213 | -48.17705 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 644d1179-accc-362b-b784-8d143a8760df | -1.37922 | -52.19928 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 649e53f7-9400-377a-8ac1-ea6fb69ddf8f | -2.842 | -52.90645 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5e0a76b-f84d-35ee-aed4-be8b5b9d19cb | -2.69407 | -51.69377 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 672fd093-03c8-3896-9275-0f66df42679a | -3.34235 | -50.35763 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 938fdebe-9cbf-3f0d-8f37-763687d95e6d | -2.72832 | -51.72079 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73a4738d-9eb1-3775-b08e-7b4b06875bab | -3.24001 | -50.2715 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d8e16006-5ee5-3542-8af1-931ebdaf3523 | -3.05622 | -51.06409 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97c35a38-6eb5-354c-8880-9d385cec40f3 | -2.8447 | -49.43685 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f1d72db-7bc9-35a9-9692-b5eeb3b923ed | -3.11981 | -53.1199 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a6285631-d035-3182-aa43-ce2ff05ef706 | -2.93811 | -51.0509 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3059f75-1d47-3660-9bf7-3623c5050aa5 | -2.54398 | -47.12439 | 2024-11-09 04:55:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f7ea2171-017f-3afb-91e0-434e8d9ac9ee | -3.90208 | -50.3037 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9105f59c-28a8-311d-9f3d-956d1d2fbf0d | -3.91208 | -52.40759 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0453e15b-1de0-32b8-9799-41fc1f70cd8f | 0.62503 | -60.08704 | 2024-11-09 04:55:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8427874b-c501-39e8-ba58-8d644bf23e0f | -4.54419 | -48.64256 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e76b99d-c826-388e-ba8e-120d522652af | -2.93483 | -53.9045 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa47f964-6d28-3140-8ab1-8ff51b7884e2 | -1.54071 | -51.92649 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d39840fd-f3e6-352e-89a6-e7b50ad1f7d7 | -4.21236 | -46.69496 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a83f8bd-2bf0-3aa8-8133-76f706c5684f | -2.58238 | -53.99899 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffcf9932-7954-334c-bfd0-84dbf5095412 | -1.48488 | -51.74402 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| deda7656-cd4a-31f5-a68b-da47d1dbf2c0 | -5.66528 | -49.99952 | 2024-11-09 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a329a71-38e8-3170-beab-e528c9243978 | -5.55438 | -45.83147 | 2024-11-09 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e0a0f39-54ac-3d1f-b2d1-e1e27505651e | -2.39585 | -53.86587 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c852668-c5a8-37e7-9be4-0dbef542a10d | -2.52815 | -47.38359 | 2024-11-09 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87021522-042a-3cde-979a-f4562e2600d1 | -2.71309 | -51.99752 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README76.md)
