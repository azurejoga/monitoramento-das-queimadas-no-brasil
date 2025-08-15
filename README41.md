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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 259a30b3-1d24-3408-841a-2934e6e9eab8 | -6.9302 | -59.5497 | 2025-08-15 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ff98e8b4-b816-322a-86c6-0c5675bf1be6 | -11.3468 | -55.4124 | 2025-08-15 04:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b61d7efa-0a8a-335e-9549-ab7027dee605 | -9.4992 | -60.547 | 2025-08-15 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 2c597154-10d0-366b-b5ce-cb99de57b931 | -9.4994 | -60.5278 | 2025-08-15 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| cfe14bd4-0435-35b9-88cc-37b9bac5e83a | -6.9303 | -59.5305 | 2025-08-15 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 51a82044-bf7a-3824-87e8-798a62ba7f54 | -6.6945 | -58.8259 | 2025-08-15 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| e46b2c6a-da4c-3628-82df-9ec7c265b775 | -9.1708 | -59.6568 | 2025-08-15 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| c29244bb-1ecc-32e7-b33e-a769959f95c4 | -6.0806 | -59.9657 | 2025-08-15 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 8052da8b-edfd-3b33-b3c5-c70b7fbd169b | -6.0807 | -59.9465 | 2025-08-15 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 17d6285c-99d5-34e9-9aae-489238e108bc | -11.35041 | -55.41079 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 81cdf601-34e1-3f5e-bb4e-c05e158e461e | -6.65185 | -58.82403 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cad66bf0-cb37-397a-9a7d-efe81e75fa7f | -11.35439 | -55.40768 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08d3a0dc-3983-39a0-8bf9-96b2062691be | -7.3323 | -60.62096 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3a63b51-0d22-372c-a3ac-61b6baab1a02 | -12.42008 | -43.4959 | 2025-08-15 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68b3d4be-4822-393f-bb3e-a18d5ee72946 | -7.88348 | -61.81575 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71ae4a23-44d8-378b-9c98-dc5770726615 | -9.18095 | -59.67809 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc191547-af37-32f3-bd58-b705dba38db9 | -6.88643 | -59.14967 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 103fb12f-cb7d-3759-8efb-733bbbf30fc1 | -9.16482 | -59.69291 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6b7ca73-ef07-3639-b06c-02b0e4fbbfa3 | -6.69874 | -58.82192 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| adc2ea44-bab8-32f6-a7bf-c8f4fb772c93 | -13.03485 | -56.85962 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55ac2c7b-7c07-335b-a58c-52e22bb19083 | -8.37612 | -46.99696 | 2025-08-15 04:51:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55937a2f-d86f-363f-aae5-a577357c12d7 | -7.87887 | -61.81176 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7129b851-87af-3698-91bf-9b72cadb7c7a | -7.95351 | -61.75172 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a6459c08-eba6-35af-8664-357c8c02c693 | -7.42206 | -60.03769 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d316ef0f-b954-3b17-8d9b-d7c24d854795 | -7.24643 | -57.65997 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4da54184-aeb4-3d68-8d1b-2b517093cc31 | -6.90258 | -59.63425 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f69d59fe-c7d7-3a68-aa2e-208822575ed8 | -7.12012 | -59.62925 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba8e50a1-10c0-3f26-be6b-dbbca65d3b2e | -7.02635 | -59.81762 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57a016e2-b9a6-3aaa-a4a5-76fe9d702941 | -9.16557 | -59.68861 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3110fdf1-ce47-3905-85a0-3129106125d9 | -13.11432 | -57.16544 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59895f3f-f585-3044-8d6e-e4ee85467533 | -9.17958 | -59.66015 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 15e8221a-6266-3918-baba-f2dd08a4cfc8 | -5.89329 | -57.73868 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3bcee7a1-fc87-3846-8e9e-a6b4077e3835 | -13.33169 | -45.23296 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 501093be-f624-3af3-99d9-910588c7e67f | -9.1802 | -59.68238 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47541468-a251-30bc-bd4f-321708bc2629 | -12.59807 | -46.96881 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18cc498b-a38e-3506-aaeb-af71c0939ed1 | -6.53341 | -56.19946 | 2025-08-15 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9a52260-06ea-396f-9731-f0e9f96f6207 | -7.33708 | -60.61653 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f7a90cb-5961-3270-ad46-9f6ad7810bb8 | -7.96175 | -63.46535 | 2025-08-15 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc00042c-3c17-367c-a2e7-03081eb7305f | -9.38609 | -60.54974 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bd6a1823-315f-39af-8a34-3550aaeab098 | -7.96269 | -61.75972 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f92336c-4d5d-3fe0-8442-a401f2f4f4a9 | -8.56065 | -63.91039 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 439d8305-6772-3a27-9e5d-775ab93eea19 | -6.94742 | -60.1421 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db0bc29d-4523-3efd-b692-509f928bc59e | -7.88064 | -61.82336 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cfe143d-9ca6-3048-8df5-0a101fec9309 | -9.1722 | -59.67658 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc0586cb-1748-30b8-bb7d-a079e0b4bc14 | -7.9273 | -61.75 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f237db2-02a8-3816-9911-6857f658eb35 | -6.06842 | -59.96631 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26683118-05ff-3b09-8e18-71837a9c000d | -9.50268 | -60.52504 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0c686c8c-8d89-36e9-bb2c-5ae6ae4b1ddd | -7.52671 | -61.34049 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91130a80-ad2f-3d67-9d90-dcd4027239ca | -13.12636 | -57.15905 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88dbf615-1da8-3e8d-9271-5bf6fc70c0ee | -13.47083 | -56.66322 | 2025-08-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e88c72a4-29d9-36a6-804d-a4db922aeebe | -6.70733 | -58.82343 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7a66ca15-43ae-3a3c-aea0-970061ac67e5 | -9.85555 | -44.6878 | 2025-08-15 04:51:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb4b8b23-b2ac-3d77-8e32-a4a300ba9633 | -9.15034 | -59.67268 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6856b4a-2714-3433-9883-09d2827731df | -9.03059 | -40.52447 | 2025-08-15 04:51:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a1d8035e-fac6-370a-b7a8-5aa209a2c179 | -6.90467 | -59.14854 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52ae013c-5d5f-34ae-b3c8-b109122f1119 | -9.14916 | -59.41527 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86b6bb0e-8dd0-3c34-971f-c56ef9388b09 | -9.14958 | -59.67698 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c7b0e69-92be-3664-b4ef-75817a2f4159 | -6.88787 | -59.14121 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4f0f92a-f0bb-3da3-ac3d-a9f3c285ed4a | -6.91488 | -59.14147 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 051b5b27-1a5b-3a27-9a28-7a6a9d09648e | -11.3532 | -55.41502 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8d0c3d8-cb99-3abe-9aa6-f948f1221be6 | -7.87194 | -61.81217 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b0867a7-3cf1-3e77-9d85-c9cd9c5fb7fc | -13.12566 | -57.16319 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b88721f-e7a3-3107-a9b0-0a171d680b83 | -7.52777 | -61.33464 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 76774d2d-eae3-3e51-bb2f-b4c86289c474 | -7.14322 | -59.65723 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2651721b-3bf0-36c6-b9f0-a86022c85a24 | -7.96159 | -61.76595 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b20ef332-ca20-384a-985e-7bc9566c860f | -12.58598 | -46.95337 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eb54fec0-fc91-3201-8039-6d7a2b32c243 | -9.49998 | -60.51868 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f22c31a1-58d1-3f5c-a9c2-74cb8571c2fe | -6.94252 | -60.00338 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a399936c-9625-384f-883a-c1301a18f21d | -6.66612 | -58.81803 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 842c7f15-75f7-3e0e-b791-e052d5d513fd | -7.32172 | -60.61921 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 765e9a44-d225-3eed-acaf-417d167527fa | -7.43435 | -60.01568 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3b2707e-d8a6-3df1-b543-c3e324783b77 | -9.50119 | -60.5389 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c4138a4e-6da3-3fc0-852b-6af2cd3659ce | -13.87019 | -43.49337 | 2025-08-15 04:51:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74cbde3c-d557-385c-a815-a52e15ce8248 | -7.38579 | -56.68526 | 2025-08-15 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c15c9f92-a425-325a-bac6-8344d56f4653 | -6.07483 | -59.95718 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42d70497-197a-307a-894c-6533e53eadc9 | -11.73794 | -64.90126 | 2025-08-15 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebd15c3e-447d-304f-9745-a86238115ff6 | -6.71232 | -58.82014 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87973330-2083-316d-9ed6-a22e3db3d2bf | -7.95756 | -61.75879 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f68d4daf-c333-3af0-abab-b555faadec9a | -9.1944 | -45.32982 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa770edc-fd09-3e2b-8d57-07a17950346b | -7.8603 | -48.23488 | 2025-08-15 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b9ea7bd2-c3f8-3a70-a611-b2e4234d4892 | -7.96214 | -61.76283 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 056633b5-26ed-35b5-86b5-6889c5e33e86 | -6.07569 | -59.95218 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54797b28-1ca6-3874-aacd-4535e02875b7 | -6.71731 | -58.8168 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e671180-5819-3cd3-9b15-e9dae2de9840 | -13.1079 | -57.16005 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff60a074-1875-3aa0-9d04-cd25af51daa0 | -6.64823 | -58.81922 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e060b95f-6835-3dfe-a94d-9bebc44df048 | -9.0108 | -59.53782 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d2b2826-cf02-359e-9abb-a3abf6903481 | -7.8714 | -61.81527 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 581d2012-aa54-3918-969f-4951947fc9a5 | -7.42168 | -60.03347 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a093b070-58ad-344a-9697-0b04728f3572 | -7.2447 | -57.67033 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee4e78ac-6520-3af3-961a-561defedd640 | -6.90933 | -59.5411 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d405d5ab-766d-333f-a330-cdbf6409e8f1 | -10.34876 | -64.45756 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec1a7011-c3ef-32e1-8b10-7a12ba2e7914 | -13.12991 | -57.15968 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e0776b6-a6bd-31dc-88f3-49d469fd3e7e | -10.31572 | -63.62449 | 2025-08-15 04:51:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5db2c64-8b4f-3b5b-92a3-13856ea20f94 | -8.05216 | -61.59811 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 112302a0-e193-3946-aef5-fc565703c266 | -9.038 | -40.51947 | 2025-08-15 04:51:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6ad1092a-06dd-3093-8d9c-9d082e1c8175 | -13.32077 | -45.23489 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6d2391b-3be3-3f2d-b1ce-ea2fb59f218b | -7.94782 | -61.75389 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f457a20-d4e9-3ebb-9dbe-8aca98146c50 | -7.0853 | -59.22816 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3019566-33fa-33d1-b071-736cc0e4e3e8 | -10.04785 | -59.36307 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a242dece-4352-372f-91e1-1dcc66173d92 | -9.19187 | -45.33461 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README42.md)
