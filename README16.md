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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5693a4b7-f63e-309c-9371-5c6f46362878 | -6.64407 | -58.83664 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| df1e7f6d-ecf4-3b13-9e1b-acccbc1df63a | -7.5093 | -45.39075 | 2025-07-26 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0e9e250-c043-3585-8007-491614bd46da | -6.64538 | -58.86899 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ced0bc32-6301-3190-b8ba-cd66dcff1f17 | -6.64953 | -58.84333 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 181.1 |
| 4a2a900f-c0ae-3210-a4df-2e9c6a42beb3 | -6.52606 | -44.59201 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea82b812-4921-320d-a374-3cf2138b4cd4 | -10.35276 | -46.64592 | 2025-07-26 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf798d78-5a28-3633-b531-e8aa514160ac | -6.63753 | -58.83821 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 04a28701-b1a1-3cf0-85a9-aa0afaa8adab | -6.65478 | -58.92881 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b5a32ab-76d6-3d27-b2a1-ab7058ce58ae | -7.4601 | -49.39591 | 2025-07-26 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 02d49814-e612-3c47-85b9-be7fb2c2fb0b | -6.01028 | -52.16853 | 2025-07-26 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 902a618f-4735-3725-a287-6c841aeea297 | -10.4441 | -46.51575 | 2025-07-26 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69b735e0-0184-391c-9e7f-e7b900b2d246 | -5.01091 | -42.76225 | 2025-07-26 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc300f22-a5be-364d-84e8-7692fe6a6849 | -6.67969 | -58.82611 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0ab07f08-52ef-35af-856f-bd7678d6be3b | -7.1954 | -44.02266 | 2025-07-26 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 504fa038-ac9d-3328-8b4c-7ebb6bf67d9c | -3.74486 | -49.047 | 2025-07-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78ed423d-e580-3b29-83df-9a0e86355277 | -6.9329 | -42.80605 | 2025-07-26 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 05b3e143-5ccd-3313-8de1-3a8f92613e34 | -9.91884 | -47.76196 | 2025-07-26 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b47e3b4-6b43-32b8-944c-a302462ae837 | -10.61959 | -44.76318 | 2025-07-26 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 724a6ab4-7f6e-37fd-8901-79c4e1494077 | -5.91348 | -44.97366 | 2025-07-26 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b57ca8a-dee1-363c-8ab6-6276032d2741 | -6.68617 | -58.82735 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0492ae42-bedb-3549-8b7b-d3b49493129f | -8.28756 | -45.00328 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c40efb4-ab18-3fea-a6fa-7b5299669db8 | -10.59386 | -44.74298 | 2025-07-26 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94899c1a-1a92-35b0-9f34-c9cb9c583242 | -9.35812 | -40.31301 | 2025-07-26 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 410f48d0-15de-300d-9aab-f2bdb33df240 | -6.52947 | -44.59249 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd5be4d7-accf-3f6c-89aa-960f69a438a0 | -6.70996 | -50.47021 | 2025-07-26 04:25:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5bceb1f-0593-3444-9b02-d0ebec5713b6 | -6.15712 | -42.59392 | 2025-07-26 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 893ce6ba-ab6d-313f-8e74-41fc309153da | -10.44077 | -46.51522 | 2025-07-26 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54af409e-aa65-3f3d-a57e-a3e57b67537c | -6.67345 | -58.86274 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e3a502e9-aabf-3b14-a9a9-735bc001565d | -6.64093 | -58.85323 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 678a78d6-5a66-3329-b928-1f9cf35ec214 | -7.78593 | -44.5489 | 2025-07-26 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 234feda0-6c07-3d08-9ed1-0efd05c009ce | -7.23573 | -43.07257 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a4bcf655-28e3-3b30-ad13-a5365b15bab8 | -9.01748 | -45.35878 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9d959a5-1e04-3ffe-ae00-efd99006a407 | -6.47513 | -43.48368 | 2025-07-26 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ceb5e88-6b83-3404-b50e-44441a5380a8 | -3.98714 | -47.8893 | 2025-07-26 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e88a531e-5605-3fa0-92a1-d85ceb726d21 | -6.8883 | -43.12403 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdc4089d-5fb6-3ae4-b3c2-ff11968263f6 | -6.22867 | -44.52059 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dae705e0-2c92-3ad5-84bd-b40311c5e2f4 | -10.50098 | -44.87832 | 2025-07-26 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baf15e4b-8717-3be4-8045-25be5a371daa | -7.08315 | -44.86664 | 2025-07-26 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae51a91e-acfa-3683-9fd2-1f1ea0b65fa3 | -3.36261 | -49.16395 | 2025-07-26 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c35967af-8d35-3f37-87fb-2e6775a17ad0 | -7.5678 | -44.48636 | 2025-07-26 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f5960fe-6225-3bc4-a1d5-1c2b96059dbe | -4.03274 | -48.06501 | 2025-07-26 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d001dc2-ab37-36f5-9993-4b4cfaddaa04 | -6.65148 | -58.83547 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 25859f35-f4f0-36c1-8810-c07993c80330 | -6.65812 | -58.83352 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 3fe55132-71ca-39c9-89e0-f1fb88e52453 | -4.17399 | -47.53315 | 2025-07-26 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c3cd781-e168-3b22-b84f-936e1f2f1d1c | -10.35661 | -46.64299 | 2025-07-26 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e77a9cf6-ec74-309a-8d8f-f934a2197def | -4.30607 | -48.107 | 2025-07-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99bfe4ca-bf47-359e-a6b7-e2f270ecbefc | -5.74289 | -43.96851 | 2025-07-26 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06ec48aa-bd31-30f5-8d88-ac2ba5241fc7 | -4.61591 | -43.32081 | 2025-07-26 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77c6502c-671f-3cf3-8741-8b7e080ab133 | -6.66588 | -58.86379 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 7c390f2c-2a39-3492-959e-c82718a1ce84 | -9.00168 | -45.34878 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b59c8ca-268f-35b1-91eb-76b2d455dbe2 | -7.23687 | -43.07006 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 892fe771-edb3-3505-b4a9-932213aaae88 | -6.65632 | -58.91469 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccbda64f-9647-3e54-a942-badc2b71b051 | -6.87199 | -43.67914 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17b10622-0c16-33a1-94e8-01bdfd83cc2c | -3.98431 | -47.88496 | 2025-07-26 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b649972b-ef4f-39ed-a625-78e7040b958c | -6.64641 | -58.86332 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| d70858f5-1c7f-3bdb-ad68-c39937b33c21 | -8.29438 | -45.00432 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b46acf69-4eeb-3f31-bf12-17ff2748bedd | -11.45802 | -45.194 | 2025-07-26 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6639b356-7be2-3dca-aeee-9ffdbe18ec65 | -6.87138 | -43.68316 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ea40863c-41d4-3b49-87db-3446650537a0 | -6.00894 | -52.17638 | 2025-07-26 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f94f3f2e-8a45-379a-8eb0-44f64fdd190d | -6.68956 | -58.84521 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2abf2acf-9357-3e4d-bbc1-bfbc6b7f1622 | -6.70333 | -43.06281 | 2025-07-26 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6edf8f5c-31bf-3fc6-a3cf-ae1ecc215b9e | -3.3484 | -49.2279 | 2025-07-26 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2215665f-e7b2-3e3e-85d5-b834ea73f796 | -6.20773 | -43.744 | 2025-07-26 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b9893f2d-0193-331c-b4a5-47d187b63887 | -7.56435 | -44.48584 | 2025-07-26 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5319e8d-fd34-3e03-ae8f-08481df04cee | -9.13905 | -45.86825 | 2025-07-26 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6286d666-66c1-3ef2-a399-a53c6d581faf | -5.32124 | -55.94564 | 2025-07-26 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4cb289e9-ab9b-3d29-8e46-50968ef32936 | -7.23637 | -43.06822 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 564ef5ef-061a-327b-8e74-2ba826adfb46 | -6.6366 | -58.84055 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f047d53f-b803-35d5-8319-d2be856449ff | -6.62689 | -58.85955 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 83b1606a-8e24-3149-b634-a20f5b10ad7f | -5.91684 | -44.97419 | 2025-07-26 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e84bc97f-168e-3bde-b823-12b4c5bface8 | -10.68065 | -51.88081 | 2025-07-26 04:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0ea580d-6432-393e-a044-93fa04246e82 | -9.13181 | -45.87076 | 2025-07-26 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8cf2b8e-60c4-349d-bb16-96694154c06e | -3.6652 | -50.95326 | 2025-07-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04caa214-eb03-3888-9f53-e1f920cdb3b9 | -6.65016 | -43.04301 | 2025-07-26 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 453e25b7-dc3b-3465-9cfd-e7b1c858ec74 | -6.65287 | -58.86135 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| e58cb998-4e25-3917-bc48-9e4b6740b6ec | -6.66358 | -58.84023 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 57575c53-3a9f-3534-ac0d-630400229403 | -6.65624 | -58.87923 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea899e6b-b65c-38e8-ba27-7a76ce228a1f | -6.66043 | -58.86029 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 58096552-f36b-362f-a993-5b09d085b860 | -9.13461 | -45.87484 | 2025-07-26 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 393fc0c5-5e65-3004-9400-8b2133c78e52 | -6.4167 | -41.14932 | 2025-07-26 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6f55311e-fc93-3b8f-b277-c62b34e418e3 | -6.67553 | -58.84831 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 21f1c166-d502-3773-95a1-dc1d83bf9aa4 | -5.90246 | -44.32015 | 2025-07-26 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0efca45-b0a8-34c8-8c5d-1af72cd46fac | -8.86867 | -49.04957 | 2025-07-26 04:25:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 806a14e8-5cf7-3109-af24-627cc6fabf13 | -6.32475 | -44.09713 | 2025-07-26 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d84d76ae-40bf-3005-b17f-827324b6dd07 | -4.07101 | -46.90313 | 2025-07-26 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e458129-6dd6-3196-a0f4-8bb01f7c9bbd | -6.32877 | -44.094 | 2025-07-26 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d5daecf-16d3-352b-897a-12bc2c63df31 | -3.66005 | -48.44758 | 2025-07-26 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e41262e5-67ac-331d-938c-bc73d5ba9532 | -6.78298 | -44.10078 | 2025-07-26 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67658321-7acd-3fc6-a66c-50cafdee4058 | -6.62249 | -58.84681 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d69db554-c1a1-344e-8359-dfb36e9b9ed3 | -6.77892 | -44.10413 | 2025-07-26 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4de903e8-0e40-390d-81b6-8d33ef73e2cb | -6.64197 | -58.85077 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 329527a1-1f48-33b6-9d56-a77ba94f694a | -9.91553 | -47.76141 | 2025-07-26 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3e4badc-7167-3939-b8a4-7dfb9ee5bc39 | -5.74058 | -43.9604 | 2025-07-26 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ed6cf30-d377-3717-b164-99d94f92f5a7 | -9.50176 | -43.16856 | 2025-07-26 04:25:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dd18cd46-ed0d-36d9-bb2b-210acf13308b | -6.6665 | -58.82677 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 892e0189-53ef-3b70-9952-c22b5fe7ad62 | -6.671 | -58.83908 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 9e1f343b-d319-3107-bd13-f2bcedce9553 | -7.2474 | -43.0699 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 0b857f13-5c88-3fd4-beb7-8ca3b735e29f | -4.35268 | -47.68792 | 2025-07-26 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82e72604-9acd-3e62-8aed-15911822262c | -7.07977 | -44.04601 | 2025-07-26 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0832f2d-f91c-3f31-86f8-f3f8ae07d051 | -6.64597 | -58.82881 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |


[Clique aqui para ver as próximas entradas](README17.md)
