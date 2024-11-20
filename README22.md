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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db1bb42d-02ec-3621-aa71-86894a0ddaf0 | -1.86599 | -47.82153 | 2024-11-20 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9fc44ed2-b396-306f-9395-80ebcf1a64e0 | -2.22173 | -46.40078 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f38a748-65ef-3cee-8310-ed2b7cd5e69a | -2.25749 | -48.42147 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 955c602b-14e3-3c5a-8243-2334b361ea69 | -3.05605 | -45.13076 | 2024-11-20 04:25:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2637eb1f-396e-339e-8569-c702e12a9d0c | -2.49361 | -49.0256 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60f8d0b8-146b-3f94-bf71-ab5f346a1d5e | -1.24656 | -52.03381 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac7b74bc-dbcf-3ebd-9fca-015c57d98be6 | -2.54645 | -47.29356 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a81ce339-958e-382b-bcc5-2f528a3b5ed8 | -2.99731 | -45.44295 | 2024-11-20 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5abbf851-aede-3722-9b1f-50a790e61ba3 | -2.69181 | -46.22222 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b29dd559-0d41-3f29-ba14-ca400829d2ce | -3.3824 | -44.4299 | 2024-11-20 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e8bd627-2563-38e0-8fcf-351ea724a6a4 | -1.64282 | -52.68165 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cca31f30-05d6-338b-b1fb-69e1bbb38059 | -1.20094 | -51.77217 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6cbf8995-00fe-3c99-a745-d31fe51afe9c | -2.07406 | -48.52576 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 778f836b-e820-34c2-8e50-be782af8c748 | -2.26624 | -50.8102 | 2024-11-20 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0cc9ca32-86e2-3d49-b9be-8e85ba4a0007 | -2.1011 | -46.38877 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e393692c-6359-38e9-9437-e2580212ca24 | -1.04368 | -51.74212 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c43249df-ee24-32f6-a42f-68734da8cf54 | -2.18999 | -48.411 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c81e840-4c63-33b4-ba8f-61778e267633 | -1.2859 | -52.46717 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a3db6df-2166-386d-ab56-5e6b2d12ce2f | -2.61167 | -49.24987 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5d50697-4258-308a-bcd6-eecd5bfef356 | -2.51946 | -46.28056 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1be834bc-77a1-32ce-beaf-2b2a9d052c66 | -1.92801 | -49.52049 | 2024-11-20 04:25:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 36d4cc94-82a8-3ccb-8200-7cd48bcffa89 | -3.08767 | -45.97746 | 2024-11-20 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e1b9f71-4ac0-3392-b256-5c47a59c9a68 | -2.69073 | -46.07732 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 137c4a3a-0ab2-33c1-92ff-87fa1a006c0d | -1.45863 | -52.69271 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fd10281-d7ad-3dc6-9b1f-ea1176b001b1 | -1.83573 | -46.28012 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84e4bd1f-159f-3e71-978a-0b4a16dc9aac | -3.78203 | -41.61149 | 2024-11-20 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 13f55801-79ff-30ee-b2c8-49da23945e00 | -1.77353 | -46.13493 | 2024-11-20 04:25:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 413065cb-815c-39a5-bcdc-4a4cff83bdff | -1.73532 | -46.68381 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10d9b1dd-0b02-37fb-91a6-d847481ed106 | -2.89291 | -48.27724 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 16c3c8d9-1e85-3e60-9865-244a345240ce | -2.64106 | -46.22145 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c57fb19c-610b-3d93-9ec7-599b54345305 | -1.64524 | -52.60657 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90fb8cf9-22a1-3c7f-92f8-173abb89ed0d | -2.23362 | -46.82314 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a72dc74-4782-3979-8f82-22cad7ebbea0 | -1.14128 | -53.66548 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8162546d-6fd3-3824-b4f7-9ed565acc734 | -2.61685 | -48.21521 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 097f2add-e930-31cc-8b14-a1e60c94ae06 | -2.21549 | -48.41085 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcee077b-62fd-3457-afa1-896ca7b2f6ed | -1.52558 | -51.51665 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc295924-6fb0-37e1-8e3b-830cfda1d776 | -2.54703 | -47.28992 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06520053-108e-3865-81ea-c3b5d61f1ce2 | -2.24311 | -46.82824 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5a655a0-4d66-310a-b944-ab4ed31bffcc | -1.66695 | -52.53044 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e369662-4e8c-3d3c-aec4-90fcc60377f6 | -2.67641 | -46.23399 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68aef46a-211c-3701-994c-bcc6d1ac7bfa | -2.14163 | -50.65081 | 2024-11-20 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b8874dc-e8d5-373e-96fb-3f33c2b16499 | -2.02791 | -45.46346 | 2024-11-20 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76493d3e-6870-302d-b042-1bcc74c7306b | -2.68912 | -46.23949 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc1d2c2f-4117-3614-9cbb-7604f2e0c536 | -1.25676 | -53.36659 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9d05fed3-7529-3c62-96c8-ae12fdbbd614 | -2.52281 | -44.99445 | 2024-11-20 04:25:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0221d9b7-fdb7-316c-acaf-0de932678452 | -2.62131 | -46.26088 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3c2320d-171b-3636-a126-76dde22cd810 | -2.57073 | -48.43503 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f832a6c0-585c-3b8f-8acd-109caea6e69c | -1.45329 | -47.118 | 2024-11-20 04:25:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c76ee305-cff4-3f9c-b79d-7515ae78f15e | -2.39517 | -46.79365 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54a16707-f4e4-3f89-8a56-29f5e767da82 | -2.82196 | -46.67355 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2270ba5c-47a8-3fa2-a3c0-49a4afeebcc2 | -2.03437 | -45.79473 | 2024-11-20 04:25:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66b1e458-f918-3f4a-a9a8-521fa2afa0e9 | -1.64479 | -47.26308 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aef58587-2383-3d7f-90b4-f9eabe7aeb88 | -2.03827 | -48.56621 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 203b1b16-dfbd-319d-bcd5-7dcd8fa1af1e | -1.11217 | -52.35077 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0a4a1aa-db8f-3de4-91d8-f0702b46114f | -2.54984 | -47.29406 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d84d7632-9212-3e8f-9fd7-df367e394a97 | -3.35901 | -45.10701 | 2024-11-20 04:25:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35e5569a-08f9-3fb4-a84a-7ea592a31c8a | -2.67673 | -46.16687 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79b5291d-8fef-39bd-a39c-c6c2b57d5db1 | -1.69879 | -52.36023 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63686888-4f23-3190-bce5-cc39dd586243 | -2.78595 | -45.9477 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93adcd5b-eaaf-3337-b604-50b53fd13660 | -2.71937 | -49.35124 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8543b6ee-6600-3821-8f15-95850d900bfb | -3.37903 | -44.4294 | 2024-11-20 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e10dfdbc-a27d-3061-a562-029441661d11 | -2.79549 | -45.99492 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec3b7062-9e8f-39e0-bd1c-5236ea985d8d | -2.75251 | -45.70338 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2157153-9f78-3ff8-8ec3-ca30aed863c8 | -2.30085 | -49.01091 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f018f792-540c-3743-8649-e40e4c8a0508 | -2.71611 | -46.08829 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3125b78-29b0-3d5f-90e9-6934a01cccb4 | -2.062 | -53.43703 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f5bbfedf-7f2a-3604-81d3-a97c9cb70ef8 | -1.42175 | -46.79896 | 2024-11-20 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61fbfe3b-4734-3c36-aae7-5e274a812075 | -2.13984 | -48.56495 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| b4467818-2600-36d1-aa00-4db92f6ab3cf | -0.27772 | -51.39384 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcf6571a-df33-3c1f-ac5e-81f0bc18ed26 | -2.72273 | -46.0893 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9ad4095-1191-3019-a402-5ebc8d3fcdef | -2.56326 | -46.54352 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d203eb6-24ca-3923-ac0e-97aa305e6be5 | -2.50271 | -46.21426 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 321b5f33-965a-3e48-a804-6d856254a91a | -1.54291 | -51.18505 | 2024-11-20 04:25:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18161de2-4a02-38bf-9c93-e25a08640d4c | -2.19307 | -49.75611 | 2024-11-20 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35040f4c-44bc-324a-b376-59aabc2cfaf0 | -2.72291 | -47.97502 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cf44f0f-9f89-3525-b4de-93500220137d | -2.43236 | -46.53332 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49f3843a-2a29-382f-befe-7930091e8c59 | -2.0227 | -48.73314 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fc718f8-cdb9-39ca-8f25-c72111a13bac | -1.42456 | -46.80304 | 2024-11-20 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aae4afec-69e7-355c-b507-593a428fcf79 | -1.30991 | -52.40735 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80252b6c-d09e-3be7-a835-40393756f02a | -2.71636 | -49.34626 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f227f7f8-5aff-3eb5-ade2-33000972511b | -2.64214 | -46.21455 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 161e75c9-d77c-35e1-89cb-e3260a32ae77 | -2.55938 | -46.5465 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab45b5be-1d71-3308-af7b-e2bdecbbef3e | -1.45704 | -52.67213 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a74c6a12-6f49-3d80-960c-c8637c8687fb | -2.6912 | -46.20445 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5396d5d4-0942-3e37-bc58-504a4256360a | -1.74762 | -50.35023 | 2024-11-20 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af82c4b1-3b90-3496-b20d-2c1806d58ff6 | -2.02145 | -51.17418 | 2024-11-20 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3fb2c8cb-2cc9-3224-84a8-4f57c0b72ee7 | -0.1827 | -51.62417 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a0ccaf9-f0ed-3a42-9317-384cf1780c46 | -2.37064 | -49.83302 | 2024-11-20 04:25:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b19fa7d-3a9b-36b4-9c4c-f32f103c162a | -1.19686 | -53.67438 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 398bba22-e13b-3a6c-94f7-7456cf08e289 | -2.52088 | -46.40153 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f1e2033-5c1c-342e-9e89-53d857b851b1 | -2.60004 | -48.29353 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78068792-5bb9-35aa-b099-c2180b26e1c4 | -1.07195 | -47.80067 | 2024-11-20 04:25:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33d773ec-9e35-34f3-95a7-182dcacb4a2e | -2.66123 | -46.61234 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 77df5eef-665b-3836-9759-4523efd72cfc | -2.94458 | -43.24683 | 2024-11-20 04:25:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6eceb2f-40c1-335c-8e6c-fdeb95824c8b | -2.21948 | -48.77047 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ed9732b-17f3-3686-a87d-1956324950d9 | -1.63198 | -52.62956 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2ba88ec-04da-3cec-a5a8-4489da5bbb70 | -2.25184 | -48.4773 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34c1ee37-4968-3b1a-bfc0-69b12bd6f1de | -1.48103 | -51.97564 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c68b3fd-3f97-3540-8efa-f946885b3219 | -2.65572 | -46.1495 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca548340-6d37-3ea0-a6ea-6140cae44a4f | -2.13193 | -48.53055 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README23.md)
