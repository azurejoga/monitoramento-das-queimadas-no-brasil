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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ff95106-3481-358a-901a-2752e06d4df6 | -7.1523 | -44.2385 | 2026-09-15 14:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 408.4 |
| 52d43720-cf72-3ec6-8258-12bf08ba6c2c | -18.1714 | -51.7466 | 2026-09-15 14:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 3ae3c28b-f43a-3d35-87dc-a098ca37e84c | -5.1256 | -55.9352 | 2026-09-15 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 160.2 |
| aefbacce-290d-35b3-ba7d-d5949ac07fe8 | -6.6953 | -58.6903 | 2026-09-15 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 6e5211b6-e361-3c03-a616-7c8def4ca902 | -14.5889 | -40.6816 | 2026-09-15 14:30:00 | GOES-19 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 119.6 |
| 21b4b2c0-765d-3bd8-96c7-4ec7bd4cd63f | -9.1337 | -65.844 | 2026-09-15 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| d3aa8e8d-faed-31cc-86ba-90ded7ca21f2 | -11.8154 | -46.5899 | 2026-09-15 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 227.7 |
| c3aadd43-8bff-3f37-bf32-03198b74b4bf | -11.7962 | -46.5926 | 2026-09-15 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 151f85a8-b1b8-39c0-ab4d-80a63bf3e37b | -11.2304 | -54.0985 | 2026-09-15 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 4994ddba-3435-3750-ab3f-cd5277c55e35 | -11.3642 | -43.9407 | 2026-09-15 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| f8d3c0d0-0890-3620-9694-79d4c4dd3837 | -10.7084 | -50.6212 | 2026-09-15 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a8d2f9f2-ea40-3dcc-8dfe-e8a6b531f2ea | -9.7687 | -46.1067 | 2026-09-15 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 243309b5-8f5c-3c8f-9c97-33b875da202b | -9.3575 | -50.1156 | 2026-09-15 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| d8aa1292-a8af-3f26-8118-8c0b364b99d6 | -12.3081 | -47.9761 | 2026-09-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 082856d9-dd80-3c3b-9df3-dc5587adf96d | -9.1711 | -49.9835 | 2026-09-15 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 97b89191-2abf-32a9-bdbf-4f74faa9206f | -13.9941 | -53.8731 | 2026-09-15 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 812a56f1-a771-31c8-a44a-7f7cfce44193 | -13.414 | -57.0225 | 2026-09-15 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 43fe703f-b018-3152-bc93-8d465b3d3d49 | -10.6335 | -50.5651 | 2026-09-15 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 10e57bde-66a7-3115-835f-1114e3f48600 | -11.9715 | -52.4715 | 2026-09-15 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| aedcae44-19a0-389d-8556-ceff17c5e856 | -4.6776 | -42.0713 | 2026-09-15 14:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 121.7 |
| 97622361-368e-35fb-857f-7fbbc19fceb4 | -12.3273 | -47.9735 | 2026-09-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 156.7 |
| d78d1a45-b582-32ad-a0ed-cb719f73cb51 | -11.5045 | -45.771 | 2026-09-15 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 360a0218-95c4-387e-82ce-f39bd74a13db | -13.3949 | -57.0242 | 2026-09-15 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d869bbb8-2fff-3398-8b82-94e759b7f5d4 | -10.792 | -46.2071 | 2026-09-15 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 290.4 |
| 573b3ed1-48c1-394b-872c-fb964c9f159e | -7.082 | -42.1346 | 2026-09-15 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 117.7 |
| 17ec5d53-d8f5-3c82-84c6-cf5e3ead60ac | -13.287 | -51.2832 | 2026-09-15 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 3fd025d8-d04a-31a6-9efd-b45e534239b5 | -13.2235 | -51.6531 | 2026-09-15 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 601a7441-f6df-3219-a1e3-6cac47cecca4 | -8.5468 | -50.4423 | 2026-09-15 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| fa49bd38-2808-3060-90a4-aee388066b88 | -7.0823 | -42.1107 | 2026-09-15 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| 86ac3ddf-d981-3e6a-a22d-f6ef0f497567 | -11.2113 | -54.1208 | 2026-09-15 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 287.0 |
| ad252f0f-09f3-3679-89a4-3b33c28ff2fb | -13.5719 | -51.4605 | 2026-09-15 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 25dedca3-dc6a-344f-8823-1aeae73b4eea | -6.8217 | -43.5271 | 2026-09-15 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 4be5d75e-6181-3515-85f4-afc613bcd528 | -7.0166 | -44.6184 | 2026-09-15 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 254e4e01-c27a-387c-a3b2-192bac1c33a4 | -8.7889 | -45.8999 | 2026-09-15 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 00d103ed-1e02-3673-a185-0f022c30497b | -12.6824 | -54.6968 | 2026-09-15 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 391e8ba0-9bcb-3fbe-9953-cf1e5c7a0a0d | -10.8665 | -46.3105 | 2026-09-15 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 2abd7444-671e-36b6-af72-a99cb20b6ad5 | -11.2302 | -54.119 | 2026-09-15 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| fdd60096-c4ad-3726-99fb-ffa5bef91279 | -10.7726 | -46.2322 | 2026-09-15 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| ce0e6f00-992e-3ca3-8b9d-6d14ac5f0874 | -15.5195 | -53.8527 | 2026-09-15 14:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 020cd3ca-c04d-3a23-9209-626db69178fc | -9.7684 | -46.1293 | 2026-09-15 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 40d2aed1-7cd6-3329-9cbf-17f86f1c5229 | -8.4852 | -44.5885 | 2026-09-15 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 9bacfd62-b1de-396f-9862-d6eae346d9c1 | -6.8408 | -43.5021 | 2026-09-15 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 90faf137-e289-3653-b700-011d9c08d575 | -10.3116 | -45.3136 | 2026-09-15 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| c308880f-2c22-33ac-8237-1de964402d92 | -5.1255 | -55.955 | 2026-09-15 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 6d71a8c0-0dd0-3c3f-8418-ea82993980bd | -15.5199 | -53.8317 | 2026-09-15 14:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 180.6 |
| eb2e5d67-43f7-3aef-9dbf-20edd561c4ed | -13.3949 | -57.0242 | 2026-09-15 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 10a30069-e37b-32a9-a3f9-ca3e958a5529 | -15.2827 | -42.783 | 2026-09-15 14:40:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d011830b-6c9f-3fef-b894-795904ae1fd7 | -13.287 | -51.2832 | 2026-09-15 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 6f058676-2876-3409-8bcb-6b96028ac780 | -10.7274 | -50.6192 | 2026-09-15 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| bfe57109-33c9-3281-ab83-334c3bee6b69 | -12.3273 | -47.9735 | 2026-09-15 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 6b13e75a-0019-3c71-a1bc-fa46f63904b4 | -9.475 | -45.4612 | 2026-09-15 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 253113cf-e9f4-3c73-a326-ba83bfbca117 | -8.114 | -45.6301 | 2026-09-15 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 2e1c5fb9-a2e4-356d-9b62-aa75f32db8e3 | -10.6641 | -54.1491 | 2026-09-15 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| cba999fe-e53a-30a9-8646-f1f042976fb3 | -15.0208 | -41.4621 | 2026-09-15 14:40:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 582def16-e007-32ba-875f-0dd85480b9f4 | -13.7002 | -51.8274 | 2026-09-15 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| bc5a5f95-7f68-353b-8df3-e2c63db4914b | -8.8459 | -45.8713 | 2026-09-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 4fcb4343-e85d-36eb-8280-1ff23e0fae35 | -7.1525 | -44.2154 | 2026-09-15 14:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 7796bfe9-6d27-32f1-b9e3-451e758d06e2 | -11.5041 | -45.7939 | 2026-09-15 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| d6dd7628-c686-3242-b560-a18df7a2377a | -12.3081 | -47.9761 | 2026-09-15 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 67a455c8-5bc7-3477-a390-28995b7720ef | -11.383 | -43.9614 | 2026-09-15 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| d2c69144-47ad-3fde-8934-350f62e82aa0 | -10.3113 | -45.3366 | 2026-09-15 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 65efd4a7-5385-3e0d-a163-dd720fc657ae | -5.1256 | -55.9352 | 2026-09-15 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 202.3 |
| 63dc14aa-2b75-3aa9-ad3c-064e2b257aea | -9.1337 | -65.844 | 2026-09-15 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 6585957f-0679-3643-be6b-68bb681bb129 | -6.8408 | -43.5021 | 2026-09-15 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| be05cb4f-f387-3bf9-b477-394c46564fe7 | -6.5837 | -58.8498 | 2026-09-15 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| bf7c7402-9e0b-3695-8f06-7889bdd4276c | -11.3638 | -43.9642 | 2026-09-15 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 6fe1cc4a-31e8-3a15-9b60-16f1d057c2e4 | -2.7767 | -49.4765 | 2026-09-15 14:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 4fd9d0e7-c758-3e9b-8a21-16b454bb1141 | -10.6827 | -54.1679 | 2026-09-15 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 12699e76-73a1-3671-bbd3-daa016f78599 | -9.3575 | -50.1156 | 2026-09-15 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 0b040b4c-89d5-36ff-85fe-79080e3c9f4f | -13.5719 | -51.4605 | 2026-09-15 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| e62de535-18b8-3edc-bd93-e624062fd07d | -9.1337 | -65.8253 | 2026-09-15 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 85d4fc87-adc1-31d3-a6df-91442cdd4d3a | -10.433 | -48.6474 | 2026-09-15 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 83f724eb-fd33-3fef-801f-300fc0e77673 | -12.6824 | -54.6968 | 2026-09-15 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 69006730-58b8-3c24-a70f-f0e63fa10386 | -13.3199 | -51.62 | 2026-09-15 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| f86ba875-ba37-3550-803b-d086f6cb626f | -6.0256 | -59.9293 | 2026-09-15 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 73fa774f-d972-35ab-bed4-20cb5c9faf76 | -13.3062 | -51.2808 | 2026-09-15 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 73d2f4f0-e631-3847-9116-31a8ea40c342 | -10.0008 | -45.7851 | 2026-09-15 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 1ffd8028-39c6-3632-8077-b3b46e6b4975 | -8.7889 | -45.8999 | 2026-09-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 4b4c112b-8820-3f9d-a0ef-d4710ef9e2b6 | -11.8154 | -46.5899 | 2026-09-15 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 7d6fa5be-f45d-32af-acf5-bbcec1da601c | -10.3116 | -45.3136 | 2026-09-15 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 15df51f5-c557-3047-a09b-985c3065fd0f | -7.2869 | -42.3524 | 2026-09-15 14:40:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| ac6262e7-2f78-37d4-a808-c29b2ac7ac08 | -6.6953 | -58.6903 | 2026-09-15 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2ea96e0e-1ef8-30fb-aa2d-408977233108 | -6.0169 | -52.1614 | 2026-09-15 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 300394f0-e941-3cd2-b374-11d64edc0921 | -2.9815 | -54.1693 | 2026-09-15 14:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 394c1899-2ce0-31ba-869e-2ca2fad191c6 | -13.414 | -57.0225 | 2026-09-15 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 236.0 |
| c53f7b89-0e36-3a98-9be2-a88f04b0b470 | -10.6335 | -50.5651 | 2026-09-15 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 46e78546-a643-3b59-9b99-de6c2be6c4d4 | -13.7722 | -48.8087 | 2026-09-15 14:40:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 532d3f57-4b16-33b1-809f-5dc3930ff534 | -15.579 | -53.782 | 2026-09-15 14:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 6d28859a-0e7b-397b-954f-fc6cb072c8d1 | -6.6767 | -58.7105 | 2026-09-15 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 1f5eaa09-7514-3ae3-93ee-6b9f6da4cc70 | -4.6587 | -42.0964 | 2026-09-15 14:40:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| cc26bcbe-3d9e-3176-acc1-95951e5c750c | -10.792 | -46.2071 | 2026-09-15 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 557fd63b-e26f-3350-8556-770790c0aa3b | -9.4234 | -47.8588 | 2026-09-15 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 1673032e-0fea-3c74-af83-996418dca28f | -11.8556 | -50.0006 | 2026-09-15 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 427c7d93-7f01-3acd-8657-5cc05d874a90 | -6.8217 | -43.5271 | 2026-09-15 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 5625187d-71c0-35c9-b438-03879df27db1 | -8.827 | -45.8733 | 2026-09-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 321a7733-2d58-3467-9ca7-9288140fe706 | -13.3059 | -51.3022 | 2026-09-15 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| cb4d6293-94bf-3e32-9931-f5ce6f6d66af | -9.7358 | -47.0958 | 2026-09-15 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f0753b67-2b59-3649-8a2c-9e2986836cb0 | -7.5582 | -44.9116 | 2026-09-15 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| eae1be72-fb55-3aa2-b086-2d8fc061109b | -10.6829 | -54.1475 | 2026-09-15 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| bd223fc3-547c-37f8-b962-9cd6d1e750b8 | -9.1708 | -50.0049 | 2026-09-15 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |


[Clique aqui para ver as próximas entradas](README82.md)
