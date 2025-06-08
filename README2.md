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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4562c0cc-af6d-383d-aa74-c11c571ffb02 | -14.88 | -48.133099 | 2025-06-08 00:24:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6945bf03-54bd-3dd0-9fd1-c31b376d2cfc | -7.0244 | -44.5905 | 2025-06-08 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4622e45-c540-3e69-b930-a92afb2019ac | -4.4166 | -47.664902 | 2025-06-08 00:24:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8b59661-4c61-331c-924d-717da87b6b61 | -6.2101 | -43.341999 | 2025-06-08 00:24:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47088038-0fbf-38a9-b65d-552bfbb79cb1 | -5.7784 | -43.6157 | 2025-06-08 00:24:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe2de3c1-9f0e-3e87-93e3-51ba9e9c2992 | -6.4485 | -45.724899 | 2025-06-08 00:24:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e548de1-22f9-33dc-afff-db1875aa8e64 | -10.3959 | -47.004299 | 2025-06-08 00:28:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 437a7070-a542-3751-a010-7077dddaf1bd | -10.7551 | -48.5756 | 2025-06-08 00:28:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6cd9d49-f9db-3383-bbf6-a963caf75ef6 | -11.6253 | -48.484402 | 2025-06-08 00:28:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20bcdcc8-7d3a-3731-bcf2-6a9eaabcb05a | -10.6477 | -44.479801 | 2025-06-08 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5105d942-47bd-397c-9134-0b6d67ed4049 | -11.6274 | -48.4944 | 2025-06-08 00:28:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3f2dbcd-d7b8-3aa4-8b60-eb6c96558f84 | -10.7572 | -48.585499 | 2025-06-08 00:28:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 182144aa-451e-3093-ad99-39400f3f5797 | -10.6509 | -44.493698 | 2025-06-08 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 54ada537-da3c-31f9-a942-935c36eeba12 | -10.6493 | -44.486698 | 2025-06-08 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7adf974b-6bcf-3729-a24e-7e4523a59306 | -12.3638 | -57.396 | 2025-06-08 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| fdc8e769-345c-3652-8188-421a3b9a2323 | -7.7364 | -44.1592 | 2025-06-08 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 5d4e053e-72ac-34b1-8ec0-d8d950328b1f | -12.3636 | -57.416 | 2025-06-08 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| c44d632c-55c6-32cb-8396-2df72a87aed4 | -7.7361 | -44.1823 | 2025-06-08 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4034ba72-4cc9-36cd-8273-be12ac51a440 | -7.0169 | -44.5954 | 2025-06-08 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 5bece43c-b551-3953-8b78-33657d5143a9 | -12.3828 | -57.3944 | 2025-06-08 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f3941d39-1430-3ec6-9c9e-77754ee79c2c | -11.6316 | -48.4837 | 2025-06-08 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 5f841df2-ac1c-3487-bf83-eb796786f7ef | -12.3826 | -57.4144 | 2025-06-08 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 518abcf3-1887-390b-88df-0261ac29b0a4 | -7.0169 | -44.5954 | 2025-06-08 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 66b268f5-6f28-320f-97c7-7ae999782a3d | -12.3828 | -57.3944 | 2025-06-08 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 17d6f68a-15b7-30fa-be05-aa1ac3761203 | -12.3638 | -57.396 | 2025-06-08 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 2867aaea-e633-3783-8b52-6686ef842d06 | -12.3636 | -57.416 | 2025-06-08 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4c5a387c-9d5a-3345-8e28-1eeb6355d67c | -12.3826 | -57.4144 | 2025-06-08 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 24c8c773-0031-3e14-a357-3a9fc06c88df | -7.0169 | -44.5954 | 2025-06-08 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 53a04908-763d-300d-a7ab-356adaf82ec5 | -12.3828 | -57.3944 | 2025-06-08 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 3d56e984-6893-3e6b-9438-a47b4cf70008 | -12.3826 | -57.4144 | 2025-06-08 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 11b947de-2f9c-3e01-ad3b-3dd8b3737aca | -12.3636 | -57.416 | 2025-06-08 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 00dd3814-2dba-3a69-a876-d14af6b5b174 | -14.03621 | -55.13169 | 2025-06-08 00:56:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5bd6e935-c8af-3ba9-bb62-42133f92f6ea | -13.88082 | -56.19532 | 2025-06-08 00:56:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9512e5c9-45da-3584-82d0-598ecfa70aa1 | -13.88249 | -56.20925 | 2025-06-08 00:56:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 148f9e42-ae55-3174-8ecf-4a0952ff6bd7 | -18.71883 | -54.1873 | 2025-06-08 00:56:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cd4e7f2a-c0d7-3ecd-8547-6f938844f894 | -16.26862 | -48.80379 | 2025-06-08 00:56:00 | TERRA_M-M | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 51983761-8a60-366f-b3d4-916174692df8 | -12.96347 | -46.74993 | 2025-06-08 00:56:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| bb3ad876-43c6-3008-999a-b80f460c2b1c | -18.72033 | -54.19957 | 2025-06-08 00:56:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f0db8e4e-d4bd-3b07-9f88-3a6cb2fc3764 | -12.97496 | -46.74772 | 2025-06-08 00:56:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f31c02f7-98e2-361c-a666-f1d67fbdf65e | -14.88005 | -48.12526 | 2025-06-08 00:56:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| fb105abe-ce43-37da-bdf9-8bb215881872 | -18.02604 | -47.37953 | 2025-06-08 00:56:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| daa39c26-843a-3318-a36c-684a7e02ec3c | -12.97739 | -46.76303 | 2025-06-08 00:56:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5180c6ab-3517-3ed8-8a1f-adaad48ded7e | -13.46817 | -56.85987 | 2025-06-08 00:56:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 04d53483-eefa-37ca-b899-531ed44340db | -14.03768 | -55.14349 | 2025-06-08 00:56:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6fc8003f-929b-3a82-afd5-84e0289e9cfb | -12.36767 | -57.3955 | 2025-06-08 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| d5956ea8-50d9-34dc-a10a-344eb55f06ff | -11.6355 | -48.49643 | 2025-06-08 00:58:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e7e59fcc-cbc6-328c-9aba-b5c2a49a9076 | -7.02368 | -44.57434 | 2025-06-08 00:58:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| e19f1c45-821b-3837-82b6-f51c66a8d17c | -7.02005 | -44.56931 | 2025-06-08 00:58:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 2ee6bfed-35d9-38c7-9d66-4ed2e22a44b8 | -11.80179 | -48.09784 | 2025-06-08 00:58:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 113ec420-fa08-325c-b85c-81e55e260d11 | -9.40127 | -48.43531 | 2025-06-08 00:58:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3bb42d06-b7d3-3002-a187-6c71c89f7475 | -6.21022 | -43.33991 | 2025-06-08 00:58:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 7ce50f9e-ecc9-39af-9c2b-14bfce82e6eb | -9.62343 | -55.10457 | 2025-06-08 00:58:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 344e8d9e-11f6-34fe-9856-e2df2f0593e3 | -12.36971 | -57.41171 | 2025-06-08 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 19b615a1-66e0-3e17-b436-56afd8235a97 | -9.07626 | -47.14331 | 2025-06-08 00:58:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 9b6b8393-4071-31c5-b890-3a0d2153e266 | -7.01316 | -44.60722 | 2025-06-08 00:58:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 5a61784c-5521-351c-8888-291fab4fec07 | -12.52854 | -58.36605 | 2025-06-08 00:58:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 17ccfb4a-c831-324a-b3c1-f8788444aeef | -11.38251 | -56.5649 | 2025-06-08 00:58:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 23827fd0-772f-345e-8699-214a7b08e77a | -12.36836 | -57.42249 | 2025-06-08 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3908af3c-e319-38d1-b545-d41a97c8f3cb | -11.55131 | -56.44913 | 2025-06-08 00:58:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 60569959-1a99-3542-9454-ba792514b6b0 | -9.41418 | -48.44735 | 2025-06-08 00:58:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| db8d1945-ed37-3505-a3a3-d28b2d10f3c8 | -6.20751 | -43.34721 | 2025-06-08 00:58:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 58991b26-2cb6-3b7a-b557-ecc6d599ca84 | -11.39001 | -54.77275 | 2025-06-08 00:58:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b5bd7153-8647-361d-bfb4-a92618790ae9 | -7.86708 | -47.89875 | 2025-06-08 00:58:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| acdd8ad6-b5c4-32c3-a86a-ed6d286633f0 | -10.48967 | -53.66655 | 2025-06-08 00:58:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 06ed50db-44de-3dc6-a1d7-f6bf4527f87a | -10.73703 | -52.50703 | 2025-06-08 00:58:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1ff1ebb3-e402-3bed-a47c-6e01303b95b8 | -7.02832 | -44.60386 | 2025-06-08 00:58:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| bb59456b-995a-3c1f-a09d-e695f71a05c0 | -10.87833 | -54.30071 | 2025-06-08 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0c2bb2f6-b518-31c3-be6c-e2739c1f7e2c | -10.6358 | -46.83142 | 2025-06-08 00:58:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 6966c9ed-421b-3728-b39f-c1e5f4f121a0 | -12.37804 | -57.40482 | 2025-06-08 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 1138ce15-8684-3393-a139-37e7c5a520ab | -7.73694 | -44.18102 | 2025-06-08 00:58:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 97185235-e43a-31c7-9bd7-90cd1d9dbd2e | -7.00972 | -44.60189 | 2025-06-08 00:58:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| a5068a3e-dd7f-35ad-b2eb-8a62042b4ced | -10.75813 | -48.58174 | 2025-06-08 00:58:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 5bf22453-13c8-39d7-aad8-5091a3c1fdcc | -11.12566 | -54.63937 | 2025-06-08 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 7c380268-e0ff-3afa-ab1f-679a4015f628 | -11.54069 | -56.45049 | 2025-06-08 00:58:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 97c52738-ae22-3b88-a5b3-1b2b95236c0f | -10.49862 | -53.66525 | 2025-06-08 00:58:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b893329c-4b92-37c8-8f27-6057fea48e1c | -11.54235 | -56.46384 | 2025-06-08 00:58:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 92636aa7-df6d-3e65-82bc-dfb1ccf69253 | -9.40339 | -48.449 | 2025-06-08 00:58:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 94e00c54-035e-322f-94ba-65197880dd2b | -12.27525 | -55.07758 | 2025-06-08 00:58:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b5f26d4a-0393-3a3e-aa0d-b5349f5bfb36 | -11.79976 | -48.0845 | 2025-06-08 00:58:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 625f15e7-1a64-303e-aa36-12b0e7b73565 | -12.52628 | -58.34689 | 2025-06-08 00:58:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 0a1c9ab6-3f7e-3dd0-8e64-247c99b06faf | -7.72677 | -44.18811 | 2025-06-08 00:58:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 48.3 |
| e0ab7059-5814-38f1-b83e-6b3a3fc04c10 | -10.23847 | -52.23722 | 2025-06-08 00:58:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9528b403-eb40-3e52-b549-82fe6f1c7533 | -11.11629 | -54.64063 | 2025-06-08 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b7db89fe-a785-3963-8b14-0f3efb542023 | -6.23772 | -48.54085 | 2025-06-08 00:58:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3857821b-11dd-385f-ba89-738c0170632c | -10.95042 | -55.33613 | 2025-06-08 00:58:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d3e2cf57-ce35-3095-8f9c-37d71dee3617 | -11.127 | -54.64958 | 2025-06-08 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 20862dbe-29f3-3e3e-963e-8f2e6cd885e3 | -10.29557 | -57.1348 | 2025-06-08 00:58:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8d194a6d-a6ac-3cf9-8d26-f86b7a33acc8 | -11.63355 | -48.4838 | 2025-06-08 00:58:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| a8bda441-1493-3e84-8340-a8faf56c9284 | -12.37997 | -57.42107 | 2025-06-08 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| c6f8e857-5a44-377d-8912-a18981801b0e | -11.78911 | -48.08617 | 2025-06-08 00:58:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6713f5e2-7c87-323b-a008-024bbeec3c6a | -11.38083 | -56.55148 | 2025-06-08 00:58:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b1365cc8-e9e1-357a-902b-84dc877f20d4 | -11.11762 | -54.65083 | 2025-06-08 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 428d3168-69da-3e58-9d5a-d5e07c3e45ea | -12.36646 | -57.40631 | 2025-06-08 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 6d8016cc-af7b-3ef2-be99-e95ba777f2e9 | -11.78739 | -54.77901 | 2025-06-08 00:58:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 75efe486-ada9-31f0-9552-4fe68c09007e | -11.11895 | -54.66107 | 2025-06-08 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e2ac1d5d-5895-397d-b83e-d1aac70ca1eb | -11.37185 | -56.56639 | 2025-06-08 00:58:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5fc0c494-7f76-3b6f-8ee8-473e49eb2cc0 | -8.52685 | -50.03558 | 2025-06-08 00:58:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cf4014ff-e323-347e-a023-5db1c89680bc | -10.74772 | -48.58361 | 2025-06-08 00:58:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 955440f3-fd6c-3d29-8c2a-ca218cdbdf49 | -8.5252 | -50.02451 | 2025-06-08 00:58:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 118ef9d9-6c89-3bf4-a00d-a19c7149132c | -7.025 | -44.59931 | 2025-06-08 00:58:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |


[Clique aqui para ver as próximas entradas](README3.md)
