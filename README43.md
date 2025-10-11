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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 799097e8-aa25-3a81-ae8f-346ee5604332 | -5.25557 | -50.90801 | 2025-10-11 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 005abebc-8760-3072-8535-b7683f15ddb6 | -16.75735 | -56.29262 | 2025-10-11 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 6b96143f-9551-3eee-85c6-96f15f826da9 | -8.87117 | -66.77787 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4ff7f07-0004-3091-b695-369443b67569 | -15.16621 | -56.83669 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b6971c8-4d94-3cd3-bc71-b87f345473ab | -15.43791 | -55.97357 | 2025-10-11 05:23:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bfb736f-97da-373d-ac91-057cc68f536b | -9.81364 | -63.18328 | 2025-10-11 05:23:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cbc53867-6e2e-3eef-8adc-8877cc5e2983 | -15.16258 | -56.8322 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c40c4b78-ef36-3c47-9d56-d09c032b335a | -9.69214 | -48.93756 | 2025-10-11 05:23:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15f26c4f-12e5-3013-a596-e54c6e5eae95 | -8.73516 | -67.19835 | 2025-10-11 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 213250e9-1bb0-35d0-967c-bea13e75fb9c | -15.15894 | -56.82773 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8ec2483-4db6-378d-bf7d-38668e15a343 | -8.73592 | -67.19411 | 2025-10-11 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 01612c9f-ab91-384f-8234-bec61b06a44f | -9.40852 | -66.75953 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00628d34-3b91-31ff-8694-679713d7af17 | -9.17622 | -68.18535 | 2025-10-11 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b1dc3565-af53-34ac-8460-365d5a9a5f99 | -15.01588 | -56.01646 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11f3a4c1-4c4c-3728-9332-b3123b1ce9b5 | -15.69597 | -48.40206 | 2025-10-11 05:23:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2ab6de6-0ebc-3bc2-b3fe-ffde1181fc27 | -8.41929 | -70.11844 | 2025-10-11 05:23:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ddc0c07-3422-307b-90f3-d550a362914b | -8.87048 | -66.78185 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ab1a72e-3794-3ac7-8749-c80416de76fd | -8.52924 | -67.02608 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45f27e1b-a2a4-3d73-a4e1-f2efdd559785 | -15.74007 | -48.97418 | 2025-10-11 05:23:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cc6dcfc-3064-36a1-93e6-fb7e410ebcf0 | -8.89067 | -66.86787 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1373df5d-e91c-3c71-b0a5-b8badf4b32b1 | -15.18929 | -56.7894 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebeb345b-2ae1-3f45-848a-d433fbed03d6 | -5.25019 | -50.90731 | 2025-10-11 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1658c055-afd2-3f59-b8bf-2cf8cdcdf83c | -15.18897 | -56.85588 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fc5e62c-6c18-36a4-bbc9-9fc6d3ca0410 | -15.20491 | -56.86265 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58cb837c-6b88-362b-8214-045fc9ee7c1f | -9.40434 | -66.75875 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b0e270c-ba1d-352b-8941-ee0277a35318 | -15.21659 | -56.74307 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0b2a3e1-2dd3-3027-adea-c7d3901f7c45 | -15.01323 | -56.07006 | 2025-10-11 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ef8b6252-6e2c-3109-9055-1791a81f738e | -15.16821 | -56.7235 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a877800-bc4c-3e45-864d-4cdabba2d346 | -8.42051 | -70.11165 | 2025-10-11 05:23:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7936c8eb-2403-3deb-a4c1-2827e202a054 | -15.20902 | -56.86341 | 2025-10-11 05:23:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e29cdf7e-e2a9-3e59-9628-c3acf35864b1 | -15.86237 | -56.74129 | 2025-10-11 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a70fac5-2414-3f39-a421-dc2aae1df667 | -9.6915 | -48.94277 | 2025-10-11 05:23:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a7234058-2d36-3c25-ade5-430c79e24706 | -15.15943 | -56.82401 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9d27ce2-8f9b-33ca-8073-48d8caa457ab | -9.54658 | -66.46944 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a521363c-fb57-3e20-8a5c-194398418904 | -15.19651 | -56.79883 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e59fc54-b327-3735-ba91-dc6d65a57e01 | -15.2041 | -56.74126 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 143dc6b2-9a16-3167-b2a7-6e793dc473d1 | -8.8871 | -66.8631 | 2025-10-11 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdb078b4-1695-3d96-b7aa-d82b2e4d3305 | -15.1719 | -56.72786 | 2025-10-11 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8486a642-438d-35b6-a5e6-8ddc446d6b49 | -8.7219 | -69.87708 | 2025-10-11 05:23:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 369aa82f-6a1b-36d5-bc16-ecea456b1a36 | -13.48286 | -48.10891 | 2025-10-11 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65e93276-fde6-3ff2-9dc3-6480e7be09af | -10.07681 | -68.47252 | 2025-10-11 05:25:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 549c92d2-6806-34fc-ac4d-2879afc30e19 | -9.74447 | -67.22012 | 2025-10-11 05:25:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de136b95-12d0-3906-9070-25b31d9bdd51 | -9.27716 | -68.7802 | 2025-10-11 05:25:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc6d210b-6573-33b8-a856-d071d3bc7f35 | -13.25388 | -48.02189 | 2025-10-11 05:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0d3a5f26-bd3b-3f20-9b7f-426cb7dfeb30 | -11.50426 | -62.41744 | 2025-10-11 05:25:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca740e5e-439c-3a8d-a1ed-ac4f0a4592b6 | -17.90692 | -57.49675 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cd906f75-5eeb-3248-a7b5-851bbd2b4a4d | -17.82351 | -57.63052 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2d839801-7b87-3510-a730-fef9fba5d527 | -10.58002 | -69.06465 | 2025-10-11 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c91be1e9-e4aa-36f1-9345-ccc4d3caae23 | -18.04765 | -57.56306 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c888e69e-3456-3c23-ae99-dc31444f22df | -17.84288 | -57.57861 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 46d3d5aa-2897-37b7-bede-b1c40efc25b3 | -17.82763 | -57.66201 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7605fa8c-7b5f-3e61-867f-28e4c308b16e | -17.84645 | -57.58314 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9d79170d-cc4f-344a-9ea8-06276abdf19d | -22.54704 | -52.04997 | 2025-10-11 05:25:00 | NOAA-20 | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2a83e748-0a20-3467-bec7-82279feb57a0 | -9.55568 | -66.7365 | 2025-10-11 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ffda82f-2114-338c-9c17-7f16daeaa7f0 | -10.59149 | -67.74877 | 2025-10-11 05:25:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24057b9e-ddf7-3fb1-b5ea-c96179cd1710 | -10.57425 | -69.07214 | 2025-10-11 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d4d4ceb-9f05-3b89-a9fa-3a8f0c3bf72e | -12.24219 | -51.14472 | 2025-10-11 05:25:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d41a1f93-d56e-3796-83f0-8b250e47c1a0 | -17.83535 | -57.66635 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d6ab399c-9e89-3027-82f4-474b5c3accc9 | -12.23784 | -51.13144 | 2025-10-11 05:25:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46f5a707-285d-3602-8127-52e7ef9e8dad | -17.84089 | -57.58873 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ae6a74e7-779e-378a-9181-c65938001e23 | -18.05591 | -57.56392 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 830f9746-9e9c-356d-a727-f082c86a20e6 | -17.83583 | -57.66271 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 35d17610-2212-3a07-8b9c-60f6d8978dbc | -12.08858 | -63.86008 | 2025-10-11 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afcd64f2-4d2e-3ddf-8728-f0be11530469 | -18.04845 | -57.55695 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b4826566-79c3-3bcd-aac4-3874db8e9f16 | -13.33755 | -48.48638 | 2025-10-11 05:25:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ecc3e2fd-7982-36dd-9283-a0945d582a08 | -12.39771 | -63.87949 | 2025-10-11 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3599e048-ab2e-3f1d-b753-fac577aa33dc | -12.09203 | -63.86066 | 2025-10-11 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf4b67d9-9fca-32bd-bcc2-32e694037b8e | -12.09865 | -64.23838 | 2025-10-11 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9dcea08-3597-3791-a5c7-a76a5f6395c2 | -12.09548 | -63.86124 | 2025-10-11 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89181929-b661-3237-81d4-d48bbd069fe0 | -13.33807 | -48.48114 | 2025-10-11 05:25:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fdddb12a-827e-3d67-8aec-e37010dcc456 | -10.87851 | -68.42203 | 2025-10-11 05:25:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf730fbb-5c68-34c5-b058-d4d58b613987 | -10.02593 | -68.86163 | 2025-10-11 05:25:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cbfef1c-0969-3831-b61a-61e2d833948c | -9.49562 | -67.13593 | 2025-10-11 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 589a5e3b-68e5-323c-97d6-f2168d85e97b | -9.56204 | -66.74955 | 2025-10-11 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d03de30-8f6a-3399-988c-94fadd6bca12 | -13.48988 | -48.11037 | 2025-10-11 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6067bde6-d750-3ba2-a5cc-59fdf70cbad4 | -12.09165 | -64.23717 | 2025-10-11 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0610de0-c541-3050-a993-bc68a64bda56 | -17.83676 | -57.6545 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 741fa9f2-792d-3e9c-bea9-043c844c4dec | -17.84135 | -57.5901 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 971e4ad1-f496-3f1a-bc61-bc3aa28c9939 | -17.82716 | -57.66553 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f4a57d7b-303e-3fee-bc75-73a4e1125075 | -10.16823 | -64.734 | 2025-10-11 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1232658-decc-3b45-bbfb-3f72b44e0dd1 | -17.81528 | -57.66132 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e092fdf6-7d31-38a2-89cd-055410e5c4d2 | -17.84495 | -57.65533 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 989537fc-9989-37f8-b79d-de3796d65032 | -13.53536 | -48.12557 | 2025-10-11 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c275b51b-a4c8-357e-abac-a4471c623023 | -9.95522 | -64.86387 | 2025-10-11 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fb77604-9b22-3e73-88e1-f33953654e2f | -10.5913 | -67.74993 | 2025-10-11 05:25:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d033ea7-bac2-3457-8d5b-91a04d012da4 | -17.83132 | -57.66477 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4d72723e-46c2-3f14-aec8-b612137f73a5 | -17.89652 | -57.67369 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| de5ad40a-fdc1-313a-9bbd-6d17816e2384 | -9.95303 | -64.85433 | 2025-10-11 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16d1576f-9277-364d-b3c5-c5c856960ac8 | -12.23625 | -51.14458 | 2025-10-11 05:25:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0efc9bfe-f3f3-3da1-8a9a-33773112aa01 | -17.84858 | -57.65941 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bc83ddc3-5fba-327c-831d-63edc87178b1 | -18.07137 | -57.53161 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 83dbe506-674d-3806-bfdf-41a5bed2eca4 | -17.897 | -57.66996 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 565368b7-7f97-3e9d-bff1-184e04f636f0 | -12.23677 | -51.1404 | 2025-10-11 05:25:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1ea90546-1762-3423-a2fb-5f297a56f9d9 | -13.26227 | -48.0105 | 2025-10-11 05:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1840707c-7bc8-3c8a-9404-ec78c21642b5 | -13.5313 | -48.12558 | 2025-10-11 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e7c27e3a-6f73-33ff-9636-448a1d394917 | -10.69823 | -68.55661 | 2025-10-11 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5f1e66b-83fe-32d9-85fc-6268e53f6d6e | -13.33785 | -48.48515 | 2025-10-11 05:25:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6a0808df-0850-3466-b66f-d5fbca299364 | -10.5752 | -69.0668 | 2025-10-11 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 934a9fc5-f525-3d21-b51c-068087f4c9dd | -13.48348 | -48.10301 | 2025-10-11 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 05f2753c-489a-37b3-a0cf-74e7eac54528 | -12.23735 | -51.13562 | 2025-10-11 05:25:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README44.md)
