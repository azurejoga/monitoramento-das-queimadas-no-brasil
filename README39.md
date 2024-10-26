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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42682f01-5c73-39d4-8859-3ba718a682a9 | -4.91418 | -45.86384 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5826a186-2821-31c2-97d7-eece1f69cfcd | -4.86183 | -45.77724 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06d34330-4f52-30c0-978c-5b8f6d2a51c2 | -4.86125 | -45.78086 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 869621c0-6c1c-380c-ad90-4eed483b17f4 | -4.82273 | -45.67156 | 2024-10-26 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 629d1585-475c-3f0b-b6f5-ee823da566c6 | -4.81082 | -45.70281 | 2024-10-26 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 885419dc-b8ef-3a38-b646-c47bcaae73b5 | -4.76316 | -45.76189 | 2024-10-26 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f86d61ff-e33b-364f-9f77-7df6860fba89 | -4.75976 | -45.76137 | 2024-10-26 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6be8d99-a3b2-3463-9b63-8c39be4beea1 | -4.7445 | -45.67786 | 2024-10-26 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50963429-aa5d-39a5-9566-eff5fb625fa2 | -4.74111 | -45.6773 | 2024-10-26 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b121ce3d-5ec8-3ab4-80f8-07ebe8b7e039 | -4.68137 | -45.8127 | 2024-10-26 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a091e2e-db61-366e-8bf1-a564fba9c881 | -4.58248 | -45.84267 | 2024-10-26 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b9857c2-69be-3f98-bb7f-949b69f69002 | -4.5819 | -45.84633 | 2024-10-26 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d26b24d-a329-360f-8466-6248b646b97b | -4.57855 | -45.67043 | 2024-10-26 04:17:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b58388f-b80d-3165-940c-64d6e3b88aed | -4.57849 | -45.84581 | 2024-10-26 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ea6d7ab-479a-311a-abd9-018e211a1876 | -4.57798 | -45.67405 | 2024-10-26 04:17:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 113fe699-e04e-3f64-8674-df9499c9c702 | -4.21636 | -45.81554 | 2024-10-26 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 804a12c1-0ba9-3339-b1ba-d7bd5c51175c | -4.21578 | -45.81917 | 2024-10-26 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8f58760-b992-3394-b9fa-44a29036a9af | -4.21295 | -45.81501 | 2024-10-26 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38e45214-c1cd-3dd8-943e-434b187ad822 | -4.21237 | -45.81863 | 2024-10-26 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e30abceb-73a5-3a33-98ab-7c4807eaa797 | -4.08133 | -45.56681 | 2024-10-26 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 491a5370-5f35-3356-ac68-de646f7f7e90 | -4.08076 | -45.57043 | 2024-10-26 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee87f157-5fce-3412-a19d-b35f50aa7f1d | -4.07751 | -45.50338 | 2024-10-26 04:17:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57403948-bc9f-37d0-96a5-eb106cfce9a9 | -3.987 | -44.6214 | 2024-10-26 04:17:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4350109-a2d5-3f27-806b-d43f3e40f7ed | -3.60938 | -45.8125 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c68897c3-c815-32bf-9775-5802b6bcad26 | -3.6088 | -45.8162 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99edeab5-0ce0-3f4b-b094-2893c3762f9e | -3.60596 | -45.81195 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 32602a36-0094-3b57-9936-632ff837e002 | -3.60537 | -45.81565 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 42cebd3e-5dd7-3957-8e2d-9b2d58c258cb | -3.60312 | -45.8077 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f8f4421-5ad3-32d8-83e8-26e39d4209d3 | -3.60253 | -45.8114 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 34.9 |
| a9cd106d-2ead-32b7-a856-e6c4af66db44 | -3.60195 | -45.81509 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 8d74b745-e986-348e-a080-28a5c463d5af | -3.59911 | -45.81086 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a01106a0-c981-32cc-8ada-095ee77d303f | -4.38049 | -46.03297 | 2024-10-26 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5c09987-531c-31ea-b9df-8d72699d6137 | -3.99159 | -45.97701 | 2024-10-26 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 782f340f-1965-3c8d-abe5-704ed8ac9e17 | -3.74176 | -45.9426 | 2024-10-26 04:17:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 598a444f-6bc7-34df-8b70-7303e172bc6f | -3.5117 | -46.02639 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 216b2c01-7518-302c-a75d-da4208e49f44 | -4.5412 | -46.03618 | 2024-10-26 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fbb6c6a-5ede-3f61-ac78-78a78aa5bf43 | -5.75602 | -45.56165 | 2024-10-26 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46e982cc-1bb3-3c1a-b440-84873b9c9285 | -5.75545 | -45.5652 | 2024-10-26 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f7f9042-6ab8-3c22-93d2-773a45b0101d | -5.75266 | -45.56112 | 2024-10-26 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2559244-6dfa-3425-bf9a-a85161517bb2 | -5.75209 | -45.56467 | 2024-10-26 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a14edb8d-bf84-321d-8362-e8b4eb04dda7 | -5.46036 | -45.87877 | 2024-10-26 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e1e6804-764e-3ccd-aec9-2a9e919a75cd | -5.45978 | -45.88243 | 2024-10-26 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fd7db8b-540f-3602-ba89-57c8c31564a7 | -5.45521 | -45.39063 | 2024-10-26 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84c7c112-2646-3c51-ae31-88fd1ea820e2 | -5.30646 | -45.00766 | 2024-10-26 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9842cac6-683e-3d20-988e-58d005da2f3e | -5.27995 | -45.72076 | 2024-10-26 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e24e218-dd3a-3edd-9348-b407cfa0afc5 | -5.27919 | -45.72112 | 2024-10-26 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70a787e0-029e-3e89-8b0e-eb104f65d286 | -5.70679 | -46.30446 | 2024-10-26 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76bea3c4-7e53-37ac-a839-cb3efb0589f7 | -5.7062 | -46.30816 | 2024-10-26 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 937d1a2a-a6be-3c06-a263-c70930c2696f | -5.64135 | -46.40498 | 2024-10-26 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a682cdd5-bf88-3cd4-bc6f-fab927eea05a | -5.63791 | -46.40441 | 2024-10-26 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebf35d29-54fe-36c8-aef7-a28842b555e5 | -5.61125 | -46.22558 | 2024-10-26 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e91234e3-0701-374d-89e3-d3c605842732 | -5.58177 | -46.38843 | 2024-10-26 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9d6c5c6-ec78-3782-99cd-39c203cba04b | -5.53835 | -46.19873 | 2024-10-26 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f677a09-0a59-3de1-90ad-a1ff20966545 | -5.49208 | -46.35929 | 2024-10-26 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2d8b39e-4040-3249-a841-d0236a90f57d | -5.35639 | -46.24572 | 2024-10-26 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c333634c-a904-330a-920d-493527d8b9bc | -5.3558 | -46.24942 | 2024-10-26 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56b501ac-2cb1-30da-bd57-4239d1ffc552 | -5.1789 | -46.19936 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7ca47e1-e294-340e-993c-6ec64893f9a4 | -5.15825 | -46.10874 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90d93400-7940-37cb-ab07-80299103247c | -5.11889 | -46.00468 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 740b766f-2e54-3d62-a145-14036bc44c0b | -5.11548 | -46.00418 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 675de0d0-d24c-3d83-8a4b-25cf2b9ead06 | -5.11442 | -45.40237 | 2024-10-26 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5716145-66d8-3a5c-bc0b-0c999d0503e8 | -5.11308 | -45.40194 | 2024-10-26 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f66951e0-b02a-3fbd-b336-c4ea0aa42508 | -5.10972 | -45.40141 | 2024-10-26 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3caed22a-4695-3755-bf9f-35217e8dfff3 | -2.05911 | -46.5351 | 2024-10-26 04:17:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 469af92a-86e6-3d1b-a9e1-cc9c1387b970 | -2.05553 | -46.53455 | 2024-10-26 04:17:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb93bd12-cba5-3d77-9f87-b4400a372873 | -2.03844 | -46.97123 | 2024-10-26 04:17:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 14c0d5c4-6690-3576-b979-0730735ca3b6 | -2.03477 | -46.97068 | 2024-10-26 04:17:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ec0f3717-bb40-39ab-9a60-5c9cfbb42103 | -2.01103 | -46.54898 | 2024-10-26 04:17:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a5e73e2-1ee2-33d0-b551-2b0db18b9613 | -2.00924 | -46.54813 | 2024-10-26 04:17:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0bdb29e9-69b8-355e-96d4-70172f43388f | -2.00744 | -46.54842 | 2024-10-26 04:17:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 05e47c27-8bce-3501-9a7d-66b15861e9ae | -1.96157 | -46.62934 | 2024-10-26 04:17:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a11cc6b-9d78-37f9-adc2-dd8612727b96 | -1.95797 | -46.62876 | 2024-10-26 04:17:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 293dbbb1-ddb1-315a-a1b7-00b3a1d579f1 | -1.95732 | -46.63288 | 2024-10-26 04:17:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c682520-e45f-35c7-acaf-55a70294e626 | -2.95694 | -47.36292 | 2024-10-26 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea0a6072-e0aa-3e5c-b624-474caf274256 | -2.77558 | -45.97956 | 2024-10-26 04:17:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a54fffb-a176-340b-bda2-e7a0deb34c9c | -2.77498 | -45.98334 | 2024-10-26 04:17:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 742a0c4c-773b-36b4-84d2-d8666ed43b14 | -2.7237 | -46.69158 | 2024-10-26 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb78a9b7-d336-3a88-96a4-8249d51ffc2c | -2.61122 | -46.124 | 2024-10-26 04:17:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea9bba81-3505-3d31-8e95-030400b6a5a6 | -2.61062 | -46.12785 | 2024-10-26 04:17:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6c005ad-f8a2-34e5-bb7b-d4b7a4392f77 | -2.60941 | -46.13555 | 2024-10-26 04:17:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4011df6e-62dd-30f1-b75b-a128ba9ac956 | -2.5878 | -46.1361 | 2024-10-26 04:17:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e125f14-4129-3861-bcfe-57ced7f6fc69 | -2.57069 | -47.25281 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99fb9b6c-d680-3ba6-a12d-923023200e4d | -2.5703 | -46.13334 | 2024-10-26 04:17:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9dda417-d3bc-3a6e-afc8-0e2033168ae2 | -2.56999 | -47.25715 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecb58cb1-e3ef-38e5-9245-0b3fbc6862ad | -2.48572 | -47.27242 | 2024-10-26 04:17:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b406db2-5585-3c51-bd6f-a165c096f232 | -2.37789 | -46.1638 | 2024-10-26 04:17:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5323396-55ae-3515-b950-a41d8f49ca8d | -2.36743 | -46.98749 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e7ecf64-60f1-3684-80b6-d366a0c8c10b | -2.3673 | -46.98662 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dfa3d2d-2095-3ba3-ad17-6b22c5759be7 | -2.32066 | -46.65177 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c45b4e84-9f33-3d49-a7bd-de2ca0acce4d | -2.32064 | -46.64479 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cfb2b64-d0fa-344d-8a9b-a8fef4869b74 | -2.32 | -46.65586 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85cdc732-75e5-37cd-b81f-505e903c40e1 | -2.32 | -46.64889 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c51678e-597f-31b8-bc4f-81708bcfb396 | -2.31936 | -46.65299 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e69d8097-6b29-3f55-8bed-49128d6681a7 | -2.3185 | -46.4949 | 2024-10-26 04:17:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 141e1941-6221-37a6-8653-5634ac687619 | -2.31839 | -46.64302 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94284214-4147-3d6e-a56f-49e02ba6e170 | -2.31773 | -46.64711 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08b391a7-c0f2-37bd-b3d8-6cc984ff3b8b | -2.31769 | -46.64013 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccaf148d-8e5f-3292-8156-34e1152f5299 | -2.31705 | -46.64422 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d87c37f9-7899-3d29-a3a6-2ccd73cdfaa2 | -2.31678 | -46.63025 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9214238-e024-3639-8334-b1b87059296e | -2.31641 | -46.64832 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README40.md)
