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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cef4d9b7-ace7-3398-8686-59fb750aeb8e | -5.73671 | -42.87139 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9e182fb4-6220-31cf-947d-b2d6cb3597eb | -4.31573 | -48.09108 | 2025-10-01 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ba57bc9-6732-351b-91ff-7c012a66dbdd | -2.24578 | -47.89046 | 2025-10-01 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f834c79-5cbc-3d60-be20-486192861739 | -8.29533 | -50.76682 | 2025-10-01 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fe45186-e2ed-378a-82ec-c5d0b9c4ef75 | -7.04962 | -43.23753 | 2025-10-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b2193cba-c528-3524-8872-e507b3b5d96a | -6.53821 | -42.83716 | 2025-10-01 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 70ad738b-83c3-3c85-904e-7f1a5b167a7f | -6.26602 | -44.17807 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4a40529-3d34-30f3-be29-5df57374ace8 | -3.25528 | -50.11752 | 2025-10-01 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6db83ab7-36d7-3ac3-8823-fc8f736321ab | -8.59655 | -44.63694 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c096ba51-a780-3d44-94b8-f9d51f7f3e39 | -3.93501 | -41.59786 | 2025-10-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f2bd6b34-069e-3519-898f-b7651bb0db64 | -6.88645 | -44.54128 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a5f5aec-835b-3b3e-8af4-2a5c86cbf38c | -7.09492 | -45.55494 | 2025-10-01 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1ebf99a-32ad-32a1-8392-48ec19051463 | -8.91878 | -46.07707 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5b2af78-3ec5-310c-8590-d31dd6afcb5d | -7.56617 | -46.77977 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19e3ebcd-228c-3f43-8e32-875143f755f3 | -5.6465 | -43.91743 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e6093540-d00c-3df3-8d85-b03da77151b3 | -5.65043 | -43.9358 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b1da12c-44b0-37e7-acfd-c68da053c649 | -7.17861 | -41.6968 | 2025-10-01 04:19:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5720a5d5-ba17-3960-ba97-68d21fc9c2b6 | -2.59292 | -48.1233 | 2025-10-01 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| adf40faa-4f4b-3972-9cee-930aaf9dcc1f | -5.93227 | -45.89133 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1e1c93d-7ea0-3d19-aca3-830d2fdaef4f | -7.54749 | -46.11648 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 267e168b-926a-3dd7-a363-6755c569fe4e | -8.70398 | -44.84304 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5701f7c8-8f90-33ed-8be2-c53d520b2cfe | -3.0902 | -47.01439 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27c419a2-9b8f-3267-9aba-5e5a9705dfe7 | -3.49551 | -52.46837 | 2025-10-01 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ace8798-4c85-333a-8020-0b6ee7f5f47f | -9.32492 | -45.68149 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e728916-95b4-35da-b150-64955d1b4deb | -6.71732 | -44.60313 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b99d5afa-6d07-359f-b9a7-44e5303071a9 | -6.08365 | -42.43582 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b121838a-0e69-315c-a41f-fc00130da9a7 | -5.78133 | -42.85906 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a546e125-0559-37fd-b693-dc13284bd4a2 | -8.85178 | -48.41647 | 2025-10-01 04:19:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ef4dddd6-e356-30f0-b040-8a896b2d1af5 | -4.52332 | -43.78735 | 2025-10-01 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69e14c6a-1ba5-3b9f-a69d-0c995f36354b | -8.55225 | -44.72628 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 983ec7c2-aa47-3748-b1ae-cd4806aff960 | -5.79747 | -42.77547 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 176131b8-6a37-3954-a5f9-339b2386f161 | -3.2401 | -52.89242 | 2025-10-01 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a5a24e0-8f2d-3ad8-b8fb-6363e9934b0d | -4.68408 | -50.47902 | 2025-10-01 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ed65b5d-3791-3340-9af6-eb6fcc233dbf | -2.70349 | -44.82404 | 2025-10-01 04:19:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7adac12e-d0c5-3563-a0ca-e5c42321d4fc | -8.57822 | -44.75524 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69f63ed7-c60a-3016-89a5-d31093212372 | -5.8317 | -43.92834 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e277900-84a5-39a0-9eed-e62032d36c6f | -7.09602 | -45.54799 | 2025-10-01 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11cdb800-ba2e-325b-8d5f-eeea57f98508 | -5.15521 | -46.40666 | 2025-10-01 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3de840ba-7a64-3dd1-b7e5-c69887f666f3 | -6.47767 | -46.55075 | 2025-10-01 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e8ac904-4644-331b-a9bd-ff9e1c8aebca | -5.82514 | -43.94862 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ca24bf3-8a56-32f0-b4e5-f9b8cb11bac8 | -5.80031 | -42.77967 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a731838c-e5c0-3f87-af69-53c9af9422c3 | -5.61911 | -43.23384 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 664b1a96-af1d-3035-802e-553401efcc8d | -6.23773 | -45.33591 | 2025-10-01 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 929a376f-5695-308c-a4b2-0723f796042d | -6.28517 | -43.65952 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b029d8ec-f5b5-3e70-9c8b-df42ffd52303 | -9.27054 | -45.74767 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0b2fecd-579a-38af-80bb-577bce896da8 | -7.05712 | -46.41817 | 2025-10-01 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6419f65a-ada0-3236-b328-3ab355d4004f | -3.27551 | -44.67196 | 2025-10-01 04:19:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54b3c1df-d50c-3cfa-9db1-8d57ab96aed6 | -5.41457 | -41.32231 | 2025-10-01 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5b310ca5-3363-3383-82f5-4e59be782e45 | -5.49846 | -42.734 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cc3a186a-194b-3a24-b56c-c57aa2c73cfb | -8.53519 | -44.70219 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe4b3dc4-2aeb-32e6-9f30-eb4e6f9fd012 | -5.27865 | -42.77161 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3d73376-dac0-3143-9329-822e7ac1083a | -6.36659 | -44.57883 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1dd4d75-c075-35ff-8d4b-11823bce1d58 | -6.07293 | -42.66913 | 2025-10-01 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 59247cc9-90f9-38e1-84ce-c71befe4d14a | -6.27769 | -44.0591 | 2025-10-01 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0ddc6a57-2787-3c58-93ae-ddbd2899fc7f | -5.06177 | -45.60462 | 2025-10-01 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fb3cdff-8f66-3f38-a6c0-124ff1e19768 | -5.94586 | -43.32047 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a89f95ab-913b-3a64-9de7-a7b02f2bb520 | -5.61801 | -43.90234 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 614c3245-ea89-3dc4-8ce5-327daa276894 | -8.59136 | -44.73593 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 953888e3-8ca1-3588-8f8c-cc6e3b9fdc32 | -5.82069 | -43.93373 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c6fffa8-bbb7-3a58-b61b-f512663c3221 | -6.3656 | -44.95676 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 137effad-03f8-3cef-8b9d-1939fefff5d1 | -9.89408 | -45.93751 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dba0815c-8971-3975-bf9a-f2747941b9d6 | -7.62802 | -45.45542 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4654a37f-a86e-3bd2-b499-e1d3a629941b | -5.90688 | -43.92653 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49c0b8f6-840c-3d38-9a2f-08e74c53fd50 | -6.6657 | -41.39419 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3280bcc8-fdf0-3539-a293-b666fc0ee95c | -3.09313 | -47.01899 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 7ef99e82-e26f-3e96-8296-31ffcf3e4d04 | -5.64319 | -43.91693 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 6d717061-a17c-33d0-a26c-ba67f759c872 | -5.5211 | -42.72239 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e250a4ba-330e-3626-a864-7eeb86325c36 | -9.37909 | -45.83619 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d78d4cf3-568e-3c12-84d2-65dae0ff3b63 | -9.41678 | -47.33097 | 2025-10-01 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f25739c-c6cf-33ba-8fb6-88f2753820cd | -8.38503 | -48.64668 | 2025-10-01 04:19:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fe4a967-ff88-3182-bc67-305d2aa91076 | -2.59751 | -48.11916 | 2025-10-01 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 435849fb-a05f-3753-ba44-1d1d73c2d22f | -7.02389 | -44.46692 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 607aac0d-c91a-36a8-ae36-0be25bb7cd13 | -5.64488 | -43.92785 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cab913a3-e926-307e-b277-f2d1bf32fb3f | -2.42527 | -47.2275 | 2025-10-01 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9554596-4ac3-3a2a-a5ab-83c7b0e3fd55 | -9.80561 | -45.93702 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e96ef1e9-8015-3737-94d6-21f755ad5e67 | -5.73104 | -42.86308 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 10dc1b3f-6e10-3850-ba7a-2ee5feb5cfac | -7.47527 | -46.46354 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dc912a0e-199e-3d31-82fc-bf0e3559e218 | -7.02877 | -44.78663 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f62a617-1c30-3d2b-8e5a-0d2167b2ca25 | -5.27131 | -42.77424 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 372925f9-397f-3b03-a5fe-6cf6e54eda7d | -6.69552 | -42.79603 | 2025-10-01 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5ece4c1f-b2b3-3aff-b802-3ed7cababcdd | -5.49394 | -42.74081 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ca2ce917-2794-3850-93b6-09d64b16ee23 | -6.90677 | -44.97878 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 306eda6e-d64e-30ac-b1b1-92bb55ab0f28 | -5.64203 | -43.90251 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4bf3c3b9-6b83-38b7-8e3e-3523c6530575 | -6.09056 | -42.43689 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6ac1d9f8-98de-3380-82b3-54efa553bb4b | -5.89003 | -42.51139 | 2025-10-01 04:19:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 943435f2-89d0-3783-b03e-1cad3bb9f23a | -5.90302 | -43.9295 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30b91320-9325-3410-89de-e451593e0d90 | -7.0549 | -46.41043 | 2025-10-01 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c4017b6-3d3e-3213-9aeb-57fb7bbf170a | -4.81238 | -42.76128 | 2025-10-01 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d1d7817c-ee4a-3d24-af39-925ecfc1b77f | -6.23968 | -44.19523 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 333f1313-c929-33d6-bdce-5fed07fe8f48 | -5.84056 | -45.76037 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4673d009-d894-37f8-aeac-8a76354642f5 | -6.56689 | -43.40071 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 54eef7f3-78db-3440-9d29-684571787dd4 | -3.9164 | -54.56178 | 2025-10-01 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7113f95-4405-39ef-b801-f8db2e237564 | -6.2362 | -44.15213 | 2025-10-01 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a966083-b057-3cb5-87ad-ac9d1d04407d | -5.62665 | -51.93841 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65a3796d-bbdd-3e75-833b-4edc126be518 | -8.54012 | -44.69226 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 649822c5-a56a-3f14-b3b5-84c242edf764 | -5.2075 | -45.67449 | 2025-10-01 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8afbc356-7f73-34f1-9e75-b473306207ed | -8.2844 | -45.37245 | 2025-10-01 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a914862-b372-3fa2-b576-a312079359fe | -6.28293 | -43.65194 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d00bbaed-d4ba-3cc6-8086-22f1879fca93 | -5.65196 | -43.90405 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd4fd82e-35cc-3764-9737-6b3104a10c38 | -6.04818 | -43.60788 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README33.md)
