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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88926678-c0bb-33d7-bfac-9ad8a14c72c8 | -5.77787 | -47.18098 | 2026-09-19 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f007561-ecac-3964-890f-698995368582 | -8.4728 | -44.51776 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd8cb491-4622-3162-ba79-405a65c7be44 | -7.87026 | -45.12251 | 2026-09-19 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad885cef-db5c-3965-90f9-419f1a0032f7 | -7.86831 | -46.4426 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6da661e9-e381-3e74-8179-350e31d7ae59 | -6.01209 | -51.79536 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f772ca63-954c-3ebc-97d0-9ce427a440e3 | -7.76374 | -46.75795 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 747f19dd-ad71-308e-9457-3fc70482d897 | -8.72132 | -44.87302 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42c6870d-4d63-398e-aaff-864407f63a4c | -1.09595 | -48.06228 | 2026-09-19 04:38:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb6f1ba1-0882-3309-ad1b-701dad0b687b | -9.28526 | -44.38396 | 2026-09-19 04:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c2c41ff-b85f-350f-9b77-ef54c53f33fa | -7.67357 | -46.1325 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e04f35e-5a42-3c09-bd6e-bd49dfa35fe7 | -7.65857 | -46.11936 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 310a457f-57cc-3738-96b7-6d9c6b34a554 | -8.23609 | -45.59876 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c99a8a97-73ce-32cd-8211-8c3c42aaf8e4 | -7.4031 | -49.84581 | 2026-09-19 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5b970e87-c5d8-371d-a4ec-0819e670988b | -6.66636 | -50.93539 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af85b437-96b8-3cf3-a556-ee116e660154 | -0.85725 | -48.71971 | 2026-09-19 04:38:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfa931e4-05f1-3a96-8b80-30ea946a518b | -6.2264 | -45.18576 | 2026-09-19 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f159ce38-0b0f-3e2c-9b25-ef1cd50cbc57 | -4.35866 | -55.4255 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52e84d8b-6de4-31d2-8a34-12dc5d5ac5a1 | -4.28471 | -48.5866 | 2026-09-19 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b873500-4843-3c83-a5ec-3939d869f0fc | -6.77258 | -47.86136 | 2026-09-19 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e2f5dff-eeda-3684-9ca9-eceadc9071a9 | -7.32496 | -45.33343 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3131fd0f-6760-31f3-8da8-65c83e927da2 | -7.57257 | -46.74852 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b22825d-cb92-3a67-9308-481c0a0d2a14 | -4.82548 | -42.87662 | 2026-09-19 04:38:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f992b012-0072-307a-ad30-0d85ca663117 | -7.65912 | -46.11587 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68765700-0901-3e93-89a5-7ecf9950832b | -7.69909 | -46.12222 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fb706c2-451f-3357-b148-0d358a9b9a40 | -8.12243 | -44.8253 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3e39ecf-bbca-3479-8556-ce6cd5c31925 | -4.50891 | -54.97115 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dee4bf84-9264-3738-9943-e6ea0d97738f | -7.85959 | -44.87675 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d708130-8cc9-33a3-a4e9-338585449214 | -1.19386 | -54.22125 | 2026-09-19 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ad1326c-7211-3a90-aa6c-4f5932e70e5c | -6.37259 | -58.31839 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35c0e00a-ec35-3389-b918-5e89069dc88d | -5.85836 | -51.94072 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 192323d8-94d4-3f65-8b51-dc669f4f183c | -3.54284 | -48.18172 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6e09194-29ee-3223-9fde-86546e5828eb | -8.43011 | -47.50042 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9bc6246-1aee-3a09-b810-47b8664dc794 | -7.09637 | -42.08778 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51f51d08-10ef-38cd-be07-8bc4d492f2b2 | -7.71607 | -44.6348 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5d794d9-b08a-332a-8cdf-552c1ef2b958 | -7.69741 | -46.11121 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82bb0ee6-b7fd-3f89-83bc-14b481636c37 | -3.42727 | -50.66798 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b9a1d11-d689-3b98-aea3-97c71eb6e5ff | -7.77829 | -44.83807 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d75c931b-1f5c-39b3-b025-ff10b3fa69f3 | -7.65132 | -46.10032 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9aaee0e-7086-3f56-9ae2-43dc3dd55959 | -6.98339 | -42.17683 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f101f15e-f919-36e3-b0bc-1da250fcacee | -6.65624 | -50.9234 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4965e70b-97fd-3e19-abca-e2a765a1adde | -5.57217 | -52.01884 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6bedbcd-010f-3a4e-bb94-fdd447c017b1 | -8.76112 | -46.9105 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4d909a3-4b92-3315-8503-68d8aa629088 | -7.2174 | -49.63567 | 2026-09-19 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbcd9ec3-1697-30ff-b5d6-ce6906e80d71 | -7.78229 | -44.83492 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2a39f01-30ae-3556-9564-f3f988aa45bb | -7.76373 | -46.73657 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1cd1725-5e83-3a18-873b-9722c8dcfefe | -4.13237 | -46.86144 | 2026-09-19 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d67bd5c1-e493-3858-853c-95b76cffa01c | -3.49837 | -49.50927 | 2026-09-19 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b7f222d-9e2e-3d43-b7f5-dd02d03545dd | -7.32552 | -45.32986 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c21b69c3-81c0-3532-a3f3-34d5de7ebe0b | -7.40676 | -49.84638 | 2026-09-19 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 952a75fd-a7e7-30b4-964e-59325d2d1fe7 | -8.36934 | -45.66045 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40efeb28-a067-3521-bca2-a88012a4ac97 | -6.66828 | -50.89968 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 593aa1f4-9990-3741-be47-9f631de7c742 | -1.48901 | -54.97683 | 2026-09-19 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07d0c984-c387-35e2-a0fd-392b2079b12f | -5.19292 | -49.32911 | 2026-09-19 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc916801-da49-3fcc-bf6f-eca827a1903d | -6.31884 | -45.6039 | 2026-09-19 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3908a23f-506e-31ec-9ff0-896a58b3222a | -1.62741 | -55.26252 | 2026-09-19 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11d72be6-e960-33ce-900f-72573b200010 | -7.0187 | -47.44031 | 2026-09-19 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f0cbd0d-1b01-371c-a682-5657a394ef26 | -8.38948 | -45.64171 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed3c7654-9b49-3933-b7d2-9a77b9d96113 | -8.83527 | -46.93316 | 2026-09-19 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 555f3ade-1d62-302c-a733-68c928429e7a | -9.00691 | -44.91532 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cca9f326-ff6d-38a5-b002-3facbe2eb5b3 | -6.37414 | -58.31517 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebece48b-bc32-30e0-a7f9-9e524cd99889 | -2.02582 | -48.77776 | 2026-09-19 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63d8b7ed-b4cf-3535-a21d-b5434a8aead1 | -8.23218 | -45.60179 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 482fbc72-f1fb-3243-b1c4-a06101091724 | -5.9788 | -53.58244 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d94bbf3-7235-3418-af5f-6de4983f531b | -4.49003 | -54.98528 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55004d97-3818-3f87-bb52-d1de9d0e36a7 | -5.22781 | -47.56415 | 2026-09-19 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa9032d4-2514-3c7b-9c8d-9c41ca2ccd65 | -6.3844 | -45.83307 | 2026-09-19 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03c345aa-9c42-3c4f-91d2-7b530693378c | -4.06581 | -56.24932 | 2026-09-19 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5d1674f-ef0b-39b2-8722-b53627e82ba8 | -1.59794 | -55.55113 | 2026-09-19 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4a6e2fb-30d2-3566-bcf3-ae085abad0af | -2.60004 | -49.50745 | 2026-09-19 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09d9e8d2-f568-320d-ae6c-c59795969c69 | -6.98197 | -42.1863 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 07f3de5b-770a-3a4f-97b6-6ee3cc39585b | -4.8584 | -48.29984 | 2026-09-19 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c9b14b8-fe35-3ec2-880e-0404d020fbdd | -8.6681 | -45.44171 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 604843ef-ee0f-339a-9201-928a0a4fd985 | -7.60629 | -45.43211 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed820caf-4605-3549-94b9-70cb00a3824d | -9.01093 | -44.91209 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 386ec4ab-dfa8-30f0-9468-b2710b029819 | -8.92991 | -44.402 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a71f8869-5cf8-3f97-b1c0-c9840e47ba65 | -9.47563 | -40.31667 | 2026-09-19 04:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2b1ddabf-c770-3425-b378-1f4f8c4d83df | -4.50556 | -54.97337 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f200ea03-e37f-3bd5-8344-776b740885fd | -7.75596 | -46.72104 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df9cc82f-829e-3da2-849c-2921c6eaa6e6 | -8.75722 | -46.91339 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72b1fd5b-2717-3700-9dee-af5fae016da1 | -6.35912 | -58.28316 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04cf079e-3e85-3ffd-a511-8bca76d189f9 | -2.90637 | -57.80106 | 2026-09-19 04:38:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7e0837a4-0edf-35c0-bef9-b5b5b7980b4b | -7.06912 | -42.1376 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3c92e9c1-896f-3af0-abb9-d625566871bc | -7.09953 | -42.09317 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2cbc8840-5dca-39dc-9132-7a9267d19c83 | -4.50835 | -54.97451 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c6535c8-2536-3c75-bf88-c1259afe22f1 | -8.0863 | -50.9687 | 2026-09-19 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c35ce752-2329-35c6-b64e-772c1c2111d0 | -3.46494 | -50.61605 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbe33d75-4394-3904-98cd-8a08d7abda58 | -4.28115 | -48.58601 | 2026-09-19 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c065e8f2-1f99-378f-ab80-1a8d857d3590 | -7.5797 | -43.44391 | 2026-09-19 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82917252-07ca-30ec-87fb-63f050668306 | -4.50494 | -54.97687 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1519a0a6-1c21-3ac2-b104-ce6f4abfa19a | -5.84558 | -47.04657 | 2026-09-19 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 873fdf42-7c08-3466-abb5-904b426fd84a | -7.63365 | -45.82821 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b59080f9-0fd7-3892-9913-65b8a45616bb | -3.36307 | -50.45153 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0a3fb954-43a6-34cd-8590-b0f86e10000e | -3.76052 | -55.95863 | 2026-09-19 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5759f3ac-8df4-3fdd-b7a0-3924826501bd | -8.44013 | -45.74408 | 2026-09-19 04:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c26031ec-1553-3bee-b2c7-b419fe5209ed | -4.43517 | -55.08018 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc29360d-e41f-3fc3-a4bc-e91250d3a10e | -6.02553 | -51.76619 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c80e8718-8b55-3b08-94c4-842b6153a4ca | -4.49398 | -55.49158 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e3067958-462a-313a-b57b-3157bcf62a7f | -2.95674 | -52.14533 | 2026-09-19 04:38:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 316a2478-a1ec-3552-b4a6-33db523d6970 | -4.12901 | -46.8609 | 2026-09-19 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec33146a-23a3-30d3-aeb3-45f59dea9fe5 | -6.99495 | -42.17863 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README46.md)
