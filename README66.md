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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b71c083-5f17-306c-a366-150c996014d8 | -6.70072 | -62.84749 | 2024-10-12 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33f06f61-4e01-3b8d-a6a7-c72aa20eb5be | -6.70019 | -62.85052 | 2024-10-12 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 598137f4-1a2b-3cc8-af24-7570a3f20483 | -2.82265 | -40.35154 | 2024-10-12 04:57:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e400dc59-caaf-3c7d-a084-9417f40d10bd | -2.82174 | -40.35777 | 2024-10-12 04:57:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5ba2b032-4122-325a-a57a-2339f5bc6c01 | -5.93212 | -43.34238 | 2024-10-12 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2da55c6a-97e3-365d-917c-15345e4e1256 | -3.41952 | -43.3511 | 2024-10-12 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 723f8126-b83e-369d-8662-56f4870870dd | -4.53247 | -43.29389 | 2024-10-12 04:57:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 868ab313-54a1-3c15-bfa7-747424a66ac2 | -4.53188 | -43.29804 | 2024-10-12 04:57:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e15895ae-c161-3ede-bdbf-0fe98c86705b | -6.48677 | -43.87598 | 2024-10-12 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 957ff026-730b-319c-8469-30581bf1208b | -6.48622 | -43.88003 | 2024-10-12 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19b680aa-c685-30da-858a-6aea3543c9e9 | -6.28949 | -43.75731 | 2024-10-12 04:57:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 677cdc4c-f14b-33e9-95b1-abaffce5ec5d | -6.63744 | -43.86051 | 2024-10-12 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 948bc770-4a52-3125-86f8-63d8cffd4fad | -6.63698 | -43.85923 | 2024-10-12 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5b3de93f-dea7-3c51-92a6-2119311f69b5 | -6.63689 | -43.86469 | 2024-10-12 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0f9d4ab2-250a-323b-93a5-27c625955fb0 | -6.6364 | -43.86342 | 2024-10-12 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| da21d96f-66a8-39ed-a825-e5e9b379e98b | -8.13357 | -44.46082 | 2024-10-12 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ead40ff-9cf0-3d05-83b3-5328cadd1a6c | -1.99953 | -56.01933 | 2024-10-12 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2cb4582b-24dc-3f4a-bcd7-b30fd1525b17 | -1.8619 | -55.43789 | 2024-10-12 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78a5cf17-fb00-394c-9045-d6101eae1eb9 | -3.9307 | -42.41226 | 2024-10-12 04:57:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c4e0bc27-200e-3518-b35f-c6cf4a9e4d89 | -3.92595 | -42.40194 | 2024-10-12 04:57:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7b161d25-f86c-3887-9dc3-f3156bb3408f | -3.92526 | -42.40665 | 2024-10-12 04:57:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 8f17c35a-d7c5-32e3-99aa-90ff80a61fc3 | -3.92459 | -42.41132 | 2024-10-12 04:57:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 720c5735-b6dc-3735-a0b0-8f2744e46ffb | -3.92391 | -42.41601 | 2024-10-12 04:57:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| d121abd3-5f41-3cdc-84b3-e59f9a144e22 | -3.92323 | -42.42069 | 2024-10-12 04:57:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 4c343921-7239-34d6-88d2-abc95c160f02 | -9.26353 | -43.53687 | 2024-10-12 04:57:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f4e4236c-b0d5-3493-b817-46d86547fa49 | -9.26299 | -43.5412 | 2024-10-12 04:57:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 98c99058-1e03-31b8-9414-a37d932eb7e4 | -4.45579 | -44.57212 | 2024-10-12 04:57:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 290b72a8-af55-36e7-a6da-f9a594902e4a | -4.45531 | -44.57545 | 2024-10-12 04:57:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0ed3a6b2-e9bb-33b7-b570-913e0bed062d | -4.45044 | -44.57132 | 2024-10-12 04:57:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c7b0522e-7548-3fef-a04e-e1676beb87a5 | -4.44997 | -44.57462 | 2024-10-12 04:57:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2d0f15b7-b3f9-3a9d-9ead-305ccfd40c51 | -6.26435 | -44.66906 | 2024-10-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5095b6d-00db-310b-8799-b6aecba769cc | -6.1237 | -44.94905 | 2024-10-12 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1aa27a7b-f2c3-3741-8655-386370a2e3f9 | -6.12322 | -44.95246 | 2024-10-12 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a06826a-13b7-3656-b525-4d619fe86028 | -6.11885 | -44.94467 | 2024-10-12 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ab5a19e6-0a44-325a-9f77-ee13cfc36e88 | -6.11838 | -44.94806 | 2024-10-12 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7d2c083e-cef1-365d-92aa-7e2b63768d97 | -5.55733 | -44.69523 | 2024-10-12 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f003cc67-a9ca-359c-aa6a-a11b0780ef33 | -5.55519 | -44.69253 | 2024-10-12 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc253d72-f57d-3dd0-9abf-49c3968f2378 | -5.55469 | -44.69594 | 2024-10-12 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dc33c9a-2753-3ec8-a0a6-b69e2e1c6054 | -5.5542 | -44.69934 | 2024-10-12 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e907753f-6cbc-3e6f-82ba-02630b8f350a | -5.55239 | -44.69117 | 2024-10-12 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e92892c0-f995-3791-9672-f4f0d5d3f209 | -5.55192 | -44.69461 | 2024-10-12 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db13becb-911f-37e2-bc72-cce5e872a190 | -5.55145 | -44.69803 | 2024-10-12 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d3145ea-2573-3758-aff3-5df98d66557d | -5.54977 | -44.69194 | 2024-10-12 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7c93efe-1257-3a6a-8024-4a71b14c66fe | -5.54927 | -44.69538 | 2024-10-12 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfb9190f-2aba-3db3-bd7f-8d8691d2dad1 | -5.23328 | -44.76731 | 2024-10-12 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cacc947-857c-3fee-950f-31edfa2b4aae | -6.50355 | -44.15147 | 2024-10-12 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f1bc476-329d-315a-a1cd-6120be842d74 | -6.49788 | -44.15067 | 2024-10-12 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3545a7d9-e9d1-3c0c-a0b4-931ab70565a9 | -5.96968 | -44.12373 | 2024-10-12 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ee51f4e-8573-371b-a11f-2065a7d37c30 | -8.13304 | -44.4648 | 2024-10-12 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6898279a-2e42-37f8-8459-9447e80864b5 | -9.55618 | -44.46163 | 2024-10-12 04:57:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83fd9a30-3db5-3358-b082-93471ae7b73d | -9.55581 | -44.46024 | 2024-10-12 04:57:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b1ff2f4-5210-39d2-b198-65260eaee625 | -9.55088 | -44.45678 | 2024-10-12 04:57:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d420bc41-0d20-3a79-85f2-671729a0628b | -9.55054 | -44.45546 | 2024-10-12 04:57:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98f1275f-c8b6-3dac-a048-cbb5e2a9dab3 | -9.55002 | -44.45946 | 2024-10-12 04:57:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f05a2886-2aff-32bb-9f85-8f464b0dea34 | -3.58353 | -44.87788 | 2024-10-12 04:57:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1200222-2d77-3a5c-bd30-cf65b2b0951b | -4.9274 | -45.663 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c676b0b5-d3fe-35ac-b49f-1b89ffb6dbe0 | -4.85812 | -45.67967 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1aa957e-b3f2-371e-9d1f-56ee2d49e4a2 | -4.85771 | -45.68246 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cf9ff46-dcfc-3129-b5b5-d4d49da9036d | -4.8573 | -45.68524 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4004c039-5038-36da-bbf1-d34ac90c65f9 | -4.85313 | -45.67892 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bedde8d6-abfb-3a69-a187-fce68df6fcfe | -4.85272 | -45.68171 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 59b78aea-e8c8-3519-87fa-4abd4e6bb396 | -4.85231 | -45.68453 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| db5ef9e1-d957-360d-a314-f94c91b3424e | -4.59417 | -45.62943 | 2024-10-12 04:57:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d0d4132b-ee78-3bf0-b1e7-51289bc1e008 | -4.59375 | -45.63242 | 2024-10-12 04:57:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8dc4f2c9-c3b5-31eb-825b-f8220e029fae | -4.58918 | -45.62868 | 2024-10-12 04:57:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c08a8726-7901-3645-b414-a7d3f5a935c7 | -4.58876 | -45.63168 | 2024-10-12 04:57:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 989a59fd-5224-37cd-9335-33f27ec0edb7 | -4.46422 | -45.88996 | 2024-10-12 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5117f8e8-d85b-3195-b0b2-8dff04f696f6 | -6.35853 | -46.15093 | 2024-10-12 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b744e577-e396-37de-8068-8000d4ff7667 | -5.88238 | -46.37204 | 2024-10-12 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22a72240-1f64-3b4f-9d1c-d6af97a714c4 | -5.87755 | -46.37128 | 2024-10-12 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2df3a48b-7252-3b1a-8d3e-4141fffcc3ce | -5.84402 | -46.23275 | 2024-10-12 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3a5f616-b908-3d12-9ef2-9c859856c937 | -5.84322 | -46.23828 | 2024-10-12 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f3dbf3d-f52b-397a-aff5-b0c71039f7b0 | -5.77359 | -46.11457 | 2024-10-12 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb2ebfea-508a-30a5-8f2f-5cd131d353b7 | -5.6609 | -46.41658 | 2024-10-12 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 815a5036-5f25-3217-bd12-f597c8b3a55d | -5.65614 | -46.41553 | 2024-10-12 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17e0cbe9-8daa-3a79-a86c-80df64fe06e0 | -5.56629 | -46.28874 | 2024-10-12 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd2af60a-4166-3ef7-b275-5e9db5f805a1 | -5.45215 | -45.40222 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c202ab1-8c27-3f83-9f41-db95db6b5bd7 | -5.4517 | -45.40523 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4746573f-1ea7-3f42-8d75-70bd1ceaa6bc | -5.44953 | -45.40174 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbc65bdb-3315-3d49-a74b-7e96d77b417d | -5.44911 | -45.40479 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf07def6-feae-3153-afba-ba309eb34eb6 | -5.44701 | -45.40151 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8832a0b-aaab-3ebc-89be-d8e98a55e3a7 | -5.44656 | -45.40455 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a24ffbb-a76c-37cc-894b-ce2f57f73198 | -5.43608 | -45.79418 | 2024-10-12 04:57:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3f9c05b-6920-33b0-890e-1e5652ce261a | -5.39575 | -45.35651 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3d2002f9-9329-3ea3-b408-acc6c0828c85 | -5.39531 | -45.35962 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d2271c2c-3574-3f58-bfb8-961a84a4e308 | -5.3906 | -45.35579 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2bb1d702-101c-38af-a16f-3d1ea9d136a3 | -5.39017 | -45.35888 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9dfcb96e-5778-3784-842d-35080f7fa789 | -5.37448 | -45.20657 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39e6738f-ae63-3a05-9dc6-27f86aa3de07 | -5.3173 | -45.40971 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 603556b2-98f2-3efb-9ffa-b0551aa0f93e | -5.31687 | -45.41267 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| effe6815-ac2f-324a-94af-17d59beb7996 | -5.31643 | -45.41576 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65e14973-a4cb-3ba2-9dbc-6a2857564659 | -5.31218 | -45.40897 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b07e84d-9711-35fc-b543-79d751412cec | -5.31175 | -45.41192 | 2024-10-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 536dfa78-f157-358d-9114-4eeeda921bc6 | -5.24924 | -45.59519 | 2024-10-12 04:57:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfdda1e6-e530-334e-b94a-cd46d9292039 | -5.16492 | -46.15304 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f708ae3f-5f8b-3a73-8a8f-0fce0a993eca | -5.16415 | -46.15843 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cde4c9af-ffc4-3f77-8b9d-c65428e5b8d6 | -5.1118 | -46.18713 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64b99eb6-e654-3d13-a1ca-ca42f34d9d34 | -5.10695 | -46.18652 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3b53e60-d4d3-30e7-a33d-2a071b70bd55 | -5.08571 | -45.84799 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e59711ca-16f0-3580-8226-d6ddd9fe757c | -5.08424 | -45.84748 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README67.md)
