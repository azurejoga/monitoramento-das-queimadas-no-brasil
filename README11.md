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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ffefc9a-01b1-307f-9741-bd17a9efcd9f | -9.10437 | -44.40452 | 2025-10-04 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7290b964-e2ba-3987-86a1-e21f12576963 | -6.99988 | -42.30776 | 2025-10-04 03:23:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dab8fabe-8c08-37a9-b485-db61f0a2a4a5 | -7.78592 | -44.13568 | 2025-10-04 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eeb7d515-ff93-3916-9c29-c91029ad9408 | -7.77481 | -42.60566 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3ceb1c04-89e0-3f27-8082-647e05d3dcb3 | -7.73522 | -42.60941 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 38e73d89-d3d8-36f4-ad8c-0564e62b0d09 | -8.05969 | -44.80685 | 2025-10-04 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 67b84841-131d-38b8-af8a-c5d90ffe338e | -7.7807 | -42.59515 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 99d60cac-2b9c-3e89-b0bc-b0c4ff6271d6 | -6.12072 | -43.11534 | 2025-10-04 03:23:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6824c5cc-4744-371f-a305-97c6d40c7fba | -7.79363 | -42.56097 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 30b81e7e-8f1a-30e7-a80d-d365c7283271 | -6.98901 | -42.79717 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 825ba01a-89a3-3814-a469-9e6f04ac8e5d | -5.98169 | -43.48355 | 2025-10-04 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3eccbd68-2f96-3afc-b75b-3edfa2fda275 | -6.22635 | -44.28202 | 2025-10-04 03:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8da8d561-9140-3a11-b28b-f454c643c241 | -7.69618 | -42.57541 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d61e8d01-bb00-3676-b1ba-47996327c637 | -7.007 | -42.3041 | 2025-10-04 03:23:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eefce963-bc8b-3019-92cd-25d6c537023c | -5.98235 | -43.48832 | 2025-10-04 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 730a440f-0724-3c32-b7d5-09e561c54251 | -7.15002 | -44.21231 | 2025-10-04 03:23:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afbad514-1150-30c7-93f7-4b68ebf71925 | -7.05243 | -42.78294 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1f47198e-9b5a-3f88-948c-d31c58091b7b | -6.36932 | -44.30663 | 2025-10-04 03:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bb335dd1-3bd9-3476-99a6-46429b50240e | -7.7266 | -42.58596 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c25b4659-be1e-3807-91b8-37e1aae1f303 | -6.6146 | -44.29361 | 2025-10-04 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 53f635cb-be7a-3e18-8fd9-ea253e6e579c | -6.876 | -37.28423 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3beb6071-b2fd-3a83-9b71-115e88cd3869 | -5.98917 | -43.48938 | 2025-10-04 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 09861183-54c8-38ed-9382-3aaf18f070ea | -7.74653 | -42.54823 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e81b0a40-ec56-3667-a4ab-874a0140829b | -10.27641 | -44.3416 | 2025-10-04 03:23:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 31e08c21-0194-3dc6-8fc7-cd334956e042 | -6.28425 | -43.62758 | 2025-10-04 03:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0e897612-26f1-39be-af58-a06e0bf275a9 | -10.02632 | -44.01247 | 2025-10-04 03:23:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20f0952c-0edd-3745-b276-9e8eed884bd6 | -5.87307 | -42.52637 | 2025-10-04 03:23:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cff86eb8-b3bc-3cdf-b057-9664e6577617 | -6.26802 | -42.44989 | 2025-10-04 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| aade7152-28ae-3aaf-bfae-917dcd9c062c | -5.66476 | -42.71511 | 2025-10-04 03:23:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 4c76de7c-d46d-3ec0-8a59-063cf992acc1 | -9.11239 | -44.39962 | 2025-10-04 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ef0f5a75-1527-3e1f-87ab-e0f25957acb5 | -9.91248 | -43.80631 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a10c2bc1-862e-3300-9c82-d55f104f8e12 | -5.68825 | -42.69661 | 2025-10-04 03:23:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c87666b2-6d97-3b37-bf4f-f09ebc2b90bc | -9.12172 | -40.13212 | 2025-10-04 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 789e8c29-8e2c-3f25-9f34-6b36101ce7ed | -10.53561 | -44.51787 | 2025-10-04 03:23:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd9fb105-e66f-39b9-a426-bc7acc92770d | -5.87946 | -42.52773 | 2025-10-04 03:23:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 241dca4f-8ab8-3e5f-96ca-b749d1868e6c | -6.99613 | -42.80046 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4d0faf6b-315f-3326-86ad-0b954eef34b0 | -6.66255 | -42.82676 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f12b1c1f-82ce-3fc2-bf83-ea90fa44d7a9 | -6.88065 | -44.50187 | 2025-10-04 03:23:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5bc0ebcd-117f-3015-a27d-7c2e0eae1b53 | -7.55961 | -42.39581 | 2025-10-04 03:23:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 01b2b145-7983-342c-9899-0eb5cf5d59dc | -9.89849 | -43.73943 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 05e7b4df-9d5c-3b1c-99c7-5daa9c981a43 | -7.72033 | -42.58485 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0e3c4ac6-f760-3378-a0ba-944cbf4b07ca | -6.71625 | -42.16596 | 2025-10-04 03:23:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4bc6d0a0-87a9-3d55-a39e-fb9218a40a94 | -6.29013 | -42.44894 | 2025-10-04 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1c5b1ee-69bb-3afb-a1fc-4832a55f3886 | -6.64736 | -41.95445 | 2025-10-04 03:23:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0c94b355-7e26-38a8-b8eb-5b2f1c4dd146 | -7.77041 | -42.61521 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c0b8c760-b688-38f7-9cab-f098dc585f04 | -7.80176 | -42.55214 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e93c914a-0e34-3bba-bd65-42198f37aa55 | -7.04601 | -42.78185 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 84330f18-b29b-32c8-8e27-51ee5b905f72 | -9.8996 | -43.7337 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f22a5202-d5e7-33ce-8562-4085dc55e44a | -7.79459 | -42.5559 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a93ad902-7139-39ff-b9ec-b8aa5dcbe0c1 | -5.7389 | -42.93519 | 2025-10-04 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| cf08ca62-52b4-3310-85c9-f6dff9da5768 | -9.90602 | -43.80346 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd0b5c4c-fa3f-347c-b1a1-35fad740a0f0 | -7.7015 | -42.58159 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0ac0444d-6f98-3805-84e4-02acc4f521f1 | -7.69711 | -42.57042 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6fe3f194-0be3-3e8d-a6bd-3572722eeb7c | -7.76753 | -42.61004 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0347adb0-39cd-3d4b-95ea-e4e549e0a880 | -5.83587 | -42.87834 | 2025-10-04 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2dfb9f6c-d636-39bf-bdb3-7e1ae00c1782 | -6.7084 | -42.79541 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f985673-c370-3131-995c-8246d651b0af | -5.82062 | -42.8876 | 2025-10-04 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f3a07e66-ef77-3e18-9b5f-172d8aa2093c | -9.94539 | -43.741 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e7968ee2-6f3c-39cb-a091-8c85c1da69ee | -6.37585 | -43.89751 | 2025-10-04 03:23:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 434a513a-34ff-3123-9eb1-e421eca7027b | -6.66227 | -42.82581 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| d38323cb-d32d-3ee2-a913-6c89d7d5bb1a | -7.80272 | -42.54704 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a2d6a7c3-766d-3b44-bd51-fcf16c2e3b47 | -6.06865 | -42.51339 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 0ae9cec2-81a2-3c69-b74b-fb4ffda1c669 | -7.75556 | -42.52339 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| d3adf0b3-5f63-3447-aa1a-9bd472a718d1 | -7.57194 | -42.3986 | 2025-10-04 03:23:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5194b982-2540-3452-b862-3d59905d793e | -9.9061 | -43.73483 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 7816a391-8f4e-32ae-9dff-8bcfd3edf3fb | -5.9873 | -43.49132 | 2025-10-04 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f4abb7af-5f90-3254-84ba-dd4f49b44e98 | -6.04942 | -42.50999 | 2025-10-04 03:23:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7dee6d9d-914d-38e1-81b6-35f2419cbf7e | -6.21935 | -44.28031 | 2025-10-04 03:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 69b2b0dc-db62-3171-9e61-d61200d49ba8 | -6.2846 | -42.44333 | 2025-10-04 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a38c3a15-d3c1-3873-a007-55575bb9f108 | -11.45076 | -43.50138 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bddc9a78-f886-3449-9f22-473fff9b9d41 | -6.07503 | -42.5147 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 4319d291-1f9e-3f72-92f8-6fd6389968b0 | -5.8217 | -42.88167 | 2025-10-04 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7f8dba9d-ede5-314f-83d6-cf36bd9fd248 | -5.71904 | -44.24258 | 2025-10-04 03:23:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 671e339c-e1a9-3e4d-8afc-714f36c923b8 | -7.76653 | -42.61554 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e8425e49-8ca2-3194-bb7a-74f7766d3494 | -5.97932 | -44.14915 | 2025-10-04 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4ea5f3fd-bd8d-3ace-b9fa-2ac30e1592a8 | -11.43936 | -43.4939 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c707cf05-386b-3e38-8923-d3721fa3499f | -5.93456 | -42.88701 | 2025-10-04 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ee8eb944-3d50-31d1-8dd2-14347d39e2a8 | -7.74247 | -42.60527 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 35af6372-071d-3fb9-8e93-c87d7e353fb4 | -7.725 | -42.55976 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8f7a72a3-780a-3ce4-99af-2c6df46d1450 | -7.01851 | -42.31153 | 2025-10-04 03:23:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a15f9760-683e-38dd-9126-6764d055e3d4 | -8.17824 | -44.13475 | 2025-10-04 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3baaf69d-7ef7-31b2-bdb8-86645ad78f28 | -6.04746 | -42.52101 | 2025-10-04 03:23:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7a4782f0-4b86-3af5-98d4-7c83b7ce1ea6 | -6.72214 | -44.14503 | 2025-10-04 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac14eeca-c7cf-3154-b068-bc78c219b395 | -7.34464 | -39.1754 | 2025-10-04 03:23:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c2da1cb8-1810-3fc8-a422-521846c3dbe8 | -9.9475 | -43.76426 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f14c5bdd-1c52-3d33-a177-7a19212305b1 | -10.28308 | -44.3429 | 2025-10-04 03:23:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b6d0058-8856-3f86-b099-affeaaca82c1 | -10.0329 | -44.0137 | 2025-10-04 03:23:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f4df223-e50a-327f-9910-52c4faab731a | -9.9486 | -43.75873 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b27eb999-b19d-38f0-ad90-c358326264af | -9.11356 | -44.40037 | 2025-10-04 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 62cbf27f-da42-3978-9aa5-aa5b28184830 | -7.72564 | -42.59115 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8be4ee1a-fadf-3f8e-a8a0-71ec333cad37 | -6.65873 | -42.80836 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d6ac0b70-5126-3e99-914e-0b980143bbeb | -7.77246 | -42.6044 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f71babf7-ca98-3c34-b756-b131b4776511 | -6.66322 | -42.82052 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9cfa7cc8-c8ca-3301-95d6-6c59dbfc5c0f | -6.27444 | -42.45066 | 2025-10-04 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 60898e97-b3cd-335d-b50c-754248009de8 | -10.53684 | -44.51183 | 2025-10-04 03:23:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e8b9fce-e259-349e-b659-7a7d413fe925 | -8.63513 | -43.98943 | 2025-10-04 03:23:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a487552e-3d97-36eb-b297-082ff43ea913 | -6.71382 | -42.80215 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d520e898-f36b-35a2-9bcf-d4592e8b1921 | -6.06889 | -42.52063 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| b9fe5c6b-1d96-3735-8133-65b824f8c713 | -7.75698 | -42.54973 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a475b39c-17d5-37ab-93a1-b8a1ae9952bd | -7.74011 | -42.60397 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |


[Clique aqui para ver as próximas entradas](README12.md)
