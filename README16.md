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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b549d5f8-6962-361a-960d-83158503e466 | -9.60853 | -56.92653 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4eba38de-cd1f-3c49-af86-2e65f3be985d | -11.71688 | -59.35051 | 2026-06-30 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a34428db-3f0e-356c-8189-4e8570873b84 | -9.13173 | -58.25797 | 2026-06-30 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d3c7639-e0e5-355f-b5b0-56538610bbb7 | -9.17138 | -58.07187 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f04e07c-fd0d-32a0-80d6-346e50a28477 | -11.31182 | -53.94542 | 2026-06-30 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1f03f28-d337-3c71-9e2d-ca0234d91051 | -12.21386 | -56.55333 | 2026-06-30 05:16:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fdd09f6b-8f5c-3b16-b395-e5e9f6e6184b | -9.1466 | -58.24966 | 2026-06-30 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c19d5ce5-eb9b-346c-8b1e-264a67f3c66c | -9.32234 | -58.02085 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4def0a7b-2713-3c1c-a264-d93d1192e360 | -13.94755 | -53.95457 | 2026-06-30 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bdfd06f-915e-3ed9-9dba-80924d594192 | -9.5951 | -56.92443 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9429919e-4e7e-3f58-9f10-7c41866748c9 | -11.05377 | -55.76035 | 2026-06-30 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49d1b941-f60e-3cec-8229-c3e442bba6dc | -10.78889 | -54.10616 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a2abd48-3476-3c61-9763-afeeaf993bc6 | -11.21991 | -53.83447 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f0c39a3-d18f-3350-8c09-7d3413f2a821 | -9.32619 | -58.01789 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5df6e19-db4c-3a90-b36e-6273398feb2b | -9.61133 | -56.93064 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8959df0a-7abc-3ad3-a3d9-8adf4c690cff | -9.20079 | -45.32805 | 2026-06-30 05:16:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1e8017c-e077-3d30-8225-6280e11004f6 | -13.25443 | -56.79797 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e10bb22-10e5-3c2f-ae49-af704c6997ce | -14.63377 | -54.45782 | 2026-06-30 05:16:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 88e8c175-3ec7-35d4-9f91-b5f65d80231e | -11.05318 | -55.76441 | 2026-06-30 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdf78524-eb6e-3e5f-946c-d410cbfa6317 | -9.75066 | -49.03641 | 2026-06-30 05:16:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5989b556-293b-301f-b369-3eeac4e16136 | -12.51193 | -48.26968 | 2026-06-30 05:16:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 702d9e72-bf16-36ce-b4cf-1207fa3dd8d8 | -10.7186 | -51.66493 | 2026-06-30 05:16:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45789610-4ac3-3966-b62c-019eeb1c39f6 | -9.1536 | -58.2933 | 2026-06-30 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ded6b3ff-8c6a-39b7-9aec-4cb5bd530b21 | -10.12983 | -52.40254 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bb6dc71-9b58-3c7a-9280-28a6bdaed86c | -11.63237 | -59.00801 | 2026-06-30 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf7320c4-034e-3313-822c-b20aeb702d11 | -13.71635 | -47.87122 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d77438a-e515-36bf-afa3-9e0a4e81637e | -10.58687 | -55.42398 | 2026-06-30 05:16:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df7f4885-e56a-3175-a352-ef8854974045 | -9.08209 | -59.39112 | 2026-06-30 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4b75c0cb-04a9-37b6-a1d9-e8bc060a2910 | -11.78213 | -47.5736 | 2026-06-30 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da162ae6-ce27-3783-96b2-dc8e9d0643d1 | -9.12512 | -58.2569 | 2026-06-30 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eabe7a23-5f7c-3676-ba8f-de17f082126e | -12.21673 | -56.55776 | 2026-06-30 05:16:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cc4b1545-4d96-31ca-aecd-d63a3d0c8bf2 | -11.90713 | -57.37875 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a782ed72-965f-32af-b6ac-e88ab9ec9c39 | -12.21327 | -56.55721 | 2026-06-30 05:16:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c6125fa9-00ec-3daa-9082-92c8fdf3d26e | -11.9027 | -57.40779 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3b940f9-3557-3644-8077-ea2cf6c8b5ba | -13.2573 | -56.8024 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34a94a9c-1da1-30da-b4f6-787915976b37 | -11.89879 | -57.41088 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8107f27-1d62-37ce-a4d2-827a00db5498 | -10.06956 | -60.49727 | 2026-06-30 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f1c4980b-012e-37d5-b277-e873039801e9 | -11.92453 | -57.40011 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc93ba6a-2be1-3550-8629-0ab87cb37932 | -11.92116 | -57.3996 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82f4bf0e-4a18-35a0-99dd-43587fac4ee1 | -10.1253 | -52.41135 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 504abaca-deec-3ab8-9c27-cf9132d6e27e | -9.32124 | -58.02781 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb0bfdba-e0a0-3774-ac55-144308bd02ce | -11.79254 | -57.35001 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6db0b353-66b4-33aa-b272-844afe7ad988 | -11.90215 | -57.41142 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73d0c515-98e5-3ad1-96ca-7424b03d4287 | -12.51143 | -48.27394 | 2026-06-30 05:16:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6898417-48c0-31d8-ad2e-ebbf9e2c7cf1 | -10.29807 | -57.12602 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d78e99db-71c6-3db4-a819-c88985938332 | -10.30309 | -57.13785 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42879fec-b64d-399f-82a0-c33f1284d620 | -11.31713 | -54.46401 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b901bfba-2470-3ac8-9276-ee9967b1bfc8 | -12.22364 | -56.55885 | 2026-06-30 05:16:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3706604-fc51-391e-94a8-6a95139a191e | -12.52693 | -48.29292 | 2026-06-30 05:16:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d980753-7f3b-34b3-9e9e-e5f5709d795e | -10.04872 | -59.11394 | 2026-06-30 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68838d35-1b30-3dd0-bdea-fcf051ce8376 | -9.31738 | -58.03076 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4aeb02b-5a43-38e5-a606-06c5f6a9df90 | -11.58569 | -47.92419 | 2026-06-30 05:16:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b809867b-6b10-3868-b2a0-f5b867f2e79d | -9.0815 | -59.3947 | 2026-06-30 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5986250-0844-3930-82a5-a8dfe0ca62a6 | -11.9016 | -57.41505 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42ca62a2-726b-3ed9-bbfb-ca36723299b9 | -11.93535 | -57.70838 | 2026-06-30 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11019325-c03c-3040-a1d6-e4dc86e69e85 | -10.2496 | -59.30255 | 2026-06-30 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9f7538a-273c-3740-baa2-a23fcc75eebf | -11.63181 | -59.01152 | 2026-06-30 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 581fd5e3-5a1c-3542-8f2c-ad7b491e5401 | -10.77209 | -54.11365 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eee3d91-a1a0-3d8c-901b-2b1c47059416 | -12.4556 | -58.48626 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 70492c2c-01ed-31ec-8557-e7dbf9bd1e77 | -11.88613 | -57.12112 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b499ec8a-2911-315e-bb5e-aade75232eb2 | -13.70994 | -47.87364 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a31821a9-b7d3-3eb3-80d2-eb6230456859 | -11.88499 | -57.12852 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 761e6498-0517-328c-97f0-5f3381be546a | -9.60462 | -56.9296 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 42fdbeef-e65b-3e20-ae3f-bea9fc5f547d | -12.54285 | -57.19864 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cc9902d-0c6e-3222-b236-0bc9a8174a94 | -12.44566 | -58.48464 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bf7ef970-9fc9-3671-8509-48ff84264807 | -11.89966 | -57.12326 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 122e01d8-0be3-33df-a852-4024722c1bce | -9.1676 | -56.94631 | 2026-06-30 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7e33f6b-253f-371a-aa34-a57a0d3baf1c | -12.21959 | -56.56219 | 2026-06-30 05:16:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb2bb1e0-189b-3dac-bdcf-1c1f657bfa73 | -9.32289 | -58.01737 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17d43802-7827-3482-ae4b-05ba10e4227a | -11.51297 | -56.12034 | 2026-06-30 05:16:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f44a4c8-3203-3058-8d43-e53f6ae3273a | -9.60797 | -56.93012 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b3c4ddb0-5498-3446-9ac6-c921a2420319 | -12.20416 | -52.86378 | 2026-06-30 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fdd7b5bf-8c1a-3ce9-a680-e46bc3622297 | -11.89233 | -57.12589 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0aa1f1f-103f-3b93-815a-8db5ac94589d | -10.59045 | -55.42451 | 2026-06-30 05:16:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c635c73-9584-388d-8091-948f5772e01d | -9.74619 | -49.02895 | 2026-06-30 05:16:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2371ca29-6521-39ae-9d74-1dd3a8490ee8 | -10.90835 | -56.85508 | 2026-06-30 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ba1f027-bfe1-3c25-b792-b0e123b78e80 | -10.13924 | -52.40516 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87c43338-d670-366c-9ade-e63cbe6e4a27 | -10.12588 | -52.40736 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14d44ec1-687c-39fc-b3db-be93eae7bd4c | -11.23398 | -54.31792 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f2806fc-14eb-36ca-b8ea-a032ca32b40f | -11.90321 | -57.38186 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0d9ca90-8e53-39de-8b2b-bb143c046442 | -9.08822 | -59.3958 | 2026-06-30 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20ec9f77-8821-3af4-8aa9-64f001e57d46 | -11.71631 | -59.35404 | 2026-06-30 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 253aae9f-5847-368e-9b72-953d1bba3e9c | -11.89571 | -57.12643 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76b10b31-c800-3d2d-a7f5-f16047a81c9a | -10.69696 | -49.60807 | 2026-06-30 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8d15826e-732a-3ff1-9f23-c2eab19e7b4f | -9.2075 | -45.32888 | 2026-06-30 05:16:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21c2a719-dd5f-3e5a-b9b6-78152ec2d6f5 | -11.32093 | -54.46457 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc783adb-5be1-3e96-86dc-7c53d92712dd | -9.59174 | -56.92391 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17e7e400-c985-39f7-ba06-8ce7989d5e46 | -13.71738 | -47.86189 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8809a1b-496d-3e10-8bfc-5082b6e11c3b | -13.25847 | -56.79462 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ac0875f-544e-3ad0-8b34-29b420b6819d | -11.89064 | -57.13695 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 570ca743-bd3b-3b40-acce-ca049fdce3b7 | -10.69654 | -49.61127 | 2026-06-30 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7a5bc5dd-2be7-315f-8414-56dfad1851f5 | -11.22064 | -53.82941 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8ecc27a-1398-3c09-bfe7-daeb8db4517d | -10.05262 | -59.11094 | 2026-06-30 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c28ac105-31cd-36c1-88fa-54e5a237644c | -9.33335 | -58.01548 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adec5f63-64c8-32e9-a7fc-0994c445377e | -9.60292 | -56.9183 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c9827d2-c912-3999-8cba-63a21f764237 | -11.22701 | -54.31199 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bc475a5d-86b9-3f10-a168-8cebed864fb1 | -11.93479 | -57.71196 | 2026-06-30 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7a237cf-b134-3d55-96db-ac022bb4b061 | -11.90248 | -57.12749 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c9b1c26-2896-3c2b-bbbd-4373257fbd0c | -10.69739 | -49.60486 | 2026-06-30 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 85c029e5-1760-374b-b280-4e6dcdd6396a | -11.88838 | -57.12906 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README17.md)
