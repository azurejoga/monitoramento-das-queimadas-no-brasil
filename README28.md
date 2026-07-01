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
| 723e02ca-1330-3c26-8a3f-c0c6705b46de | -11.62569 | -59.01576 | 2026-07-01 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 02d9af18-c2f3-3914-ac5b-7d6dc0911b6b | -10.67029 | -54.53909 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 278572cd-86e6-35fb-b3a9-d68ebce0f2ae | -11.84416 | -56.94477 | 2026-07-01 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 59dbb5b0-5102-3495-964f-7fd931baf100 | -11.92169 | -57.3876 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c169d7c-e847-3904-98fe-360e8a0914a7 | -11.42309 | -56.06447 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 8b51fd1c-6c81-319e-bb48-018bc7990464 | -11.42025 | -56.06903 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 2fd376a9-2dc0-3901-a9bb-1bb12fd8bdaa | -9.17239 | -58.06154 | 2026-07-01 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18728b43-5b6f-3754-a156-e063d92b5103 | -11.63443 | -59.022 | 2026-07-01 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a005c099-056e-3225-93ed-301ab0c6fd6f | -11.43496 | -56.06214 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4d382c21-9f9b-368a-a65e-113c2692cb02 | -9.02948 | -59.54173 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7c8005f-ead1-316e-9c56-d2aa523c0040 | -11.84049 | -56.94658 | 2026-07-01 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d52ff5d4-c9c3-3dad-8cb2-506327f621cb | -12.41465 | -58.3878 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2717873a-5942-3ac5-a317-4494051684cb | -11.63572 | -59.01208 | 2026-07-01 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 37164465-61e7-3861-9d70-3f3aa6bdd4b7 | -11.88905 | -57.13332 | 2026-07-01 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cec9c57-a5de-3180-bd1c-d5a86ed4c14a | -11.42787 | -56.07305 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1e71ba95-aced-3ba7-9a21-f158a39eea89 | -9.17722 | -58.06226 | 2026-07-01 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44903393-b4ee-36c3-840d-1316fcdb4fa0 | -11.43404 | -56.06992 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| acd226ac-45fa-3f65-a988-564c02f6640e | -11.42833 | -56.06916 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a9cf402a-37e0-3450-bcf2-c13ba09b5eee | -10.12928 | -52.0908 | 2026-07-01 05:44:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b6e29e0e-2d86-3836-ae45-a9feabd4aaff | -14.6329 | -54.46966 | 2026-07-01 05:44:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78f918a6-c207-3825-ada8-29a5205a0a52 | -12.42104 | -58.38868 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 85916c37-3e32-3f6a-a359-d754caf8bddd | -9.02137 | -59.53619 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e32824bb-f0de-362e-8b13-d8ed6254eeda | -9.16979 | -56.93801 | 2026-07-01 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e4f5e29-ba52-3ac3-86e8-2036d0d4454b | -10.77334 | -53.54759 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e3983367-3f3c-36d3-8d2f-45cc8dad5ea5 | -11.92209 | -57.3843 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 178bfa3f-3005-3199-a20d-77bbb5f0025b | -12.14987 | -57.22211 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0db358e-d2a9-3bb4-9641-52bdcdcde644 | -9.07755 | -65.42178 | 2026-07-01 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c226c4f0-5334-3ba9-bbe2-c3be262de7b4 | -11.90066 | -57.3845 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cf10f02-e6ff-347f-b8e9-d17bf105da82 | -9.16936 | -56.94122 | 2026-07-01 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f09f4fb6-f3cb-3572-b6ed-af7e24e58882 | -9.08085 | -65.4223 | 2026-07-01 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab5384d9-6db0-3990-a1c8-d831b7bfa2da | -10.30176 | -57.12763 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60a95c4f-0f93-3405-ab53-bbd67489fa11 | -10.66585 | -54.52288 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d385c56-93f4-38f1-a77e-f63777d3b3f6 | -10.77175 | -53.54343 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c47ce573-cc83-32f5-bba0-32790de339af | -10.08217 | -60.49725 | 2026-07-01 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 890f78d3-aea4-3594-8e2d-33c6e0ff5eea | -12.41886 | -58.39425 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 57c88396-7502-35e1-ad24-661a4a3d77ce | -9.33389 | -58.01511 | 2026-07-01 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e8e8d80-7e5b-3938-8f8d-e3ab527e5dbb | -11.42447 | -56.05267 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 70ad70cf-06ae-3ff5-8f16-9fc14314a87a | -12.21654 | -56.56259 | 2026-07-01 05:44:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 49e5cc98-4e3b-3430-b39b-1b9ad0656f7c | -11.43927 | -55.91623 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b558159f-73b3-3ffa-bc91-369241387846 | -9.62129 | -67.32473 | 2026-07-01 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e29a097-c036-3899-ab0d-686190f9470f | -9.33488 | -58.02053 | 2026-07-01 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51b1a49e-d23c-3fc8-86d7-7cbb799b8712 | -9.6978 | -56.10015 | 2026-07-01 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 201c9d2c-ecbc-3780-9354-edf03ceaafe0 | -11.84372 | -56.94823 | 2026-07-01 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65c81d85-f1cd-33a4-84db-3eb979633f51 | -11.42971 | -56.05749 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| fc5e4ef0-133d-3019-9458-14e83e9714eb | -12.41541 | -58.39354 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d942ebaa-b7a5-347b-9f3c-95a0fc8336b0 | -9.02656 | -59.54 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e3fa635-fd5f-3ff8-9b1a-ae4031664378 | -12.41472 | -58.39923 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0a3d44a1-6323-3e23-8b35-fdb2aca3ea3c | -11.42596 | -56.06982 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 2ec8809b-83e2-33b1-8545-ce2e443c2e8e | -9.60079 | -56.92019 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4994953-5e08-3b48-b4df-185bc30faa71 | -9.60506 | -56.92797 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b332fc13-81ab-3c79-a574-1b459ba4c368 | -11.42354 | -56.06056 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b7b2914d-855d-3586-88e4-63065c2aca6c | -12.41392 | -58.39347 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c80bbac3-4f44-3016-8bf1-48aaa56affd7 | -9.69224 | -56.09936 | 2026-07-01 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 260914ab-abc7-3031-8455-4e11742487ba | -11.42925 | -56.0614 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 6e08fa60-4df6-3d8b-9b15-7703a0a52f1e | -11.43977 | -55.91214 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a68100d3-a43e-36c1-80a2-57286e911801 | -9.69319 | -56.09202 | 2026-07-01 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6f360ec-505d-36f0-aa5f-4ab75471106d | -13.26527 | -56.79988 | 2026-07-01 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63b9d20a-b92e-31ea-aca2-98385864f0ee | -11.88863 | -57.13672 | 2026-07-01 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07cf0cd8-4cd8-35e3-8ea6-49b4a9ed3aa3 | -13.26571 | -56.79607 | 2026-07-01 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00355141-678d-3245-9efe-fa0d9fa0b992 | -11.50204 | -54.50504 | 2026-07-01 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bff9a91a-207b-37a9-9865-854b444ca4e2 | -9.60023 | -56.92403 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b2eff1a-0f2e-3fba-9661-66fa9ac01de4 | -9.02713 | -59.53576 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3179095-44be-3740-a661-8a6a23c0962d | -9.09027 | -59.49706 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0821663a-9089-379f-9843-e00908a85457 | -11.44058 | -55.91513 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 401db6bd-8451-3642-ba73-110190300ada | -11.4345 | -56.06603 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a9ba98f1-d489-30f1-869d-f01d35d2e0ae | -9.61009 | -56.93133 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97e6cc99-cbc1-3ee1-89c0-fcbb0d723881 | -9.55093 | -65.68238 | 2026-07-01 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 054b4076-ce24-3f7e-86fa-2bd9543b277c | -11.8409 | -56.9431 | 2026-07-01 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 782b2553-35f9-395f-a4fc-35783e9f28f4 | -12.42035 | -58.39432 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 19ae6392-e450-38ea-95c2-a24284685894 | -10.77241 | -53.5376 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43428fe5-b0f2-3970-9a18-642828fd9fae | -9.17034 | -56.9401 | 2026-07-01 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90773b82-9b4f-3e61-96ec-a0b682958974 | -11.44106 | -55.91101 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98983c9f-d04e-3ec4-a5bb-efcef48bc78e | -10.27962 | -60.5398 | 2026-07-01 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29be93eb-b764-37f5-8ebb-95d26c7740ac | -12.41959 | -58.38861 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 14a1f353-5495-38cb-b708-d872ff9313e1 | -11.83832 | -56.94742 | 2026-07-01 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ce430f4-cea3-3060-8939-b3fbfa3a1927 | -12.22212 | -56.56343 | 2026-07-01 05:44:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ac33b382-cf82-367b-a250-3cfd66d52235 | -9.60524 | -56.92738 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6cea5f65-0aa8-3f08-aa09-4a78949f2208 | -11.04974 | -56.92192 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8343c07c-5325-3621-bad0-a7883cb46239 | -10.77835 | -53.54453 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49c5e5cb-27bf-3abb-b007-60e7e15044b3 | -12.41318 | -58.39916 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e3a9079-bf4d-32f2-af30-ecb9d80bebad | -9.60549 | -56.92472 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86d26f5a-ba17-35ac-b582-93821d209171 | -11.90071 | -57.38418 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0672f581-e025-3e48-adf2-df649e802e99 | -11.78815 | -56.99752 | 2026-07-01 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de384ee1-ba01-3165-b93a-ec852415590f | -9.08649 | -59.49212 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13d5c308-df5e-34c6-aa92-9b5f2de8605e | -11.90552 | -57.38854 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef7f1156-c34a-3a1c-a99a-8b4e7e800b4b | -9.69732 | -56.09829 | 2026-07-01 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c00ef3b-2568-3736-8274-fabdb7c2d529 | -9.03149 | -59.53641 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25b5ec99-4639-3b05-bbed-8d8a2d832aa8 | -9.60968 | -56.93454 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f890dfef-a05a-3278-8d96-604de062bd02 | -10.0844 | -60.49652 | 2026-07-01 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a585c32-c378-34d0-aa21-4f8a08e0c609 | -9.69221 | -56.09379 | 2026-07-01 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b27a211-6361-3804-b784-f0495686814f | -9.60483 | -56.93061 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e9176d3-d55a-3395-bdb2-e51bd3e49ddd | -11.83875 | -56.94395 | 2026-07-01 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d089d35d-df64-3c8e-b71f-00f274fbba88 | -11.42693 | -56.06206 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 53130016-5819-33a1-8e73-653c1310535e | -11.42401 | -56.05664 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 397f8039-e2bd-32ba-9ee5-0fece7b4be0c | -10.6777 | -54.52987 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 91e15f5d-a269-3ea9-b711-fb089a48b219 | -10.67207 | -54.52385 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| e5768d2d-cfcf-3b9b-9ede-b9487d65cf8e | -11.90145 | -57.37786 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcf3abc2-186d-3afe-9c32-800c3ed239a3 | -9.69777 | -56.0946 | 2026-07-01 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b39d921c-c599-3fff-b7de-1dfb52bd2e5c | -10.66644 | -54.51784 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b7bd0e0f-a4e6-3724-9765-294f83e54a03 | -9.59998 | -56.92665 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README29.md)
