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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbaf9118-18cb-3a02-8560-018f3ca43ca7 | -4.25623 | -53.51685 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9c6d4a0f-9544-3123-adc7-c11ae86fe643 | -11.66879 | -46.60634 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22867bc5-ca95-3119-b0d7-5ed019f0526e | -11.53296 | -50.41459 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9086f56f-f2bf-3487-8398-b05a02084e95 | -12.54631 | -44.68953 | 2025-09-12 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8b934a1-ee49-3b9b-a3e2-54d027b51e0a | -6.90457 | -44.54961 | 2025-09-12 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1c743d9-8fc4-3506-b086-146f9336c943 | -8.07781 | -42.56601 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd9894fe-5404-3aeb-84b7-63914f841b10 | -11.69487 | -46.5923 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec660307-0d1b-3735-8f65-dd06650be386 | -7.18025 | -44.87207 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 597a63cc-5565-34f7-9087-29a96ca2e008 | -7.22712 | -55.05813 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4a18b1b-8282-3962-a574-bda3f87ea846 | -8.3687 | -44.84111 | 2025-09-12 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f93d1ee-bee1-37fc-908f-90939f213bfa | -9.89436 | -51.89196 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bf23e40-c49e-33aa-9a7f-eec89128bf95 | -12.54397 | -44.69057 | 2025-09-12 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e0218265-1a10-3a10-8fcf-e3b2c47feb37 | -10.3884 | -50.49934 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8409ed4-8d4e-38f9-a3c6-2a666fca41b8 | -8.93281 | -51.07159 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89cd2af6-8e59-366e-96fa-61bfb4dab6c8 | -11.10083 | -48.39965 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e3dfea6-b083-3f11-bbb6-c5a664866248 | -9.79112 | -51.07341 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e917d23a-177a-3562-a3c4-9a996ec47615 | -9.06162 | -47.03956 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 46b460fd-f7c7-3d88-88d6-77a84e7bc8f7 | -9.78075 | -47.85574 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65e70eee-c2c0-3298-a0c8-d19b183852b1 | -8.89421 | -49.9315 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 52bc5dad-fac3-39f1-a6aa-07e7814239ba | -10.40432 | -48.58914 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef9669d2-04aa-3223-977c-e70780763b6c | -6.65614 | -44.14101 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bcf5dba-45bd-3c13-9d94-be72c0405a85 | -9.89531 | -51.88651 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de0970ad-af5e-3889-b069-1011624ae4aa | -9.03017 | -47.10954 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d0ccd87d-d4b9-3349-8ddc-47074eac6842 | -8.48066 | -47.27484 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d41cfbb0-713f-3946-82a7-58950aa9ea6b | -5.49824 | -42.67662 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5b690cd4-5a7f-3dc5-9830-46914546364c | -6.05869 | -49.85274 | 2025-09-12 04:25:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b35eefc-e62b-3ea7-856c-f4715b3b58ec | -5.8625 | -48.15699 | 2025-09-12 04:25:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8377d4a8-6323-3325-b51c-d31fb2134d1d | -10.70807 | -48.64188 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fafbbc6-5f2d-3981-b322-155d15c99307 | -7.15377 | -44.34181 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c6c433c-d436-39ac-be8b-801bce58dfbe | -7.25154 | -44.47934 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0a94188-0315-3da3-b7bf-ee888091a16e | -10.89755 | -47.24118 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47302879-4ecd-3941-a2ad-8be14e9ad837 | -11.093 | -48.40574 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0203e08f-e9bb-3a71-8d91-27a2afe2f2ef | -11.48324 | -49.26897 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b270ee8d-dc3d-379a-87d9-729b44d5f123 | -11.53474 | -50.59911 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fd278ac0-1b54-384e-8f09-d979fb21582e | -9.03157 | -45.79653 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac11386d-6a1c-35bd-b3e1-6a2e8b7c2903 | -6.45069 | -41.76518 | 2025-09-12 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ec672427-cfe2-3fb4-852c-c4894a2fbb75 | -11.5218 | -50.60983 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e72ecf46-b217-3f0a-a467-743ea19fc947 | -11.69651 | -46.55966 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c05581e2-4e97-3965-9da0-b8397ddfa785 | -10.34994 | -50.54996 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 656552d6-718e-3d38-8efd-757d0f55280d | -5.4976 | -42.6809 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ec0d39cc-96a0-3b7f-95eb-486aa9655d5d | -11.69263 | -46.56269 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c9bf993-0072-3965-bf51-f453a51349be | -7.32684 | -44.3755 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 01d9ee16-4aa4-39a7-9587-a07332ef3944 | -10.85748 | -44.78497 | 2025-09-12 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05e76d7f-544d-3595-93e8-d2832e73bb2e | -9.03624 | -47.07124 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f7736356-bbbd-3da1-a266-c07a113968b7 | -11.13881 | -45.24227 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df98d9ef-71c3-3813-82a4-30822c3afc15 | -11.6732 | -46.57784 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f8a835b-187c-3703-ace3-cb47697be3bd | -12.13075 | -44.84464 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adfa6b31-5306-3b1f-9d57-3e7b394218cb | -11.52538 | -50.58884 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 57e29ee4-51a7-327b-b20d-3569475b1c47 | -5.64612 | -51.86787 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0e5f368-61fb-34fb-81cd-236106de4884 | -11.08331 | -48.44477 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cacc79b4-907a-3cd0-bcba-ac57761f6fd0 | -9.04232 | -47.05434 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 202b1506-9741-3216-9e31-83672038fcf8 | -11.70289 | -48.28631 | 2025-09-12 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a02e793f-23db-3a34-aa3a-0b61084a7231 | -4.48083 | -48.11547 | 2025-09-12 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2f10eb86-e3f9-3817-8883-1de8ec47ee02 | -6.80898 | -45.64198 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95e99e08-79fe-3afb-aac6-06fb76e3be7d | -7.71761 | -50.35748 | 2025-09-12 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 184d1d8c-99db-3c15-aa98-4e8a7619ee6f | -11.41053 | -45.59501 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b81bd88-1eb4-3b1d-8f8d-7e23ab874a87 | -6.66387 | -44.09114 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd3495da-2bc3-321f-b4fe-d2662710a898 | -11.68819 | -46.56929 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e92510e2-25ba-3b96-8bb3-a6be59974fca | -10.35839 | -46.38931 | 2025-09-12 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfff39fd-faf2-367d-975b-f73e95438aca | -7.53032 | -44.66989 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 812c458a-63c7-30e1-8cfd-28119d892287 | -11.97459 | -46.64756 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 13bcd5d8-7e49-3790-8477-0c56b75e2542 | -12.12661 | -44.8728 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a1ec8bb-9745-328e-a5ff-40ea118eddfd | -9.07424 | -46.95961 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfecc472-0c99-3c35-9d21-707dcc4b4b43 | -11.66323 | -46.59814 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84270454-9819-3c33-afaa-75a661976016 | -11.1578 | -45.3214 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67e3c7a4-ffd5-3b80-af12-4f9540bee4ac | -6.48067 | -45.15818 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a700e552-27db-31b8-86a1-b800287d25e4 | -7.84955 | -46.06562 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d2a1fb9-37e8-3591-a74b-5ebe6cb546bf | -11.69209 | -46.58819 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14c82d5a-37c4-3e0a-bad0-81bb835000a3 | -10.38405 | -50.50298 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0e4bd11-4aee-39fb-b395-161542fe7435 | -6.68513 | -44.15266 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a3da70b-caf3-34a9-940f-248c356ca555 | -10.43193 | -50.61998 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b928fb16-a103-3636-a7c8-9efda5c77bbd | -5.21727 | -49.42906 | 2025-09-12 04:25:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50bfa646-2705-38a3-8ddf-20c2849483c5 | -11.4396 | -43.56326 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8dd3b26-979d-378e-a739-ae569a3debef | -9.7513 | -45.39304 | 2025-09-12 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c17face0-6b29-38cd-8062-0f866fd1b9f6 | -8.76576 | -48.7238 | 2025-09-12 04:25:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7af14876-f45f-3c2b-9364-2aa87f8658dc | -6.8256 | -45.64455 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e07cf8c5-1465-3bb2-883f-ec57f5f64d32 | -11.93652 | -44.30635 | 2025-09-12 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86a94ed6-a4fa-3b06-9829-d349e62ad0e8 | -11.00694 | -51.34488 | 2025-09-12 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 907951e6-59d1-3ba2-9ae6-c3159dbb5e38 | -6.81335 | -52.80251 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93cc7c2a-ef3e-3c75-b4ef-ca78368ce80d | -9.83595 | -47.76698 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f79bada-68bb-3b65-96f8-1c471482862f | -9.73557 | -45.42814 | 2025-09-12 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d51d874-04ae-3c06-86a1-5833d1ca53a7 | -6.43863 | -44.3926 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 454d2d50-774e-39e9-896a-5109cd88b71b | -8.18584 | -46.1085 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25a3f7fc-f4af-3a15-9060-72409e424ce9 | -8.42838 | -47.26294 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff4d3e23-c9ab-3631-b660-5c7b44b6d1d0 | -11.67044 | -46.59568 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60f867e0-5f0d-303e-b2af-1aa93bf27114 | -5.9451 | -45.954 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f23bb39-8959-35de-9e70-ea42e4ca61e2 | -11.68765 | -46.59481 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95345c93-3e85-32e9-beca-43589ad40fe3 | -8.18252 | -46.10797 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5e9bb14-ac8d-3163-8e32-8172cab61cb4 | -8.88101 | -49.935 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d0fb0537-0f7e-3ae1-8a54-868de0b62d0b | -5.40507 | -45.93271 | 2025-09-12 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bad8b06-6721-3d23-a0b1-c4527218dad8 | -6.67589 | -44.14361 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75950278-dc8d-319c-a3cf-7ab3c4a1f949 | -11.68265 | -46.58302 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f130bacc-ebcd-345a-9549-37e2183e6a87 | -7.15259 | -44.34944 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f4aa517-84d3-34e0-845a-d0f08e010db6 | -10.35502 | -50.51995 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3e66862-80d7-3f69-bb30-c412d227a9cc | -9.0632 | -46.57581 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6786750f-6792-369c-a88f-b8ebd96f859c | -9.10741 | -47.11478 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ee11182-f0e8-3db7-91f4-0ac0b186a9aa | -10.11908 | -47.90727 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72021252-ae2d-30b0-8a0e-88a062208a4d | -7.72713 | -44.86902 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e269d18c-3ae6-3a06-81d8-6a0bce876256 | -11.20173 | -48.40511 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fb87695-76ae-39fb-9c69-9e0b18101580 | -9.06107 | -47.04304 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README76.md)
