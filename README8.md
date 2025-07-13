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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4aa345f5-89c7-364b-b52b-d539b07c8b83 | -10.56818 | -49.11796 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b76b412e-8e37-3f89-a633-a0368ad34da9 | -13.11627 | -47.2934 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48ad577f-f0f8-39fe-92d6-6e687f036a87 | -11.825 | -47.51072 | 2025-07-13 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04c7be4f-8bd1-3e23-ab02-e4dc7a8ce1a3 | -15.6011 | -46.87432 | 2025-07-13 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4757a8f8-ecb3-33d1-8556-d7ee818eec9d | -9.57906 | -48.56209 | 2025-07-13 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fa580de-4ba3-3be5-81a5-14101a891e76 | -11.7597 | -47.84806 | 2025-07-13 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f036fe92-819c-35e7-b0ec-86a3ce259698 | -9.87456 | -45.3492 | 2025-07-13 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac8ece96-daf7-3e66-b608-5d430ecee8b4 | -13.19297 | -47.25928 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7088fde-610c-3f0e-aa0b-e55ff0f73fbc | -12.71458 | -45.02797 | 2025-07-13 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0a8f894-bfb0-33df-8561-aeb5259d582d | -8.93978 | -45.84466 | 2025-07-13 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c1dc9eb-d500-3007-bd97-bcb6a501c775 | -9.87511 | -45.34572 | 2025-07-13 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cd7247f-457b-342c-96ca-4cac947b4c48 | -12.15096 | -50.24254 | 2025-07-13 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70d66241-48f3-3744-84bd-44a90cead707 | -14.40827 | -49.63524 | 2025-07-13 04:21:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 654d23a3-1d46-38b0-b0de-4f4e6449a847 | -15.33989 | -49.75648 | 2025-07-13 04:21:00 | NOAA-21 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7bd30fd3-7292-3016-be26-fefc01baa959 | -12.75183 | -44.41452 | 2025-07-13 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd31a356-d2e2-3fef-9801-601f4caa6797 | -13.00956 | -46.26717 | 2025-07-13 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af9dd88b-d740-36fe-b55a-9c6e3b54ef61 | -14.85874 | -47.99416 | 2025-07-13 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f558fcd-7d05-3cf3-be70-b52f9145af61 | -12.44845 | -50.459 | 2025-07-13 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec5ce2e9-f860-3aac-8e13-394b3cf06bf6 | -13.14027 | -47.26864 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afe9c0c4-e351-36b7-a94d-c159175b7c30 | -12.71123 | -45.02742 | 2025-07-13 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0eaed224-0626-3e38-ab7e-65a64fe21acb | -13.14273 | -47.31705 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c48c009e-28f5-363d-8e3e-ed4ee12cb7d1 | -13.16221 | -47.30209 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 412699e9-a41d-3b73-950d-632f406e0e01 | -9.14181 | -47.11347 | 2025-07-13 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56ad0e62-230a-3aaf-be54-240171647f67 | -14.31587 | -52.74187 | 2025-07-13 04:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8eb6eb04-9375-376a-ac57-4bb6e00bdde0 | -8.88816 | -48.08435 | 2025-07-13 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a17965d5-15df-367a-a610-1cd7faeff9d6 | -11.73389 | -47.46516 | 2025-07-13 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f2e1a38-7f45-318e-ad23-e1ef8f0c7ad9 | -13.84242 | -45.9159 | 2025-07-13 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 892fb8da-2b9c-381d-be95-a1269a7dc5a3 | -13.88361 | -44.45947 | 2025-07-13 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c170df8b-58cd-31e5-b982-475d35dc463e | -11.83231 | -47.5082 | 2025-07-13 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f3153bf-88cb-3214-a724-e3a52048c86d | -9.53146 | -46.29873 | 2025-07-13 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dffc255-d130-3982-aac6-798238477bb6 | -11.86678 | -58.70805 | 2025-07-13 04:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dab08c03-873b-3313-b89f-76d74b4b1465 | -13.01805 | -47.82074 | 2025-07-13 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d92f419-9882-3f3d-8b70-cbd76e613117 | -13.88619 | -44.46343 | 2025-07-13 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f37b1d3c-9bfc-31e9-bd03-d9dc4eca3d20 | -12.71178 | -45.0238 | 2025-07-13 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4333a92-ab42-3222-9440-915d0fd8d7a2 | -8.92552 | -47.34086 | 2025-07-13 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8077257-6e07-38df-94aa-63ae9bf198a5 | -9.80033 | -48.56367 | 2025-07-13 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c733561e-ffa3-366b-b825-46eecdb6c965 | -11.65601 | -48.26971 | 2025-07-13 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18639d2d-c7ce-376c-8d69-962313deb24c | -13.88132 | -44.45125 | 2025-07-13 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3064824-a54c-3363-88c6-1b81d5794cef | -8.64144 | -47.68403 | 2025-07-13 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 111f633f-a351-3579-bc80-0801b4428e6b | -15.63726 | -48.54774 | 2025-07-13 04:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14d6151a-759b-3fdd-a87b-c1ecb8179116 | -13.84297 | -45.91234 | 2025-07-13 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6785aacf-9076-3833-80cc-c3445edb6acc | -10.5769 | -49.13261 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74856dcb-6022-3601-b5cc-108d26d80af4 | -11.73897 | -48.52669 | 2025-07-13 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e36b05f3-62b3-38ad-9478-5a28a2fe952c | -12.01754 | -49.52457 | 2025-07-13 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2d2debe-ce79-3bbe-8416-30b8daa24d8b | -10.68501 | -48.31099 | 2025-07-13 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e56d4eec-f63b-338f-a06d-b8a10a6d2be2 | -11.82895 | -47.50763 | 2025-07-13 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9be4cf5-fc32-3814-9126-d5f1be50bd39 | -13.84294 | -45.8904 | 2025-07-13 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f054d6a-c497-332e-9372-a91421749ea5 | -11.73483 | -48.53003 | 2025-07-13 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58670a97-1a75-3c35-a125-d48a26c5ebb2 | -12.01827 | -49.52029 | 2025-07-13 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ce68b19-28ad-3e77-a327-02433c94a7a3 | -13.83907 | -45.89344 | 2025-07-13 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 386ba105-aa7e-32fa-9bd3-ef0a8bca0cc4 | -11.72983 | -48.51707 | 2025-07-13 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae596238-4e42-3d8c-a172-c40652b406c2 | -12.42479 | -50.45974 | 2025-07-13 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e101d2d5-deff-308e-8c6a-7804b94f2dae | -13.10961 | -47.29233 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9f7a02f-2e12-3ce6-9ae8-ac4f3d5d8bd8 | -15.83621 | -48.13379 | 2025-07-13 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66fcaedb-41f4-3ac2-bb44-d50fdef79394 | -11.93817 | -45.7655 | 2025-07-13 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c7f72d4-e3c2-3587-b9de-48bbdce1794c | -10.68851 | -48.3115 | 2025-07-13 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed52c2a9-3720-3142-8a3a-9cc0e307c9ee | -9.79863 | -47.73995 | 2025-07-13 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fb730e9-e7b6-3e92-a4f1-7b09368cdb2b | -13.8391 | -45.91537 | 2025-07-13 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7b466ef-d2b5-3598-bc94-7086bfa02bc2 | -11.41692 | -46.42496 | 2025-07-13 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8421bfe6-9d4a-3c86-a443-abae14f8f381 | -12.99634 | -46.26502 | 2025-07-13 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37a2d14d-2332-3238-9039-019cb9548620 | -8.91346 | -47.35041 | 2025-07-13 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b88dbcd1-72da-3095-bcc1-590856962f9c | -13.02817 | -47.82229 | 2025-07-13 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8889e995-0db2-398e-bb23-3fae86bcd7a0 | -12.44763 | -50.46378 | 2025-07-13 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08f71f61-db92-32ca-b3ba-5a5289e5b7e0 | -10.5718 | -49.11858 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 81cea4f7-d200-3153-bea1-645adcfa0a13 | -13.02757 | -47.82605 | 2025-07-13 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3d01a27-7b78-3337-9b36-9d4d4d891ff1 | -10.64596 | -44.48549 | 2025-07-13 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fb6b886-b5c9-3901-96af-a9ca2081200a | -13.19629 | -47.25983 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bc14b6f-082d-3340-9995-dc7c59fc7e6b | -13.10904 | -47.2959 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41988328-138f-39a1-abc8-63271d895439 | -13.13824 | -47.3237 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8c5e93b-64b6-33c5-86df-1dc0c3823efd | -13.12072 | -47.28696 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e15d7814-b81f-373c-b205-5ecb6bafefb5 | -10.95829 | -54.37704 | 2025-07-13 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04434da9-f0c8-302f-8a89-781ef6bc4840 | -10.79674 | -49.63044 | 2025-07-13 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5cd38b9-666e-3132-b297-dfbd9d179816 | -10.65095 | -49.4295 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d07d97d5-9a0e-3c11-aa81-f8a18ee32558 | -10.09158 | -52.74019 | 2025-07-13 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9d169ff-84f2-3c0b-94c2-43a3fcc02664 | -13.12277 | -47.31366 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24390bcf-2fba-3882-b827-6e7f0c6bfa9d | -10.57544 | -49.11914 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ab86cf78-ccaa-3b08-a0ef-d766a1a67f6c | -22.90501 | -43.47913 | 2025-07-13 04:23:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| da561d9b-802d-3dbb-a464-57624278a1ff | -16.46482 | -52.54727 | 2025-07-13 04:23:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e22f4a5c-f1f8-314e-984b-000a565f7dff | -20.99781 | -51.79165 | 2025-07-13 04:23:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0a0dbe31-c1b6-3266-ab8e-0777b35d398d | -22.85653 | -42.98089 | 2025-07-13 04:23:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 26cf4028-8733-3921-a7a7-0f7d2a5c8d20 | -19.86902 | -54.39803 | 2025-07-13 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7096ad08-1fd7-3a3e-ab7a-125c51e27c92 | -19.08742 | -56.04157 | 2025-07-13 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 217cf78a-6e95-3094-8a31-bf9fe418c3e2 | -18.0943 | -45.48645 | 2025-07-13 04:23:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0844136f-a133-3018-a20d-b2b854229f6b | -22.64242 | -42.49562 | 2025-07-13 04:23:00 | NOAA-21 | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9400cf51-7422-315d-95ed-e0f6bd741684 | -18.45458 | -47.36954 | 2025-07-13 04:23:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a64f021-7db7-34e1-a73b-04256804110f | -19.094 | -56.04133 | 2025-07-13 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5943c77e-c3c9-3d35-8ef4-838fec5643de | -20.47933 | -53.67694 | 2025-07-13 04:23:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ff1c6f1-c70e-32bc-8013-758da3d13561 | -17.314 | -44.92882 | 2025-07-13 04:23:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6897d59b-17aa-3e2a-b931-0884986fbae5 | -22.90675 | -42.94711 | 2025-07-13 04:23:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8117d043-0c04-37c2-8c66-eff92706eec9 | -21.04708 | -50.04695 | 2025-07-13 04:23:00 | NOAA-21 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1d78abd2-4c6f-3bde-ad3d-976274d7c8b7 | -19.08627 | -56.04715 | 2025-07-13 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 33f18ab9-e0f2-3612-b81a-50689019bc07 | -16.67297 | -49.43316 | 2025-07-13 04:23:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c49c90e-2177-3604-a0d6-f1953144f0a2 | -19.08696 | -56.05146 | 2025-07-13 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 531aa798-0cd9-3511-94ae-57562f36947f | -17.65499 | -50.48304 | 2025-07-13 04:23:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b06f3d7a-1441-3c8f-8759-d36615ffbecc | -22.66233 | -43.29104 | 2025-07-13 04:23:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 596edd70-a5c9-3040-824b-57b7b1bfd949 | -17.77576 | -48.58234 | 2025-07-13 04:23:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 589f488e-63e5-3986-9119-65f487293557 | -19.89106 | -48.93197 | 2025-07-13 04:23:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 7ddcc791-c3bc-3b0c-bc28-456e5c49512b | -17.91208 | -54.1362 | 2025-07-13 04:23:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1954b32b-e266-3770-a8cb-cf03a389abdf | -19.08918 | -56.04026 | 2025-07-13 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| bc85a5a0-c735-32f5-b316-a7fbf86d2b9e | -19.09224 | -56.04263 | 2025-07-13 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |


[Clique aqui para ver as próximas entradas](README9.md)
