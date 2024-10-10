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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c60993cb-8995-3438-885f-2bf0da0ffc83 | -4.06133 | -51.11499 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a76b15ac-8f6d-3077-b5bb-8fe5980660bc | -4.06044 | -51.121 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 124c2825-7613-39d8-bdad-8af801e430fb | -3.84889 | -51.25817 | 2024-10-10 05:36:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a0dbe6f-6869-327d-8ca3-09cc15225d86 | -3.84252 | -51.25726 | 2024-10-10 05:36:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bbf3f1e5-ec43-3eed-b2c9-ac8113ea37f5 | -3.69034 | -51.1082 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 825385c6-372e-3a85-8c2f-83abac6c1dae | -3.68957 | -51.11351 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2dfb726f-83a9-32d3-9415-c3d08eccf6c4 | -3.68924 | -51.07058 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ab616c5-008a-3c8f-920b-5f960d0c205b | -3.68393 | -51.10722 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88633a8b-0d47-3d4f-858b-db834d78a40d | -3.68316 | -51.11254 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92631a5c-2d09-361d-b181-0774686bf098 | -3.68284 | -51.06946 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 619d5f01-5548-3f3b-9b8a-2fc33e333172 | -3.55857 | -52.05282 | 2024-10-10 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bff56d0a-985a-307b-86c1-80b942fb59bc | -6.40914 | -51.71917 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d4245ef-2824-3536-a78d-54099865affa | -6.40725 | -51.71945 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6c271292-f931-356e-90a8-9a48599fb07d | -6.40275 | -51.71814 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 400b350b-f530-38a0-a487-3711a85a4879 | -6.20429 | -51.50747 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23cf83af-6521-3f3b-bd4d-cb58fee9fe4a | -5.76176 | -51.44538 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51ae3b2a-093f-3685-a83a-9679c15645ed | -5.761 | -51.45095 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 324f05e1-db5e-3936-a7bf-dd75b97ea0ae | -5.76024 | -51.45646 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bea14390-240c-3989-abea-85e0f215faa7 | -5.75455 | -51.44993 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e4eed04-640c-37e8-8c71-076b86aac044 | -5.07121 | -51.95369 | 2024-10-10 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 835420c3-04ca-3bf0-ad39-a2c0db51ed87 | -6.39521 | -52.72248 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 85aaa34d-083c-3b6a-a565-d4d7fca6c46a | -6.3946 | -52.72704 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 373b7e17-a115-3cf3-90c6-acea1cd2b39d | -6.38858 | -52.7262 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ea0a7e1-e5a3-3213-8883-d04d801c7e8f | -2.68445 | -53.34629 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7e339b72-0a21-31e2-908c-d7db118419dc | -2.68392 | -53.34986 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 70d6cd10-43e2-336e-aa4a-e2b220b71f72 | -2.68339 | -53.35343 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a7512551-4f43-314d-b501-61dfa2b33946 | -2.68003 | -53.33825 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 91c3d9f6-d212-38be-90cc-cd6139ff57db | -2.6795 | -53.34184 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5dc88cb9-d717-300c-9aad-94048b9c6c0a | -2.67898 | -53.34543 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e004ad64-954c-31d4-8db4-1d21658b479c | -2.67845 | -53.349 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e6d14700-35a8-3633-b20a-6f763a85c490 | -2.67792 | -53.35257 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5cf15b3c-6f41-361d-bb7a-04bd969d5bb6 | -2.67456 | -53.33738 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0082a7e1-18b8-3b79-9027-31c262220794 | -2.67403 | -53.34096 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d6298a80-4629-34eb-a105-659f55955a43 | -2.67351 | -53.34454 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| c29b3912-86cb-31ed-b8ea-dd9d5486db63 | -2.67298 | -53.34812 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 2edb4625-5f85-35aa-8185-55116d518c26 | -2.67246 | -53.35168 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| fd539c87-41ad-36e0-a28c-6fee31b1de53 | -2.67193 | -53.35524 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 04cfe96e-fa00-3db9-afbe-476eff3c29ba | -2.66856 | -53.34009 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c2cadd22-e393-3c45-9b32-fa30287cfddf | -2.66803 | -53.34367 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| a062839a-8faa-389f-be31-fff870c080e6 | -2.66751 | -53.34726 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 0ecbbf41-f4e5-3f5a-a631-cb7d9833e7c3 | -2.66699 | -53.35082 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| bade262f-288c-35ff-b2b8-4849fcf7d334 | -2.66646 | -53.3544 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| c48f3f1b-5a98-3cab-9d2a-3e5f268e2adf | -2.66256 | -53.34281 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8289d5fa-7b9b-3d1c-9be1-001fa0f180cd | -2.66204 | -53.34639 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cb78e041-2554-3f90-a701-2cb02b8d8a53 | -2.66152 | -53.34996 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e2fb4703-76b9-3545-aade-18926f40ac03 | -2.66099 | -53.35354 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 0ddc8ad8-fe3d-3df9-97b3-c9d4f71a49ce | -2.66047 | -53.35708 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 2925a423-eccd-3667-96f1-6026a0ff0819 | -2.65657 | -53.34551 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6823d9c6-9d33-3c91-8bbb-91faddf87c38 | -2.65605 | -53.34909 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c68b92d5-77a5-36c3-a65d-9c0e74fa7382 | -2.65555 | -53.34657 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c19fef2-df78-32d6-9a86-971d0292aa63 | -2.65552 | -53.35268 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| b46abb0f-a3a7-3c8b-a455-35ae984356f0 | -2.655 | -53.35623 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 7ab2734b-859e-3dce-80bc-a5870c7191cb | -2.655 | -53.35016 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 114bd48c-223e-33a3-a2cf-51ecd1eca93e | -2.65445 | -53.35374 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| fff1c61a-be4b-3365-9394-ea0e58027076 | -3.51212 | -53.01573 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71328984-23ee-3176-b3d7-7fdb1b60a884 | -3.49857 | -53.45125 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ef2599a-5b86-3f4d-89ca-a05f8ed93239 | -3.49848 | -53.45345 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ba2f66d-9db0-3f4a-81e0-511a80c0c49c | -3.49805 | -53.45474 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f38ba84-b81c-3b51-abe4-7b592c32c7a5 | -3.48328 | -53.28884 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a63ab6a7-d971-3121-9aab-83e572785265 | -3.47771 | -53.28804 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fed6d533-25f6-3d45-9b8e-27f4ee0015ef | -3.45202 | -52.81505 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f02cc147-18a4-3d45-b25c-fbe2a376a3c8 | -3.44633 | -52.81384 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45d23464-7951-35bd-a0a3-e1867c95f21b | -3.35695 | -53.37851 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36f8c43f-5857-3b00-830d-93c84cde349d | -3.33449 | -53.22233 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9f206927-f50b-35b5-bbf2-de187c1878f2 | -3.33395 | -53.22606 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5f59bd32-7fa8-349a-9bc0-fca695029f12 | -3.32947 | -53.21764 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f9a25570-ddd2-37a1-9e58-6c3cb034eea7 | -3.32893 | -53.22135 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2b5cfb30-d77a-3e9e-86b3-0e937bd0284f | -3.32838 | -53.22513 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 54e25ae3-b30a-308a-bb50-064105271482 | -3.32728 | -53.38852 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 559c8893-9e00-3240-a05d-92e9d90b95a1 | -3.23105 | -53.27593 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a152bbf-7a52-37eb-9834-8a6baf6e7e2e | -3.2305 | -53.27973 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07df2203-c328-3021-bda0-b526ed3b987d | -2.86225 | -52.90751 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8687de4f-be93-3667-a76c-8b1673e4a82d | -2.86167 | -52.91142 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a0b36fe-6bb0-3f4e-8730-ce8d02325101 | -2.8566 | -52.90657 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aed10ac6-753d-3ae1-ab63-bdb1316edf14 | -2.85602 | -52.91056 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6cb7f74d-c0a7-3bbb-b874-86059cf786d8 | -2.85145 | -52.9416 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6d1c710f-26a9-336a-a562-dd568b478971 | -2.85097 | -52.90559 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 72c18630-ee01-3a7e-8c16-61ee1d2180b6 | -2.85038 | -52.9096 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7a78c575-3ff5-3fab-ae43-ac3a876ad463 | -2.84693 | -52.93316 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 09a86450-3830-3b5e-b8b9-ed39de5ad4e4 | -2.84636 | -52.937 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 10b8cceb-ade4-3157-8635-0e45214c4e1a | -2.84582 | -52.94068 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5b04eb17-c8ee-3afe-ba21-175cc9a4c860 | -2.84474 | -52.90865 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dcca90ec-0a4e-3741-a99e-ea4779692dcb | -2.84084 | -52.9746 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2faf67a0-6d5b-348a-9059-60670354627e | -2.84074 | -52.93602 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 664142db-6855-3f5e-95a2-5acb694f673a | -2.8407 | -53.31979 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2741901-3237-39f6-8bbd-264d4ea3d1a7 | -2.84016 | -53.32339 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b200a52-c621-3762-af80-7d517ab0a1a0 | -2.83525 | -52.97354 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a11b2a0c-9201-38de-a9c8-5766df93031c | -2.8347 | -52.97726 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6d50bb6-841c-3796-aabf-f098d34660bd | -4.08838 | -53.62508 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6031adcc-25b6-3a91-b0c9-1332c53a9a3e | -4.08278 | -53.62505 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdece2ac-62a9-3f38-b6d4-7b54ed37038f | -3.87924 | -53.63241 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79c580e0-f4f4-3029-9989-d2a724979389 | -3.80719 | -52.42049 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96bed636-af62-36bd-aa4b-7de0e678f83c | -3.80188 | -52.41536 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea86494f-a0d7-3154-bdd7-099c7e942923 | -3.73963 | -52.31625 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a651dccf-7ef7-3e63-9570-973eee0239f8 | -3.73431 | -52.3111 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12c8a382-f800-31ff-954b-1beeadba52b6 | -3.73366 | -52.31554 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6288e4f2-0e4e-3a06-aa6e-180e726b22c9 | -6.60345 | -52.89516 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c134efd5-0e4d-31a5-9933-6e433a676f32 | -6.59768 | -53.07207 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c193d245-954e-39d8-b9ce-32c88cf3d229 | -6.59709 | -53.07644 | 2024-10-10 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aed4bba-4f13-31e0-a2a5-0ed6c27440eb | -8.61912 | -54.59838 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README128.md)
