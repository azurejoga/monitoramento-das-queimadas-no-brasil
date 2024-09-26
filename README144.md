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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d789137-33c1-32fa-9916-adcc859bd134 | -17.84444 | -53.70191 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4453a52b-4a2b-3500-8d44-a9ce790abc4c | -17.84207 | -53.69289 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 67acaa78-377c-348d-8f60-4ee8e8f856ec | -17.09785 | -52.14635 | 2024-09-26 05:01:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e3acc3b-9980-3e91-b60a-1022bd84de29 | -17.59612 | -52.97223 | 2024-09-26 05:01:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 873bdeca-74f6-3060-843e-86fd63203e67 | -17.5721 | -52.9546 | 2024-09-26 05:01:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e82f046-04e6-397e-acad-9591dee0f4d4 | -17.92081 | -53.66882 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e01bf0f-56d1-391e-afdf-abcf64c8f976 | -17.92021 | -53.67304 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02262cff-5f8f-304c-bf31-dfd79e28eb9a | -17.91962 | -53.67725 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c6c6f29-9b68-39fc-90c7-461dae4c2562 | -17.91722 | -53.66822 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fee1cdb-16b5-3fb3-a425-77ee9977cbe5 | -17.91663 | -53.67247 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a9df0cd-7db7-3e13-b618-acedf5a21a85 | -17.91544 | -53.68089 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15454b73-0205-3ddb-9696-456af293ce50 | -17.91485 | -53.68509 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1eaf8760-709c-3a4a-8491-5123bcc64135 | -17.91305 | -53.67187 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee03dcae-d334-368d-9b87-67078edb6ad1 | -17.91007 | -53.66699 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f93a491-9742-3e89-b952-63e3a0847c5f | -17.90888 | -53.67548 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba91dd5c-1608-3007-8030-4e9de14de8fb | -21.38277 | -54.60051 | 2024-09-26 05:01:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 85134ef4-c10f-3f69-b0b1-71d15e2889a4 | -19.12667 | -57.47625 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a4b30e18-fb80-33c3-bf26-85967b47caf4 | -19.12337 | -57.47567 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0d07f27a-378e-39df-b6f8-6d11ab3acf0d | -19.12207 | -57.50521 | 2024-09-26 05:01:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 17ef4693-79da-349d-b551-fc98a1842ba8 | -19.11949 | -57.47871 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 226e4bcd-1c3a-302a-b96b-a8feac445ee9 | -19.11876 | -57.50464 | 2024-09-26 05:01:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ba26d929-4795-3aae-8b1c-35556d4c666a | -16.62147 | -54.0933 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83b478ea-f5f2-3b60-808c-9ccbd2de498d | -16.6105 | -54.09541 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff64587a-22c5-347b-939a-70f657be27dc | -16.60703 | -54.09485 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 690757dc-2027-35af-b46a-71ebb89cd0e2 | -16.60646 | -54.09883 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e8604af-359c-304c-a8fd-2b3caccd3ec4 | -16.60242 | -54.10228 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 285df99f-fa95-39c4-898c-94f3570ca67f | -16.60196 | -54.09145 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96459767-38ed-3026-a240-eed95d9e7a91 | -16.6002 | -54.10339 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6aad9eac-4518-3cee-bd03-ad6f77504882 | -16.59894 | -54.10179 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 676b9247-30ea-3843-bbcf-854dda465031 | -16.59672 | -54.1029 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56a47b1b-1c58-31da-93ba-ad5229638aea | -16.59325 | -54.10233 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fcfc71f-5fdb-3cdf-beb2-cac549fdaa45 | -16.58517 | -54.03609 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 715db6ba-0ff0-3a8c-87b3-69672d799f74 | -16.58458 | -54.04012 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85d849b7-713f-32ed-b9f9-47dd067352d8 | -16.62318 | -54.08133 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2879a9cd-b99b-3daf-b1bc-c44ac3a65290 | -16.62261 | -54.08531 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcbae73d-83a7-3376-9c3b-8a73afbf6fae | -16.61971 | -54.08077 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63b54ccd-1b59-35fc-8a15-3bce56fe8b86 | -16.618 | -54.09269 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf39571c-e0d2-381e-9b7d-b3c77f879370 | -16.61453 | -54.09208 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe513f6e-9043-3d53-af7e-e6626e63ff49 | -16.60299 | -54.09829 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8eb5f0b9-7d6d-3d39-84b0-5ba092eec339 | -16.60137 | -54.09544 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72216e00-008b-369a-bd99-c9ad170c82b0 | -16.60078 | -54.09942 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6991fbc9-80d2-3966-9626-e5633eb377ed | -16.60007 | -54.09383 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58d97eb4-682c-3cea-9952-60aaf6b7d13f | -16.59951 | -54.09781 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83ed2965-60ff-32ea-82d1-c470c77525dc | -16.59267 | -54.10628 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7aa3b13-d22f-3366-8ee7-9e6d557792ef | -16.58979 | -54.10173 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8575f928-3393-3706-a8f9-7b07dad169fa | -16.58866 | -54.0366 | 2024-09-26 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d99bf5a-0f4c-3adb-a976-7d4e3964ffa5 | -20.76431 | -54.83989 | 2024-09-26 05:01:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11737977-773e-3a81-a89e-7fb2474bfdca | -20.08182 | -55.55296 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4f536bd0-b185-3269-a836-273f272bbf8c | -20.07814 | -55.52591 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 74906e12-8917-32a0-a534-4ca2897b7b35 | -20.07644 | -55.53743 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 140b28b7-7635-355d-8839-fc395aa34790 | -20.07587 | -55.54127 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03430909-a61c-3ae3-9a4c-60f039c3db18 | -20.07474 | -55.52536 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ab307f6-dd3a-3abb-aadd-b1b1fb784f70 | -20.07133 | -55.52483 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48c56a48-e636-3fd7-a2dd-b4f472333c64 | -20.00782 | -55.48278 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5e318e0f-2ca4-30a0-b03f-10f533ed99f7 | -20.00726 | -55.48668 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9aeef3e4-9c24-3635-9acf-767c07813f25 | -19.99704 | -55.48509 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e608af8f-73c2-39dc-83b2-366127ababfc | -19.99028 | -55.50767 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bf39fb88-c42c-3d8a-b9cf-08ec532eae3d | -19.98744 | -55.50326 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 750ae64b-42fd-31b8-afe8-f62bd5e70363 | -19.98689 | -55.50702 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 78803583-6df7-338a-a7bb-f23ddef691fb | -19.98633 | -55.51081 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c024b3c2-3518-33a7-a1c1-1fd991d9080e | -19.98578 | -55.51463 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbdbc9c7-4f20-3789-a942-77a68394c168 | -19.98522 | -55.51846 | 2024-09-26 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62c42a3a-e1a4-3470-a614-a655f6992c21 | -21.94196 | -56.19507 | 2024-09-26 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9b7bc6b-0353-313e-8652-84ab9579955b | -21.66836 | -56.02798 | 2024-09-26 05:01:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b57b788d-79ba-3e53-ac64-6aaa9ac13834 | -21.39865 | -54.66329 | 2024-09-26 05:01:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe1ef7a5-f806-3ed7-bd80-808f1d214edd | -21.39807 | -54.66758 | 2024-09-26 05:01:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1087e439-9f18-30d0-848f-f9ef88e0174a | -21.39568 | -54.66411 | 2024-09-26 05:01:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b7491a70-7e56-3835-9fb4-895974578b36 | -21.3951 | -54.66272 | 2024-09-26 05:01:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ac5d324-9616-38f6-a018-11e3aab9dadd | -21.35066 | -54.62204 | 2024-09-26 05:01:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8bad265d-1c03-3ec9-9508-cdc01bc82a40 | -21.34593 | -54.65625 | 2024-09-26 05:01:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5141a626-c3a0-375e-a408-bf6f244e7605 | -19.11618 | -57.47812 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5403bbc4-b0d7-30c0-8eb8-7963fbedf31e | -19.11561 | -57.48172 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 601b6105-6da8-312e-9e3d-064df4c1b296 | -19.11058 | -57.49194 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 615c5bd0-157f-3a4d-891e-6cbd0089d796 | -19.11546 | -57.50407 | 2024-09-26 05:01:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3dd3789b-3532-3b2e-bad3-10f391da60ff | -16.58987 | -56.01613 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e7688119-3eef-3b2c-b8c8-ae407b5405b2 | -16.58656 | -56.01558 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5a5d80c5-dc00-3ec5-ab42-2dcd1014ad66 | -16.58492 | -56.00424 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| ce29aa83-38c8-345d-8733-481bdfaa5d4f | -16.58325 | -56.01503 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 98b7f36a-f1cd-3a32-b360-1c96864821a2 | -16.58216 | -56.00009 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| cbdb3337-c063-317f-9446-f140b8534ff4 | -16.58158 | -56.02582 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 666c056c-63da-31d6-8925-656a3eade7b4 | -16.57884 | -55.99954 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6534c7ad-641e-3c97-86ee-76e27772e19f | -16.57882 | -56.02167 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 94231a74-004b-35f0-b74d-8509fb3b9f52 | -16.57829 | -56.00314 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3e5c8251-e8c7-3338-824f-8077be66c5dd | -16.57663 | -56.01393 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8945056b-f0f5-3c77-af31-68ffcb307dca | -16.57498 | -56.00259 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 60ff6d31-79b0-331d-93d0-f2be86ddb519 | -16.57276 | -56.01698 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e51b096a-9757-374f-a3ae-534bfb0dae3a | -16.57 | -56.01283 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ff5c1515-77e5-3cd2-8999-65e1168dd199 | -16.56614 | -56.01588 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 016a4a65-85bb-3620-9efe-ca4d332d0233 | -16.56558 | -56.01947 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a29e695f-8841-3a88-8e77-a4d63d997cfa | -16.56227 | -56.01892 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e066d5f5-f136-34f5-b48a-d646154c34bd | -16.56172 | -56.02251 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e4d7df65-d485-3ecd-90c5-2dbccd0a1b11 | -16.55619 | -56.03634 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 04ab2031-f0d8-32d2-bc83-04f24b13049d | -16.55508 | -56.04354 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1710f128-6613-3b98-bca2-dfe0dea880ed | -16.55452 | -56.04713 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 767477f9-0afa-3422-ab81-acf0d2f794d2 | -16.58711 | -56.01199 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 28796f0f-17a2-3646-9f61-af4c37cc8626 | -16.586 | -56.01918 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 19fe00fd-2947-34ba-ba29-13cf082bf585 | -16.58547 | -56.00064 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| a21ee0d1-ca91-3250-a4e0-4a215f72807e | -16.58436 | -56.00784 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cf06dc8f-117d-3d21-8999-e7bebaf01256 | -16.5838 | -56.01143 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 86ff5145-af4a-31a0-bdb5-dbf7a1856348 | -16.58269 | -56.01863 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README145.md)
