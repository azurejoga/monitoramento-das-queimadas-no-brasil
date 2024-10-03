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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29ebc096-5d9b-3756-a70b-6464346c1a06 | -9.56238 | -64.25755 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3e6f657-9910-3004-8278-7670fc3527ce | -9.55642 | -64.25638 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25d4ff53-ba5f-388f-94e5-ecfbc6e0b979 | -9.55558 | -64.26073 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9789cc33-a8b6-3cc4-b8a5-c52d20a864b2 | -9.55045 | -64.25523 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a8b282d-b9b3-385d-99ec-4ff87870e20b | -9.54694 | -63.14713 | 2024-10-03 04:51:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c0fbc58-b908-3a96-89c7-76ca478b6573 | -9.54624 | -63.15081 | 2024-10-03 04:51:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1521cfec-bd79-300e-9f0e-2f2a2550c3c5 | -9.54067 | -63.14983 | 2024-10-03 04:51:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dae5e5f6-99ab-3690-98b4-b24a4ada0ece | -9.52931 | -63.61641 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf9e540c-9ff5-3947-b8ff-2acdb9e95448 | -9.52915 | -63.61833 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f35d5fe-53b8-3b3a-8ec9-4e25b9ace366 | -9.52438 | -63.61098 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02f97485-fd12-3b23-a406-7abdcb09ea41 | -9.52425 | -63.61292 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2ce965a-c243-3013-bd08-710b576f08ea | -9.52362 | -63.61508 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17787020-ab6c-3194-ad99-8d20942e8e07 | -9.51473 | -62.92671 | 2024-10-03 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1f163db-0011-34d8-b652-accd22418f34 | -9.50924 | -62.92566 | 2024-10-03 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 450d8af7-3fa2-306c-8702-154b7a721ade | -10.70507 | -64.14905 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69cb0e2f-e5cb-396d-9361-4dc5d0ea7111 | -10.70431 | -64.15301 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc0c53b2-254f-3442-990b-fdb47ddbea03 | -10.69833 | -64.15279 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f07a763-0c66-3fd2-9133-fe4a9fc4f843 | -10.69748 | -64.15723 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b4ed394-959c-32a3-a5ab-8fdc289c8275 | -10.69237 | -64.1524 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02ee8db7-65ef-330b-9481-4b3762333687 | -10.69156 | -64.15665 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c81a450-0442-36ee-a70d-f837b8413e4e | -10.62815 | -64.51845 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae77e850-9ca6-3782-ab99-7185904e7663 | -10.62228 | -64.51681 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec2dcd69-a7f3-3819-994a-7dc9de70460c | -10.61624 | -64.51605 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86b78f3e-3aa0-39bc-8dee-53a6421c7f7d | -10.61592 | -64.05226 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3f38571-4c6e-3b5f-bebb-f5d5f5ca5520 | -10.61521 | -64.05602 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64debd0f-266a-39b5-8fb3-fdcc8798d85d | -10.61445 | -64.06001 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ec6bc6d-68b8-3a0b-9829-93707458eefc | -10.61012 | -64.05124 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa4242b1-e794-36fd-ad0c-d881d1c8a53c | -10.60939 | -64.05504 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7c8320d-05ad-3162-bb6e-b87fde3e34a8 | -10.60861 | -64.05915 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef60de4f-d502-315a-b7e0-20e6d509d44a | -10.36535 | -64.08283 | 2024-10-03 04:51:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e84a2878-3ee0-3555-b6cc-a2b144dba776 | -10.11066 | -64.42044 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a67b7077-1402-3b64-acbc-2f58e74d6148 | -10.1047 | -64.41921 | 2024-10-03 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1545798e-02ac-395b-a378-e8b5e99644d6 | -10.26479 | -63.33182 | 2024-10-03 04:51:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88bcdeed-f248-32f5-8d04-58d0b28732b9 | -10.26409 | -63.33549 | 2024-10-03 04:51:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9f95c46-c006-3756-8d6f-d2007d78341a | -10.26338 | -63.3392 | 2024-10-03 04:51:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efc1205b-be95-3a73-87be-5e001e558313 | -12.02198 | -63.7758 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 067de934-d3eb-3516-b378-2c5001773dcf | -12.02126 | -63.7795 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 331ec26e-d03c-3393-80e1-35dbe81b4bd7 | -12.01644 | -63.77469 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 044c3ace-385c-3ff6-8aa5-58a96a4a8f9f | -11.68035 | -64.04399 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f873c4bc-0eeb-3387-8ff2-3ee9fb5f47e7 | -11.67957 | -64.04805 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 186f5493-d836-3075-a57e-55d47521abdc | -11.67482 | -64.04214 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c5c0866-130e-3393-855a-3b467887143e | -11.67404 | -64.04613 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 198d93e0-e6e0-36ea-aa9a-10cca535fce6 | -11.67343 | -63.98866 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a3312ecf-96be-34c9-8f74-952dff89825e | -11.67318 | -64.0506 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5b24a38-d8b0-3e65-a860-8557615a6449 | -11.63476 | -64.03591 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2dbee12b-860b-36e3-9043-31bf1c452ecf | -11.63397 | -64.03994 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1041b6c3-3950-3358-b47c-a78ecbb43f37 | -11.62907 | -64.03484 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2ceb9459-ccdb-31fe-a60c-4475a942dc92 | -11.62828 | -64.03886 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 63aee2bd-ad58-3796-be70-01af3ec742cf | -11.62337 | -64.03381 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43ec26e6-27f4-3449-a6e4-6ce463273035 | -11.6229 | -63.97663 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3e1d59a-34fa-364b-8e35-6b24ddc66ff6 | -11.62148 | -63.97477 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45449855-f021-3c6b-a9e9-0a4e4a8d403a | -11.62073 | -63.97874 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d19c613-1ffe-3d58-ab86-1d146e868931 | -11.61725 | -63.9755 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a6c1d06-2f76-3813-946a-0259a5d88c55 | -11.61656 | -64.09828 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a2bd5bb-a9d5-3634-bbcc-e1e6bc39858b | -11.61499 | -64.10625 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 177f4846-ae94-33b6-af06-cbb77a808bd1 | -11.61463 | -63.67756 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c097447c-b7f6-31b6-a2af-4ee82b2e4700 | -11.61389 | -63.68139 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b1feee9-363a-35b3-a3f2-566411e63d98 | -11.61106 | -63.72573 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3cca966-208d-355c-99f3-2040593603f0 | -11.61104 | -64.09153 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4836e9b-0a5c-38d0-881b-5ede10125d02 | -11.60555 | -63.72432 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e10f5e0a-2c91-3894-8da9-0e27b92b95b5 | -11.59756 | -63.76548 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e192d793-d1a5-375b-911f-1729ff507d43 | -11.59094 | -63.76968 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8dac20a-cc92-3d2a-baae-2ce8529aa2da | -11.58058 | -63.76336 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d570548-a0f6-3092-9fa5-47ce059a03cd | -11.57959 | -63.76843 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69db9edc-df07-3718-acf2-b875634bacbf | -11.57478 | -63.76336 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6945b73-2621-39d1-b6dc-170399c59dc3 | -11.5619 | -63.76983 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6cc167d-796d-355c-a6f5-8f352c49675b | -11.55912 | -63.76856 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ee0dd18-4c15-398f-9e8a-3606c9d25a4e | -11.55839 | -63.77242 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38da6309-f662-3d1e-8bee-632fb7148f51 | -11.55766 | -63.77626 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09a393d5-ce2e-3589-8bf4-56211c9bc1e3 | -11.55681 | -63.73677 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72fdfe23-d166-3b7b-ab19-a01ff1b4f7c1 | -11.55555 | -63.77256 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 918fb61e-2379-3328-a4c8-ebfbf48aca41 | -11.5548 | -63.77639 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b639b926-7db2-399a-8355-241abde851a8 | -11.55378 | -63.7356 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc632028-1001-391a-bbdb-928b78add6d9 | -11.55305 | -63.7394 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dda44d43-743a-39fc-81b9-b7f81e118799 | -11.55118 | -63.73593 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4c5bf0f-be7b-35cf-8d87-7291cd05adba | -11.55044 | -63.73968 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fffac8c1-19e1-3b6c-b866-1229d0db4486 | -10.9928 | -63.92543 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57d61085-195e-303e-b872-c6731f4470c0 | -10.99199 | -63.92953 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c6ecb1b-2719-31db-a0ca-cba2184cfbd9 | -10.98311 | -63.94458 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 230f849f-689a-3ad5-bfbb-64c6afc8c35c | -10.98234 | -63.94849 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb91a083-10e5-32b3-928a-7a6ff085ebe8 | -10.98214 | -63.94656 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 630c5d08-f0a5-3bd2-8a2b-ab13498e8f01 | -10.98159 | -63.95234 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f33df5a-7d4d-3a91-bd23-dc40e8248a11 | -10.98141 | -63.95042 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38d08036-c1a7-37d7-be8f-014438dcba35 | -10.98085 | -63.95608 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb8bfb4f-d81e-3993-9fd7-95c63aaefd5e | -10.9807 | -63.95414 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65eded89-77a3-34ca-a51a-2b160ce9454d | -10.98015 | -63.95965 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79ce1ba8-ca54-33e3-a29c-bb690c34e440 | -10.89793 | -63.89184 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08e217d5-ed86-3fe5-bc0a-1d7df978858a | -10.89716 | -63.89579 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e26d277-efb1-3507-9b44-40379a36d9b0 | -10.89648 | -63.89255 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0e631fc-f249-3770-974f-a65cb3baa4df | -10.89647 | -63.89929 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f60ce696-9513-3816-ac42-c36f24107331 | -10.89579 | -63.90276 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef715574-9680-3627-8b2c-7bd3e76242e6 | -10.89575 | -63.89642 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d63f8449-7822-3954-a097-52f4f070fa18 | -10.89508 | -63.89995 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c06cfa3-4357-3041-828e-aa6c8a5ea9db | -10.89498 | -63.90693 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e15e34ad-a4ee-3473-b071-252dbc196a6e | -10.89441 | -63.90352 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f92fe2d7-2c5f-3bb5-b5d4-8d2a51894268 | -10.89403 | -63.91176 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 76584f02-8eaf-3ff5-8275-7402fba12dca | -10.89357 | -63.908 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a7bd555c-6823-34f5-bda2-f72121365242 | -10.8908 | -63.89803 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf3541fc-9be6-3fed-b0eb-191f9c0c8f63 | -10.89011 | -63.90152 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| afa067f3-ff48-37c4-b894-1c4d80231552 | -10.88939 | -63.89877 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README138.md)
