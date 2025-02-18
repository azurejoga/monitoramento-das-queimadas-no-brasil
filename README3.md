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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 577face5-41bf-3988-b830-9fd5e6330a8f | -6.60892 | -36.17736 | 2025-02-18 03:23:00 | NPP-375D | CUITÉ | PARAÍBA | Brasil | 2505105 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f70d4d8-1423-32a1-84f5-f3db31b18719 | -7.65391 | -37.05981 | 2025-02-18 03:23:00 | NPP-375D | PRATA | PARAÍBA | Brasil | 2512200 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 163a41bb-7ac0-3638-92ac-8ca097b73648 | -7.47539 | -34.84199 | 2025-02-18 03:23:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 21183a09-b845-3c35-af20-ae52a1a83ca9 | -10.18023 | -36.46271 | 2025-02-18 03:23:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc08c79a-dd58-32ef-8b18-4ebe4c1a0617 | -10.8247 | -37.1654 | 2025-02-18 03:23:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8297d5d9-11fb-35b8-b7bd-1c1e0a9649bd | -17.76538 | -39.76942 | 2025-02-18 03:25:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 39f79ecd-5977-3fef-99da-942e51cc94a2 | -10.61002 | -45.10902 | 2025-02-18 03:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 342e1218-07d0-35f1-9ae7-a55aeceb94ae | -12.84549 | -43.82763 | 2025-02-18 03:25:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35d2bda0-d035-3125-a448-c2d12ca810c1 | -16.35129 | -43.69829 | 2025-02-18 03:25:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26f3eef5-5f26-3820-b2e9-1202ae669602 | -12.84275 | -43.82762 | 2025-02-18 03:25:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d33f572f-1c02-3819-9837-a66fddc4a467 | -16.34555 | -43.69682 | 2025-02-18 03:25:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4616fa17-07a6-3654-9bcc-568d62d6acf1 | -17.52684 | -39.41302 | 2025-02-18 03:25:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 57a2de70-b0e5-353d-8358-788c0da10dd0 | -13.28371 | -39.80096 | 2025-02-18 03:25:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6271b1ed-cc4f-32df-b899-2763a9ff8bf3 | -12.84996 | -43.82407 | 2025-02-18 03:25:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba4f93be-dba8-370c-9db1-36aa80f09c74 | -12.84895 | -43.82894 | 2025-02-18 03:25:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7feb5a43-e4c2-38d9-8c06-59022e95f237 | -12.7818 | -38.5001 | 2025-02-18 03:25:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 20586853-11b7-3c81-8886-bdc4df5d6127 | -16.90022 | -43.66002 | 2025-02-18 03:25:00 | NPP-375D | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c980c4cf-d839-3c6e-a351-54a959677e23 | -11.59099 | -44.8514 | 2025-02-18 03:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b94cd9b-358e-3f17-92ca-9a32815a3b1d | -20.21165 | -40.73169 | 2025-02-18 03:27:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7e1df1be-cc5b-3f62-a15b-f97c84f6a9ce | -19.96984 | -45.164 | 2025-02-18 03:27:00 | NPP-375D | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e88ba1e1-0567-37f6-b4d3-f84c9c1a1c9e | -22.89871 | -43.75252 | 2025-02-18 03:27:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 80e8d7c7-a8d5-365e-ae50-0f466e2d1450 | -20.41438 | -43.55153 | 2025-02-18 03:27:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f6959978-301b-3f4d-977d-4a1ce6f79d9f | -18.43981 | -44.48909 | 2025-02-18 03:27:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e15f255-445c-3bf2-8f56-5a7f008fe8fe | -18.77388 | -41.93149 | 2025-02-18 03:27:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 063fe2f8-4532-3a9e-bfd9-14dcd1ed6892 | -21.41669 | -48.55003 | 2025-02-18 03:27:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5ebaf9df-2404-3d9c-ae85-41691616d2bf | -22.54214 | -48.81572 | 2025-02-18 03:27:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ed740bb-8e35-38f3-aad7-bfd07cb64039 | -20.70181 | -41.70433 | 2025-02-18 03:27:00 | NPP-375D | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5b8c17a1-8ee8-3693-a9b3-44bfa0935356 | -21.38259 | -48.56905 | 2025-02-18 03:27:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e4445be1-7844-3149-81d1-c0fc14c52f4f | -20.41883 | -43.55664 | 2025-02-18 03:27:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5d56b34c-2bf0-32dd-aaa3-75982fe11fb9 | -18.44564 | -44.49034 | 2025-02-18 03:27:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0848b935-cc00-3b7e-8ed5-3195825911a2 | -21.38076 | -48.57627 | 2025-02-18 03:27:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 19b1f713-35cc-344b-a63d-d361e92e3fd0 | -19.17052 | -40.13409 | 2025-02-18 03:27:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fbe4aad2-3c17-3c50-8b0c-87927f54ceec | -20.60948 | -40.98845 | 2025-02-18 03:27:00 | NPP-375D | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 44e49440-624b-3a5c-9e82-2dec751586bf | -19.96396 | -45.16263 | 2025-02-18 03:27:00 | NPP-375D | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fa2e43a-32b4-3af9-8c68-80c53f0e573b | -20.88797 | -40.79701 | 2025-02-18 03:27:00 | NPP-375D | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 12859c18-cc8f-343a-87eb-b88c4c4fc96f | -18.77264 | -41.9375 | 2025-02-18 03:27:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 46b9af2b-e7ac-33d5-b130-675c352b6086 | -21.37383 | -48.57467 | 2025-02-18 03:27:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8e6663f1-fdf7-30a4-a046-76e5734f3ae4 | -18.92736 | -41.93745 | 2025-02-18 03:27:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b722fb20-b275-34a9-8be6-c2c003a9915d | -21.41504 | -48.55662 | 2025-02-18 03:27:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9808a554-3a8a-3789-aae7-3d1256aec58b | -20.41959 | -43.5531 | 2025-02-18 03:27:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a46a46d2-8195-3ac5-89f5-9864eac6c050 | -19.9629 | -45.16736 | 2025-02-18 03:27:00 | NPP-375D | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7a537e0-6e23-3ba9-8f1a-f70a898da311 | -10.60647 | -45.10065 | 2025-02-18 03:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5bff779-3f28-393f-9017-5d9c8261e266 | -13.28291 | -39.79866 | 2025-02-18 03:46:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cf9803fe-e0a4-3b65-8fa5-6fa6d78ee8bd | -14.03512 | -41.45462 | 2025-02-18 03:46:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ac5be214-5564-330c-9694-a7c0f388ef00 | -7.65411 | -37.06078 | 2025-02-18 03:46:00 | NOAA-20 | PRATA | PARAÍBA | Brasil | 2512200 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bc0dfa83-18c2-3b66-a94f-169351e760cb | -10.61024 | -45.1065 | 2025-02-18 03:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1325cdf7-9412-3f96-8987-48c588f43c5d | -10.60934 | -45.1114 | 2025-02-18 03:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e6aafbf9-1164-3b0e-959a-4bab97a24ba8 | -12.86314 | -38.36797 | 2025-02-18 03:46:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5df52d5d-4113-3a9f-8f15-34560d389891 | -12.84388 | -43.82732 | 2025-02-18 03:46:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7fdefb2-bf47-392f-a845-cabae759f0b2 | -12.8528 | -43.82506 | 2025-02-18 03:46:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e271a60-6a04-3b5f-8822-10cb90633879 | -12.00154 | -38.16644 | 2025-02-18 03:46:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0792f19d-8633-348d-a2dd-0d4a0f5f19f1 | -13.24671 | -39.9779 | 2025-02-18 03:46:00 | NOAA-20 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3a62383b-32cd-3a65-ba56-26a67cc3b149 | -10.614 | -45.11234 | 2025-02-18 03:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d0f2b297-4e9e-30b7-8ade-f2cb707bac98 | -12.70302 | -44.67314 | 2025-02-18 03:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c78700c8-8b01-3c06-9467-d2dc91bb1b48 | -7.58909 | -37.51553 | 2025-02-18 03:46:00 | NOAA-20 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 61e25c05-929f-374f-9175-c39bf1820b18 | -11.59005 | -44.85315 | 2025-02-18 03:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fcbb9c0-1344-359a-b6ae-e43a53fe7b28 | -4.44128 | -38.05945 | 2025-02-18 03:46:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3e5e5295-cf85-34d8-86b7-7aa3092b92b8 | -11.59194 | -44.84972 | 2025-02-18 03:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e9c60bca-8bc2-3a47-bba1-64063d80bb11 | -12.70236 | -44.67599 | 2025-02-18 03:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a909eca7-dc7e-3b19-85a7-003924c8898b | -4.8074 | -37.6776 | 2025-02-18 03:46:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8c829b0a-c84b-324f-a181-0bbd3d7010e4 | -6.69278 | -42.13382 | 2025-02-18 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 62261060-1885-372c-bb1b-98193d4ccc05 | -5.01312 | -38.5424 | 2025-02-18 03:46:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d83409c7-4213-3f60-8d37-71ef7a10e7cb | -12.84867 | -43.8243 | 2025-02-18 03:46:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf2dfa16-7bc3-3ce2-8e28-8cc85be9b3a3 | -12.32609 | -52.49075 | 2025-02-18 03:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eea02d3-153c-3c55-9894-c31741fa5ac8 | -12.31898 | -52.4891 | 2025-02-18 03:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05903862-63f0-3c64-883a-11a7146b9b60 | -13.28568 | -39.80293 | 2025-02-18 03:46:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c79c1bc9-0e5d-3f30-9742-8164eea3029c | -12.32301 | -52.48397 | 2025-02-18 03:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0f063fb-46a7-3ab7-8993-dea1af7bcf4f | -5.19547 | -35.82225 | 2025-02-18 03:46:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 937b1e54-e2c3-3af9-bfb6-0768b05e7ad3 | -5.15783 | -35.78043 | 2025-02-18 03:46:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4e1603d3-e19b-3dd4-aef0-f895a02f5317 | -14.03819 | -41.4542 | 2025-02-18 03:46:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 447fde5c-99c3-317d-af79-0a83ab1cf65e | -10.60845 | -45.11634 | 2025-02-18 03:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20cd7774-f574-3749-89ac-688cfd463756 | -13.28231 | -39.80233 | 2025-02-18 03:46:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6e4a51da-b03e-3681-86a7-3d55c6c3e061 | -6.61026 | -36.17913 | 2025-02-18 03:46:00 | NOAA-20 | CUITÉ | PARAÍBA | Brasil | 2505105 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a326a336-0a82-358b-8674-cdbfdb1acbaf | -10.60558 | -45.10556 | 2025-02-18 03:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 43108ca3-c443-34d6-8159-8465d9cc4af0 | -8.40229 | -36.59932 | 2025-02-18 03:46:00 | NOAA-20 | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3f9951e2-d139-3363-83bf-8e71383ed26d | -12.32141 | -52.49126 | 2025-02-18 03:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6af0270-6646-3888-9f49-20df52f9c935 | -4.53695 | -40.15493 | 2025-02-18 03:46:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2c485ca7-99c5-341c-baaa-5013ee3ff4bf | -11.59087 | -44.84851 | 2025-02-18 03:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 565e9c19-00df-36ca-8ce9-5eec1ad97c52 | -7.47621 | -34.84261 | 2025-02-18 03:46:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f004819f-f08f-316c-934c-bafa49f50de6 | -12.84801 | -43.82808 | 2025-02-18 03:46:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b053e8b8-cb2c-35e9-8529-ad43e965e6cf | -5.2492 | -35.8698 | 2025-02-18 03:46:00 | NOAA-20 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ae86fc8f-2967-3530-8b86-cd1125e1079c | -11.59538 | -44.84935 | 2025-02-18 03:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 509643e1-757c-3b48-a536-7e885cafd91f | -5.83805 | -37.48011 | 2025-02-18 03:46:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 42699bfc-a66a-3198-9a13-86c4296eb188 | -12.32852 | -52.49286 | 2025-02-18 03:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59f4ca04-4dc2-3c9a-9bf6-16dd689f4a96 | -12.66938 | -43.41593 | 2025-02-18 03:46:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12c1a0ba-5d0a-3808-8e54-8f0417f0c81a | -7.4771 | -34.84301 | 2025-02-18 03:46:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c8d9ce64-4b6b-3e98-8492-1d5c76fcfe27 | -12.33319 | -52.4924 | 2025-02-18 03:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43594565-db27-3f05-8ec7-9823e567be9f | -13.84799 | -41.39954 | 2025-02-18 03:46:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9d7c6630-f8da-33e5-a7ec-e3a587288259 | -12.41739 | -43.8047 | 2025-02-18 03:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32fbafa6-bca4-3877-8578-cdf601ac4e50 | -7.54871 | -45.87084 | 2025-02-18 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d068cbf4-7d0c-3623-a0b6-3f1b806724f2 | -15.4766 | -42.16998 | 2025-02-18 03:49:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78173935-88a7-3506-bb40-172f21a00270 | -10.42366 | -39.23246 | 2025-02-18 03:49:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c7f616a7-c8e1-3fc6-99b6-db925c12a4e1 | -19.92899 | -46.51615 | 2025-02-18 03:49:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9441c9d-c4d3-38ee-bac6-572c9014db2f | -19.38929 | -41.56127 | 2025-02-18 03:49:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a9a07f9c-9d15-3abc-be21-545dfc821805 | -17.52835 | -39.41276 | 2025-02-18 03:49:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e05189d2-72e5-38da-ad18-2a7cc0f61ad0 | -14.98061 | -50.78402 | 2025-02-18 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52b98107-a0e6-36c1-b2a2-d4b574d1df6a | -20.45696 | -44.77874 | 2025-02-18 03:49:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7fcc12ad-62aa-3f53-bb06-9324f4e22eac | -21.6265 | -43.46965 | 2025-02-18 03:49:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b97aa14d-9f1d-315b-8f34-ac33a102e514 | -20.49575 | -41.62284 | 2025-02-18 03:49:00 | NOAA-20 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eb519f3d-3272-3ea8-b860-72745abb8147 | -20.60687 | -40.98761 | 2025-02-18 03:49:00 | NOAA-20 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README4.md)
