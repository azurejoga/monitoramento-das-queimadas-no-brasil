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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9765d379-76b4-36d0-b4df-b7d5d79c9ff7 | -2.89091 | -50.40806 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8aec06cf-d94d-3729-a9fb-202293721935 | -2.00275 | -48.46819 | 2025-11-17 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 589599f4-c9c0-3f92-b9b9-a254ef52d3cf | -4.89311 | -44.86214 | 2025-11-17 04:38:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f7cd9c0b-5f76-37b7-a798-7fe87d274293 | -3.1927 | -50.65198 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d0145237-378d-3536-8de2-1f50c8a22c4d | -6.71711 | -42.93748 | 2025-11-17 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5ee4e337-e25a-3aae-8df9-2933b2bec5f4 | -4.12393 | -47.29338 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e17420e-5b14-3456-8f25-809071d06fdb | -2.5885 | -51.82785 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8efa82f5-2985-3817-be66-9fc4734c880e | -3.52071 | -51.23597 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d8f3097b-e41c-315e-931b-2d9a27ea68b7 | -1.18139 | -49.1921 | 2025-11-17 04:38:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b6add3e-69c7-3bdf-8c12-44e4e7aa5df3 | -3.38566 | -47.18815 | 2025-11-17 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4686790a-3017-31be-b914-cbd6a8365984 | -5.76297 | -42.51179 | 2025-11-17 04:38:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e03b7cdc-a0b1-3eaa-8326-37b79a416a63 | -3.25094 | -50.68393 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c04a72a-fbdd-34cc-9609-5120dd7e042e | -3.39713 | -50.18125 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8d489bd-573e-3a77-b111-9aa8032bcd4f | -7.06111 | -42.24801 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3da6620f-4c7c-322d-b135-f84fbeaa58d4 | -3.24412 | -50.5044 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04576e1e-f54e-30a1-9d02-fcc40e871e16 | -4.11946 | -47.30006 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0a84567-0bf0-35a5-8b28-83d3172188ce | -7.09177 | -42.73436 | 2025-11-17 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e9d2d417-4ccf-3528-8691-6b9d47580889 | -4.04439 | -50.48234 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| def5ecd1-1b28-398f-aeb1-c405c997312f | -2.88412 | -51.42795 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76e2d3f4-5c60-3e94-915c-85a1ec718000 | -3.81472 | -47.49493 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c9b5d9f-8f23-349d-a75e-0c1a497d07f6 | -6.70871 | -40.79662 | 2025-11-17 04:38:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1f9ba3f5-a79d-3b7b-9ab0-e2087f6f1232 | -3.59322 | -50.71735 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ef22376-41f7-3fe2-9c9b-9dfc5c1a6c54 | -2.94642 | -48.59219 | 2025-11-17 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da9439bd-389d-39f8-821b-0132bc264e6a | -1.11784 | -48.03402 | 2025-11-17 04:38:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7442333-ef97-390b-9d70-63411adbf56a | -2.47532 | -50.23886 | 2025-11-17 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3d8c2cad-8d27-3750-b6e3-927f8d068b84 | -7.13066 | -47.12246 | 2025-11-17 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f202f435-7305-340a-b04f-5500950dce2a | -7.24519 | -42.57296 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c1e27d0c-95f0-349d-9c56-8335b24b0ef0 | -4.40806 | -45.83142 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb86106d-b242-3033-8eb5-ed5efc2a0da3 | -3.88664 | -46.4637 | 2025-11-17 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f50909c-8890-3bc0-9186-ea5bc68ab712 | -6.41619 | -41.47238 | 2025-11-17 04:38:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2511ced2-0e89-3e81-b550-cf420c398784 | -6.39582 | -42.28381 | 2025-11-17 04:38:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 45458eaa-0048-383f-9ff9-e92d043671a4 | -7.43 | -48.93734 | 2025-11-17 04:38:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f6abe74-ac71-3bc9-a058-796d5c13d543 | -4.74033 | -46.38227 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f378829-7b70-304a-8d59-9126da7790dd | -3.6512 | -50.22468 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a67a1461-e0d6-3c5f-9236-e53f85920cec | -3.32869 | -50.28525 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8eea6af5-1340-329d-9ca2-81e0b18dc984 | -3.30962 | -53.85149 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfaf9d71-cd4d-38d3-a149-7016745e7bc2 | -3.44044 | -50.10345 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b79c159a-20e1-303e-a181-b420bc2f6049 | -4.42173 | -45.54731 | 2025-11-17 04:38:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a78a8388-26b1-3b43-ad26-1379e41c01c7 | -3.85805 | -40.76563 | 2025-11-17 04:38:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bed8f7c5-b324-3ffa-a3bd-e6b9f092db2e | -4.73331 | -46.38124 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 646e1bc5-a53b-3405-8773-051141e456bb | -5.61806 | -37.80254 | 2025-11-17 04:38:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4306d8de-6431-3929-afb8-b70de6f31577 | -6.07282 | -43.25965 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c86a1a04-8450-3350-a0c6-9836ec9462ea | -2.95302 | -48.59321 | 2025-11-17 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bf2b4a2-ca68-3a72-a2b5-f05ad4d0cdc8 | -2.88809 | -53.28107 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd8cc962-dce5-3d0b-973e-e8b8882de5d0 | -2.91443 | -54.16189 | 2025-11-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17756f5e-675c-3c11-8353-526603045180 | -3.50973 | -54.37434 | 2025-11-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42d3b289-2849-3152-865f-e90743b004aa | -3.08236 | -51.25399 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e23c0a79-82a4-3931-b14d-06c753fa4a16 | -4.2371 | -47.1216 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4c9688c-1dcf-31ff-aad2-d50beab0e525 | -5.40135 | -47.26348 | 2025-11-17 04:38:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02720b26-6184-321a-b114-0f3aa9f94e9e | -5.82198 | -48.99977 | 2025-11-17 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8842c99-35a4-376e-88b3-1e548f167857 | -7.26766 | -48.02327 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7a08345-dcc3-37c1-824b-9ffdd05ded7a | -4.41038 | -45.84024 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9ed71f5-af33-3185-be1b-bada004ba604 | -2.50914 | -47.81939 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c70999aa-1ba1-3424-9314-8b550235d283 | -4.09861 | -47.11197 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ca7f6f1-6698-3b78-9a34-a67d1578d5cf | -4.74093 | -46.37833 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b42f553c-44bc-38c7-a5aa-e110607ad903 | -3.87764 | -47.17842 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e65971d3-27ba-3fd2-a38d-ddafaaa32cba | -4.07699 | -46.19742 | 2025-11-17 04:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb7861a1-7eaa-37fe-a872-444609f05d9c | -4.65664 | -46.54516 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2126483-2938-3f61-bb5e-0d2c33caafc9 | -5.11142 | -46.22931 | 2025-11-17 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a56d9ae9-c812-350f-b0f1-544ea4c2c66d | -3.83328 | -49.80923 | 2025-11-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f41eafaf-99b7-3c89-9d51-c6e8bab7b8ad | -3.39994 | -50.18538 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dfab2a6-1d35-3727-b4bf-e813acb0a236 | -4.04556 | -50.4824 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78b644de-5b47-325f-9633-b8ca80964feb | -2.44126 | -49.22919 | 2025-11-17 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61aaf889-86e3-3aeb-afe7-dc0d24191345 | -4.20456 | -40.67503 | 2025-11-17 04:38:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5bf68c2f-5043-3026-adb3-75482423c8c4 | -3.46699 | -50.12218 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80ebac62-132b-3d1b-9245-d025a624d194 | -1.4636 | -53.41393 | 2025-11-17 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b84b7d9-524b-336c-93b0-b3fab088f253 | -7.9801 | -42.28104 | 2025-11-17 04:38:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4b59ceb5-9738-33b5-b721-f670cf040d63 | -3.3797 | -46.06462 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcf0e339-80fa-35b8-a71d-088fb79daf29 | -7.36929 | -45.834 | 2025-11-17 04:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 205fe385-3a35-3f03-a598-4bf6d4e62501 | -8.34702 | -46.88026 | 2025-11-17 04:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03888da6-1959-3b88-a107-c60c426fe8a4 | -7.09695 | -42.73039 | 2025-11-17 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a1addda6-c730-37e3-a833-5a08225e8c38 | -3.47511 | -50.24496 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9ab2a26-cb4b-3c2d-900d-52f9da09603f | -3.49406 | -50.34429 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3fbeabd-f09f-3753-8acb-e70cfc5d4de3 | -7.9749 | -50.00064 | 2025-11-17 04:38:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c196c3e-cb70-3758-bf38-1552b6684949 | -7.22327 | -47.98705 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a872b042-be99-34e8-ac70-11d039541873 | -3.88947 | -47.19135 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5874f05-e58c-3a6f-95c6-031435cbb0b7 | -2.51908 | -47.82093 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ec1c9310-8876-337d-9a1c-8587fa65f884 | -2.75809 | -48.42586 | 2025-11-17 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b1b61cac-69b0-3c74-b8c7-542d971285ab | -3.23846 | -50.49601 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f262a070-c917-33ae-b114-29bbb2b5ce7c | -3.49374 | -54.05282 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40080b68-5e5a-3dca-b7df-ca6bdbd06a2b | -1.52059 | -46.82922 | 2025-11-17 04:38:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7784ff92-5e04-372b-ab07-d8e6bd777ab0 | -3.75179 | -50.429 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebdef1c3-e694-3c7c-98d6-c0778ab86a31 | -4.6893 | -46.31135 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8890dbd5-dc1d-313e-a335-5a9f1edc82b2 | -5.58205 | -47.09234 | 2025-11-17 04:38:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e9655da-5657-3258-bae7-d04558e3e8cb | -5.32998 | -43.04675 | 2025-11-17 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b342a8b9-c23d-30a5-9d2c-243a78488738 | -3.38321 | -46.06516 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b288802b-b8fb-3a0b-9e7d-bed311a1e9dd | -3.46171 | -49.98985 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb48c81c-183d-3fea-a02a-e11bfab07461 | -2.433 | -52.12274 | 2025-11-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25c1b63a-c134-3cee-94a7-815d1b7e8a79 | -3.0924 | -49.50272 | 2025-11-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6693900a-d669-3d6c-89e2-d209e1db5d3e | -3.40869 | -46.90265 | 2025-11-17 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fea132c8-c21a-378e-8d56-ae9d5057e3e6 | -7.66085 | -45.35305 | 2025-11-17 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ed4cbc6-b4d7-395b-b810-ff2e4a5da321 | -3.85499 | -51.14399 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8d3544e-f4e3-33f6-9abd-b6a50a8fd270 | -7.95432 | -46.84546 | 2025-11-17 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 626d003b-42cb-3012-a506-e0f20cb5020d | -2.6736 | -51.88306 | 2025-11-17 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2faf3758-44be-35e6-ab94-2bd66b9b648d | -4.93853 | -44.53667 | 2025-11-17 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 845f99f5-573c-3e9d-810a-3fb06249ef02 | -3.81305 | -48.92232 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9e8e6b58-53d9-37da-b59f-12aba6e8ee3d | -3.37559 | -46.068 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 567a886a-788a-39fc-907d-284b040b7419 | -5.88463 | -43.9805 | 2025-11-17 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3539fc6-7878-3614-9c90-6842337e1fe0 | -5.72439 | -46.72779 | 2025-11-17 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2324792f-429e-3c00-aee0-190786da9c79 | -2.91073 | -47.83939 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README31.md)
