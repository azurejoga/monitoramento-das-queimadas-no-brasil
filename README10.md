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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4554b221-3335-3d7a-859e-b1586d987c79 | -8.73402 | -36.89685 | 2026-09-09 03:49:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d677635d-2d2f-3d16-871d-5d95ed36709c | -9.69235 | -43.51017 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23c1ad17-145a-34d0-a388-6c25e20d11f0 | -6.16328 | -44.65899 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 23d77507-0bd1-34b5-b6ad-be03df7f2d9a | -9.70192 | -43.45425 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| be5f9937-d474-3aa5-b62a-7a4f83a95fb6 | -5.83299 | -42.28103 | 2026-09-09 03:49:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 013bb739-368c-3142-abb7-3076368216e0 | -9.70989 | -43.40768 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f031a117-2b63-3ea3-acf3-abea8b1168a6 | -10.73208 | -46.01123 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 375441ba-cc5f-3ead-a4f1-900de6d5d3d5 | -7.1936 | -43.62174 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 30a19908-226e-3c3f-856e-5413793bb4d1 | -6.87094 | -46.01303 | 2026-09-09 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71f94164-ab30-3d30-a485-c53ef9098f8a | -9.69837 | -43.44968 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 62e62c04-c8d1-3e7e-95d7-dd853da979ab | -7.19833 | -43.62745 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dd09a1c-2c9a-39f2-9769-4a3dd933321f | -7.52364 | -45.92675 | 2026-09-09 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1c3239d-fe4a-31b3-8f9b-c1e1a4ccf76b | -10.74514 | -45.96763 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 68d9eb47-6c26-3b11-8900-e53c47373be0 | -6.75829 | -44.58078 | 2026-09-09 03:49:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b762b3a-0d9b-3a16-8f44-339c11cccba0 | -5.71601 | -46.19307 | 2026-09-09 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0db23d8c-c337-37f5-bd6a-14adc583d601 | -6.1602 | -44.6565 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 65fee409-8c53-3cc7-9a00-da6bd4b8ceb9 | -5.76526 | -45.07785 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| ac9ca4f3-ec84-36c0-93ac-8b8c39fe58d0 | -8.21797 | -46.01264 | 2026-09-09 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4a03620-0c49-33c0-8cdd-2d129fcb42c6 | -12.43658 | -43.41292 | 2026-09-09 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3513597d-766c-3d1f-9195-bdeaa7dca543 | -10.2304 | -44.63258 | 2026-09-09 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f324f2bf-da2f-3b7e-9ed8-49377ef4a21c | -5.77685 | -45.07064 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ddc6c18b-b945-36a9-a7a4-b2f68b925774 | -9.77551 | -43.50739 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e59ba5e7-ac70-3666-bc1f-5ad4b8546e9a | -9.72064 | -43.47357 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be518c23-e0a5-3590-a9ca-62df38206927 | -5.83777 | -42.27791 | 2026-09-09 03:49:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b323212c-771f-3485-bbf1-bbbff54ff653 | -9.70679 | -43.45112 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a9f3c57d-39e1-3c3a-8175-3f1092a6a644 | -8.84432 | -36.53337 | 2026-09-09 03:49:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e71e01b0-4824-39a5-b263-f2919aa7c5a7 | -6.0338 | -42.63841 | 2026-09-09 03:49:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ae1728ef-dcf2-362a-9823-54f6a16978d7 | -7.19438 | -43.61728 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 69d37124-bf9c-3287-a925-1b15b6261fcb | -9.77812 | -43.4673 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36bfae18-ec4d-3f14-b34f-918da1734e37 | -9.69575 | -43.49031 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82de9c92-b522-378f-8efc-ab5bd6e18068 | -9.25844 | -45.6523 | 2026-09-09 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bd5cf4d-c0db-315a-abfe-25cacb4b8f6a | -11.00073 | -45.08039 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1143789c-2e12-3ce0-903d-f452a0c36d72 | -6.83167 | -39.4085 | 2026-09-09 03:49:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ff41b16-3be9-3dcc-ab8d-48a94f47a03d | -6.86573 | -46.01191 | 2026-09-09 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 586ec035-8490-3a73-bfba-c96888fc5030 | -9.69482 | -43.44517 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fffd4c5f-03fc-3575-8fc5-654154984ae5 | -5.77635 | -45.07353 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3c6f665a-7ff4-3f36-a040-0b09fd2d08b6 | -10.1734 | -36.30452 | 2026-09-09 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6caee212-8ff2-3078-ade5-ad507a2e1b6c | -6.37142 | -43.59244 | 2026-09-09 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26a065d2-9e2b-36ae-b56c-08c554f67e0f | -6.15937 | -44.65279 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8924b715-6ad8-3f92-86b3-10b9ae578d01 | -9.72507 | -43.4711 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dd96c11-47b3-3adb-9e38-0d5e792445d9 | -9.77905 | -43.51207 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 323ca478-56b2-3a80-9f43-d33f3f6c9851 | -5.83009 | -42.27287 | 2026-09-09 03:49:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| da8d3465-2504-3bcc-93b3-c31c7fae95fa | -5.38051 | -49.14941 | 2026-09-09 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc810aec-3688-3cd8-832b-0d05065985f1 | -12.49879 | -43.77288 | 2026-09-09 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0efe49f8-8c09-33a5-849a-5ceb645ab379 | -10.58841 | -45.74652 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ced7c930-335e-3051-bff0-f828d5ded665 | -9.70472 | -43.46326 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00c9f6f6-771a-388c-9121-b8383990526c | -5.83487 | -42.26978 | 2026-09-09 03:49:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 89c7022c-c921-3f1f-b376-80ea4e07b61e | -9.69778 | -43.4785 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0b062920-7b7e-32f9-8046-a3ff111b0e6c | -9.7625 | -43.40796 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8c5d341-0608-3727-acc2-90721d5d15b7 | -9.06005 | -45.77708 | 2026-09-09 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b2f6c37-ba9a-3db5-b09c-613475b1bbff | -8.42149 | -46.89194 | 2026-09-09 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 895ccb3f-9b01-3e72-ad46-43bf0be33d61 | -6.0325 | -42.64631 | 2026-09-09 03:49:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e52c15ef-115c-38dc-8063-072dcf1f1c9c | -6.3662 | -43.596 | 2026-09-09 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 4f0e9431-99b0-3b80-a06f-2742e0351215 | -8.09213 | -45.68165 | 2026-09-09 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e4b4872-f59f-3186-ba09-60ce506e934d | -7.20057 | -43.61402 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c67de455-f074-333b-80c7-0477259d4590 | -6.16421 | -44.65366 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| fd0fe3f6-27bd-30a7-b581-bfb588efd525 | -11.30914 | -37.58762 | 2026-09-09 03:49:00 | NOAA-21 | ARAUÁ | SERGIPE | Brasil | 2800407 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 42ded731-4bec-331b-8264-0c200612242a | -10.97098 | -43.10112 | 2026-09-09 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 522975a2-789c-37a4-a49b-17b38e32eee8 | -9.69415 | -43.44905 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 25fd2860-547f-337a-ab7a-b0e2b979ad8e | -9.05361 | -41.12236 | 2026-09-09 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 377f932a-573f-3b26-aaa5-fff8aa01af44 | -9.77526 | -43.45878 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f72ad435-124c-30bd-8dd8-082e53cae349 | -6.36173 | -43.59511 | 2026-09-09 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5501740e-4be8-371d-84b4-48c82f2432ce | -10.17002 | -36.304 | 2026-09-09 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 83825150-1c46-3ef4-bb0b-8616ccfe44a1 | -8.0992 | -45.67099 | 2026-09-09 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 94af00cf-a416-3256-8620-074f9a2cb08c | -5.83362 | -42.27724 | 2026-09-09 03:49:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3750c062-140e-3b75-b9c9-8bd972cd738d | -6.86051 | -46.01082 | 2026-09-09 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 097836b8-4734-39a0-a1e9-28132d5894c4 | -9.70922 | -43.41161 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8bdb9907-ef54-3081-bfe5-25a4bd199309 | -9.77129 | -43.50668 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ab14de2-ab93-32af-b628-b060b442c66b | -8.09868 | -45.67389 | 2026-09-09 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5eeeb0a2-624e-3625-a813-7433c3fad450 | -7.19804 | -43.62245 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ff35c24-1a20-3c0c-baeb-ac55bf10b5ab | -7.19388 | -43.62673 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9d3c90a2-37ab-3421-99e7-cddc13f04f05 | -9.69643 | -43.48636 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b54fa806-3a3a-3b5c-bcf0-d6db0aa839b2 | -10.72376 | -46.05655 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 60f115c5-7396-38d0-99e8-7093b7f179cb | -7.19019 | -43.62152 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3c94c5c2-ccda-3e1d-abf1-ad334662fcc4 | -9.70101 | -43.43431 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 36390027-d1e8-34ee-9f12-927c82f4174d | -8.09161 | -45.68455 | 2026-09-09 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48a5719d-c15f-37ae-96bd-440f63a881df | -11.48158 | -42.24122 | 2026-09-09 03:49:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 50ea182b-1985-32fa-9ef7-913e21e6fbaa | -6.16109 | -44.65113 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 14d8760e-7474-35ae-8994-85a0032d06c2 | -10.36613 | -45.1707 | 2026-09-09 03:49:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad8f86ad-b107-36f0-83a6-f82cb32d13c1 | -9.40808 | -41.18207 | 2026-09-09 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 614a2122-624b-35c1-9b2e-88af57dee22b | -9.78165 | -43.47192 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9aaf0f0e-0974-3317-a6ad-c4d9afb1ba60 | -9.77594 | -43.45488 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3e03e67-98c1-3dd2-aa68-cfe1fc1c6cab | -9.76602 | -43.41256 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4183a583-0c81-39d1-916e-74d25c8d11c9 | -9.77061 | -43.51062 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 077e4f02-3270-3e3b-b078-58013e7ac924 | -9.7057 | -43.40696 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e4583a29-912d-3552-b97e-723fc9a107f2 | -8.73071 | -36.89634 | 2026-09-09 03:49:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30ac8f74-1387-3e77-ae89-9ae1c94df9a3 | -10.73697 | -46.01221 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 088e3f71-937a-3f1f-84b6-6c16e9c1d68d | -7.26309 | -45.35499 | 2026-09-09 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06ce6bab-6460-3ad1-88fc-5e1eba7830fa | -6.15844 | -44.65813 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b5bd1952-ae8e-3cb6-b93b-4d653dbc0426 | -6.16199 | -44.64574 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 310ca2f7-eac6-30fe-b92f-8b05e64057d1 | -12.85688 | -44.39362 | 2026-09-09 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06100d44-d492-383c-a5da-088771bfc1d4 | -10.75003 | -45.96851 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 88f1731c-345a-3a3d-8680-3d40a3088fc7 | -6.16031 | -44.64743 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| df2d9214-1a81-319f-bc7f-7a4fbbb4c141 | -9.77619 | -43.50344 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8038c93f-9f49-3e63-a33d-7bc7c43f3219 | -10.71501 | -46.04881 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abc8be03-2216-3c17-a169-949da24cdb1d | -8.84765 | -36.53391 | 2026-09-09 03:49:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3898e832-01ed-326f-b2ac-3de484990a1f | -10.36007 | -40.56132 | 2026-09-09 03:49:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a26fad8a-2d3b-3703-870e-988244ccaff7 | -12.27478 | -45.81155 | 2026-09-09 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6909095-112e-368f-8266-6d1a08b184c4 | -7.18916 | -43.62104 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8bc328c2-4031-3efb-90c3-6342ba671621 | -5.77131 | -45.0728 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README11.md)
