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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 680d62dc-e3bf-38d6-95b6-1a9cfc1fe9a6 | -6.8497 | -55.57041 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2af9356-27c1-3474-8795-65d7b064f077 | -3.87621 | -58.90198 | 2026-09-14 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d79684e-a7e6-34bb-9e0b-9db3f08e5d73 | -5.13529 | -55.96002 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5728aec-a27e-31b7-957d-c96f5d969768 | -6.32429 | -59.98374 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 721bde34-b231-3457-abb9-9eba2dee3319 | -3.54527 | -53.98396 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2628e20c-89ae-37ab-b2b3-810cfefde180 | -2.90149 | -50.3872 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9a09f54b-7167-3d2e-ad83-19fe25169b45 | -3.38126 | -61.31388 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc8dd45d-15fd-3602-8e73-74211904babb | -2.90294 | -50.44668 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a7512d42-a7c7-35ed-b1b9-25be253713ee | -2.88457 | -50.40872 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7578d8bf-abb9-36eb-981a-f54fd1255727 | -5.12167 | -55.95213 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e023d308-a564-34eb-a079-12a3176865be | -2.91967 | -50.4255 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 120ceddd-7f72-39d9-a440-64237957e2a3 | -6.58648 | -58.84261 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 731ed9c9-9f95-362b-84b7-aa3e96473f84 | -6.59298 | -58.8544 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5112570-0c09-357e-b9e8-0696a51766de | -6.4991 | -58.38401 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73848995-c18c-3ae2-bed7-1f2449ed199a | -3.38937 | -50.75533 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2e00a88-02ab-3c5b-b8a4-1d351517a5d3 | -6.30222 | -55.27482 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b83a01b7-1233-3a64-bbfa-2a4f3a129ab9 | -3.41086 | -58.21355 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8fde086-ad4e-3693-ad41-d959b74567e4 | -6.37488 | -55.26052 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8f64805-6913-32b1-b3f6-63c12cf5be99 | -2.88293 | -50.39556 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c8b3633-3e63-3718-b982-e8453d0adfdc | -3.37784 | -61.336 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d3a6b87-fa2a-35c4-9aef-47cea7469929 | -2.90131 | -50.41056 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| dab2b596-ccda-3220-9989-85226030065f | -6.11132 | -57.86234 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2d43ad0-18cb-3d36-b231-5941ceb0ffe3 | -6.62517 | -58.37801 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8829d255-9254-3aba-9f65-e62dd7915e54 | -4.13706 | -54.01757 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a70b5cf6-cb70-3769-849e-1cd0d9370662 | -7.10045 | -55.63596 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ddf0b4b-4053-3370-9b0c-bdd853ea7e18 | -6.87342 | -55.29117 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 327d0b31-7939-3890-b685-ad63b1c8cfae | -2.9006 | -50.39315 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9eaa6f35-7c44-345a-b969-b864c5d4c8c8 | -3.74163 | -61.75204 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86197ab9-ca2c-3451-958c-b238879e972e | -6.64345 | -58.82494 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b81a3fbb-3aca-39c6-9cb4-7b043c867632 | -2.93062 | -50.39715 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 76574145-e7a3-3d52-bd90-fda51e144737 | -2.67534 | -57.55878 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b268ce93-3d19-3dd2-9c0e-41b46b2397e6 | -6.02386 | -59.94518 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ff5c3d2-af8e-3ef3-8b4b-af5d5a1894ef | -3.1693 | -61.18736 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f0ea3fe-4e7d-3916-86de-2b3b80555e72 | -3.63519 | -58.63982 | 2026-09-14 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 491d117d-128d-3ab8-9e78-3df1b9252f19 | -5.13606 | -55.9547 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ce565dc-ba20-3a35-98e2-a165b602efe8 | -2.48748 | -58.00652 | 2026-09-14 05:36:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73763ad0-aad6-3ceb-adca-34c4c8e71cef | -6.31165 | -55.2823 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10120b87-1d80-3f9b-a736-5b009dab6f58 | -6.10901 | -59.8886 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e440d5ad-c83b-336a-b57e-794d0d6f8ebc | -6.30065 | -59.95485 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4ed9a78-2b64-35e4-9702-ac0ee78a752f | -6.58895 | -58.85379 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9508c1c7-2cb6-3c2d-aec0-90199c069061 | -6.27705 | -59.93267 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50e7aa4e-adb7-3ac2-9ebb-ae1eb5bcf6bd | -6.38003 | -55.26123 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d22fdd4-f9f3-39d3-a1d1-33dfb7089f34 | -4.77905 | -56.15605 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 924e6a78-9f01-35a0-b66a-81cec4a046ab | -6.10723 | -57.63137 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 40125798-2680-3ff5-9b46-0022198902d1 | -4.39987 | -55.23365 | 2026-09-14 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c487c5de-d49a-37fd-b2f3-c10cd21e27cd | -2.88632 | -50.39704 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fba2d1a4-db50-3b29-a008-c73c63727086 | -6.11074 | -57.86638 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ee10ec6-79bc-31a3-827b-7c61b4b9f442 | -2.67479 | -57.56255 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8aaf236e-066d-36ed-8759-413eb2ca5d4d | -2.67394 | -57.55566 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 732cd134-52d4-3eba-b15c-40461ab766ce | -6.30565 | -55.28781 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8583fe80-faac-3eb6-92b6-086a2c8ae0d8 | -2.90328 | -50.37531 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48b3115d-6819-311c-9305-203da4000710 | -6.29621 | -55.28035 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80dbd789-011f-3cf8-bf3e-1a3698f288f7 | -3.38778 | -50.76646 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9613844d-a077-3193-a873-5cdf472c139d | -2.66069 | -57.50333 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33741d08-b8c4-3dbb-a216-393f2746f419 | -3.16824 | -58.64571 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b5efd69c-049d-3960-a44e-377b96927bde | -2.89616 | -50.42265 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 815e7f1a-b2a1-3b5a-bc6f-147d0e6901d7 | -6.1531 | -57.69205 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3e2449ed-864e-30fd-bcd6-3150d04b3621 | -2.90799 | -50.41166 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 7258d75e-b455-38fd-8e71-31d72912bf67 | -3.89849 | -60.59326 | 2026-09-14 05:36:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e96c756-bb8d-3355-9d67-4ecce90eb50e | -6.7882 | -62.98005 | 2026-09-14 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 687963e2-d082-3818-bac1-8e580bb32840 | -3.07833 | -61.52941 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b94954d0-ef98-39fd-93c8-1751f3349862 | -3.7315 | -61.75049 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2c05a5ef-94e1-346c-9a01-272bfbe98e95 | -6.28593 | -59.92468 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d120ee4-e975-31c0-b8d2-848ed2c4cea9 | -2.89971 | -50.39907 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d4000602-d2b1-3233-be03-c3e4b94235ef | -6.11579 | -57.6739 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9678b56-9c4b-306f-8aa1-91bd7aeac98e | -6.01572 | -59.9485 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f09a7260-4622-303a-a695-774fc1e844c9 | -6.58192 | -58.84553 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23dd6fc9-c5c4-3455-8b5b-f28512f56fc5 | -2.89439 | -50.43446 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ab1e5564-b73a-3bef-a6a7-bcc1a05a4890 | -2.92721 | -50.42065 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4d919569-7454-3510-8310-f32accbb5552 | -6.85392 | -55.56655 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7518b194-8025-3d7b-b579-36ceb9640342 | -3.39015 | -50.39074 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6bd890d1-6968-3245-9dc3-20ce3ce4b622 | -6.22461 | -56.04156 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f7b315b-16f2-3bf5-8eb9-1d13a22eb66c | -6.29072 | -59.94419 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 545460f1-9c6f-3730-9e84-04a7c4e2966c | -3.17252 | -58.64815 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 72ed364d-1dbe-39d7-89e8-b3f8cab4da7a | -3.18707 | -61.11773 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45c5b626-3f7c-3e6a-bb22-a989b976a298 | -6.29061 | -55.28298 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f4a438a-457a-3231-8472-12d43ff1a2e4 | -6.29665 | -55.27715 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ce092d6-420b-3cee-a291-0ee152d75aa2 | -6.31499 | -59.96164 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1052e6eb-73a5-3203-b796-c29de2d5fd4c | -3.41193 | -58.20653 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 42590d1b-7f4a-32a7-9be3-05aab20f07d7 | -3.15435 | -60.27053 | 2026-09-14 05:36:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3db59af8-c2be-3e2c-9ec6-ba650cd48c97 | -6.10442 | -55.66721 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 334c0dac-eb0c-39e2-92ae-6af00167e93a | -6.78711 | -62.9871 | 2026-09-14 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5939c1d9-aac8-3bf8-ac26-a130f48da73f | -6.37568 | -55.25464 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5642b40a-44e8-3c86-8e3e-92b71b2a3855 | -6.29531 | -55.28688 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95b4b9a4-a1d6-3e28-847a-231b16f4af31 | -2.67153 | -57.54372 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 08506266-0457-30d9-ac9d-2f8cba2f350e | -6.79882 | -58.78599 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0942cd2d-10b5-33e6-b049-5383d8ad5ba3 | -3.73881 | -61.74792 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71407eee-7394-3eb4-b46b-1c39a574d272 | -6.0819 | -57.86394 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c00d992a-f720-3481-8077-b52209d72bb0 | -5.73289 | -60.22361 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd40894d-393a-3887-9934-7dfe4ee7ee29 | -3.37386 | -61.33915 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc433de2-c8aa-3fa8-9fae-e5f5d7cb095e | -6.68116 | -58.87789 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 662ea312-7c37-38e7-951c-0781e7bc710b | -6.5784 | -58.84137 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 81fd9812-e7b9-3248-92ee-82cac606084a | -4.12672 | -60.68719 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e09ea248-b4a3-31f9-bc53-52553fab9fb6 | -2.93216 | -50.43362 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2e59bf8-3ef8-3cd9-80c5-4a9303b8ab4a | -3.3767 | -61.34335 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 799ca363-56de-34ea-ae5a-38be89f74d7e | -6.28457 | -59.93385 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74b9821f-319a-3ef2-b8be-b976b62c9b74 | -3.14299 | -60.62905 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a116c79-38ca-3a40-bb2f-cc6d064ee004 | -2.61056 | -54.75634 | 2026-09-14 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| bd699baa-b93a-34a7-9669-6e3c47d35ee4 | -2.90208 | -50.45266 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| efb00c6f-ee86-37ca-aeb7-242a8365323f | -6.54438 | -58.55804 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README53.md)
