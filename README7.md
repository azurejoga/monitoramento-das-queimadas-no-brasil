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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10a736e1-2be6-3faa-bc7c-e975b4903ae1 | -4.15892 | -43.35226 | 2024-10-20 00:24:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f1beae59-6925-3e4d-a292-c017d0f444d5 | -4.13153 | -43.08605 | 2024-10-20 00:24:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 21d20347-efd1-3120-b8d1-9438c981ec48 | -4.12214 | -43.08735 | 2024-10-20 00:24:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 662d86e8-42e4-3886-aa8c-dfa94f17031e | -3.88234 | -40.95908 | 2024-10-20 00:24:00 | TERRA_M-M | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1212c310-f7ee-3f12-823c-ba836ce8fb79 | -3.86467 | -40.63871 | 2024-10-20 00:24:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 8f2f5127-d9ca-3782-85b0-7c3e6640336c | -3.78913 | -42.48442 | 2024-10-20 00:24:00 | TERRA_M-M | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| afc3275d-90c3-3704-8d93-65f9339e4b45 | -3.67871 | -43.70647 | 2024-10-20 00:24:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| dc8f8b69-502c-3bb3-9277-cd841a89d602 | -3.67727 | -43.69579 | 2024-10-20 00:24:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| e23d63d3-15b3-3cf3-b35f-b7f88b98e003 | -3.53012 | -42.20836 | 2024-10-20 00:24:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 392524ec-3d12-30f1-ba04-43c8ce53c334 | -3.52089 | -43.61058 | 2024-10-20 00:24:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a8552956-df23-3f29-9628-ad630d91b82c | -2.2199 | -50.4594 | 2024-10-20 00:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| c1bcf89b-e9e8-3f70-aa06-175c22db8008 | -2.2808 | -48.5941 | 2024-10-20 00:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 5fac6662-f703-3afe-abac-3a8657cce6c7 | -2.2993 | -48.5936 | 2024-10-20 00:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 204.2 |
| 7cdf3a2b-aa58-3427-800c-f81caa85a460 | -2.2994 | -48.5722 | 2024-10-20 00:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 79960121-a365-37f9-846d-62db7364a817 | -2.3178 | -48.5932 | 2024-10-20 00:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d2aecd16-01d7-3d17-af51-d1f6c7539765 | -2.7773 | -49.3067 | 2024-10-20 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 180.0 |
| f2021108-8f8b-3d0b-a0eb-2a1d75605d4d | -2.7774 | -49.2854 | 2024-10-20 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 852d36a4-815a-31d1-b3bd-71e951f8370c | -2.7958 | -49.3062 | 2024-10-20 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 2a94f614-26b7-31e9-8d2c-ba22696e9ad6 | -2.7959 | -49.2849 | 2024-10-20 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b9afbcc0-f102-333a-b0d6-9fcd7df73262 | -3.0478 | -51.0226 | 2024-10-20 00:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 16157352-92fc-377f-a7d0-a9477d4a839e | -3.1278 | -54.3662 | 2024-10-20 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| c65387f5-bfa2-3a93-8ca9-3e5bb019b727 | -3.1462 | -54.3658 | 2024-10-20 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 32903274-3ced-3ee9-b5cd-e9beafedeaba | -3.1462 | -54.3457 | 2024-10-20 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| c85489d4-407b-3b86-a7bc-741cf355e89d | -3.3813 | -50.6788 | 2024-10-20 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| c468963a-59e5-3644-a679-b916e8e17db8 | -3.3814 | -50.6579 | 2024-10-20 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| e3c23061-b934-3a04-83b1-74acf432a825 | -3.3997 | -50.6782 | 2024-10-20 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 641f84fc-3833-32af-a58e-504c369550b6 | -3.3998 | -50.6573 | 2024-10-20 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 69e5c872-c3f1-3a4f-b3a2-b030e7830d23 | -3.586 | -54.6941 | 2024-10-20 00:25:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b3b5d80a-fd1d-337d-8979-690e6e72a6e9 | -3.5861 | -54.6741 | 2024-10-20 00:25:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| afa9ce99-ea13-3048-9d8e-5f1b691c3090 | -3.6045 | -54.6736 | 2024-10-20 00:25:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a66ff9c5-e3ab-3c89-8c80-19366790b8fe | -3.815 | -48.866 | 2024-10-20 00:25:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| a55ebb1e-2cb5-30af-b0e9-f7d19a1a4e67 | -3.833 | -48.9722 | 2024-10-20 00:25:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| dbd3339c-f40e-32ea-920d-af9a288d5321 | -3.8331 | -48.9508 | 2024-10-20 00:25:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 859b0955-3122-3fe7-b0f3-f10fccd40f61 | -3.8334 | -48.8866 | 2024-10-20 00:25:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 38e72dac-11af-330e-ba6a-f21c69db20da | -3.8686 | -45.8254 | 2024-10-20 00:25:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 36b23775-0b32-33f7-9324-42b005add07d | -3.9018 | -49.9884 | 2024-10-20 00:25:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| d8cf75bc-1a43-3f43-a3c3-7f7a7796125b | -4.1985 | -46.6318 | 2024-10-20 00:25:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 9ba8231e-1cdc-3d43-ab89-d8cac030eb02 | -4.4899 | -44.7564 | 2024-10-20 00:25:31 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 2db511d1-e79e-378f-9318-2ddcad8536c8 | -4.8925 | -45.8162 | 2024-10-20 00:25:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 6d0081e2-3ae5-36e4-8ade-6dd8d015959a | -4.911 | -45.8374 | 2024-10-20 00:25:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 690f57ca-f228-3485-96ba-67c2a9c3062c | -4.9112 | -45.8151 | 2024-10-20 00:25:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 417dcbee-2cb0-38fe-aa7f-9044bc3dc6fb | -5.2072 | -46.11 | 2024-10-20 00:25:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 6acbcae8-c067-3e1f-a289-cc0a2cbb87db | -5.2073 | -46.0876 | 2024-10-20 00:25:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 51d67801-6727-326c-bef2-3198e14bdc56 | -5.509 | -50.5872 | 2024-10-20 00:25:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 27f83ce4-811a-33de-9052-08cc5abbd735 | -7.3638 | -72.8628 | 2024-10-20 00:25:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 38fcef08-2b14-32f3-9212-48380122e6c9 | -1.4745 | -48.98481 | 2024-10-20 00:26:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 251351eb-56bb-34a7-b1fb-9da00bf5e2ae | -1.46456 | -48.97976 | 2024-10-20 00:26:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 9137e700-2583-3ee5-b49e-79a7307f442d | -1.05633 | -48.27292 | 2024-10-20 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 83273b4a-15c1-38ab-8eac-1fe971cb09cb | -1.01839 | -48.85211 | 2024-10-20 00:26:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 65194bc0-2f35-3885-a28d-4b92b59e2965 | -12.5147 | -63.3014 | 2024-10-20 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d2df9a19-4032-3b48-a18b-e48bc5e7d2ff | -17.5737 | -40.23 | 2024-10-20 00:26:43 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 92.4 |
| cf7c0053-337b-3647-a57c-ba2f8b174137 | -17.5939 | -40.2245 | 2024-10-20 00:26:43 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 335.0 |
| 759e8ad1-df44-37ae-90c1-ba6fceb04da0 | -17.5947 | -40.1985 | 2024-10-20 00:26:43 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 128.8 |
| 53f680f1-b4d9-3512-afd7-a5dd59e16caf | -2.2015 | -50.4598 | 2024-10-20 00:35:18 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d1378f12-2c38-3581-9f7b-016ef3dd2cf0 | -2.2808 | -48.5941 | 2024-10-20 00:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 274555c5-2932-3824-b0d9-4ac37d9b9c7e | -2.2993 | -48.5936 | 2024-10-20 00:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 2ab10d9f-b32e-3dd1-a493-80e2cfabe27b | -2.2994 | -48.5722 | 2024-10-20 00:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 1b860f3f-1080-3997-8a30-7e47ad6c859d | -2.3178 | -48.5932 | 2024-10-20 00:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b23a4e53-5362-3546-9043-45e78ded411d | -2.7585 | -49.4134 | 2024-10-20 00:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b3be1cff-e12d-3327-892e-4e8f5ece9bd7 | -2.7773 | -49.3067 | 2024-10-20 00:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 195.3 |
| 28e99340-7b8b-32e3-9fc2-9884abc663f1 | -2.7774 | -49.2854 | 2024-10-20 00:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 2c84db42-fe0a-3f92-bb03-b5603e58e9df | -2.7958 | -49.3062 | 2024-10-20 00:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 4f052f6a-17e2-3bbe-8779-1b648fc4c151 | -2.7959 | -49.2849 | 2024-10-20 00:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 0a2f4a62-85ab-30bd-83f4-b0b067eba91e | -3.0478 | -51.0226 | 2024-10-20 00:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ad71a844-7340-3e22-ba3c-0cd81186c512 | -3.1278 | -54.3662 | 2024-10-20 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ef48c16e-91c5-31b0-92f2-f7e1064c0332 | -3.1462 | -54.3658 | 2024-10-20 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| b1c22ba6-6a70-3a0b-9576-e346c2b268a2 | -3.1462 | -54.3457 | 2024-10-20 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 00b9c4b6-8d49-3e88-8862-b57be623c2c2 | -3.3813 | -50.6788 | 2024-10-20 00:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 3d883272-1dca-3872-b7f0-7091fb510bc4 | -3.3814 | -50.6579 | 2024-10-20 00:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 7170f8d5-b617-30a9-bb06-7f2cb1a4893d | -3.3997 | -50.6782 | 2024-10-20 00:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 54ecb2cc-8d7e-3f41-aa0a-b340596d2918 | -3.3998 | -50.6573 | 2024-10-20 00:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| a40a3a8b-328b-32fa-8c70-67c346e8887e | -3.815 | -48.866 | 2024-10-20 00:35:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5599c788-4ab2-3a0e-8159-03de3951e89c | -3.833 | -48.9722 | 2024-10-20 00:35:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 6788f152-bb65-3ce4-a325-809a52c338ee | -3.8334 | -48.8866 | 2024-10-20 00:35:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7ae5d8f0-620a-3096-b61d-988984e9aaa0 | -3.8686 | -45.8254 | 2024-10-20 00:35:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| bd2801a3-6ae2-3153-86ee-6ccf16d9eb6e | -3.9018 | -49.9884 | 2024-10-20 00:35:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| c9c3351b-035f-3250-b903-58349ee9846e | -4.1985 | -46.6318 | 2024-10-20 00:35:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 8522f989-ff60-3acb-b438-2e4c73cac590 | -4.3354 | -48.5647 | 2024-10-20 00:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 1ed8d219-8a05-3f80-80fe-b5cb4e13c550 | -4.4899 | -44.7564 | 2024-10-20 00:35:31 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 5ceaab1c-bfe1-34a2-b18d-ae4921e00e05 | -4.911 | -45.8374 | 2024-10-20 00:35:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 70e6dd94-3f8e-34ac-a86b-540aec70f696 | -4.9112 | -45.8151 | 2024-10-20 00:35:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 22ee3aab-567f-3456-b0d2-946e5ee8de67 | -5.2258 | -46.1088 | 2024-10-20 00:35:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 40876c48-d1ef-334d-b999-bb596dc3d37e | -5.226 | -46.0865 | 2024-10-20 00:35:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 001818cd-ed2f-3fd4-bc79-dc0a027efdc3 | -5.3873 | -46.9191 | 2024-10-20 00:35:36 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 8a3fe083-92da-3322-80e7-67528e7b50cd | -5.3875 | -46.897 | 2024-10-20 00:35:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 709dcf48-fbcb-3fbb-a1de-b1521c9d40e1 | -5.509 | -50.5872 | 2024-10-20 00:35:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 59c8a0ad-4610-33b8-a2db-77e5711f486a | -5.4059 | -46.9179 | 2024-10-20 00:35:37 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 131.2 |
| d45b1973-deb2-33d1-8124-5cb4ef4e3eb4 | -5.4061 | -46.8959 | 2024-10-20 00:35:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 90b4390d-fc79-3b83-8c29-56d0c2f9c386 | -5.4476 | -46.362 | 2024-10-20 00:35:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| be664142-59fd-388d-9d81-cec28ecb3be4 | -5.4477 | -46.3397 | 2024-10-20 00:35:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 0e2fd4a8-b8ff-3c6f-a725-3043a3692f00 | -7.3638 | -72.8628 | 2024-10-20 00:35:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 2c54475c-adea-3c76-beea-970aba686d85 | -7.6815 | -47.3213 | 2024-10-20 00:35:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 09a49a5a-341d-3185-b9ce-259c5cc40e6a | -7.7679 | -73.079 | 2024-10-20 00:35:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 74.7 |
| ac6e3a14-c3a7-3cb0-a3dd-e39282a51706 | -12.4967 | -63.1874 | 2024-10-20 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f15ec08d-fb8f-3549-9cdc-cf465754a074 | -12.5147 | -63.3014 | 2024-10-20 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 48830e4a-bb85-35f4-9ef1-385105ffe316 | -1.165 | -53.6571 | 2024-10-20 00:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| c43edb51-01a7-3e83-af16-e6a1331686f6 | -2.2808 | -48.5941 | 2024-10-20 00:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| c645afe3-5cd8-332c-b34c-0942df757d75 | -2.2993 | -48.5936 | 2024-10-20 00:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| d007b8c4-25fe-3b05-9f2a-3d6eb0b343ca | -2.2994 | -48.5722 | 2024-10-20 00:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b5c73071-0553-3a2c-a7da-8f5438f1d477 | -2.3178 | -48.5932 | 2024-10-20 00:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |


[Clique aqui para ver as próximas entradas](README8.md)
