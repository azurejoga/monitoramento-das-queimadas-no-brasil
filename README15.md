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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 802fbcea-a5f9-3277-9a29-f2a26667efe7 | -8.97106 | -45.03656 | 2025-09-16 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4356a1ee-b389-3ada-ae11-01cddb49c3b9 | -11.41938 | -41.41979 | 2025-09-16 04:02:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 216ad5eb-ab6b-3567-ac17-9cdb7dae399f | -6.43419 | -43.31198 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b20154fc-1a87-3710-a28f-47eecca466fe | -7.40177 | -50.00202 | 2025-09-16 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 155e63cc-ff5a-3ff7-a194-2d389acf2c4e | -12.0605 | -46.55438 | 2025-09-16 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92ea51a2-bdeb-3cec-aec3-c8fe374d76c4 | -7.44797 | -46.15847 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35517820-2f3b-3b43-a3fc-5e704e682c70 | -7.19767 | -48.60781 | 2025-09-16 04:02:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91a15e3d-5b9c-394a-8ee3-f3488bb7c2d6 | -6.45088 | -43.32341 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8e3cd83-e7b8-3d15-a4cb-9c547b1bfba1 | -6.82475 | -47.85891 | 2025-09-16 04:02:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 24f47323-032b-357d-8246-e8a13a7ad238 | -7.72401 | -45.30594 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d66e7ac-6c8a-33fd-b1e4-c491ee7261bc | -10.71397 | -44.75351 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 59a6be52-2277-30ed-96c3-6ef7c472cbac | -11.12936 | -45.33977 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 373f7e84-eb1b-3999-9f8c-2af2cf26f03f | -5.74326 | -43.92482 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47d8c07f-1a3b-34fe-a82f-c7d69f10ce9a | -6.6711 | -45.54142 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe21d4c0-93fe-3a5b-b2e8-17b357aa3bfa | -7.09286 | -39.67135 | 2025-09-16 04:02:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 9865dfdc-4189-3430-8551-9768f04a3bd3 | -5.00442 | -47.64462 | 2025-09-16 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a134da15-27e4-3e42-b992-713c2bdb8508 | -9.11693 | -46.92413 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07ae27df-959f-3367-a472-2f306aa3f975 | -12.43894 | -44.74876 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f5d0612-5c86-358c-8902-072b62e0af3c | -6.96736 | -44.44691 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 02217b2e-b740-3621-ae42-af3ab3e55056 | -11.43499 | -46.92607 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddb7efdf-7799-35a4-8f50-759db01e5a93 | -6.06057 | -43.55395 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 23485ac0-c1a5-34df-a822-8f23443b4d18 | -5.21103 | -45.18139 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adedb6db-bab0-33ae-b1b8-b866a156726e | -5.63801 | -43.17237 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 857db404-c921-3018-a5f8-84780d1a9c5d | -6.54624 | -44.00361 | 2025-09-16 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4bb9494-aa73-30f0-95a6-2a5adb9aeefc | -11.74098 | -43.37663 | 2025-09-16 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6034e9ee-e87b-3ece-8faf-197111214414 | -7.13477 | -47.9786 | 2025-09-16 04:02:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 68c57a48-cccb-3dfb-a50b-486b34605e99 | -7.03168 | -44.14988 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 92afb446-3175-3e0b-a198-5c32dcfc13d2 | -6.97051 | -44.53863 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 151de78b-e297-3ac5-9aba-a23713b95602 | -10.23583 | -46.74085 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5c87c2e-7a0b-3f38-b54d-166c863c7647 | -5.6715 | -43.50187 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 412f25dc-c9be-3c1d-b36a-c25490f4ff8c | -5.66364 | -43.31834 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1213272-480d-387a-b311-39a60b45974e | -5.79003 | -45.9413 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da141421-f4b2-3b76-af23-bb50002ba56b | -8.96654 | -44.19426 | 2025-09-16 04:02:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| adde6ef1-45ac-303c-9ab0-61356e708c54 | -5.80833 | -45.70193 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1663cc39-0d65-3beb-ad33-2f74af98af92 | -10.72486 | -44.74861 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8249c589-c297-336c-b891-2e02c128c1bf | -5.79503 | -45.93777 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a81c8fd2-d093-324c-bfa4-af280d5a058e | -7.45083 | -46.16718 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b582b81e-0f27-330c-bfbb-f420cc69890e | -11.13099 | -45.33018 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a660dd2-e0f9-3ccc-a8e7-8b1ad9787629 | -5.99945 | -43.70419 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be912513-8869-3f3f-aad2-7eb991627268 | -5.83161 | -45.26772 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9af31540-7157-3543-926b-6857ab438cef | -6.76337 | -44.71467 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c4dac17-3bba-304b-9347-772242fa7d5e | -11.45289 | -46.9289 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1bb3971-cb9e-369e-95e4-1aea92158640 | -7.39053 | -50.00018 | 2025-09-16 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae09c4f1-f683-32a1-b5c2-f7b87b8f2e68 | -9.10312 | -44.85412 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 43b82cb0-4b05-3206-9475-c4f1f7368e1a | -5.94167 | -45.71026 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b59ba7e-841a-3ca9-8664-285388155bb7 | -8.6006 | -46.33681 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78a6bf0f-d79a-3c7f-8729-5eb3fbdde450 | -7.14226 | -47.98708 | 2025-09-16 04:02:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3d1b3aa6-483b-3fff-aaa0-671939092e17 | -6.53029 | -41.82955 | 2025-09-16 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ed7dcf9e-7a1e-36ce-982c-31728e1170bc | -6.63324 | -38.54755 | 2025-09-16 04:02:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c726b6de-3871-32ab-85bf-45e0d1b5fb60 | -9.97965 | -48.36411 | 2025-09-16 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b982bcd-8bdb-3dab-8f87-5df3a775acae | -7.42372 | -40.07826 | 2025-09-16 04:02:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bb664d9a-8f60-322a-9183-62e49500db0e | -5.34898 | -44.8199 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c930963-426f-3549-80ca-32fd881aedd6 | -7.0528 | -44.11564 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 713f4269-35ed-3a9b-a894-bb5c6b7e3039 | -7.6254 | -42.24952 | 2025-09-16 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f6c73794-cee1-3fbf-b9d2-798f7ca426e5 | -8.34722 | -44.72263 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdbc4484-ada2-35bf-a465-0e856bf11733 | -6.00259 | -43.69837 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10306d96-c0d3-32f4-9b22-1a0f0e68d54f | -7.44167 | -46.16967 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88464312-a0c4-3691-a80d-36c62e4b5ab9 | -11.12855 | -45.34459 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 30781a3a-dd72-3100-b1bb-953af2f3c681 | -7.13542 | -47.96963 | 2025-09-16 04:02:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c69ed31-bf17-3d9c-a2cc-57072b2a378b | -8.65819 | -46.35448 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 303dc3e1-26ca-35be-9c64-ee793dc2a8db | -11.69793 | -46.87261 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8886d876-5322-3d7b-8682-024735d4b632 | -9.05466 | -44.84283 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c0ebed2c-0070-3053-a59b-abc7fd754255 | -11.12773 | -45.34939 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c37a7516-2eac-38a8-ae57-b13cd942048c | -8.62028 | -45.7198 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68423d40-657e-342e-9259-0f13fd2dd811 | -10.96186 | -49.57289 | 2025-09-16 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 258dbe86-61cb-3ce8-93f0-215bee936723 | -11.35182 | -47.35466 | 2025-09-16 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87332200-911e-3484-8e7a-13150dd08f74 | -6.98339 | -44.77225 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b16c9cc-01fc-374b-a1c0-d3a3829c1298 | -7.67691 | -46.29502 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97a730b8-f396-33d5-a880-80e5aaee36f8 | -11.20966 | -41.60501 | 2025-09-16 04:02:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3c5824ba-73f8-39d3-84cc-0033efe143e0 | -7.27625 | -46.5998 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7798fe8c-3e8f-3ab8-b8fe-dbbced24281e | -5.67151 | -45.04783 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff8ce377-25ad-3048-b171-1dceb9d44960 | -10.95597 | -49.5731 | 2025-09-16 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3631639-2911-3452-a223-dc86d8f06b3e | -11.13179 | -45.32545 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2da0736f-cb72-3e8f-9f8c-052bc9088ec9 | -8.08684 | -46.83291 | 2025-09-16 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 446af0bb-2fd1-336f-986c-bf4097151b01 | -7.68774 | -44.50697 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00831aa9-16dd-37db-b343-501ec9dc98ed | -7.85723 | -46.10398 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a87907e9-ddd4-3467-aaa8-7c6df276ea50 | -8.12754 | -50.16821 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afab794c-5b66-325f-a164-77bb96c4f483 | -10.71914 | -44.76824 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| de78454d-f82d-3cbc-ad90-14c5b17e0464 | -7.08147 | -44.54965 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1483655-6d4e-3a78-91a3-80700086cbf3 | -5.98801 | -45.84734 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0545b0a9-552d-380c-a662-310a51ab67a9 | -6.83206 | -47.84716 | 2025-09-16 04:02:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 033d76c2-a37b-363f-b358-f085d4369ae8 | -4.48701 | -48.11053 | 2025-09-16 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ec1e731-b5b1-3ce1-b8ac-bbea16419a60 | -7.27341 | -46.59023 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6c13feec-9922-347f-9355-2e0ccea5d59a | -7.01063 | -45.6384 | 2025-09-16 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3446409-b358-38e6-91b9-b085203982aa | -8.97714 | -45.04748 | 2025-09-16 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f2347ad-3c7c-37e0-b1f1-1626b7e9f690 | -5.74185 | -43.93086 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11cb1bfe-93fe-3544-b60f-1a6bf8b04d93 | -9.47696 | -54.43666 | 2025-09-16 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27d6429d-bf56-3443-b978-b14b87b44309 | -9.10149 | -44.8637 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| a2dba247-4518-36be-9202-caeb49f134e4 | -6.28758 | -44.08772 | 2025-09-16 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b189b95-a432-3363-a3ff-2acc026e6f26 | -6.54547 | -44.0083 | 2025-09-16 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9defdf48-5b51-3dae-a62e-3961b8c7ea55 | -7.44552 | -45.8396 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41f18a0d-69cb-363d-9458-93992fbb8ea1 | -6.89598 | -43.88582 | 2025-09-16 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 966f6b30-0947-38af-a40e-e108be1acd08 | -7.29742 | -43.93099 | 2025-09-16 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5dfee6c3-2ba7-3544-8f9a-13167cec0c4a | -7.4466 | -46.16639 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c6406624-22d6-32a6-a6ef-f066185a4bda | -6.16189 | -45.11357 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39e5eeb1-8304-3725-ba31-19494c5ef899 | -8.22055 | -45.58512 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f3f66502-869d-3c79-878d-8a61487b8bbf | -9.0977 | -44.86301 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 3528cb3c-a1ba-324c-8a64-6c3001e4a3ab | -7.27416 | -46.58588 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c2f97f5a-329e-348c-970d-95fc1b827cba | -5.6644 | -45.06526 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d101e80-aa02-3298-896b-37bab9fb54f4 | -11.5838 | -45.02678 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)
