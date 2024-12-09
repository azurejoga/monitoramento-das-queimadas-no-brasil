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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9983a97b-408d-336e-b4b9-924f06403d6a | -4.08702 | -46.65425 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 555e04ef-6c40-3cc4-8e95-2e2aef378263 | -7.75693 | -35.14195 | 2024-12-09 03:53:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ae1b73bd-5ba2-3bb3-99da-13d601866818 | -6.96637 | -34.93462 | 2024-12-09 03:53:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 5ccf30fe-7b6c-3676-95ca-60d3a6a95f6f | -6.97639 | -34.9184 | 2024-12-09 03:53:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 4ca1faa7-d04c-3895-a586-efa1a5610d70 | -7.51978 | -39.26588 | 2024-12-09 03:53:00 | NPP-375D | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2a53f4f6-698c-3042-b117-b986c6e16551 | -5.42615 | -44.70732 | 2024-12-09 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ea10513-efd4-33aa-adae-eafdc3ea0a05 | -3.96637 | -46.96318 | 2024-12-09 03:53:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f03ab5d-0c05-37a9-a754-f7d18d658014 | -6.83323 | -44.38625 | 2024-12-09 03:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46150a30-b7a9-3208-b935-5309adf78634 | -4.08101 | -46.72174 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fa54d6b-0418-3244-be9c-ee2e48063495 | -7.88608 | -35.15008 | 2024-12-09 03:53:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d6abad15-42ab-3048-8492-d46fa92d29a2 | -8.49551 | -35.01408 | 2024-12-09 03:53:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b109c808-b975-30a2-8a23-d7f494574b0a | -5.47545 | -39.40966 | 2024-12-09 03:53:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 56480bd5-bb71-3b54-918b-8ca6e98eb02f | -8.07355 | -34.97609 | 2024-12-09 03:53:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8bab69f9-0baf-365f-b405-f27cce651f13 | -5.58035 | -45.10592 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a5a19ce-cd44-3b90-8428-62e02e66d4f8 | -5.58415 | -45.10476 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71be8a39-dfe8-3d2a-9f55-8218f8c35809 | -7.90908 | -35.19838 | 2024-12-09 03:53:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3a0cfec9-d997-36c7-8dd3-4f38814a3959 | -5.57766 | -45.20808 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ee7fe0ed-c583-3197-ad7c-78ed22ae975f | -7.78475 | -35.13283 | 2024-12-09 03:53:00 | NPP-375D | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f8eefbbc-7513-389b-b0a3-05f9cf9ef697 | -6.97203 | -34.92218 | 2024-12-09 03:53:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 82ef0dba-6a8a-34e7-bc34-4fc7cd68690f | -8.41977 | -35.11153 | 2024-12-09 03:53:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 43d55dbd-96ed-3154-bb7b-2ec27d955135 | -5.86047 | -45.36269 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b561a11-9d6e-3b4c-b76a-7fa89051fc1a | -7.88978 | -35.1506 | 2024-12-09 03:53:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 24b82145-57d6-3544-afbc-309e8ae2d4a6 | -4.07628 | -46.71774 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3e1b2a90-80b6-35dc-9b1d-54c13cb8045b | -5.1861 | -43.9333 | 2024-12-09 03:53:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63a48cb4-1b7f-357c-8e42-c1cb9077147d | -4.0832 | -46.70878 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 381946c1-6326-3e96-85f9-9d4e8594367e | -5.5815 | -45.21368 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4a4e0e96-739d-35a2-8a8a-a1cda8c9503a | -7.74937 | -35.26929 | 2024-12-09 03:53:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e77c33ff-80d2-39fa-81f7-6060e2caee02 | -8.17047 | -35.23745 | 2024-12-09 03:53:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 302bb237-f926-3f5d-a4c1-0dd78346b76b | -4.04611 | -46.67277 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4b23e00-db29-3d08-863e-e6477fdd2776 | -4.08684 | -46.71927 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4520719b-a4c2-3119-86c6-9315e83f7aa9 | -6.97311 | -34.94016 | 2024-12-09 03:53:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6392ab1a-510a-3e72-b743-c2189fe372bf | -7.78409 | -35.13722 | 2024-12-09 03:53:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 561a2e5a-8a88-3b7a-bd41-d062fb53985f | -5.42167 | -44.70654 | 2024-12-09 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd7117d4-09cb-38e1-b9de-42b347ab75c1 | -4.08375 | -46.70553 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 41b251ce-9aee-38e3-8149-3db6253c71d0 | -6.97442 | -34.93149 | 2024-12-09 03:53:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| bc58d5b1-848b-3f84-9948-13d3bc0c22ef | -6.25826 | -40.62253 | 2024-12-09 03:53:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9aa4f85e-085b-34fa-8e8e-a0ddd71f55cb | -7.75324 | -35.14137 | 2024-12-09 03:53:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 28b5d7a0-771c-3706-9c19-85696505119d | -7.91212 | -35.2033 | 2024-12-09 03:53:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 85a67fa6-e022-3313-ab09-b3340518e0d6 | -4.69966 | -45.285 | 2024-12-09 03:53:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef01c481-5f3e-3f4b-9c56-e0c3e9315caf | -5.64578 | -35.47178 | 2024-12-09 03:53:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9754f476-51ba-3a66-8ba1-9e951782d0de | -8.52666 | -39.44218 | 2024-12-09 03:53:00 | NPP-375D | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 582e0d24-182e-3b65-9f0e-028b3ea1609c | -6.98077 | -34.91454 | 2024-12-09 03:53:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 6805dd01-2ff6-34cb-91a8-10c04fd82be6 | -4.08901 | -46.7064 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea4ed6cc-c891-3f50-b2af-533a07cbcad5 | -8.52999 | -39.44271 | 2024-12-09 03:53:00 | NPP-375D | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| db2dd9aa-491d-3599-8d70-74e419671712 | -7.52312 | -39.26641 | 2024-12-09 03:53:00 | NPP-375D | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 64e4a939-9c69-3173-a631-71e2e5793f69 | -5.37586 | -45.12534 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc101efd-718d-3d32-af93-5f070a128d28 | -7.0862 | -45.21264 | 2024-12-09 03:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c8686bc-20d7-3676-bab0-7d180060b02b | -4.92604 | -44.86989 | 2024-12-09 03:53:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 116ef82c-f14a-3e9b-b7cb-6c541c7db5f7 | -5.57687 | -45.21289 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d130616-b9f9-3414-aa4e-aa5658196d51 | -8.07366 | -34.97824 | 2024-12-09 03:53:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 321ce2f4-a29c-3daa-aa95-aa0a7f804df6 | -4.6985 | -45.28848 | 2024-12-09 03:53:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 224b5483-3e49-307e-8d06-bf34478da0ba | -5.18184 | -43.93252 | 2024-12-09 03:53:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44207c89-7448-35d1-a6b2-099446986fd0 | -3.94582 | -46.63324 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8edff49-663e-33ac-a1b3-55e2fdb5a435 | -3.96581 | -46.96651 | 2024-12-09 03:53:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb2ddb07-5804-3bc5-9287-78470cafa58c | -7.90843 | -35.20271 | 2024-12-09 03:53:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 15986102-82b2-3973-8332-cd72bccf0e2e | -6.30925 | -47.34245 | 2024-12-09 03:53:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 962432d2-999c-31e4-89a9-41acb8ecf1ef | -4.08646 | -46.65757 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17375f4b-f35c-3379-ada7-f7f6a1ef31db | -5.86342 | -45.36028 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7157429b-2dfa-34d6-88a4-578162414046 | -6.30453 | -47.33834 | 2024-12-09 03:53:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4c17efa-041c-3f09-887b-281c6e117ad1 | -4.8194 | -44.3545 | 2024-12-09 03:53:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bac283b4-6522-3437-ac46-3bf1aab1df2c | -5.37046 | -45.12929 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6421ee7-e894-300a-bafe-119fd417ad5e | -4.08265 | -46.71203 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4ec634b-153b-3616-bcda-a9dd1389d400 | -4.04088 | -46.67176 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad82aa4c-74b4-3674-b43a-93ced1e04e92 | -6.83392 | -44.38223 | 2024-12-09 03:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77ce9b9f-d3d2-3b69-a429-32c5c55a72bb | -5.18677 | -43.92934 | 2024-12-09 03:53:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d9e8dfd-7358-35d0-93c5-9dc5908493f6 | -8.11479 | -35.06248 | 2024-12-09 03:53:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 512ea5e6-de2b-3e9a-807b-bfd050618ee4 | -3.94637 | -46.63004 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62e9629c-8e9b-3400-9011-8ecb4fd2ac04 | -4.07683 | -46.7145 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73c130e1-de60-39e2-be91-5b8deb8800a6 | -4.08157 | -46.71846 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f242d9f-ede4-385e-927a-24acdfffcfbb | -5.57991 | -45.21142 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b93bc691-f084-3740-ab11-79500c223853 | -6.97269 | -34.91783 | 2024-12-09 03:53:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 29720172-6310-31ca-97a7-b570cb32dd9b | -7.18249 | -45.44169 | 2024-12-09 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e59589d-3ee3-30b6-8bb5-d5a3719006e0 | -4.08629 | -46.72257 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5da18b04-1047-3b81-840f-92a5f3293dec | -6.44613 | -47.05813 | 2024-12-09 03:53:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20a7822a-3337-3fff-a57b-dda16e156192 | -5.57908 | -45.21622 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4fc92ff7-343d-3c11-a089-a5aadc87b9f2 | -5.47825 | -39.41377 | 2024-12-09 03:53:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 58f599d9-575d-3475-84f8-5014b99cb73b | -7.88913 | -35.15498 | 2024-12-09 03:53:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| feaa57ca-bb60-3c5b-a2b8-a55c8d39e7a5 | -5.36928 | -45.12593 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0b53488-ec9c-3ff8-b611-4aea2828c0cd | -6.44555 | -47.06134 | 2024-12-09 03:53:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81c3a584-02c7-3ea0-b7bc-c8ce34dee77a | -5.86254 | -45.3653 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 57c2ca28-5094-3a34-9a1a-089e510e4590 | -5.58074 | -45.20663 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3691431b-6945-3254-87c5-62573b730f72 | -5.37388 | -45.12678 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5e63975-59c8-39cd-b5eb-8183a598c545 | -7.91277 | -35.19897 | 2024-12-09 03:53:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3b81faf1-030e-3954-b175-17f9a3919661 | -5.18251 | -43.92855 | 2024-12-09 03:53:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a78873e9-6e06-341b-bbe7-4b0000993c53 | -4.08572 | -46.72595 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af99cc10-a633-3fb5-8e5f-d02b518be634 | -9.03674 | -35.64361 | 2024-12-09 03:53:00 | NPP-375D | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| c616e447-accb-3c65-9e13-a7399795e444 | -4.08738 | -46.71607 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3262223-dfa0-3cbb-bac2-e709b1a60822 | -8.74944 | -36.18865 | 2024-12-09 03:53:00 | NPP-375D | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 474b6ea4-d3c2-367c-94bf-d323b42c17e4 | -5.58229 | -45.20887 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88a3e9b5-d726-3e7a-b9c7-5a11d44159b7 | -9.03308 | -35.64309 | 2024-12-09 03:53:00 | NPP-375D | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 2f1b3914-072b-3c23-a96d-0051e5bf0bf6 | -8.4235 | -35.11209 | 2024-12-09 03:53:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 30946415-e515-3342-b324-fdecee621164 | -6.97376 | -34.9358 | 2024-12-09 03:53:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ef459930-5ab3-3ea5-8e2b-1924ca1e284d | -8.49581 | -35.01205 | 2024-12-09 03:53:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 61be1562-37e5-35e4-9068-8d6f3971c182 | -3.94693 | -46.62679 | 2024-12-09 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67b75969-e9c8-31fb-a047-bc4bf1156936 | -6.97507 | -34.92714 | 2024-12-09 03:53:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 58770ba5-3cfd-3b3c-bbf4-16781e2469ed | -5.86512 | -45.36354 | 2024-12-09 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19831508-893e-3218-945f-5b55aafcbd36 | -10.91973 | -48.9359 | 2024-12-09 03:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c120a49b-4152-38b7-baaa-a5243a6a22af | -12.36439 | -45.93563 | 2024-12-09 03:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a61c9ce5-d21e-3464-8c82-e37658d1a075 | -12.36342 | -45.93739 | 2024-12-09 03:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3060d42-0492-32ce-bcdc-fb0e2c8c986a | -13.27278 | -51.09804 | 2024-12-09 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README6.md)
