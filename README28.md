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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00bfaa78-a8e9-3b24-9402-ecb1dd3d5823 | -17.06121 | -47.15466 | 2025-08-24 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50565d5e-b88b-3b2c-8809-e445dcc3150a | -18.75376 | -45.0911 | 2025-08-24 03:45:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 957f36f3-7e51-39b9-8d14-7d5d3cdd6f05 | -17.58897 | -46.0988 | 2025-08-24 03:45:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 660cb060-a0e3-31a5-8249-5e20407e2c43 | -15.10993 | -48.66244 | 2025-08-24 03:45:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d4051640-770d-3ca3-8cf4-1d61f7b004a6 | -17.84627 | -42.8656 | 2025-08-24 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fe6b6dff-4cc0-3be6-bc4a-68a1f40565fc | -14.85272 | -48.32493 | 2025-08-24 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71dd0afd-afd7-39a8-a815-29a45fae36b5 | -13.16543 | -46.92878 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 290b2794-740c-3090-8121-5a75eb0e637b | -14.80787 | -47.92618 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a03cb352-c70b-328a-8828-3690dab1cf88 | -14.42653 | -41.78391 | 2025-08-24 03:45:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b590290-a204-3a49-97d7-36d8545d6908 | -15.70766 | -41.92562 | 2025-08-24 03:45:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e31a0808-883e-3cd0-bf58-69335a49baab | -13.33535 | -43.19219 | 2025-08-24 03:45:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa1fdea7-cb18-3278-9d2a-a64fb6b0a045 | -18.3959 | -46.84711 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3c6f709-59c5-3b82-86ac-9c5163c1f5c7 | -10.5901 | -50.20421 | 2025-08-24 03:45:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 81bdaa4b-e6d7-3726-a525-b4bdc8b80a2d | -13.46854 | -47.0169 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8979345-9856-38d0-bfa5-a4bf13a30126 | -14.81088 | -47.94044 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6aeba03a-7ac7-3d34-8884-922b7f6ab8f0 | -15.12821 | -48.63511 | 2025-08-24 03:45:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ad9331f-6a4f-3864-9a8a-5101fdb8da52 | -14.81121 | -47.93672 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 43d46952-2409-391a-bca3-54404a7d87cb | -17.59382 | -46.09986 | 2025-08-24 03:45:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| beeb5dcf-002e-3f96-bdf0-1476c46f3d57 | -13.05392 | -45.23355 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85a527a0-397e-3ce6-a479-a4a4cb8b6277 | -17.60368 | -44.30128 | 2025-08-24 03:45:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 44ddb3ee-5543-3386-b840-16433bb4b322 | -13.05004 | -45.22664 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 392f4b6f-ad45-33ca-aa47-1462365c85ff | -15.22803 | -48.21978 | 2025-08-24 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 381bd1cb-9d63-3597-9a0d-213ad7d27226 | -18.40081 | -46.84252 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df1ab825-6377-3187-81f3-52149b02dc46 | -13.47678 | -46.88738 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c7c7762-ad39-38a0-9a40-78d936b94812 | -12.72446 | -48.14122 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e16bf8b-cf6b-34c1-8569-22f44e43ce85 | -12.72541 | -48.1364 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2faa8063-4c6c-391a-be66-e78089ca925b | -12.54275 | -45.61717 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4ef4f7b-5611-307a-9e34-12c343edc501 | -12.72169 | -48.12787 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2d57172-1d3e-364b-aedf-93a5cffcec93 | -13.46778 | -47.02075 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 794a5045-74bf-3f38-a2a9-eab108534fcd | -13.04782 | -45.2384 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2614b4f4-84be-3ed5-8091-504bc8ce5878 | -17.40674 | -48.12435 | 2025-08-24 03:45:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2cfde7f-c46c-3aab-b571-d1bb7daa8d35 | -13.03782 | -45.23642 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ff307e3-1c84-3a24-bc90-353d19aad276 | -13.03895 | -45.23048 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e258659b-2fe4-31c1-979c-b45e8ecd8885 | -12.99232 | -45.23014 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce2dc607-36a5-3065-a2d0-1ed40116d75b | -12.72664 | -48.13021 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 389c8d09-f9b9-3168-87d9-6badf2273566 | -17.3891 | -42.62537 | 2025-08-24 03:45:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 94665666-a5ca-3553-b2e3-9adc59fdf790 | -16.79768 | -51.35789 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f96ce3b4-fda5-3efe-8d10-876176f553ea | -11.12995 | -46.33687 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e43e6eda-eff4-340a-9669-03dd491bdc31 | -11.78876 | -48.78838 | 2025-08-24 03:45:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21e9bf44-e2de-383f-b131-3f7234419831 | -10.58551 | -50.20752 | 2025-08-24 03:45:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1bd73136-e630-3faf-81f8-4f3ed5b31f40 | -15.12737 | -48.63906 | 2025-08-24 03:45:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56111235-6028-39ed-ab8e-ac6019213906 | -13.0312 | -45.2167 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5b8f535-0570-339d-9860-75647e767286 | -13.14141 | -44.90247 | 2025-08-24 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6df5e22f-a63b-3606-9729-670301560b7c | -14.9418 | -48.00443 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 131fa01d-9538-3ff2-bc4b-dc3f5a9981a2 | -16.78197 | -51.35915 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2b9878f-b69e-342c-ab2f-c4779a306ae3 | -13.49078 | -46.90379 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d452898-f46c-3204-9eca-c09a8a5fcf4f | -17.60521 | -44.29851 | 2025-08-24 03:45:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 92.3 |
| a19cb9ed-878d-36a7-b419-c061f3dd6b51 | -17.01429 | -47.95247 | 2025-08-24 03:45:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c093a16c-ee07-3416-b096-d2ee6ddf24a4 | -12.55171 | -45.63094 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 740bdbd4-b9f8-3868-a688-204f6efdb6cf | -14.807 | -47.93035 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1f48c84c-fc33-3953-b483-2eea2b039b2f | -13.04229 | -45.21282 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fcb278f-4c12-3497-b4e5-76c93eaf1f47 | -11.283 | -44.96751 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41121795-a32c-33bc-b280-c6ca4a28e350 | -13.03339 | -45.23246 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 432da503-e125-35cb-b011-39ba4fab7446 | -16.79651 | -51.35771 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f42f484d-fec5-384f-b9a5-2b010af61b33 | -11.13133 | -46.33801 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2a3b840-c7a6-3611-9b7a-be0ecc49d41b | -14.39869 | -49.76899 | 2025-08-24 03:45:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11d0b941-2979-37d9-ad93-ac1e71b76c71 | -13.4784 | -47.02572 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cdf8f6d-ae97-314f-ba38-60f93633c6a6 | -16.4198 | -49.14961 | 2025-08-24 03:45:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d06539fb-ae6b-3ec7-8d6b-e18aa72f5dff | -16.79788 | -51.3516 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d70262a5-2d7d-3ec2-b5d2-5699e64706fa | -12.98675 | -45.23212 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7afe761c-797a-33f1-99da-d1418b042bad | -18.39579 | -46.84145 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d74b9830-2d3e-3a2b-8567-08ba19770f05 | -16.07183 | -47.84144 | 2025-08-24 03:45:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e8cae33-08b2-3e71-a886-4da067b972be | -13.03395 | -45.22951 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8189c70-4470-3af7-ba22-dd32a5a590f5 | -13.16621 | -46.9249 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd1eb84a-abfd-3044-86d7-02afa97c66be | -13.04394 | -45.23149 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b2fe284-0a27-3caf-a1e6-2be74bf827da | -13.4908 | -46.89984 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8118d511-a4ae-30ce-9255-4a73253ef10d | -15.00801 | -48.48622 | 2025-08-24 03:45:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d690f16e-f3fb-3747-a47d-79328a03e910 | -14.88045 | -47.60794 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93590c4b-de51-3917-af31-3408f9ad9d12 | -18.70933 | -40.00473 | 2025-08-24 03:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1c236c61-edad-326a-9f2b-32c4d86dab20 | -13.04617 | -45.21971 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 297c4d91-c667-3876-b8a4-5e38af9819a8 | -13.46132 | -47.02417 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a58cf3ab-058f-3443-b21b-516e2e1ec065 | -12.73343 | -48.13194 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6fdb9a57-151d-3d59-af5e-f77c23efc6fa | -12.9627 | -46.32158 | 2025-08-24 03:45:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c7238be-9bfd-32db-b800-b8d09f995788 | -12.96039 | -46.3214 | 2025-08-24 03:45:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 432f6a8b-8e4b-37ec-a81e-dfaa484e4b6f | -17.19044 | -42.74271 | 2025-08-24 03:45:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66be8d6e-ecf1-3836-b7aa-45510f495d56 | -12.73086 | -48.11386 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0a317b0-eaa5-35c1-ad3a-1cbd1e6d62b2 | -18.39515 | -46.84451 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86d08fb9-3c99-3b8c-b513-4df524aa6d1d | -11.27909 | -44.97821 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5658529-2f5d-3f0a-9266-26f740e1d051 | -14.8073 | -47.92643 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4daa5100-a59b-39f4-8a85-615f4c738a85 | -14.79204 | -47.94438 | 2025-08-24 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c8fa15f-81b8-33a9-9075-8afab3de4913 | -12.99403 | -45.22129 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f5ab2d3d-440d-3d07-9e58-57ff567ea1ce | -17.38215 | -44.27388 | 2025-08-24 03:45:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 559985a2-f814-3d43-b04e-a3cc571a53f5 | -12.71922 | -48.13595 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8864994-c980-39f2-b5fb-2bc7a21375e8 | -13.03726 | -45.23939 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e341558a-62f5-36b7-9244-75b0a1d2edf0 | -11.33041 | -47.85073 | 2025-08-24 03:45:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 404e3211-9d59-3571-8252-610bb93c0513 | -12.20144 | -47.1134 | 2025-08-24 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71bf5a00-adaa-3d5e-8d0e-9206a28f44aa | -14.81607 | -47.94234 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a8690f9-78a9-3266-b023-ed1c70d8b361 | -11.52419 | -50.48757 | 2025-08-24 03:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c98fc901-4ae8-389b-9d4a-175cbf9c65d0 | -13.46692 | -47.01687 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3ee58a6a-ff6a-3505-a57a-c037bbf02da6 | -13.35358 | -47.50772 | 2025-08-24 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd24920e-849e-354a-9f46-2e9758955a02 | -12.72897 | -48.12302 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 664df603-b598-386f-8118-184dca83a811 | -11.27968 | -44.9751 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa3894cb-2e0b-333e-9955-a44397f23138 | -17.39398 | -42.62092 | 2025-08-24 03:45:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| df451c06-e2b0-3a2b-b3bf-62d315b5e348 | -12.72502 | -48.10681 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7cedd03-4f14-3506-80fb-8f09466dcd07 | -13.03669 | -45.24237 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51d5a77d-c789-38fc-84ed-47d8970f13d1 | -11.13829 | -46.33162 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d707ef5-5f87-3856-b8de-5016bc67bbeb | -17.58772 | -46.10496 | 2025-08-24 03:45:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| daf1615c-27d5-39d4-b531-35b172a88bfd | -12.99902 | -45.2223 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 590750a6-6a57-3ba0-bd05-41e1517fb956 | -13.04007 | -45.22458 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03596334-4f80-3752-a19c-51dbde77c98d | -16.78309 | -51.35942 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |


[Clique aqui para ver as próximas entradas](README29.md)
