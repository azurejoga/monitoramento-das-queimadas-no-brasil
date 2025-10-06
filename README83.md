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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b7b5e72-dc98-3607-abf2-43778e6f8301 | -7.80101 | -44.13405 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a6b12ef3-e14a-3681-9fa9-2f8a355e053b | -11.11547 | -47.24204 | 2025-10-06 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 69c1784f-f6a2-35c4-897c-12f1d8341576 | -7.47035 | -42.61755 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 79a968a7-e6ef-382e-a287-f475f2b49145 | -8.18062 | -44.12669 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6eed2c37-1792-35ed-a7aa-205b00bb2207 | -15.17986 | -45.77094 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d468a069-d0db-36e8-9c6e-7c13a13e5368 | -15.52115 | -44.20469 | 2025-10-06 12:00:00 | TERRA_M-T | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 16ab8b71-9e7b-303b-8d34-4950285a4f6d | -16.29227 | -45.2417 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 16dcb4e8-c19d-33d6-be8d-bae4b53ce4e9 | -12.48795 | -45.55618 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| d7be97ca-04f9-31e6-b454-85089a97af1a | -11.70642 | -45.42072 | 2025-10-06 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e553e830-0a97-3ecc-b252-e1ad9732107b | -15.58622 | -47.26416 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d76c0da2-c0ee-328b-a40c-91a0ecea4a3f | -8.18192 | -44.24338 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d6a11d00-fa85-3129-8146-e0eb716e0a6a | -8.16684 | -43.34015 | 2025-10-06 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| c538bc30-d1a4-3a80-b799-87af84cdb5f3 | -14.56259 | -46.99372 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 288.9 |
| fcaec28b-8598-352b-9792-041754fc3d3c | -12.99734 | -51.03323 | 2025-10-06 12:00:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 150ff6a3-4f4f-3916-8442-69a9baceeb3b | -8.16849 | -44.27073 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fd8d758d-ee71-389f-ba33-6636f15f638f | -15.61549 | -52.5324 | 2025-10-06 12:00:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| d5e94d30-757b-3ae5-a3fd-e24568f86e71 | -13.1441 | -43.29731 | 2025-10-06 12:00:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 7c2eb68c-3386-347d-b13d-e14115012e69 | -12.98303 | -46.78952 | 2025-10-06 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 77e281d4-29f6-3945-8091-1167cc198511 | -11.69633 | -47.48274 | 2025-10-06 12:00:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| da9135a0-465a-3cab-8033-5c8c5ca6b89f | -14.85242 | -48.74434 | 2025-10-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2323f4a1-8808-3c1f-b61a-0332242fc6a7 | -12.56064 | -48.14999 | 2025-10-06 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 21be3374-9daf-363f-9601-bdf82679e16e | -15.29128 | -46.31601 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| efadf0ab-c282-3d84-87ef-c6bff6460d2d | -11.64473 | -47.01789 | 2025-10-06 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 8afc042e-c4d0-38c3-bd20-bc48fd7562db | -13.63478 | -48.70916 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 26e659de-a122-31e4-97e3-e3cb1042d586 | -7.81866 | -47.37745 | 2025-10-06 12:00:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| bdab5ad8-f1d1-395a-a446-fb9e37fff0f3 | -14.91755 | -46.81663 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8b2411e3-38c4-33c2-9c5e-0dfdf0da0c61 | -14.01437 | -43.84666 | 2025-10-06 12:00:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 85938ba1-b480-3c52-9fe1-c5a6c17f61f3 | -8.20378 | -44.15893 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 13733c88-96ce-36f5-8901-54bdb3fc8dbc | -7.25788 | -44.12521 | 2025-10-06 12:00:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 145ee2d0-8763-3d2f-a21e-ad82ff3bc4ae | -9.4336 | -44.7036 | 2025-10-06 12:00:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b595801a-7a63-3ca6-99a7-0228275017e1 | -9.68525 | -48.39739 | 2025-10-06 12:00:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b7b4a815-f18d-3f5f-a4e9-cdf2c5376e36 | -10.14021 | -45.40146 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6096b60e-ea24-38de-984d-534e01c21d01 | -8.88189 | -46.70895 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 1c8f93b0-8d3c-340c-844a-a0a03624843f | -14.54752 | -46.95008 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 493e3707-3303-3967-af13-da97627d4ce4 | -16.00975 | -50.83812 | 2025-10-06 12:00:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 47.8 |
| d1c7b022-3629-38bf-a208-b346ab04c6cf | -8.08062 | -44.79273 | 2025-10-06 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| da05f2d3-3f5d-3b6d-be19-ba30ebcfab99 | -13.77149 | -45.74027 | 2025-10-06 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| af390031-bcaa-3873-abbb-94ad898939f2 | -13.78076 | -45.74166 | 2025-10-06 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 16aec001-09e9-309f-9206-5a7e00a6a749 | -17.85251 | -41.99046 | 2025-10-06 12:00:00 | TERRA_M-T | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.9 |
| 8b01e39a-d76b-3d0d-b9b0-1d4e67909769 | -7.71286 | -42.40252 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 95df1507-575f-39e6-9bd1-962cd8cba0db | -17.66441 | -44.43458 | 2025-10-06 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 3dae7a64-7770-331f-860e-57c42be74a59 | -9.68256 | -48.41429 | 2025-10-06 12:00:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 4b63304b-325c-3111-b793-3f02a850545c | -14.55557 | -46.96307 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 0d4ddbdc-6d67-3a3f-bab2-35705a8edc70 | -13.68997 | -47.31315 | 2025-10-06 12:00:00 | TERRA_M-T | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 6028f6b4-210c-3354-9e4f-3fd62d99ad46 | -14.55708 | -46.63281 | 2025-10-06 12:00:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 439c780c-34f1-3398-bafb-8506b8a6604e | -13.298 | -48.08893 | 2025-10-06 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ba51c2b7-8f7d-3e32-884e-263faafc1b72 | -8.875 | -46.71526 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 3013436a-ad20-3083-aa18-702140c311e5 | -7.67729 | -42.58706 | 2025-10-06 12:00:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 22ab4789-3c38-32e6-ada8-14ee94d944e9 | -14.86334 | -51.50833 | 2025-10-06 12:00:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 9a699511-895c-3105-961e-583ac6029f91 | -12.43929 | -45.58345 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 02b910fa-8c64-300f-8d18-624918f2c5e2 | -16.04153 | -50.95638 | 2025-10-06 12:00:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 6893a21f-2676-3b34-a012-1007516dbed5 | -8.88129 | -44.19606 | 2025-10-06 12:00:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5b1cb56d-5f02-3a99-8e38-fe37a1bbf067 | -16.63857 | -43.21248 | 2025-10-06 12:00:00 | TERRA_M-T | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 46b81bf9-8475-3952-802f-d34d3c9ad7c7 | -14.55205 | -46.98588 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9b4c3ec5-5e99-3230-b845-e1ea60a3671f | -13.36334 | -48.02744 | 2025-10-06 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 7b1e29cf-e4d0-3837-9264-a7583bb43bf9 | -15.21438 | -46.37784 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| b79aceb2-8387-3d96-81d6-fb112c7c80e4 | -12.91604 | -47.2846 | 2025-10-06 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| bfb7d3ef-abe5-376a-b7ba-ec97fa9266dd | -7.28794 | -44.79787 | 2025-10-06 12:00:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8fb30972-55af-306c-9ddf-5dacbbb7c3d0 | -13.26962 | -47.58795 | 2025-10-06 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0fd4cbcc-bf8a-329c-b175-edbfd8205754 | -8.18975 | -44.1279 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2a1f36b2-6598-339e-b82f-14b05017c956 | -14.55991 | -46.678 | 2025-10-06 12:00:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 45.7 |
| b34a9f18-a73a-3af6-942c-8b2904b1235d | -8.91267 | -46.58179 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 03bb09d4-2689-3566-b769-e9e61500dc0e | -8.16075 | -44.25981 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ec66e110-dae5-3c11-99b1-5856b72eacae | -13.27705 | -47.58217 | 2025-10-06 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1fc0b6e6-e75b-38cf-97b6-66022075ec3d | -8.16815 | -43.33114 | 2025-10-06 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| bf8ffdeb-f383-3e0c-9c22-1d65655e8cbd | -8.62381 | -46.27029 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 90248c6e-4176-3ec4-93bb-473cc5016ed4 | -8.10889 | -44.79671 | 2025-10-06 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| aedc693a-478c-3b69-95ae-0fc554c4146a | -8.58536 | -44.32733 | 2025-10-06 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 5bac72d0-70c8-34c0-a68e-ec9ec3fcdfaa | -18.26748 | -53.32054 | 2025-10-06 12:02:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 97b2f117-990f-315c-af1d-71cb09de5119 | -20.19869 | -46.15042 | 2025-10-06 12:02:00 | TERRA_M-T | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 551b0b9f-1462-3bf4-80f3-54adb53391e6 | -22.03744 | -45.30552 | 2025-10-06 12:02:00 | TERRA_M-T | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.7 |
| 379f4fe5-c88a-38d3-b64a-904735e63983 | -21.95251 | -46.45803 | 2025-10-06 12:02:00 | TERRA_M-T | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| aaad36fc-38d4-356d-900b-6d942a20d9c0 | -21.36681 | -44.50023 | 2025-10-06 12:02:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| b6146326-f284-378b-abc7-c63230b09ac0 | -21.41108 | -45.04641 | 2025-10-06 12:02:00 | TERRA_M-T | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| e6b40874-b41c-316d-bfd4-02ae4b8441cb | -18.40178 | -45.19978 | 2025-10-06 12:02:00 | TERRA_M-T | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f10a1cb3-aef7-38d1-ade4-c7f57d9df6a4 | -18.5106 | -43.91817 | 2025-10-06 12:02:00 | TERRA_M-T | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2fc4eec3-1a3d-35b1-bbae-d83abbdacc7f | -19.79182 | -46.52497 | 2025-10-06 12:02:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 61bb6964-86eb-3353-88e9-caa63fcc6700 | -22.4547 | -46.86126 | 2025-10-06 12:02:00 | TERRA_M-T | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b92dba96-c6ab-385a-ab00-d8aa3611fb47 | -21.39767 | -45.06682 | 2025-10-06 12:02:00 | TERRA_M-T | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 8cabd879-870b-38f1-9f10-08dd9bee5b13 | -19.58695 | -44.65042 | 2025-10-06 12:02:00 | TERRA_M-T | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bf1f018f-44fe-3495-95d2-9da0c5212b34 | -20.3483 | -44.07954 | 2025-10-06 12:02:00 | TERRA_M-T | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 57318011-5d59-3363-90b4-f662a2e672a5 | -18.28853 | -45.40491 | 2025-10-06 12:02:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a2174054-9e0b-34b4-8cc2-acbbdcb1853f | -18.12891 | -53.39834 | 2025-10-06 12:02:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 040e29a8-9cf4-36de-8c4c-9d6367f30416 | -21.39633 | -45.07629 | 2025-10-06 12:02:00 | TERRA_M-T | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.6 |
| 9072594c-29e0-3356-b95e-bd3e54d9190f | -19.58419 | -47.87241 | 2025-10-06 12:02:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c0970735-9ae4-3d97-81c0-511e840e0582 | -17.96336 | -44.40411 | 2025-10-06 12:02:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 123.0 |
| eb9cc6d8-e836-37a3-893e-33fb8c9951c7 | -22.36329 | -44.20892 | 2025-10-06 12:02:00 | TERRA_M-T | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| caa42d8b-f6bc-3f2d-9f62-0a6387d7f24c | -19.93965 | -44.63404 | 2025-10-06 12:02:00 | TERRA_M-T | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 7fa1bd39-fa2e-39bb-944e-b6a1b75fb5ca | -22.95999 | -46.12858 | 2025-10-06 12:02:00 | TERRA_M-T | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| f7f6ec6b-b8a3-398a-bfa9-ec3549fcda6e | -22.30581 | -45.55215 | 2025-10-06 12:02:00 | TERRA_M-T | SÃO JOSÉ DO ALEGRE | MINAS GERAIS | Brasil | 3163201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 101d902f-b5c7-3cad-9c32-7159d409c6ef | -23.18745 | -45.64042 | 2025-10-06 12:02:00 | TERRA_M-T | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 299c318c-7181-3277-b019-98e21d7877cf | -21.18045 | -46.3123 | 2025-10-06 12:02:00 | TERRA_M-T | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| b578e49c-d582-3b63-b1b2-f7c48f9026aa | -17.70299 | -46.30043 | 2025-10-06 12:02:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f411015a-da3d-3e41-af6e-063811213632 | -19.93833 | -44.64339 | 2025-10-06 12:02:00 | TERRA_M-T | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6eef8e91-2ddf-38c9-9ae6-55451d13a9f2 | -19.58828 | -44.64107 | 2025-10-06 12:02:00 | TERRA_M-T | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a3288575-aeb1-343c-9db2-d6ab3b47d769 | -22.63466 | -44.58314 | 2025-10-06 12:02:00 | TERRA_M-T | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 058c8d70-714c-3409-a3a0-c13a47c2d7df | -18.27828 | -45.41276 | 2025-10-06 12:02:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 29.9 |
| fe25ec06-1977-3633-8b32-89b3b5d5eee6 | -21.68816 | -46.3751 | 2025-10-06 12:02:00 | TERRA_M-T | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 5c1872ea-80d0-3786-bebf-94792edcb5e4 | -21.21699 | -45.62096 | 2025-10-06 12:02:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 19dd7ebe-c53d-3e40-87b4-e3078cdda4c3 | -17.96467 | -44.39488 | 2025-10-06 12:02:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 29.9 |


[Clique aqui para ver as próximas entradas](README84.md)
