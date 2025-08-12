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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99c2f0fd-00b2-3a51-8dc4-f1a6f7483a09 | -8.52165 | -43.32521 | 2025-08-12 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dbf2a7cb-34dd-3f17-926a-5e8e46316d74 | -7.23212 | -41.90778 | 2025-08-12 03:17:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ab5911e5-0d7d-38ac-b0c4-8a9ca66f59a4 | -9.33153 | -37.9802 | 2025-08-12 03:17:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 32cc42c2-cbaf-30f2-8d79-edef6d84a929 | -7.20888 | -35.5959 | 2025-08-12 03:17:00 | NOAA-21 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 46af99ab-5b30-373b-8927-b10b715c5709 | -7.23101 | -41.91362 | 2025-08-12 03:17:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d9508839-cc73-3aec-bd58-ddd1314b41c3 | -9.331 | -37.98306 | 2025-08-12 03:17:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5e0ffb2a-7758-332d-a18f-6b61276c98cb | -8.51594 | -43.3171 | 2025-08-12 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| a81b27ff-4b27-3404-8746-b6733269938d | -8.52297 | -43.31843 | 2025-08-12 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 30ea449f-5102-3ce3-bc99-65ca54b2559b | -7.30233 | -39.64135 | 2025-08-12 03:17:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 786b463c-47fa-3f9e-96d0-1cd0958e3820 | -9.33115 | -37.98163 | 2025-08-12 03:17:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 68ee83fc-b219-3d23-bea8-945e72e36c53 | -7.2336 | -41.91295 | 2025-08-12 03:17:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 51c41eef-d4ad-3ecc-a91a-bce7c7e869e9 | -9.33064 | -37.9845 | 2025-08-12 03:17:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 65f5741a-5184-354f-a359-c784d8b63b56 | -8.51892 | -43.32581 | 2025-08-12 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 71a98e51-fd1c-308e-863d-1140a76ec88a | -7.30234 | -39.64486 | 2025-08-12 03:17:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d1972227-d4d0-3d5d-b6f7-98af6ea6a86c | -8.51726 | -43.3103 | 2025-08-12 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 610f251b-800a-365c-a6ff-501813b35f39 | -8.52429 | -43.31163 | 2025-08-12 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5e8cb3ef-77fd-3e66-859e-76321279a83c | -8.52165 | -43.31228 | 2025-08-12 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c54bf6e2-7f7b-35e0-8fe8-6c4adc28745d | -8.52029 | -43.31905 | 2025-08-12 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 9e69da1d-5526-3fd2-8574-62e951f9d779 | -17.57263 | -45.32927 | 2025-08-12 03:19:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e656d9eb-f94b-368a-a3c3-f2f1cd30c6c4 | -17.9635 | -44.29701 | 2025-08-12 03:19:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7328ca1d-7643-3bfe-b569-089b8ef898d9 | -17.56598 | -45.32739 | 2025-08-12 03:19:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b5f11e38-b256-308f-8b0a-3762642a74a4 | -17.56454 | -45.33366 | 2025-08-12 03:19:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2b444b3e-2963-33d2-b492-8b858b35cfb0 | -17.57124 | -45.33535 | 2025-08-12 03:19:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16597877-05f9-360e-9a9c-927eca9e8c89 | -16.00742 | -43.2761 | 2025-08-12 03:19:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d05cd1d-e737-32e5-be1e-10535a86b621 | -12.04456 | -40.29503 | 2025-08-12 03:19:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8fc1419c-da60-3212-82b0-fdc1f464b5bf | -17.56751 | -45.32895 | 2025-08-12 03:19:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 575d4382-8818-33f6-8a93-71181a867b8b | -13.96358 | -42.58424 | 2025-08-12 03:19:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 246b95ae-8a03-3e5f-9460-71d771c1a451 | -17.56604 | -45.33516 | 2025-08-12 03:19:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| cdddb38b-1be7-3419-a0d0-4ecdeba32b2a | -12.9972 | -44.89373 | 2025-08-12 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fafa0c4-f8f1-324f-bc94-4dcfa5e5871d | -17.96217 | -44.30283 | 2025-08-12 03:19:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 09d5be67-db83-397f-99da-234cbb9cc475 | -12.99879 | -44.88641 | 2025-08-12 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c64ed992-39f1-36a0-b958-7a7446daf8ba | -12.98463 | -44.88305 | 2025-08-12 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22eb8700-043d-3fbd-bca8-490d563fe5f7 | -12.5738 | -47.0232 | 2025-08-12 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| fb1e1c52-a691-3e60-a49e-bb408d33615c | -16.2957 | -52.923 | 2025-08-12 03:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 046cece5-9ddd-3bc2-a85f-6eb726e7d637 | -8.9401 | -60.7288 | 2025-08-12 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ebf18729-24da-39e4-96a8-c2e55c2d3792 | -7.1299 | -60.1182 | 2025-08-12 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 6259a31f-4ee3-303e-b7fc-7a543c1f1c38 | -12.555 | -47.0034 | 2025-08-12 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 26d28a60-c90d-3e15-8b00-28375bba9c86 | -12.5546 | -47.026 | 2025-08-12 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| e16b9dc2-11a1-354a-8754-5486f417d690 | -7.1482 | -60.1366 | 2025-08-12 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 840bbcc2-4061-3ecd-a82b-e4aed5c537e3 | -9.7041 | -49.4825 | 2025-08-12 03:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 493419b9-2ea3-3950-bcb9-53c7199b61b3 | -17.6349 | -46.6799 | 2025-08-12 03:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 9c0ef8f5-0710-3c1f-a4f4-4c5db8e7bc35 | -9.723 | -49.4806 | 2025-08-12 03:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 905bc138-2b01-30e2-85e6-c3c5b0ae36d0 | -17.6544 | -46.699 | 2025-08-12 03:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 084d05c4-741f-3af1-b1be-49c4adfa28da | -8.5211 | -43.3063 | 2025-08-12 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 08aeb51e-ecfc-3ed5-b5af-e4222d9f1ad2 | -17.6549 | -46.6757 | 2025-08-12 03:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 660.8 |
| 2a9eb424-8248-3448-a095-112d047be617 | -17.6749 | -46.6715 | 2025-08-12 03:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 198.6 |
| e080a711-4867-3f22-8059-c228d4ef20f0 | -17.6555 | -46.6523 | 2025-08-12 03:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 3fe0f984-bac3-30ec-9e70-e3e2262ed989 | -17.6743 | -46.6948 | 2025-08-12 03:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 1ae60b2e-1935-3f99-8c4c-35be57c6a8ae | -12.5746 | -46.9781 | 2025-08-12 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 4ca47f6e-7c35-3d23-ad27-090156759537 | -6.5856 | -44.564 | 2025-08-12 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0adfd037-f6f0-31e8-b0c6-fd0e4cb4ef9e | -12.5742 | -47.0006 | 2025-08-12 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 348.1 |
| 8d579e37-8e6f-3b8e-a135-d57de966046e | -16.2961 | -52.9016 | 2025-08-12 03:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 459e1f0d-e083-3159-b24e-1f443db46d79 | -7.1483 | -60.1174 | 2025-08-12 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| ce48da69-c42e-3bec-8bbb-1554e244c6a2 | -7.1298 | -60.1374 | 2025-08-12 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| cbe70d7f-6dcd-3919-bca7-ef7afb2b16cc | -21.24469 | -46.71934 | 2025-08-12 03:21:00 | NOAA-21 | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a544f6d8-7956-3314-8f7a-2168589bb7c2 | -23.07999 | -46.98479 | 2025-08-12 03:21:00 | NOAA-21 | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 7671fef1-0889-33e7-b93c-bdf65fb339f5 | -21.2435 | -46.71875 | 2025-08-12 03:21:00 | NOAA-21 | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d33f4811-ea8a-360e-88e2-e0851d314b5d | -21.27023 | -45.26594 | 2025-08-12 03:21:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d73aa461-6ead-3eda-b73f-02184c13d6fe | -19.71828 | -46.22802 | 2025-08-12 03:21:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7bb3cfb0-89f5-3ba1-ae34-d9932fc7266d | -22.71588 | -43.23849 | 2025-08-12 03:21:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8c489105-6d66-385e-915e-982479e7c210 | -20.42881 | -46.49279 | 2025-08-12 03:21:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90e2763f-b2f4-3759-b6e2-76f9b55e503c | -19.33547 | -44.4213 | 2025-08-12 03:21:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f23c8b02-40f0-3a34-a5e1-1823f309be85 | -23.0815 | -46.97871 | 2025-08-12 03:21:00 | NOAA-21 | LOUVEIRA | SÃO PAULO | Brasil | 3527306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e90f4cf5-da24-3ef3-8e94-00a3f0d3b0c8 | -21.99297 | -44.88136 | 2025-08-12 03:21:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e0d1f09a-08fa-3d09-81ea-8f869d8b8d9d | -23.07714 | -46.9818 | 2025-08-12 03:21:00 | NOAA-21 | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 7b204513-d7d8-329f-9bb7-0a8c5ace576b | -9.723 | -49.4806 | 2025-08-12 03:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 4de35662-85d9-38c4-9c9b-b5daa11c0600 | -12.555 | -47.0034 | 2025-08-12 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| d15f75f3-95d4-3449-9ab6-027e4e8663f9 | -6.5856 | -44.564 | 2025-08-12 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 3128babe-83cb-35c1-8dd6-592a75ae1ec2 | -8.9401 | -60.7288 | 2025-08-12 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| dacf462d-31a8-3ea5-8e50-e17c54d35e36 | -7.1483 | -60.1174 | 2025-08-12 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 06490972-205c-39cf-9b5e-3c18be7abb29 | -8.5788 | -54.7162 | 2025-08-12 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| c8a61877-2fbb-3748-8e3b-eb1f3f3cb609 | -7.1298 | -60.1374 | 2025-08-12 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 07fafd6f-9792-39ec-98f2-be03b0dee387 | -8.5211 | -43.3063 | 2025-08-12 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| e0a3c364-705a-388e-a38f-c400b329553d | -6.5858 | -44.541 | 2025-08-12 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 61e4dc67-da69-37c6-a94f-69ed7d4bcd69 | -12.5742 | -47.0006 | 2025-08-12 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 28a99107-c5fc-3823-b84f-e60f46c8d756 | -16.2957 | -52.923 | 2025-08-12 03:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 733ac483-5fd5-3ee8-ad2d-5706f7b51706 | -7.1299 | -60.1182 | 2025-08-12 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 991f07a1-d303-3f85-9fd6-608aca28fad0 | -12.5746 | -46.9781 | 2025-08-12 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| d875e94d-e283-3349-ae69-bb4bbab9a5e0 | -7.1482 | -60.1366 | 2025-08-12 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| d16cdc8d-1aab-34f1-adf8-2d1d0b031dfe | -16.2961 | -52.9016 | 2025-08-12 03:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 2f89eb6e-4a17-3966-a86e-67d739c15724 | -7.1483 | -60.1174 | 2025-08-12 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 4d0b1936-72ea-3ea9-ab59-c81298ca1a9a | -7.1298 | -60.1374 | 2025-08-12 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| d246b7fb-c7f3-394a-97bf-ec2e3e3f788d | -16.2957 | -52.923 | 2025-08-12 03:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 507b0b88-8223-3102-9973-a6fc2ac1dc12 | -23.0038 | -49.0309 | 2025-08-12 03:40:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 678270ba-9927-3ab6-af80-fefd2b8fd1ad | -9.723 | -49.4806 | 2025-08-12 03:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| ff57413f-60a5-3d33-8d89-4df93b53ab83 | -16.2961 | -52.9016 | 2025-08-12 03:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e057ab6f-33e8-35df-a15f-61c78048eaf5 | -6.5856 | -44.564 | 2025-08-12 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 8df8e04e-3f22-3b47-9f50-30519ad973c1 | -3.9684 | -47.8901 | 2025-08-12 03:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 5f5ad4ac-61cd-33ba-84d7-8f1b3282dcbd | -7.1299 | -60.1182 | 2025-08-12 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c0047945-1b68-3834-b02c-2c5c9e02974b | -8.9401 | -60.7288 | 2025-08-12 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 249e3c36-58d7-3245-926d-a4b8b010ecc1 | -22.9828 | -49.0361 | 2025-08-12 03:40:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 7a335a7d-45fe-3129-85b3-2d87ec30fe2f | -12.5742 | -47.0006 | 2025-08-12 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| e39d34ae-59f1-3d55-ac5a-a686cd44dd95 | -7.1482 | -60.1366 | 2025-08-12 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 5bf3bdfe-9ff5-3907-bf49-3d010e2008fb | -22.9835 | -49.0126 | 2025-08-12 03:40:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c419c4c7-2355-392d-b8d4-080713b8a813 | -8.5211 | -43.3063 | 2025-08-12 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 2acd255c-ba8a-337c-80c0-bf383f752997 | -12.555 | -47.0034 | 2025-08-12 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 044c3143-48df-3b3e-8d36-35a4e66f8561 | -3.0707 | -40.81714 | 2025-08-12 03:42:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7d88bb47-d0ef-3aca-85e6-51b608814c3a | -3.05979 | -39.89508 | 2025-08-12 03:42:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5fd797c5-5827-3165-95a9-735f264a2c60 | -6.58045 | -44.56335 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4e33c8e-444e-3861-8555-4722d80f1e5f | -6.57982 | -44.56688 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README8.md)
