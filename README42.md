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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64cb44c1-79f1-36af-9cd6-5beb4edf629a | -3.98173 | -47.88191 | 2025-10-11 05:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e4f887d-ac7b-3d5f-8b23-13f51b2258f4 | 1.19187 | -50.87658 | 2025-10-11 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fff9dd7e-0fd8-31dd-a812-829bbfa36a0b | 1.19673 | -50.87578 | 2025-10-11 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94d9b568-dc8b-39de-aca6-3d262a2157e9 | -4.42621 | -47.60539 | 2025-10-11 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c678f5f9-7f07-364d-86f7-0fe8fd3671b7 | -3.42411 | -52.73345 | 2025-10-11 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2a87d83-3f83-3088-ae4a-9f118f9bd2f0 | -15.15531 | -56.82321 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 582ba756-5617-3c84-a31d-8053d8de8de4 | -8.89135 | -66.86385 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36e363c8-f4a1-3aa2-b090-052c4f4da20f | -9.17365 | -68.19989 | 2025-10-11 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef48b5c1-0fe3-3226-a91a-1637687bd6ef | -8.87539 | -66.77866 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d6b2936-4908-3241-9a5d-165d09210091 | -8.43014 | -70.10748 | 2025-10-11 05:23:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9a9121c-ee83-38f2-9273-7f4d9921eae1 | -11.53131 | -49.28579 | 2025-10-11 05:23:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f105199-95f4-3109-afab-60593ac00d19 | -9.81769 | -63.18008 | 2025-10-11 05:23:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| deef474a-61cb-3205-b3fa-8aec6979da6b | -15.2036 | -56.74507 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55c24296-967a-3d39-8f8f-3231db36f960 | -11.62146 | -48.79611 | 2025-10-11 05:23:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30bdfae1-eadd-3e09-a3ac-8bfee7e19280 | -15.70312 | -48.40269 | 2025-10-11 05:23:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64c9af75-e2c1-36f9-a89a-b9dd97e1ed9a | -7.90532 | -70.91629 | 2025-10-11 05:23:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 448b8d77-b12b-3609-8aff-18c7ae0dfeeb | -15.17507 | -56.73611 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b20df13-a090-3901-b0bd-82c82c42caee | -5.25605 | -50.90466 | 2025-10-11 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17825900-4d44-3b6d-a582-42e5bc34386f | -9.81426 | -63.17952 | 2025-10-11 05:23:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f83e52f-4637-3cb9-9ac6-561e89d6f6b9 | -9.17331 | -68.17481 | 2025-10-11 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1448a3b3-2fb4-3228-a35a-34b8a32e6fac | -13.01252 | -61.43314 | 2025-10-11 05:23:00 | NOAA-20 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 520a1b16-4bff-3bc2-9a55-4a6664cba872 | -9.45988 | -67.11266 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d77d764c-f967-3247-8361-2cc0c9dd4709 | -15.2008 | -56.86188 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96ecdb95-4ee9-33ed-9504-51f298592fe4 | -10.56071 | -57.5172 | 2025-10-11 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 106dbbcf-bb1d-37a0-aeb7-559e5a1a6135 | -15.18764 | -56.76972 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85dcc600-90a0-3cc4-9425-1eae9c3e4bdd | -8.54896 | -67.02442 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d4a3598-69bc-361e-b308-5ac7882eb7ad | -9.1649 | -68.16838 | 2025-10-11 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72318128-98c1-35dc-b5d8-a646ac312d9c | -8.42706 | -70.10585 | 2025-10-11 05:23:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d856faa0-4b40-3d00-8491-9e15d4fcdd01 | -9.54593 | -66.47318 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 201e4c23-f94c-359e-ba6f-2b87e1145eca | -15.19027 | -56.78196 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5e636bc-4946-3250-a5b6-6ef5dd49fe46 | -9.54248 | -66.46872 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fba5edcb-5b7f-378a-b788-df47f81571d3 | -8.7213 | -69.88033 | 2025-10-11 05:23:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efbbe3b5-b98b-3f29-9579-6c77a797c015 | -15.18137 | -56.75288 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78752a45-d941-3fcf-8201-05c6037d4101 | -15.18917 | -56.75809 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0363b36f-f0de-3bf4-97e6-dca78ca7a3ff | -15.22494 | -56.74408 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7a2e7c5-2837-3b22-bda8-ed0d3c846e7c | -8.43077 | -70.10408 | 2025-10-11 05:23:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e18b22e2-87fe-3104-9008-3b43790a18a7 | -8.86694 | -66.77712 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a28b4ac-9806-387a-b246-b5df42d12e9d | -15.1967 | -56.8611 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb86f490-74e6-369d-81b7-72ecced06e5c | -12.14254 | -48.02076 | 2025-10-11 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cd4a642-c8b2-3a1f-8d32-fe71de96f60b | -15.15845 | -56.83151 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 319e4d32-bd9c-3a19-b6dc-0fd43745da13 | -15.19259 | -56.86034 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 636ff346-9109-3c57-98ea-2a7f1a19bb92 | -15.21313 | -56.86418 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99f144b0-9e95-3a09-a8c2-2dd771f6b5fa | -15.16984 | -56.84113 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f6452bf-d182-3a35-ac83-bc19e156e8af | -15.1604 | -56.71825 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bac1afef-5300-38b1-9953-c96edb393ba2 | -15.18486 | -56.8551 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e1712bd-3a2d-34af-93d2-bcbaa6c3854c | -15.22077 | -56.74353 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1328c29-30bf-3452-af98-de8cb872cdf9 | -10.56137 | -57.51269 | 2025-10-11 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a6811af-939a-3001-ba88-be2ce2872d0b | -14.44035 | -50.35125 | 2025-10-11 05:23:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e7b76e5-e533-3ac2-97b2-eac15f5d1d5e | -9.81707 | -63.18385 | 2025-10-11 05:23:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc76a2d7-70db-3c15-827b-d7c09ea0026e | -9.8768 | -62.41175 | 2025-10-11 05:23:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b50d1c3-6705-3fc8-ab83-522c1bd205a0 | -13.59918 | -56.93645 | 2025-10-11 05:23:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b95d841-1648-36a1-932b-78f1bc5d1edc | -14.43621 | -50.35321 | 2025-10-11 05:23:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 116314fb-3301-36a4-b360-2ca991be7602 | -9.90319 | -57.80267 | 2025-10-11 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1305fd20-7ffb-3d75-b08f-a82ab6778ca0 | -11.53194 | -49.28037 | 2025-10-11 05:23:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59004692-5b94-36ee-8a82-eb7e6a9f1af7 | -15.19289 | -56.79416 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52c07183-32b6-31e4-a71f-6fb232a39de4 | -10.38866 | -57.64404 | 2025-10-11 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f93ed03e-689a-34cc-bfa8-00c291c89f16 | -8.41456 | -70.11407 | 2025-10-11 05:23:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84c85f04-e974-345b-a769-0beea5ae6e1a | -15.18124 | -56.85059 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab1bd25e-1503-3c14-b48b-2d37d5fae08e | -16.19618 | -59.33463 | 2025-10-11 05:23:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43c69a39-801d-39a9-97d6-b0c3d5cbf9e6 | -15.26833 | -56.90996 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c8746ce-01cc-3210-be15-fb9303ee1756 | -9.16868 | -68.17402 | 2025-10-11 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c933547-d581-35f3-ad53-236cb1d77d69 | -13.01583 | -61.43367 | 2025-10-11 05:23:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 774f4961-9ab8-3710-9e10-fcd81fd2e9f9 | -15.16774 | -56.72713 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a52b9c10-de52-3cc9-a83d-13b4a1a2c056 | -15.17397 | -56.84182 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e37b4f09-5b67-3669-be76-442b2e7af61c | -15.20825 | -56.74196 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 504eeb1d-5b5c-36ba-8ab5-132e7204ce92 | -14.6539 | -56.21577 | 2025-10-11 05:23:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bf0de1d-2161-3baa-8085-a88a876bec37 | -13.59868 | -56.94006 | 2025-10-11 05:23:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bca9d82c-e180-3279-bbc8-3b261150f1e0 | -12.14325 | -48.01405 | 2025-10-11 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe7d9ba3-5bd1-326e-b687-c79ec1b283e8 | -9.40785 | -66.76337 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16264522-5253-369b-a95f-b6f1e71723b0 | -9.93106 | -59.92202 | 2025-10-11 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 498a9f0f-66cc-3e3d-9ce1-87d3746af055 | -15.17823 | -56.74443 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bccc814-ad7d-3c7d-a904-f1d8eba9daa9 | -13.59465 | -56.93952 | 2025-10-11 05:23:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f9c0961c-35a5-3b0c-bbe1-1006761857cc | -15.27287 | -56.90739 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9c4350c-445b-3411-bc7e-0aa88ace07bb | -8.88641 | -66.86712 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad234473-98f7-3b5f-b361-ead06965e31c | -15.21362 | -56.86054 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df24f857-7353-3931-b6d6-53fa33383c0d | -15.86657 | -56.74187 | 2025-10-11 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4034c893-783a-3e5e-b749-5e94f7db5f31 | -15.15627 | -56.81577 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee5ef2c4-12f1-3f9f-bd20-43fd4b8c38ba | -9.41712 | -66.56326 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 434489e7-33f4-39cd-a459-dc660695aa8c | -15.19127 | -56.77438 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e38e5450-3bb2-3778-a894-f05f5853ebbb | -15.17556 | -56.73235 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 029018f0-29a2-3c19-b7cf-f02db2f145e4 | -8.88779 | -66.85909 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b4d1e41-9418-393b-be62-c20bf88452d9 | -15.18848 | -56.85958 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 550bd334-bbe9-3e0a-b3c3-9c2c72eafe92 | -15.20064 | -56.79957 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ace8490a-4d38-3e94-be48-5b614248c488 | -14.44309 | -50.34866 | 2025-10-11 05:23:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a22705d-887f-319b-a0e1-79d47e06a387 | -15.16407 | -56.72268 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8ba40e6-5751-38eb-b56a-13739513b201 | -15.73944 | -48.98043 | 2025-10-11 05:23:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dfafd00-f859-3e06-959d-367e47555be3 | -9.52457 | -66.76698 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d442bc1-2ccd-3018-8a74-c0cf52293f6c | -15.15579 | -56.81948 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d5002d6-d402-386d-b76b-d45310a7e4aa | -15.01532 | -56.02069 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8132f1a-6371-3e1f-be4a-c520f2516074 | -15.27243 | -56.91073 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a35f0e9-1486-31ce-8e0b-7df0fffc4c61 | -15.16248 | -56.7228 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fbc4038-8542-3104-bd6c-54771fa5baca | -15.16455 | -56.71901 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90d27e41-986b-3b33-a7d9-dfb6a366c8f0 | -10.55697 | -57.51672 | 2025-10-11 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a922c52b-74e9-33d7-9a86-f56ab4450c25 | -14.65446 | -56.21151 | 2025-10-11 05:23:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5585be7-037a-3b87-b4a1-28de1b72ab52 | -9.16781 | -68.17886 | 2025-10-11 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f7578d60-2723-34f4-baa8-df0d586dd845 | -15.18663 | -56.77745 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc7a903a-d0f9-3f2a-a17c-e96aa679a1b7 | -10.23958 | -59.12256 | 2025-10-11 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03743bfb-413b-3ba5-bfbb-5d95d4652d82 | -9.11978 | -67.75939 | 2025-10-11 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cffc374-c3a8-3248-bd70-61dcc26838e4 | -9.17245 | -68.17966 | 2025-10-11 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ba9fbf2c-7315-3311-91ba-780f6beab03e | -15.16298 | -56.71914 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README43.md)
