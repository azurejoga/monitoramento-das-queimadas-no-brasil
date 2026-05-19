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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df1840b1-0454-317a-8bf5-0ceabf3f93af | -11.32272 | -47.43548 | 2026-05-19 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b7eea56-0346-3394-abae-f82fd588f6e2 | -16.35215 | -43.879 | 2026-05-19 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d5d60d7-3d31-3e0a-baf6-1d087ffc25e7 | -14.15291 | -52.89866 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3072a8cf-2e10-312f-8489-a9ae99446de4 | -12.22278 | -46.60255 | 2026-05-19 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7916c1b-2014-3132-8425-a470d4d07e7d | -11.31032 | -47.41262 | 2026-05-19 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 197cca8f-ab54-3742-bb8d-12b4c38164e8 | -10.65538 | -42.30843 | 2026-05-19 04:10:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 48bbe660-24f5-3880-8070-46e8981c6dbe | -13.03008 | -49.93501 | 2026-05-19 04:10:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8f65f88-3d47-3115-b2bc-a5396591e9a6 | -10.45141 | -47.94978 | 2026-05-19 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 99faf1ee-549a-3fd3-9af0-9ca8eee0c162 | -12.60543 | -44.52816 | 2026-05-19 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9ac4023-ac8d-32b3-9bdb-2b61af7d6f53 | -11.84274 | -48.25478 | 2026-05-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0edf02c-0c31-3b57-91c3-36db88078879 | -11.32049 | -47.42463 | 2026-05-19 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f1583093-b1a1-31de-98ab-3e700640ebe0 | -11.63577 | -48.02292 | 2026-05-19 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d667545a-67a2-3a93-b41e-8dfdcec1c06d | -14.15108 | -52.89791 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd78626f-f923-3a44-bf55-b39afe2ea3ee | -14.50098 | -49.18058 | 2026-05-19 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1dab5c5-2788-3725-bc9f-7dd17e78a519 | -12.06549 | -45.28429 | 2026-05-19 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d00682f-40d5-3560-9fb8-8b7a20e7ba49 | -11.3174 | -47.41889 | 2026-05-19 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad2f5355-d60b-38ce-bab1-07671aebf27e | -12.062 | -45.2837 | 2026-05-19 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b1f5cd7-e62c-343f-a7af-5a2ab016cb9c | -11.31655 | -47.42386 | 2026-05-19 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3aa74b95-ea4c-31ce-b152-e14aa4d683da | -14.16653 | -52.88673 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4c3d8ad6-17ed-339b-a59b-bb0e3872d8fb | -14.15364 | -52.89506 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 864a7468-e440-3f03-aa33-aee0145c9d62 | -10.0968 | -48.01242 | 2026-05-19 04:10:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42bdc5a9-d987-32a0-82e0-c55d77d58b6e | -15.57855 | -43.84439 | 2026-05-19 04:10:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d1e4fa06-f614-3c38-8e03-6fcc59466406 | -14.15922 | -52.88486 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3bcdc9b3-9125-32d4-bcf7-43a591b9d1df | -14.70928 | -48.3243 | 2026-05-19 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20bb0050-a176-3edb-abfe-ded136475562 | -15.33384 | -47.83732 | 2026-05-19 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 366cbe0f-f07c-3fcc-9732-233b9fd31f70 | -11.96089 | -49.52715 | 2026-05-19 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7db4094f-a3f7-3bbc-a18a-dde9ace6da30 | -11.32975 | -47.44212 | 2026-05-19 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76a0cf80-9e06-35cd-9731-e48de42043c1 | -11.18427 | -55.92258 | 2026-05-19 04:10:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 331ccfc9-403c-33f3-ad9e-b1f581f2a878 | -12.057 | -45.27061 | 2026-05-19 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 096853a7-706f-37f8-86d0-2d85b3c2cce4 | -11.97875 | -47.37191 | 2026-05-19 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7541d26-4c15-3102-8922-691723a14aa3 | -11.45422 | -52.91939 | 2026-05-19 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abf7af74-e817-33c2-b0c6-fcaf7a52531d | -11.7949 | -42.63539 | 2026-05-19 04:10:00 | NOAA-21 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f46a87d3-4856-3f92-acd5-16070dbcd5e4 | -10.64823 | -42.31087 | 2026-05-19 04:10:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8abe7360-c28f-38e9-9f62-e023ecc19066 | -10.65429 | -42.31541 | 2026-05-19 04:10:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f99ed961-c1e5-3e24-a96a-f00896585c87 | -14.70804 | -48.3312 | 2026-05-19 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 844ed7ea-b604-3e70-a13c-7e667adc7e69 | -11.63511 | -48.02669 | 2026-05-19 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f71797c-9afe-3acf-9edf-74c85e8c2cec | -10.45208 | -47.94592 | 2026-05-19 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d5f0a647-c3cc-3fd0-8187-f817b855ed52 | -11.61418 | -47.09678 | 2026-05-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8c54b067-5323-3603-b74a-46cad31f9105 | -10.65484 | -42.31192 | 2026-05-19 04:10:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cea67cf9-244e-37d1-8613-d73377837cec | -16.35545 | -43.87955 | 2026-05-19 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae809d34-0f44-3763-bb06-8a54d82097f8 | -10.4534 | -47.93832 | 2026-05-19 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 95410dc2-b03e-3a09-89a9-387a1af39bf3 | -14.15178 | -52.89433 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1478b29-bb36-3608-8127-05b8b06b5883 | -10.44725 | -47.94907 | 2026-05-19 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3243d7c6-967b-3486-b045-1e5f0a6e30a5 | -11.08038 | -48.26062 | 2026-05-19 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cc25756-8635-3b19-86df-078a571aba25 | -14.16182 | -52.88227 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cc067c9d-6050-34e2-bbf7-27bb6699e703 | -12.25431 | -44.6078 | 2026-05-19 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b353eb43-9d6d-334c-bb58-07eb99fb68ee | -14.14821 | -52.89417 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d384b6a8-420b-3363-978e-4cb12695db5a | -10.4582 | -47.93529 | 2026-05-19 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 36d86104-2e31-3797-a5c1-840951e68281 | -14.22699 | -43.65573 | 2026-05-19 04:10:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e49c536-ad76-3089-89ee-4eb10c153974 | -11.17745 | -55.92126 | 2026-05-19 04:10:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16748e5d-c686-31ba-91a4-c29f501e1dd0 | -11.18569 | -55.92033 | 2026-05-19 04:10:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8be8d82-203b-3f58-a7c8-90afe1a29cf4 | -10.40167 | -49.44054 | 2026-05-19 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a04a548-07c8-3573-96aa-d64a78a36062 | -14.97328 | -45.45637 | 2026-05-19 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e53bd2a7-b32d-3eed-b610-45b9a7853b20 | -14.08418 | -42.11593 | 2026-05-19 04:10:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 88de5a91-db43-3ba9-87fd-ced1e55ce89a | -16.13843 | -43.54982 | 2026-05-19 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96f4b74b-bb8b-3951-908d-0729cc40f674 | -11.1855 | -55.91647 | 2026-05-19 04:10:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bdebe02-4661-38ef-8b32-be225cc63194 | -14.16396 | -52.87167 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74b0c4e3-5c5f-313b-a36f-5eef50b50825 | -14.15449 | -52.88039 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08f3e9ff-689d-3237-9717-5fec002c363a | -10.99246 | -43.7262 | 2026-05-19 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60dcb504-0a16-3969-acee-2ace23d953dc | -11.61336 | -47.10165 | 2026-05-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 00b0288e-6bcb-35be-a525-f907c2e096df | -10.67596 | -42.15442 | 2026-05-19 04:10:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e971cd57-249f-3b3e-8a02-fd9568a83a1a | -14.15248 | -52.89075 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d86f3d6f-397c-3065-9d6c-dbe269879d82 | -10.37967 | -45.1324 | 2026-05-19 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cdd722a-b426-397a-a82d-13af1c96c18b | -14.15576 | -52.88454 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5fa46a99-64de-3a5a-b43f-3e1889227af6 | -11.31427 | -47.41333 | 2026-05-19 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c3552f6-67ed-3cc2-b4db-32f6c4d298e5 | -14.14893 | -52.89059 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b867f29-130c-36c8-baa0-5fa29608ec1f | -11.60949 | -47.10099 | 2026-05-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 169ca725-750a-3241-8d98-b59ae91a879e | -10.65375 | -42.3189 | 2026-05-19 04:10:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 11c5a3ef-6f8d-37ba-8d3b-70d1d2c5c5fc | -14.16721 | -52.88334 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ed0d04fc-c2a3-3f69-a8be-042395ee3fba | -10.49716 | -42.40833 | 2026-05-19 04:10:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 122b848a-ab2d-373b-96ca-53fc4d6f2740 | -11.84586 | -43.96659 | 2026-05-19 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3547fa9c-76fc-385a-a124-599cfe482939 | -12.05284 | -45.27399 | 2026-05-19 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a3383482-8eb7-38c4-b155-78d7858395d1 | -10.29447 | -43.66794 | 2026-05-19 04:10:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72a4bd5b-a790-35b3-bfec-e631bebaf77b | -12.05633 | -45.27459 | 2026-05-19 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f6154583-e4e0-3948-a5d7-3f59927858ec | -12.05351 | -45.27002 | 2026-05-19 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c29b924d-3c78-3edf-a424-f845cf40faf8 | -11.3258 | -47.44133 | 2026-05-19 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7f6e065-5db3-3377-bb71-3fadcf9e9fd0 | -11.01838 | -45.13559 | 2026-05-19 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d297b4b-88dc-321a-ad5b-b79659f48fb0 | -10.65208 | -42.3079 | 2026-05-19 04:10:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8d9f94b0-e41b-3806-b55c-168cf9725eda | -11.45989 | -52.92046 | 2026-05-19 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65fbf048-2be8-3a2e-a130-62075c7f531b | -10.66587 | -49.70373 | 2026-05-19 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 80d7e688-9979-321c-a13f-e5b4a912d420 | -11.25517 | -41.90586 | 2026-05-19 04:10:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9d897bb5-0a09-342b-be19-fbcb4ff871a6 | -14.16115 | -52.88563 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bfe15c21-7d73-3a54-97c0-1d5e3688fa3c | -10.03739 | -44.15108 | 2026-05-19 04:10:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c50f2fd0-2593-3bbd-82b6-51f806574993 | -15.64231 | -42.48587 | 2026-05-19 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cd9e8a7-6a45-37be-ad71-c88e32a1a503 | -10.57321 | -46.67371 | 2026-05-19 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2b553ef-103e-377d-bd09-17bf12868fd3 | -11.17888 | -55.91899 | 2026-05-19 04:10:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b3bd8b4-a61b-3613-8722-ad3ed66f2026 | -10.45557 | -47.95048 | 2026-05-19 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 388b3584-a8f2-355c-8d3a-bb11f5df0513 | -14.15987 | -52.88148 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0d0a6d4-5c5c-3fce-8d7a-0656e7d6ce3c | -10.65153 | -42.31139 | 2026-05-19 04:10:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e0e87ba6-b54c-32a3-9816-eabd110ee7df | -10.44792 | -47.94521 | 2026-05-19 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 68dd5e96-a343-385c-84c3-75fbf622df28 | -10.4008 | -49.44537 | 2026-05-19 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ec73056-e9ea-3e0c-a6fc-fd38f8b6500e | -12.46658 | -38.35081 | 2026-05-19 04:10:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bc91d72f-fae4-3a88-82e4-b8c7469d32ac | -11.61032 | -47.09609 | 2026-05-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8e825a4c-4ff8-3fa6-9868-80cfbe1c9493 | -12.60942 | -44.52501 | 2026-05-19 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3890ed37-c4f9-35f8-baeb-d2678b0abcd3 | -12.61342 | -44.52187 | 2026-05-19 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bd12b99-feeb-3e66-8c26-462d8958a061 | -11.70055 | -47.81859 | 2026-05-19 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efdf3050-9a2e-3a2b-ac54-3f06e85f8d99 | -14.16045 | -52.88906 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| feb39cba-1072-3d58-9d0b-a47b67f3809b | -14.1475 | -52.89769 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30f7e358-2109-3be2-9e86-59a7815a9ff6 | -11.03037 | -42.84911 | 2026-05-19 04:10:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8ac58df1-f132-37be-a770-316edf4d74b3 | -14.59669 | -47.89061 | 2026-05-19 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README4.md)
