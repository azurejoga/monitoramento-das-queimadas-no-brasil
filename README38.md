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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7c380fa-cb1f-3521-b050-0cbe6c7bceb8 | -10.98626 | -50.9187 | 2025-09-04 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f44e43fb-10de-3a24-9776-f13054b708aa | -14.81505 | -48.21017 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e100f452-3d91-38c5-9356-bd0c17037970 | -13.4384 | -46.93133 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 119c3a34-39f4-3719-a530-7ad6a1420ffe | -10.70557 | -49.02072 | 2025-09-04 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae11afe1-4dec-3a71-b58a-bbb3e2a7ea9d | -12.94726 | -48.0632 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a84627d8-15da-3798-b8db-5c2e779ee0e4 | -12.91101 | -56.93773 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ccfa61e8-3bcd-3217-b8e9-78da391085a7 | -12.94672 | -48.06672 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c989720b-ef3d-3b96-9145-4c073733f0cb | -13.4498 | -46.94096 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9837a6d3-6258-38b3-a96a-f144ded6e34a | -11.65508 | -54.52555 | 2025-09-04 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2aaae67f-ede0-36d6-8fdb-0ae0d30fa93d | -12.85934 | -48.01593 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4f9d0c9-4357-30fe-821e-71431d33c765 | -11.64889 | -54.53384 | 2025-09-04 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1efc7189-714c-383e-88ed-13a0b7936df1 | -13.58396 | -48.12428 | 2025-09-04 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49154454-c7b6-35b4-96d1-7a7de4be45f6 | -11.63527 | -52.19616 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8cd9c06-e187-37d6-86a0-ffa8cafb0399 | -11.44004 | -46.90758 | 2025-09-04 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4029fb4-a1fd-3252-911e-51ee64fc26ed | -11.09301 | -45.12682 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33bfca43-a19b-33cd-a2a9-372f18738bcc | -15.00864 | -50.07204 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abdc0645-c3d5-31ed-819c-5b494a38324d | -13.70706 | -46.8809 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d50b388-afaf-33f5-a086-4415c6584b71 | -11.13708 | -44.63743 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f944c3c-1274-3522-9bdb-fff494ab6890 | -10.75594 | -45.27091 | 2025-09-04 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0316c17e-4733-39e1-a053-1a8498edbd42 | -8.73692 | -47.07725 | 2025-09-04 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05210940-1df2-3cb7-8706-032e94f0b182 | -6.74744 | -58.72722 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c4b347c6-5fc9-3a65-9c87-a754480adf6a | -8.44797 | -45.09533 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5f2aab2-dcd2-3b51-8b25-d1592ad964a2 | -14.56732 | -48.05299 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84a67b41-f056-3fe4-b3b7-6a993aa012e9 | -14.5973 | -48.0148 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a567081f-1264-3d44-a08c-54c26b717d33 | -13.56866 | -48.13221 | 2025-09-04 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 267af106-2e9a-365d-a6e4-f1a35966fcde | -13.26794 | -51.84655 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 04168423-ee84-345f-9c96-6be5c800953d | -14.58904 | -48.02436 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 192634d3-0b76-3e3f-b36c-d9d2bd5eb1ca | -9.62337 | -40.61131 | 2025-09-04 04:27:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a05112b-feb2-30c4-a8f8-c1520995cbbe | -6.74112 | -58.73008 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| b5b75293-a6f1-3e67-918b-4ef47e514efa | -12.46169 | -48.07734 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bbb3be4-7c40-33bb-9c0f-5b16e52762ae | -10.09361 | -54.79383 | 2025-09-04 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dba65a9e-7415-3667-b87f-ad1e99fcbd77 | -11.887 | -51.54742 | 2025-09-04 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84cca7fd-4ae7-39c7-894d-236dd17ec60c | -15.03166 | -48.10752 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a7e8e9e-678a-3a5b-abf8-5f65e1bc4f40 | -9.33862 | -55.21502 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc3cb49a-a780-338e-a61e-c12d7fbfccfa | -11.63052 | -52.20042 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 04a4ce2d-9ce2-3740-a059-d5ceaf2d0659 | -12.89071 | -48.03185 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 461b50f6-dcbc-3498-ac3d-c133a69a880f | -8.53368 | -51.32177 | 2025-09-04 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4adc7007-d43f-33d8-9c95-0d08acf097a7 | -14.55052 | -53.06593 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b886dcb-b9fa-35b5-bab9-10284bd91a6a | -13.74231 | -46.94215 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74295c8c-c459-309c-bedf-a15aa4fe8305 | -14.99173 | -50.06906 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efcef3ac-4b3b-3c37-b696-1a9007f77a4e | -12.90755 | -56.93433 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8f75ebd-9e78-39ed-ab1a-363db663dcb6 | -10.58534 | -55.4196 | 2025-09-04 04:27:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2569a22e-525e-328f-b6fb-ee92d2b09aad | -14.56669 | -49.13681 | 2025-09-04 04:27:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a921a9f0-9df9-3bb6-943c-e588ccd1bc30 | -10.50235 | -50.44594 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3670ebde-7955-35e7-b15f-a7cd5fa5373b | -12.97533 | -54.77536 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 499c4bb5-facd-3775-a13d-a72f7ab4bd5f | -8.36241 | -48.34616 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 456f5a5c-d90b-384e-8445-7d88553841b9 | -14.93421 | -49.05146 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14523e3a-bd45-3e24-b760-ba6aa6303dbf | -11.73801 | -47.74711 | 2025-09-04 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb529009-7beb-3215-93f6-42c3a4abc437 | -11.58384 | -52.16346 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d612bf6e-b069-3c1d-be9b-5c3f92b1124d | -14.55356 | -48.07613 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32700876-ef99-3905-972c-f209cab03b5b | -8.42793 | -45.71468 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 203baae2-32ff-3dcd-80c8-fbdd84403859 | -10.48925 | -46.76757 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff07c8ae-ead5-3d6b-b674-11da6f45cbad | -9.69039 | -48.99969 | 2025-09-04 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db556832-080c-3e1c-9775-c70a86e35fd1 | -10.43165 | -50.37138 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0696e19a-8afd-3360-b6ce-d71bec871fca | -8.8737 | -52.03006 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7345dd2f-3099-3c92-996f-c74c83498a0a | -11.59279 | -47.78426 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d431f04-a00f-3fbc-908d-2b7e784b476a | -7.60677 | -55.26615 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6d876a6-b4af-321f-8f9f-997cf771679a | -13.50063 | -47.01141 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a859f87c-9c00-3192-90f9-e0cdfc075517 | -11.67541 | -57.35416 | 2025-09-04 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0566059-8bda-32c1-86ee-1ef9c83d95e3 | -11.05079 | -45.14814 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| d43ae306-4812-3d8f-9cf3-3766df4c2b45 | -14.78204 | -48.13921 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10a4c515-bcdc-3295-a573-2c3339f13d25 | -12.18037 | -53.89505 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8569e639-ed0e-3073-9bf4-fbc36f4b813c | -10.09263 | -54.77235 | 2025-09-04 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 788e59d5-1c1c-3a41-89a1-bc1d0c80f2cf | -14.53924 | -48.05924 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6149827d-f93b-31f3-b0c0-32db6f8a116b | -9.43371 | -48.09696 | 2025-09-04 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8478dfc-1e91-377e-9658-d106b1360694 | -9.3362 | -55.21033 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| beea45fd-34d2-3632-b55d-f5de3ba3ad67 | -10.14679 | -46.25489 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b6c6a14-88ac-3e9d-95d6-f838d70da057 | -14.9991 | -50.06652 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8202ad5e-dc53-3c1f-b2f6-20f117fbe909 | -11.84439 | -51.44923 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41422558-ff12-3972-ae18-72929a43f378 | -12.77958 | -48.15459 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59a3ab55-0d3d-30c5-894e-58a0698d4d8f | -8.10292 | -45.48931 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e38240f3-9cf6-33ac-8b4a-bc66dce8c5d2 | -14.55796 | -48.0696 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8102cf62-f796-3d5f-a7a4-9bb183f0fce8 | -8.07962 | -45.34958 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6977d53b-2b3a-38e5-a64c-de7df50ebfef | -14.81284 | -48.22438 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fce570f4-a582-337a-a637-1221c7e2a478 | -14.78645 | -48.13265 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e9589f8-7cb7-3215-84e2-5158aea2b8f5 | -11.97682 | -45.79676 | 2025-09-04 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f43a2443-cd9a-3e6e-b09e-69daee96069a | -8.0768 | -45.34551 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88a96655-5466-3ca7-8ec1-9922fffa37f6 | -8.87542 | -45.85673 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fa8d8a5-f5a7-30dd-8ad1-55b81c52c161 | -8.53062 | -51.31639 | 2025-09-04 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c32b863d-6779-30aa-bec8-8566cc16fb40 | -9.54714 | -49.16859 | 2025-09-04 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7e1c276-0815-3591-9166-f8a24c1b8fc8 | -11.62751 | -52.19477 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dc5e4305-c355-375c-87ac-1fe279b48304 | -15.03344 | -50.07654 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e1cbc5f-6eae-3792-bb86-62464ad7d04e | -12.91272 | -56.93536 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64558e77-4912-376c-ad4c-1ad01d9698a2 | -12.94286 | -48.06969 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 757bcf2e-8fbb-34ce-ad98-d2f17134beb5 | -9.62804 | -47.08118 | 2025-09-04 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0b2f971-b771-3841-8b27-aa877cb11f3a | -14.5929 | -48.02137 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d4eecb3-71d9-36fc-aebf-d612e6e5c123 | -10.11932 | -46.16658 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2888059e-d4b3-37b4-82dc-beb96b5f4a05 | -14.82384 | -48.24073 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e175ffb-4f04-3abe-9c7c-178a4097c6c3 | -8.36973 | -48.34361 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40ada2cb-64f3-3039-99f8-cca3afdc3979 | -9.60095 | -47.03418 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 844ff902-0bd6-38f2-84ac-de98fbbad033 | -15.03566 | -50.04205 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46be7328-2418-38e6-8146-2796d7d734a4 | -15.0256 | -48.10289 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cf1fec8-8d48-38a0-bb46-296fbb9f8cc3 | -12.97168 | -54.76994 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ffef872-c711-3e90-855b-7957b24eb78c | -13.44087 | -46.93209 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc2c19da-32cd-3333-b04b-60d4be02eb7e | -12.89879 | -56.94552 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 276e76c1-b8b9-37db-b1e2-104a7814b2a5 | -12.96047 | -48.06536 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21810f33-c8ca-3228-9f80-f7d36c26ecc0 | -11.78804 | -50.64386 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9308904-b854-3432-925e-8b59ebb3883b | -7.74957 | -48.76902 | 2025-09-04 04:27:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 419505aa-8338-3065-bfd1-4743b38c919c | -13.44808 | -46.92969 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 859c628c-bfe4-3b2c-82e7-7c27c44ceb98 | -11.85749 | -52.42664 | 2025-09-04 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README39.md)
