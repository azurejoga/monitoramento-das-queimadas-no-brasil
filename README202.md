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

## Dados Diários - Página 202

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92c15a2c-4758-3cef-8e9a-59b61ac95130 | -3.49259 | -39.49694 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| e2aae585-f064-310a-8a1b-2cbf32b16e28 | -4.11736 | -41.7816 | 2026-10-07 16:37:00 | NPP-375 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 1bc91390-a73d-3d5f-8acf-08ff211c85dd | -11.14227 | -46.16763 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3e11c260-29e7-3287-b913-7978dbd4c316 | -7.77278 | -43.8137 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 54c82f48-d979-3862-9764-4c6c68ceb5c0 | -3.52172 | -40.66382 | 2026-10-07 16:37:00 | NPP-375 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 50.1 |
| fabb05ac-67dd-3f13-bfdc-4949221137eb | -4.56144 | -40.72122 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| b373f73c-e624-32bc-b09a-d8216d10f397 | -8.03056 | -40.56398 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| d7ceb466-7af2-3e5d-8254-93c6bbec3613 | -5.91604 | -51.94326 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7ebf2cf7-976e-345f-b0bf-25d47587fddc | -6.95459 | -44.40734 | 2026-10-07 16:37:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d7f7802d-3abd-39d3-ae21-3510756fd9ae | -6.44371 | -45.20331 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4cba6f55-2b8d-36e7-9a98-003f2c3b416e | -6.03153 | -43.02754 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d209f1b2-9bfa-3e1d-9130-705ebd79e5ab | -6.68631 | -52.96501 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3e2bac96-1a98-38e2-a1f8-8c973be2e281 | -6.376 | -45.05052 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a47c9259-0708-35f0-8861-76b78869924b | -7.21726 | -44.15897 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 30a2fb98-0268-313a-8f78-7a81965e2692 | -16.91364 | -42.12019 | 2026-10-07 16:37:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3f67614b-03db-3980-bbb8-4d318a7b7e67 | -6.61521 | -37.89819 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f4d7b79a-64ab-31ed-98d4-bd8ee8da5110 | -9.23772 | -45.66492 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b9eb8617-60a2-3b8f-9980-0694c8625ebb | -5.55199 | -43.96889 | 2026-10-07 16:37:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e974adb9-8242-3cea-84b9-f12014dbc4ab | -10.99603 | -45.4176 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| be619d7e-b463-3bd7-9559-f48aeb4bce87 | -8.7662 | -44.16417 | 2026-10-07 16:37:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a732e20d-5a36-3eca-afb3-976a77ed6ef8 | -3.76766 | -41.71772 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 8ea721bf-cf38-3d23-bbe9-2fc1a4751a02 | -9.58693 | -54.63764 | 2026-10-07 16:37:00 | NPP-375 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 0758259e-64f5-3302-915d-a57cb4538a3d | -9.4031 | -45.89052 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 768ced1b-f5fb-305f-abac-5c7d13d39086 | -7.03209 | -45.42873 | 2026-10-07 16:37:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 701f166d-feec-3c96-a4d2-1bbe86bbeef0 | -6.81564 | -42.97839 | 2026-10-07 16:37:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| e9a4112f-cfe1-3a3b-93a7-04f17c0791bf | -4.80392 | -42.74865 | 2026-10-07 16:37:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e8774fd9-34f0-3adc-87f6-e6674fe9d939 | -4.27731 | -39.54972 | 2026-10-07 16:37:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5efc863f-d5c9-34f2-bab4-a4076059f917 | -7.46685 | -42.99024 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c0be2595-bd2b-3a7a-ac36-f256baa4f02e | -7.20053 | -55.12749 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c723b760-7696-382f-a64c-2d5683d34dbf | -9.82924 | -46.24395 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 3edc9a22-073c-3b5e-b7e6-658a92751be3 | -5.74261 | -53.4747 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c6d5b5a1-cacc-3fdd-b824-4cee18107075 | -7.17629 | -47.80126 | 2026-10-07 16:37:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 5e29a883-cf25-3e84-a3b4-0b43cbd10a4c | -9.97025 | -43.57024 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 73ab0d0f-a79f-3b40-9311-b076a36d6f73 | -3.80688 | -42.37518 | 2026-10-07 16:37:00 | NPP-375 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7536f9fe-f355-30fe-b1b0-64692a466192 | -4.37729 | -46.34383 | 2026-10-07 16:37:00 | NPP-375 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4f749f9f-9594-3089-b635-d91cb6e239ce | -16.19031 | -44.57061 | 2026-10-07 16:37:00 | NPP-375 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6954f0bd-25ad-3e07-a22e-0ca2288461fe | -9.93188 | -46.80628 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 280bf9d4-d854-30a5-8c47-f0ffb48a6bd3 | -6.17802 | -44.03973 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c1d12985-4c96-3a18-9d77-a96963cea162 | -6.174 | -52.92799 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 811119be-f3d5-3b33-8bef-cf54afc8f597 | -7.49335 | -44.44002 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db48c9ff-3f0f-3c25-a182-96c39434dd28 | -7.17186 | -47.79713 | 2026-10-07 16:37:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| a4bcfdbb-6d3b-36dd-bae2-4be03b409d5a | -3.69924 | -40.8586 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 35.4 |
| c0651550-3e87-3000-acc2-4b170a44db56 | -3.36015 | -43.38832 | 2026-10-07 16:37:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 8eb22096-b1ba-37eb-9fda-de35a504eee6 | -5.72457 | -41.72678 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 40.4 |
| d1a5fd5d-52b1-3b81-a49c-f3e341f302d1 | -10.52227 | -47.286 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 2e4d4c15-49be-3c40-bf71-2880ae3066b3 | -10.17643 | -46.71946 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| fd4945b8-dee6-3fde-b6ed-c31131a27abe | -15.9259 | -47.37361 | 2026-10-07 16:37:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cc0fc119-23c5-3774-bf90-837ba89c8c24 | -9.77777 | -45.91734 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| b13498d9-3c39-307d-a1bf-e31b39c71828 | -7.17094 | -41.99263 | 2026-10-07 16:37:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| c3c1d2ec-3548-39c4-9c39-2a6946a3b0a6 | -9.95044 | -43.5518 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 280937c2-2d61-3daa-bed3-2274b2fad581 | -8.53675 | -54.58698 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c6402ddf-e82a-308b-ad44-219fa2dc9c70 | -3.29753 | -42.27871 | 2026-10-07 16:37:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| d745c86a-2646-3f0a-a863-73c0e6d5f45f | -6.37353 | -45.80083 | 2026-10-07 16:37:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c3ef95b0-ff65-36b9-a556-612f79d4523d | -5.53412 | -44.95603 | 2026-10-07 16:37:00 | NPP-375 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 88e07dbc-7b17-35c4-95b5-e09685d487a1 | -7.5554 | -46.68925 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e9a5fc07-e4c0-3394-9c60-117fde9d2fc4 | -6.48492 | -52.82198 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f5ed5d5c-7067-34f0-a9d3-b3b3729fe7e2 | -5.79762 | -52.35896 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| bd02cf74-ae6a-3e20-bd3e-5f54cf1d5244 | -8.01369 | -47.18172 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c56999df-a8f4-39fd-a5b1-3b40bc53533d | -17.02133 | -45.92083 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9cdc8289-5fe8-3c6a-9c7d-fa96c1db6b2a | -3.70015 | -40.83981 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 0d47bc77-311d-3380-b3ba-3c0aabde2e7b | -6.00647 | -52.75861 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41b8ed4b-2a4d-3ab9-8229-a3eb0e8f9a7c | -9.93545 | -45.91489 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cecf442a-ad7a-3c69-a41f-cc4fa1e5fad9 | -4.2648 | -50.74281 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 87e9c76e-d321-339b-adb3-1f248d783caa | -4.28584 | -49.87476 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 997da51f-9a49-3f91-9cbf-c23e975015f5 | -5.96646 | -53.59658 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4260b84f-358e-3588-8d01-6ddaa615a61f | -10.78709 | -47.63464 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d79e9276-77ce-3dd3-b2f2-3fdd99e80683 | -9.20104 | -46.7052 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a302a169-cb9e-3398-a738-4ee33bb64200 | -6.1453 | -52.6538 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| aacf90f1-10b6-33df-9511-8f77888b8b62 | -6.70058 | -44.98515 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c58afc10-250b-38b6-b949-97623bbc673d | -7.48568 | -42.8243 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c441b4ad-7a3b-3a79-b730-53f5749e9c1d | -5.73372 | -45.16114 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 169.4 |
| a729cfa5-2026-343c-b338-7b95a08c9a29 | -11.10487 | -47.59708 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 32ac253b-2c91-35f2-839d-7eb61fd9ee16 | -7.87686 | -44.22892 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 5daa8bc6-38ae-3ded-9192-841fee31283f | -5.37242 | -44.16446 | 2026-10-07 16:37:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4f1bcf8b-9a79-3c7b-88bd-bd0474de426b | -11.09875 | -47.63911 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1b25618a-ca92-3127-8eb4-28c6df13d2f1 | -8.96945 | -47.56777 | 2026-10-07 16:37:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 37ee2240-7c68-3088-bd2c-67581bb8457d | -7.06597 | -45.37136 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 73f5894f-c61d-3992-80f1-55bcfff420fe | -3.84914 | -42.2303 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 20c488c6-e68a-3f49-9c96-d4d73ec707c1 | -3.23314 | -42.58483 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99ddd5e1-9ef0-345d-b8e5-9bca44052202 | -6.20293 | -52.78763 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 21586451-55dc-36f6-85c2-86aba1b21336 | -17.24834 | -44.42814 | 2026-10-07 16:37:00 | NPP-375 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3d06762f-5862-36ec-aa82-2f24119ac34a | -6.60899 | -53.02293 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 38783db4-7015-3f7a-be7c-48a9d358e094 | -6.05165 | -53.47617 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 1c6e39e8-476b-354b-8d31-87d63578ef31 | -8.06179 | -55.29226 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 01d042b5-cbf1-3462-a1b8-6a3ed07c663e | -4.74025 | -49.92275 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 616dee4a-232c-315f-bde8-0833eed733f4 | -5.97193 | -40.9428 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 5bd91251-e1ce-39b6-80bc-75aac3cfce58 | -17.19059 | -43.54184 | 2026-10-07 16:37:00 | NPP-375 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6be123a9-ab8c-3d13-a472-c2d35f166a3f | -5.73145 | -45.1687 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 35f24bbf-9984-3cfc-b9c7-5be1c811e0a2 | -10.88502 | -46.67838 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 5a149b55-ae79-3f79-b2ac-a27bd662eedd | -8.19756 | -46.35437 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ad740b0f-db4b-3099-abfd-c26c0768360b | -4.91264 | -43.22337 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| be4da169-bde7-344e-ab36-4ad8468e3dde | -6.62086 | -37.87885 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 65b34a02-b70a-3c91-bc3b-30ed04dd3a84 | -6.25509 | -47.31374 | 2026-10-07 16:37:00 | NPP-375 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 15e3daf8-b209-36bd-86d0-4b7ccad7b4b8 | -6.19814 | -52.82971 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 565e66f6-35cb-378a-8cc2-6d93e090506a | -5.97336 | -41.35848 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| fc497cbd-b9f9-3c66-bbb0-8dc49bbee50d | -4.27332 | -43.01923 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 00d97ec3-5161-374f-bf69-8c745ada6906 | -5.03757 | -50.01602 | 2026-10-07 16:37:00 | NPP-375 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7bb75625-2c78-3e79-a653-214708a23f7f | -6.43543 | -44.84286 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eb8f809f-fe21-37e1-a300-f05c0640bcc3 | -5.95406 | -46.37128 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 46a263aa-b1d5-3859-9a2f-a068627b620a | -8.28586 | -50.6629 | 2026-10-07 16:37:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README203.md)
