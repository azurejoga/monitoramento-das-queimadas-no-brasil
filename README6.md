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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c36d0a9f-5540-38e6-a512-a1ba333c8904 | -6.4782 | -42.2397 | 2026-08-07 02:30:00 | GOES-19 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 50.8 |
| 2649c705-ddd5-3b80-965c-aaded41cea51 | -11.1447 | -44.4632 | 2026-08-07 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 41a03228-ec0e-36c4-889e-8e2b50681a92 | -11.1443 | -44.4865 | 2026-08-07 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 39d8b7c1-5681-3b90-aa93-1f57c16e16c3 | -11.1447 | -44.4632 | 2026-08-07 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 39740554-c4ba-312a-97ad-dc1bea92fa80 | -11.1443 | -44.4865 | 2026-08-07 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 154.7 |
| dfe2bcd4-a399-393f-a090-b9f26eab4458 | -11.1447 | -44.4632 | 2026-08-07 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 1b02df49-0648-38c7-84e0-00b40aca1536 | -6.4782 | -42.2397 | 2026-08-07 03:00:00 | GOES-19 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 9e3f19e0-d1d8-3d45-bbc2-5a49907eb67b | -11.1443 | -44.4865 | 2026-08-07 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| da7b22f8-769f-3b04-961d-caee9743d6f0 | -18.57669 | -39.91612 | 2026-08-07 03:06:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ab662d7b-9227-3347-a5d0-6e0570fca43a | -18.58358 | -39.91816 | 2026-08-07 03:06:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c749e451-301c-3129-a567-755c1d790493 | -6.4782 | -42.2397 | 2026-08-07 03:10:00 | GOES-19 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 80d10e2f-742b-3306-ad08-4a82f8aeff42 | -11.1252 | -44.4892 | 2026-08-07 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 96c56c7b-f78a-3413-8d45-d1f0562904ef | -11.1447 | -44.4632 | 2026-08-07 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| da80f57d-b6eb-39a1-aa2a-5f50894c8201 | -11.1443 | -44.4865 | 2026-08-07 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 67ba39b5-f352-31bd-93f9-62dbd747d218 | -6.4782 | -42.2397 | 2026-08-07 03:20:00 | GOES-19 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 50.6 |
| 34b47d13-f5f8-3474-871f-56d38e583db5 | -11.1447 | -44.4632 | 2026-08-07 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 47c704e6-f5f9-30ee-8621-b97ace043f92 | -11.1443 | -44.4865 | 2026-08-07 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| f3c78f4d-e0dd-3a3d-9fea-a1dc0b2bbdc2 | -6.4825 | -42.22831 | 2026-08-07 03:21:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b9ac7f36-9570-3887-8805-22a016c6699d | -6.9882 | -42.91104 | 2026-08-07 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 5378684c-cc33-3951-9524-f407569e0102 | -6.91188 | -41.94448 | 2026-08-07 03:21:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a1deaa8f-9411-3df1-ac1b-ec2ff9446002 | -6.48204 | -42.22602 | 2026-08-07 03:21:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 06efc1bb-9156-3058-8684-820836909ab1 | -3.07308 | -39.64683 | 2026-08-07 03:21:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e5746ab9-edbc-3d73-96fe-db966bf16897 | -9.39794 | -37.80503 | 2026-08-07 03:21:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 78652ab4-1368-386f-af04-51e30ff47351 | -4.99343 | -37.0965 | 2026-08-07 03:21:00 | NOAA-20 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 461e2780-ac10-3f8d-90c8-661270e6516f | -6.4757 | -42.22691 | 2026-08-07 03:21:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| f93b18c6-0a2c-3cae-be83-b41866bee44b | -6.98395 | -42.91906 | 2026-08-07 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| cdc4b21b-da46-3ecf-b53e-110b066894ef | -6.98688 | -42.91813 | 2026-08-07 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a86b7b48-ba89-3f96-a931-e4d4fbddcb69 | -6.47328 | -42.23974 | 2026-08-07 03:21:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 1a94c6da-940b-38df-9387-c53028f31b17 | -6.92081 | -41.95209 | 2026-08-07 03:21:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4629b288-17e4-3347-9414-98f321253cee | -6.98529 | -42.9121 | 2026-08-07 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 22b1bcf3-3c19-322c-be9d-f046a9adc0ab | -6.47298 | -42.23703 | 2026-08-07 03:21:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 53357a65-05ed-342d-bd32-c9793403e80f | -6.47152 | -42.24503 | 2026-08-07 03:21:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 311a97d5-371b-320f-aa61-5908c045f9fe | -6.47456 | -42.23297 | 2026-08-07 03:21:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 3698efdc-38d5-3b04-a046-3f20ca224371 | -3.07401 | -39.64613 | 2026-08-07 03:21:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 6049fb0f-7824-300b-bf60-3c048ffea975 | -4.99293 | -37.09951 | 2026-08-07 03:21:00 | NOAA-20 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6b899f20-94e9-348d-8d75-3b3bab7def62 | -6.91074 | -41.9506 | 2026-08-07 03:21:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bb84971e-767b-3281-b19d-a70ff1f8d9ba | -6.9923 | -42.91358 | 2026-08-07 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 53d8c2a5-8a67-3890-84d9-51cf2dd8b8bb | -6.91535 | -41.94454 | 2026-08-07 03:21:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e8cc6799-7204-3d51-a9ee-88f0b0ed187c | -6.47519 | -42.2249 | 2026-08-07 03:21:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 315d3b9f-4680-334a-817d-6956d8d6a162 | -6.91417 | -41.95066 | 2026-08-07 03:21:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 849ab52e-a76e-3daa-87ba-503d0093ee9f | -6.47412 | -42.23075 | 2026-08-07 03:21:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| d540ff6a-3e44-3562-b74f-41e6c35da631 | -6.9174 | -41.95195 | 2026-08-07 03:21:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d9573fef-0d41-3053-a495-85da96c1825d | -14.2694 | -45.29818 | 2026-08-07 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c71246d-cdde-3b3d-9ae4-3413d5413668 | -14.27218 | -45.29765 | 2026-08-07 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 611cbe57-e59c-3832-924c-87b392eea8c1 | -14.27384 | -45.2904 | 2026-08-07 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80b77665-2aea-389e-b35a-4ec4c923e881 | -14.27101 | -45.2909 | 2026-08-07 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4183541-6787-3e9f-ba2d-807531b10df8 | -14.26509 | -45.29595 | 2026-08-07 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c5d55cd-1dbb-3bf0-8706-ddfcea26c693 | -14.26675 | -45.28868 | 2026-08-07 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be963c7a-f561-3487-b6df-e3381425bf45 | -15.86722 | -43.59771 | 2026-08-07 03:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7688a3ca-329a-3dee-ae54-a5c83554c736 | -20.61145 | -46.29375 | 2026-08-07 03:25:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 007feab9-4cca-32e8-ba84-a122d1da5dc5 | -21.85355 | -42.05421 | 2026-08-07 03:25:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e44377fc-4588-3160-921f-149d936de9ed | -15.86897 | -43.60104 | 2026-08-07 03:25:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c23fd816-d729-3dd9-b8c0-57d1e48d81b4 | -15.86609 | -43.60296 | 2026-08-07 03:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9cc974cb-08fb-3bb6-bee2-e38256c58545 | -19.38795 | -40.26183 | 2026-08-07 03:25:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 89f45e39-e75c-301b-a101-0749c4892f4a | -22.45552 | -43.13977 | 2026-08-07 03:25:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3a6b9efc-a05f-3ba3-a3fb-be18c3227897 | -15.87012 | -43.59583 | 2026-08-07 03:25:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 160cb4f3-cb21-35bc-92f0-f13b6796af35 | -21.6298 | -43.66241 | 2026-08-07 03:25:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6980bcc1-8652-374f-bc4f-d69d466fe2b5 | -19.91286 | -40.13955 | 2026-08-07 03:25:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 409ad10f-a158-3533-a93a-b164566c4636 | -17.53039 | -45.36018 | 2026-08-07 03:25:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3ecb58c-f782-3167-a298-4342e19376ea | -20.60482 | -46.29183 | 2026-08-07 03:25:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e1aebe6-536c-3913-82ee-2e0ddc2c9bcb | -21.8748 | -41.62449 | 2026-08-07 03:25:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4974e3e0-d186-36bf-ba0b-f90d3a2dfffb | -19.82769 | -40.24208 | 2026-08-07 03:25:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e69f2954-e70c-334d-ac42-d89561c16b4a | -21.60246 | -42.99753 | 2026-08-07 03:25:00 | NOAA-20 | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 117813a1-e733-35ac-a898-0bed5b8313a3 | -19.90815 | -40.13841 | 2026-08-07 03:25:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 96faf816-caaf-359c-bbb3-54e0ba4f9fa7 | -20.99192 | -42.59194 | 2026-08-07 03:25:00 | NOAA-20 | SÃO SEBASTIÃO DA VARGEM ALEGRE | MINAS GERAIS | Brasil | 3164431 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ac355e5c-45ec-30d3-8ea2-243748fe0779 | -22.53103 | -43.56886 | 2026-08-07 03:25:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a0c2c5b8-bb88-3ffd-a8d6-c4713132e3a9 | -22.63875 | -43.65302 | 2026-08-07 03:25:00 | NOAA-20 | JAPERI | RIO DE JANEIRO | Brasil | 3302270 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8d2a6b7e-d381-3c53-a3e5-bbb0808bb9b9 | -15.92472 | -43.98878 | 2026-08-07 03:25:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94403839-3a2f-3422-b498-d92d1f274e45 | -22.53197 | -43.56472 | 2026-08-07 03:25:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9a44ea0e-4cf3-3889-a2a6-568bcb68b848 | -19.82687 | -40.24406 | 2026-08-07 03:25:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0904bd4e-143c-31c4-9d05-b67c8ccbd6a0 | -22.45655 | -43.13514 | 2026-08-07 03:25:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ba109a4a-0b33-3a37-a748-4e87cdca73c5 | -21.63548 | -43.66368 | 2026-08-07 03:25:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2509f486-f3a3-3a10-919c-9bc648ef90b8 | -22.52728 | -43.55969 | 2026-08-07 03:25:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e2a55032-7c9f-3868-afbb-84e74fe47b09 | -15.58722 | -43.7403 | 2026-08-07 03:25:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 12a25f2f-dae6-3837-be22-593a7ecb9701 | -22.53303 | -43.5601 | 2026-08-07 03:25:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cc3d98c8-d42f-397e-9e89-f3e3490dc49a | -6.4782 | -42.2397 | 2026-08-07 03:30:00 | GOES-19 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 681e44db-eef7-32e5-8c86-49216e4a4854 | -11.1447 | -44.4632 | 2026-08-07 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| efa9aa21-ac3c-3245-b4a7-351f49c8a09b | -11.1443 | -44.4865 | 2026-08-07 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| ff77df71-058c-3a5e-888b-4a30db832a11 | -11.1443 | -44.4865 | 2026-08-07 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| fa446db0-5118-3ca3-8e33-a229b4f4b7c5 | -11.1447 | -44.4632 | 2026-08-07 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 50dcff91-2598-3e9f-a8b9-a089af5c2abc | -11.1443 | -44.4865 | 2026-08-07 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| baee692a-e1e8-37e3-a974-25327a759840 | -11.1447 | -44.4632 | 2026-08-07 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 74c29279-2e99-3d98-913b-fcce2ccdc766 | -11.1447 | -44.4632 | 2026-08-07 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8f7c4e96-292f-3aca-b769-d3a67cfade63 | -11.1443 | -44.4865 | 2026-08-07 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| ceafa8d6-7d02-3447-841b-4b70c53ee0da | -3.07717 | -39.64325 | 2026-08-07 04:06:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dc4794b2-0a67-3f5f-8933-e4b4b9ed312c | -3.07382 | -39.64274 | 2026-08-07 04:06:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 33ff18ce-ca49-3860-ae42-07f9cba83f56 | -3.07327 | -39.64627 | 2026-08-07 04:06:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f659e22d-1ddf-385b-a209-b51bb8347114 | -2.91342 | -40.43361 | 2026-08-07 04:06:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 46e9bc86-e64f-3d1e-b4e3-b33a69fd8773 | -4.65302 | -43.12788 | 2026-08-07 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88c77109-105b-36c2-98f0-8c1d0ef4b792 | -6.91123 | -42.42618 | 2026-08-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 762ee680-f289-39dc-a919-863c99650099 | -6.91324 | -41.93803 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6e153057-7031-36ec-96d8-041e0ac8f440 | -6.95231 | -41.92643 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e9356bc4-9071-304c-ad9b-e6d71261807e | -5.42654 | -43.43132 | 2026-08-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c225f04-4bce-3c3f-9ca3-84f2ea633bc4 | -6.91823 | -41.94946 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| de2e7d6b-b363-353a-957f-68793035fb0e | -8.51926 | -44.89303 | 2026-08-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5c3f91b-613e-38a5-95ce-2c3efaa0943b | -3.02655 | -48.4114 | 2026-08-07 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d47dda0e-6a3c-3255-9862-ebf5712fff38 | -6.8561 | -46.00389 | 2026-08-07 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb9c714b-7de2-3553-a2fd-0839add94a4c | -5.27676 | -37.72383 | 2026-08-07 04:08:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 698a0998-9a0c-33a3-9d8d-af9db2d9347c | -6.34376 | -43.42585 | 2026-08-07 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d4bbc12-7b7e-3bc5-adf1-b23a0b12a90d | -7.75024 | -45.02615 | 2026-08-07 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |


[Clique aqui para ver as próximas entradas](README7.md)
