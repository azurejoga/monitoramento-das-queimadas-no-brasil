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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f102f311-96a1-3d5f-9a7d-c4141578d22f | -5.60653 | -40.81096 | 2025-08-30 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 50745e6d-4d4a-3d78-abb3-9c9ef9092fb3 | -3.36319 | -43.37188 | 2025-08-30 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87d0c61f-31ee-3360-8861-45e51c3a7f0a | -7.0505 | -44.28556 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5edc85a-7b79-3656-9732-ef2ffcfb1e9e | -6.50132 | -43.52874 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97f050e4-0c2a-399c-9b9a-6cd4411c280a | -7.10565 | -44.58628 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bbc3bf57-b197-341f-82f3-188813d8d8a2 | -5.18142 | -45.12435 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79d44700-f961-32f6-9b94-c6a01762b3ce | -7.73331 | -50.27362 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 529ed736-3882-3ed3-a171-b11ca38670e0 | -5.60861 | -44.21945 | 2025-08-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df6c1894-ca42-3d27-bbfe-5ae8a046fd54 | -6.23587 | -42.40566 | 2025-08-30 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 18733391-a6d5-3b60-ac1d-d70c063fc892 | -6.68735 | -49.77155 | 2025-08-30 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab4d6963-9eaf-31c5-b3a7-7e0758fe5da3 | -7.13546 | -43.49206 | 2025-08-30 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 633e539c-8f2f-301b-9979-bdc8e6962f9e | -5.75978 | -45.36123 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ec57ef0-e20f-303f-a402-539b190870d7 | -6.66218 | -44.37749 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 54306b0b-7227-3f90-b43b-fc2146d7c314 | -7.264 | -39.67459 | 2025-08-30 04:19:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e0f53708-a6b5-3856-be55-189ab4747437 | -5.83046 | -44.10534 | 2025-08-30 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49207bff-8ae1-3c58-a3a1-7459e5543a88 | -5.55129 | -42.63793 | 2025-08-30 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3c23440d-3bd8-38ae-a60b-e16d01783a8d | -6.94532 | -44.06465 | 2025-08-30 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84d28f15-e685-313b-8e27-0bd0a5468122 | -6.38284 | -45.5743 | 2025-08-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a17a408f-b274-3878-a9ff-0e392e740674 | -6.49183 | -43.54566 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea42ee0d-e424-36de-b694-a898b42db19e | -7.72929 | -50.27287 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e40db26-07d1-3355-9219-55c8b488b736 | -6.53206 | -42.96703 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60eae8fc-a804-32e5-8389-8f3701ac796c | -6.50267 | -45.09583 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 509f258d-1611-3802-8b0c-f65556ec2966 | -6.04392 | -44.46174 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2438505d-26d2-34f1-93e8-3fc97e695e4a | -4.42311 | -40.71703 | 2025-08-30 04:19:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e5bc7f15-a549-3359-a8aa-ae6a702d1a38 | -3.42142 | -49.04416 | 2025-08-30 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee866b3e-97c6-3ab8-8e6e-d15fb542ba13 | -7.20453 | -45.45649 | 2025-08-30 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6533ca72-eaa8-3a91-82d1-412b9af41c2b | -7.20456 | -43.70572 | 2025-08-30 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eda6af3c-87d1-3c6d-b6cb-e315ae51b0b5 | -5.61107 | -45.00799 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 23b601ce-e929-3000-b07e-5024bcccecc0 | -7.40678 | -42.05998 | 2025-08-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 82c4cce2-6d48-35ec-8eda-d517476bbde3 | -7.60448 | -42.71865 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9bc51f7d-146c-3bfc-937d-795496403590 | -6.65957 | -43.93383 | 2025-08-30 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ed4c92b-ce0f-369d-b46f-06523b22dfbf | -3.62723 | -49.19173 | 2025-08-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69decbe2-08e4-3bbc-94fd-4fa1d761f483 | -5.70195 | -45.96102 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a9e38b9-12d4-3230-881b-bfa49e0b0085 | -6.63685 | -44.38779 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dbd751b-2051-3925-bd30-4380da993cb7 | -5.43151 | -45.52355 | 2025-08-30 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4fd00281-b054-3acb-b524-072a296a7c22 | -6.94114 | -46.1754 | 2025-08-30 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 026e5ded-e7d9-341d-94bc-8d0cf15f977e | -7.62323 | -42.66589 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b584a358-d6ed-352c-b7c1-2cce2e2c9f8c | -7.6762 | -44.98503 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b69a1e0c-8b1f-3cac-8c10-2a7fcb90d1a6 | -5.69803 | -45.96405 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd792ccb-0e06-3892-8768-6b810b5a5244 | -6.81004 | -43.72542 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 313cf728-8989-33e3-979d-944b25596827 | -5.61437 | -45.0085 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8ead9483-a9e3-3517-8b75-dc9fa42e06eb | -5.72689 | -43.93977 | 2025-08-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f50ee99d-53d1-3aec-831c-61cd10d09cd7 | -7.08925 | -44.29876 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96c2f5ed-7ab2-357a-8686-d5605817a77b | -6.25161 | -43.38012 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 133ae2df-236b-3eba-aa2a-a87aecb362fc | -5.61714 | -45.01247 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79fd3433-a97b-394b-9216-56eb42099050 | -6.99712 | -44.36609 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8001be1-26d3-346e-ab80-8f20b1ad5ff3 | -7.01431 | -42.02571 | 2025-08-30 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b4dd9bd5-3f92-3201-aed2-761404df53fc | -7.77196 | -45.46116 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7ae7759-e59c-33ce-8b37-4215c824a895 | -6.22163 | -42.74891 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 527f79c6-8570-3eb6-adbf-1967c798a264 | -6.54489 | -44.10286 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e83859bc-610b-3f26-949f-1ccc8235ffaf | -6.16775 | -43.33063 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a498af2d-eb0b-3a66-b53c-c529608e76ed | -7.15444 | -44.90572 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c63cbe68-318b-3825-9539-b6df75a6fc03 | -6.13061 | -43.30281 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 55e46020-5651-3a02-9ff2-3105a8824f50 | -5.54728 | -42.64114 | 2025-08-30 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0095f78f-8e07-3fd4-b6cc-4b2506ece2f1 | -4.79759 | -47.26533 | 2025-08-30 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b0f059d-69d5-3122-ad61-95cdcd9d5b28 | -8.05518 | -45.41059 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 85eadec0-d158-3251-9d60-bc53e583231f | -6.32062 | -43.79484 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc3e8c97-92ba-3512-8fb5-16fe25bd837c | -5.18582 | -43.12584 | 2025-08-30 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 870ef086-4178-3b64-8e32-56eb3216e7b1 | -6.41063 | -45.59296 | 2025-08-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90b8ea11-6c10-395a-894b-2db81aee9df2 | -5.73021 | -43.94028 | 2025-08-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ee4557da-27b4-3c28-8336-3178031a95d3 | -7.09426 | -44.3103 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a66e6156-a82a-3f2c-bde0-f5fcd385bcd9 | -5.7215 | -44.28011 | 2025-08-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e696f595-1a86-37f4-9441-c9917468eb5d | -6.21993 | -42.76017 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9d3072eb-ebc6-39af-b19e-1de793b4b85a | -6.66718 | -44.38895 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 201560f3-aacf-37b9-a4a3-822410a2a34a | -7.09613 | -44.53865 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87158a89-eca5-3659-a683-d1abee8a8b73 | -3.42485 | -49.04823 | 2025-08-30 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d002743-ef1c-350e-bec6-b5096ace86ae | -7.72527 | -50.27211 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 63dc6117-1514-3bc2-b17a-6f5dd50c7f18 | -7.1736 | -44.86975 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1ed5743b-4ae3-3ce8-9f7b-a652484b207d | -7.84845 | -46.9656 | 2025-08-30 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e5fd933-75ad-3ecc-97d4-d7ed3c9f3f7b | -7.60042 | -42.72197 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8bad3664-c813-336f-aaba-97b25bd30a29 | -6.49741 | -43.5318 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63ec67fb-ff22-3d19-9f6b-9bc83ad903af | -8.05464 | -45.41405 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5fb33333-add9-3bec-9094-fa178dc5b557 | -6.93779 | -46.17487 | 2025-08-30 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd98d72f-5e94-336d-9167-5fddf9eeafd3 | -6.53209 | -42.98983 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 161d0514-c5f7-3f27-b6f3-3bb28a6a620f | -6.05891 | -46.09428 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7bd4e26-5fa0-32a5-84cc-8e1c4ff7d183 | -7.72003 | -50.27844 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f61c0c6-a8e4-36b8-ba2d-ac7350f877d5 | -6.27492 | -44.46292 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 206d8d87-06c6-325c-a72f-63e2dbba2698 | -6.25216 | -43.37653 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 039f7fe9-07e2-3e40-aedc-c2817ed4edbe | -5.74974 | -43.83604 | 2025-08-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75551506-fe3c-3e8b-9080-357d1268a8cf | -7.71941 | -50.28204 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eebebdb9-f959-3d2c-9c7a-94331dc1102e | -7.95836 | -46.38909 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1216d10e-f592-312e-ab69-d39f5270fe87 | -6.17842 | -43.32858 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 23b17de0-3545-3ca6-9a76-515a75b3352a | -7.9046 | -45.87131 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 260fb76e-2bd5-3632-9be9-66960a0155ae | -7.01554 | -42.01755 | 2025-08-30 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6a08990f-231d-3e6a-8bf3-5c3a70d5221d | -8.10863 | -45.00384 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25e64fef-3256-3e66-8a09-583b3f0421a9 | -5.58599 | -46.32954 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cb90960-8701-3e94-8abf-cd2434f50745 | -6.29198 | -44.46204 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 121e1723-db60-36ee-adec-14f8bfaeda2b | -6.53341 | -44.57041 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b462bcec-4ec1-3cb5-a75f-bba6a6c27d1f | -6.91312 | -44.38152 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6412534-a532-3e49-8c7d-62f7c36e3f14 | -7.11262 | -44.58736 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c22d20c0-b103-3661-abea-5130071888fb | -6.48619 | -44.39286 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5169c2db-4c7e-3112-8967-0d1f0cb13c63 | -6.87967 | -44.44395 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52e1d033-1270-3ef1-a3bc-d99013b78369 | -6.17238 | -44.18035 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e731e2f-f703-3742-a63e-8465dcccff88 | -6.02914 | -42.81594 | 2025-08-30 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ace20fa7-074e-38db-9e8b-237e60b3399b | -5.69673 | -45.13465 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a55a54ca-d6c1-3545-abf1-fe22a6d3c02a | -6.06261 | -44.7755 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 82c4e6bc-40f5-3044-8586-3027b5f50f2c | -7.90129 | -45.87078 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98b0251d-388d-3937-9aa0-d9504a6817a8 | -6.28207 | -44.46049 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58021843-5922-35e3-842a-83d2c1d6132d | -7.15336 | -44.91263 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e41a9065-9c4e-3901-a943-09ed321e4b59 | -6.65903 | -43.93734 | 2025-08-30 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README19.md)
