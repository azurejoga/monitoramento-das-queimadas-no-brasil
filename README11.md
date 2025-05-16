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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc5b83f8-eca2-3e3b-a968-ceb5f0ea78b4 | -11.55558 | -47.6189 | 2025-05-16 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36d71984-79a7-3177-a7c7-5237db25b6f7 | -15.26796 | -51.47219 | 2025-05-16 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12eb3bc1-4fb7-3f55-9fd7-809228fa431e | -12.87394 | -55.06464 | 2025-05-16 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59ffe782-3f88-3b45-a5ce-d1ca99464a12 | -17.05413 | -45.92072 | 2025-05-16 04:57:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6194fdd9-bfaf-30a7-9e29-4cab856f6a0c | -14.47199 | -56.32565 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fe936d28-51c3-338e-880d-7a8bae96ba20 | -11.16242 | -48.6765 | 2025-05-16 04:57:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| afa028dd-0b66-377a-8c40-ced11996e92a | -12.12193 | -54.664 | 2025-05-16 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a52d512c-ff53-376e-bed0-0925afef2b5a | -15.26936 | -51.46189 | 2025-05-16 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60851bfc-52aa-3e6f-a866-3cac07287141 | -11.89987 | -56.41116 | 2025-05-16 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 478b6670-ee52-339d-a638-117441f74929 | -14.18257 | -45.48269 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8973441-27f8-32c8-9933-9a51ff84e4d4 | -10.3466 | -47.984 | 2025-05-16 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1494ae7b-a47d-3c64-818b-6ef39a558fc5 | -17.05456 | -45.91652 | 2025-05-16 04:57:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 931f4057-d15b-3c12-96d3-d36ca4e1ceda | -13.04034 | -53.71901 | 2025-05-16 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99ec8a45-00a7-3030-bff8-793dc068a896 | -13.9602 | -56.78653 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcf0b4b3-4711-33ea-96d1-94aadcd81404 | -14.00891 | -53.04189 | 2025-05-16 04:57:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1d086bd-b93d-3386-a72b-ff58c6f2da25 | -11.34863 | -55.09461 | 2025-05-16 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0328bd87-6536-307d-9a99-982bc7deae2a | -11.58548 | -47.87177 | 2025-05-16 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17d8735d-456b-3132-8af8-a4e9da4906ac | -10.45966 | -49.05037 | 2025-05-16 04:57:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ee0903d-8d39-30ca-8a83-4cdb1f7f0e89 | -10.34495 | -51.6904 | 2025-05-16 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83877f01-9d55-32e6-88ad-2530a7783ccf | -11.78389 | -47.35208 | 2025-05-16 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7f050f73-e046-396c-9231-91033a30491b | -13.67473 | -53.9425 | 2025-05-16 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f880908-c195-34e8-af5f-6a3ca527ce9c | -14.17291 | -45.46485 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69045f2e-e06b-38ac-8e38-f88303362412 | -15.27259 | -51.46762 | 2025-05-16 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c9220d7-a63e-394b-9933-f1879ea5e11b | -12.34598 | -49.95596 | 2025-05-16 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 396f48a7-f12e-3bd3-8ba1-806c1481fd54 | -12.37221 | -47.32642 | 2025-05-16 04:57:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41474898-9687-34f3-9af8-68522708c838 | -12.72571 | -54.97154 | 2025-05-16 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5453ce5a-b87a-3d9f-85f2-3972e8366e7d | -13.39191 | -48.44986 | 2025-05-16 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9353da9c-965d-3b47-a57b-02794e1fe0c7 | -13.09238 | -52.29622 | 2025-05-16 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55b9e79a-2b93-3dd2-b4b0-9e8331675c70 | -11.58589 | -47.61229 | 2025-05-16 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b186217e-5da5-389c-a289-d3d77b109356 | -12.45831 | -57.20302 | 2025-05-16 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3e5d775-b162-3f8a-8b6d-8485bb741568 | -9.92416 | -59.92558 | 2025-05-16 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03f6d247-0d3a-3b19-b92a-e28b66f51c77 | -12.87116 | -55.06055 | 2025-05-16 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e6f0571-8674-3a82-9d08-e0752be79ab2 | -11.42467 | -54.32411 | 2025-05-16 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8e737b4-e431-37c2-beb1-629b41482fc4 | -13.30322 | -47.20513 | 2025-05-16 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e665c00-541d-3392-923b-c19558612edd | -13.67702 | -47.96694 | 2025-05-16 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd297bf8-3a81-33f3-b600-547d65147ffd | -14.01498 | -55.1267 | 2025-05-16 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16f40227-56e0-38f5-8b3f-8dce8acfe483 | -11.89711 | -56.40702 | 2025-05-16 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 747dd3e4-e76e-3d37-8688-f1c8f99dd854 | -12.16093 | -48.80313 | 2025-05-16 04:57:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07db505d-ae3d-3f57-b0bc-b0906f1b64ba | -17.05993 | -45.9214 | 2025-05-16 04:57:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27c57262-35a3-3d16-b547-8fb6018d4116 | -12.26245 | -49.31315 | 2025-05-16 04:57:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 269cf4a1-5efb-3202-ab60-536545fdcc35 | -16.93962 | -53.45015 | 2025-05-16 04:57:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ae1c003-6608-3d6d-90c7-98490b1f9869 | -11.91746 | -54.40516 | 2025-05-16 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8df705a-9f15-3423-95f8-a2ba008760e4 | -11.0283 | -48.80336 | 2025-05-16 04:57:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2770d38c-2af2-3f96-8b93-6ff46b7b70ef | -13.05098 | -53.71646 | 2025-05-16 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5509aa40-7f8d-3eaa-81d3-ba6e855264c2 | -12.98814 | -54.27514 | 2025-05-16 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c3689ac-c0f8-3ff6-ab04-68e1da0e7de1 | -13.95962 | -56.79012 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 166f7512-b44b-32ea-b5ee-c5f56f9e9ab0 | -11.57691 | -47.60588 | 2025-05-16 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4d9cbb58-2f8c-3b3f-8285-799e6cbb6bb5 | -13.97816 | -56.79662 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93c93f49-e98b-3f7c-8b17-f694c6d4b395 | -14.47255 | -56.32209 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3812c333-9e11-3ebf-9627-73c7818a1e50 | -14.01386 | -55.13388 | 2025-05-16 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 169809ad-b398-382b-b84c-754dde4d6b46 | -13.59772 | -47.37438 | 2025-05-16 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10843e7c-a000-3565-a9e6-253db429b5cb | -11.78147 | -47.35551 | 2025-05-16 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9bd46f3-b835-3fe1-a1a3-e0e973d627e9 | -11.5852 | -47.61753 | 2025-05-16 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 185b6c47-a085-3d07-a743-2a4275f145f6 | -14.01442 | -55.13029 | 2025-05-16 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dba423cf-d07c-35f3-ad61-307692f32ab4 | -14.01608 | -55.1416 | 2025-05-16 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| edf84c01-d85d-3020-aafb-ed07ac4db5de | -14.17635 | -45.48608 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f800d289-9fa2-3a23-8b78-2e03550091d9 | -14.01941 | -55.14214 | 2025-05-16 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a957a3d2-6207-372c-84a2-621470420cdc | -11.42412 | -54.32768 | 2025-05-16 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16851983-7f8b-314f-9987-68e969d29d14 | -13.9809 | -56.8008 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14a45885-5fcb-3aff-9209-e46c2341dbe7 | -11.42078 | -54.32715 | 2025-05-16 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c300bc8a-ec06-364f-9712-516d5acf7dad | -11.63066 | -54.94136 | 2025-05-16 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffa0e835-c30f-3145-99fe-48447ab2eb80 | -11.96496 | -63.51722 | 2025-05-16 04:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 58d4f410-af03-3389-ab65-7d5478ea4516 | -14.02205 | -55.14233 | 2025-05-16 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 972b0855-32c3-3861-bbbf-5e54030a75d7 | -11.89319 | -56.41004 | 2025-05-16 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f11f7f16-7138-30a7-8613-eabf83edd359 | -13.05042 | -53.72027 | 2025-05-16 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b66c1a03-1d85-3e78-b53f-a74f7f036b9d | -11.42023 | -54.33072 | 2025-05-16 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9601f5c7-0c14-3bc6-975a-5dd9054d7161 | -11.78715 | -47.3505 | 2025-05-16 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3f9797e-8034-3eaa-8233-b7ab6444bd06 | -11.90045 | -56.40758 | 2025-05-16 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 013b121c-a7a7-353b-93a0-057a6bcb4954 | -10.39161 | -57.5405 | 2025-05-16 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba06c8dc-e437-3027-8b16-abaabf0c9e0b | -13.80105 | -53.30194 | 2025-05-16 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 135324d6-a255-3080-857f-278c2b516332 | -10.14556 | -53.63548 | 2025-05-16 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81b0bd6b-dccf-3728-aaf8-d28ccee49e19 | -13.57181 | -52.8712 | 2025-05-16 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28008aa7-be8f-33a9-94eb-af0e63011e20 | -12.34546 | -49.95974 | 2025-05-16 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4add47f5-c96b-3450-a1af-874a8d360614 | -10.96317 | -49.42192 | 2025-05-16 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9298f3e-5a48-303d-9f56-0d7bf5234eb1 | -11.16688 | -48.67713 | 2025-05-16 04:57:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 384d5232-cbcd-3d21-9b0a-963f32c2014f | -10.39313 | -57.55285 | 2025-05-16 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84647273-6649-317e-ae8b-85f165b756dd | -11.61575 | -48.01674 | 2025-05-16 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4051cdd6-ce06-3ed3-bb9d-a537576eedde | -14.01609 | -55.11951 | 2025-05-16 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a73d51b2-e07c-3858-ad28-6ec2c02c5154 | -11.7864 | -47.35609 | 2025-05-16 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25606e0c-5538-37be-8c92-f80f417653ee | -11.63053 | -48.47473 | 2025-05-16 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef758685-47d6-38a4-b831-3472b747abeb | -12.2636 | -49.31493 | 2025-05-16 04:57:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5128c3c0-9974-3ee1-9a87-bd298f0a5878 | -12.34028 | -50.32752 | 2025-05-16 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 56a749cc-c5a1-3019-b526-c1ad2caccf8a | -14.17245 | -45.46898 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffe7dad8-361e-3142-84dd-aaeb2a921da6 | -12.61078 | -56.02476 | 2025-05-16 04:57:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cbef4f7-daea-343a-ac3e-fc71e63cb408 | -11.7651 | -54.68758 | 2025-05-16 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13d1cc86-0f5e-36f3-b065-aceaf787c93d | -10.69577 | -59.11354 | 2025-05-16 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0f79da1-2332-309d-b429-f288c3f189e5 | -17.05375 | -45.92149 | 2025-05-16 04:57:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbd38e80-154f-310b-aa47-d9ee12dd8b39 | -10.51679 | -59.38446 | 2025-05-16 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b1ccc99-f358-388c-a24a-460ccb1fb630 | -14.8705 | -51.97832 | 2025-05-16 04:57:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 139bfec0-5c40-3ed9-ae1e-6fe0b7147131 | -12.87172 | -55.057 | 2025-05-16 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c2fa3e5-8331-32bc-8fa1-aff185c035d5 | -12.33979 | -50.33116 | 2025-05-16 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 828d155d-5761-3805-8d40-3a3169894927 | -13.6183 | -54.88341 | 2025-05-16 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9bec688-2dd7-369e-862e-a82568b1acad | -11.78883 | -47.35267 | 2025-05-16 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2e78526-5dcc-37ef-a8cb-d17da82f74cc | -17.06001 | -45.91794 | 2025-05-16 04:57:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c034e0b1-0ac3-3b38-b7e3-19b0012b9905 | -14.17198 | -45.47309 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e396485d-1340-3e91-9799-b2bd2d67b968 | -10.34797 | -51.69522 | 2025-05-16 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc07374c-8dae-3187-acab-71d69d27c0fb | -11.5845 | -47.62286 | 2025-05-16 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9cb150f9-c929-3846-8c33-9e792766ec62 | -13.59271 | -47.37339 | 2025-05-16 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64be9bab-aa7b-3e32-a397-91ca5057ebf3 | -11.51418 | -48.57821 | 2025-05-16 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 741a5c02-0354-3236-9ceb-d289e2973479 | -11.76788 | -54.69167 | 2025-05-16 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README12.md)
