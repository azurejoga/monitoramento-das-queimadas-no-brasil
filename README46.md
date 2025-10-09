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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| feb27e5b-aea0-3716-8854-2ac1d49b93eb | -18.54573 | -45.06227 | 2025-10-09 04:21:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dba2760e-96e2-3375-8191-c5ab23184260 | -14.53189 | -48.70364 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7413490-c70d-313b-ac84-96c455aed5da | -17.26545 | -46.96752 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4a5c7705-8c98-3cef-bc80-32389f59f789 | -15.75075 | -48.72322 | 2025-10-09 04:21:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 434318da-a9cf-3149-8ae3-13ef3c54174b | -16.59812 | -46.54573 | 2025-10-09 04:21:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4c9f51f-d894-3216-90bc-ac9544cb37ba | -17.63512 | -47.20726 | 2025-10-09 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cd5b7389-5dcd-318f-9b0d-48d346364dd0 | -16.71543 | -47.60638 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 94721b38-b595-30fc-8cb2-d611c1d61517 | -17.49389 | -45.30167 | 2025-10-09 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd559d99-dbbf-33c0-ac72-ca1ae0aec372 | -17.26125 | -46.90763 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d1f999b-b054-386d-bf93-78dcd77223a0 | -15.74707 | -43.67399 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96f336d3-7ae9-37ee-bcc2-2e46f04631fd | -15.39321 | -47.31088 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00b8f764-5075-3d6a-bb8a-b70aec0dbdc7 | -19.44567 | -45.55419 | 2025-10-09 04:21:00 | NOAA-20 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e77d3f15-1646-33d7-a301-5dff6a7be3f3 | -17.64996 | -44.44072 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ff97884-6756-34e7-a64a-c9714e04dcab | -17.26489 | -46.97112 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 337f6577-af3b-34e3-a201-658c31b480a8 | -17.37831 | -46.898 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38eab53d-3ba4-36f5-acc3-75c76cb1d96e | -18.0407 | -44.98296 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea67acdb-d017-3ccf-9abb-dcb3fd6e33a1 | -18.09056 | -44.46095 | 2025-10-09 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd69d12e-e60e-3849-8adb-ca4f2bb38073 | -17.2275 | -46.92776 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3305b3df-ec2e-3a4a-8cc4-446c8fc944b0 | -15.06892 | -46.6183 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06ecf518-0248-332c-9a0e-937a5c8e0b03 | -17.63182 | -47.20668 | 2025-10-09 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 223f073e-d513-3b27-a664-4ce84f3540b3 | -15.47173 | -47.96403 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f22bef24-7907-3fcc-a485-b1b5981c3ef1 | -14.45684 | -52.90081 | 2025-10-09 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c560d05a-3bc6-39bd-ba57-905c450f0c6c | -15.58222 | -43.91744 | 2025-10-09 04:21:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e39c7238-d141-3018-ba5b-370eb3d08375 | -18.08703 | -44.46046 | 2025-10-09 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95f99850-131b-3e23-9193-9f3b645ffb19 | -17.38445 | -46.88055 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d7a45c5-2606-311f-868a-42f6846bf9c8 | -17.09595 | -45.48641 | 2025-10-09 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba49aaf6-190a-337e-99c4-19d9a793b050 | -17.39265 | -46.89211 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96881d0f-70ae-34fe-915e-95f31bb35a9e | -16.28361 | -47.14043 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25db310e-23fa-32c1-b586-3cf0deebd703 | -16.26465 | -48.63064 | 2025-10-09 04:21:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87cc7f39-24f1-37f8-b40c-13a637adcfe3 | -17.54037 | -46.06688 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b8375ed-4ff2-3e1f-91ff-222e0e530eb6 | -18.02484 | -57.56397 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 29d9eaec-59f1-3be6-b3c2-bd3dc7981e54 | -16.42165 | -47.82464 | 2025-10-09 04:21:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 647a2853-7ea1-3455-aad9-473b3c61bef9 | -15.28625 | -46.16478 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f64a8c1-7ca8-37fe-8692-711116625433 | -17.97787 | -44.96144 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08ec0b51-d2c5-3f20-b17b-032505ff15a4 | -18.07419 | -44.47469 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00bf06b7-2e67-3e20-9997-ccb370ca1e52 | -15.40199 | -46.2711 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d19d3ff6-bb9d-3f03-ae79-4949296b086c | -16.26125 | -48.63003 | 2025-10-09 04:21:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76429242-ae33-3ac5-b80f-14d382dfea6f | -17.91699 | -57.51115 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3ca862ff-6aac-38b3-bb30-f349ccf2ed84 | -15.48471 | -46.86679 | 2025-10-09 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0f451fa-e6b4-3110-85bc-42da8311d212 | -17.57988 | -46.07741 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aeef2fa9-473a-35e5-854d-be8c0d7b7e8c | -17.65347 | -44.44129 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3cca5fa3-1d7b-35c5-b58d-535915655157 | -15.07223 | -46.61885 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1e818c0-1f45-3708-a582-1c3f02914103 | -17.65405 | -44.43718 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43069340-323e-36b7-a760-df9b39bd38b4 | -17.38114 | -46.87998 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 887d40e4-2f6e-3222-8bec-57d9019ae9bf | -17.87178 | -48.23002 | 2025-10-09 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee8c49b6-df59-3f4c-b3ed-77bd8e99f3d1 | -16.03472 | -50.99535 | 2025-10-09 04:21:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5feeab42-318a-300b-846e-68a0d662e409 | -17.26819 | -46.97169 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 4dd2dc46-23cb-3dc9-9443-e0dff746df69 | -17.90016 | -57.66397 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ae69af83-6050-3dd2-806d-9d2b4b841c83 | -16.32858 | -47.09291 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2e6d92b-05bd-3148-8e34-cde5a437d906 | -17.35962 | -45.05178 | 2025-10-09 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbb5ef9b-d193-35a4-b49f-17deec79899b | -15.48971 | -46.85667 | 2025-10-09 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d529403d-8f18-3725-bf4d-6cd8746e697b | -17.93732 | -57.54631 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c841e650-4a7b-362b-a4f4-6f7a43dbf336 | -15.48915 | -46.86023 | 2025-10-09 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f06d8da-092b-3ccc-b4e0-c238d7771f00 | -17.92891 | -44.60538 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dcfdf7d-e455-3cf1-8ca4-dad20f961ad0 | -15.0066 | -47.5353 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b176f90a-9631-343a-b723-93c6ed1d4420 | -19.72504 | -43.90421 | 2025-10-09 04:21:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5cbe026d-d4e3-3606-855c-4e77fcc72c5f | -17.15668 | -43.43386 | 2025-10-09 04:21:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 762bae33-d0cf-3fd3-909e-0231c25c061b | -15.37251 | -47.33335 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97a7b5a3-9d62-3d57-8500-0b35cd12661e | -17.58713 | -46.07482 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04789b40-b126-35b9-bd89-e9c73f8161be | -15.22298 | -46.37389 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ac208db-8494-38d7-8650-b9372a846e4d | -18.05163 | -44.95644 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bb17af4-d565-34fa-a81d-dac319ff932f | -14.85059 | -48.43516 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98b1824c-00b0-3038-91f2-e4c93580f522 | -15.06448 | -48.07658 | 2025-10-09 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b2e7618-91bb-38af-868a-6279403fc804 | -17.65111 | -44.43257 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf8936ab-e00b-3169-bbdc-f724c7dd058e | -15.78269 | -46.24588 | 2025-10-09 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8dbf621-e23b-325d-b5d1-a8ad973b42df | -16.62123 | -46.76705 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99bdd7ca-769b-34e0-9030-e2444b918d6f | -15.29396 | -46.18072 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 607db242-8233-30b3-b4b6-ce41060b3c92 | -16.7498 | -43.97309 | 2025-10-09 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2a22205a-0663-316a-95a7-19724a5f0132 | -15.54232 | -45.29607 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 975e418e-dd4d-3a9e-9445-3b86f5272c7a | -18.0476 | -44.95984 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e40da8ad-ee44-3761-acaa-267e5ad7f9f8 | -17.88838 | -42.86884 | 2025-10-09 04:21:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22af888e-fb1b-37da-9280-de9531e2d77d | -14.84802 | -48.45044 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e81ae3be-aadb-3226-8391-4a8644ff041f | -15.40088 | -46.27819 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a0203f0-a491-32c9-8242-0bc5bbb03b41 | -18.02541 | -57.56778 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 28f5a36e-9cf3-3c26-b716-adfd09f4626e | -17.23412 | -46.92889 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89a5c596-d637-3cb2-939d-cba575c58647 | -17.93912 | -57.54353 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 52bb50c7-89e4-3f9e-8ca3-0a122f3404af | -18.06179 | -57.52683 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| caaee268-66c8-3e01-8fc8-856697b3e8fa | -17.92829 | -57.50786 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 71312739-d9f9-32e1-a1f2-0523603c281e | -19.18023 | -46.50525 | 2025-10-09 04:21:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f8de199-d286-3c0b-8398-d1656f51d2cd | -17.16039 | -43.43419 | 2025-10-09 04:21:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 394ef377-c48e-330c-981f-19e6f8a6c4c1 | -15.07005 | -46.61118 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 622edcfc-c94f-3c3c-83df-e0e642fe1729 | -14.93762 | -46.78275 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70ac1808-8fa4-3567-b209-fd576a4c747e | -20.84949 | -49.48094 | 2025-10-09 04:21:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cfac9daf-0acf-3b94-b740-8b973aeb18bd | -15.07392 | -46.60817 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 69a951cb-6ed8-39a1-a5db-e01bbe0a74b9 | -18.29968 | -45.43306 | 2025-10-09 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 470303f4-341f-380d-83f1-1c8beb5e3913 | -14.4648 | -52.90685 | 2025-10-09 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d08f1975-8cb5-357d-9836-e3ec26c2a76e | -17.38163 | -46.89856 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecc27b34-546f-3146-b034-7f5b41165317 | -18.54516 | -45.06622 | 2025-10-09 04:21:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38ebbc2a-8c29-3f64-8b29-8a69bed4aa92 | -14.9781 | -46.28926 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 134d399f-7022-30fb-bb67-959f318c1f5f | -15.99667 | -59.54875 | 2025-10-09 04:21:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d210ce37-d265-3547-9f59-369c6256c9ac | -15.39089 | -48.05643 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 354bfa94-ea8b-3045-a04b-019461820799 | -19.71926 | -44.00109 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e614a881-e342-3f3a-bd4f-f8ad6652a0b9 | -16.60235 | -58.15965 | 2025-10-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2c116758-7422-3779-b7a3-51c22c01196b | -15.29068 | -46.1582 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b0ad1f0-e658-3122-a6aa-7e4e554b3baf | -14.64228 | -49.253 | 2025-10-09 04:21:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac10c75a-47c0-319f-bd8b-42d0e723bec6 | -14.97479 | -46.28871 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e67380e-47c4-35d1-b569-cef3702ea327 | -15.58502 | -47.85075 | 2025-10-09 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11177daf-84d5-3cae-a06f-ec5a12fdcf8c | -15.2329 | -46.37554 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86939a1a-12fc-3ae8-af27-4c35ced8b8e9 | -15.55912 | -45.32144 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b9e3485-e7dd-3f2b-b1f6-824991a17c7f | -18.03494 | -44.97387 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README47.md)
