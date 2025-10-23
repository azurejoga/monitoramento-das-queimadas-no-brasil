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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cf2b5aa-b4dc-3435-bae0-00dfb24d1dd5 | -10.9782 | -50.2723 | 2025-10-23 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 0c35f226-2a03-3400-926e-b7214bf644a0 | -17.5961 | -46.6415 | 2025-10-23 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 2de32700-4a86-3066-843c-e10aa2e7fd68 | -12.8331 | -48.6336 | 2025-10-23 14:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 018b68a3-767d-31d2-be40-9d6c2ef13562 | -11.2492 | -49.8773 | 2025-10-23 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 2c1a1761-f08b-3f67-b799-09ac76fb3d17 | -10.9592 | -50.2744 | 2025-10-23 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 144.9 |
| a3975185-79d9-3454-876e-bcd6d367593f | -17.6173 | -46.5906 | 2025-10-23 14:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 209.8 |
| 8cec7944-91d1-36c7-9d11-65d648220196 | -17.5973 | -46.5948 | 2025-10-23 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 279.0 |
| 0850f944-7510-34ab-a3b6-4e77f2619717 | -13.0504 | -47.223 | 2025-10-23 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| fb776a9d-032d-3fd1-9a89-b5c04028430b | -17.335 | -55.0366 | 2025-10-23 14:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 188.7 |
| bd0a1560-993c-3c14-9565-7a36b1b5f494 | -15.6004 | -45.9249 | 2025-10-23 14:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 738106c6-8713-3ae5-be0e-760af551ed0a | -13.0311 | -47.2259 | 2025-10-23 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8053aeaf-9737-3884-9a50-148de2fc199e | -17.3547 | -55.0339 | 2025-10-23 14:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| bcd6327c-d6cc-3a52-bd93-b60a0b4fd6f2 | -17.5973 | -46.5948 | 2025-10-23 14:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 334.6 |
| 0b2213a7-0fac-3c14-9a2b-e55770c96a49 | -11.0823 | -49.616 | 2025-10-23 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 18f0c20c-4bf6-328d-834a-c9d8746f2b05 | -4.4915 | -39.454 | 2025-10-23 14:20:00 | GOES-19 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 102.4 |
| f7a60eba-0f4b-319c-a5d5-d2d39f293dd9 | -13.0504 | -47.223 | 2025-10-23 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| f17157f9-78ca-3a95-8405-4841a7964ab6 | -11.2492 | -49.8773 | 2025-10-23 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b060725e-6f31-3b84-8d05-910dec0090e1 | -13.0311 | -47.2259 | 2025-10-23 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 30bb3931-0649-3009-995f-9eb1843c58ff | -10.9592 | -50.2744 | 2025-10-23 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 210.6 |
| cb0ca1ab-0fa6-371c-9384-df50887ee837 | -11.0738 | -51.5787 | 2025-10-23 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 53726515-007e-352f-b099-0afd1ffff552 | -10.921 | -50.2999 | 2025-10-23 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a37d0e20-3d9a-3d38-80d0-058f0f62c7d0 | -17.6173 | -46.5906 | 2025-10-23 14:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 176.5 |
| e04128e5-15f3-3e28-8acb-868453dc9f3f | -10.9782 | -50.2723 | 2025-10-23 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 628fb2cd-bddd-32c0-b4b3-cf0f8c873c25 | -11.7057 | -51.1302 | 2025-10-23 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 61ab2782-3ae6-30ab-9266-87541647c1ee | -12.8139 | -48.6362 | 2025-10-23 14:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 1234d674-14f1-3463-ae71-a097c1856683 | -11.0823 | -49.616 | 2025-10-23 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 4867ec9e-8bb2-32b2-aaaf-c4049f71ae95 | -13.0504 | -47.223 | 2025-10-23 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| ab890f40-b179-3d10-a899-a80a6261dd25 | -17.6173 | -46.5906 | 2025-10-23 14:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 126.1 |
| ca4d1971-798b-31b6-96a4-0770fc492016 | -17.5973 | -46.5948 | 2025-10-23 14:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 370.1 |
| 0613ae58-dff5-37a8-a348-ff90274d5b96 | -17.3033 | -58.0974 | 2025-10-23 14:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 168b4497-b299-3705-84b2-3c3d5711e3b4 | -10.9782 | -50.2723 | 2025-10-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 233.4 |
| 120ac462-8275-3a42-8f81-6ea40d66054e | -12.9028 | -62.1244 | 2025-10-23 14:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 2663b6de-4f2e-3290-be3c-05f45ec24bda | -10.9592 | -50.2744 | 2025-10-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 273.3 |
| fa372082-87d4-3634-ae11-fddac768ecef | -17.3547 | -55.0339 | 2025-10-23 14:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| bbb5bdd0-a959-378d-af64-ac330163ef2d | -12.8331 | -48.6336 | 2025-10-23 14:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 347623e1-902e-31f4-b04b-4f4cc5c79370 | -10.9589 | -50.2958 | 2025-10-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 788d0a1d-49a3-39a9-92c9-c530ab331030 | -11.0738 | -51.5787 | 2025-10-23 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 1f63d11b-f769-372a-a538-d80b35ce61b0 | -11.2492 | -49.8773 | 2025-10-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 223400c3-ceee-3b8b-b380-fa234fc9818b | -17.3037 | -58.077 | 2025-10-23 14:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| d8ad48af-f8c2-35bb-b77e-2618b788a056 | -0.8398 | -48.7464 | 2025-10-23 14:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| dd095625-ab65-368b-9851-338f149769bf | -13.0311 | -47.2259 | 2025-10-23 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 00670885-756b-35ec-b5b8-71eaa3cbcd7c | -11.0741 | -51.5576 | 2025-10-23 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ae821ccb-a09e-3d04-b9d4-02e09219b970 | -11.7057 | -51.1302 | 2025-10-23 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 43e74679-4218-3c41-b257-c3036093c4cf | -11.2492 | -49.8773 | 2025-10-23 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 33eeb0cb-d4ca-372a-9f74-e3b2d6c6437a | -11.2816 | -50.2602 | 2025-10-23 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 718713b7-881a-32df-b91f-6a0a90a9578c | -11.0738 | -51.5787 | 2025-10-23 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| a5677256-5de6-303a-af46-3f8e81cb5dad | -13.0504 | -47.223 | 2025-10-23 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ed8520bb-7b8a-3b47-b12a-404b5f1814b4 | -12.8135 | -48.6583 | 2025-10-23 14:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| c8ec8042-6d3f-365b-99c6-ad212b48691e | -13.0311 | -47.2259 | 2025-10-23 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |


