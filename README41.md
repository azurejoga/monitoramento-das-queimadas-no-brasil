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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a20c72f-11b7-3cd5-b66f-19530c8a1398 | -4.83312 | -45.4044 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3cfd1b0-04ca-3aa7-b4c5-95b6f804f7a7 | -4.83253 | -45.40787 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 869ae289-6ec1-3887-ac16-1d392b13ec9f | -4.59047 | -45.62938 | 2024-10-13 03:47:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 005a1f0f-af34-3b2d-996f-a0dddf44d68e | -4.58992 | -45.63263 | 2024-10-13 03:47:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e28004b-3cc7-3465-82e0-843dde0feb09 | -4.33856 | -44.75219 | 2024-10-13 03:47:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0becdd6-e738-3515-adb1-0966e97f36a5 | -4.33806 | -44.75523 | 2024-10-13 03:47:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d9ed886-5e06-3c14-9956-88b410bde018 | -4.15754 | -45.78057 | 2024-10-13 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cce13c5-0a1f-32bc-996c-cef873dc8cc4 | -4.157 | -45.78118 | 2024-10-13 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e935b6d5-0a87-3e55-82f7-9cfaeaca9796 | -4.15691 | -45.78419 | 2024-10-13 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d20b0701-733d-3379-8b4c-4b52f12753d6 | -3.89721 | -45.98148 | 2024-10-13 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0dfbb1f1-696b-3739-9e0b-cc65fbfb50aa | -3.89164 | -45.98055 | 2024-10-13 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51679045-1f95-3903-8f9f-f280c4e0bd2d | -3.73505 | -44.66571 | 2024-10-13 03:47:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1ec606b-7d1f-3299-b742-99abe6f8f549 | -5.04939 | -44.85811 | 2024-10-13 03:47:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d68f55f7-f4d4-37f5-8981-d1c0a3461681 | -5.04888 | -44.86114 | 2024-10-13 03:47:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f7292b8-0103-376f-aa8a-0a9b35d0e256 | -5.04483 | -44.85418 | 2024-10-13 03:47:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3292908-224d-3aee-9e15-e146e663c8c0 | -5.04431 | -44.85725 | 2024-10-13 03:47:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9df6d551-f6b5-3382-8acd-f33828b1426a | -5.0438 | -44.86029 | 2024-10-13 03:47:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddcdcbd6-dc24-3ee0-beaf-f5eae0643962 | -5.06853 | -45.38301 | 2024-10-13 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a137b95e-74cb-3674-9475-ce4753c439eb | -5.068 | -45.3861 | 2024-10-13 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c6acb8a-c142-3724-ab04-42e6efda289e | -5.06326 | -45.38218 | 2024-10-13 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30b9842d-ea07-3880-a5ae-3809122937d0 | -5.06274 | -45.38523 | 2024-10-13 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04b3a502-f52f-3b0b-a7de-4fcb2745c484 | -5.84612 | -46.23801 | 2024-10-13 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f4ca298-7061-34d7-9cc9-90fd9f999742 | -5.84549 | -46.24155 | 2024-10-13 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81908b2a-e2ac-3f27-bddf-cd3baea6559e | -5.7719 | -46.11214 | 2024-10-13 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2c72bc9-d668-37ba-853c-b27eae9886b1 | -5.77126 | -46.11578 | 2024-10-13 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff2037dc-ddfc-3bd0-abbb-730fb9fce5c6 | -5.77062 | -46.11945 | 2024-10-13 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16d9b4ca-6e7b-3ce6-b276-3faae363ffcd | -5.70355 | -45.67549 | 2024-10-13 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cf229e7-c2a1-364f-ab2e-b27be0dd18f9 | -5.703 | -45.67874 | 2024-10-13 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40855ac4-352c-39dc-a6c3-e5021e9671aa | -5.70209 | -45.67523 | 2024-10-13 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32a08b2e-7157-3ce9-9563-0159e9f34f10 | -5.70152 | -45.67847 | 2024-10-13 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20cde733-b47d-37e4-a77c-e47d30ad391f | -5.56929 | -46.16816 | 2024-10-13 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fc6f3bbc-8593-31a9-b8fc-bbd4ed201b7d | -5.56866 | -46.17178 | 2024-10-13 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c80d85e4-c29e-363f-8dea-398a157e0078 | -5.56802 | -46.17547 | 2024-10-13 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d4fbbca8-6ba5-31f4-aaf7-fb2a35cb0d89 | -5.19122 | -45.48648 | 2024-10-13 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b9b62b1-3528-3f2a-865a-59af1152bf08 | -5.19065 | -45.48988 | 2024-10-13 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c7d513a-9e2a-3f4a-8f7f-f1f73ef7caae | -5.18987 | -46.19746 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dda7194f-ee06-3c9f-9979-d3f4c30be431 | -5.1844 | -46.19617 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebcd6efc-1125-3b28-bf0d-759242329344 | -5.16428 | -46.15156 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab8eec78-a270-388b-902f-d1c944485545 | -5.16366 | -46.15514 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 976c0ad1-48a6-340d-b326-647c1bd59036 | -5.14116 | -45.39835 | 2024-10-13 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e62c70f9-64a3-3f49-b2b8-dd5e9c8604de | -5.14059 | -45.40163 | 2024-10-13 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39f188fd-1dc4-3b81-b844-a130ac1fa096 | -5.14003 | -45.4049 | 2024-10-13 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 502305d6-7b3e-3549-8ba1-0594944af027 | -5.13948 | -45.40809 | 2024-10-13 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23306d13-2926-3954-9a89-6662cb19d288 | -5.13648 | -45.39412 | 2024-10-13 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e984db9-aff7-3aea-9c09-44b6d835ec78 | -5.13592 | -45.39735 | 2024-10-13 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0831d0d5-bc47-31a0-b904-dae9a7f28041 | -5.13536 | -45.40062 | 2024-10-13 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f45cf511-b2b4-30bf-be40-64ac0b803ed0 | -5.13479 | -45.40387 | 2024-10-13 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d1f513ff-e82e-30b1-832f-1605e2a62455 | -5.13423 | -45.40712 | 2024-10-13 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 99bdd794-7326-3fa6-9329-386eecfd91f4 | -5.13127 | -45.39296 | 2024-10-13 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4784742c-aec7-34ac-8c42-b0098aa3e4a2 | -5.13016 | -45.3994 | 2024-10-13 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6ff3f02f-2acd-38ca-8093-e26e8981caec | -5.12959 | -45.40265 | 2024-10-13 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bbaa5879-96cf-37b6-9a69-122558cf516d | -5.09198 | -45.845 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 42a587a4-02ad-3799-8967-56340ef436cf | -5.08657 | -45.84405 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b4246107-ac88-3449-9787-107269631d94 | -5.08595 | -45.84762 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f17e16c0-d0af-3b86-a58f-cb4f94dbe342 | -5.08532 | -45.85131 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a6b8b47a-001e-3164-bf9c-56b6adb4fa7b | -6.47966 | -46.06286 | 2024-10-13 03:47:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53cb0312-887c-33e5-9a5f-4de5e69f510c | -6.47903 | -46.0664 | 2024-10-13 03:47:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6043e793-3c32-32ee-8f07-bae8e8e9ab2c | -6.47684 | -46.06444 | 2024-10-13 03:47:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5baf0dc2-c728-3f2c-b949-90b50b29601a | -5.60142 | -44.96982 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 798fc9fa-83eb-31ed-8c7f-161e8f56415b | -5.60022 | -44.96742 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2fde0bd-9684-3baa-8609-cd3d6945120a | -5.5997 | -44.97034 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a5b46ad-6a98-3f30-9cee-7df75b307aaf | -5.59636 | -44.96891 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 202df62a-8939-3677-9b9a-2d8cb6e16244 | -5.49743 | -44.97719 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de54a0dc-0482-3f51-9744-3127615a3a79 | -5.49285 | -44.9733 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ba01e14-28af-393c-b0a0-a059668ea55d | -5.40158 | -44.92712 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c31de5e-25b0-32b8-bd8a-914335253f2d | -5.40108 | -44.93 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c374f027-5bc3-38a2-ae41-1b88f414b88f | -5.32058 | -45.01371 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2273cffd-1a8b-33df-b723-408c16727960 | -5.31551 | -45.01264 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee819222-e682-3f6f-a570-592bc4b641c2 | -5.19416 | -44.9376 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38cbd8a0-1a9e-3f9f-819d-c8f038e152bf | -5.19365 | -44.94051 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da6f02b3-a825-3539-b800-40114f7be9db | -5.19315 | -44.9434 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59df8142-a4bf-3fd1-bb4b-9cf968013fc3 | -5.19265 | -44.9463 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3c22400-4b3a-3d2c-a47e-047157f9c62c | -5.19214 | -44.94923 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df0ddefd-1241-3863-85f5-ee920279bc07 | -5.18855 | -44.9397 | 2024-10-13 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ab0bcf4-1918-30d0-8fea-5028d4682546 | -7.24714 | -45.38418 | 2024-10-13 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b335ed89-9425-39ff-9ece-51f7b8020d2d | -7.24663 | -45.38717 | 2024-10-13 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 460aaf55-4693-3001-a4e0-93eecb14ac2d | -6.75012 | -45.22561 | 2024-10-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d03a170b-d618-3fab-a363-7c07f5cef19c | -6.74916 | -45.22406 | 2024-10-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1672e0f7-0997-35c5-8ec4-4df0edfea35b | -6.74864 | -45.22697 | 2024-10-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82e489ca-a117-3375-a5b9-72d2cdd58e7e | -6.48222 | -46.06533 | 2024-10-13 03:47:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc5b22ca-8e79-3d53-9c0f-9b0554b4134c | -7.389 | -45.62823 | 2024-10-13 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5319b5ae-5cbb-31f5-9dfa-629f9b1abc93 | -7.24611 | -45.39019 | 2024-10-13 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ec9335e6-e0cb-391e-829f-447d8735ab72 | -9.94977 | -47.27516 | 2024-10-13 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4478d626-d452-34d2-90b8-885a560d4c3a | -9.94911 | -47.27876 | 2024-10-13 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b8660e3-c7bd-32e0-a1ec-8d99d1528d2d | -9.73817 | -46.94623 | 2024-10-13 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6979df2d-c08f-323e-80aa-aba55ab59f1f | -9.73281 | -46.94508 | 2024-10-13 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df70d9fd-6acc-3772-b183-6f6c5fe62dcf | -9.73217 | -46.94854 | 2024-10-13 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d99f0542-6327-3b1d-91e3-4f0c97c9db65 | -9.73153 | -46.95199 | 2024-10-13 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5c3697e8-e217-3469-a5b5-8047c2f034b4 | -10.77208 | -46.7349 | 2024-10-13 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee68df7d-4d7a-3a23-888b-a4d7ad14425f | -10.17973 | -46.28199 | 2024-10-13 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94b2446d-6064-3bd7-bb3a-980a87c0d870 | -10.17915 | -46.28511 | 2024-10-13 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f3f2b86-17b6-32f8-b9b8-d2f10cbdd49a | -10.17228 | -46.29368 | 2024-10-13 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9a459ed7-1415-39ed-9241-a85715857c9a | -10.17171 | -46.29681 | 2024-10-13 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 21179c66-9216-3526-97db-0ca6c87d7d64 | -10.17113 | -46.29992 | 2024-10-13 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1530293b-58c3-3b71-ada6-5468388dc1af | -10.17056 | -46.30303 | 2024-10-13 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 86055021-487b-3674-9ae7-cad93b1d0ecc | -12.26282 | -47.15569 | 2024-10-13 03:47:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31e755f6-c3c9-3269-a8b1-18805a459750 | -12.19522 | -47.1118 | 2024-10-13 03:47:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddfcdd5c-2fa5-34b0-a0bc-d6c72bd57d46 | -12.17938 | -46.73562 | 2024-10-13 03:47:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a71a14b-0e2f-3191-ab8d-cbcd0b2b0155 | -12.17881 | -46.73867 | 2024-10-13 03:47:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55f58e43-be9a-3c55-b68f-1e24c223d9b0 | -12.17432 | -46.73451 | 2024-10-13 03:47:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README42.md)
