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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1eb35575-a674-31c7-9402-9b8534b4dde7 | -14.02696 | -55.12012 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe023df4-3d83-3dab-9396-37dc5d869c7f | -11.5744 | -48.14013 | 2025-06-17 04:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9766e6eb-0760-30cc-bcbf-9e7eeddbbcc6 | -10.8547 | -53.77003 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db5efbc2-8406-3c1b-a685-169c08b187d5 | -10.29121 | -60.53486 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2db7ace5-3504-322b-a408-47c12a9a170b | -11.14502 | -53.9341 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 85d94940-717c-3c91-8f90-aef15b233ece | -10.27688 | -60.54384 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66faffe6-855f-35da-b13f-1e8854846b64 | -13.29211 | -57.07724 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d77c0472-c839-3e34-89ad-122f289bcaf8 | -13.39181 | -48.46296 | 2025-06-17 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7ba3d53-e84d-3852-aa38-ac555d4dc5b5 | -15.27065 | -51.47281 | 2025-06-17 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d7847ba-7968-3ce9-b92f-17ee01e69e4a | -9.40478 | -48.41491 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6dcd359-2a40-3c6a-a5bf-2a6eaf553644 | -12.02744 | -57.08903 | 2025-06-17 04:57:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6855397c-1e74-3cb7-9645-5cae357dc3ef | -10.29552 | -57.13906 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12572c80-182d-370f-b3b2-9feec6114a5c | -10.87696 | -54.31055 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1039ae1-f941-3357-9d06-37278bc3edc1 | -10.27409 | -47.61018 | 2025-06-17 04:57:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 710d5423-4846-32db-bd72-61a6852b294b | -15.26278 | -51.47164 | 2025-06-17 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e85a2af-2d92-3354-b859-28e2f2698efe | -10.33723 | -48.10188 | 2025-06-17 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de20650a-8780-3085-bbcc-9e61e7d7bb05 | -10.8463 | -53.77987 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e8de8c8-8aae-33d2-90fe-907a625bac5b | -12.52455 | -57.22086 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b20864f-72dd-3c26-a99a-17edc9d3cf05 | -16.30033 | -52.93476 | 2025-06-17 04:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3d161fb-6ba9-39cd-9207-b42c54300bc2 | -10.28577 | -60.54161 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca397148-4116-375a-9b56-eb49f009ece9 | -12.65478 | -54.11054 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfa77bb8-3dff-365f-9c7f-36c6a459f216 | -10.36213 | -57.2286 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eff69390-120e-3bb9-9095-51110ead4188 | -10.45087 | -47.94728 | 2025-06-17 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73115385-8686-3f9e-90c3-b91239969fe2 | -10.93456 | -56.83739 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 053ff8a5-68be-340f-9838-142a04a6f700 | -13.89484 | -48.73331 | 2025-06-17 04:57:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cd659fc-b3c2-3789-9cb6-8f31707f8ee1 | -14.27936 | -57.50317 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 807f2401-7818-3f1a-80b8-887ae6748ad0 | -16.59431 | -45.87907 | 2025-06-17 04:57:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39ad8b81-2546-3408-8f1d-5c6e2e5934e1 | -13.58704 | -54.28783 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 933f7b23-c92e-3eb0-8866-87560b92f1e7 | -9.40983 | -48.41109 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7404c848-41c3-37d3-9fdc-0f81fbc71f63 | -9.38966 | -48.42615 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fde72694-fdf1-3c16-a7a7-6048ba43c7d6 | -12.23195 | -44.21095 | 2025-06-17 04:57:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db594208-82cd-3619-9d96-58dd56d6e1fd | -16.29603 | -52.93867 | 2025-06-17 04:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 634d58be-2e88-32f7-b831-3f12d195c8a9 | -12.6576 | -54.11474 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af24c94b-7f77-35d1-af2c-a3eb0eddc376 | -11.13775 | -53.93665 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 19602755-0935-38ea-811c-bd7247ad5ebe | -11.0825 | -55.06136 | 2025-06-17 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 88833a5a-c7f5-394f-97bb-5bdc7e134b6c | -12.08899 | -57.37497 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2a53477-0591-341d-bc6b-6ebe6bade675 | -10.93581 | -55.32475 | 2025-06-17 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1805ca3-d7a5-3373-beac-894cca2bddfb | -10.93635 | -56.82639 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cfe1311-79ac-35ec-aa2a-ea5feb86c2e8 | -11.56549 | -54.57546 | 2025-06-17 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0311f691-ed91-317e-b2b4-920b2d9b5b0a | -13.28934 | -57.073 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f762da7f-0cd4-340f-8567-6cc99fb899c9 | -10.93237 | -56.82947 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d9c0d059-f670-317e-95dd-e0c30193deff | -9.413 | -48.42059 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18eec485-a109-3a3f-b676-3e81edc55b65 | -10.84458 | -53.76847 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ab06398e-b13a-348e-a956-891ed833eb65 | -10.28776 | -60.53031 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 892d9d41-d83c-3847-b07a-a0ac78832c83 | -9.67313 | -48.77042 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a7d6bcb-974a-31b7-87c4-6cbc7409864a | -12.20764 | -49.62948 | 2025-06-17 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1105a71-6c66-37b5-8cbe-9783334f3564 | -14.84873 | -52.28116 | 2025-06-17 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1835777-ff41-3c4f-a75d-4cf16635ed83 | -9.45923 | -57.85101 | 2025-06-17 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0931017b-d4ad-35fa-84d1-94dd75570af0 | -10.3366 | -48.10664 | 2025-06-17 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23e553ed-7b77-302a-84ea-f536b4b1061b | -14.03251 | -55.12839 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6de2eaf3-f74b-345c-86ff-531460a7adcd | -12.50851 | -58.35315 | 2025-06-17 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e2906bf-ea84-38e1-92da-2aa898f22a9d | -11.40354 | -47.62632 | 2025-06-17 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aced47e1-dc7b-39cb-bc09-b829d928dc01 | -8.51683 | -54.76729 | 2025-06-17 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3ecc431-bede-3ab4-859f-803f1682429f | -10.33692 | -48.10455 | 2025-06-17 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfe306d6-7a61-3271-b7f0-d2c3fd3ef88d | -10.93526 | -55.32826 | 2025-06-17 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd2bafa1-1f12-3b6d-ac03-afa713f46525 | -12.23089 | -44.22017 | 2025-06-17 04:57:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| becee496-5273-3fed-88a4-4600bee46e77 | -14.85916 | -45.12941 | 2025-06-17 04:57:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1174211-070c-36e6-a7a3-a467bee638df | -10.29598 | -60.53187 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f1db05e-3131-3f11-8e16-d37e49f67736 | -14.20301 | -57.41037 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9928944b-4f2a-371f-8690-d0be230950fc | -15.62749 | -57.30631 | 2025-06-17 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f573d42d-8e04-325a-99e9-024045d34c10 | -10.93857 | -55.32879 | 2025-06-17 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49fb95e3-c34f-36cb-a8e2-ee3ffa13cc91 | -11.1383 | -53.93304 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 499c77a9-7f96-35fe-a3e5-648856e1efb0 | -9.41806 | -48.41674 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f8ce844-b430-36da-baf2-5881fd80c9e5 | -11.56991 | -54.56889 | 2025-06-17 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c0677dd-f069-37ed-98dd-e62782857c18 | -11.89284 | -47.46413 | 2025-06-17 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51887c47-fe19-3d7d-b8e3-150eda306cff | -9.40795 | -48.42436 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc1e2c8f-e925-3836-a215-ba29d2c73dac | -14.04492 | -56.04888 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 902ab967-8f9b-3340-ae13-88bc44abff7f | -10.87864 | -54.32174 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3db80659-f07d-3cf7-9af5-3461a1eddef7 | -11.80551 | -57.34805 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02554995-75ad-32ee-a8dc-936750f854f8 | -9.46615 | -55.93383 | 2025-06-17 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1736dbd-b1a8-3551-99d6-da118e2dbb02 | -12.42794 | -50.03001 | 2025-06-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b7031c7-2e44-3205-9ba3-a3ebc884934c | -12.42847 | -50.02619 | 2025-06-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b541232c-1ed4-3f2b-8fc6-3d9c64bc5f55 | -9.39469 | -48.42246 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61aedbc6-852b-3f99-86d3-3b77de683e56 | -11.39254 | -47.63564 | 2025-06-17 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| deae77ce-9bac-3465-a7e2-084506ffd6e1 | -13.96298 | -56.79543 | 2025-06-17 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1557fc28-3830-380d-876b-24e5a029152c | -10.27885 | -60.53262 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e59ea64-9a7c-3c72-98e2-30eaab6a1bef | -9.88184 | -47.80949 | 2025-06-17 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8aa908b9-56af-3bab-a27c-526d7328623d | -15.07942 | -48.94422 | 2025-06-17 04:57:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 805caf1c-624e-30cb-abee-ce0c6338222a | -9.46338 | -55.92973 | 2025-06-17 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61ae2396-650b-3b75-bfce-0933bd3912fe | -13.72271 | -58.68238 | 2025-06-17 04:57:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6db8832a-05c0-3a35-a0dc-297c107af57a | -15.26282 | -51.47517 | 2025-06-17 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d08fd1c1-7e2e-33e5-8091-cf3209d3ce78 | -10.28297 | -60.53335 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a843d5e-fb17-3a58-b678-9ae76b4e6d3e | -14.03029 | -55.12067 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c50dee8-233f-31d6-baf1-8a33999fce66 | -10.84851 | -53.76536 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53d0ef07-fcd0-368b-ae0a-700ab884cd8f | -13.28994 | -57.06936 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47e97c14-48dd-3134-80e6-7f61bb2d1d3c | -10.29145 | -57.14232 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 741fd779-36b3-30f6-ae54-93d534036aea | -14.55029 | -53.66543 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eed32f30-7157-3480-a836-b5d3ff9fccf8 | -10.93177 | -56.83315 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4357d31-ba78-3ba3-8244-78208359fa42 | -14.02363 | -55.11958 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ae6f90f-3ce8-3167-b90d-e697c3616172 | -9.6682 | -48.77402 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 228568b1-9b5d-3430-922d-0f80a366f431 | -11.0091 | -55.05322 | 2025-06-17 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6ede984-12bc-3411-932d-bb1ab7a4f05a | -9.41363 | -48.41615 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 364f53a2-9a5a-3316-9981-8ff2ab1be2e4 | -16.0904 | -52.08413 | 2025-06-17 04:57:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9dbd178-9a93-3856-9308-82b226d052df | -12.34499 | -49.30758 | 2025-06-17 04:57:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 742955dd-82e2-330e-a271-7cfbd810a931 | -9.41426 | -48.41171 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abeb89ec-236d-335f-8381-1be2dad89c83 | -14.20361 | -57.4067 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 134d70d1-8393-31a5-8d92-32c60481d3f0 | -12.16922 | -56.53738 | 2025-06-17 04:57:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f51ac879-7800-3994-9116-2efa9944b0f4 | -11.84394 | -57.8592 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e6bbe8a-32e7-3659-991e-a05114f176df | -10.35868 | -57.22805 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dda91a3-e629-3122-86c6-9fb409c02bae | -10.28512 | -60.54535 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README20.md)
