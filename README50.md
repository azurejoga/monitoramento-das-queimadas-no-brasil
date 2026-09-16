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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4ed5384-376e-399a-9366-63fe6448746a | -3.37041 | -61.33213 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55485d96-73dc-34ff-ae98-4e5f3ad0ece9 | -2.8982 | -50.42747 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9628038b-c6a5-3f47-9dbd-7271f20a3524 | -4.37429 | -55.02821 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4df9257c-743d-3aed-8a5e-517bfe3052db | -3.33633 | -58.12923 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a702ccc6-ca91-337a-972a-7de65b54206f | -4.51998 | -54.96979 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d43d1186-7eaa-3d2c-99e3-9b86a4590ccf | -2.95829 | -50.40012 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e9768f7-bef0-37df-94fe-099a32f76628 | -2.26224 | -57.09032 | 2026-09-16 05:33:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0bdcb94b-639e-3849-a0d4-dcaf2bcd9fae | -3.73691 | -61.74798 | 2026-09-16 05:33:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e65d7712-e922-3e07-bc61-2b6cbad55448 | -5.69256 | -52.29078 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab5900da-ca01-31e4-9274-08448416b6c3 | -4.52329 | -54.94833 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d11062d8-b9d6-3504-a511-bbf5662a929b | -4.43063 | -55.7858 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a1c8042-5f51-3a60-a588-9a3d32879795 | -3.34594 | -58.17951 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2989ad07-adbe-3650-9264-c8215425b85e | -3.11473 | -61.13726 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65dbd332-2513-379d-a602-befdcdccf573 | -3.37099 | -61.32853 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1db61d89-4f23-3751-8b81-8b659b09c6a0 | -4.44269 | -55.51733 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1386ce7a-cd0d-31a0-a21a-24c3c40fe50f | -3.02254 | -51.33779 | 2026-09-16 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab2b77ea-d8cf-3577-b9fb-828f561fd715 | -3.39926 | -50.75381 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f6f4250-2671-39f1-be27-2bc06f8280e8 | -6.81031 | -52.48101 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 48989242-718d-3821-946c-9e803c29d203 | -2.47215 | -58.07616 | 2026-09-16 05:33:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccf4eabe-5621-35ef-b5f1-60f8d908ef44 | -3.64411 | -58.61358 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf37864a-d6ab-3aa6-8d09-124165f949bb | -2.91118 | -50.41526 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1a58da3-6946-3510-8a38-540ea432179e | -6.10886 | -57.67786 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93ddcdd1-9f49-3c97-8d41-cf2e5ac27a72 | -6.78475 | -47.87811 | 2026-09-16 05:33:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07f143e3-66f6-336b-8de6-5774dae8ed11 | -3.21884 | -61.14253 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c8c9323-5823-3df2-9a57-1f1c5e5c09b2 | -3.77894 | -58.84616 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 897311d1-ecb4-3a01-883e-7d75fd91fdb4 | -5.15022 | -55.93355 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8b10c128-0ac3-3299-990f-6307bb0ea77e | -3.73692 | -55.94557 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fab52da0-af31-39b7-b464-97e1ef27aa17 | 0.00692 | -60.58881 | 2026-09-16 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d89c3738-af14-3b55-b94d-537a78a5dc25 | -6.10436 | -57.63544 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef258518-dfc4-3023-bd5d-4226f74b990a | -5.75534 | -57.5953 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d8bc9bf6-ef34-3a3e-bce9-d3cbb3f0a4d4 | -3.16234 | -58.63789 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5847ff14-e694-3fa7-bff4-f564663e0dea | -4.37484 | -55.02459 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dbe51a2-d490-339b-a790-764a21f912f0 | -5.10992 | -47.60709 | 2026-09-16 05:33:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd0df056-5bf2-3b99-89d0-a8624e22a6a8 | -3.3877 | -50.45649 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f16e2266-8bbc-3007-bb81-a15923c214e1 | -3.71556 | -60.61404 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba2fdd7d-3e48-3e25-9409-d3ae076301e8 | -5.14171 | -55.93722 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdcf67d9-8670-37d3-82b1-c19f339a2d0b | -3.70555 | -60.61246 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1df1040d-98b2-3c36-a7c8-3731c1067fc5 | -5.13708 | -55.94147 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dad84575-bd5e-3372-9a4f-5e132e4c9373 | -3.10971 | -61.10353 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a66d513-62e4-3d4f-bcc3-0a698ab3b434 | -3.47887 | -59.48384 | 2026-09-16 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69a788a4-9edf-3651-8032-85390b106534 | -3.59792 | -59.06731 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2fb4327-040a-337f-857d-95bfdb5bc55e | -3.37673 | -50.45494 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1bea88f-0ef2-35c4-a579-0c397912e7c3 | -4.51534 | -54.97275 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7ea9274-5ed2-3de2-ada3-c9c237bd8a12 | -6.09691 | -57.68442 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6afd572f-4a79-356d-acde-0b43d71dc006 | -3.38098 | -50.83945 | 2026-09-16 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f5f7b9e2-deac-33b4-a299-3d39a5994c41 | -4.54152 | -54.932 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01a76aa0-96bc-324f-a0ae-8db5f7feaa1b | -3.74257 | -61.75644 | 2026-09-16 05:33:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78277aa3-cd4e-3b35-8614-95fb1567e4ef | -4.52054 | -54.96619 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d66edbaa-36a0-335e-8c9e-6577d7bf3a75 | -3.37156 | -61.32492 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afe89db0-c949-37a8-a9f4-1cc444c3be2f | -6.07363 | -57.8608 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd5bf0b3-3fa2-38b8-bd09-3dbadc0c1a9e | -3.69549 | -58.88413 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddc43103-64bd-32fe-982d-81bfa60ef7b3 | -3.42858 | -58.23296 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ab156ac-d828-3f47-84f9-637e21061be1 | -3.45584 | -60.51968 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3402cb0-6420-3696-9568-cc99cafc1921 | -3.4286 | -58.21051 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4e0e80e-3aa7-3ba3-a9de-08e14b50dd4c | -4.43451 | -55.78638 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e733fcfd-bffd-3046-aba0-5c66464c1572 | -6.10794 | -57.63598 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f0f6c38-7952-3469-b0cc-df59e5a9f43d | -3.705 | -60.61594 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f7317c4-82c3-3441-a71f-c8fb6399b0f8 | -4.53208 | -54.96757 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c531583e-257c-3d57-829a-4485d5de923a | -2.68339 | -57.60068 | 2026-09-16 05:33:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7488d116-b43a-3e5a-8831-be8b0c8d0577 | -3.76367 | -51.14069 | 2026-09-16 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 425386fd-f051-3695-97ae-6cda7660b82b | -4.8397 | -55.77242 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0e4e17a-84bd-3244-8c45-bec8f0b5904c | -2.69605 | -57.61037 | 2026-09-16 05:33:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59cb14a3-219a-32a2-8c3c-e31d90e23e19 | -5.13794 | -55.93838 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fbb47e4-1b04-3741-a8e1-5ef3fb279009 | -5.12256 | -47.6148 | 2026-09-16 05:33:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d34db494-dde4-3a19-8729-fcb9a5172d7a | -3.12155 | -61.25207 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9007ae4-b055-3c4c-9917-17c316c579cb | -5.14642 | -55.93473 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 43575af5-fa82-309e-a3f1-acce9b0a8ba5 | 0.14937 | -60.60345 | 2026-09-16 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c15c8d1c-64a4-3f84-8e11-ea7d9d352dd5 | -3.36268 | -50.7413 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29a66326-e6fd-37e8-a06c-92b61f439185 | -5.75423 | -57.59024 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b09658bf-a4a6-38f8-b404-a707cc894c0d | -2.70704 | -57.60821 | 2026-09-16 05:33:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6bb713f-35cf-3965-87cd-cc74d6359226 | -5.14715 | -55.92978 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 73270030-e5e3-30f4-9fed-85076f364be2 | -5.12936 | -55.94009 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68e92586-06a0-34d4-870e-21a2ba549a5a | -3.22549 | -61.20963 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b39e1da-480e-36b0-b351-aa257b92a59a | -3.15341 | -49.22316 | 2026-09-16 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11d6bbef-cbd2-372b-9106-37368ea97128 | -3.11028 | -61.09996 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57d6b873-fee6-318b-a939-c9ae68e6a0dc | -4.46503 | -55.05651 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9f7c62b-cbac-3c5a-9067-b746847265ed | -4.51179 | -55.46104 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bbcea1a-e7e2-35bd-849c-e288f527fb87 | -1.28562 | -55.71295 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 251e9229-6060-38a3-b430-1174bdc0b7d5 | -2.78107 | -57.02509 | 2026-09-16 05:33:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96e5e9ba-d77a-305c-822a-ea63325aaba9 | -3.44645 | -50.66017 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32e52791-149d-3e85-b3a7-fd9b9f9c45cc | -5.13722 | -55.94326 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5023fcae-58d7-3fb5-bd70-72d546858304 | -1.28427 | -55.72176 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95ead2f7-8b43-36e9-b7d9-0833fc05e5c6 | -2.89223 | -50.43013 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46dc4657-c64c-3dce-8eaf-22adac5e3fd6 | -2.86903 | -49.63245 | 2026-09-16 05:33:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 961ed705-2123-32da-8216-58525ff203f6 | -3.29929 | -59.45931 | 2026-09-16 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b48caeb-d830-3716-aefc-77deba40c86c | -3.33291 | -58.12869 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f94adbb3-ca5b-351c-b54b-9611b94ac58b | -5.14182 | -55.93901 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 67728987-a4d9-3001-901c-d17abbc22e2f | -2.95042 | -50.41413 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bed33891-3603-33d3-8dc5-84e11d517e19 | -3.37517 | -50.84185 | 2026-09-16 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f46a7ad-02c1-3153-b4d8-8d5c554aabce | -4.26264 | -56.01282 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e488b106-873f-3f10-8417-f81f0c103859 | -3.70388 | -60.62291 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e844436a-e079-3a3a-bfdf-bcc5f05553a9 | -4.43909 | -55.52002 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9996860-5c26-37b7-aabc-34f22f200ba6 | -3.29875 | -61.60399 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27b80971-ff53-3c33-b0b3-7d231fcf7fd7 | -3.74034 | -55.94342 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53da1312-9a7e-3096-bd91-df887b8edda2 | -3.73766 | -55.94085 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31b83bf2-a5b2-3c01-9827-cde98d59dbf0 | -3.15669 | -49.22193 | 2026-09-16 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10660bc1-ed51-33e7-8603-cd81d7d1f1dc | -4.54614 | -54.92911 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6606e28e-53a6-3499-9e11-48508a3f3f9f | -2.95748 | -50.40451 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13fc436d-0e22-3eb1-b91b-86f989c6a2a5 | -2.68972 | -57.60553 | 2026-09-16 05:33:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6bbfe3d-c8a3-3e94-b4ab-a8305c20ef00 | -5.63185 | -51.69257 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README51.md)
