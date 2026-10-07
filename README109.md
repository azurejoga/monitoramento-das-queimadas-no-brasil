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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f989a32-4a31-3391-8a7d-c4509069d38e | -2.78433 | -51.67204 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 711fc5b4-066d-37ea-8537-6307fcf56572 | -3.04475 | -53.94278 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c6877c3-18e6-3073-8627-44f6c9ce853a | -3.08587 | -54.28335 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1d6f6efc-a404-3a9b-a70e-fa6b2cae5656 | -3.92848 | -56.05948 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f0b6784-5a4c-3d55-a627-e632c9e9ee9c | -2.78354 | -51.67496 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a54bc0a2-b592-3e9b-b929-9835abbf3815 | -2.16446 | -59.2291 | 2026-10-07 05:40:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2f87690-a8d4-3d60-b8b5-61fe93930648 | -3.29195 | -54.05322 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| eeac91be-8ed6-398d-a445-6c32a54622c7 | -2.94232 | -54.17438 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3e909a0-50d5-3df3-ae4e-35da7977f050 | -2.93502 | -54.147 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d52c455f-016a-352c-8192-acb02aab3245 | -3.73609 | -59.44756 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31b0f108-a785-3be7-a6e9-066a0ad56676 | -3.74309 | -59.44049 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7c7e65b-00d1-37e1-8555-ba95bb15c215 | -3.79345 | -59.32114 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cac43acc-0440-3d28-a33b-247eccaf3f45 | -1.79389 | -57.1128 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0c9c5e5-00ac-340c-bb60-3fd2998f0de9 | -3.7345 | -55.98052 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2121880-6d30-307f-825d-09f0a007ecc9 | -3.98177 | -56.21814 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21627ed1-28ec-355b-8ed5-001349534947 | -3.35708 | -50.76207 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a79c73f-7ffa-3700-bd17-ce347323edb6 | -3.49519 | -50.10249 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51c81d2e-049b-3eef-8cc6-97382c1add3b | -3.26834 | -50.40899 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a712744c-5d52-3af2-b501-2f8bc419e2f1 | -3.37943 | -58.23874 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0c6dff4-ff58-397b-b06a-6153a4c52dfd | 0.31869 | -60.43968 | 2026-10-07 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7df0f82b-6fbc-3842-a764-c05de3306089 | -3.27155 | -54.06032 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44dbf9c3-4a26-3a12-b8f6-c083a5e8b80f | -3.50339 | -54.63727 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33c16c02-33b5-3cee-8420-08db23562fa2 | -2.90151 | -54.02158 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2219a9b-88eb-353b-99f8-3212240beccb | -3.68675 | -55.95391 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f54bc712-3758-39bf-92c7-7e4b9c9049f2 | 1.70936 | -55.62567 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7cca7c9-ee0a-35b3-9c39-fdc73a531ef1 | -3.03912 | -53.91601 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 41b82ad3-e90f-377c-ba67-fe7bd7e062a8 | -4.11897 | -50.82578 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3ec1efb-bf3c-3334-95e3-92f9f18036e4 | -3.66445 | -57.09193 | 2026-10-07 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ac208e2-22b6-3f0e-88e3-7c65fb41895c | -3.27283 | -54.01275 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f0f9b43-d4ad-3e89-b554-364bd9a3f6b6 | -3.10119 | -54.15147 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf38ed73-a324-344f-85d3-94d442a47b11 | -3.35754 | -59.50073 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32ec4a27-08b5-3343-b5e3-32f015982af0 | 1.70394 | -55.64178 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb64a6f5-e152-3825-bf8e-4b18dabeacd9 | -3.2831 | -54.00914 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0de556c9-631e-3590-bad4-267bc91f0547 | -3.53861 | -50.09536 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a59cdef-b636-369a-89ef-ccf7d3230c68 | -0.42268 | -52.06452 | 2026-10-07 05:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd19222d-c016-3e02-a563-abb199f73a84 | -3.53472 | -59.4127 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 296c8adf-d59b-3536-9aea-1b43cebcdc4f | -3.28394 | -54.03489 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 912ca2c6-99aa-3204-a32a-b0f0407a765f | -3.54044 | -58.64787 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b76f4d6-1851-3df9-ad71-e3e0854b8f2a | -3.09442 | -54.28957 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ea743ec7-ed4e-3969-889a-0b179f15be09 | -3.77959 | -59.19512 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b33dbc37-e332-39df-b7d8-39730b894f99 | -3.03757 | -53.92616 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5198c9a-4bc1-3555-8f27-0254977c61de | -2.92959 | -54.15114 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d1f831b-7652-3158-bfb5-c4d3ac1e4fdf | -4.26684 | -54.8696 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd2925e7-ea11-370d-ae6f-82da5cf9e141 | -3.18048 | -50.54478 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6251f067-13f8-36ce-a6de-e634f7d5eb9c | -3.05821 | -54.15052 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5355574-f285-3dbf-aaf2-f08ce1fb9c9a | -3.48743 | -59.5845 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ea957ff-6742-3bf9-acc4-858bf1feb82b | -2.94409 | -54.19451 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cf144c6-d11e-3e35-98c7-911b8afeac9b | -3.33069 | -59.46997 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5557fd58-5fc5-31dc-856e-b15d4c07dea4 | -3.1792 | -50.55351 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ee3e6a60-9f97-3282-8f96-0d27307f3e3e | -3.29025 | -54.02554 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ec1e3aa0-5c01-331c-83ee-94a0182bc0c8 | -3.27103 | -50.432 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17f100d1-1c36-3a59-b834-fb01bf184f9b | -3.83862 | -50.31026 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62311ce0-9449-327d-8c05-23741fda1a57 | -3.27765 | -54.04421 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 676c859f-e506-3aa2-af99-a085e80f5a9e | -2.93426 | -54.15186 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| df5ace26-5508-30df-8100-aa0d6c9cf9d0 | -3.73848 | -59.44743 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5789de3-3841-325b-b05e-9ad9879d8dc0 | -3.99262 | -56.25716 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2a9f48e-97d5-391c-953a-0a8a16192a55 | -3.96448 | -56.05235 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ad816a6-7ff2-355a-964a-1e3756075b35 | -2.87284 | -54.14722 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c869f39-1bc0-3bbb-abde-57b2c8f741f8 | -3.13032 | -53.76496 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97d5c2a8-824c-3ae9-84ec-50e165d210f5 | -2.9359 | -54.17195 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d05417db-5048-3129-b5a4-873edfe7f35a | -3.50821 | -54.66622 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15eb46d8-ed21-33bc-a0b8-6e966b66f58f | -3.10046 | -53.73373 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b482cc7-b165-3857-865c-4b3a7fedc471 | -2.83993 | -54.06578 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e987e5ba-11e7-3bd1-8467-37b3981b26d5 | -3.38105 | -58.20491 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2063586d-a90e-38e0-a511-dee74138efde | 0.70188 | -51.43433 | 2026-10-07 05:40:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8b943b7-6b6d-3a8e-9d84-8672b39521d0 | -3.77748 | -58.52637 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3afebdb8-7412-3cde-b6bf-b750a1e88904 | -2.80332 | -54.08524 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 708cea31-904f-3554-98da-9c9384ce11e2 | -3.34328 | -59.47953 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86203e6e-af37-348c-8a58-0522152fc843 | -3.2816 | -54.04994 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c51022ad-6634-3bbc-9f48-4d3c0d54d84a | 3.15143 | -60.5906 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 859b1b3b-ef83-3563-b2b8-d12a3d58c82f | -2.15473 | -59.22379 | 2026-10-07 05:40:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7cf5a950-8569-3918-8c7a-85e2272763b6 | -2.7849 | -51.66842 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91513369-7d82-3591-a892-af2b8d6a3e4c | -3.50293 | -54.63922 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56079180-5a03-315d-a53a-c949c9250c71 | 2.75595 | -60.02088 | 2026-10-07 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9fc7b7a-1650-3967-af84-4d3fab897126 | -4.10587 | -52.06603 | 2026-10-07 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6767d2ce-8c1d-3926-975f-0040db5fd9c6 | -4.18702 | -51.13206 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 619b23af-0f5b-3e2f-8f33-e167c6e4eb72 | -2.76219 | -54.10376 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad1c5caf-798a-3158-8ee2-12466d2fdf8c | -3.10549 | -53.76641 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5607ddf0-c0f6-3ca2-8b1d-dddc6789cb38 | -3.84415 | -50.31491 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6fd28fb-2e9d-3d74-9398-e00ed544ff53 | -3.47687 | -59.47294 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d86fb608-b6b5-357b-bc06-2877e22999de | -1.99995 | -56.95114 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56c85208-13bf-3953-89b9-c5f21631bdcc | -2.987 | -54.13158 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2576f025-3633-33dc-a921-235435ada132 | 3.15308 | -60.60105 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 801b6b13-6aa8-35b4-856a-f0dd2b292f50 | -3.19116 | -50.55534 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91f13d2a-5bf6-33b6-88df-41790ca2c1d4 | -2.14179 | -54.44253 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18ab1045-72d3-3b72-873b-16c1f963ec8b | -1.10229 | -54.15463 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37996019-d98e-30a2-9101-713946d7c567 | -3.07794 | -54.17854 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 786b9ee4-3eb9-3d57-b2c5-3feafc29d47d | -2.85406 | -59.26158 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5ec6759-527d-3534-b897-ee2579ea44e3 | -3.73835 | -51.21099 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67bbe297-e21e-307e-8435-4808e1db85b2 | -4.14752 | -54.03058 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e03ada49-af7a-32c2-a873-a792e1ffa6de | -3.50368 | -54.66543 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f51c72da-d4c6-3895-858c-2fe53289df28 | -3.11368 | -54.16377 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b9fd409-33f2-3897-9f92-137151ce9f49 | -3.05417 | -54.20963 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa4c5b3a-5418-3f69-a097-ae1fe735154d | -3.23104 | -54.37417 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5d1c7c3-5986-30c9-90c6-ad22299f28ef | -3.80532 | -51.03946 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b49ebca-dad5-340c-8361-957630f540fb | -3.49451 | -50.1071 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a446ca87-0e04-39b9-ae10-2caa58208941 | 1.32377 | -60.71372 | 2026-10-07 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4765fa6-ba6a-3c55-bebe-e85181ded3df | -3.53981 | -59.49363 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ffa3d2e-b305-31e7-92d4-821704a09477 | -3.38831 | -58.20601 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1becb18e-3243-3eb5-a3c6-8dcb919c1984 | -3.62309 | -55.28109 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |


[Clique aqui para ver as próximas entradas](README110.md)
