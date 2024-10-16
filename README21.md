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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa2a033a-7840-368c-8592-4e4f7d9aaa71 | -3.1099 | -54.2263 | 2024-10-16 02:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 174.5 |
| 679e5e20-5b40-359e-893b-964d23315ebd | -3.1282 | -54.2459 | 2024-10-16 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 6818641c-6378-31a6-acd3-4d8be07c49e4 | -3.1283 | -54.2259 | 2024-10-16 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 198.6 |
| e115ff63-12d7-35f1-a75b-fc8b45568100 | -3.2862 | -47.133 | 2024-10-16 02:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| b3dfaad9-5520-395f-a78a-3dd22ffef1d6 | -3.2863 | -47.1111 | 2024-10-16 02:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| be6a3eb7-4aa4-3f69-9013-bb22cece8df7 | -3.288 | -50.9321 | 2024-10-16 02:05:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| f53c9cb4-0a87-3e88-89c6-1710f0a9df1d | -3.958 | -46.4442 | 2024-10-16 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 36b9490a-ee4f-3d5f-951f-a2b345379469 | -3.9581 | -46.422 | 2024-10-16 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 136.3 |
| de62f71b-eb38-3a88-bb85-3b9189364139 | -6.2545 | -45.8817 | 2024-10-16 02:05:41 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| f66c4848-7eaf-33ca-8c23-7f66708d0311 | -9.1709 | -46.9792 | 2024-10-16 02:05:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 2d4d5cb8-de90-3a06-84bf-913496e40435 | -11.6915 | -65.2432 | 2024-10-16 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.5 |
| f802f204-d731-3cb2-b0c7-326959b31ccd | -11.6917 | -65.2243 | 2024-10-16 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9fce890b-ea91-38c9-b3ae-cd1efaea9d79 | -11.6918 | -65.2054 | 2024-10-16 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 54502b78-c2be-31c6-8775-ecdf25017ec7 | -11.7103 | -65.2424 | 2024-10-16 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 220bda1b-9f1e-35d1-a89a-33be22583e8e | -11.7104 | -65.2235 | 2024-10-16 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 846220de-8be5-3f0a-b2c5-3ade26278319 | -11.7106 | -65.2046 | 2024-10-16 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.3 |
| f25e3c94-eb3e-3780-9059-cb1160a8a518 | -11.9381 | -64.8729 | 2024-10-16 02:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8db06b4c-32f6-3fed-b0f0-2092a7659bd7 | -12.4733 | -47.2846 | 2024-10-16 02:06:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 2826843a-396a-39cd-bd65-bb9c5fdf83ff | -12.4925 | -47.2818 | 2024-10-16 02:06:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| b24e8822-e10a-3489-a17b-662dec01f0c4 | -12.3983 | -63.7093 | 2024-10-16 02:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 54f558b4-404f-3607-ada7-a3643b67416c | -12.3795 | -63.7103 | 2024-10-16 02:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9bfc8b1b-3ee4-3dbd-9205-4ae785ef776e | -12.8012 | -62.9398 | 2024-10-16 02:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 295a69a0-058a-3b12-b651-7d3553683a79 | -12.7824 | -62.9217 | 2024-10-16 02:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c9aac604-5377-3973-b849-5f2bb1e2fae8 | -12.7822 | -62.9409 | 2024-10-16 02:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 29a21d23-dede-3514-a665-08b619bd6809 | -12.7821 | -62.9601 | 2024-10-16 02:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 4e7f8a5c-2f81-3944-81c9-4afaaf850d30 | -12.7633 | -62.942 | 2024-10-16 02:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 82b6ca18-14bf-31c1-968a-97cb20228e11 | -13.383 | -46.947 | 2024-10-16 02:06:21 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 98.5 |
| dacd7d2a-6e8d-3445-8a74-8910accbaa81 | -17.2439 | -42.6575 | 2024-10-16 02:06:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e80df98f-af42-3824-bc47-c3efbf951514 | -17.0262 | -58.2912 | 2024-10-16 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.4 |
| 9cf5cd88-7f99-350a-8505-c3ed59c13225 | -17.0066 | -58.2934 | 2024-10-16 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| cf41a0ee-7a89-3d61-8d66-9df2d3ce7385 | -17.2177 | -57.3102 | 2024-10-16 02:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| a93e7b18-c343-397c-b2a4-4d96c0ec2669 | -17.2157 | -57.4334 | 2024-10-16 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| f045b73c-aeda-31d6-83f2-a2edae60db43 | -17.2081 | -56.6946 | 2024-10-16 02:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 74b64463-4f0f-3640-b25d-b43d643ab309 | -17.196 | -57.4357 | 2024-10-16 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| fc5fbae8-ab66-3e7e-9993-f25c7b76f0bc | -17.1954 | -57.4767 | 2024-10-16 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 312dd91b-e893-3159-bd76-228da8f57451 | -17.1951 | -57.4972 | 2024-10-16 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 16f234fa-cd1e-3972-99e6-bc7cc4af5f8c | -17.1758 | -57.479 | 2024-10-16 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 75b94505-95b2-32d5-8779-654e8e59bb1a | -17.1754 | -57.4995 | 2024-10-16 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 61dac6e9-c1f6-3135-a0b9-1e13d1b7c966 | -18.2574 | -56.4154 | 2024-10-16 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.2 |
| b9a6fb5c-4d54-3537-9a0d-768fb22c3dd4 | -18.2383 | -56.3763 | 2024-10-16 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.2 |
| cd1cf830-cde5-36aa-8959-6d42ada0ea08 | -18.257 | -56.4363 | 2024-10-16 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 8ff5cdc3-073b-372f-b21c-928b27648ec4 | 1.0016 | -52.2164 | 2024-10-16 02:15:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 9e6b27d1-f72e-32af-81f9-53deccc74f27 | -3.1098 | -54.2464 | 2024-10-16 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 4f430848-e9f6-3a2c-b174-f1e47d74f9e6 | -3.1099 | -54.2263 | 2024-10-16 02:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 157.9 |
| d12f5ef8-cc39-3309-be05-eaa212f76113 | -3.1282 | -54.2459 | 2024-10-16 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| ca8bab66-f0bf-36c5-bc41-edf6d2548932 | -3.1283 | -54.2259 | 2024-10-16 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 189.3 |
| 8ad65969-574a-391c-bd30-bcf3c2f23fd7 | -3.2862 | -47.133 | 2024-10-16 02:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 115efbc0-a9d2-354c-957b-23aba1dd53c3 | -3.288 | -50.9321 | 2024-10-16 02:15:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 99f9c6f6-0ad5-36b3-b7e4-1d1575d3f1da | -3.958 | -46.4442 | 2024-10-16 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 6ee87f81-32bd-3e0d-88be-cf81347a8055 | -3.9581 | -46.422 | 2024-10-16 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 684dd272-7600-3c8a-b545-3ea0298fc9c8 | -9.0948 | -47.0316 | 2024-10-16 02:15:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 358eea59-8904-3af8-8bf3-5d18b3555ad3 | -9.1137 | -47.0296 | 2024-10-16 02:15:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 8983265d-46a7-38e4-b784-a8d206457b4c | -9.3805 | -40.3998 | 2024-10-16 02:15:58 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 28f99686-29d5-32c0-bd98-b35bf2d66ab3 | -11.6917 | -65.2243 | 2024-10-16 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| acd537b1-8ba2-3b85-9ef7-a1b2c012c3a4 | -11.6918 | -65.2054 | 2024-10-16 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 6f9aaa93-3898-3820-a57e-1b6f6069706b | -11.7103 | -65.2424 | 2024-10-16 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| fbc9bdc3-5364-3428-b6ae-a45d9c160054 | -11.7104 | -65.2235 | 2024-10-16 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 8e9ba8a6-4078-3793-b6e2-06c511202787 | -11.7106 | -65.2046 | 2024-10-16 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.9 |
| dd831001-7be8-3b16-b80e-c653df98c6ec | -11.957 | -64.8721 | 2024-10-16 02:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 874e24b8-d4e0-3c6a-b273-d9e09896e125 | -11.9381 | -64.8729 | 2024-10-16 02:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| da98e7c5-244a-3bd2-b44a-1af204fba592 | -11.938 | -64.8919 | 2024-10-16 02:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 1201187f-8e4e-3e6f-a5ea-dd3d8a216b21 | -12.0619 | -46.7134 | 2024-10-16 02:16:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 8a2861bf-8cb7-3285-b823-1bf7d5013a80 | -12.0431 | -46.6935 | 2024-10-16 02:16:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ddb4aae3-f8c2-39d9-b473-116620df1397 | -12.0427 | -46.7161 | 2024-10-16 02:16:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| a00b6b95-5638-3b91-a07f-2babde4c764c | -12.4925 | -47.2818 | 2024-10-16 02:16:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 532ce091-079f-3270-9f3f-ef271e7bab18 | -12.3983 | -63.7093 | 2024-10-16 02:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 110.0 |
| d30db8a5-8e5b-3935-a539-327aaf131594 | -12.3982 | -63.7284 | 2024-10-16 02:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 84d221cb-9524-3fd7-b1a3-0f513e71272f | -12.3795 | -63.7103 | 2024-10-16 02:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 15effc25-f9f3-3cb1-8802-c90389bab3ed | -16.9403 | -57.5063 | 2024-10-16 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 40e6b312-2e6b-3657-a58e-9bf0bdd0514b | -17.2081 | -56.6946 | 2024-10-16 02:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 91cf9340-ddca-38b0-b495-447db8da1668 | -17.1954 | -57.4767 | 2024-10-16 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| ed861b12-03e8-3f2f-9617-fee87dba4314 | -17.1951 | -57.4972 | 2024-10-16 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.9 |
| 9e765ead-50b6-3840-9fb7-691ccd28a3c1 | -17.1758 | -57.479 | 2024-10-16 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| a399e5c9-ed84-36c6-9a4c-586b67a8cd57 | -17.1754 | -57.4995 | 2024-10-16 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 6d6ba276-6d86-3eb9-a39a-7457cdb24927 | -18.2574 | -56.4154 | 2024-10-16 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 75690eae-3495-350a-a29e-74064a6a3064 | -18.254 | -56.6029 | 2024-10-16 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 54798397-a019-3de7-82e0-ef6c73348159 | -18.2544 | -56.5821 | 2024-10-16 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.2 |
| f39d1e24-f694-3560-bb5e-7e019bad17c4 | -18.2548 | -56.5613 | 2024-10-16 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 6baad21a-2065-3b16-a053-9191bf0465b9 | -18.257 | -56.4363 | 2024-10-16 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 385b9c64-7690-33bb-b1e2-a928dc13b81b | -18.2746 | -56.5587 | 2024-10-16 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.9 |
| e9097977-21ab-3ddf-9ca1-bb106838869c | -18.2742 | -56.5795 | 2024-10-16 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.5 |
| 12dd1ba8-8b27-356e-86ee-495e441a0a74 | -21.0671 | -51.0712 | 2024-10-16 02:17:02 | GOES-16 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 132.3 |
| 2e199f59-5352-3b60-8da2-10b0e340cc8e | -21.0677 | -51.0486 | 2024-10-16 02:17:02 | GOES-16 | LAVÍNIA | SÃO PAULO | Brasil | 3526506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.3 |
| 4f7a4082-2d88-3dde-aef2-0f6584781e99 | -21.0877 | -51.067 | 2024-10-16 02:17:02 | GOES-16 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 185.9 |
| 9ecf92db-fbc4-39c5-b598-a9a1f6659c0f | -21.0882 | -51.0444 | 2024-10-16 02:17:02 | GOES-16 | LAVÍNIA | SÃO PAULO | Brasil | 3526506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 138.6 |
| 5159c043-d399-3e6b-8dd4-f9903c410495 | -12.332 | -63.715401 | 2024-10-16 02:21:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9e88de21-df53-3b24-95e5-2500b3b99d07 | -12.3224 | -63.718102 | 2024-10-16 02:21:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bc0f65d4-3834-3ff3-b3aa-02c2043e2e24 | -10.5722 | -67.835098 | 2024-10-16 02:22:09 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 70d8ea71-c082-3b62-8baa-a5c12e129e65 | -10.5756 | -67.848801 | 2024-10-16 02:22:09 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 76fa0aeb-ddfa-3075-8369-e64c916368f3 | -10.8468 | -69.638702 | 2024-10-16 02:22:12 | METOP-B | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 04053481-aae4-330b-ac31-e50a778c33de | -10.8493 | -69.649101 | 2024-10-16 02:22:12 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c7460791-f439-362a-9d7f-c489aa8214ce | -9.7228 | -67.947098 | 2024-10-16 02:22:23 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5814c97f-e08c-3b6f-b46b-1afddbb8b46b | -8.5591 | -70.041 | 2024-10-16 02:22:50 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4f0aa18f-9b15-348a-8580-0276373f27af | -7.3497 | -72.623398 | 2024-10-16 02:23:20 | METOP-B | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6c47568-4db4-35fe-ba84-548ae3031ab2 | 1.0016 | -52.2164 | 2024-10-16 02:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 00b133d2-7b41-3118-a336-f9a1fec3dcd4 | -3.0687 | -50.3746 | 2024-10-16 02:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 304b65b8-1a3c-3047-a3e4-505b800ee7e3 | -3.0688 | -50.3536 | 2024-10-16 02:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| cedbdb30-fb30-3d92-b79d-b0d107bb2929 | -3.1098 | -54.2464 | 2024-10-16 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 1accfbb1-24f8-30f4-8cf0-be37f40bb5e2 | -3.1099 | -54.2263 | 2024-10-16 02:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 06153161-b291-3ccb-84a6-75db4b5233eb | -3.1282 | -54.2459 | 2024-10-16 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |


[Clique aqui para ver as próximas entradas](README22.md)
