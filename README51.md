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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d24f8896-d631-369a-9b15-2043247174f7 | -13.20693 | -47.28375 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c716bd14-f64f-3819-83fd-e085a7b51703 | -10.71862 | -46.50492 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| bb92d4ba-ddc6-3639-8d4a-681be74d6a4f | -10.71432 | -44.759 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d00b9f46-7dc8-321b-b191-51b2cfd9fb32 | -11.72108 | -47.46161 | 2025-09-16 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 74f7c25e-7c51-34c3-8596-3ea8500d7240 | -8.20405 | -45.55148 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04b62587-31ff-30a7-b390-b1e565ae357d | -7.50094 | -49.47533 | 2025-09-16 04:29:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 377238fd-b211-3413-b316-c5b820c6b8ba | -7.57286 | -49.85152 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ef28bc6-7a77-3e0e-9bb8-281600937c9c | -8.59689 | -46.41195 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef4fe479-35e3-3e75-bc44-bfd51c166c72 | -12.11324 | -47.53278 | 2025-09-16 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c73db65d-aa4f-3dad-9228-f02441e9db55 | -9.64119 | -45.86906 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ab2d875-b8be-35ee-b1df-bea90b67f218 | -8.91416 | -46.2393 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdf0895a-2832-3539-aa51-9176b4ff2194 | -12.63245 | -47.51875 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68856e27-cb80-3130-927a-6619a969b931 | -11.6959 | -46.87481 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 90fd606f-fe89-3cb7-a787-64862b1330d1 | -7.98002 | -45.64434 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91c1cb02-d7c4-3ff9-a785-0abddbc83a8e | -10.71083 | -46.51094 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 63304f48-4093-396d-8972-9b13bab8a860 | -9.21692 | -44.49825 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c089f6d-7e7b-3d9b-88eb-516dacbb0d3b | -8.33325 | -44.74056 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc6bb130-77ed-31c4-ab91-6ad563d142c0 | -10.64075 | -48.74773 | 2025-09-16 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aad5c699-752c-32bd-98f6-2d2ddb7d0c27 | -11.12082 | -45.33634 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c406a405-7c18-3e3a-ba4d-a3824f7150c1 | -10.72985 | -44.75271 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfbc6860-f7e1-36d5-9a62-9f8fd65336b8 | -10.71358 | -46.49321 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 17de4d5a-af27-3ffe-8588-5282fde45b7e | -7.83778 | -46.1162 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8eb45ad6-ecf9-3d7c-9a28-90afd5db92b6 | -12.84496 | -47.13786 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d281b07f-1eca-345e-bbde-30626d6d9be6 | -12.28791 | -46.41325 | 2025-09-16 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2590b64-9faa-38cb-8b03-4bc76da7ef2a | -8.12775 | -43.65559 | 2025-09-16 04:29:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34d2ffda-0eaa-3042-98b2-3a50937ab840 | -11.88084 | -46.83452 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc768bc0-e122-314a-afd4-3c69a236cd9c | -12.05112 | -46.56823 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3aa258ab-ddfe-38d4-9523-d0dd33e1b615 | -11.44207 | -46.93944 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3598eecd-255f-35dd-9462-deed2ce54ff7 | -10.06886 | -48.1782 | 2025-09-16 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 449bff60-8407-3493-bdf3-4cec5fc60755 | -7.46558 | -46.14338 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0520a281-9a0c-357e-839f-be8755ddff93 | -11.44882 | -43.55788 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d29560fe-3b84-3a0c-a163-44b6ff46719e | -12.62241 | -45.75504 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af08337a-9c3a-3210-b9a0-d0a459337fa2 | -12.82436 | -47.22588 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89f705fb-9eae-31a5-806f-3729b8f62122 | -12.62749 | -45.75887 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eaa0677f-c260-34e5-9a72-54575d941cb2 | -12.75802 | -47.96371 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd82636b-3b5d-3e30-984f-b55fb3be631b | -8.95479 | -46.26369 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a7714f1-4b61-34fd-96f0-8a7289e40b46 | -9.48538 | -55.96877 | 2025-09-16 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ea645ff-e960-3da1-baf7-cd94f3e2910a | -10.72463 | -44.7637 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a64e88c9-3e6b-35ca-9968-d184fb20e6a8 | -9.80775 | -48.56343 | 2025-09-16 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba46af35-36a3-31d4-90ab-ce5e658f7969 | -11.11508 | -45.32763 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebd0527d-0373-320c-824a-5173e8b32593 | -11.7149 | -46.89939 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b9b7de8-6410-3e49-ae3b-b59b9f7deeed | -8.58072 | -46.36276 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a247ae96-67b8-3de4-9544-f5969115abaa | -8.12142 | -48.27731 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59fd68e5-1150-302a-a6cd-f74040a7190e | -11.07159 | -49.741 | 2025-09-16 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2430630-4e43-3550-a813-6f720d7a264b | -12.6144 | -47.95137 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81a5cf83-ca15-356b-9c8c-5bd40c5e6cd7 | -12.7569 | -47.97078 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b829664b-94b2-316e-be74-af5053863d96 | -12.73541 | -47.2041 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dbbac60-8341-34c6-a089-da54987a738f | -11.64992 | -46.59739 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cda1c405-c424-392e-a7df-7b0f46a4968d | -12.05783 | -46.54715 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7250ab8-5a76-327c-9116-038c62a04920 | -8.43599 | -47.21354 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| caf4fb9e-c9d6-3af4-a1ce-d2376c957777 | -12.26358 | -45.29625 | 2025-09-16 04:29:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d544f548-bb0e-30d7-9827-54c2e351ea91 | -10.71751 | -46.51202 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b70461da-35d0-39a5-a334-93b906feba84 | -7.71628 | -45.30081 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7a62b76-864c-3dd5-aef2-907e8328d08f | -12.859 | -47.14719 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5270f32-fb67-326a-bdd5-51a34af9589d | -9.06076 | -47.0299 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 586ab592-a172-3c74-8407-e1aa35dddd06 | -7.39635 | -49.9985 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0345762-d484-317f-bde0-2254eaab774a | -12.11597 | -44.83543 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5736af09-77f8-3739-8807-a897625c43a9 | -12.69039 | -47.98933 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88963ce6-9e7d-36be-9077-2676d4edd27d | -12.96797 | -47.96196 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de9b9c31-8816-3b08-90e7-6d63dbf01987 | -11.11165 | -45.35035 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d4308821-a3d0-39c0-bbdc-5ebec9a9fe8e | -12.63704 | -48.00239 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e84784ec-53a5-396b-ab09-fa6a78086b48 | -9.54087 | -46.29448 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c57b26da-e073-3581-80a5-02e5da290635 | -9.74068 | -55.37733 | 2025-09-16 04:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8aed891f-3fe2-3ecb-9e42-cdfbfccb5aba | -8.79178 | -46.03208 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 705e8ec9-bd33-3073-a12c-5d46f4cfb3f1 | -10.72311 | -44.74848 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9ff5e8af-aef3-3ebf-a084-a374e690c06c | -12.66477 | -47.71988 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc5609ff-6d03-3a3e-af9f-710471c6a568 | -10.16732 | -46.14175 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 685a2e99-9ddc-3ed5-9304-38356d234e43 | -12.11825 | -44.82915 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dda78ddb-4b1d-3d26-8ffa-94de24259c0d | -8.9776 | -47.05965 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56b3dbf1-1d52-3b44-a174-143af6965c88 | -10.72405 | -44.76765 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c14e84b-2ac3-3cb0-b677-9bc814bb51b6 | -7.99358 | -45.65769 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0606d623-9217-36a6-bb15-01777d06f995 | -11.48184 | -43.59551 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71fa2f93-252d-3026-be33-3a0a5e23dbb6 | -10.71303 | -46.49675 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bb888626-8c9f-333a-9790-7e0c94011d3c | -8.87664 | -46.18256 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcd3157a-4f95-34c3-9a59-f331d3ec4e8d | -11.10991 | -45.33849 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 709473f3-a7f4-377b-9771-5ba47f325e94 | -12.76023 | -47.97134 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f3a4422c-f937-335c-9ca9-8b0319568dd4 | -11.60257 | -46.96877 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7eeb77f-c4f5-3dc6-94c2-72ffece1302c | -11.43934 | -43.54506 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d18fee66-9e7f-33cc-87ff-9caa2fd69b00 | -8.6051 | -46.33793 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa186de9-32d0-325c-8f94-3385ab2e04ed | -11.90809 | -46.74749 | 2025-09-16 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 660ffc7d-1359-3dd1-9a1c-2583267e4442 | -11.0532 | -48.2763 | 2025-09-16 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0c25d87-f192-372e-9f99-e04446482dd7 | -12.17779 | -44.10265 | 2025-09-16 04:29:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81a99e8d-72f4-3dd2-be0e-5f17a071762a | -8.97699 | -46.23117 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fee7df4-1afa-33e6-a947-7f467c9711a8 | -12.61384 | -47.95491 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fbaa882-07ca-3ec6-9abc-c571c672364e | -12.76356 | -47.97189 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2f66c64-95d1-3966-8d85-56ce3d50781c | -12.54171 | -45.87019 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e04a3ce3-bbf9-3ba8-b454-fb6661b2dd80 | -11.44012 | -43.53784 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00ffe65a-131e-3293-b1c3-0adfdbdf64d0 | -7.40514 | -49.99105 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c4eca87-9147-350a-8076-1fc4d362ebb0 | -11.70206 | -46.87204 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a89bbf9b-86fc-334e-85d5-b22c6500616e | -12.80247 | -47.94197 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f60d861-62b2-3ac4-a27f-9e2e6fdcdc75 | -12.63484 | -47.99475 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b39b5ce-8c8b-3705-9517-a6e489c2b74a | -10.64067 | -48.74829 | 2025-09-16 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a41817e-cb7c-3bfc-827c-d00554b0fe67 | -11.27857 | -50.80326 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aba94b75-2620-3e13-844f-f3806754be95 | -7.99528 | -45.66888 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17a132c9-4990-33d2-9911-07bd5d7e1880 | -8.9555 | -46.01796 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 817de75b-7125-39e1-8e3c-d4771c48f53b | -12.29689 | -46.39982 | 2025-09-16 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e27c2458-e5a9-3556-91da-be7972a36532 | -8.67534 | -49.93451 | 2025-09-16 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 913a4293-41fe-3956-b351-6698596bbf21 | -10.71522 | -46.48265 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e0d6315-9735-3f5c-8e18-1c8fd13457f9 | -11.02523 | -45.06322 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 613a1f80-f30a-38e8-a411-8a3f35cead19 | -12.662 | -47.71579 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README52.md)
