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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c3a29b7-d8ed-3a49-be35-56e618c2a7a5 | -11.7569 | -43.31483 | 2025-10-11 05:01:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2fb3b1a8-4279-31fd-82b0-edbd6faaac06 | -13.84551 | -45.81141 | 2025-10-11 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b48e49a-778d-33af-9ec1-6ef7b6f83a51 | -10.53532 | -47.32059 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 045e28f0-0049-340b-9f47-ed237293342f | -11.99169 | -49.8556 | 2025-10-11 05:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c4bc6a8-2bd1-3b13-adea-79f06ef652ea | -13.26812 | -48.01643 | 2025-10-11 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e8fa33f-27df-3e42-a927-af1ba33cf872 | -12.9042 | -47.05663 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eed2c58f-2a50-3315-9b36-147e5f5d8591 | -12.99286 | -45.22591 | 2025-10-11 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ab556d0-6e51-33db-b317-4874944dc601 | -9.40254 | -66.76197 | 2025-10-11 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e5156df-a23b-31d2-a86c-435c3a079098 | -8.20535 | -43.34073 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 63922e2d-5788-3883-abaf-c63291e6d5f5 | -12.89937 | -47.0534 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ddb7ec2c-dc25-3aa2-8e2f-32b55b0acb50 | -10.52464 | -47.34567 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 08a2ab9a-b5b7-319e-88e4-dc0bddfc6a56 | -8.17862 | -43.31697 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a3929bb3-a1ca-3a13-8df3-82586ed1cfd3 | -6.44019 | -45.82455 | 2025-10-11 05:01:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e923aca3-1472-329b-89e7-71ddd5761488 | -13.36345 | -47.62626 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60144cd4-f6f4-3bc4-9c9f-1ad4bda3f8a1 | -11.76276 | -43.32104 | 2025-10-11 05:01:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac992340-276d-3dea-b205-a3142bbfcff9 | -7.74342 | -44.69919 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 155ba263-cf07-3974-98fc-6fcdfa4d2ddd | -7.85918 | -44.49734 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e228bc33-8abc-3754-8f42-82b94835e3ba | -13.22423 | -42.34225 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c5de86e6-d69c-324f-81f0-d2047fe7d28b | -13.84164 | -45.79523 | 2025-10-11 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f931620-fd56-3b38-8bc8-23b9e0d6a24b | -6.92155 | -43.5875 | 2025-10-11 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dc9356bf-ef3c-31b4-a1af-762b785a764e | -7.53781 | -44.60781 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5930401-3679-3ce6-9a5f-2de88de8e7c2 | -6.91619 | -43.58213 | 2025-10-11 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 26b1d1aa-7da9-3745-be53-4be2be754ca0 | -13.35203 | -47.63604 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fd1691ec-3f9c-34ab-a6e0-3a8bd80c5331 | -11.74351 | -46.39822 | 2025-10-11 05:01:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e05f50e8-bd9a-3725-9058-ff51224d111f | -10.19352 | -44.61406 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e53b5b65-fdc5-3052-926c-a3d958d8983b | -8.01114 | -44.46375 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0537482c-0a3d-3a92-9a29-9aa57a75af35 | -13.22373 | -42.33765 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 6da39e86-237f-37d0-9411-cbb2363c4de4 | -8.15767 | -43.32009 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7b8d4dc6-48dc-3c9d-a1c2-48394a5255f9 | -7.40963 | -45.91751 | 2025-10-11 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7af0565-9776-3d0b-ab72-b523c1b190da | -11.44793 | -43.47648 | 2025-10-11 05:01:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d95d17c8-e9de-3bd3-95b1-facd58119e3e | -13.20261 | -42.34637 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e6c7cf99-6b3e-3b5a-a6b8-b2529dc2aab5 | -10.06391 | -67.55313 | 2025-10-11 05:01:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 23.2 |
| e4ad80b6-f78e-3c00-8c4f-5c4bb8b78dcf | -12.23647 | -51.1287 | 2025-10-11 05:01:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96d6c11f-23bc-3551-bd9d-125a34037682 | -10.20094 | -44.6025 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bce09ef5-5612-338c-aca5-e3638b1cccc4 | -7.12257 | -45.91739 | 2025-10-11 05:01:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6c10515-bf7f-38dc-9f85-9d7c6257e1eb | -11.7378 | -46.40072 | 2025-10-11 05:01:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7005aa12-9b50-353b-a439-f07eadc94ab7 | -12.71597 | -44.93842 | 2025-10-11 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74030ce2-b643-3f46-b0e6-9ba55ad239a9 | -9.50452 | -47.87635 | 2025-10-11 05:01:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9386518d-c21b-36db-a70a-b3b0e7a73eb6 | -9.40879 | -66.76334 | 2025-10-11 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94037308-e602-384d-abbb-946cfe4c8cba | -6.43506 | -45.82393 | 2025-10-11 05:01:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cfee4ae-45e1-3b34-b79f-26ff04e1f60b | -13.84596 | -45.80759 | 2025-10-11 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df74400e-3792-3935-a660-35044f2669f8 | -8.16558 | -43.32036 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 676771ff-f29f-36ae-95a4-3ca1d6853326 | -8.20597 | -43.33597 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9780b9ca-30ab-33cd-8516-9a694ab20c63 | -8.01209 | -44.46172 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9444d035-63a6-3da8-b5da-3737b5da75b1 | -7.67914 | -43.99007 | 2025-10-11 05:01:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bc9b574-5bdc-361b-9616-55523ac06a7c | -12.24 | -51.1309 | 2025-10-11 05:01:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aefbe1ed-6d34-352b-8acb-5ff754d19887 | -13.50937 | -48.12662 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b8e8b03c-fa1a-3743-9729-ac064c072c47 | -7.5272 | -44.29762 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4934a021-4c21-3a6e-b5c5-728e479a8556 | -10.51565 | -47.35692 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e14a003c-99d0-3f8d-a78d-09a26e6239c8 | -13.21541 | -42.35003 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 33.1 |
| bd1238f5-4bb4-35db-afeb-583d64acb9d1 | -10.06502 | -67.54767 | 2025-10-11 05:01:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 18.2 |
| ff352674-fb45-3f95-abeb-969dbef30ff6 | -12.90155 | -47.0364 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd0849c6-6d48-335b-93d9-08880b4380ab | -11.75629 | -43.32024 | 2025-10-11 05:01:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 78ea4f36-6824-301d-8dfd-78c436ae9ee4 | -10.57038 | -44.50642 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a18e5ca0-84d2-3606-afd7-4f138e184b94 | -11.44927 | -43.48284 | 2025-10-11 05:01:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e24cfdc-5780-3411-8139-677fd93c0c3c | -11.76302 | -45.04478 | 2025-10-11 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53f81cf2-ba15-30a5-bb79-262baacf3eac | -6.73678 | -42.87196 | 2025-10-11 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f826923f-fc04-37cd-b285-5c82dda06cc2 | -10.15364 | -44.55227 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3de055ab-a86c-339e-a8e6-25c9968bae70 | -8.01785 | -44.46233 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5acdcc38-5f32-3854-b626-5f37482059d9 | -12.98654 | -45.22929 | 2025-10-11 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0eee25e1-6bb8-3459-9118-b27db1d4046f | -13.29464 | -47.12608 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d698526c-3679-31a4-8ed2-fbd5863adb51 | -10.06636 | -67.54803 | 2025-10-11 05:01:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4ba514fe-0194-30d0-9003-8094263f0cb0 | -10.15317 | -44.55602 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cfd0ee05-849d-3992-a3a0-b26b3513a114 | -10.51217 | -47.34531 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fa1ed1f-19c2-3991-94c6-2cd229702427 | -8.00685 | -44.45238 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18b020bf-b62f-3bb6-b146-95a77e025cc8 | -7.33766 | -43.867 | 2025-10-11 05:01:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b5a491f-fc39-3705-83cf-c5aa53d703c8 | -10.37689 | -57.64284 | 2025-10-11 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64bcd0b9-8a07-3168-ab2c-c7dbd52ea6ab | -13.31259 | -47.97883 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 857c58bb-8bbc-3894-ad45-2e0fbe461474 | -11.91214 | -44.18313 | 2025-10-11 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a142ede3-6575-3047-add5-0ed1c4bb0c23 | -13.32797 | -48.48956 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39bb4d1b-1852-3a07-ae4e-c2bf77742306 | -9.40971 | -66.75846 | 2025-10-11 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 319dbcdb-bb4a-31bf-adf3-fcd7cf730d71 | -7.53349 | -44.29441 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbd9d332-826a-36e3-a38d-341f982afb23 | -12.99869 | -45.22664 | 2025-10-11 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08f0dc1e-6f29-359b-b803-2af916ab01e0 | -6.80684 | -44.6321 | 2025-10-11 05:01:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6dfc944d-3f76-314f-a712-598f2802adb4 | -11.7431 | -46.40152 | 2025-10-11 05:01:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02474520-b2e8-3539-8899-f7bc0f0b8ed2 | -7.98645 | -44.47362 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 612d949e-fb1d-37f3-bc89-42f6eff2903b | -13.25894 | -48.01088 | 2025-10-11 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| afb28da9-d446-3970-a835-38b1968b9fd6 | -13.20913 | -42.34247 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| d7854570-2621-35bf-936c-043ef2c75e2f | -13.30135 | -47.98898 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e481c822-eaaa-36fb-90be-ba8406c6a694 | -7.38038 | -45.17842 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30ed7963-0139-317b-8074-1bb4ec3f04a9 | -14.015 | -47.06194 | 2025-10-11 05:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07b9b9ec-ce3a-3176-adf5-69360d613ecd | -14.65386 | -56.21305 | 2025-10-11 05:04:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c692516-9783-360b-bbf5-e9fb51da0503 | -15.70257 | -48.39927 | 2025-10-11 05:04:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c2ed101-964b-3aaa-8c99-5be4dbf6ab4b | -17.95558 | -57.61684 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 171be57e-00bd-32a3-853c-3c6d511650b9 | -13.66484 | -48.74421 | 2025-10-11 05:04:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 122ed800-584e-3597-94c9-8d1526aadaf0 | -17.81921 | -57.61904 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6e3f37c8-a3f9-3fab-a5b1-56c0a61b2043 | -15.17922 | -56.7419 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b59d52da-4d96-3ddd-8d28-e2a3ffee9665 | -15.19406 | -56.79215 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 162837dd-2d68-3c06-a603-0b0bdaafac7e | -14.44274 | -50.34731 | 2025-10-11 05:04:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d3f0999-9bd4-35e0-99c0-7274df2d8eb3 | -14.65443 | -56.20948 | 2025-10-11 05:04:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 809eec6e-61fd-3aad-a3cf-0bfcc2ee5bbf | -12.09026 | -64.23864 | 2025-10-11 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5273a09-06a4-36a8-a35a-e246413c3437 | -14.95081 | -46.74827 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 211cae61-2ed8-3c76-86e0-08734e5e3e6d | -15.19072 | -56.79161 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f05d69f9-c0c0-31b1-bfee-112ec5bae89a | -17.94162 | -57.61814 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6d40e3d0-15b5-3c28-b06f-3d04740bad73 | -15.67825 | -56.19482 | 2025-10-11 05:04:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94b0d279-244b-3fa4-8020-67ece6b531db | -18.06837 | -57.52316 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f19e50f1-873f-32f3-9c52-f3967d64ab1d | -15.16208 | -56.82772 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6aaf0f2-d298-38a8-a5f4-cd4706f601d8 | -15.18752 | -56.76889 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5d6de38-8ab8-3dc6-b080-72867eae4237 | -15.15656 | -56.81939 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc261d9d-2a4b-32db-a481-dc38e4c9e4b5 | -17.8999 | -57.66353 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README38.md)
