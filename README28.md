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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4781dba1-1bb5-3afb-9933-6257786ca988 | -4.43036 | -45.96735 | 2024-10-27 03:36:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8112d66f-e94a-3f43-92b5-5929a56307ed | -4.42475 | -45.95995 | 2024-10-27 03:36:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 94003833-4cc0-33ac-8294-8090a20557ac | -4.42372 | -45.96572 | 2024-10-27 03:36:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5e0416bc-3270-3ea3-8d4c-ffd6a9eac7e8 | -4.06157 | -45.67604 | 2024-10-27 03:36:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 333588e3-aa2c-3187-927c-96fbe0124ab7 | -4.06053 | -45.68195 | 2024-10-27 03:36:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 798bddb5-1dea-3153-b2f1-8c399f40009b | -3.75378 | -45.77958 | 2024-10-27 03:36:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 82b3b972-9d30-35ad-a3b7-520af263e029 | -3.7527 | -45.78561 | 2024-10-27 03:36:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7346fd3a-4c33-38c5-bfc3-1feeab7eeac8 | -3.75037 | -45.78119 | 2024-10-27 03:36:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1fe3bc71-1ab0-30db-bd45-d9f257e83530 | -3.67443 | -45.88538 | 2024-10-27 03:36:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e62c52c-a463-3b59-9870-61784027cb5f | -6.18455 | -45.43819 | 2024-10-27 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dde87273-0290-33ce-acd2-0f728de3b12f | -6.18362 | -45.44341 | 2024-10-27 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98419252-4dcc-32b0-a78e-4ec9cf70b525 | -6.18056 | -45.43927 | 2024-10-27 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 301dae66-a414-3a81-92d6-a6f801ef8185 | -6.17958 | -45.44452 | 2024-10-27 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ab9c2269-e477-3662-bb1c-41285f4dc662 | -6.17729 | -45.44219 | 2024-10-27 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2cd73eb0-4743-3504-b480-4c9263894813 | -6.17633 | -45.44754 | 2024-10-27 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c918160d-1d33-3630-8dff-0ccfff5ab600 | -6.17319 | -45.44367 | 2024-10-27 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5f906cdc-50ad-3985-a0ad-b32f2007345a | -5.99343 | -45.97318 | 2024-10-27 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09e2916d-24d0-338e-98fa-10475307b7eb | -5.40818 | -45.40052 | 2024-10-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4d5b720-241e-3b84-a787-ce9c025443cf | -5.40726 | -45.40563 | 2024-10-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59bb8f5e-06ef-318f-88cf-e7f0222a56cc | -5.20278 | -45.53852 | 2024-10-27 03:36:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d822c1b6-f497-3f42-9fdc-e080804e8288 | -5.20203 | -45.54172 | 2024-10-27 03:36:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91486a4b-0f51-3fef-bb99-e855b9dc334d | -5.20176 | -45.54407 | 2024-10-27 03:36:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 421c64fb-7b59-3ae0-9fb3-c31929bc0b94 | -5.19623 | -45.53782 | 2024-10-27 03:36:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57369a5c-0baa-30ee-b10b-0d1c690d65d2 | -2.47586 | -45.84042 | 2024-10-27 03:36:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2730617b-886f-3c21-ab55-e317dcfb7c57 | -2.47475 | -45.84672 | 2024-10-27 03:36:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a0cb856-40bc-39a0-8c8e-4ece62d5dee0 | -2.47471 | -45.84255 | 2024-10-27 03:36:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c40cbe27-6ae4-3abb-adab-a6ca31ec4db5 | -2.46788 | -45.84563 | 2024-10-27 03:36:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e11888ba-682e-388f-9dfa-254cabab94b9 | -2.46784 | -45.84142 | 2024-10-27 03:36:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3c6664d3-3bc7-3bc4-8ed4-94f47b562cce | -2.46677 | -45.84777 | 2024-10-27 03:36:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2632508b-837a-34af-b235-31744417f9eb | -4.81494 | -46.87473 | 2024-10-27 03:36:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7316daf4-38e5-3f3d-a7b3-f51782999ae4 | -8.7877 | -44.7266 | 2024-10-27 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c5fab25-ae69-39a2-a94d-6bcf2153ada9 | -9.94445 | -36.29622 | 2024-10-27 03:38:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 291db153-1304-327b-935d-cc1a274062b4 | -9.94385 | -36.29997 | 2024-10-27 03:38:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 49745236-e09d-3571-b8ca-eb1aa41ca231 | -9.94104 | -36.29565 | 2024-10-27 03:38:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.5 |
| 7aa45a64-45dc-3f4b-93d0-9d5d1d0fc090 | -9.94043 | -36.2994 | 2024-10-27 03:38:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.5 |
| a99fefb4-a176-3eb3-aea9-d669dd99b309 | -9.93702 | -36.29884 | 2024-10-27 03:38:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.5 |
| 26e53f41-66c8-338c-b7bf-72a3178faeda | -9.44872 | -36.03594 | 2024-10-27 03:38:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 23dbb2f7-d163-38d8-b6db-205aa9e3fd08 | -8.556 | -36.38238 | 2024-10-27 03:38:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c3e37979-74b9-32fe-857f-41bdff5f96b4 | -14.91479 | -40.68003 | 2024-10-27 03:38:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3c173c7-6508-31c5-b9c9-dc7298b85e23 | -9.35865 | -39.92149 | 2024-10-27 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5fd82250-ba58-354c-bf7f-054272f08551 | -9.35447 | -39.92074 | 2024-10-27 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 740e0199-ceb5-32a3-84d3-268ddcfbd404 | -9.08877 | -40.21635 | 2024-10-27 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b3379d8d-819d-3671-8c7c-438c555eaa44 | -8.16418 | -40.50359 | 2024-10-27 03:38:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ec8f6d30-595f-309a-97c5-4eeec5a625d3 | -8.16362 | -40.5018 | 2024-10-27 03:38:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c5c9aae7-034f-35e5-a0cb-fd08028b48a7 | -12.23616 | -40.97698 | 2024-10-27 03:38:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba80e3f5-ed3a-3234-b192-968c8b37c108 | -12.1206 | -40.36201 | 2024-10-27 03:38:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 99408e8f-8743-3fd8-b376-18859b222b72 | -12.10561 | -40.39806 | 2024-10-27 03:38:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 245132fd-d474-39b0-be5b-93f05b1c269e | -15.00717 | -41.55775 | 2024-10-27 03:38:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0808fcea-49e1-33d8-92c9-ae7653ce7d38 | -15.00293 | -41.55704 | 2024-10-27 03:38:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dedb6d44-cc84-3527-9ed3-196ab1846acf | -15.00643 | -41.56178 | 2024-10-27 03:38:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4e37d79d-2cf2-3b59-90bb-fbe541da6662 | -8.67221 | -41.03954 | 2024-10-27 03:38:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 95242dd2-8eec-3113-b101-b72df2886d20 | -8.35273 | -42.26361 | 2024-10-27 03:38:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 627187ed-264e-3b9f-9c6e-bf2b1c2cdeb8 | -8.34826 | -42.25985 | 2024-10-27 03:38:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a23ddf3d-1e96-3824-a122-7bb328357646 | -8.34774 | -42.26273 | 2024-10-27 03:38:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| da31194f-0fce-33fa-adf0-be6e512d2a63 | -8.29462 | -40.96018 | 2024-10-27 03:38:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 82fe14ce-1e71-35c2-aad3-f881ac17cd63 | -8.29395 | -40.96126 | 2024-10-27 03:38:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| a5388fa7-8be3-391d-be28-7c5c9ecccfa1 | -12.21393 | -42.78492 | 2024-10-27 03:38:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ae687878-db8e-348a-ab71-13a81b77fb33 | -13.71233 | -42.9115 | 2024-10-27 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4cdba9ed-280c-3434-9022-cb94770642c1 | -13.48086 | -42.46353 | 2024-10-27 03:38:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e9f1fe4c-4a43-34d4-9fd0-d3e9b48c3013 | -13.47865 | -42.94305 | 2024-10-27 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f40c5903-5529-3ffc-b9be-58cfb4c29fa1 | -13.47806 | -42.94485 | 2024-10-27 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0c461c93-b32c-33cc-af4b-d2ef42d3d94f | -13.06947 | -42.13117 | 2024-10-27 03:38:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 25f73c3a-5444-3c75-9ecf-6c5f98d02206 | -13.06845 | -42.13678 | 2024-10-27 03:38:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 92ba344d-00d2-3556-88ff-c910c3cc6bf7 | -12.92295 | -42.28632 | 2024-10-27 03:38:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eca16e5c-71ee-311d-bd94-95d7f455a229 | -14.28085 | -43.24825 | 2024-10-27 03:38:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2016dc90-91ed-3209-8a50-c4199c8b5159 | -14.28065 | -43.25168 | 2024-10-27 03:38:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ea5dcf66-35cd-3b17-835d-45f7bf728e07 | -14.27979 | -43.25365 | 2024-10-27 03:38:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8c679e0c-6d4f-33f3-9d01-4f207fad7bc3 | -14.27587 | -43.2507 | 2024-10-27 03:38:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 784acec1-eca0-3028-b15e-b5ea3e7367f1 | -14.27501 | -43.25269 | 2024-10-27 03:38:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 76727cac-f5b5-324e-9350-5c871191bfb2 | -13.82873 | -43.23619 | 2024-10-27 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 99a8f9a1-c605-3582-918a-878cfda909de | -7.58534 | -42.28688 | 2024-10-27 03:38:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bfcbc689-2e20-3bee-9f6f-c47cbf795159 | -10.90783 | -43.03383 | 2024-10-27 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdb4ff72-0a62-3062-97f7-1f9bb10a6e69 | -10.74542 | -44.38271 | 2024-10-27 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e0174de-812e-33a9-95db-20c3abd22ab7 | -10.60722 | -44.272 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4f2df4b-d08a-32e4-8358-26846976a60b | -10.60653 | -44.27553 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f90d2113-d1ce-3a36-9a65-c8e02136c6ab | -10.6063 | -44.27352 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c038400a-7c21-3e3b-abe4-b66221c17b44 | -10.60081 | -44.27258 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad937956-2e78-3332-b998-993293b0f166 | -10.60017 | -44.27604 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c6725c4a-751b-383f-b033-4fd165a7d97c | -10.59951 | -44.27951 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 37bfc44e-77a2-3223-aeff-c8463b1e29ca | -10.59885 | -44.28307 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7f523264-4ccb-36c5-85e3-cfadc7049ccc | -10.59468 | -44.27508 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8987b8bc-d889-352e-81ff-271b0fb001a3 | -10.59404 | -44.2785 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0e09e158-83f4-3407-bf8c-dd741c021028 | -10.59338 | -44.28202 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a7dd3ed6-3f9e-350c-bf7e-2fed32e192e1 | -10.57698 | -44.27884 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 125873e5-63bc-3759-8c5f-927c4a6d17ac | -10.57153 | -44.27769 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6b8aca19-ccde-38bf-8363-2c8a465ef5ed | -10.57086 | -44.28123 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a6bd92cd-73c6-33f3-8ffa-75be97b5d9ee | -10.56671 | -44.2732 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ee691b5b-126f-3922-958c-014b57a4bb4f | -10.56605 | -44.27668 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 089b2547-2d4c-336e-b788-5d50098a3a09 | -10.56538 | -44.2802 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 830582df-abfd-34a8-89c0-f6693574cb95 | -10.56056 | -44.27573 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6e0465dd-b22f-35c1-995e-e6ad33e3a949 | -10.55989 | -44.27925 | 2024-10-27 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3ee04b04-22fb-32a9-afe7-2cfdff6cb939 | -10.95038 | -43.93422 | 2024-10-27 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efd89f20-7cf0-3d58-979e-d15ebcbf1bdf | -10.94504 | -43.93336 | 2024-10-27 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbf7a4a8-b756-33d6-a2ce-773c9d65daca | -13.65001 | -44.11732 | 2024-10-27 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5343337d-5f41-32ba-88f7-ba5d7d07166e | -12.46582 | -43.78586 | 2024-10-27 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a5970a8-3544-3ef3-b4b9-739520b85783 | -12.45047 | -43.78278 | 2024-10-27 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42db9b3e-b938-3e3c-87d6-108a4ea7764c | -12.44847 | -43.78133 | 2024-10-27 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0f9f5d0-2b5f-3fb0-ab19-8839f82c3128 | -12.44789 | -43.78444 | 2024-10-27 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5eef5bc9-8b52-30a2-a2e3-ff6ca677d3c6 | -12.44535 | -43.78177 | 2024-10-27 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 718c71d4-08d0-3873-88cf-7b5c4da69d13 | -12.44048 | -44.39822 | 2024-10-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README29.md)
