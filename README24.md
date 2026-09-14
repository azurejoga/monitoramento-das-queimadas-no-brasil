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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66aa939b-df96-360e-b649-5a875d65d9ca | -4.81075 | -42.88878 | 2026-09-14 04:32:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f744732-468c-319f-bb80-5faad1a6ed01 | -6.51082 | -47.59999 | 2026-09-14 04:32:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6944c22-d2b0-39e7-87e1-e443f2bfc98e | -4.38634 | -55.20889 | 2026-09-14 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3119ceaf-b08b-396d-aec7-e82ae0271eaa | -2.92401 | -50.44431 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7634b938-ef9a-3c63-b6d7-461817ebd29a | -6.7474 | -50.9247 | 2026-09-14 04:32:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d7266d0-1900-34b0-bf0a-75d8df5915ab | -5.12624 | -55.96599 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d9d43af-8a16-3780-ba84-666bac07e75d | -2.95635 | -50.39856 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe7d7bf2-4ea7-3460-8640-b0bab057d796 | -8.53474 | -54.71788 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c94ca77-1bca-3591-8632-35823f9ef33c | -9.44943 | -47.8574 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8bf5ffbc-18ed-337e-9396-6ab851604806 | -7.11749 | -41.78862 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4bee9c90-905a-36ae-a4b6-29ddf045b913 | -2.92449 | -50.4126 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| f0bd5766-0fde-3517-9444-00be7498612f | -6.77118 | -42.75053 | 2026-09-14 04:32:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a8f12146-884e-3562-ade1-239f4fab2ab1 | -3.85785 | -51.983 | 2026-09-14 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2741ee60-f258-3b8c-aeb1-7eb2a9616c8d | -2.91845 | -50.40585 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c9042523-fdb1-3b3a-863a-3710ac24a953 | -6.28472 | -55.27716 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ca5903c-97d3-3ae5-af02-9e94fc6ad31f | -2.89195 | -50.4435 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 555ac85b-a5ab-3432-9d93-65b06bb2be64 | -6.11172 | -57.68117 | 2026-09-14 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| dd0f6b9f-d3e3-3a46-9d67-830f71fc5266 | -4.09038 | -54.4345 | 2026-09-14 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb9a905b-d421-3e1f-bd27-9d22b7318c6a | -2.94523 | -50.41029 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 228caca7-5e65-3949-9390-a8f7c389ecb4 | -2.92815 | -50.43006 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 72091709-9869-3c88-8dae-535e5731465e | -8.50424 | -40.19751 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 511edd41-6a6c-333e-9de6-e8d66d44b6fa | -9.33195 | -44.37597 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b6ea396-5d31-3762-9c8d-650bb0c02046 | -6.28864 | -55.28028 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bac06301-66d3-34cb-b653-da0b8f5a2690 | -6.7706 | -42.75436 | 2026-09-14 04:32:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bc94c002-7f48-3ca9-81c1-79a929556fda | -6.58342 | -58.84737 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9ef92b4-1b53-33bb-afcb-19cb02152374 | -2.92308 | -50.42144 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 0627a5fb-7371-3e40-b78c-2caca573b097 | -2.93413 | -50.40969 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5186229f-8003-3952-8548-8cb46f293514 | -2.91911 | -50.38909 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 282e74f1-8f8e-3dc8-a586-0cb40c895e87 | -9.42007 | -50.14368 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43e6ef97-5424-3693-a97e-d88a83b3ec72 | -6.59062 | -58.84882 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66810c73-f072-3ded-b46d-8103850040d1 | -9.42836 | -50.11888 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| e5b62009-20d3-3a57-a42a-c02edc3d6e7c | -5.13334 | -55.96227 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0dea0d59-ca07-359e-83d8-0cdd09651a06 | -9.45375 | -40.38532 | 2026-09-14 04:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3fc9d831-50e8-354f-a865-715d731632f2 | -2.67159 | -57.56169 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 79f9273b-d8ed-35a8-a824-4b64867702ab | -2.93695 | -50.39204 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b0aa794d-b379-332e-8627-7d286711e4e5 | -2.89571 | -50.44871 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 253da571-773f-3139-8871-035e98101825 | -5.64935 | -49.07746 | 2026-09-14 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4ff14a5-a93d-3548-acaf-27dc72a57a98 | -2.90947 | -50.39206 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 07c564be-fded-3938-90b5-0da5956db6ed | -5.61597 | -45.24581 | 2026-09-14 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cca578bc-de6b-34b8-8109-f2bf2d2647b5 | -5.80569 | -53.79855 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 907918e1-94f8-3693-9dff-61ddf5f02889 | -9.39854 | -50.19795 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bff4efd8-e54b-31ad-96c4-3a5283e35c1b | -8.5367 | -54.70747 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fc19439-abcf-3b53-8d44-7b6339588bbe | -2.89626 | -50.41698 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 5faa9336-11e3-3097-b11b-bae5830d64aa | -6.25044 | -41.96124 | 2026-09-14 04:32:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 24f8af77-2af3-3f0b-a05c-f7b835f2642f | -3.38104 | -50.77266 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bd436bc-b8e2-3c2d-a287-f5428159ec8d | -4.1358 | -54.01008 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2c0b80b-51ce-3220-8db4-6c2b43d3a28e | -3.04693 | -51.26361 | 2026-09-14 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ccea585-95e7-3d97-9225-3657ae6ca445 | -7.01838 | -44.64177 | 2026-09-14 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b550aa72-25a5-3c7f-a1c9-08a50c5561f8 | -7.10794 | -42.09946 | 2026-09-14 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 28c4478a-4244-31f2-9c98-3830d4583ca0 | -4.57159 | -54.91085 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6f3ce05-03e9-3e39-9dd5-eaf54f832c5a | -6.57621 | -58.84604 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5858bf2c-165a-37ac-a75e-b8dd0ecb7f29 | -7.09961 | -42.10639 | 2026-09-14 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dfbbf20b-db14-3a79-ac05-c276e5531d04 | -8.37878 | -50.72267 | 2026-09-14 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce36b068-7208-38bf-abaf-d99629963be0 | -3.23446 | -50.58827 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b090546-face-3536-966c-c9d385a7419e | -2.61707 | -54.72947 | 2026-09-14 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91fafea3-0403-348d-812b-6d44a29fb078 | -7.02061 | -44.64925 | 2026-09-14 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf9e80f6-9816-369b-bad5-8bfa87bef06f | -7.01783 | -44.64525 | 2026-09-14 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b68d124-5272-31a7-b0db-dfca08c43088 | -6.30106 | -55.27858 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc7448e3-7f03-38f9-938d-c4990638f4b3 | -2.93037 | -50.40454 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30e85f53-3dca-3c57-9c5f-2a99bc9a4488 | -2.93709 | -50.43151 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bce9696d-3ee9-3926-9ba3-b60151b6d9a3 | -9.3308 | -44.36118 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e64a106e-53d3-310f-81d8-3dd7dc5e87e0 | -2.9259 | -50.41612 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1cd62e8a-7834-332b-804e-bf62554c6e56 | -2.9052 | -50.41846 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 189.2 |
| 3e5c11a6-ebf4-3d45-ab1c-e6cb6d980fd7 | -2.93036 | -50.41687 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7527deed-fce3-36fa-84b4-df35306f51e3 | -2.97065 | -49.55829 | 2026-09-14 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c30dacbf-40ca-352e-be4a-433ea6ba87f2 | -7.11195 | -41.80051 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 75ec7479-db86-3dc5-bf7c-81e3f33956ed | -8.40934 | -44.65456 | 2026-09-14 04:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 003f914a-a78e-3f46-bfd8-cb64dce643c6 | -3.23354 | -43.03603 | 2026-09-14 04:32:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e93baa3-00c9-398a-bcd4-ed302c9c6a06 | -2.95936 | -50.40803 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33f9abfc-3e83-32c4-a269-db519ae9dcfb | -6.28402 | -55.28117 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68317dba-21ec-3d86-8b66-0bbf9ac9ac33 | -7.11323 | -41.79225 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d2aca3f-cb54-35ce-89e6-a3eefcd948ba | -4.33966 | -54.78427 | 2026-09-14 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7788412-53cd-3544-96d5-fa5ab5eea85c | -3.60761 | -53.84656 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cf0ad71-064a-3a3a-a9d7-199610c529f1 | -9.39501 | -50.1709 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| d355d4a4-b11c-35d2-b317-f7fdca8e8bf4 | -2.91434 | -50.44724 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| c17e042e-c473-37a4-ab03-165dbaae3615 | -3.79436 | -44.10671 | 2026-09-14 04:32:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81742fb7-3e1e-3214-99e5-de1e9e84537d | -8.53605 | -54.71093 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 916e5270-5a6a-3d1a-bac6-e9fb324fe775 | -9.39897 | -50.1716 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| a7db693b-8b98-38ce-93e2-983af6253d34 | -2.93184 | -50.40805 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41d59789-c463-39b5-bd06-8450385425d1 | -2.91098 | -50.47742 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d0e31dd-688c-3c46-a0b6-46e37d51c999 | -7.55314 | -41.83892 | 2026-09-14 04:32:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dedd26be-2c2d-32f0-8da7-e140523f5b08 | -6.30181 | -55.27443 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9ce8742-f5ef-3cdc-9ebc-a04d98c3a732 | -2.94743 | -50.39708 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ec5431d-094b-379c-a3de-c4bbf11aebad | -8.75123 | -46.42352 | 2026-09-14 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd2dcb85-f8b7-3192-ba66-c60080471e47 | -3.86041 | -51.97948 | 2026-09-14 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fc5c5dea-77c5-3493-b6b9-c2cd27983572 | -9.44683 | -47.87312 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 824819cf-b078-3092-8744-88ec87c826c6 | -2.91848 | -50.4602 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d191ebe2-812e-3952-9623-42e4183601ae | -9.90185 | -47.61315 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c01e516-dd1e-3d22-8d59-28f13e872307 | -5.11497 | -41.07825 | 2026-09-14 04:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f31f75ff-e33f-3eba-966e-22cb075ebd88 | -8.61659 | -44.4387 | 2026-09-14 04:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f212ec3-4812-3949-9329-da53b00481f9 | -6.28352 | -55.27519 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08fd70e7-df75-3565-bb66-f4426efea9fe | -2.90216 | -50.40892 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 3e9b9592-5819-38f9-8114-52a1d798139a | -3.39162 | -50.76499 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a018e32-e541-3d91-9579-f62ab6b5acbb | -2.92966 | -50.44846 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb0b954d-b005-371e-b6cc-c891f8d12884 | -7.09557 | -41.81085 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 030575a0-ded4-3303-9afb-0a9a74f00bf1 | -3.593 | -43.04472 | 2026-09-14 04:32:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3bec2a0-5047-3fe6-91e8-e07759d16948 | -8.34017 | -44.75516 | 2026-09-14 04:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 408b1c4a-ac27-3581-80c0-5165e20eb7bb | -9.13335 | -51.57257 | 2026-09-14 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f0e9023-8370-32bd-a259-790797f5a2ee | -4.45619 | -50.15903 | 2026-09-14 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19572c8d-af6f-347b-a1be-66a890acafeb | -9.4069 | -50.173 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README25.md)
