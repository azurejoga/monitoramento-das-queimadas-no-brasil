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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ba61e0f-dbc3-37ee-ac90-408fe35e5791 | -4.46909 | -48.81594 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3880f38b-6b0b-3af9-a3f8-51bf4f216502 | -3.0237 | -51.19607 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7773ba9d-d5b3-3ec8-af6f-3bb69070e898 | -5.35859 | -44.14172 | 2024-11-09 04:55:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ed50989-2562-3fe8-8e31-dffbf6767797 | -1.44322 | -53.00208 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cb9dd77-9a58-39de-ada5-4b6bffb5e878 | -2.57549 | -49.13425 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2944d519-e406-3a76-afbe-c3f2f2ac02ba | -1.24719 | -51.76896 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06b4785a-b146-3a26-a2ec-9645e53a535a | -2.23018 | -48.3737 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 512bab87-7aef-325c-9b50-d92e85efb481 | -4.75471 | -48.36308 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10f00c6d-1492-32ce-a2e0-aa72dc66dff5 | -3.63732 | -50.75511 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d82ed2a4-ffa4-3fdc-b893-7897eac59910 | -3.07361 | -53.88327 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6819e55-00fe-3490-8bd3-6edf5856a388 | -3.09237 | -54.55769 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcf3cbe0-a5ef-371c-b6eb-e6b70012f28c | -2.17852 | -53.70422 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47b91ff4-15cb-3da7-9ce4-9e3f30d823f2 | -1.68247 | -53.17725 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7cdd7cb-734e-302d-ac3c-b159e4617e77 | -2.15027 | -49.14031 | 2024-11-09 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 892d2039-10df-3aef-94d5-b0ec4b174d01 | -3.78718 | -51.32712 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3131804-095e-33d3-b196-43ad1af8f914 | -3.11719 | -50.15221 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 322aaac0-c0a8-30b2-b2d5-c84724e58cd3 | -3.2835 | -53.67164 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54e2be07-3d27-3b7d-a167-b4acd7997163 | -3.2715 | -53.33772 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60b19115-b45b-38d6-af2b-064a7aa38d15 | -2.86972 | -49.37563 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 058c3f10-1ab8-380b-a581-89ed6159dd87 | -2.10283 | -51.09679 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71bda47c-0cd3-391a-8af0-80dc292aadfb | -2.94424 | -51.50041 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7892016b-5d00-3d6b-9828-f4ef5dd20fed | -3.97459 | -48.18882 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d209eeec-a061-30ad-9cb8-42a6e295826f | -3.70823 | -54.34688 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0278c38c-b779-3043-a72b-99562598d657 | -1.36791 | -49.35262 | 2024-11-09 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7773bb45-1ba9-3a76-8e73-7fa478241a4d | -5.63015 | -44.83436 | 2024-11-09 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9703c23b-43f9-37cb-9600-ca3083efe525 | -3.03933 | -50.36094 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18510f2d-6cd8-391c-a4da-e062253c6605 | -0.00058 | -49.9607 | 2024-11-09 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f9526cb-633c-3192-b4bc-d9cb3f1355d5 | -3.67086 | -54.237 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13caa2c5-76a9-3cf7-9799-e1c23deea9ee | -3.97726 | -46.41615 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aa611951-5a9e-35df-94b6-dfcbcbcfc6fe | -3.84945 | -49.89817 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fbd4db8b-fc24-3394-bdce-4b9a2184a66b | -2.62922 | -46.77888 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4ccf853-f1f3-36b9-8a84-cd066f72f8ff | -4.24473 | -46.01451 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ca49e29-005f-3bff-b7d9-aec3627b74af | -3.08746 | -53.88192 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b26df114-a1f8-3634-8a46-13fcbaece576 | -5.80847 | -44.48085 | 2024-11-09 04:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 237f8d47-b03e-388d-80fe-b3e4a2f57ff6 | -3.29817 | -43.54333 | 2024-11-09 04:55:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2fbc5d3-679e-3ee8-9b40-248fe098cb61 | -2.96193 | -53.86255 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8be5324d-ad64-36d3-aef6-170503386dae | -3.01186 | -53.43861 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70ab4c91-dacf-38ca-9bb5-2c6c8b48ec36 | -2.86028 | -50.3224 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 855d7f77-5948-3f92-bf54-8547a5cdd469 | -2.80796 | -52.9931 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b9f8d72-1e28-37ca-b7c8-c0533cfb8387 | -2.32441 | -50.57327 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ee17c6f-29ba-3b2b-9762-644d06adf634 | -2.46487 | -53.68821 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5d9a6f7e-ccbd-3e3f-ae6e-0dea3b9df9f8 | -6.54933 | -46.91644 | 2024-11-09 04:55:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69bc92ab-4c9f-3e6a-82e7-5236ffb9c849 | -2.2821 | -53.81985 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3152b1d-4eca-3d0a-b639-c21f8f8e1b54 | -2.26153 | -46.83147 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8a5869c-2757-311e-b762-c90ddee2e3ca | -3.71299 | -53.39281 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29b5bb3e-7dfb-3d93-9f6b-2f60d45f6026 | -4.23082 | -47.55508 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92c2468e-d839-3347-b5a6-5ae7148d473f | -2.52611 | -47.06628 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 000d10f0-863f-3699-8e59-488ae4410c3e | -2.0836 | -52.04608 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e59e75c5-3e0a-38e2-88b2-f0f0ee0494a5 | -2.77657 | -52.86798 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3147c9e6-704a-3b1d-b53f-fe891d30b51c | -0.3879 | -51.94181 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e836853f-3d8f-386c-a8ec-54f0f31dc35f | -2.86713 | -47.90483 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56d7b6a4-a90f-3f78-bd54-7932074e652f | -3.02904 | -53.26474 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bc7e7fa-eb19-3f45-800b-c8f3a5dbad87 | -2.40234 | -48.49805 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e82ef7ef-78e3-39a6-89d3-6b30f70efdeb | -3.32899 | -49.10085 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db3ab859-056d-34b7-98e1-0ef4dc9fb768 | -2.97476 | -53.91079 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 470f581f-ebc9-3837-baa1-5f48575d8d68 | -2.5752 | -54.02288 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dade732-16f9-36c5-b904-d73addb24e67 | -4.8386 | -45.63912 | 2024-11-09 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eb278d8-282b-3783-82bd-9aedc81d6a43 | -2.93565 | -51.53296 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cd67f84-711b-3d77-9cff-334c59968ecf | -3.25111 | -53.35926 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 545d0186-435a-3683-9fb9-9cf740453004 | -2.4221 | -48.47506 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5053ac99-15dc-3884-8cfd-c315404e7b2e | -2.07976 | -50.3437 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9066762-50a1-30b2-8b74-0f23e825b8f5 | -2.11911 | -50.66363 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a6e1dd0-503e-3e91-9da1-778bd3ef6bf0 | -2.72892 | -51.73941 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac1d15a6-7e36-3317-a0ea-cdc4f17c21bc | -2.32995 | -50.44455 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0808af7-450a-3396-b93f-fed36501bdc9 | -2.32115 | -53.67668 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a50fd314-7f7a-3d32-9b0c-7eae4df40f57 | -5.47055 | -43.65205 | 2024-11-09 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 92b6a293-7329-30ce-8dd1-1591889deb50 | -1.52788 | -52.18305 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb20fd8c-e899-3d7d-89bf-8de3bc20e431 | -2.31914 | -48.52402 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d08954cf-6def-3829-beab-6b28a0cbc370 | -3.81459 | -50.79613 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d3c3555-741f-372c-a5de-79eb20bb6f76 | -3.03023 | -50.37207 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbb59c29-978f-3e31-8008-b6f7861ea3c3 | -4.21141 | -45.85041 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fdde5a7-512d-3821-9e4a-1d567ec148eb | -5.04223 | -46.79268 | 2024-11-09 04:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c3a9730-c496-3011-a545-2d695409cd6f | -2.6761 | -46.78501 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 157c9239-df27-3a82-bae9-24602ec559d9 | -3.02196 | -48.07914 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfde9ce3-1aa9-3f84-91e1-ffb5680a90c3 | -1.63001 | -46.11042 | 2024-11-09 04:55:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e596fd84-04b5-396f-81d2-187734ef160c | -2.8327 | -49.43967 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1a12f9e-b1d9-3614-9270-0b6b8e4edb83 | -1.64243 | -52.27197 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ef1a17e-1f4e-3368-81e1-09288d8726c3 | -3.29789 | -49.17444 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2a4b962-da1c-325f-a9a8-ea45070d6829 | -0.22451 | -51.6477 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 671afd56-29e3-386f-931d-54ba72c88f98 | -5.19685 | -44.91868 | 2024-11-09 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf09bd60-9dea-3482-8a48-291e03c8e77d | -1.19646 | -53.91819 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 890f9f8b-1318-3b99-a28f-d7ceea7b6a7a | -4.80616 | -44.78017 | 2024-11-09 04:55:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee5476b4-d1ac-35e0-9c4c-d75ea8ad2064 | -1.3933 | -52.06557 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1932f209-8ce4-3f31-9099-e37d0437ed7d | -2.20591 | -50.33679 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c75cd2b7-ea32-3ce7-8326-03430de4cea4 | -2.93374 | -49.50823 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6780c3f6-4495-3022-90e8-b7b414022b3f | -2.42192 | -50.43307 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 624034f8-716d-3fab-829a-a5693532ecee | -1.51289 | -51.60959 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| efbcc442-4e11-3dd5-8354-6cf80f465f9f | -4.8639 | -48.11554 | 2024-11-09 04:55:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2c4c65ad-1b67-3979-893c-61d106921616 | -2.02008 | -48.01432 | 2024-11-09 04:55:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abde9d6d-3e1a-37bf-b4ac-2a4c72b9928e | -2.39818 | -50.31139 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee92f3f4-274b-3316-8241-6851bb1e62c4 | -3.62122 | -50.19109 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2af4de2f-44ac-32e9-9b6d-e4306de92a23 | -1.51617 | -52.17051 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9b687e6a-8cf7-3220-bc64-195b17a5524d | -1.24216 | -51.77905 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 561106e6-8099-3ee1-ae3a-d042353d76d4 | -2.9215 | -49.36245 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 676c5ebe-4695-3aec-b120-e2e52a4d51bf | -4.69205 | -50.54549 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d853a93-3467-39de-ad96-517d8af49192 | -0.36849 | -51.42326 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b311fe0-af7d-3145-8474-49a3ffcc393f | -4.42716 | -45.70144 | 2024-11-09 04:55:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b75e2ffa-aa8d-3c06-b5d5-723dc28e32f5 | -2.95315 | -53.91804 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09f7d2ce-49f7-3fe5-99c9-68ecd736230d | -3.29264 | -46.41756 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1a5fdb29-f775-337d-8e3f-b90cbdaa07a3 | -6.26553 | -44.53971 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README73.md)
