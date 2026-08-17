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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e21f6595-28fd-3859-a847-2d720e0e9c99 | -13.43719 | -43.83918 | 2026-08-17 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dffc9728-caf2-3ce9-9977-ba8fb150a385 | -11.23755 | -54.01812 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc40b18b-881d-3578-b678-5710d5c14952 | -11.13219 | -46.50264 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34ebf032-fdd6-3886-98eb-8fea7bb36f35 | -14.97813 | -46.58838 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f6f1a33-37f9-3aa2-9a4e-955e1ec2e8fe | -15.07884 | -47.01046 | 2026-08-17 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f5d338e-e4e9-3344-86df-9a475a1f698b | -12.2354 | -47.02979 | 2026-08-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3eeb2b28-1866-3d7f-a1e3-3771fa248d08 | -14.31872 | -53.04951 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d24a94b6-f66f-3796-82e6-3c544d376762 | -13.51664 | -46.28092 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4345b0b-0942-3fa2-9579-12c909d9c9ef | -6.83908 | -56.44148 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 16278f0a-3f47-36c5-9d5a-0178c24e9ce4 | -12.25075 | -43.15245 | 2026-08-17 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ea2874a1-ff69-31dd-a37b-689d7c3ff124 | -8.02794 | -55.14827 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3989d591-577d-3996-90c9-6041233483b2 | -11.71294 | -54.60517 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b61bc6d5-e267-3dd3-9a0a-8ef0b91de65f | -11.3142 | -45.86278 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 61207c1a-476e-3616-ae08-2949b7377b62 | -11.73037 | -54.56816 | 2026-08-17 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65b0a8af-34b7-3e55-8467-7c537216e665 | -11.28104 | -45.8144 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abc7cdea-a5ae-322c-9d58-f743f53c8fa8 | -14.48028 | -45.67248 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2868b957-c48f-3b79-a2f4-34aa16d04599 | -11.27995 | -45.82141 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a9e248c-3e7b-3090-9d96-a4fc15e3d9f1 | -14.92739 | -46.60921 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df4d54dd-1a42-3043-bd78-3bb4e0ed01d2 | -10.11623 | -48.8121 | 2026-08-17 04:21:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 971feb7c-9c71-31a7-a74c-ed1397cae9cb | -11.10026 | -47.29435 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb0e31d3-d5eb-3d3c-98c1-20845025f1ce | -11.7095 | -54.62341 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b94ea1d2-c644-3527-91c5-7695d0100857 | -14.29814 | -47.17337 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 897adc53-521c-3c19-a940-f63ed58d221a | -12.17929 | -45.14742 | 2026-08-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1b4e505-8be5-3236-a035-0ceb5724dc3e | -14.29757 | -47.17694 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b11e3dd-fd1b-351b-8564-177d8afed05a | -7.77876 | -48.27385 | 2026-08-17 04:21:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e555c74-874d-30be-94a7-4b1a00383ebd | -12.7331 | -48.46288 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| adcedb3c-4c75-37cb-8d3a-f1b47f034f1d | -12.65682 | -48.49448 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 914878c9-5e65-343a-9af9-e5cf61159529 | -11.2866 | -45.84401 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6152401d-4a25-36e1-baa6-980e7dcd3152 | -15.07222 | -47.00935 | 2026-08-17 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66d3d9c5-790d-3fa9-9ff9-0968a029e2a0 | -12.24149 | -47.03447 | 2026-08-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8575cd62-d0cc-30c3-a845-79342073d395 | -9.98183 | -53.94133 | 2026-08-17 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c8026e6-5b81-337e-835d-ddd4f39af602 | -6.83998 | -56.43658 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0f03cc0-1af2-3a9e-b294-2a9026cbf476 | -12.74973 | -48.42614 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0a8379cb-f634-3d3b-bea2-84f2f16d803e | -12.71325 | -48.47572 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfe19a89-532e-3208-be47-5e20ac90db17 | -14.28929 | -53.06227 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b694bcd8-f143-3959-bce9-161978adbe4c | -12.55295 | -47.8664 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3688f5e-0065-3b1f-9084-0d0cc0ab69b3 | -12.00498 | -46.46825 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d35db6e2-dc54-365b-8bae-4f7c2becfcec | -12.66181 | -48.50727 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e10bc774-d82d-306f-a66d-fdb151a51bbb | -6.82402 | -56.45384 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da22c579-1452-347d-a406-65b63c53da74 | -11.23857 | -54.01247 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c856379-1276-3eb8-98b7-d56af86c7763 | -14.45666 | -51.84012 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5de7c5fd-7ccd-311e-b324-558015a8abd4 | -8.06402 | -48.52947 | 2026-08-17 04:21:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3929325-4f8c-3c83-958a-fcb39032f4e8 | -7.38006 | -55.50948 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e41d41f8-9011-34e0-8cbe-60ddfbb9199d | -13.50338 | -46.23532 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| abf076f3-648a-340e-bf1c-a793a0319747 | -11.46646 | -46.58254 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 1026de45-3d07-378a-87ca-7a9838838602 | -12.45963 | -46.64734 | 2026-08-17 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55e2263c-4f05-34a5-96d7-7e16519f22d3 | -12.20754 | -52.87205 | 2026-08-17 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73e9bb00-5137-39c7-9063-ebfd7bf44b20 | -14.30413 | -47.19999 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5e8ba36-1a37-3808-9a70-c4044fce1371 | -8.73586 | -45.30343 | 2026-08-17 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d07d26d2-3a8a-3215-9d20-885cc747d063 | -8.10096 | -51.66409 | 2026-08-17 04:21:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e373fc4c-6a6c-31e1-b11f-7f6e5d52831b | -15.12862 | -50.05628 | 2026-08-17 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 469a25f8-9d0e-3851-8e28-2d2f988e4e38 | -12.32761 | -47.26214 | 2026-08-17 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b727ee50-453a-3c44-ad84-35d80093df4c | -13.51606 | -46.24102 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30684419-bd22-38b4-9f88-8f3282d90174 | -11.50738 | -46.60361 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30a579b2-385a-31d2-9e8c-3f846b860928 | -11.47755 | -46.57702 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| afc11f48-866f-386a-9f69-efa3812fceb2 | -8.64124 | -54.7216 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e794506-114b-34c5-8ded-e57210b40ca3 | -15.20861 | -52.70817 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d685bfa1-b8a6-3d21-a782-661768576016 | -15.91576 | -55.53919 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3112406-ecd8-3156-a5f5-86e218b4c044 | -16.81482 | -49.0707 | 2026-08-17 04:23:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb84c505-ac72-391c-a39f-8eac6bfd9311 | -18.4454 | -49.72788 | 2026-08-17 04:23:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9b9e885-72e1-3d7c-87f7-f0a851147f44 | -18.44407 | -49.73578 | 2026-08-17 04:23:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 899ec3fb-848e-3c91-b194-5342c0e5e0eb | -15.85957 | -56.3449 | 2026-08-17 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2d209d7-decd-3056-8f54-e1cc8df8838e | -17.32698 | -54.92841 | 2026-08-17 04:23:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| adeb91b5-aa04-3cc4-a8c3-ca4486f3f3d7 | -15.2672 | -52.90961 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0e1db6e-2fea-3938-b317-11106ff9b3a6 | -15.22907 | -53.86188 | 2026-08-17 04:23:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3f8f338d-ebb0-3c4b-8aa6-43b11f9e6719 | -16.21232 | -57.638 | 2026-08-17 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 18e2e486-7ce4-3913-a358-393b3b16610c | -14.08818 | -58.45813 | 2026-08-17 04:23:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 48f0d072-9604-30f7-ac8e-426779d59302 | -15.94587 | -47.84824 | 2026-08-17 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ce9bb94-5424-346e-8e90-2c951dca730c | -15.90875 | -55.52214 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bc132dd-88ae-3e59-8a66-b59e7a8b5836 | -20.40181 | -46.51329 | 2026-08-17 04:23:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 362ce7a1-762c-3878-a4bc-529344aa0390 | -16.08704 | -49.787 | 2026-08-17 04:23:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e274ec10-4400-30ca-b3f8-5f2b2ba1839b | -16.67141 | -49.44543 | 2026-08-17 04:23:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a260524d-a225-39d9-b248-98f1cbf91121 | -16.60579 | -52.59468 | 2026-08-17 04:23:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb705982-8808-3978-a0b5-a6ad29da6fe4 | -20.27485 | -47.20441 | 2026-08-17 04:23:00 | NOAA-21 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 831952b8-b2e9-38a2-8f5b-da13f7a37fe4 | -14.09134 | -58.44309 | 2026-08-17 04:23:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 73b95c96-cdd4-3637-824e-278ed87fe911 | -15.91793 | -56.48614 | 2026-08-17 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eccbf102-e7c0-37e4-8ca3-36f8592da552 | -15.03469 | -52.68118 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6ee0a2a-88ee-39ce-be1b-cb0c190d4e56 | -20.61917 | -45.08968 | 2026-08-17 04:23:00 | NOAA-21 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 84b070ce-0c59-304b-a768-404ab461d579 | -18.42279 | -49.6763 | 2026-08-17 04:23:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0622ed28-2bb0-381a-bb25-b08a187e1903 | -16.29579 | -53.17546 | 2026-08-17 04:23:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4480936-e821-364a-90e5-593300c5a443 | -15.94645 | -47.84463 | 2026-08-17 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c8243a4-4281-3f82-b1af-80d4f217728a | -14.09857 | -58.43932 | 2026-08-17 04:23:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bd266069-8b4b-3d73-a4d6-4610c824d505 | -20.40518 | -46.51386 | 2026-08-17 04:23:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b593a28-f10c-3935-a13a-b8f49f088ae5 | -16.20505 | -52.62734 | 2026-08-17 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a45ec40-c49a-3074-b8af-e0985bfe4a7e | -20.61061 | -45.91845 | 2026-08-17 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecc9ab80-5a9d-3336-afe6-f555a1aeafee | -16.29504 | -53.1744 | 2026-08-17 04:23:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a8493de-8dcc-3b7f-95de-5e1f29ce3c79 | -19.81685 | -46.93501 | 2026-08-17 04:23:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c40145d-a631-317f-9939-2edb8ae9beec | -17.88468 | -49.94519 | 2026-08-17 04:23:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4e7fd73-22ce-3f55-8116-faf0026d91f9 | -15.91633 | -55.53632 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96720a67-cd68-369f-aa7c-a1966665de99 | -15.92068 | -55.54055 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edc51c95-7302-3fb8-9f19-718ab8268a97 | -20.12803 | -44.86178 | 2026-08-17 04:23:00 | NOAA-21 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1711e9e2-7c5e-3244-8c44-b2abc518709e | -15.91031 | -55.54059 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 8fc996fc-f8d4-3639-b134-6da8725597da | -15.91861 | -56.48277 | 2026-08-17 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d188b98b-af57-304f-8ed6-1db940197fcb | -19.1884 | -46.14477 | 2026-08-17 04:23:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82685a6f-1231-3c27-ae15-c755ee69f098 | -20.57138 | -47.15479 | 2026-08-17 04:23:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5c369c4-f844-3ee4-9556-fe9111af0662 | -15.90387 | -55.52061 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 016d238a-8f2a-3a3f-b69e-890bf926cf3e | -15.90332 | -55.52343 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 4ca07d6a-e2df-3cdc-bd2a-2b1535641fef | -18.4475 | -49.73643 | 2026-08-17 04:23:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9e68bbd9-fc7f-32d5-b13b-2cc01ca03c30 | -15.20291 | -52.71552 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ddba831-2759-34cb-a4a5-7a8841c698c5 | -15.8198 | -48.16791 | 2026-08-17 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README23.md)
