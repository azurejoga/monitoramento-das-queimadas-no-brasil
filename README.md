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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 447ad275-5ada-3af2-8536-021d851a3613 | -7.6113 | -45.2026 | 2025-08-11 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| ad7da260-1bfe-3156-a112-c7c05125d94a | -7.6301 | -45.2009 | 2025-08-11 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 01f5e44e-bc73-381c-bc18-d1cb35bc64a1 | -8.9215 | -60.7297 | 2025-08-11 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| d8e043c7-c591-3c54-99d8-1b101663bfef | -3.4254 | -49.0517 | 2025-08-11 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5af8644d-da4d-3326-aa48-8c2737ea58af | -6.5856 | -44.564 | 2025-08-11 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| d99b0016-9243-3354-bd63-a2c57680eac3 | -8.9213 | -60.7489 | 2025-08-11 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 104efcd4-3eeb-30c5-a203-8839270a2b5d | -7.0614 | -59.1972 | 2025-08-11 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 173.9 |
| 20719967-9581-30f1-ae52-2ece545f477d | -7.6115 | -45.1799 | 2025-08-11 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| eb0c6af8-ba08-3041-a287-88aefe3e8fb7 | -7.0799 | -59.1964 | 2025-08-11 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 197.9 |
| 3c914383-03b8-3298-be7a-e87460c0df18 | -18.8428 | -48.6592 | 2025-08-11 00:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 1c9a1809-bea2-31e9-b3c6-046fc35ab739 | -9.3806 | -61.5315 | 2025-08-11 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| e4b0b3ec-7e8d-3d93-8d52-947f9fdcc0d7 | -6.5858 | -44.541 | 2025-08-11 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 46d26092-2439-3f52-bfed-7cb6832d8262 | -8.9401 | -60.7288 | 2025-08-11 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 98a93795-63dd-37b4-89ba-7d04b28d2efb | -8.5604 | -54.6973 | 2025-08-11 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 2577ff31-1b5a-3469-b93b-d292a13969fc | -7.0797 | -59.2157 | 2025-08-11 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 57ea47af-6f6b-3152-9aba-cae81e0c9b42 | -8.579 | -54.696 | 2025-08-11 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 614bf585-f359-3165-9f4e-12426a6075ae | -7.0613 | -59.2165 | 2025-08-11 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.6 |
| dfa6054e-13e1-388e-bc66-d9d4c059c956 | -8.9399 | -60.7481 | 2025-08-11 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| dde70ab5-f540-34cb-8f9b-e1459cdcc57a | -18.6293 | -46.8394 | 2025-08-11 00:00:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 7e1fec58-330a-3efa-b89d-dafb33e87e5a | -6.5668 | -44.5655 | 2025-08-11 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| dcdd09a1-b6ef-3e11-b20c-d282058725a7 | -5.4851 | -44.3764 | 2025-08-11 00:05:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65086c29-f77f-306c-838a-7adc9f9871a5 | -6.2897 | -43.702499 | 2025-08-11 00:05:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba17a305-7384-30f4-abcf-2f1a102b7643 | -9.651 | -43.823502 | 2025-08-11 00:05:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c75fbb39-8ca7-3ef6-92db-5838a3395b1a | -6.5795 | -44.558899 | 2025-08-11 00:05:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d704b94-37d5-334a-a1c5-98afc0aa2eec | -18.626301 | -46.8428 | 2025-08-11 00:05:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6e84c533-92d4-3539-94d0-3c390d3d58f5 | -11.4482 | -42.221199 | 2025-08-11 00:05:00 | METOP-C | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1d8290fe-6075-384c-893b-2392de27d897 | -13.0058 | -48.374298 | 2025-08-11 00:05:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46f4885d-3517-39a7-83ad-24a89c2aea7c | -11.4462 | -42.2113 | 2025-08-11 00:05:00 | METOP-C | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d30b5783-0b95-3bb7-a3ca-a33cb01e8752 | -6.6585 | -40.921001 | 2025-08-11 00:05:00 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 91b1fc8c-3a5f-3232-a37d-289b5964a2bb | -4.7755 | -42.662899 | 2025-08-11 00:05:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3d3fcf1b-7512-3b4a-a8e8-cb2e5c014a31 | -3.4241 | -49.003399 | 2025-08-11 00:05:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 317c4916-6c91-391d-b685-52d606d6bd5b | -18.845501 | -48.631802 | 2025-08-11 00:05:00 | METOP-C | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e8f06924-7113-3f14-8850-31b90b847a09 | -6.6569 | -40.913502 | 2025-08-11 00:05:00 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7e66cd23-f280-3a41-bd82-205c60afb32d | -7.1327 | -39.460499 | 2025-08-11 00:05:00 | METOP-C | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4d5c97aa-cbd3-3f79-bf1f-099a06a7336f | -6.577 | -44.5471 | 2025-08-11 00:05:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24e02e75-894a-3abd-9883-ed61f8ee6ed1 | -3.4027 | -39.159302 | 2025-08-11 00:05:00 | METOP-C | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 00bff7a3-35e6-3d90-b37a-cece793a5ad4 | -6.5744 | -44.5354 | 2025-08-11 00:05:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11174395-e2cd-38a5-941d-f90f7cfcfe71 | -3.4042 | -39.166199 | 2025-08-11 00:05:00 | METOP-C | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d289c374-331d-390c-9640-a939f62494ea | -13.0155 | -48.372501 | 2025-08-11 00:05:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca37698d-4ecc-3b62-b3f4-33bef85e0d6d | -9.8639 | -43.526501 | 2025-08-11 00:05:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47625a66-e38c-3e97-a8ff-10f015416117 | -4.3523 | -40.153801 | 2025-08-11 00:05:00 | METOP-C | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cb730565-48b5-3524-9413-8e50e422f486 | -3.4191 | -49.026798 | 2025-08-11 00:05:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d011b7ef-4fb5-3a2b-841b-38c26d467a2c | -3.4144 | -49.005501 | 2025-08-11 00:05:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 282bf0de-2567-332a-8a26-3789fde1859a | -7.1342 | -39.4674 | 2025-08-11 00:05:00 | METOP-C | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 53dc9451-6065-3e4b-ab06-9362f88e004d | -9.8663 | -43.5378 | 2025-08-11 00:05:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80fc454a-0a07-3ce2-8dc7-a92cb604dd80 | -4.1068 | -48.182201 | 2025-08-11 00:05:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aed493ea-df0a-3d1c-aecf-970c2bde971d | -13.0105 | -48.345501 | 2025-08-11 00:05:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4d4150e-1d1e-3afa-8945-53299b7f2863 | -18.323799 | -43.6763 | 2025-08-11 00:05:00 | METOP-C | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e727a88f-b355-345e-8d3a-f7112655f888 | -6.5867 | -44.544998 | 2025-08-11 00:05:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3b9923d-3b8a-37b1-a9c2-c51dc6969337 | -11.9556 | -43.379299 | 2025-08-11 00:05:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f41e9c0e-fa75-3a78-8e61-d879a78f63d0 | -7.1311 | -39.453602 | 2025-08-11 00:05:00 | METOP-C | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6eb3ebf5-3768-314b-8b2d-951b5f35de68 | -13.0008 | -48.347301 | 2025-08-11 00:05:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e920155-56d2-3fb4-b026-feab0c5c3904 | -3.4288 | -49.0247 | 2025-08-11 00:05:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b457b36e-d24c-3cb1-837d-25ed2c8f9af4 | -5.4875 | -44.387501 | 2025-08-11 00:05:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc4223b2-0e0f-3803-b24c-4c0d04a4c697 | -6.5841 | -44.533298 | 2025-08-11 00:05:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b6b022a-b468-34cf-8a77-7056f1d911bb | -18.622 | -46.817101 | 2025-08-11 00:05:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6da5b2ef-4eba-3803-9baa-6835a9296b77 | -8.9399 | -60.7481 | 2025-08-11 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 5b668892-d2c5-3111-86b0-0b20ae020139 | -7.0613 | -59.2165 | 2025-08-11 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 7b4224f5-4ce8-363f-a337-35bee98bc85f | -18.8428 | -48.6592 | 2025-08-11 00:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 97.1 |
| ad99a77b-747c-3703-ac94-090c4da0b93f | -9.3806 | -61.5315 | 2025-08-11 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9e5901d0-55a3-3803-9058-fa6bfdc0d36f | -18.8422 | -48.6821 | 2025-08-11 00:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 61fc98d5-a630-3801-a09b-720052cd9655 | -21.0536 | -50.0356 | 2025-08-11 00:10:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| ff70da75-eca3-3e59-9365-1147918dce98 | -13.0097 | -48.4104 | 2025-08-11 00:10:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9e114021-31cb-3101-91c1-20639a36190d | -7.0799 | -59.1964 | 2025-08-11 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 198.8 |
| c0394d95-12c8-37e0-90cf-76677e1f75df | -7.6113 | -45.2026 | 2025-08-11 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| db185d34-6aff-3269-85fa-dc4130eb8be2 | -21.0542 | -50.0128 | 2025-08-11 00:10:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.9 |
| 9d3ba742-6995-379f-8250-436893147296 | -18.8629 | -48.6551 | 2025-08-11 00:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 102b4e21-5eba-3801-9f7c-2be12460f1b0 | -18.6293 | -46.8394 | 2025-08-11 00:10:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 7edd6e3a-cbc7-3428-a691-0b5e66bfd627 | -8.9401 | -60.7288 | 2025-08-11 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| ea55c33c-b37d-310a-b1c1-204abbea7f2f | -7.0614 | -59.1972 | 2025-08-11 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 95f5d07f-d513-3b87-93a7-6ed717757f1a | -18.8623 | -48.678 | 2025-08-11 00:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 58.7 |
| b10301fb-b162-390d-b535-c06319ec8710 | -8.5604 | -54.6973 | 2025-08-11 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 057bd482-0fcd-3166-a4a3-5c93a89b4aeb | -8.579 | -54.696 | 2025-08-11 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 969f5de1-f086-3923-adb8-81a6ad235de2 | -8.9215 | -60.7297 | 2025-08-11 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 314da5b5-dd9d-3b4a-a4e3-4cd68fa97f5e | -8.9213 | -60.7489 | 2025-08-11 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 5691423c-9ea1-38ea-ba92-996107ff6658 | -13.0101 | -48.3882 | 2025-08-11 00:10:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 7b6f7df8-fcae-3cab-a4bd-71b0f0500d6b | -7.6115 | -45.1799 | 2025-08-11 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 9fd69487-5ac0-34fa-9873-ac8804930e29 | -7.0797 | -59.2157 | 2025-08-11 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| cc2b24e7-a220-3003-8d51-d920cb3e3ce1 | -18.8422 | -48.6821 | 2025-08-11 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| b023c90d-7747-319c-9288-c5e536098f28 | -8.9399 | -60.7481 | 2025-08-11 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| f3dca438-2fbc-3ef2-9401-e2159b9dac08 | -9.3806 | -61.5315 | 2025-08-11 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ee3342e6-5cbc-3cf8-9eda-cc6ca5b9c3b8 | -8.579 | -54.696 | 2025-08-11 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| b29647e9-45cf-3de0-be93-c902cba26f02 | -18.8623 | -48.678 | 2025-08-11 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 3713ab5a-79f2-3bc8-8c2d-a571d489bf09 | -8.5604 | -54.6973 | 2025-08-11 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| d37907dc-6f70-3b72-aef7-4ef3cf90d9a2 | -18.8629 | -48.6551 | 2025-08-11 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 136.2 |
| af1e612d-8cca-3f3f-a057-51a131029160 | -21.0542 | -50.0128 | 2025-08-11 00:20:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.6 |
| 69fdea34-9b20-36ee-a78b-7b652a970ae4 | -18.8428 | -48.6592 | 2025-08-11 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 964dd443-1caa-3481-9558-c8a26cd0e744 | -8.9215 | -60.7297 | 2025-08-11 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f0ba0565-7cc9-3845-95d6-39f94224013e | -7.6113 | -45.2026 | 2025-08-11 00:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| f56dbc32-3e10-3d24-9218-3fb6c355b5aa | -7.0799 | -59.1964 | 2025-08-11 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 164.4 |
| 1b02d246-006d-3e58-a57c-cf3b5019c3bc | -8.9401 | -60.7288 | 2025-08-11 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| c2471902-daa2-326c-8d9d-c29cb3a95c68 | -8.9213 | -60.7489 | 2025-08-11 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 6cf9ec67-5cb9-3308-92bf-1849f1f42ec3 | -7.0614 | -59.1972 | 2025-08-11 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 374c30b7-0b1b-3f6a-ba5e-bbbdefc5e796 | -7.0797 | -59.2157 | 2025-08-11 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| c0494d30-0b21-3bc7-9f6f-e6ad82953abc | -7.0613 | -59.2165 | 2025-08-11 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 3314278f-a403-30be-ad1d-f159f2778f20 | -21.0536 | -50.0356 | 2025-08-11 00:20:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| f61eedc3-224b-3042-93bd-cd3aa5db7266 | -18.6293 | -46.8394 | 2025-08-11 00:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| a92e3817-9969-3dcc-9d93-89fef39f0831 | -21.06171 | -50.03331 | 2025-08-11 00:24:00 | TERRA_M-M | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.3 |
| 282c0187-309f-313c-bfeb-4c35ccf0300f | -19.55914 | -46.58496 | 2025-08-11 00:24:00 | TERRA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9717161f-fa4b-3ffe-9acc-880c7e065282 | -19.41911 | -43.35986 | 2025-08-11 00:24:00 | TERRA_M-M | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |


[Clique aqui para ver as próximas entradas](README2.md)
