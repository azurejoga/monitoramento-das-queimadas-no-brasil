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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8045ad3f-0d40-31d1-8130-11c63d947ad3 | -16.98954 | -56.68951 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4ee3a431-b4d4-3656-ba17-bc17865a5dee | -16.98936 | -56.60416 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 99eab27b-9e29-3955-ab63-a4f16dbfe4ac | -16.98765 | -56.615 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 1d395805-32e2-3bbd-96c5-1ac14cf843bc | -16.98099 | -56.61386 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 77dabbe6-1e24-3e75-ad17-542d368dc339 | -16.98042 | -56.61748 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 582b1b2b-50fd-33d4-88b5-349ddc71643f | -16.97709 | -56.61691 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e06ebedf-8120-3459-a4d0-df6197d2f47c | -16.97652 | -56.62052 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0947d0ba-2e4a-3ec4-881d-4b7b3ae72b8b | -16.96499 | -56.13294 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 729e8329-2e0f-394d-8bbe-3055b740cefb | -16.96443 | -56.13656 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 749747ee-a9a2-31f2-b144-0a2248f92221 | -16.96387 | -56.14018 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a6c54227-dc72-3b5c-8ae5-ee73d953d0f2 | -16.96054 | -56.13962 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b055bc71-b5ab-3ba3-a00a-5da3fe6bedc1 | -16.93571 | -56.62502 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3801740f-8d0b-3919-939a-b6868ce584f6 | -16.89797 | -55.86863 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f9813270-36ae-3246-9119-3fff99908c63 | -16.89407 | -55.87171 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 37bcdb74-3016-31b3-99ee-76f5488c8a88 | -16.83231 | -55.85803 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d3bee188-f358-3e62-954d-85be0910cf5e | -16.82619 | -55.85329 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| feae6e03-727c-30b9-86eb-ab4db74aa380 | -20.26317 | -56.52909 | 2024-10-08 04:59:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 501a38f6-437b-3e76-bdd3-04fc0d129ee0 | -20.25982 | -56.52851 | 2024-10-08 04:59:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0399e9bb-02ee-33a5-b56b-a7aed412b29b | -19.65038 | -56.56363 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e84ae23f-e68f-341e-8abf-f5536e9b7dc8 | -19.64981 | -56.56731 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 23594515-83ed-3c82-b73c-6fee3b23d15f | -19.64704 | -56.56305 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 72bfb4ac-d78c-3f1a-9a67-014b1b28c351 | -20.2745 | -56.93395 | 2024-10-08 04:59:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85e28ccd-4560-3dc1-a3a9-ad55502c1b29 | -20.26595 | -56.53339 | 2024-10-08 04:59:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 35ddf374-7582-354d-be58-dc0580587f86 | -20.27321 | -56.53081 | 2024-10-08 04:59:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 22d722cf-9fe0-33d9-bde7-d4588bc57484 | -20.2693 | -56.53396 | 2024-10-08 04:59:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 11bb90a7-9d3d-3fb9-92e9-941ada036b6c | -20.23696 | -56.52077 | 2024-10-08 04:59:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5aa60e6c-cb2d-33fd-b41e-1970c4f79b34 | -20.07641 | -55.96355 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 16980a56-6a13-3b43-b98a-8748c5dd4ff8 | -20.07584 | -55.96735 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ce2852ec-7c27-34b9-9391-2e209c937afc | -20.07303 | -55.96299 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3763eb02-4b4c-3185-8388-3eb9f52179d0 | -20.07246 | -55.96677 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e48c6e9a-c630-3756-81c4-908e27192894 | -20.06965 | -55.96242 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0cca863a-6fbb-3e89-982b-b11cd06f64dc | -20.06908 | -55.96621 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| beb31e3f-7a14-32d5-b976-8743690c65a0 | -20.06628 | -55.96185 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c54d12e1-7c20-39c9-b471-fb66ebea5af4 | -20.0629 | -55.96128 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 971a8dc6-e865-38aa-8863-9bce54c38616 | -19.71195 | -56.48611 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3195666b-e1ed-37c2-969c-b2e04932d595 | -19.7086 | -56.48554 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 63b07464-e34a-3772-b4de-308240509c75 | -19.66804 | -56.44898 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 3f4a413e-4d01-3503-a402-55a4744a7e19 | -19.66462 | -56.4712 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4b3ebe7e-71fd-36ce-9040-a260a85091f2 | -19.66242 | -56.46322 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 8114172e-c119-32a4-9c9c-05aefd56fc3c | -19.66128 | -56.47062 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 54a408ae-8350-3b2b-91aa-b45ce1708df0 | -19.66071 | -56.47433 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 62e0d579-126e-356d-a705-fe45b0dc7ad0 | -19.65964 | -56.45895 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b3448081-967f-3909-af28-974b87e2a5b9 | -19.65907 | -56.46265 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c9b83304-ae9c-384b-86f4-0c9adcbda63e | -19.64393 | -56.49424 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8e19e2cb-2e9e-3c00-a8e2-64f5c4556733 | -19.64336 | -56.49794 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 009289c3-dc66-3df0-af61-c96ee1d47667 | -19.64058 | -56.49367 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2342f3e7-5cc2-3a81-a701-2a129cc0b73c | -19.59034 | -56.53059 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6f21d9af-3870-3c4a-9d26-72498d4c464b | -19.58977 | -56.53428 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9745bada-1588-3a1b-919f-e4df01298c7f | -19.58699 | -56.53001 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 26418125-f06a-39db-9179-e31e2b411ad7 | -19.58643 | -56.53371 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fb4fa27f-c807-373f-ad9a-1715d8b22546 | -19.58365 | -56.52944 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5a91ce3e-2f86-3d03-9ba0-277b18cc828e | -19.58031 | -56.52887 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 19eeff5f-25e9-3c02-a5b9-0993d0098527 | -19.57975 | -56.53256 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0fcfe09c-5655-3825-92ef-541111981716 | -19.57584 | -56.53569 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a9cac1dd-bad2-3272-b798-0974bbbc0ffa | -14.9076 | -57.2781 | 2024-10-08 04:59:00 | NPP-375D | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 252fbb7b-c776-3df7-b6ce-df3336b6947b | -14.31986 | -57.57569 | 2024-10-08 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89c772f2-8ca7-35d8-a4c4-01e3af213410 | -16.65999 | -57.08337 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 334fd0b4-7bf8-3a77-b2fd-aa5694063334 | -16.65941 | -57.08701 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 88dcccf1-318d-31e2-bf98-631f6eefd451 | -16.65242 | -57.13063 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e967f9ea-669c-35bb-b4b3-f791001b5735 | -16.65184 | -57.13427 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| fa78b577-6ea5-3565-b988-351ef986033f | -16.65126 | -57.13791 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 42f97d8a-e0ab-3e10-b3f3-71b08593baa5 | -16.6485 | -57.13369 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| f43f4e4f-5b34-31fa-a415-b35d53a45d52 | -16.64792 | -57.13733 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 7865e61f-1005-362a-8065-7e4c642fbb25 | -16.64299 | -57.12526 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 80f8870b-063b-358a-9a18-fe61b4aeca19 | -16.6363 | -57.1241 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0674c7b9-0205-36e1-9d90-aa2bd2ca54c2 | -16.63355 | -57.11988 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f348b0b2-b17f-3040-881d-1e9807abd96a | -16.63079 | -57.11567 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0140db09-7045-3ec4-90b8-48cf84a2cca6 | -16.63021 | -57.11931 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 57b56d31-2bbe-3bcd-a69e-cced48c92101 | -16.62745 | -57.11509 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 233519a0-7f21-33f1-990c-5f0b965dc9aa | -16.62687 | -57.11873 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 79a985e3-214d-3736-ac07-a27752baa2d7 | -16.62411 | -57.11451 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 289ad116-04fa-3758-b282-15dc69c90b8f | -16.60942 | -57.14187 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3575f0b6-2e99-37c5-8485-f8e64f6a328c | -16.60608 | -57.14129 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e6fecb47-2458-3e9e-be85-21b47be0df38 | -16.59096 | -57.14989 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d087d890-a74c-3c78-92ba-4ed8bbc45d73 | -16.59037 | -57.15353 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f60c84a0-51bc-3c96-a809-ea2e5afb4bd0 | -16.5715 | -57.14279 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 89e23dee-93a5-375e-98e0-fcaa3ad4485b | -16.57091 | -57.14642 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 459525ba-493f-323f-a90a-52b89c9d04b2 | -16.56757 | -57.14585 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 94e538e8-f5e0-33ec-98ca-3bec8ca65521 | -16.5411 | -57.41544 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 018a8c45-c9e6-3af9-89ab-82bf83ec2b14 | -16.48487 | -57.24448 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0f204e54-0594-3b0c-8e85-5d8a1e518402 | -16.48153 | -57.24389 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bd1061d7-3974-38db-8d00-3ac79fafdee4 | -16.47779 | -57.2883 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b8d1b80e-0ca9-3078-b4d6-5ab100601cd7 | -16.4707 | -57.26827 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 584262b5-cc01-3308-a28b-bd08723f3ada | -16.47011 | -57.27192 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1133e093-ba8f-30f0-934e-9d811db62d34 | -16.45097 | -57.3476 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d9204625-77a6-3189-91d5-c7d365793c70 | -16.44881 | -57.33968 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f0f5ca80-d716-3a77-aa84-bb4dec588d8b | -16.44821 | -57.34335 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c0807ada-da3f-3df3-8a61-93995a2327c3 | -16.44762 | -57.34701 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 83b7a8f4-cb9f-35e7-97a8-926809e52eb6 | -16.44545 | -57.3391 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 575fda8f-0da5-3d2e-8499-45a1dde1b4e1 | -16.44486 | -57.34277 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6695d26b-6cc9-3376-93d8-16eb4aac2e62 | -16.44426 | -57.34642 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 49fa8fb6-7990-3a63-93cb-597e43123a17 | -16.44367 | -57.35009 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a81372b4-01a6-334d-b7b6-864dc3f0d709 | -16.44176 | -57.25573 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 67622940-81ab-3e69-8b42-cbeacc321b7f | -16.44151 | -57.34218 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| aa8095fe-7cb7-3304-a7bb-d29c71dc1b5a | -16.44091 | -57.34584 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2f2c8b2a-72a4-3a98-971c-74b31366a68a | -16.43875 | -57.33794 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| dd4ae065-bad8-3809-b298-2c28fb1bbac1 | -16.43841 | -57.25515 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d62b2cd8-c785-3501-be63-f9cbdafdf8e4 | -16.43837 | -57.31905 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d357d572-2d40-3a27-a738-e8dd8402e8c1 | -16.43815 | -57.34159 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 49f7f84c-a95d-322b-b0e7-7ec39f0cd98b | -16.43782 | -57.2588 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README100.md)
