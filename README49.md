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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d266523e-ecc7-32d6-89fb-cdd8d358277d | -10.09522 | -68.37638 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b02dfc34-3df0-3488-af8b-b31ff9caa8bf | -10.09461 | -68.3784 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cef98f4a-f54d-3970-a728-dae60a4ae763 | -10.09436 | -68.38111 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abc09f2d-5c93-3365-8875-d41961b107a7 | -10.09087 | -68.37287 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a204918-2ddb-3b33-8fe7-59360132a3a1 | -10.09004 | -68.37761 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1d51148-c3e7-3d33-885f-69583f9014e7 | -10.09708 | -68.36423 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bee23e22-73e7-3816-94a5-76162a238e0d | -10.09543 | -68.37367 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0308ba6e-fa42-367e-8cdb-df0c4ed6f6da | -10.08131 | -68.29369 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71c70c04-48d2-36ec-80a6-48b1876122b4 | -4.91151 | -47.04013 | 2024-11-01 05:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ed3001da-a260-3578-ab17-d80c501d1691 | -4.91094 | -47.04112 | 2024-11-01 05:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a0172d5d-e7db-304c-a2ad-84ae876f9d89 | -4.91068 | -47.04626 | 2024-11-01 05:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e82a6dec-d6f2-3460-9d73-88b3330d5af1 | -4.91008 | -47.04723 | 2024-11-01 05:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b5ec6e7e-1b34-378b-b8e2-f9192803155c | -6.64808 | -47.86755 | 2024-11-01 05:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4176f297-8650-3029-85bb-2c139d156ce3 | -6.64727 | -47.87368 | 2024-11-01 05:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4a97c23f-a18c-39b5-8dfe-8f0c15cf6645 | -6.60455 | -47.39048 | 2024-11-01 05:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 00952a01-b2f4-37c7-a61f-741fc8bbe622 | -6.60371 | -47.39694 | 2024-11-01 05:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d3f42607-6e13-3646-8ac2-7051fedec70e | -5.04409 | -47.97491 | 2024-11-01 05:25:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a32add3b-3317-3ad3-92fd-b6112c7a864f | -4.89878 | -48.06837 | 2024-11-01 05:25:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6f72c7be-454f-3184-8e3d-486980ebb268 | -4.89812 | -48.07321 | 2024-11-01 05:25:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5921aed8-d7fc-3a29-976a-6f814432d824 | -4.7764 | -47.8444 | 2024-11-01 05:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b6c1d3f-e341-326c-8744-094d165ad739 | -6.39166 | -49.56744 | 2024-11-01 05:25:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 48b240f2-6025-32e3-9774-854ddbdd711d | -6.39104 | -49.57209 | 2024-11-01 05:25:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3e0bd9ab-8c38-3fcd-8ea4-63475a6ef007 | -6.39043 | -49.57669 | 2024-11-01 05:25:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0735aabb-9ae2-36d9-9986-bb9eb39efa7a | -6.38502 | -49.57138 | 2024-11-01 05:25:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ea424eae-d096-3b15-90a0-8adc3e2b3e94 | -6.38441 | -49.576 | 2024-11-01 05:25:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1757f76f-5b6a-3159-83dc-6d729056bb4e | -4.96489 | -49.77866 | 2024-11-01 05:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4927557-a5f4-3a91-86e2-27e17c6500e0 | -16.55651 | -56.23618 | 2024-11-01 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 46dd5808-83bd-3c8e-b47a-546da62dbb51 | -16.55597 | -56.24068 | 2024-11-01 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c7575c3f-6197-372c-8544-61863c582f7a | -16.55209 | -56.23556 | 2024-11-01 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b4323a08-ec24-3ce5-83ca-12d88104e0eb | -16.55154 | -56.24006 | 2024-11-01 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 947c4575-dbcf-3d18-ac7c-c6fe6dbb39ba | -4.01568 | -54.82249 | 2024-11-01 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2996501a-2af8-353e-b0ae-81d2b0f66887 | -10.37601 | -56.35741 | 2024-11-01 05:25:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44f92fa5-2974-34be-b5e3-4017d5d612be | -12.78279 | -57.03913 | 2024-11-01 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7db2b80d-bd1a-3671-9d31-06ded43913f0 | -12.78126 | -57.0375 | 2024-11-01 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb34dba5-1126-39b5-9e8f-e00984cd7ca4 | -12.78078 | -57.04108 | 2024-11-01 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8fc8a31-be40-3d1d-8356-94e4faef086f | -12.77881 | -57.03852 | 2024-11-01 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8baefde-cd39-3286-801d-7d39947681c6 | -12.77728 | -57.03691 | 2024-11-01 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2532d08-28b6-3c73-bfc7-8c0e9d10cfad | -16.42473 | -57.20328 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d4a8a587-cb5a-3cf0-9fe4-896d47853c35 | -16.17116 | -56.78626 | 2024-11-01 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1731992-6354-3fdc-b796-a8dc3220e3eb | -16.16844 | -56.77341 | 2024-11-01 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47efb0c3-654a-386e-99b2-817f3d4772a7 | -15.62795 | -57.50846 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 645f1aa8-a9ff-34a5-9f84-541140497b18 | -15.62694 | -57.50555 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4f9fb59-262f-3359-a97c-6f082b7d94d8 | -15.62645 | -57.50923 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0baa75d-0e5c-301c-91af-fc2e53c09300 | -16.91159 | -57.51861 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8c49adaa-ea82-3abe-80cb-ab0f99131365 | -16.91109 | -57.52239 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b6156865-765b-30a4-b490-04cfb2c6b883 | -16.91059 | -57.52616 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 00e88610-108d-343d-b249-4c78147f556b | -16.9101 | -57.52993 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 6abdbc3c-3ad6-3528-be11-947523cdc1ac | -16.908 | -57.51426 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 04187912-3c39-39a4-97ca-571f6f929d5a | -16.9075 | -57.51803 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| aefdb4c0-a86f-3412-ad6c-5f494aa94e76 | -16.907 | -57.52181 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f104b89f-d9eb-3e26-81f6-6121ed24f797 | -16.90651 | -57.52557 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| c2dbd2e2-57ab-3649-95ed-ebeb8243f2f6 | -16.90391 | -57.51368 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0ae39093-21e7-3258-b9ee-19e936e223e5 | -16.90341 | -57.51745 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7554d068-5789-3287-b6c7-329c113dca65 | -16.90292 | -57.52122 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d03ca66f-a3d6-320b-922c-06a32b45ee11 | -16.90031 | -57.50931 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3dfd1da0-0edc-3422-858c-3fe71c0d215b | -16.89932 | -57.51686 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b49080d7-9aa9-3b36-8bcd-0454de373652 | -16.63129 | -57.82084 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 72e4ecd4-7950-3f9b-a0de-9a1859c4186e | -9.3393 | -59.33278 | 2024-11-01 05:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 182ebcf2-06e8-3572-8b91-c735caf6d2b7 | -13.10948 | -60.39014 | 2024-11-01 05:25:00 | NOAA-21 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ceecaecd-e6e3-3b44-8b55-908eaa3f73e0 | -14.23805 | -60.173 | 2024-11-01 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be24e27f-b5d7-36be-bad7-4268e647c5e0 | -14.15249 | -60.2073 | 2024-11-01 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75109c60-b4b6-37c1-958c-881b4b027954 | -13.81791 | -60.26672 | 2024-11-01 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adcfc42b-3d1d-3d98-ad22-719fe494f887 | -13.81449 | -60.26619 | 2024-11-01 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8a1ba4f-9069-3dde-a7eb-ab2463a04d74 | -15.25861 | -60.09096 | 2024-11-01 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9820631b-3d64-36c7-a64c-d4c0871dddee | -15.43813 | -60.24995 | 2024-11-01 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 632cd755-d192-3b57-b369-cb70206262b7 | -15.43755 | -60.25388 | 2024-11-01 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd768363-42c6-3f58-80d3-0940c220dd23 | -3.28545 | -61.22514 | 2024-11-01 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4a838c1-65ca-30a3-83e3-b94cb3e2eb75 | -2.86435 | -60.87257 | 2024-11-01 05:25:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68685134-77a7-3322-a2f2-562b92ce0eb4 | -12.88862 | -62.12239 | 2024-11-01 05:25:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00685ff9-5da1-3b72-84b9-b4b45f6c5488 | -3.08868 | -61.71568 | 2024-11-01 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d0bc4af-3a82-3006-b30a-99749cbc92cf | -3.08927 | -61.71198 | 2024-11-01 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a9a8abb0-c958-34f6-bc5b-2662b0f59c8d | -8.85416 | -64.16099 | 2024-11-01 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a160134e-73a8-3409-bb0d-07e355852046 | -8.8499 | -64.16454 | 2024-11-01 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d8da5e4-e8f3-3c6d-b184-ff7d01f6323a | -9.70162 | -64.19273 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00134a93-6a9c-3e8b-8b35-e1804aeb0975 | -9.2744 | -64.3326 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d61d8d2-7937-3a4d-bf3f-3d8224267334 | -8.83013 | -64.19543 | 2024-11-01 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d490b8e-24b3-3de4-b022-27ebbebea9a5 | -9.27263 | -64.33344 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c295c8e0-fa89-39a0-887d-1961e464335e | -9.91949 | -64.80914 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e0b8138-5e27-3fa4-87bf-5508aca57284 | -9.91512 | -64.8129 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5fa095a1-1810-306f-9faa-26cb57ccdfbf | -9.91367 | -64.82159 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 911d993d-4dab-3b1b-bc89-c35a137f21f4 | -9.9129 | -64.80356 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 74e6dd2b-63d2-3f3a-93c7-964946d8508b | -9.90924 | -64.80296 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94e92351-ed79-30d6-b7e2-220ee485da9e | -9.90852 | -64.8073 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f1143c5-4036-3847-ad72-3286f973b714 | -10.68108 | -64.99488 | 2024-11-01 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94d4b5ce-ef0f-3fc4-ba2b-df0e694787cc | -10.67814 | -64.98988 | 2024-11-01 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 777ed95d-78de-376e-b3d1-af5ea424e5d0 | -10.12751 | -65.08846 | 2024-11-01 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3e68afe-4121-3534-bff0-64f8a2d5a0d8 | -10.12504 | -65.08916 | 2024-11-01 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38963c78-1473-39e5-95d6-6180d783c474 | -9.92022 | -64.80478 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e22b0878-26a8-346a-ae2f-a8601c8eb571 | -9.91877 | -64.81351 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35032d74-b009-3734-a181-4dd6555e6710 | -9.91805 | -64.81786 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5638567-9bd4-3857-aa75-145b2656348c | -9.91656 | -64.80417 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9ded1953-56b1-356e-b084-638542aa2b1d | -9.91584 | -64.80853 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e758ea5b-81b8-3f0f-bc5e-4bbee9a62bde | -9.91439 | -64.81724 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5d6dc8ec-02a1-30a3-a088-11e900aee361 | -9.91218 | -64.80791 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 83cd00e3-3363-3968-90f4-0747b4d036c6 | -9.91146 | -64.81227 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1fe7e82d-6e50-3439-a9f1-d437e89ac4e1 | -9.91073 | -64.81663 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bb3d2f42-fcd5-3955-b5ea-3a4610c76f8d | -8.62473 | -69.71755 | 2024-11-01 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c177e40-1130-3153-8519-bccd89a227f0 | -8.62418 | -69.72064 | 2024-11-01 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b215aad-53e8-3db0-b297-f8d410953523 | -8.62361 | -69.72377 | 2024-11-01 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26ca8a01-dc6a-3b08-8f23-8fda351c0cd9 | -7.90575 | -72.33513 | 2024-11-01 05:25:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README50.md)
