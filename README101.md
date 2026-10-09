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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f595d12b-be27-3059-9e8e-c9cea6d4a17a | -11.65384 | -43.6804 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7dea3c22-1ef5-3565-be36-a92122125c07 | -11.25927 | -46.26723 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5cfbba3d-487d-347e-b2bc-3fff4616e851 | -9.95599 | -55.33661 | 2026-10-09 04:27:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ce8391d-f853-3a09-9f4a-a88e15fdf170 | -7.59853 | -46.76635 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f39c17b7-7d16-38e3-914d-fef5e029e090 | -10.24692 | -49.67754 | 2026-10-09 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a55895fb-2fd0-3596-aeb8-a55ae9aa1fd2 | -11.00442 | -45.41525 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb60412b-c92c-37f8-8b3d-523f0a096325 | -8.33258 | -49.12738 | 2026-10-09 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b289a00d-b895-33da-bd7f-d7f134f45e9e | -5.99116 | -55.37056 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f771388-62a0-31f2-8aad-14257ab53ea7 | -6.76425 | -48.17028 | 2026-10-09 04:27:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99cf2341-724f-3052-b86e-94b2bfefac38 | -9.01992 | -44.37323 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ed4cbcf-95ce-3da1-ba9a-d1d1d474fd81 | -6.99847 | -59.10001 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d274c212-8d6b-30c4-9834-e34c0a31bcfb | -7.90949 | -54.72023 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 24574e1f-8e69-3348-be83-1f6dc14d6a79 | -9.85912 | -45.73294 | 2026-10-09 04:27:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc8506f5-e343-357d-8a2a-7cb6662c25a3 | -11.85215 | -43.58912 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47f7b218-a8eb-3100-958c-4d2275b02919 | -13.01857 | -48.52559 | 2026-10-09 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8fb04ac-d03e-39ab-a6bf-690ee08ef2b2 | -11.83477 | -43.60369 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e555479-a094-3f09-acd4-37130c668a5c | -10.93251 | -45.38139 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c516871-4d54-38d6-8168-80b7aea401e7 | -13.16623 | -46.86986 | 2026-10-09 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3297ac30-08cd-3f51-ab36-61dfbb6156f2 | -8.25384 | -54.72593 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a372782-f2ff-38b7-a76b-81d47e05299b | -8.74152 | -45.14713 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 50661523-4a3a-309b-9987-454b6c0058d4 | -6.00638 | -53.49571 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2ff0bf4-6c03-3ca3-be46-519f4d264a77 | -10.86246 | -45.54437 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d060bd7c-f816-3871-b752-dba07b251a47 | -8.90269 | -45.24348 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70730c03-81b0-3619-8eef-193f891c38ba | -11.66073 | -43.686 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c7970079-8ce0-364e-8f01-696201c81547 | -6.42188 | -55.19718 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89d397bb-c575-35a6-9cc5-6967c0c87bc2 | -12.2159 | -57.09623 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17062a50-f1d5-3ecd-9765-79361d789ba6 | -7.08717 | -52.69047 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe5db51a-6e4d-32c2-a890-238fdd47fd10 | -8.16371 | -46.80614 | 2026-10-09 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58d9b5d4-a9b7-3093-a5ed-9ceb528b3776 | -8.97572 | -45.91008 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94959294-b282-35a8-9733-9a644ee2bab1 | -10.12048 | -52.19976 | 2026-10-09 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6afd39fe-56cb-376a-b087-b248fbbadd07 | -11.20768 | -44.87567 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49573ead-7860-379f-b7ed-057d995c8967 | -12.22119 | -57.09718 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 271.4 |
| 30dccb0b-ef1e-337f-8e8f-5f2164c7dfd9 | -10.87796 | -44.80484 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 159a233e-5809-3264-9156-ac604bcb2ea0 | -13.19197 | -54.36973 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 41d82310-4507-3c08-af9b-ff6a46d30c5c | -11.74721 | -61.07196 | 2026-10-09 04:27:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b1a41f76-7d20-3323-99e7-d4ae88c59ea4 | -6.99084 | -59.10459 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f54c1dc-8395-3c28-8e8a-89204f5d2791 | -12.2087 | -57.10542 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab7cc37a-8923-3926-9bb1-d52b332fc271 | -12.03439 | -43.44873 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 11958f23-e2f3-3807-b957-5342dfe685a1 | -9.34918 | -46.57822 | 2026-10-09 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52825c2a-9670-30ad-806c-65cf94508c0d | -10.90002 | -45.527 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 835c5c43-3158-3dc7-8a77-15c5cedeaa84 | -7.25483 | -48.06287 | 2026-10-09 04:27:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 261d5919-27bf-3fb1-ad94-e7c89f1130c2 | -12.02675 | -43.44741 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32d5c15b-9f33-32d5-96ce-800a4bf96659 | -13.1588 | -54.34707 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 73412426-bbba-30e4-87e4-d4c558555742 | -8.96766 | -45.15868 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 88598c94-e761-3dfe-9206-b7aa5052820d | -13.1618 | -54.33023 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48372e16-481b-364d-8fb3-c67cf07425f8 | -11.2255 | -45.31886 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5db3a634-a286-39b0-a93b-eda91884bdff | -6.10065 | -55.6981 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97c633a1-cc79-3017-b4ab-5622b61c33a9 | -8.74549 | -45.14392 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 682f3113-ba21-3f20-814d-ab80bfb5996a | -12.2339 | -57.11078 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b2e3c3d9-c6d7-3d42-ad58-df84d3bb23da | -8.72623 | -45.15617 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97dbc272-0dde-35e1-a120-882e4eb59e2f | -6.12534 | -52.73034 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07adad7e-dace-3dcd-abc4-33361f45335f | -11.64373 | -43.69773 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f603c780-fe02-3bc6-b7ce-e93f977ff5b6 | -11.66138 | -43.68137 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0b9ea287-09e9-345b-9bf1-868c562b211c | -9.12072 | -45.83064 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 599de725-99a1-3637-ad61-97e2edc7d388 | -10.3014 | -46.59887 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b13edc1-043b-3116-a9ba-6d33d640bf06 | -11.12928 | -46.16575 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61b74efb-fafa-352c-ae44-4e63ae6b60e7 | -9.02552 | -44.38905 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a637940f-f4a5-3265-8ab1-0d2f0e234fb3 | -12.53832 | -46.5268 | 2026-10-09 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc03a411-f558-39cd-979f-ca3701ff2352 | -11.09149 | -44.03775 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 944afe52-5aaf-3460-a9ac-3853866a3adc | -8.97216 | -45.12891 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14210212-c7f6-3479-a684-cb58624276fe | -10.88326 | -44.7933 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1a67733b-131a-3010-8ce7-1d3093dd8eb4 | -13.36445 | -43.88599 | 2026-10-09 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b06805a-8ee5-363d-bd7d-611bf71f33c5 | -11.99976 | -43.47287 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81c8fca7-98f4-351b-a659-c23ff8dc02f6 | -5.95256 | -55.34414 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 503dc1fd-58d5-3bfc-9ca7-3451e784c229 | -8.29621 | -45.44271 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fc4ca80-e6cb-3135-aa08-e8cab92dfc89 | -11.38683 | -55.0951 | 2026-10-09 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c9ffe5f-da03-37a2-bdef-da15291887c7 | -13.20594 | -47.87367 | 2026-10-09 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0776e9c5-e763-3f6f-b24d-d1b798d5dc22 | -8.06847 | -45.64246 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ddc58af-27a8-326a-afcb-4669ca5df4c0 | -10.67714 | -58.73876 | 2026-10-09 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e198b26f-642e-3784-89c4-2a8c675d26b0 | -9.02962 | -44.38557 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed2d834c-f008-3f25-b443-83e45dd7fbb4 | -12.17702 | -57.09919 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d2e7e20-e07f-36f5-85ff-7f51a385b707 | -13.16836 | -54.35207 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82406cd7-09b2-3396-9b20-8fdae4c088c9 | -9.29037 | -47.43398 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8f0309b-3091-354b-84ef-72e1e330ae94 | -12.22131 | -57.09108 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 291a551b-1c32-34a2-805f-0c25f09ad886 | -10.40643 | -47.28151 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c399582-5d82-334a-aef9-f4f4054d81ff | -10.91588 | -45.39848 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78c7c3a9-9f42-3025-9069-8288326cf1d3 | -11.08984 | -43.99733 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b1b2e528-ab3d-31ca-b76e-6b9ab5338528 | -9.83113 | -47.4571 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a868ba49-f16a-38b7-91ec-595bb0b7c863 | -13.59445 | -48.58418 | 2026-10-09 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8b947a0-483a-362d-b70a-698b091cf13d | -7.29156 | -46.15763 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6dfb746-8356-3f11-8437-32fa2a023bba | -11.7488 | -61.073 | 2026-10-09 04:27:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e2ab3fc4-e415-394c-a873-24620939b229 | -9.89076 | -44.79976 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c400ce6-924e-336d-a316-767c740e1f86 | -13.1259 | -46.32462 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e25937cd-91fc-30f0-a655-17ef1b9f018c | -10.98594 | -47.79663 | 2026-10-09 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e50712d0-b742-3f38-b0dc-2668d991f5f6 | -6.49175 | -55.96051 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10a94403-d088-3b8d-b028-e2a23f311ee0 | -12.21527 | -57.0996 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d01582f5-7210-3f72-a36d-a78e811852b5 | -10.27943 | -47.83285 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50ab0eb4-0c6e-3f96-9a98-49ba088b84ba | -8.78934 | -47.26439 | 2026-10-09 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ab38d2e-e214-3255-94a9-b56f10699ec7 | -8.84309 | -45.42233 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1cdfbf59-f7df-3f8e-af70-dfeaa34d738e | -11.61044 | -43.71665 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5a43f423-a7d1-39fc-96de-43e0a00f448f | -8.18582 | -46.35895 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8415571-c444-3460-9b08-a7fecd115fe2 | -7.84226 | -45.15883 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76b2112f-1856-387c-bec8-aa234e07ad44 | -13.13003 | -48.57315 | 2026-10-09 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd0fd9c8-5743-3756-becb-dcdf0462f536 | -11.01007 | -47.86193 | 2026-10-09 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b055375a-6119-3ef6-9a36-3e145e96c05e | -6.24394 | -52.85841 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9bf755d0-eed2-3d7a-954b-4fa303ae5003 | -13.17102 | -54.35377 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f03f90b9-5220-3a6c-8820-992b6fd4e43d | -12.2325 | -57.08981 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 66da3464-bedc-387b-b8ac-201d266f0c53 | -11.25713 | -45.24892 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b31ae387-9aa1-3002-92bd-35705f152a02 | -5.99286 | -55.36074 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2ad2a3b-50bb-3b1b-ae8b-362dc21439ad | -5.21677 | -60.04794 | 2026-10-09 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README102.md)
