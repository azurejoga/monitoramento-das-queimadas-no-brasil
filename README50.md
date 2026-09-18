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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a74b7e98-fb59-3d25-ab11-28028dbd1d44 | -9.9506 | -46.6064 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5de0b6ec-21d3-3950-aa0e-fa54176fd303 | -9.75562 | -46.09591 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5c6806a6-1baf-32be-98e2-c5e6f3e347de | -8.90465 | -45.01162 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2eab1570-133b-3cd7-895b-61bcf27f265f | -12.62189 | -50.89162 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3a0941a0-ffc0-3a13-b1ab-edb6328d5809 | -12.25885 | -50.74971 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e7223c1-b982-3946-9fef-5b0baadcdd29 | -7.87931 | -54.72286 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e190a24-665b-36b3-b81c-9cbb70198e2a | -10.65499 | -50.48245 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d1d8bdf-ae1c-3eff-b131-541c28ecde18 | -9.08593 | -45.72343 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03c26505-7471-3f01-88c5-7b3ec7317838 | -11.27537 | -43.37258 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31629374-fdec-3a37-a685-3fcacbc81043 | -15.56265 | -46.45325 | 2026-09-18 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3309858-fe9e-388f-9166-c05a4349afbf | -9.54566 | -45.45911 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8b1ac8f-9683-3c79-a25f-3f1a35b5cd5e | -8.54117 | -44.54589 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7142f722-d6aa-3c95-b7eb-6c4b21aa85fa | -11.19717 | -55.04056 | 2026-09-18 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edd9cd24-5395-3642-9b82-73676c980b20 | -10.52142 | -46.73926 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b0db22f-b768-3fd8-86e9-f342f45d725a | -10.506 | -46.27792 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f15727e9-ed5c-309b-b49d-a45a3fc8c08d | -12.17368 | -46.98416 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bf73defa-5291-3471-8974-13bc6dbd7f29 | -11.28058 | -43.50656 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4983f6f9-9f4b-3607-b1c6-4f77547b7330 | -8.48644 | -57.62735 | 2026-09-18 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e4ff034-0523-33c0-9cf1-8f117af148a0 | -9.48111 | -54.48263 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7e092b06-9f62-3aeb-bb16-e7b05fe4e22f | -12.17313 | -46.98768 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 07ea37cf-4ada-3d83-8ffb-0e387ae1f340 | -10.48934 | -45.29409 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5084737c-6e61-3ded-91bf-f7381a7ead67 | -10.48779 | -46.3073 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71c0f9d9-632a-3a3e-b655-7c7e70624d52 | -11.89491 | -47.5739 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c317436c-839a-3048-a510-31d10b42efe2 | -11.52153 | -46.86976 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 42fc7c09-0641-3b80-a661-983445a90ffc | -12.51771 | -47.08833 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ff4eff18-8789-3605-b4ad-dfcdc5d18859 | -10.6398 | -50.23827 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab483a21-00ec-31d3-9d91-172ecbbda181 | -9.15709 | -49.99445 | 2026-09-18 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e01a0d25-9fd7-353b-bbf4-1c47de25b0ac | -12.16925 | -46.99064 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 020184d2-2142-3b28-9dff-83b51f45e379 | -9.33216 | -44.35002 | 2026-09-18 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a689a61-51b6-3473-bb9e-bcf44b241eb8 | -13.62011 | -46.93918 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 32de94a0-10ea-393a-9b9b-aadcb22d5007 | -13.74641 | -48.79844 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f07ab638-9aeb-3f10-ae32-4dd3eeafafdc | -12.5748 | -47.09389 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9afed90e-226a-3ec9-828e-6485a1a0a022 | -12.4127 | -50.67337 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9e8b187-9095-32e4-839c-c8bc42101fc4 | -9.32488 | -48.18421 | 2026-09-18 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c6e448c-cfaf-3e13-86f1-89fa0882c1d0 | -8.88025 | -45.86549 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f082e821-5621-3086-b2f5-8649d81511ff | -9.94196 | -45.29364 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27686fdf-0547-3093-b2e3-1d5c4bbaf8c2 | -12.43278 | -50.67188 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0b6d1c9-1c88-38d5-b814-96826b455d05 | -12.16869 | -46.99417 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 44a338db-4b47-3c5f-8f2c-8a639e9e2aa6 | -12.62577 | -50.89231 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c288504-3ab4-3f5b-8839-949857252b82 | -10.59184 | -48.69486 | 2026-09-18 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b47ffe2d-f6a8-33ea-bab8-e57ab0f17c85 | -10.80896 | -50.19843 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4592642c-5537-3262-bab0-a61b238e5bf3 | -14.82909 | -48.26971 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa0963d7-230f-369a-81f1-3ef61978c77b | -11.88422 | -47.57586 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5febab0f-e618-34b5-ae65-aec1f14f2978 | -12.12891 | -45.15436 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db1849a3-f165-335c-9d0c-69d777350285 | -11.88818 | -47.57277 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1bce8fd-6034-3bbf-b7aa-a93d329a4c51 | -9.11426 | -48.98493 | 2026-09-18 04:21:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c3d878c-18fe-39a0-aa73-eab3c39271a1 | -8.46373 | -44.51966 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 811c8f74-88e0-3973-8c43-792ab7e99981 | -13.68555 | -48.59468 | 2026-09-18 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf45f457-0fd3-39ba-923b-9d1234f124ea | -11.31566 | -43.42207 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b19a784c-6bcc-37cb-9b04-71005d3c91d7 | -12.55357 | -50.72829 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 23e5251f-02d4-31ed-b22a-cfd833ec4502 | -9.4817 | -54.47951 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 60c43ac8-8e00-3619-9dac-688a608e49de | -12.45774 | -50.69884 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93b1afb9-6134-34c7-a4aa-bf275091bcc2 | -9.75507 | -46.0994 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d79c8337-9856-3f1e-9b41-3f7059119412 | -13.60111 | -48.29353 | 2026-09-18 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e2b46cd-0e45-3b7c-9b77-329033499d8a | -9.84602 | -48.39427 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 716e0aaa-9e2b-374f-b261-e3b9870aec26 | -9.61188 | -48.56074 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfa7a1b0-af8e-30e3-a0f1-00206c2370d1 | -9.24003 | -45.91266 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c446343-8b2b-3b23-bf71-9f572f6d7258 | -12.26175 | -47.13742 | 2026-09-18 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 071cd3a2-61bd-3902-a026-5c6d2b4b3b07 | -9.77383 | -46.08803 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 457f69d8-e5ff-3fee-8dab-7eeb7c9a3e82 | -9.77052 | -46.0875 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3397ae4c-9a5e-3239-8e2c-adaa9e31dc76 | -13.55171 | -43.50637 | 2026-09-18 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2997272d-1ca2-380a-aa52-6274ce7c7bf7 | -9.08977 | -45.72048 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31fe9bc0-d315-34be-a4e8-2ea0f90157be | -14.43857 | -44.85751 | 2026-09-18 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5835ec6-5e68-39ea-a5a9-3a0d301edffb | -14.13163 | -48.72536 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5d37a5a8-936b-313a-95a5-c640964bd4f6 | -12.55443 | -50.72339 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b65a1e73-7d46-36a8-9529-9a7e42d45999 | -8.87814 | -45.85455 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6afe7fcf-ff03-3284-a7c7-b3cc57b9046a | -9.59933 | -45.85596 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0ac025e6-dbf0-3ca8-8955-331ac8c3fecb | -11.5271 | -46.85612 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d6e1a24a-0036-39e6-86ed-f66dea3f972c | -10.32267 | -45.33968 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd740ec5-bef3-337a-987d-5393a4ff81d0 | -9.70924 | -54.82997 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fcbab102-f96d-345c-a02f-928bb98898de | -11.52705 | -46.87789 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf315cb5-7196-30ee-a8ac-612ce54a32bb | -11.22408 | -43.42946 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58061da8-5834-3337-81b4-e61637b77e49 | -10.49828 | -46.28385 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 814460a0-de5e-33b3-a2f2-8025e5bf53d4 | -10.76632 | -46.20117 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82ee0af9-0a2c-3cb1-b78a-2f1cfc401c73 | -8.6785 | -45.30639 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2b76bff-b830-3c8f-8dfd-9c45ce093da2 | -12.17204 | -46.97303 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cbbd1964-c3e8-30f3-adb3-6411c38d2acf | -11.28238 | -43.37365 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f1624863-3af1-3a98-9db0-2e351cb0f416 | -9.76209 | -45.05009 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f887c28-01b3-34bb-bd48-e9e841628708 | -8.77916 | -46.90972 | 2026-09-18 04:21:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f1fad4c4-b5b5-33c1-bd5d-020f2336ce76 | -9.92125 | -46.57629 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e64161f5-7137-3bc8-a39d-9a17e7168c8f | -10.91708 | -53.98441 | 2026-09-18 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7260b188-781d-3d66-8057-0370bd54371c | -9.48697 | -54.48003 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0529f2e0-5ba2-3505-b595-e67d10addcb5 | -13.74288 | -42.60593 | 2026-09-18 04:21:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03154cd9-a655-3086-a151-e97e32d480b7 | -8.46148 | -44.51213 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d7ba6f0-14e6-381c-84fc-b40ae55f5962 | -9.18926 | -45.69409 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6aca00df-9781-3e22-9ab0-f863ce4ff83d | -8.44782 | -47.66056 | 2026-09-18 04:21:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2631d1d3-28a2-3512-ba40-97ebb4348b28 | -8.87429 | -45.85751 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf1a9384-75ca-3bd5-b0a0-daccbf2ed41a | -9.74183 | -46.1188 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef978e17-42ee-356b-b5e6-568699647ce7 | -9.71551 | -47.13945 | 2026-09-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6c3ea7d-e73b-3735-b5e7-638e512931fa | -12.31706 | -47.95742 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9b27c368-1eb1-3993-a7d0-562156e1703e | -14.5483 | -48.90599 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02b6f466-c092-3949-90d6-3eb851d57f78 | -13.23208 | -42.33171 | 2026-09-18 04:21:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 6eac4fd2-b00c-3376-b5e9-fa9a3e0a154f | -13.68619 | -48.59087 | 2026-09-18 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee3e46b2-7391-32b4-b6a2-028d36a95e3b | -11.33115 | -46.76184 | 2026-09-18 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c4e26c6-9be8-37d7-9ba6-1c3f207190ab | -13.23964 | -42.33282 | 2026-09-18 04:21:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 12647aa8-591f-3d9d-b24a-c9e7baf507bc | -9.94019 | -46.54285 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3d54716-42b7-39af-aa00-3ce71f478207 | -16.01919 | -43.60059 | 2026-09-18 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82c93c7c-858d-3ea1-bf36-b2b76990d4ce | -14.89644 | -48.1527 | 2026-09-18 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2732d282-c26e-30d5-9adc-19755fe9c54a | -7.49756 | -55.01198 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66a8e6d3-000f-3f7e-a8ae-49f800b24cf4 | -14.19505 | -45.14862 | 2026-09-18 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README51.md)
