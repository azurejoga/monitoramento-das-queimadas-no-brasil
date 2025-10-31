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
| 7cdd5100-20ee-3928-afca-3663089c078a | -13.81267 | -47.068 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e29c4e95-f12a-3a35-8120-5615eeb3a7fe | -12.50151 | -43.95651 | 2025-10-31 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79ecb36b-b0db-387a-ad37-cabfef496636 | -13.60154 | -41.07718 | 2025-10-31 04:08:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2883e017-8dff-307a-96d3-6f6c6bda28df | -7.60916 | -46.47441 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52658545-15e1-3650-9bec-41e7a4ee0fbf | -13.80147 | -47.06595 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2962fc8a-fa19-3799-a717-7ebc988c7909 | -9.87611 | -44.87026 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f15f4f4-7d7d-3235-8cd7-2e024623702d | -13.42457 | -47.36005 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4213d557-1d86-3da8-86da-677e3aa8dd8a | -8.10253 | -46.74836 | 2025-10-31 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17232d40-5f46-3515-a2d8-73381f889f97 | -10.85312 | -44.90564 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a75745ee-ced3-3b40-b2ee-b68b9c907ed8 | -10.25208 | -44.54942 | 2025-10-31 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccde25ab-e8e9-3230-b66f-8f506673ab25 | -8.83888 | -40.97373 | 2025-10-31 04:08:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 27504daf-a32e-350b-b521-e8674eb137bb | -9.51467 | -47.26778 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9504cf65-2b0a-3861-8db9-3c2f3938be9f | -12.29202 | -43.78548 | 2025-10-31 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b5f6f78-36ee-359b-9b18-153e02346fc8 | -10.94465 | -44.63096 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ccf9eef9-50a1-3c08-9f73-472856075b50 | -10.24767 | -44.57614 | 2025-10-31 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3898ec79-1a4b-30ed-97a2-384f0a9f4f9a | -7.66978 | -43.5817 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e1c629f4-f348-3542-a27f-c24e76cba14a | -9.85406 | -45.3567 | 2025-10-31 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2d00f67-1714-3fe1-9f53-d30a942d4ee0 | -8.16793 | -45.50974 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73db0758-23ce-3afe-9d69-8293c16a4f39 | -10.25695 | -42.37566 | 2025-10-31 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f8063806-8cf9-35ae-b036-6031020eb022 | -7.55754 | -47.4146 | 2025-10-31 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07656b94-1656-3cd4-bfaa-c3d9ac57dc3f | -13.23025 | -54.35283 | 2025-10-31 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a5b8fadb-1b10-3cbe-b641-d6a9eed2d8c6 | -7.62692 | -43.62847 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6ad9ab8-8d3a-34d5-8bbe-62754163b873 | -7.30676 | -47.81208 | 2025-10-31 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e93d6539-608b-3eb5-9466-a5d54ee5221e | -10.64074 | -45.2432 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf3ec381-169e-3e63-b6db-b11a40a0f7d8 | -8.33082 | -45.38397 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cf97adf-4f4b-363a-8d64-5e798ccb5bcb | -11.69612 | -46.69906 | 2025-10-31 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49a58a5d-8064-365e-bd8e-a14a9058d5cd | -7.65374 | -43.59413 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| a19d7ac6-cfca-31f0-969b-2f3b33f51372 | -8.46304 | -45.76637 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f29d1e7c-8cae-314f-8718-41311cd6bdf9 | -9.51529 | -47.26417 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcc66478-6f38-34d1-8ff4-6c3285db7c8f | -13.5363 | -47.4247 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cc5684e5-54e0-3a28-a3ab-50b3fb4c1ee9 | -7.6229 | -43.63165 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac6de033-7596-30f6-9f39-43eb6ac9516a | -11.58319 | -44.96832 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 962917ea-7665-3e01-a11b-345363805ba8 | -10.24863 | -44.54882 | 2025-10-31 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 483c02d3-daf4-3bda-9888-813ed6832778 | -11.3633 | -42.25278 | 2025-10-31 04:08:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2eb43870-69e1-3b1b-bea4-433da6b1427a | -13.78879 | -44.3651 | 2025-10-31 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7af7935-6a74-3301-879b-8a776ae01bc6 | -13.67307 | -47.20313 | 2025-10-31 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 96772537-61e1-3460-a7a1-59f2c86465d2 | -10.54283 | -44.78716 | 2025-10-31 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e028da1f-1ff1-3cc5-bba4-a721312d1a91 | -10.24731 | -44.59981 | 2025-10-31 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 117ca86f-536a-340d-9765-f501972156dd | -10.74638 | -47.83461 | 2025-10-31 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3e4dacf-8a8c-3e6b-8ced-194571efd951 | -9.83334 | -44.15125 | 2025-10-31 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44fcc1d0-bc39-3e8d-9113-c6937473556d | -9.848 | -44.86556 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7bbe5fd-e318-3258-9dfe-1f1895614b76 | -8.33177 | -45.38226 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bdddd1a-f1f2-315f-a63c-af7662bd9e92 | -12.15156 | -45.23044 | 2025-10-31 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d2d5b3e-083d-3a02-a940-4536fa8192d8 | -9.72844 | -48.02235 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d047bfc3-c6e1-3d9f-afcb-c6ad79241190 | -10.95364 | -44.16927 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22050473-6f7f-3332-a02e-2106b72feb56 | -8.16193 | -45.47718 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afe09185-70f9-3079-b48e-465a56d0752b | -12.29505 | -43.19253 | 2025-10-31 04:08:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9498081f-9840-309e-ab2c-cc560426f19b | -10.88648 | -45.07365 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bfd675a5-dd27-3082-a4c1-e8da69e9050b | -8.0969 | -45.14685 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f1937598-2865-33b1-8a22-ef9d00464513 | -13.12983 | -43.15566 | 2025-10-31 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 49b36016-5cad-32bd-b9d6-9c44ad4b767e | -8.09762 | -45.14257 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ad069efb-4d5c-3a81-9bae-2e4d360045dd | -10.54082 | -45.03825 | 2025-10-31 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91998d9b-ea5d-3f6a-9310-cb0ccf61788a | -12.20278 | -42.91734 | 2025-10-31 04:08:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 292d0124-0f08-3529-8601-e323b5d7d142 | -11.13056 | -45.15728 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 508e3348-3ee3-31d8-867a-53f0219c2d1c | -10.53306 | -53.71735 | 2025-10-31 04:08:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5680e07-2554-3ffe-b9d9-840a41bbe24d | -9.93193 | -44.90413 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1239eb75-50cb-3861-84ac-1ccf785216bc | -12.58323 | -43.36631 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a465e4e7-87b9-3768-98c2-7795a3c9b19a | -12.28058 | -48.07114 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 519bf048-d88f-39bf-9e68-c7d94eef10ca | -11.50876 | -43.99721 | 2025-10-31 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba75a4ce-babe-39d9-82a8-ec4acb7504ae | -9.86055 | -44.85529 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| cac0120f-3315-37f0-8aea-afce96963253 | -13.26993 | -47.76279 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c6962b0-8251-333e-b90c-13df045c028d | -10.95304 | -44.17296 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0540909-83c7-3d2e-8358-3fa4e720cd07 | -8.10356 | -45.17429 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d78654e-c83a-3038-9438-e78b4148c08a | -8.17858 | -45.70044 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 886c9fc9-4f2c-365c-aacf-4b4d2263923d | -7.93424 | -42.23719 | 2025-10-31 04:08:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 53ebbb42-cfd9-373c-9718-e145095652c8 | -12.06636 | -47.34176 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee41a23f-549d-322e-9c43-21db3eb947c8 | -10.53218 | -53.71762 | 2025-10-31 04:08:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b24cef3c-3545-39bb-98a3-c03667ba9507 | -11.11542 | -54.63931 | 2025-10-31 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ced2669c-25b5-3c0c-8cec-07ff9df6e236 | -7.68061 | -47.76357 | 2025-10-31 04:08:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf0737dc-5f7a-3cd5-af70-2bfb7d5b4716 | -12.74255 | -43.45469 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad713add-60e5-31b9-8d71-266e2e7c4e0f | -8.79726 | -42.81318 | 2025-10-31 04:08:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a80c7faf-6cc7-3c08-a656-e424909c6aa7 | -11.46315 | -42.76017 | 2025-10-31 04:08:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d5facebd-8d95-399e-b403-aa6a11a7a1a1 | -13.21972 | -53.87729 | 2025-10-31 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dec8eed9-7291-3213-a461-23d1bbb3b4c7 | -10.89084 | -44.3157 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df618deb-bf37-3681-a304-44b5f7a8563d | -10.75885 | -44.17878 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7336c232-b90f-30f5-bc59-60bb0b279c25 | -12.13006 | -47.15912 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25184c5e-0112-342b-9110-143274c7279b | -13.53167 | -47.42849 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fcdb74b-b476-32fd-a618-e4b2b81f00d7 | -13.88319 | -47.33396 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deb0f41d-8f77-319f-9bc9-e426066cb464 | -7.63873 | -43.57676 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c1f7295-076a-3789-b5eb-9169b69bcd22 | -12.56616 | -43.96009 | 2025-10-31 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81b5885c-b11a-3584-94b7-03741b6b4528 | -7.43649 | -46.88665 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 610adbd0-f771-3c98-a7d4-563b477b89c5 | -11.36057 | -42.29184 | 2025-10-31 04:08:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 91c937f2-ed65-3106-9bee-8ce3dfbb6f2c | -9.50599 | -47.26996 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56710661-dd91-303f-9523-80f46fe54975 | -10.74517 | -47.83374 | 2025-10-31 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a40ce58-1060-3e20-8743-82bbcbf4e84c | -12.82789 | -43.49415 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd6c2c26-455c-3dd5-83e0-3cfb597b417b | -14.1236 | -44.1871 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9da7cb87-f173-3de9-895d-607e594963ae | -13.23713 | -54.34974 | 2025-10-31 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ac1cf58a-933b-3c9f-b579-499169b9e7c2 | -12.82457 | -43.49361 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 21c36ef8-8fda-32d2-8b6e-55700dc48e19 | -13.24912 | -54.3522 | 2025-10-31 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3375924d-6b8e-3308-b298-902836d623f8 | -15.40922 | -40.86383 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 398bb6d1-fa07-39c7-92ef-2951c9e85255 | -10.74584 | -47.82997 | 2025-10-31 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 835a527f-bbfe-37f1-b235-da849e7324e1 | -8.17622 | -45.69832 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7677f397-eb60-3273-9242-a994bc6573be | -13.66826 | -43.08133 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8a1f7559-f793-373d-860b-b862bd1ea454 | -8.10388 | -46.7511 | 2025-10-31 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 153a9f38-eb02-367f-8b80-e524e32fd311 | -8.05239 | -49.63369 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0e4df31-0302-3e03-8eab-cc05e50deae9 | -13.34577 | -54.28724 | 2025-10-31 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77888554-b1e4-37a4-bd83-b5a3c4ea03cc | -8.09256 | -45.15052 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38a7cb76-8a98-3a6f-94bc-26cc6aa38d3a | -8.17484 | -45.69976 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81dbad08-d625-3775-b4ca-36885a965a49 | -13.68693 | -44.73315 | 2025-10-31 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a1b4c53-a3b0-3aad-98a1-19c0ec2b611f | -10.59585 | -44.05756 | 2025-10-31 04:08:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README29.md)
