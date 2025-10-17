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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85e088d7-3513-36cb-8828-15119518a633 | -7.9563 | -44.11468 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e42a5eb8-abc8-3737-ba50-a2877bcbbd44 | -10.29925 | -43.97851 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fcdc0ebf-3aef-3a1f-bcc9-b02288356e1c | -6.7216 | -44.37661 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ab3ed35-e0be-3719-8066-0c304f28e24d | -8.09651 | -44.98372 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d3a2e73-1200-3bd5-b323-00e7484188d3 | -5.40871 | -44.41609 | 2025-10-17 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1f402ca-f151-37b3-8950-41abd95dd74d | -10.65452 | -45.29299 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb9efed9-ae28-3356-acfe-d455385c8a61 | -2.87535 | -50.71978 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 355137c6-f8fd-3fee-96fe-3fc3aaa8e98f | -7.17353 | -42.3696 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aedc3781-c0de-3346-bb20-01c58ca588f6 | -5.74623 | -47.4727 | 2025-10-17 04:19:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca7d4582-2e02-31f3-8680-cba10286f11e | -7.47011 | -42.15896 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b9da532c-7661-32c2-a045-9a56b8fccaf5 | -8.30531 | -43.43642 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 57e59757-d683-3dc4-9a66-fdc50469300f | -7.17819 | -42.36236 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3801730f-6b0e-3624-b136-fac7c89126be | -10.14191 | -44.53895 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 628331f3-2209-3240-8b11-7181889aabbd | -8.61819 | -50.44781 | 2025-10-17 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d4a5b75-3c1d-3222-8ba6-d11f6dc08bad | -8.47066 | -50.10272 | 2025-10-17 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33eb57ac-1f42-3434-be15-bb68df5e687a | -4.61084 | -50.82512 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a44d7c8-0fae-32be-b316-cda259c06d41 | -4.15269 | -42.20998 | 2025-10-17 04:19:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8bcd19fa-9d1b-3b2d-8155-46c510fc10d8 | -11.47405 | -44.1875 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32b27ffa-e7e9-338d-a5fe-e57b547d2961 | -5.90569 | -44.74162 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e019c12-c456-3b46-95ee-173543277846 | -5.49361 | -42.16384 | 2025-10-17 04:19:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 90f2633f-2ffe-3a72-8e58-116e5685c93e | -3.50423 | -52.49105 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 23c39602-3a1d-3de4-bfbc-4c816f68ea08 | -5.13896 | -44.96228 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b889b28c-6e60-39ab-a16a-11ceef0a01a7 | -7.46539 | -42.687 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a9726e6-75c5-3c70-b259-29dfa071d226 | -6.3315 | -43.9536 | 2025-10-17 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2acf4108-2a4e-3b00-9eec-aecc11944611 | -8.39356 | -46.27276 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f21f234c-6e8b-3ac6-9a8e-f07c4b81e52b | -7.29331 | -42.29598 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18f39f5e-a6b5-39e0-b589-a4d533e5fab5 | -8.38284 | -46.31842 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18146170-03b2-3db4-8f7d-a173ca0402fb | -6.70403 | -44.38092 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c7f8ad8-53c3-38bf-9144-e6655bdc4594 | -11.48081 | -44.18856 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1114fa22-5f9d-3427-b9cb-1e505efbf35d | -3.66211 | -50.27075 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2949dc4-fc74-35a4-8143-50dfde985abe | -8.78799 | -46.6819 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0106d379-b649-3b87-bc5c-2f3082cd330b | -7.044 | -42.73583 | 2025-10-17 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 62817718-79f7-3dbe-99a8-6ded1718819a | -10.65499 | -45.24652 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76e43c6e-7d87-3559-a23a-f7cce42dc61a | -4.51766 | -50.40911 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c58e9ecb-5a52-3d10-9a7c-8b7d78aa1af1 | -5.4652 | -44.64317 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 681ee62d-6498-321f-96e1-ebf04a5a9e32 | -8.3773 | -46.31022 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 903ed200-6e5d-3602-9b6d-1e0bcf9c946d | -8.25978 | -44.06417 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fdea9363-b2d8-34ec-be55-6c07f266fc75 | -9.43764 | -47.9016 | 2025-10-17 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1457d275-09ea-3084-899a-541693eda7fd | -4.26255 | -49.6945 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f36d702-0faf-31f7-bcce-be62b4f9a41c | -7.66847 | -42.5954 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2e9ab4e7-bf3e-3981-b2d8-617cc463c152 | -11.40709 | -44.1959 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3274104-0ac0-31e8-a7bd-9c48965672b9 | -7.34141 | -43.86745 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 397af7ca-12f7-3664-8fb0-714e40d304f2 | -10.50438 | -43.41188 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0719ea68-87a5-341e-8504-7282c3841d2b | -8.72834 | -43.86734 | 2025-10-17 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b17ad29a-8be2-3109-8aba-d20601c517f5 | -5.87735 | -44.83599 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bf14461-5572-389d-8c93-d6e230138ee4 | -6.42613 | -46.88203 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b32025fd-c3fd-3198-83ab-9a383cc8444c | -6.42676 | -44.71833 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8c91272-51f7-39ad-9831-065470d032e0 | -7.00528 | -43.97335 | 2025-10-17 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4bfbacb-60a4-35e8-8e8b-06bfc7c07451 | -7.15775 | -46.52835 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f39954c-fc54-38de-9b53-533f585131cb | -9.50978 | -47.26581 | 2025-10-17 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fddbf97-0484-35ef-af51-1e899eb479f5 | -6.13087 | -41.76937 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a6f29922-357c-3439-a342-ce72d8d0f5ce | -6.33134 | -45.06348 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53973363-f242-3977-95a8-b270ddf3fb7a | -9.6201 | -49.13227 | 2025-10-17 04:19:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0cb11f5b-f87f-3895-8d4c-60fadffdcd59 | -4.0177 | -48.96798 | 2025-10-17 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee9cc003-6c1c-3239-8ef1-ab5598c9c890 | -7.29835 | -41.95061 | 2025-10-17 04:19:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c8b9f8ef-8e22-320a-8c7d-e45835c27178 | -4.9556 | -44.96197 | 2025-10-17 04:19:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0e3ae2c-3c35-3078-bae6-6d3e2cd6077f | -7.07452 | -44.25137 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df483c21-091e-3f39-9da9-a6d244fb83a7 | -9.28553 | -46.91172 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1722203-2e0b-387e-b204-c5d4220edc49 | -7.07731 | -41.97665 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1356c522-39ff-3fab-a5ff-66040f9fe97f | -4.10997 | -48.0184 | 2025-10-17 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f97356a6-a18f-3bbd-bae7-2bb788c57818 | -5.30917 | -42.65107 | 2025-10-17 04:19:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3fbf238-5880-3856-8f9e-24f4f2052db3 | -5.58632 | -42.58745 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 67044174-1097-32b1-9aea-431b90c2872e | -4.42849 | -42.88509 | 2025-10-17 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f7a1ad7-8950-3bdb-988a-a7eab8772016 | -6.27242 | -52.63004 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ae13ac6-0fd3-346b-8b21-b918072add35 | -6.20204 | -41.7304 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4df0b664-9498-33d4-9da9-77696a3ae049 | -8.37304 | -46.25124 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43de0dc3-8044-3dc3-949b-14ecbec78091 | -7.22162 | -43.80534 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d25eb478-4a4c-319b-834b-228b27f49a5f | -6.22208 | -47.03918 | 2025-10-17 04:19:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f395c8d0-5838-3f71-8e0d-118591302ffa | -8.07712 | -45.41312 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 440dd1a1-fe0e-3f00-a5f2-796b24eeb248 | -10.25891 | -44.03979 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 207bc673-1dc1-3379-8530-43568a046a21 | -6.75019 | -42.36395 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b4fa9a84-236e-38b6-9b26-12a7da8a244a | -8.4533 | -46.23847 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a92e4eff-874b-3f11-a540-3e7b47a231ad | -11.49706 | -44.05874 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 001bd5b6-7720-371a-b2c2-104c59122d2d | -8.08594 | -45.42157 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20eb720a-8671-35b1-9149-529d581a654a | -5.19991 | -47.48656 | 2025-10-17 04:19:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c273c48f-12fc-3a2e-a192-a9270913d224 | -5.24728 | -43.22183 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c06f93d-d547-38fc-aede-2e64bdcb7766 | -6.42791 | -47.29864 | 2025-10-17 04:19:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a123ecdb-2f3c-346a-9b38-5ffb1d8d12cc | -9.10062 | -48.91538 | 2025-10-17 04:19:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40a4a147-f00b-31dc-a042-d2d36837ec2f | -7.10804 | -44.73452 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf23d37b-8ba3-37df-aaeb-a59199dc4ee7 | -5.22279 | -46.1925 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e9953c1-180e-3e4a-819c-ffe81a85ae05 | -7.05253 | -44.26213 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5faf46e-1abc-3459-8f21-a8f936e69875 | -11.48473 | -44.16278 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78e367cc-f1ab-343f-bca9-7a1775d035e4 | -6.927 | -45.13019 | 2025-10-17 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3a2415a-baeb-3cde-a441-0b2cbed75194 | -5.31681 | -42.94835 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d88396cc-a0c4-3e59-a10d-32915c5ec2ee | -11.37782 | -44.19569 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9b09e69-2c59-3ebd-85f2-f90566167a7c | -6.70786 | -44.37799 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 218b28b6-0190-388f-a600-0c783d7ddbcf | -5.88123 | -43.91837 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d9f4132d-e0fb-3d5b-ae7a-0914c3f14792 | -7.33734 | -44.15744 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e41e641e-57ee-368d-99f8-0199808fdc43 | -5.23497 | -42.01612 | 2025-10-17 04:19:00 | NOAA-21 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a4380048-6201-3585-8d36-b29c22d9f43a | -11.40317 | -44.19905 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef3f2ece-f336-3736-a716-1be4381ad728 | -11.14511 | -45.85828 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a967627b-cc54-372e-a45f-cca41b9ce39b | -5.25436 | -44.20464 | 2025-10-17 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e298d8b2-77d5-32a2-9223-762b6a859a90 | -7.68278 | -44.62759 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d2b2887-d675-30b3-9e75-383f5ba87451 | -8.25349 | -43.43597 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1591f50d-45e9-3297-a322-ae77c154fc62 | -9.02935 | -46.62085 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1abeafb-4e50-3a8b-9e64-c7616c1bfb75 | -6.51752 | -46.50976 | 2025-10-17 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76be8641-dafa-3278-ae80-030a6cbda280 | -9.24723 | -44.36613 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64539285-0784-3d8c-9a62-c432360b8f16 | -11.39209 | -44.24986 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5578c76c-0a97-32b5-adf1-741a8f1efb00 | -6.79746 | -46.89008 | 2025-10-17 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f936127-c737-38fa-9a49-3866cd9ab104 | -8.84191 | -45.9796 | 2025-10-17 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README55.md)
