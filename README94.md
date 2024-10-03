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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05a50840-3ffa-3103-ac74-ed4ae78adf90 | -12.10291 | -50.01394 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd898f5d-77ac-3db7-bc1e-d3ccb4e675d1 | -11.97623 | -50.18776 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3634dcfd-caf9-3039-b2ef-65a182986550 | -11.97404 | -50.17919 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f49e1f73-e85b-3ba5-b573-ed383e3810bd | -11.97338 | -50.18317 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a926e517-0715-3f33-a006-7c86dd2dcbe6 | -11.97053 | -50.17859 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da2392de-e09b-3b5f-a699-d2b53c51f752 | -11.96703 | -50.17799 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e61b380-e7b6-3f12-9284-995c08ef0d17 | -11.9563 | -50.15566 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 155d3ca5-70fc-324c-8edc-7aa41d16abf8 | -11.95564 | -50.15964 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc5b70a7-2500-3fd2-9091-051a63a1711d | -11.95346 | -50.15107 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6635433-d99b-353d-a5dc-133d9755c21f | -11.94996 | -50.15047 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a6ae93da-e650-3d65-9527-2666e3f1dd5f | -11.9493 | -50.15445 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76319415-27b3-3fa3-bbed-b32576f823d2 | -11.94646 | -50.14988 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3231eb5-e1d2-363f-92a3-19e9fee03c55 | -11.9458 | -50.15385 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba99f7ba-86bd-3f2e-9a66-a2a4626e4549 | -11.94514 | -50.15784 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b629c40-4be3-3e46-8d94-96b96f07e64d | -11.94229 | -50.15326 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5406e244-8761-3cb6-927b-b4327a6d5334 | -11.93879 | -50.15266 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e39fe01-20ee-36c5-b535-5b8988837d22 | -11.93813 | -50.15664 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd87edd7-7a90-319c-aa68-e2ae5e0ef085 | -11.93529 | -50.15207 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11056bb4-8b66-3aa7-9fb2-738b7f3bd0e4 | -11.68911 | -49.90122 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abda090f-e537-378c-a021-026eb629ae33 | -11.68659 | -50.03416 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9172738-2b4f-31bf-99d4-1938e63214e3 | -11.24791 | -50.02726 | 2024-10-03 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 011b7087-9ed1-36c2-bc43-00da9f7b9ea0 | -11.12528 | -49.6056 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ecbdbcc-0972-3a48-8d3c-e3195171421b | -11.10955 | -49.61483 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff1bc534-cef2-38d0-9209-4baee4e15251 | -11.10545 | -49.61811 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd1d9400-e38f-3af8-af96-0cf1d1df6209 | -11.09983 | -49.60923 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3190201d-0427-3426-b7e3-62f60cf0aa66 | -11.09702 | -49.60481 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f09f9bf8-da42-3dfb-941c-73b2d552b03f | -11.09638 | -49.60866 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33beabb6-5a21-3dcd-b36d-713c3beea4e2 | -11.09573 | -49.61251 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be3dd94d-b5b6-3f9f-af3f-fc8a5993ad57 | -11.0945 | -49.6043 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be7172d8-a21e-308f-ae81-704546f679f6 | -11.09388 | -49.60815 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f89deabf-4286-3ed2-b93c-592538ee39bf | -11.09356 | -49.60424 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d1ed2ae-5e68-3bc7-ae21-e94110a51400 | -11.09325 | -49.61201 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0396a0ea-5e50-3e0d-93c8-48e0aec6f389 | -11.09292 | -49.60809 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dcbcd03-77fd-323c-b088-d98b899776ed | -11.09228 | -49.61193 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 694b5f15-9221-3b35-ba93-35dcfea10d63 | -11.09168 | -49.59987 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa0b5780-4b82-368f-beb8-867d460b742e | -11.09105 | -49.60372 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a977b5e-e5e8-3e7b-a384-96ec572cca1a | -11.09042 | -49.60758 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dd7d414-cb22-3959-b4cd-8528b9250f3b | -11.08947 | -49.59159 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8051bfac-22e2-35de-b64d-81075d9b5199 | -11.08885 | -49.59544 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e3af4a8-6136-319a-ba40-e40d180e576c | -11.08822 | -49.5993 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bd29f392-3604-34f0-82ea-e877399151d3 | -11.0876 | -49.60315 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01739bed-068a-3a6c-9998-3f34b9931c83 | -11.08602 | -49.59102 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a463a17f-e366-3e24-b20e-71653f72f8d2 | -11.08539 | -49.59487 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 416ae59f-a1af-3f19-86af-f93583f41ac3 | -11.08477 | -49.59872 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a968ad0c-156f-3d93-bd2d-2ea80a772437 | -11.08414 | -49.60258 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 28ed4f08-fad0-38c1-a459-7068a65fd717 | -10.97749 | -50.16566 | 2024-10-03 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 362c3d02-79b0-3396-a7d4-68915cba6e39 | -10.97596 | -50.15287 | 2024-10-03 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cb5127d-aa58-3e5d-9ead-226d78078b32 | -10.97529 | -50.15694 | 2024-10-03 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3708d35-78ac-3abd-92ae-084c1b4e3498 | -10.97175 | -50.15634 | 2024-10-03 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bd38da1-5868-3493-94a6-5b98dce10a2e | -10.89331 | -50.14827 | 2024-10-03 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c6c0b9d-7f6a-3081-a96a-457d11568c6c | -10.89319 | -50.14724 | 2024-10-03 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c3df96a-34f5-3877-8c47-da6a5cad1263 | -10.88977 | -50.14767 | 2024-10-03 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e38c1ae8-1b45-3c4a-b1d1-87e16279fa65 | -10.88736 | -50.11806 | 2024-10-03 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4186dbf3-6440-3407-bd7d-455a5cd6885c | -10.88669 | -50.12211 | 2024-10-03 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b8e22f3-a619-303c-acb0-bdcbdffeeaa5 | -10.88449 | -50.11341 | 2024-10-03 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db9127ba-6a01-3ed8-ae0e-83806d58ca87 | -11.35183 | -50.78748 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9eb1932a-c37a-30d9-8b44-e05b4f0a4474 | -11.35036 | -50.79609 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c017b1c2-c162-34c6-afe9-ebd4cec02d38 | -11.09583 | -50.721 | 2024-10-03 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b3bdf71-728e-3e7f-bdf2-d337fa0bbe3a | -11.0922 | -50.72038 | 2024-10-03 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fd1dcb3-2d46-3e69-b7df-2e62fedcfad3 | -11.09148 | -50.72469 | 2024-10-03 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ed211c1-1eff-3478-b3c2-eaf56a341686 | -13.6371 | -51.18601 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 679930f9-2066-3b9b-b865-d6da5d3c2525 | -13.63349 | -51.18537 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fbac20f-f3e0-381c-87cc-9ca4ca00b779 | -13.61908 | -51.18283 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dab01453-4121-3350-a38a-715510fa9523 | -13.61835 | -51.18709 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b6069a0-8751-3795-8ea7-1cf28dc32d0f | -13.61475 | -51.18645 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 510c1bf6-d88c-3daf-9743-9f8b8772c726 | -13.60387 | -51.22857 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba1d1446-440c-341e-b5d5-64ca2bb3ef57 | -13.56552 | -51.23507 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2eb652c4-b610-3347-923f-5faad2ec59a3 | -13.56478 | -51.23936 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 15cb9e5c-b318-3d7d-af38-1dbc18db6a1d | -13.56404 | -51.24365 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 75b0bc39-8d64-3ee8-9bed-dc02dc323ac1 | -13.56191 | -51.23443 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0d237cd0-a10c-3dbf-97ca-c05f0eab9d01 | -13.56117 | -51.23872 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 61eddd05-a5b2-3619-a9ce-a59eeff324c4 | -13.56043 | -51.24301 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 746dd778-cb83-34b5-93af-c6a25cbe166c | -13.55969 | -51.2473 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 54319f1c-b165-39fd-ac02-ff4ab01d4f1e | -13.55755 | -51.23808 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fbd0ef69-0986-357d-95bb-9d15135127c5 | -13.55235 | -51.26818 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dddfa740-abf9-343f-b631-6268c033132d | -13.55032 | -51.23681 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60be47b4-06b0-3a30-bf35-afb083f7551b | -13.54873 | -51.26754 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abb34732-7e0f-3c29-9d39-35d20e9abca6 | -13.54798 | -51.27185 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41c68e98-0e18-3bf4-ae37-c21e6d301d17 | -13.52746 | -51.14606 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| d670979b-8cbb-3ecd-b449-adc9289251ca | -13.5253 | -51.13692 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2c3bdee-4f9e-3c58-b089-abb949a10c89 | -13.52529 | -51.20284 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f37b417b-5e5b-36b0-affd-d333e9752cbe | -13.52458 | -51.14117 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 9cff2563-5fb8-3082-8a59-3a1e08b85542 | -13.52457 | -51.20712 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 969571f0-4c07-3b20-9e09-ee4e7836f406 | -13.52386 | -51.14543 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| f226d448-8dc6-3459-9b16-59ddeafdf985 | -13.52314 | -51.14968 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ca169d2d-0946-3689-a14d-bf22e3ea9c46 | -13.5217 | -51.13628 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.2 |
| df68d69f-0837-3749-85bc-b811ff2ba8c9 | -13.52098 | -51.14054 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b378eee0-2579-35c3-8224-8b84cc3bd1fe | -13.51954 | -51.12714 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 16c0c63b-974e-3882-8d00-7d76257509c5 | -13.51882 | -51.13139 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 4c9e4fd3-71bf-33ab-81d5-db65706c61cd | -13.5181 | -51.13565 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.2 |
| ab99441f-e979-3516-936d-1a8f7714a07f | -13.51738 | -51.1399 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 39f411ee-171e-3e75-bcd5-ad02f06078e5 | -13.51594 | -51.12651 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 830cd049-01c6-3191-b8ba-65b362bb2e0e | -13.51522 | -51.13076 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64eb5dcb-5170-3391-a9cc-3c6563787166 | -13.51162 | -51.13013 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9c97173-f96f-3a6b-8ee9-43f70996505e | -13.21207 | -51.18704 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aa99a72c-9c63-311e-b9a3-896754fd9301 | -13.19902 | -51.19805 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d3b5315-c440-39be-a49e-8eec6d0f2430 | -13.19829 | -51.20237 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c5a61f3-ff2a-34e4-8b9b-f80b9a7b18f6 | -13.1954 | -51.19741 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d7ba9ea-3289-33f5-90ba-3c0bb56e20f1 | -13.19466 | -51.20173 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e72a1a6d-8b00-39c5-b833-58e28c76ade4 | -13.19031 | -51.20542 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README95.md)
