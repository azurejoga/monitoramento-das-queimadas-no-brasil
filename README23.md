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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 064d71a0-22e7-388e-a7db-1eb62cba6911 | -11.35203 | -43.64336 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| df9a3783-bb01-3514-ae9a-76f24f560b31 | -7.57753 | -45.11986 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff9ea51d-280f-3870-90ec-e7dd74bb90f9 | -8.29246 | -46.31224 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 929ccef3-9f49-34ad-ad9c-44eed3ae19e0 | -7.10068 | -44.57709 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c60c2e6c-e9e7-349e-b5cc-49779f1f0f1f | -5.53453 | -36.84894 | 2025-08-31 04:02:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 56722d76-71d2-3fcf-a5f0-7249dc30d050 | -6.86899 | -45.14732 | 2025-08-31 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3b04d63c-e613-37ea-afa8-bdadd4da41b6 | -7.10218 | -44.31333 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| b299344d-d7fd-3b70-b0f0-57e840de7a05 | -6.9503 | -44.31472 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4b42d43-bf6d-35cc-92af-765bd1370c46 | -11.3435 | -43.63002 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 31b0234b-2dd0-3462-ab78-d9fbec368f00 | -6.18031 | -43.56633 | 2025-08-31 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a13720d-c2bc-3f32-b501-3025235d9018 | -7.01339 | -42.03458 | 2025-08-31 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 37f68db7-e4ae-3add-a7f7-3666625086ee | -7.15138 | -45.13988 | 2025-08-31 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 298f8bff-80ca-310f-8a44-2b4b3b3c01e6 | -7.10669 | -44.30951 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 88b9f5ad-66b0-3640-94cc-482603bf308b | -6.77258 | -44.6341 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 98277668-5765-3a6e-91e4-5fdb4d665cb0 | -6.53722 | -44.44324 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dc98561-64d1-36f2-a5d0-bbff6369281b | -8.84821 | -40.50329 | 2025-08-31 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1f36b26b-ed34-30a3-8ff6-0dce24ebf7f9 | -6.42951 | -43.9649 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c63252d-f123-36ee-83b0-0f8fc90e8109 | -6.61835 | -43.73436 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfad65dd-7b14-3d90-af09-f5d5d89baa6f | -4.14887 | -46.78651 | 2025-08-31 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb84a0b0-9bbb-3518-9798-23ea91cb9ed9 | -6.44595 | -43.95837 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47b3781a-935d-3ea5-8a11-d212b67dcfe9 | -6.59029 | -39.64836 | 2025-08-31 04:02:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c87e5595-384b-3c86-88dc-f57dd521197c | -4.15908 | -46.78271 | 2025-08-31 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4f9bc32a-0d6a-3064-8b07-8eba67a6655b | -11.33244 | -43.63216 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f54b455f-0127-34e0-8041-b5196bd0ed44 | -7.57359 | -45.11922 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8422adc-359d-38d0-877d-a02b33787ae5 | -9.60565 | -42.93066 | 2025-08-31 04:02:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aeeb3415-a0b7-3541-bd19-ce2527bddedb | -10.48823 | -51.62507 | 2025-08-31 04:02:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b54cd42f-25c1-3bd7-944a-228436f08656 | -6.18325 | -43.34017 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b00dc950-03bc-33bc-9f7b-77b21f8016bf | -11.33939 | -43.63331 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95ee6355-2d46-34e3-aac6-09f85dfdac84 | -11.35874 | -43.53687 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f248dcd1-d4e2-34ea-a40c-adcd06ad7428 | -8.8896 | -45.08331 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9412185c-b2ad-380f-8b6d-30f6d82bf3fe | -6.47654 | -44.40471 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 848fb82d-9321-3a67-9bcf-c73d0e8c21e5 | -10.03952 | -48.09245 | 2025-08-31 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c634fad-b269-3bce-a315-135e3d5eac5c | -11.36596 | -43.60166 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f65bfb06-6c4d-3f58-a561-82fee68ef86c | -8.25903 | -47.1912 | 2025-08-31 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aaaff3fe-b646-3ba6-b19c-e08560b4b0cf | -5.44128 | -42.82866 | 2025-08-31 04:02:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 59feaf5b-ddfe-31cf-b7aa-5e7013f9a14b | -6.94727 | -44.05507 | 2025-08-31 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1da52402-fbb6-36d2-b696-e0d50e579358 | -6.27508 | -43.16958 | 2025-08-31 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1eaad092-90e5-3c05-9ef9-e7679e147c1c | -10.60839 | -44.32816 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| f7e06ee0-65d6-3d04-a92b-51609acb412b | -6.48162 | -43.53735 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c09e0e37-858b-353b-9299-f9d515f1559a | -6.42846 | -42.76199 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 147eef71-82aa-37a5-91f4-d5836babe3cc | -11.33013 | -43.66797 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1cae3e1-e1b2-37de-83fd-80fadc9a656f | -7.40734 | -42.05532 | 2025-08-31 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d5521cd8-c4bc-331e-93ce-d5337b843b3f | -6.16353 | -43.324 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 845d4e07-4fc6-3987-b476-12ea166511d1 | -7.75863 | -45.45852 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdbed412-e098-3f0e-b41c-049fe7d4b842 | -11.07785 | -44.62349 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9db498e2-f327-3bd8-a568-0091efb3ce58 | -11.07492 | -44.61856 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8abfad12-aac7-376c-8ee5-5a4a5ae20c55 | -11.32057 | -43.68259 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f44f309a-ed41-3ec9-a7bf-f8d7f462e8ec | -11.26644 | -44.92693 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8427ee8a-398b-3023-8ec4-1fb2ebae7f77 | -7.97055 | -46.41285 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ad4c72c-c6b7-31da-89d8-69328ada4e13 | -8.26136 | -47.18879 | 2025-08-31 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90516250-6db4-3733-ba69-5dbfed7eb8bd | -6.77171 | -44.83164 | 2025-08-31 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9d44b45-0688-3baf-92f6-990f04f146e6 | -7.01059 | -42.03032 | 2025-08-31 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 403e32c1-ade8-3aab-ae5d-3f09bb93402d | -6.50973 | -45.42451 | 2025-08-31 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d822389c-3d92-37b4-bd54-308729be0b69 | -6.16715 | -43.32461 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 95fd5ae2-16ac-3a80-89b3-1eaf24aa306b | -4.55529 | -50.47802 | 2025-08-31 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c612df6f-4a85-35d8-85ed-a6fac2c24c9d | -7.41413 | -42.05639 | 2025-08-31 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 32ab4e86-c471-3f38-8b52-951a86930965 | -8.08853 | -43.64767 | 2025-08-31 04:02:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4de4a7fe-6794-31f7-9003-a84a209bf983 | -10.61053 | -44.90618 | 2025-08-31 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8971e71e-8b15-3926-a7a5-b7b308cceca9 | -7.18209 | -43.84588 | 2025-08-31 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 778e7e10-b788-317f-90cd-e1621dba844f | -6.54256 | -42.752 | 2025-08-31 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c1c8d19f-733d-3ba6-b68b-24286728475f | -6.18661 | -43.31921 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e0fa8056-6204-34c5-b91b-cd001961ff3f | -4.91278 | -43.14672 | 2025-08-31 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a45c2d63-ad8f-36d7-9c36-dbae88f8276a | -4.15823 | -46.7878 | 2025-08-31 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 223c39ab-beaf-3bbd-a63b-1c1cc6517649 | -7.70828 | -50.27537 | 2025-08-31 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6c9d5e19-3371-3493-b492-8ba7bf94d0d9 | -6.65019 | -43.94741 | 2025-08-31 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 766d727e-328c-32fe-b523-e1053c5ad6e0 | -8.16044 | -42.30747 | 2025-08-31 04:02:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 42eedf10-cf5f-3757-991f-7307dd1caded | -6.17274 | -44.12852 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5550522-5999-3cf2-b5eb-ee7fbe1668a0 | -7.67242 | -42.65432 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b30409b8-3539-3fb8-9b5f-7b8a1fc23191 | -5.9864 | -43.33104 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 46b9437f-ae3f-39dd-9ffb-2abb467ea569 | -6.95397 | -42.01359 | 2025-08-31 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 250f47e2-a4d3-3c95-8a53-9a36d58d4c5e | -6.32092 | -43.78954 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fb46106-840a-3c8e-94f4-4e3cf8995754 | -7.43769 | -50.26045 | 2025-08-31 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 638fa043-ec42-3832-bbb6-806f7d4fafb4 | -6.57744 | -43.68879 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 54ab11d6-6e41-382e-9097-f93cfc465e60 | -5.6368 | -44.12522 | 2025-08-31 04:02:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7b0cdeb-e019-3b40-a2e6-6eebb8ef80b6 | -6.18107 | -44.12527 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3f1cddb-ed98-39e6-9a31-1452a9696c1c | -6.22069 | -42.76721 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fef16538-dd46-384f-ae90-84b999800ab4 | -5.9833 | -43.41781 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 585fa385-e122-3911-970f-bcc2d0c59c71 | -11.41729 | -44.68226 | 2025-08-31 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4458055a-ccdf-3877-8866-ca206faeb57a | -7.62906 | -42.6589 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad38e854-a51a-30bb-829d-017561ac7f42 | -7.37689 | -43.40563 | 2025-08-31 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bd45d5c-c01e-3e2c-b24b-b8b78ccd88ac | -6.00638 | -40.22823 | 2025-08-31 04:02:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 09261081-d7fe-386d-ae7b-e317df00314d | -11.34982 | -43.63502 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2ae59e36-571a-38f7-ad32-0d6ee2fef13f | -7.76265 | -45.4592 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a5ccc09-8177-3b88-badc-453affb89696 | -6.2464 | -42.41046 | 2025-08-31 04:02:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 49da34ac-e2ba-3ed4-862c-8779c70759a2 | -5.53749 | -36.85359 | 2025-08-31 04:02:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6bb65ed2-aacf-3940-b42c-0f2e7ab1282e | -11.31575 | -43.47423 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85f5ff5d-d7c9-39bc-afdb-62fc50029ec1 | -9.2506 | -47.06483 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8b3b24c8-928d-38c2-8c7d-ababc7aa865c | -4.01762 | -47.72252 | 2025-08-31 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6729d39-fcfd-3673-9f12-82509b3725d0 | -7.73367 | -50.26143 | 2025-08-31 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e6ea477-9b16-3e67-b20c-3b5a86702341 | -6.37507 | -43.54656 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cacdc8a-63cc-3efb-b549-a4bac39269ee | -5.80082 | -42.55955 | 2025-08-31 04:02:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 19407894-60a9-3f1d-913c-ec8fe85fef8e | -8.15363 | -42.30637 | 2025-08-31 04:02:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a06fd5cc-d980-33ab-8124-d320dbf1ff20 | -6.43324 | -43.96556 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac6910ba-637b-34fe-9253-fff8f657ce0f | -5.58571 | -46.32584 | 2025-08-31 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a72d929b-6c1e-3b4a-993a-339ab2db4836 | -9.68322 | -47.04956 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd9ebefd-d4c7-3831-afff-38077720fab1 | -10.4215 | -50.85793 | 2025-08-31 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79b8050a-b63b-36fe-87c9-e3797b5c5ac0 | -10.60547 | -44.3233 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5dbc7e77-8149-3aef-99ad-b09d3dd6e1db | -7.40889 | -44.08244 | 2025-08-31 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff609d81-d50d-3fa5-ae70-565e4f0c4841 | -7.71317 | -50.30623 | 2025-08-31 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f55ff32b-bd56-3537-9232-9e3225d661b1 | -4.2256 | -47.21097 | 2025-08-31 04:02:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README24.md)
