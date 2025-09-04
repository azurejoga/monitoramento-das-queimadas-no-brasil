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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81533234-4106-3b54-b605-c41600a4d6a4 | -14.77281 | -48.14185 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 743b3b09-9c39-32f9-a197-9612043434ff | -16.30916 | -52.95393 | 2025-09-04 05:18:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfd740b8-04c2-39e1-9095-42e36d74c6fd | -11.19702 | -55.02626 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2a08fdb-5c2d-3d92-8db4-1471c6f36610 | -15.74071 | -53.63744 | 2025-09-04 05:18:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b591fc6-8ece-3341-8f3d-098fec6c3c3d | -8.44263 | -70.14208 | 2025-09-04 05:18:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f351dc2-458c-3588-a488-5532ce2cd9b8 | -11.58138 | -52.12182 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cd91a78-7983-3178-a186-46c79f960889 | -15.60935 | -52.8899 | 2025-09-04 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81091925-95d6-3f1a-8769-87954f3f7541 | -13.73753 | -46.92451 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c3fbcd1-336a-3cd1-b05e-cbc4163acddd | -12.18014 | -53.88536 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dce99769-bf09-396b-80d2-d5d2a5638714 | -14.38899 | -53.07347 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdc08b4f-aa3e-397f-9e1a-5fd8c08fd820 | -14.56995 | -54.54255 | 2025-09-04 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e00ee4f-c86f-34bf-805d-77d5a0cb47bd | -12.64289 | -57.00568 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b8406da-42cf-344a-b847-ea16a3dad2ea | -12.8979 | -48.0331 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c756e16a-1eea-3daa-b6fb-272ae0f58f90 | -13.44912 | -46.93185 | 2025-09-04 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3ff2645-b0b6-30a0-aa3a-7605fecd7a07 | -11.67524 | -57.35239 | 2025-09-04 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98147682-edcc-3d4d-a74b-1f6432317492 | -12.9469 | -48.06585 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 561ea50b-b7d7-35c0-9414-840fc982e846 | -12.98613 | -48.07227 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e972295-222a-39bc-be45-215b2740c282 | -13.74089 | -46.94292 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68e75cfd-85ff-3c68-b728-92365e130481 | -15.59449 | -52.88804 | 2025-09-04 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0da15ef2-5af4-36ac-828c-ad8b55589557 | -14.06204 | -54.03196 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ced091d-4f8f-3cf6-9661-70bb1372447b | -14.58462 | -53.03073 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea7d08c4-f2e8-3405-9255-8eaf8dd43aec | -14.54997 | -48.06889 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4496f04d-b486-346f-b9b4-1200acd73f7c | -12.6027 | -56.99972 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72647f3e-3892-397e-a375-5536350eb297 | -11.6542 | -54.53505 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02f0967e-b651-3114-94d3-c1498d3c6773 | -12.64416 | -56.99695 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92d173d1-0bd3-3861-b8b2-6c035bb5456a | -14.53219 | -48.07133 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e60617e1-10a7-346c-88f3-ba0b25d6bf61 | -15.02131 | -50.02837 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff7d6b9a-5d3a-3f4b-ae4d-abbd244f0302 | -8.8811 | -69.34892 | 2025-09-04 05:18:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 181f56b9-ce95-3bd4-93c8-ab444fad359c | -15.02083 | -50.03272 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0452d1d-e6fa-3398-8f59-2bc60257120a | -11.20913 | -55.08562 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d1bbfa6b-22da-37d1-adca-3f37f8083e07 | -12.89983 | -56.93284 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 28f55a4d-f303-3bd9-87a3-47acea93e4eb | -12.96995 | -54.76986 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b235e57b-4366-3c52-8cfa-a73dac4bd444 | -14.56574 | -48.04596 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8adfe9b3-42a6-3c0b-9ba0-7277126b3544 | -15.98755 | -55.97841 | 2025-09-04 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 744ea399-8f30-34a1-9137-906035f112ff | -10.87536 | -55.74035 | 2025-09-04 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 125ca1c9-b8ce-3459-be96-d372cec32419 | -15.15786 | -52.37452 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 105bc1cf-efd6-3911-b512-d2762074ecfa | -13.44168 | -46.93513 | 2025-09-04 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36513bd6-c1f9-36dc-81db-7ddbffe46b8d | -12.64176 | -56.98773 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6a698b6-8076-37bd-bb70-3482e0d7da73 | -11.85481 | -51.45209 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 696fc7e0-d8a6-324e-991e-ff10c6a4f5c4 | -12.88993 | -56.94925 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4b7f26ca-b1ce-31fe-9f38-022bd3a3d96e | -14.99259 | -50.07191 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b47488b4-ae6f-34cd-8968-0a97258d6fb1 | -14.59492 | -48.02408 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 050fca74-7215-3cf3-b067-bb5e07128783 | -11.62873 | -52.19807 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cca1f264-e19f-386b-9a45-67f9c3a5953e | -14.56845 | -48.0854 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 94205a82-4dce-3485-a199-8b0022d23e80 | -11.86586 | -51.53137 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6f5646d-2a07-3544-b6c3-21fbef274123 | -14.53851 | -48.04902 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04c85ffb-16f1-3a03-9854-716a6df73275 | -12.91212 | -57.00039 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6069a65d-0e8f-38bb-949b-c6065743d165 | -14.81847 | -48.33727 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8bb5419-46be-3c84-bfb1-6ff6af3e8edb | -11.6267 | -52.19583 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a39d5b6d-0d2b-3550-a7e4-d81844e6f3ae | -13.81249 | -56.60416 | 2025-09-04 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5eb33093-fada-3390-b72e-9d02b6a11099 | -12.94394 | -56.98739 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3d78eeca-f038-3c03-ac60-a605803f2998 | -12.87242 | -48.02386 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cfd54d9-d473-3fc7-a368-675bf9bfc71e | -12.45736 | -48.08773 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a427737-6eae-3aee-83dc-e26eb5a9445f | -13.81559 | -56.60949 | 2025-09-04 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27d666fe-e157-34b1-ace2-73d18a9c03ac | -15.55196 | -48.42071 | 2025-09-04 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 224cd100-de14-3fa5-8c21-4217d4c6efdc | -12.97307 | -54.77834 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92e17bc9-fbed-3309-ba74-d34938332ff5 | -12.89727 | -56.95037 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4630752c-b60c-3a00-a837-1c953df5a4ff | -13.10464 | -57.11524 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| ec12a5ec-9c2e-3982-9544-16214d48d3ee | -15.54805 | -48.40913 | 2025-09-04 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4919ec0d-fea1-3409-b694-b07065a68ee5 | -10.14933 | -68.53228 | 2025-09-04 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7834c8a3-840f-39c5-af5a-32e63b9b9132 | -12.63987 | -57.0008 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc8fab5f-2d86-35e1-9ca3-6aaaf3bb7e3c | -12.49887 | -48.06919 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d0a4401a-634d-332b-b61b-4ea2b9dfc096 | -15.30525 | -52.75761 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b6880d2f-e03e-34f7-8bbb-38fbd367c85c | -12.96941 | -54.77382 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c64585f-17a9-3055-801a-67c21f3c9059 | -11.63728 | -52.19146 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 184bf5bf-ecaf-330b-adef-4bd9c2d92334 | -10.25198 | -61.77508 | 2025-09-04 05:18:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32279382-f8bc-3e28-820b-0bf8294159c1 | -10.88682 | -55.74238 | 2025-09-04 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f1d144a-0c1d-3343-94fe-e9d225cc5988 | -11.1935 | -55.02208 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32b1c13d-b546-3986-bb10-6d8d32353c6d | -13.74331 | -46.93696 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0e2e806-d263-3f9f-968d-910e28c5334b | -11.63294 | -52.20429 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 530b6fa3-58d0-3066-8aa1-ef529dfa46ba | -11.83684 | -51.42694 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e5146c0-7461-3708-93c4-e8cf9f4503bd | -10.7869 | -52.76421 | 2025-09-04 05:18:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f8bde49a-1db5-37fe-8d60-2cc29a1d63cc | -11.87501 | -51.54179 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e609b6d-b149-3438-a513-0c28fb2dc609 | -14.5866 | -53.01485 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce78c4f2-d7dc-345b-bb1b-a0740693eb83 | -11.88652 | -51.53373 | 2025-09-04 05:18:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5fd8484-d81d-3d26-9a40-eb94bbcf4fe7 | -12.46446 | -48.08186 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf5bc129-6e01-3f9c-9c2d-13c444049ef3 | -13.85769 | -47.9763 | 2025-09-04 05:18:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1fbf0c8-7456-3c16-ba08-52b2ad657994 | -11.91346 | -46.66157 | 2025-09-04 05:18:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd8a56dd-d778-35af-bd0f-73cf1146be39 | -14.54004 | -48.06071 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57fab3a3-b6e2-30f5-8519-2798ae217ed3 | -15.00851 | -50.03565 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 741adf95-c3a0-3790-a521-492514838f62 | -13.56466 | -48.13676 | 2025-09-04 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e381c827-5edc-39a5-8089-a3acce85f59e | -11.87341 | -51.55435 | 2025-09-04 05:18:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45733836-93a3-34cf-8e6c-745c853aa1c6 | -12.90526 | -56.94712 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9eba9639-d0d6-368f-ab02-97948d8dac4f | -15.01535 | -50.08269 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81e7b8eb-0d42-3e94-b0cf-5629e49be3e2 | -14.57096 | -48.08563 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 078a510f-fd04-3f2c-a60d-5a49eb8d5b15 | -12.80819 | -47.66943 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0f41e48-556a-3280-a964-a655050490d7 | -12.96832 | -54.78174 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b415464f-eafb-3456-bd14-ef2bba315d8f | -12.98666 | -48.06765 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56e2e7a9-a01d-33eb-a858-26854450cf44 | -12.23852 | -50.14715 | 2025-09-04 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7270c586-5dcf-3467-8793-157816f15bda | -13.45545 | -46.93912 | 2025-09-04 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d7a47bc-2fb4-39c4-84e6-998da42610cd | -12.87902 | -48.02402 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6761d38e-c475-37d0-9e6e-049f54f3ebd6 | -13.81339 | -56.57071 | 2025-09-04 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cb1d033-2bf8-32c2-b67c-116bbacf299a | -12.90846 | -56.99981 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5ba2713-cb0f-3216-8547-8c2c539dfd36 | -8.88152 | -69.34848 | 2025-09-04 05:18:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a8b9826-41b0-396d-a83c-17e65fbfdb21 | -15.18166 | -52.34832 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c91c137-588c-38c6-8c4a-60528f897da1 | -13.10799 | -57.1172 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 50862586-f6de-3370-ba0b-7c0804eee168 | -13.0042 | -48.08605 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f2605ee-5265-3501-adba-75c2347c6f5e | -10.87154 | -55.73967 | 2025-09-04 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92948f70-33dd-3121-93f9-8f0d372669b4 | -11.59105 | -52.16295 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0b342f8-d986-3c29-9694-444adbebd5f8 | -14.9105 | -49.62436 | 2025-09-04 05:18:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README89.md)
