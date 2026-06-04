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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 744cbd59-33f9-36de-a00a-14ec657f6185 | -9.37182 | -50.54008 | 2026-06-04 05:01:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c839266-95b9-3673-b1b0-f587ee98680b | -12.43867 | -58.41635 | 2026-06-04 05:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d627516-56b1-3b1f-9728-b248c7689b9d | -8.28255 | -48.22627 | 2026-06-04 05:01:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0991bd18-0612-3516-97ed-857c4f5ed152 | -10.54872 | -46.61805 | 2026-06-04 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d23e0755-3e24-37c0-851b-06ac6b03552a | -11.88735 | -57.83393 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fb1dce2-baec-3674-adc3-a89c0d0af7fa | -8.04936 | -46.79552 | 2026-06-04 05:01:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a30420f9-bd23-320d-8127-2d9b28193701 | -10.13752 | -49.15422 | 2026-06-04 05:01:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6c90225-2edd-31de-ab29-b2e8f5ddaa26 | -11.58945 | -58.50706 | 2026-06-04 05:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2619e33f-db10-394e-82aa-b3fa185837e2 | -11.54638 | -52.78612 | 2026-06-04 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bc991c1b-05c5-3bb0-99b8-426e75e037f9 | -12.45163 | -58.46914 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f5999648-db44-363d-806d-df7081b05747 | -12.30192 | -47.90763 | 2026-06-04 05:01:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e6e4025e-e6d3-3ef4-9766-d527d3f1ab74 | -11.59741 | -55.33143 | 2026-06-04 05:01:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d4a9a14-1e42-32a6-bd17-ea0d4d0ca230 | -12.54897 | -57.18821 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e00e54c-f06a-34fe-93e1-127606de878d | -9.03812 | -46.32038 | 2026-06-04 05:01:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c64caac1-c434-3b02-bdad-a5589252783b | -12.2184 | -57.27778 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5ffebcf-481f-3a32-ba44-81910f5a9b7f | -11.60688 | -55.33682 | 2026-06-04 05:01:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b9d8e7a-70d0-34c8-a305-2a3c0b2b833c | -11.88388 | -57.83331 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d4efc75-95dd-32b8-9fd9-737adab77eec | -11.78835 | -57.35311 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cd0f954-5e76-347e-952c-5beff47b6943 | -9.89109 | -47.85782 | 2026-06-04 05:01:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc25aeb2-7e60-3499-86d3-eaf7a979640b | -11.54578 | -52.79008 | 2026-06-04 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6830ec57-9543-3f57-b7c1-5f62bf1b04b5 | -12.22458 | -57.28268 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| d5350bb6-d46b-3e8d-ab5a-96597494e28a | -12.23322 | -57.27264 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4d7f9aef-a51f-36df-bc86-f2921553ad93 | -12.46651 | -58.46756 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d483c986-ab03-3588-b13f-07da3d9e4a30 | -10.86395 | -53.7479 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bc35c6c-1a9d-3ea7-838b-aacfb77725e2 | -12.22302 | -57.27092 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8cceeb57-59ec-3fe1-97b0-9d5795f8a09f | -14.04832 | -46.34341 | 2026-06-04 05:01:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc9a71c6-ff6e-33dc-b071-513b6356cd0c | -11.27069 | -53.97065 | 2026-06-04 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a01dbeb2-5ba6-39b3-80e3-d3e5d8f57891 | -9.3648 | -47.08601 | 2026-06-04 05:01:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 635ed314-2e15-3675-b69a-cd65a8bd31f0 | -11.54929 | -52.79062 | 2026-06-04 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a79857b6-0a6a-3401-a406-6a2ef5447cec | -11.78752 | -56.99722 | 2026-06-04 05:01:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8f1112d-2417-30ef-b04c-f781425efc24 | -10.61177 | -46.71487 | 2026-06-04 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5620ae27-ba37-3d48-9d3b-e7671f7ef7e1 | -11.74248 | -57.82653 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fdf7e64-b108-3359-a54f-9170dcb61015 | -12.45873 | -58.47037 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8b9f3ae4-6420-3e34-a25d-f3915e2d2b0a | -12.43721 | -58.40349 | 2026-06-04 05:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 704843c6-a467-3e6d-b353-ba45c18854c9 | -9.03852 | -46.31741 | 2026-06-04 05:01:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18cd3088-47d9-334d-b70d-85f4ab5cbf0d | -12.26741 | -58.18466 | 2026-06-04 05:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e7ea1ac-8395-3c42-9b52-4199b5c549f2 | -10.85663 | -53.7505 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8928db7-0c6b-3e31-b0f7-b0819e98caa9 | -12.22241 | -57.27464 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 8e868b3b-44f4-3064-ba96-f5958847f5cc | -12.4545 | -58.47381 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 242fae53-d427-3d78-97c5-be87bd7752f4 | -10.57294 | -57.31651 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 274f718e-7a80-3955-b126-650df30d96f1 | -7.34701 | -49.82255 | 2026-06-04 05:01:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6cc7600-1d18-3023-baf5-35ce6870b8c0 | -10.38155 | -49.44534 | 2026-06-04 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15a2c474-6a56-39c1-a04a-2b905ff96004 | -12.46296 | -58.46694 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 10db000e-07b9-3ed8-8a5e-dc92b759eef7 | -12.21779 | -57.28151 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9ebb3daa-8a25-3d1a-b778-12f15ec42caa | -11.27233 | -53.97057 | 2026-06-04 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d82e5424-8ebf-3756-85c8-fbfadac45e4f | -12.73498 | -54.19733 | 2026-06-04 05:01:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05665923-82b0-3d6d-8682-0652b2908585 | -11.88453 | -57.82941 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b10f55f-9b18-3d50-bc92-f0a12a97c881 | -8.57239 | -45.99602 | 2026-06-04 05:01:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7eead0da-e447-333d-bbbc-6f2565db8c40 | -10.60979 | -46.69034 | 2026-06-04 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4cd80c66-8bcb-3298-a832-b1685868be46 | -11.2634 | -53.9732 | 2026-06-04 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04868d90-ff41-37d2-b03e-30633f05bd29 | -11.63012 | -55.18949 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cd0f6dd-b87a-3696-8c19-464e64e92ebe | -13.95579 | -46.18295 | 2026-06-04 05:01:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1f445d7-321d-38f9-a2cf-59fd9d1d22bd | -11.61019 | -55.33736 | 2026-06-04 05:01:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e933549c-372f-359e-8d55-972e8af948a2 | -9.80526 | -48.2446 | 2026-06-04 05:01:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90482df3-0cc3-32dd-ba41-d80696463045 | -10.38993 | -49.44662 | 2026-06-04 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 178899d0-659f-36a9-8393-66792fc1a1fa | -11.62737 | -55.18544 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a5deed15-e6c0-3b00-9c1d-03a0f6246ce5 | -12.2286 | -57.27952 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a3060bc-29bd-3e82-aa50-6db2bdfa3269 | -9.16825 | -58.07086 | 2026-06-04 05:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 685e918f-3753-3f24-a714-17bb1f4552dd | -10.80756 | -56.5917 | 2026-06-04 05:01:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d664f1a0-e888-34fc-a86c-9e790e216c25 | -12.73554 | -54.19366 | 2026-06-04 05:01:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ee98ddd-b79d-3953-8ae1-7fa1f5fd9f9a | -10.3821 | -49.44147 | 2026-06-04 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca48848a-ae99-36a5-b7aa-96ac2ed55af5 | -11.53032 | -56.97757 | 2026-06-04 05:01:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19cc0584-98a5-34b4-848f-23950481c05c | -11.48419 | -52.91395 | 2026-06-04 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 870efbbc-8f13-3fb5-af5a-ff5dfb6db827 | -12.3129 | -47.8983 | 2026-06-04 05:01:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8061ed6b-af54-39ca-94bf-667cc78e033f | -7.34625 | -49.82755 | 2026-06-04 05:01:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c06f4d93-578d-3524-8ac3-efb361ca859b | -10.55419 | -46.61589 | 2026-06-04 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef1977fb-daa8-3b1a-810b-063a7784488d | -11.63663 | -58.24745 | 2026-06-04 05:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31d864a5-7d6f-393a-879b-a1a3d4bf023a | -10.38938 | -49.45047 | 2026-06-04 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d05eae07-f4e1-39f5-95dc-30d0be3f2880 | -11.258 | -48.35486 | 2026-06-04 05:01:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bc5024a-6598-3303-a931-e5bc6efb7520 | -10.53329 | -46.61695 | 2026-06-04 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 014b404b-2bdf-3890-89e5-3ec3370d1e4a | -9.89656 | -47.86102 | 2026-06-04 05:01:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c39e3991-6e10-3e13-83a6-f3e40964ed9a | -12.2218 | -57.27836 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 08eb411d-da1f-3131-9f4d-4bb46c0c7a1a | -8.07235 | -46.18221 | 2026-06-04 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afa038c5-3b17-33a0-b42d-0143e93a618a | -8.57195 | -45.99926 | 2026-06-04 05:01:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cf06b05-a1f2-364f-a58e-66ff9d6c96db | -9.89263 | -47.85537 | 2026-06-04 05:01:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0809a989-b94f-3ae7-a786-ccdb546ee537 | -11.62064 | -55.18411 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 903579ce-d884-3344-b10d-b498637211f4 | -12.73892 | -54.19419 | 2026-06-04 05:01:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7c6e451-44d1-3226-90da-89e770e453cb | -8.29456 | -48.23679 | 2026-06-04 05:01:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be357a69-1a6e-3e5a-8f6a-69e287fc2113 | -11.61734 | -55.18357 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a80913cd-f037-3f3f-aa89-220ac0497cc6 | -11.5534 | -52.78719 | 2026-06-04 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 768bf2ba-443a-3945-b66c-83b843919610 | -9.37567 | -50.54065 | 2026-06-04 05:01:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e725b0a-02ca-3d10-afd8-f70ea9cbb2bb | -10.90326 | -54.1276 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3238dd01-70a8-35d8-a17b-a4928814d58d | -7.34994 | -49.82927 | 2026-06-04 05:01:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05afb5cd-7382-309b-912c-eafeeab436ea | -10.84932 | -53.75309 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bab6e25e-b40c-3025-b0b1-54321cff0d0e | -12.4616 | -58.47504 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dda2726b-1be7-3442-8986-d6b5ffb19444 | -11.26116 | -53.96542 | 2026-06-04 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b34accc-bb62-3d6e-ad50-53e5ff2c406e | -11.33906 | -53.96249 | 2026-06-04 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 58585084-cef1-31fb-bd48-0fe569f8fe99 | -11.7909 | -56.99778 | 2026-06-04 05:01:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1cced183-257c-34cc-9e84-4303156c95e7 | -12.21717 | -57.28524 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 51240be8-bc76-3346-bbb4-9dc006cf842a | -9.62578 | -48.87896 | 2026-06-04 05:01:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2e8b2a3-8781-30de-8605-a87df1600121 | -11.60743 | -55.33332 | 2026-06-04 05:01:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c04b01c2-1f3f-36df-b3e7-40850704cfc6 | -10.90215 | -54.13476 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0d2f66b-489c-3ca5-a833-07f4014903a1 | -12.21656 | -57.28898 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9ede0490-29b7-3ab3-a4f0-504f0c2e6ea1 | -12.55592 | -48.3507 | 2026-06-04 05:01:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04b8f307-f9e7-3fd8-9f0f-3d856a39f0bb | -12.43513 | -58.41571 | 2026-06-04 05:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 938365cf-41b8-3646-a4fe-77300b6be4a6 | -11.79239 | -54.01774 | 2026-06-04 05:01:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa77fc81-1c02-3067-847d-362a283dffe1 | -8.29015 | -48.23611 | 2026-06-04 05:01:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 416e5e73-d3e8-3810-93e8-01dac738d452 | -10.57104 | -57.328 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8f5b08c-3a9a-3cc5-ba83-ce76408cb147 | -11.62009 | -55.18762 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f4f7eec-2676-3f9d-b90f-e7fcae23edc8 | -11.89147 | -57.83064 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README13.md)
