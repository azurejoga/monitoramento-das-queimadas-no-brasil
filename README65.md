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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96cdfb91-5024-3f9a-9f7f-dfd6f31aa0c4 | -16.46359 | -53.91194 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a214d1e8-ba16-327a-a0d4-0f7deb8aa07e | -18.08704 | -54.30877 | 2024-10-08 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b5e7d0b-03dc-3ebd-8e6f-63d1f063e985 | -17.76946 | -53.80033 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8387d092-67fd-3a93-bde6-4d2717f290ca | -17.76868 | -53.80484 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8918db9c-6880-3a23-89ce-53f0899f1814 | -17.76792 | -53.80925 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b3040a4e-79d7-37e0-bfde-815bea3ccff0 | -17.76433 | -53.80853 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a69f0237-9508-32da-9586-a3cb88d3423a | -17.76357 | -53.81294 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66f45f90-e9d8-3a28-bb93-aa15b38f4d6c | -17.75997 | -53.81224 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab7ba3a4-e308-3e80-b6f7-79974d5d3782 | -17.34059 | -55.02021 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| fdb67710-261c-3505-bf37-8fffb06ffd78 | -17.33763 | -55.0144 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e10cedee-1d76-337b-a17b-fa9c4741f822 | -17.33673 | -55.01945 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d71b1bef-0656-3145-899e-538dc0ce3775 | -17.33582 | -55.02452 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9fd15969-3704-33f0-8176-597bdacd5f16 | -17.33082 | -55.00787 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 031e95b2-4ff2-306d-8e69-8d0d2f902ce0 | -17.32923 | -55.03899 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9f1dddd2-02b9-3ec2-9c7f-4b126dcbe092 | -17.32786 | -55.00207 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 70e03e7e-a922-3caf-9f40-f405c2533c55 | -17.32696 | -55.00713 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cdfbbed0-0dae-3b06-9615-ed8bb50efafc | -17.32605 | -55.01218 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 62a136c6-31c1-35c4-8579-4d9d67f301f2 | -17.17566 | -53.92638 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe791cfd-7919-3bb1-b628-ace5ba255245 | -17.15868 | -53.93726 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0176d46-caab-3996-8087-559c3ecbb45f | -17.1571 | -53.9462 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b7698b7-7eb4-3ebe-a001-2fe1d27a37f8 | -17.15424 | -53.94106 | 2024-10-08 04:36:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4957c2fe-a544-3cde-8ff4-0c41a9362e3e | -17.02397 | -55.07489 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 814e5b9c-c638-309e-8736-668bfbe91ce5 | -17.02391 | -55.07275 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b028dd76-2c38-3733-a48d-39ee10b50589 | -17.02299 | -55.07789 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75a22813-fb36-3670-84c1-febfc75d8e2b | -17.00014 | -55.02568 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f10085c-c157-3cbf-b3e5-44faae71715f | -16.99053 | -55.03441 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f85040a-3166-39e3-a272-e7e51d13de62 | -16.98665 | -55.03366 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 506fff87-540c-37e7-8338-ec3bd8ece36d | -18.08621 | -54.31343 | 2024-10-08 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8779a97e-1c70-38da-a62b-114034d4b36b | -17.77099 | -53.7915 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 63080aa3-f7a5-3139-83fc-d098d710476e | -17.76716 | -53.81364 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 36d3acf2-0953-3967-ae91-3a736a886530 | -17.7659 | -53.79943 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 28e14b34-0c82-39ad-9c52-856e8b172177 | -17.16076 | -53.94687 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7222f1ed-38cd-3952-8af4-d764e08ed065 | -17.15789 | -53.94173 | 2024-10-08 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96481070-6890-30b8-b661-714172ab41a4 | -18.20955 | -54.44884 | 2024-10-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 321fa79a-1135-377b-9a19-a2ffba70c3ed | -18.20586 | -54.44814 | 2024-10-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe803bd5-ad4e-3c84-b5f3-e9274adaf866 | -18.21245 | -54.45407 | 2024-10-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc36349a-16a2-3c81-aec6-2b52f9bef7e2 | -12.66469 | -54.71386 | 2024-10-08 04:36:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f26283ba-7f64-32c6-a783-ecc05a37b11a | -12.65992 | -54.71691 | 2024-10-08 04:36:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7f121fe4-223d-3fec-8acf-1f83625430d8 | -12.65583 | -54.7162 | 2024-10-08 04:36:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05170926-94d8-314f-80bd-6382fb20106a | -12.65508 | -54.69687 | 2024-10-08 04:36:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 824b836b-55cb-34a5-a074-19630cb1142f | -12.65242 | -54.71171 | 2024-10-08 04:36:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b43b8e58-6c7f-3f6e-bc78-5a97b78c6871 | -14.81373 | -55.91601 | 2024-10-08 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c453baf3-a49e-3423-89ce-ed69540bf3ec | -14.80991 | -55.89487 | 2024-10-08 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6670a7a-e31e-3c92-9870-c9f53179123d | -14.82678 | -55.89326 | 2024-10-08 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 924e402b-45ec-3204-81de-78bb5ccc3584 | -16.61505 | -55.55583 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0c021be5-8512-3fca-8da5-4831b7fc1bd8 | -16.61458 | -55.55585 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4e6813eb-3aa2-36d1-9cb2-e77d4880215c | -16.61437 | -55.55947 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fbdb9336-00e9-339f-a650-e47950bcae12 | -16.61369 | -55.56312 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dda5c738-252e-3939-bd8b-46b42d5738f9 | -16.60451 | -55.56538 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7f9f95d6-7405-32d3-9e3b-254d5cfbc656 | -16.60385 | -55.5691 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4b7319cb-5318-39f9-9940-f0aba5b602ea | -16.60208 | -55.89816 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 684c2faa-7259-3dcd-8399-51144ee66729 | -16.60136 | -55.90203 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 635bfced-d84d-3715-befd-a84e5005aae5 | -16.59456 | -55.89267 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0ca4cd23-23ed-3a9a-b2db-75d0b9410011 | -16.59312 | -55.90041 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 51ef0ea6-9809-397a-acf4-6823f2423327 | -16.58076 | -55.89798 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| cc19740f-5f23-3e1f-8006-2ca8700a48cd | -16.56694 | -55.9033 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| c11cf5e0-8d1c-3bdb-b958-9a1ad04b54c1 | -16.56621 | -55.90717 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| bb09ed8e-b941-350b-961d-33fe6f39917c | -16.56548 | -55.91105 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bcf238df-d5f4-3006-b39a-c3deee9292f7 | -16.56208 | -55.90637 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4654cd93-c74a-3701-bee1-9ad2e3e84702 | -16.56136 | -55.91024 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8931e88f-9be8-34d1-b6ed-75662d711dfd | -16.55796 | -55.90556 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ace76d7e-60df-30da-bc33-d7a978cb7eb2 | -16.55723 | -55.90944 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f6e0205e-052f-3919-a663-eb86bfc5ed4f | -16.5565 | -55.91333 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 725fe639-ef68-3b21-8a1a-56e455e3aa8d | -16.55237 | -55.91252 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f4fe709c-c060-3f1a-9f2e-bdf8b600e6d7 | -16.55164 | -55.9164 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| beeead3b-29ae-324c-9b29-dffc2458a649 | -16.54955 | -55.91646 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c93e3ae8-fdd1-32d3-ab91-9e16816655fb | -16.52534 | -55.9319 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b39fb602-4deb-3392-8e83-31cf523928a8 | -16.4217 | -55.94878 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 44b2288d-f6ef-342f-ad70-f270b4854a17 | -16.42099 | -55.95272 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 88f32fe3-1077-3eb6-8b45-c679788a072f | -16.41827 | -55.94404 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 924f2696-3816-3956-99ea-422549d27d34 | -16.41755 | -55.94797 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2ddbe3c0-539d-3dc4-9a10-78ac7b8c8409 | -16.41683 | -55.95191 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 63ca0a51-99e1-32b1-94b0-7cd3a114d81c | -16.15893 | -55.93386 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a739616c-2da0-3c0b-8b49-4b3caf89c003 | -16.13326 | -55.86372 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4f309a04-5329-3ff6-90df-9e30cb244dca | -15.904 | -54.94051 | 2024-10-08 04:36:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c003a02e-be5d-38dd-b723-2cf8974f0700 | -15.59109 | -55.08924 | 2024-10-08 04:36:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 761c5d07-4ee3-3c19-adbb-947aa09eaec3 | -16.61775 | -55.56375 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5d171000-3159-30e4-b56f-d1d8c19344e7 | -16.61392 | -55.55949 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fafa4d0b-4fb4-38a3-980d-0ce2be24fd3a | -16.61327 | -55.56315 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a5ac04e0-2f5f-3fd7-9cb5-3b7b5d373899 | -16.613 | -55.56681 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| eda86c7c-5401-3950-90fb-9db4a49d1cf6 | -16.61261 | -55.56684 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e47ef91e-37ab-3e6e-b905-1cf7a2acfef1 | -16.6062 | -55.89897 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| db25f87e-c10e-3e13-a700-4c72e225f35a | -16.60548 | -55.90285 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ab9585bb-9298-359a-a2e4-315062c9f434 | -16.59384 | -55.89654 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9b269267-f5fa-3811-8afd-928ed6dec06e | -16.58972 | -55.89573 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 51d1fa40-b95a-35e8-b4b0-ff51999b3fab | -16.589 | -55.89961 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ee07cbe2-d6d9-3e45-aa46-3ce0603ea1c2 | -16.58488 | -55.89879 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c0d1168b-9272-3f39-850f-b5ffab925da1 | -16.54885 | -55.92036 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7b786504-b591-3610-865c-bef8dc46adb8 | -16.54678 | -55.91948 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4cb6844f-90f6-302b-a219-6776683869d5 | -16.52605 | -55.928 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 35031daf-38a4-3281-9736-75e19b10c91a | -16.42585 | -55.94962 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 4f8c0cee-a0e2-3695-b0e1-2df4ac677d7f | -16.42242 | -55.94485 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 39915968-bb91-39c6-8f14-d0671f3d90a8 | -16.41341 | -55.94717 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c74289a5-b352-3c27-a4a2-e28bb83207de | -17.15941 | -56.13712 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2233b15f-6e8b-3612-82ee-1747e0cfc126 | -17.15311 | -56.14809 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 86dda772-7b7a-38d0-bda4-3a82fd20b4f6 | -17.166 | -56.13372 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 69d8b51a-2686-3f71-8193-97394571b1b0 | -17.16427 | -56.13403 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d302a8df-e7b3-3dce-88bd-c2ce55b19ee8 | -17.16355 | -56.13795 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b360fc90-87b5-3854-a3b2-6a624b5a254e | -17.16186 | -56.13288 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 4329ff5f-f6fe-364f-a937-f37e55aa47d1 | -17.16112 | -56.13681 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |


[Clique aqui para ver as próximas entradas](README66.md)
