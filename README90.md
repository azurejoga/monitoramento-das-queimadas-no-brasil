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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8371dc82-0189-3567-8c87-5a12616213b3 | -6.92422 | -38.33917 | 2026-10-06 15:35:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 713f2e36-e768-37b5-b3c6-2a51929184af | -5.97841 | -40.91437 | 2026-10-06 15:35:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 9731c30b-2222-31de-a6cf-c07e6c267149 | -6.32892 | -43.75668 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4cd87819-a7fc-3fd5-8dc4-e23cbf09b750 | -3.27395 | -43.08669 | 2026-10-06 15:35:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bdcfaa50-079c-367b-8955-e842cfcdffd7 | -3.63042 | -38.82178 | 2026-10-06 15:35:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 6c44079a-e06f-3df8-893d-21bc3eeaf143 | -4.93729 | -38.99543 | 2026-10-06 15:35:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c0b2597d-f68f-3e77-b0b6-39f2dd27ce62 | -3.88878 | -44.34909 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 66435aa9-7bc2-3028-bbaa-2ceb4acaf00f | -3.86709 | -44.04155 | 2026-10-06 15:35:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9cd90b8a-77cb-3789-a742-8d06020b1214 | -4.79362 | -42.1615 | 2026-10-06 15:35:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 6a7d7ee1-c51d-34bf-a446-4a24139ce7d3 | -3.79895 | -41.76248 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| f6553ad1-dd71-36f0-8b7c-c53031d6c900 | -6.01592 | -42.27496 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 3679d982-cf60-3216-9020-5e9505ced61b | -3.30788 | -43.27787 | 2026-10-06 15:35:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 9ee7f346-7387-33c0-99a6-0a976b9262eb | -4.79994 | -42.16064 | 2026-10-06 15:35:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 84a6c7aa-21a7-330e-9ac8-99eab016d52d | -3.29331 | -42.2554 | 2026-10-06 15:35:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b57cad2-09b7-3649-930d-cbc1d61398dc | -3.5024 | -39.49687 | 2026-10-06 15:35:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0985f7f2-2d36-3a5d-a556-4242f1b41c5e | -5.00213 | -42.84321 | 2026-10-06 15:35:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bbfcc0ad-22d7-3144-8a27-d4bdd6c3172e | -4.07485 | -42.20149 | 2026-10-06 15:35:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 05d43843-2de3-3676-8b0c-ccb98a5f8c78 | -7.43718 | -36.00948 | 2026-10-06 15:35:00 | NOAA-20 | CATURITÉ | PARAÍBA | Brasil | 2504355 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3c718d9b-22cd-3ba9-8a05-84e92fe260e1 | -6.79903 | -38.32177 | 2026-10-06 15:35:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1b9c4fc9-4232-357b-96bc-d6af1a280f77 | -6.92001 | -43.67152 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 420789ce-de2b-3fbf-87a7-9804ad9f528f | -7.42946 | -39.48569 | 2026-10-06 15:35:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| af5d08be-6f0b-3ab6-8261-6d5bdc01b9f0 | -6.93785 | -43.67424 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ef93f92f-68be-3573-b0a8-60f5a9fbc88f | -6.08164 | -43.89377 | 2026-10-06 15:35:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 91775abe-a722-3c68-81f4-7a3d9de77cda | -5.73811 | -41.63312 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 02d96100-1dee-3d47-bd89-09bee3807c70 | -6.88098 | -43.68156 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 47a96210-4de2-3dc8-959c-7aa9c421e18d | -3.82623 | -44.49983 | 2026-10-06 15:35:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a8270c29-1e36-35a1-88eb-ccc3cfcd4939 | -3.81005 | -41.8017 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 7204603c-d614-3217-9e8f-3a4594bef269 | -3.81141 | -41.811 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 3e2b040a-bed7-390d-85e6-6f44bf5382d3 | -5.46461 | -41.22873 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 36.0 |
| 2e384daa-fa1e-3d98-967d-2e9b85a3bc47 | -6.01516 | -42.26945 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| b7aa2a5a-eed9-3c1a-8a02-65b41c244f52 | -6.89611 | -43.63123 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b7819cf7-f891-3bcc-a02f-97f93395d5da | -3.27245 | -41.85487 | 2026-10-06 15:35:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 45f43a94-7490-3acb-9565-279adcbcdab4 | -6.84019 | -41.79967 | 2026-10-06 15:35:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 314c9b59-35a8-31b7-a214-1da4b88c7e69 | -5.13369 | -42.97992 | 2026-10-06 15:35:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 69588f76-a249-358e-9bd8-2f660e50883f | -3.80669 | -41.82124 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 5b3fedf6-6235-3c40-a2b1-8c24a9317d60 | -3.96733 | -41.54562 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 99660619-7ead-3e41-a5ed-eb9ef141eece | -3.94844 | -44.02286 | 2026-10-06 15:35:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ff9824fd-b01b-30f3-8a43-2e3cef16adbb | -6.92279 | -43.6697 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d74c0919-f115-3a31-bdf3-b361218acc86 | -5.73877 | -41.63802 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7311302d-7ac3-3981-9f28-241e230fa3d6 | -5.73065 | -41.62453 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 5030fca5-52de-3772-ad47-60d2f7481ff1 | -3.67531 | -42.92623 | 2026-10-06 15:35:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 0c8406d8-4869-368c-a8f3-4242fb30d48a | -3.13862 | -40.07991 | 2026-10-06 15:35:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 35a99a6b-94da-380d-abcd-d7a21c2af97e | -6.84196 | -39.54403 | 2026-10-06 15:35:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 22.6 |
| c8f11fed-df5c-39bf-971b-b42b5de3a029 | -3.80608 | -41.8138 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| e2cc4ba5-c4c1-34d8-82e9-cd313526ed07 | -3.94458 | -44.38419 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| cef1b387-eb93-315e-ac35-d079ecad7c68 | -6.3167 | -43.33625 | 2026-10-06 15:35:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 10e12a85-9794-3657-9bc8-c3149220930d | -4.16363 | -44.26177 | 2026-10-06 15:35:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 45ff0f43-35d0-3143-8a50-4ecb27fe61c7 | -7.4895 | -40.64643 | 2026-10-06 15:35:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 9adf9e0c-c604-3b84-9776-bfd7d9e45151 | -3.29571 | -43.19248 | 2026-10-06 15:35:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c2503f86-e2ec-328d-b4f6-004eeaff226c | -6.8369 | -39.54799 | 2026-10-06 15:35:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 4f2cfe28-4db0-3d60-becf-f9e3bdb3c03e | -6.20668 | -35.63287 | 2026-10-06 15:35:00 | NOAA-20 | JANUÁRIO CICCO | RIO GRANDE DO NORTE | Brasil | 2405306 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fb4456b3-7809-3d1b-be6b-fcc85f74380b | -3.81763 | -41.80739 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 2f5dc7d3-d8c9-3c42-8e46-b241e2dd3769 | -4.96912 | -39.03472 | 2026-10-06 15:35:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 423824c1-46b1-36a6-84b9-e4dfe808c19a | -4.91657 | -41.74842 | 2026-10-06 15:35:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 24.2 |
| cfc24397-c741-3567-8619-08f56636253a | -5.73143 | -41.6222 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 91325a82-2f1f-3e08-9e0d-c0a6cd4f105b | -3.30059 | -42.34994 | 2026-10-06 15:35:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 697c165c-77f3-390a-ab40-b4076fd61de6 | -3.17083 | -41.41133 | 2026-10-06 15:35:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| a1300ba5-b003-32d4-92f3-4a049f05cbc6 | -3.7093 | -38.83541 | 2026-10-06 15:35:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fe4693d9-1bce-3504-8828-4573ceb1e966 | -7.61395 | -42.36833 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 1ed42dc9-4f95-3b10-980e-e1b99d549f1c | -6.8415 | -39.54062 | 2026-10-06 15:35:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 3eaa5b90-c10a-3c3e-8cdf-7604185b0759 | -6.64337 | -43.7781 | 2026-10-06 15:35:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7198f152-3c79-3533-bfec-2d99e2389df2 | -5.7321 | -41.62693 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 97f421c8-58df-3a8e-a453-af3e9cc87139 | -5.47065 | -41.22812 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 36.0 |
| 1e69650f-2be8-372d-a877-01f9513406da | -7.48415 | -42.79686 | 2026-10-06 15:35:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 8a9e5a53-4bc4-362c-b7a5-635ff6c324fa | -7.4218 | -35.38328 | 2026-10-06 15:35:00 | NOAA-20 | ITABAIANA | PARAÍBA | Brasil | 2506905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 835d0354-2a4a-3544-98c0-c284d2e89a85 | -4.54025 | -43.72423 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 667e200c-1883-3923-b95b-fa63787821da | -5.61526 | -35.61458 | 2026-10-06 15:35:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a0b9073b-8ca3-3c49-aa70-df5d93922470 | -6.92709 | -43.67041 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c62d7eb3-68d4-3afa-8135-8cfa3ca51771 | -5.46333 | -41.23438 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 2b5d9a03-a2ab-3c90-b677-624cb99f9fe7 | -4.80065 | -42.1657 | 2026-10-06 15:35:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 44.6 |
| d9d98cd5-ecdc-3597-aefe-1280b1642d9e | -4.51584 | -42.06081 | 2026-10-06 15:35:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 2caecef2-6362-3f7a-83c9-4da23c0dbc6d | -4.54114 | -43.73069 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 53f70ac3-46b6-32bf-bd4c-d3caf03ef4f9 | -6.60723 | -37.88845 | 2026-10-06 15:35:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 17.8 |
| a3bbf976-3c8b-3fa7-a0e0-dec5ad4edaaa | -5.98432 | -40.91338 | 2026-10-06 15:35:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0bb1654e-2a6a-3e77-bfae-810f145d5857 | -4.30827 | -41.78238 | 2026-10-06 15:35:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 821a8abb-3c52-3908-929c-d607f094ad05 | -3.80601 | -41.81658 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 58.3 |
| 767527f7-e6f8-3c5e-9aa4-d5abb03c5f28 | -3.97464 | -41.55373 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b512e784-765c-3e12-b035-8e2291c9974f | -7.1529 | -35.48811 | 2026-10-06 15:35:00 | NOAA-20 | GURINHÉM | PARAÍBA | Brasil | 2506400 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7d49a440-4790-38e7-9791-e08df0dc7351 | -4.30028 | -42.99484 | 2026-10-06 15:35:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| c298afcb-413f-3618-b9e0-c1b006257874 | -7.48654 | -40.64763 | 2026-10-06 15:35:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 4d78a4a5-65c5-3d97-9de4-d764712ce7ea | -3.72465 | -38.76466 | 2026-10-06 15:35:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 23.2 |
| e2aa843b-96ae-3d52-80d0-5ec369a33abb | -4.2988 | -42.984 | 2026-10-06 15:35:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4f7816b0-c2ce-3614-8dfb-0e0dbd206070 | -3.94367 | -40.72835 | 2026-10-06 15:35:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 99b388d3-6366-324c-ac79-92ed2693752a | -4.07253 | -42.20428 | 2026-10-06 15:35:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| eac46228-f365-3a60-a943-321de8d80c13 | -4.5477 | -43.72433 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 69999aef-b5d7-3fda-aa56-5fc1b1e93d52 | -3.62766 | -39.4001 | 2026-10-06 15:35:00 | NOAA-20 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 90aa97ed-c928-355b-bda5-cbd605905aa7 | -3.97398 | -41.54922 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 8c2bf7c3-3e6d-3871-9d09-5f7770245505 | -4.17672 | -42.44244 | 2026-10-06 15:35:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| cf3013f7-03a8-3344-b42a-9e52101a7630 | -7.42895 | -39.48197 | 2026-10-06 15:35:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 44377938-1102-3432-941e-488001f6d04e | -6.90228 | -43.62333 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f99bbe39-bd82-3170-ae9c-ef9145989115 | -4.93213 | -38.99604 | 2026-10-06 15:35:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6004b5b7-5aea-3101-b43d-5398d223a6f9 | -5.95226 | -41.36867 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| c02f8a1d-8636-3e56-805e-4aa72bdb6deb | -3.3137 | -43.27125 | 2026-10-06 15:35:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 02a75a66-9a9f-3325-9ee8-896010c31b43 | -7.1861 | -42.01395 | 2026-10-06 15:35:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| e2890ba5-b241-313d-b560-4e272284b3c9 | -3.85334 | -42.2288 | 2026-10-06 15:35:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2cb5874f-4478-35e7-854c-5a46d711f642 | -3.28825 | -42.46469 | 2026-10-06 15:35:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d1ec597e-4ba3-39de-ad5e-24c64c9aff7b | -7.60954 | -42.36929 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| d3967d47-3030-3e76-a99c-f286983aced4 | -4.51117 | -42.05658 | 2026-10-06 15:35:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 234d8117-ee04-30b2-80f4-0d23eb61457e | -4.54716 | -43.72321 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 73a62c3b-374a-3bdf-aebb-dbe1e7ca05f4 | -6.60655 | -37.88354 | 2026-10-06 15:35:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 17.8 |


[Clique aqui para ver as próximas entradas](README91.md)
