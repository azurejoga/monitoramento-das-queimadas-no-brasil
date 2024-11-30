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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ae05e26-8845-31d8-b9d9-8413b1aedc94 | -3.81121 | -52.31634 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47a3a264-4c54-321e-81b5-d77a0e4317e9 | -3.84437 | -52.02403 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9321a0ee-c085-3eb1-a010-7aa0393b39ad | -1.11106 | -53.59306 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ffed4b3-471d-3989-b41e-142ccd3d0387 | -3.49974 | -53.79772 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd80f5b7-b99b-38b2-b290-47e96cda404a | -2.85 | -54.08438 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7546decd-63f6-30aa-9476-083db15da7dc | -1.09492 | -53.60851 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83888284-9ba9-3ef7-b046-d4c21dbb9ab1 | -1.64723 | -52.40176 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b82d3b74-c8ea-30d5-ae9f-6b7f17673ee0 | -2.69775 | -51.36376 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dabcaf85-79f9-32cb-9cd4-8465288f4c11 | -1.21653 | -54.18922 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ef82a24-18aa-389b-a550-631b2d6fc41a | -1.62115 | -53.33088 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f976e56-5950-3f4e-9b74-f7fbef56ef7e | 0.99354 | -50.26158 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03eda128-e163-3ab2-be5b-7b3b3ac0b6f1 | -3.22473 | -53.61332 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 462d7113-5563-313c-9ee2-c02ca4fd8ead | -1.60605 | -48.6989 | 2024-11-30 05:01:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3487708-9a9f-37c0-8e2c-726785272aed | -1.72597 | -52.4753 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cbf3e20-fd8b-3b4d-816f-6ea5861be174 | -1.59766 | -51.27327 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a1e6359-6c8e-3014-8b78-15ae921dab6e | -2.62179 | -46.80099 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 074e8a8e-5b35-31d8-9a54-b186d39905db | -3.32204 | -54.17884 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a90c0660-bb8c-3b1e-951f-50c72e91a188 | -3.09248 | -54.0283 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3e7a7ae-4712-39ea-9ad2-9317ba98dc05 | -2.98267 | -54.08335 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb20aa1b-342b-36e6-9377-3153bf2ee598 | 1.29224 | -50.70809 | 2024-11-30 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73f1dde1-ebce-33df-8a1c-88f3d2605eb9 | -1.25275 | -52.17897 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71e8c84e-dd7b-3309-b046-410d48f5ccf3 | -2.79868 | -54.0406 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbe13378-8c34-3d94-ba53-86f1a2d0b4f5 | -2.27879 | -46.44007 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b277f67e-ef22-3fa7-a48c-30fe250513ce | -1.5893 | -52.28391 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 15dcbd53-6384-3041-a0bd-7d819f67205e | -3.05851 | -54.04823 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c20ccc1e-58d5-3a0b-b298-705a3e89cf22 | -1.76978 | -55.67604 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b013a44a-ff84-3247-9f32-3d322a521689 | -3.11738 | -53.27014 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e093ef16-ca37-3d99-9a1e-4c8ea916f2a4 | -1.82936 | -46.30399 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff68b572-60ba-3c44-bc89-83d6baacd2b9 | -3.07849 | -54.56869 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec583e36-d7a9-328e-9502-befe551b7117 | -2.90222 | -54.18181 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 063a28c3-48a9-3231-b5d9-63dda8c00af5 | -0.92743 | -51.62842 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 719f53d0-3ea5-3f6e-9324-467c7df8483f | -3.09918 | -54.02935 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce6410b1-1bf8-3307-9e1c-aaa5add5f596 | -2.84717 | -54.05887 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d54fe26-2de7-370e-84f4-0f070997229c | -2.78549 | -52.98248 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93b61868-c149-3052-9180-3e363bbe0fac | -3.11173 | -53.10786 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02ff1e0b-f329-3f9a-9266-719acc155476 | -1.16941 | -48.15783 | 2024-11-30 05:01:00 | NPP-375D | SANTA BÁRBARA DO PARÁ | PARÁ | Brasil | 1506351 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a650ba9-e1de-39e5-9e5a-4284a858c922 | -2.97846 | -53.89201 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07e8675d-0544-388e-a9d8-8935a120b381 | -2.85102 | -54.03436 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2319245c-d224-3698-ad0f-ad8df11aab6e | -2.70707 | -52.0024 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2678d9ff-bca4-3240-b3d2-3a8577db98ac | -2.98536 | -53.35522 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d24874a6-bff1-3fe9-a60c-b4e1934cf4d5 | -4.23583 | -47.57527 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 772707c9-0fb4-3b82-9a41-f6d70bdc5cc2 | -1.14357 | -53.61591 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ca702dc-0af2-3051-8b95-5e1e727161c6 | -2.84501 | -54.09436 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 296f6e12-0667-304d-b01a-6e7852730d5a | -3.11788 | -53.98957 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80e58cde-6b46-3f25-9a29-19a7eeb68026 | -3.59643 | -49.98679 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83707d30-ffe8-3461-a9e8-bbc6855722ce | -4.05729 | -49.05511 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7c1554b-6ade-3eff-b150-a9d3bcc2859f | -3.87286 | -49.99107 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a96d7af-091f-3b44-a085-4bd05d152834 | -1.69451 | -52.46353 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8522d62c-007d-36e8-aeab-4db95b8427f8 | -3.12834 | -51.11907 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92947e45-297b-3e08-9558-dc66deac8ce6 | -1.57339 | -53.83273 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ef3e251-dd1c-38c2-aae4-8ac341f9f371 | -3.3931 | -53.271 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f0078fe-0245-3360-bc9b-ecfffde19cdf | -3.43287 | -54.11684 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 553a7656-4867-397d-bbe0-c44070f6ef08 | -0.77676 | -52.38855 | 2024-11-30 05:01:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d5c6eb1-c2e6-35e6-b0fb-01415e3230a7 | -2.94176 | -51.5895 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6f0e6e0-22ad-3232-8113-f39e30184aed | -1.25193 | -51.79035 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 320a7187-09d6-3b02-94f4-fa7a5cc53f06 | -2.63109 | -46.20128 | 2024-11-30 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0c5b7d6-50fd-30cd-b857-a222742d9232 | -3.38237 | -50.69897 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1e6cdfd-1b89-3eb6-a5ad-499d4415df5d | -2.19392 | -53.77752 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86a99f8e-a12e-3736-89c3-403d1976f8b1 | -3.23824 | -53.63754 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cbdfbbf-27df-31b1-af4b-5515f175990a | -1.0609 | -55.24295 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| badb8cc7-7100-3128-9c10-1c117b9c7990 | -1.18681 | -51.76391 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42f9d714-0797-3020-8dcc-a8036d4f6ef1 | -0.98706 | -51.75123 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1fa4c9a-a062-3175-82b9-eb2fd3217369 | -3.29905 | -53.82917 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 157ddea7-ebea-307f-b6fb-805823dbc412 | -3.05684 | -53.16751 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1590fdb8-f6ba-3d07-bdfa-ab8800aba922 | -3.4039 | -50.66273 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2684a49e-e140-3628-aed4-8287601d79bf | -2.63568 | -46.87819 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d52154c0-1b17-3931-b1f1-8653605f1980 | -1.30633 | -52.86546 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44914d42-1d2e-3556-90db-7e8adc4f3256 | -3.03898 | -54.04162 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e076d10-a1a2-3466-bbe9-1e5066b929a9 | -2.98933 | -53.35212 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4630f2f1-875d-3430-8b31-5c4f9283d656 | -1.39162 | -51.59126 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64f9ba7f-9c08-3610-ba88-070758f35db2 | -1.12931 | -51.67413 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22bec4aa-561b-3d9c-83e8-5313a9e81398 | -2.43666 | -53.89458 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e790487-4cd0-3fb0-a8d5-06000f708b7c | -1.37327 | -55.87922 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9de25d98-1d16-35db-bcaf-874400f07745 | -3.28141 | -53.69878 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3d26fba-dc03-3a87-8dff-18bb6e2c27aa | -2.748 | -54.11164 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af1b1065-7e53-305f-8839-53bcc3949444 | -3.0557 | -53.2199 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2d0d029-5ea9-3f3c-b8a4-3b35e4c3a358 | -3.10696 | -50.36401 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83916103-5b7a-3952-9252-f562172fa98c | -2.76497 | -55.33594 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| faeb4e07-2bf9-3972-8a1e-96464c867a62 | -4.06194 | -46.67994 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09503745-a074-33dc-959d-bf73a53bc755 | -1.32517 | -54.63698 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b81cdf8b-5270-3d52-b8ae-8fbbce09b34c | -3.10451 | -53.82057 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 734dcc43-a815-39f1-903d-8453d8af1d75 | -2.61052 | -46.5784 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fb826f6-6a00-3e82-b11f-cf08ab622261 | -2.35107 | -49.00888 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dae46219-fcd4-3e0c-830f-4cf5d797b25d | -1.1791 | -53.8857 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1811c4e8-445a-3072-a0fd-e2b2b62e600f | -3.68867 | -50.9255 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea4d6c79-94fa-3a2a-b62c-cabd280a2a40 | -2.57079 | -49.99755 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8554e26a-87b1-3023-8322-5ffcc9ce2ffd | -1.1793 | -51.95356 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42accd94-add6-32bc-8e05-69acbe8502e2 | -4.30381 | -48.23163 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5e64c07-b530-342d-af28-2fd837e01006 | -3.69604 | -51.7986 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0e1a1ae-c0ed-3b0b-86ff-c9d0fb69142f | -1.23583 | -51.80014 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d852033c-5eca-3b6e-9f46-6bee9e25f369 | -1.11259 | -53.40944 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c91fb3a9-e4bd-30bd-8ed4-b5ca08d32e08 | -0.27136 | -51.62771 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cb0b825-6dea-38ab-a91d-b84044edcdaf | -1.08937 | -53.64361 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 06b569fb-03a2-314e-84fb-20e2b12288d1 | -3.08242 | -53.25032 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6152771-de9b-32d6-ae4f-f995524bd4d2 | -2.96737 | -53.9408 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59604b92-a22e-3eae-8b42-be80d11d487a | -3.3716 | -50.17987 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2acd92ad-1cc1-33e9-a962-bf7f02543355 | -2.80148 | -54.04462 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8da94da6-ad48-3fe8-bf57-aa5e90315f5d | -2.56625 | -54.33922 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2416c0d-d628-33a5-9c38-33bdf04a89c4 | -0.88101 | -51.71576 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47322114-f01c-3ae9-8632-65e322038ee8 | -2.98556 | -49.59087 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README96.md)
