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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eaa7bc0-852a-34ea-ab2f-22cdef54bfa7 | -10.6641 | -54.1491 | 2026-09-14 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 363.3 |
| 8d88f09e-fb75-3d81-8d71-a47f279efada | -10.6827 | -54.1679 | 2026-09-14 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 174.7 |
| ab273e53-11ee-302a-8226-c1a11da81060 | -10.6829 | -54.1475 | 2026-09-14 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 396.3 |
| 3882239b-af02-3d08-b4a9-5283741fabaf | -10.6643 | -54.1286 | 2026-09-14 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 2e3992bf-50d2-3e90-8763-67d829465031 | -10.6638 | -54.1696 | 2026-09-14 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 5022921f-c03e-34e4-8f6f-3b5a83f00d9f | -9.4328 | -50.1086 | 2026-09-14 06:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f0106ccb-72d1-3a47-b659-467944ec89ae | -10.6832 | -54.127 | 2026-09-14 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 7058fb2f-fabd-3cc4-b01c-2dfdb61fd45b | -10.6638 | -54.1696 | 2026-09-14 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 725110cb-3edb-3fd1-9697-484980b9a945 | -10.6643 | -54.1286 | 2026-09-14 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 79cf6a1b-c9aa-357f-8d00-e148c2e66f3d | -10.6829 | -54.1475 | 2026-09-14 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 333.1 |
| 8ea44cde-51b1-386e-a0ca-dbaebcd4f9fc | -10.6641 | -54.1491 | 2026-09-14 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 328.5 |
| 202ca8e5-60be-3999-882f-ac3364119641 | -10.6827 | -54.1679 | 2026-09-14 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 39a07c6f-36db-3d9f-8acf-a992d57c8e1d | -10.6643 | -54.1286 | 2026-09-14 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 35e86c8a-7ae5-33bc-81d0-10ebce46b7f4 | -10.6832 | -54.127 | 2026-09-14 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 91646209-8920-3cde-a545-3d586b747e70 | -10.6827 | -54.1679 | 2026-09-14 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.3 |
| c7001f93-3f94-37b2-92f2-5858539cd40b | -10.6641 | -54.1491 | 2026-09-14 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 257.8 |
| dcaa7e03-9d61-354d-b0c4-46dd13675b7e | -10.6638 | -54.1696 | 2026-09-14 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| aad2b507-2d3c-3239-bde3-0470f73720aa | -14.1861 | -47.3844 | 2026-09-14 07:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 0a666611-1194-33e0-9963-a3da60372ed2 | -10.6829 | -54.1475 | 2026-09-14 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 305.1 |
| 2db165e6-a445-3454-ac49-3de9aff197f3 | -14.2055 | -47.3813 | 2026-09-14 07:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e3d72a63-4d07-3eb5-9a29-716efb2032fe | -2.88 | -50.4 | 2026-09-14 07:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e558100a-2399-33b8-9815-fbb698b1b219 | -10.66 | -54.12 | 2026-09-14 07:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 020b36eb-fad0-3ec4-9aa6-69486ba6fa0e | -2.88 | -50.45 | 2026-09-14 07:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d24bc319-41c6-3d98-9e7a-bceefd694606 | -2.91 | -50.45 | 2026-09-14 07:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75746cc7-dee6-3287-8bef-ebac097e148a | -2.91 | -50.4 | 2026-09-14 07:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4738d65-66e2-392a-a6f6-0ddd081e3520 | -10.6827 | -54.1679 | 2026-09-14 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 0379c2f3-cae0-3f0c-8c5a-4617b8e04f9a | -14.2055 | -47.3813 | 2026-09-14 07:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 116.2 |
| a921a370-50d6-3987-9e4c-1b8fdb004316 | -14.1861 | -47.3844 | 2026-09-14 07:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 28113756-9234-3df7-b329-4bb5d0e3c77d | -10.6638 | -54.1696 | 2026-09-14 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 66b56aaf-cd7f-357a-91de-8a7b0a0a6fa0 | -10.6641 | -54.1491 | 2026-09-14 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 266.0 |
| 4079961f-7a05-3b71-9046-82f0c43e1cc9 | -10.6829 | -54.1475 | 2026-09-14 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 255.9 |
| 7503ac10-8d25-3b20-a8f7-aab97154f8d2 | -9.4328 | -50.1086 | 2026-09-14 07:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ca5648c9-ca4d-3443-9fbe-2a3e3ab41db7 | -10.6643 | -54.1286 | 2026-09-14 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 93c0006f-36a0-3a04-83ba-655941af11b7 | -10.6832 | -54.127 | 2026-09-14 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 91e20589-0c46-337b-9d95-51349a5b8fa8 | -2.70892 | -57.61692 | 2026-09-14 07:29:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2d600f1e-4cb8-34f1-ac17-8003fbc487ed | -2.66897 | -57.56881 | 2026-09-14 07:29:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fc2fd497-3f05-3ce2-9f9d-821bc5bce2c1 | -5.1208 | -55.94938 | 2026-09-14 07:29:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 77531ce2-1a98-3bc2-b3ef-636f49b13c07 | -2.92636 | -50.39272 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| ba0f427c-1b85-3271-a7e7-d45ce7c13e3b | -2.8855 | -50.43049 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| f8457fd1-535d-37e1-b56e-90403a5705ad | -4.126 | -60.6847 | 2026-09-14 07:29:00 | AQUA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 34969f3b-f9bc-31fb-9ccd-894aa3cd7dc8 | -5.11929 | -55.95961 | 2026-09-14 07:29:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 69aad697-062f-3145-a71b-418b448a610e | -4.13446 | -54.0144 | 2026-09-14 07:29:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8e62e112-8d33-3830-8678-767293586b2b | -2.91673 | -50.41061 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 459.8 |
| b3a797cb-e295-3a17-8daa-c57d632fc4ab | -2.90633 | -50.38467 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| cd30dc99-5032-37e0-96d5-039d93d55191 | -2.67772 | -57.5701 | 2026-09-14 07:29:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 5004e5e7-ad7a-3d28-ab35-845dba9eb1c2 | -2.65936 | -57.51398 | 2026-09-14 07:29:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b72e0337-1b10-3315-9102-93f1ae221fa7 | -2.90284 | -50.40863 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 478.6 |
| f4d531fb-47b4-31e2-ab01-08c01bd1d980 | -6.29556 | -55.27924 | 2026-09-14 07:29:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ca15f0d2-bb8c-3ac0-bf18-b327310c42f8 | -3.72447 | -61.7433 | 2026-09-14 07:29:00 | AQUA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1e203acb-7d7e-388c-b5a7-d9c00eafb397 | -5.13017 | -55.95092 | 2026-09-14 07:29:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ec2f75e4-58c5-3aec-8d64-ffa190a00e9e | -2.92302 | -50.41663 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 921250c3-07c9-3c1e-a2a6-99e584466fff | -3.41321 | -58.20639 | 2026-09-14 07:29:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d3db1d4b-c340-339e-8536-179d096b6869 | -3.40445 | -58.2051 | 2026-09-14 07:29:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e0303ba9-ec5e-3ce2-b9d4-37cdddafe2ea | -2.92024 | -50.3867 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 7ed426f4-a16b-306f-b8a0-fc73f0eeeae7 | -4.11809 | -60.67284 | 2026-09-14 07:29:00 | AQUA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e0f9debc-33fc-3427-b19a-638716817689 | -2.66067 | -57.50527 | 2026-09-14 07:29:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ef771916-52fe-3565-879a-86dde66f7fe5 | -2.61007 | -54.75085 | 2026-09-14 07:29:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| bde0ead8-8a85-3f2a-af96-51f286e2e583 | -2.66416 | -57.5414 | 2026-09-14 07:29:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d49e3e2c-663c-38c9-bd71-75ac275ff681 | -6.11177 | -57.68134 | 2026-09-14 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 331640dd-0228-3c41-be82-f3a275a9373c | -2.88895 | -50.40664 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| fa8ec4fc-b5a4-3d79-b512-814a6e048ff7 | -3.59727 | -59.07172 | 2026-09-14 07:29:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 25d7a542-6fec-33ca-bf24-276da9357b9c | -4.11647 | -60.68326 | 2026-09-14 07:29:00 | AQUA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 90b7a6c9-30e9-33f2-b073-161e17cc39a6 | -3.59866 | -59.06272 | 2026-09-14 07:29:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 80f01295-58d4-3303-9f77-7bdfa010eba8 | -2.70051 | -57.53783 | 2026-09-14 07:29:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| f79ac785-446b-3831-9154-f5a28acd81ce | -6.13696 | -57.69414 | 2026-09-14 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 84a22458-93df-3813-90fd-914591805646 | -5.07665 | -56.24805 | 2026-09-14 07:29:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 12183b55-ee8f-3c97-ad5b-be1f348a8ca6 | -2.90913 | -50.41465 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 526.4 |
| 69fa002e-98b6-3ff1-be4f-02ba1fb82dd0 | -3.73477 | -61.74485 | 2026-09-14 07:29:00 | AQUA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 79af80ac-1ad1-3611-91bc-96d8b4a8d4ac | -2.91244 | -50.39073 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| a6ddaf2a-2d4b-3b31-9bc7-a0d0fbc5236d | -2.66548 | -57.53269 | 2026-09-14 07:29:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cc96f021-431f-31b6-bbf0-bf2b390ca69a | -3.16977 | -58.65149 | 2026-09-14 07:29:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 98d8a769-2048-329b-b758-ed2abb3bc6ce | -2.89937 | -50.43239 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 425.6 |
| 4c77b345-f131-3004-b3ff-1ba11190bc84 | -6.28559 | -55.27782 | 2026-09-14 07:29:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f32966d7-7629-3ed0-9644-8b1bd47741f8 | -2.65804 | -57.52269 | 2026-09-14 07:29:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ee7cdf38-6355-35cd-b68b-146c8f2567d8 | -3.17112 | -58.64264 | 2026-09-14 07:29:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9ef63525-f872-3cf4-8845-e2bbac64d026 | -6.01743 | -59.93878 | 2026-09-14 07:29:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a80e93d8-6bc0-388f-9191-a05c799d62e0 | -3.72679 | -61.74936 | 2026-09-14 07:29:00 | AQUA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 28fa066e-aaaf-3bb6-8b81-4f49570697ad | -2.67028 | -57.5601 | 2026-09-14 07:29:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| be785050-434f-3925-b5dc-9173889f84f9 | -6.11309 | -57.67242 | 2026-09-14 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 8269db55-4070-36b6-aeb6-bdd7c3b96e70 | -2.69919 | -57.54654 | 2026-09-14 07:29:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| de9a3f96-02d7-3903-bb08-69b991ea442f | -2.6716 | -57.55139 | 2026-09-14 07:29:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b690a33a-a01f-3616-b2dd-ee77f73fc6fd | -4.39005 | -55.19886 | 2026-09-14 07:29:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 74041eff-75a2-30e0-b17f-e95b478d12f6 | -6.01601 | -59.94806 | 2026-09-14 07:29:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| efa91227-3ddb-3878-865a-80c67b3ec98f | -2.90584 | -50.43841 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 203.5 |
| 2735d057-df73-3ca1-a37a-416559e80aa2 | -3.17604 | -61.11344 | 2026-09-14 07:29:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4f040adf-58c0-3cf8-9b41-a3c2709cdcde | -6.07304 | -57.86052 | 2026-09-14 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8dce169a-5a8c-374b-9a7b-8d3ed764a7ba | -3.1623 | -58.64133 | 2026-09-14 07:29:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 1c81de0d-7adb-327a-a15e-48e6408dd350 | -4.12761 | -60.67428 | 2026-09-14 07:29:00 | AQUA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 86663406-82b6-3f76-8f7d-6084b5a2768d | -6.10252 | -57.66502 | 2026-09-14 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4eea6351-8786-3e23-a04a-6849e890e4dd | -2.91969 | -50.44043 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 2144f87a-e584-3871-af03-b8e80d167514 | -2.91324 | -50.43432 | 2026-09-14 07:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 278.3 |
| 99a871da-e4a8-32bc-934e-7fc5de152b09 | -5.59094 | -60.18559 | 2026-09-14 07:29:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ef3b807a-149e-3af0-8c8b-3601d71db27e | -10.6643 | -54.1286 | 2026-09-14 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 3c2dff54-c570-3295-9951-93895886328c | -10.6832 | -54.127 | 2026-09-14 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 0de8c2fc-ac71-3578-8dc5-d4a234b2a4e0 | -10.6827 | -54.1679 | 2026-09-14 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.2 |
| f47eae11-a658-383f-a141-831fd6830c10 | -4.115 | -60.6886 | 2026-09-14 07:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0f91657b-a664-322e-ad5f-d4368adfb6bd | -10.6638 | -54.1696 | 2026-09-14 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 89fd0bf0-1840-3040-8ee4-b3342553c82a | -10.6641 | -54.1491 | 2026-09-14 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 214.0 |
| 526a9294-9bb1-38e6-aa84-7de54bb6d42e | -10.6829 | -54.1475 | 2026-09-14 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 281.0 |
| fd5cd72c-e596-36c9-94c6-cd14d252215b | -10.67093 | -54.12673 | 2026-09-14 07:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |


[Clique aqui para ver as próximas entradas](README64.md)
