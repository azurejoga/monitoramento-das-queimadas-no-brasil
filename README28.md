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
| 7d55afef-fe8f-396e-a2a5-5040ae08c98f | -6.34224 | -54.91755 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bfb5c355-a919-3104-a216-30257ef6df63 | -8.09853 | -51.65919 | 2026-08-19 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5956d23d-0655-38a5-9647-1ea32c6fbc19 | -8.35861 | -45.97998 | 2026-08-19 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6bde6ef9-4dc2-3f5c-80c5-c50b9af78c7d | -6.34861 | -54.91911 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c149344-63a9-3c54-a6a3-aea18f2fe99e | -6.26899 | -45.92724 | 2026-08-19 04:19:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c35ce4ac-fd68-3094-9ced-418ddf260287 | -8.57772 | -54.73511 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 64b37e2c-332d-39bf-81db-55e1514e502f | -9.72804 | -46.79068 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a4e1f994-e40a-394c-8de7-bb92bca13a1d | -8.58058 | -54.74141 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aa4723dc-dd48-3e24-a181-e95680047ceb | -11.19937 | -54.02017 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 425093b6-6598-3e29-810e-3f19ce292e95 | -12.23914 | -43.15674 | 2026-08-19 04:19:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9b3bff9c-4c80-3399-8315-49f0664ac08e | -9.74772 | -43.30802 | 2026-08-19 04:19:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 32c182db-d10d-33cc-8729-c977d06079a9 | -8.08261 | -44.35727 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72df84a6-a6a8-35a4-a82a-d5ac2f83ee45 | -7.0187 | -45.89873 | 2026-08-19 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 645d91c5-bbd5-31ca-86b4-f2fa1b71eb25 | -8.53178 | -54.72545 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 617d9ae1-a530-38fc-b865-36813e3eb8b9 | -8.57838 | -54.75245 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 668c589a-a309-3ab5-a26c-7cd00024e221 | -7.55064 | -55.5705 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f75f728-438b-3863-af05-5d9c6f71c72c | -8.56684 | -54.72072 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 266d16bf-07c3-35ba-a683-2b1619af10bb | -11.32008 | -45.20885 | 2026-08-19 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b6aeac0-02dd-36a6-b546-ccc3be8fa487 | -8.21853 | -55.02168 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2128a23-059a-3bec-afd7-1826e10b419c | -7.12089 | -47.54716 | 2026-08-19 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 011a76b0-f3ed-31da-a990-7b5c4f156c51 | -7.17675 | -43.10558 | 2026-08-19 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e0c3273-2b00-3322-85df-e68e563f2581 | -11.22423 | -55.07653 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ed05f39a-1880-3d2e-8be7-e3dbe7a49518 | -6.44751 | -52.74267 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6e1c969-7590-3356-aa01-19293ed26bfd | -6.63923 | -45.50841 | 2026-08-19 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c45d0c6-0c57-3dcf-97dc-032923232ebe | -6.01425 | -50.1991 | 2026-08-19 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fa4015f-5f0e-327c-adbe-8ff92aab5d0b | -8.5838 | -54.75963 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 88831898-048b-3963-ab61-e6373a90eb32 | -6.34414 | -54.90512 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab654efb-8f08-3b6a-86c9-64f2d6381a8d | -12.70132 | -48.51829 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c87bfda-f43b-33e7-b116-ed8442e8ec4d | -8.58328 | -54.74171 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4b808e08-1121-33fd-bc14-ad6cbeb9f0ce | -0.9806 | -47.50243 | 2026-08-19 04:19:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faa43c12-3ca9-352c-92f2-3918c5103c7a | -11.23375 | -55.06019 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa7b1415-8af3-3e03-9321-bff9bb19ba6d | -9.72756 | -46.78758 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4fdc5cb5-da84-3c9b-984c-a08577b5fe15 | -6.01867 | -50.1987 | 2026-08-19 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f69a06e9-ddd8-3c23-aa70-6e326094a4f5 | -12.04974 | -46.45974 | 2026-08-19 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72894203-af4c-3d34-8f23-82ee88f46143 | -6.01923 | -50.19543 | 2026-08-19 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0795e297-b261-3570-b274-9b0a8b4dcc96 | -9.73085 | -46.83917 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e896836-1b5e-3485-9ede-6e567feefde1 | -8.04731 | -50.10687 | 2026-08-19 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6aaf4ac3-ddb3-3771-9789-f94b33a6ed33 | -7.95313 | -44.6417 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7554dad8-640f-3430-8b30-9e1d30faff82 | -8.58932 | -54.73186 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a006819b-9a61-39b3-a0f9-530620517890 | -11.32292 | -45.21336 | 2026-08-19 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ddcb8fd-1991-32b5-a873-27366da87353 | -11.19545 | -54.82102 | 2026-08-19 04:19:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fdc957f-b2b5-3ac5-ba31-15764186d626 | -7.19053 | -43.45306 | 2026-08-19 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 39f841ed-a54c-3cfa-b0e1-65da9ade4fae | -7.19334 | -43.45728 | 2026-08-19 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1c97ab06-17b3-3e25-9f5a-20bf6f4b3b04 | -8.50033 | -54.86765 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3d2bba0-cd52-311a-9a72-a7f70bee8206 | -8.5383 | -54.76215 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| be182d71-a976-3153-b6ab-c609ad035ac5 | -11.21416 | -54.00911 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31f414a3-ee95-38e7-98c8-123c91e8dc6b | -8.57346 | -54.75723 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b8320c10-967d-3aea-bc5b-4d6574556c96 | -8.56351 | -54.77339 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3273670c-0e72-398e-88aa-eec5e15bc1bc | -14.02355 | -42.60604 | 2026-08-19 04:19:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b449c6ec-8ac6-372a-897e-aff1b232b7c8 | -9.46273 | -51.62978 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61852479-bafe-390e-95bb-c7c35e3324cc | -11.12745 | -47.28029 | 2026-08-19 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 227b6da2-fe0f-3bb1-99ee-1308a83cd7b2 | -9.63701 | -48.20608 | 2026-08-19 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8761290f-d25a-34ad-9743-be0d24a7d298 | -8.58924 | -54.76669 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46870cd1-5cf0-3ff4-831a-ab418337c024 | -12.76091 | -48.44587 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a07004de-4ebd-356f-9c2a-b18fa043d358 | -8.58165 | -54.73605 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a4b16ff-8ced-3b7d-b119-88f709ed93ca | -7.01473 | -47.97347 | 2026-08-19 04:19:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 888277be-37f2-3c85-8874-6a2dff6b98f4 | -8.5712 | -54.76898 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3242753f-237f-3c5f-9fa0-699a5b8a230a | -11.08848 | -49.91705 | 2026-08-19 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 406ce8c8-68a1-3cc4-ac22-669535af5b75 | -6.64073 | -45.49941 | 2026-08-19 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88a6b70b-2e0a-3ead-9354-fa51adc927db | -11.22867 | -55.05493 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6a6129a-3db9-3fe2-85c0-0c25c81c2911 | -11.7192 | -54.63094 | 2026-08-19 04:19:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41b2b47b-2c31-3412-a7fe-98603fc603df | -6.40479 | -46.63428 | 2026-08-19 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04da194b-dc9c-3d0e-a7b2-afea698296bd | -12.2397 | -43.15322 | 2026-08-19 04:19:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a734d536-4827-35ba-9b36-8556b258a4e6 | -12.24465 | -43.16489 | 2026-08-19 04:19:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3050880b-22c9-334a-a5b9-92cafda60622 | -8.56012 | -47.41253 | 2026-08-19 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46ef2f8e-d594-3375-adee-d017a4f13cd2 | -8.54484 | -54.76374 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9281c982-bcaf-3aa1-9ecd-d0f3e60c3305 | -11.23864 | -46.15147 | 2026-08-19 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c292e1a9-b37f-3994-81a9-9faa0e8f02e8 | -6.38923 | -51.74899 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 064f4d8e-2ac9-35a8-8e11-1b9a3699ef03 | -11.71442 | -54.63305 | 2026-08-19 04:19:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba6e2696-acd3-38f4-a2a6-ccf8c959b53c | -11.2201 | -55.0641 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce7a4745-f231-3237-858b-c05f193110c0 | -8.50596 | -54.85752 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b83b32e-7668-3fa1-bd9d-2ecb214f764d | -7.28477 | -44.07264 | 2026-08-19 04:19:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3c99cae-cb5e-3a08-953e-f116abb6a5b2 | -8.36655 | -46.34861 | 2026-08-19 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d93b1122-b46a-3a47-a57c-eb7ff393fad3 | -7.94256 | -44.63988 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1dbd797b-5067-36ae-ad85-64b1ed995861 | -11.31527 | -45.21609 | 2026-08-19 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4b6389ac-ed1e-38dd-8d77-c2fd60fc2198 | -8.58265 | -54.76537 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9f8689c3-ee4b-31a9-91df-a35cf830e152 | -8.57331 | -54.68723 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2638272-8f49-33ec-aca6-3ef6f2a8c399 | -5.91795 | -49.2603 | 2026-08-19 04:19:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d70313ab-18b9-3b5b-8732-550dea4672d9 | -8.58002 | -54.75872 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 11f03440-960d-317e-a223-8321536320cd | -8.0836 | -44.35643 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d3edb94-4b87-38e6-b36c-481b6d552a48 | -6.35226 | -54.89991 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7faa5bf-d3de-36b3-a75c-57aaca38c4de | -9.39651 | -48.24312 | 2026-08-19 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44374628-c3fc-3c9d-b793-5d8824fee3a7 | -8.5412 | -54.7591 | 2026-08-19 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 91644687-1f94-366a-b1fc-236b5d6f1b56 | -9.4061 | -60.5518 | 2026-08-19 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 8ef7f684-bb2e-3be8-b568-94a654cb8130 | -5.4503 | -48.4201 | 2026-08-19 04:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 15277f69-155e-35a0-af8d-789033bab69a | -9.3875 | -60.5528 | 2026-08-19 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 2d701120-691f-357f-9fb8-25bc4ae2e36e | -5.9011 | -43.6279 | 2026-08-19 04:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 1e639962-693b-38b5-823c-f9a7c963cda8 | -5.4317 | -48.4212 | 2026-08-19 04:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 55446be6-778a-36a0-931d-aa3806d7eaec | -8.5785 | -54.7566 | 2026-08-19 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d78d0212-7960-3200-bfcd-ca1e342f94f4 | -5.92 | -43.6032 | 2026-08-19 04:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| d21a8a3f-634f-3574-84a8-be930297bf1d | -5.4319 | -48.3996 | 2026-08-19 04:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| b9b6a188-c669-363f-a24c-433dbada56cd | -8.5787 | -54.7364 | 2026-08-19 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 32df7f1c-1d98-36fd-ae10-901a25241053 | -6.0178 | -57.8631 | 2026-08-19 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 1ad46f9e-0c7d-3cb0-98af-64dcb953441d | -8.5413 | -54.7389 | 2026-08-19 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b5458a81-2a7a-3858-bde5-bba7746fa40e | -6.0912 | -57.9187 | 2026-08-19 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| efe6995c-7c71-35be-b8a5-c23f3e1429d9 | -9.406 | -60.5711 | 2026-08-19 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| b69ae025-ada9-39ce-b54f-9a9c0ca5bbe3 | -5.9198 | -43.6264 | 2026-08-19 04:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 3989a99d-e35b-34aa-8de4-431dc226f758 | -8.56 | -54.7377 | 2026-08-19 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0158a115-66d0-3787-b5ce-677007f4928b | -5.9994 | -57.8639 | 2026-08-19 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 257952f1-a8e3-38b7-a836-93d4bc1e4bf0 | -9.4256 | -60.4353 | 2026-08-19 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.0 |


[Clique aqui para ver as próximas entradas](README29.md)
